# coding: utf-8
"""
接口蓝图
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from functools import wraps

from flask import Blueprint, current_app, g

from ..response import api_return
from ..tool import get_error_info
from ..auth import TokenErr, need_token, create_token, clear_token
from ..model.base import AdminUser as UserInfo


api = Blueprint("api", __name__, url_prefix="/api")


@api.errorhandler(TokenErr)
def error_token(error):
    current_app.logger.debug("Token错误：{0}, {1}".format(error.desc, str(error.kwargs)))
    return api_return(error.name, error.desc)


@api.errorhandler(Exception)
def catch_error(error):
    file, line, func, _ = get_error_info()
    current_app.logger.error('代码错误：{0}, {1}({2})[{3}]'.format(str(error), file, line, func))
    return api_return("ERR", "服务器内部异常")


def need_login(func):
    """在need_token的基础上验证用户数据，或者可以验证其他访问权限"""
    @wraps(func)
    @need_token
    def wrapper(*args, **kwargs):
        user_id = g.get("user_id")
        if not user_id:
            raise TokenErr("TOKEN_USER_ERROR", "无效的用户")
        user = UserInfo.query.filter_by(id=user_id).first()
        if user is None:
            raise TokenErr("TOKEN_USER_ERROR", "无效的用户", user_id=user_id)
        if user.status != 1:
            raise TokenErr("TOKEN_USER_INVALID", "账号已禁用", user_id=user_id, account=user.account)

        g.user = user

        return func(*args, **kwargs)
    return wrapper


def login_user(user):
    """登录用户，创建并返回token"""
    return create_token(user.id, user.password, g.get("client_info"))


def logout_user():
    """登出用户，清除缓存token"""
    clear_token(g.get("user_id", 0))


# 导入蓝图要加载的接口文件
from . import user
