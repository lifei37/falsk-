# coding: utf-8
"""
权限认证
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
验证token的装饰器
"""
import time
from functools import wraps

from flask import current_app, g, request

from . import cache
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from src.config import Config


# token名称
TOKEN_NAME = "token"
# token缓存前缀
TOKEN_PREFIX = "user_token_"
# token缓存时间
TOKEN_LIFETIME = 7 * 24 * 60 * 60


class TokenErr(Exception):
    def __init__(self, name, desc="", **kwargs):
        self.name = name
        self.desc = desc
        self.kwargs = kwargs


def create_token(user_id, expiration=TOKEN_LIFETIME):
    '''
    token是一个加密过的字典，里面包含了用户的id和默认为10分钟(600秒)的过期时间。
    :param expiration: 过期时间
    :return: token
    '''
    s = Serializer(Config.SECRET_KEY, expires_in=expiration)
    return s.dumps({'user_id': user_id})


def clear_token(user_id):
    """
    清除token
    :param user_id: 缓存token的用户标识
    """
    pass


def need_token(func):
    """校验token合法性"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        token_id = current_app.config.get("TOKEN_NAME", TOKEN_NAME)
        token = request.headers.get(token_id) or request.data.get(token_id) \
            if isinstance(request.data, dict) else None
        if token is None:
            raise TokenErr("TOKEN_NOT_FOUND", "缺少登录凭证")
        # 解析token
        try:
            s = Serializer(Config.SECRET_KEY)
            data = s.loads(token)
        except Exception:
            raise TokenErr("TOKEN_ERROR", "非法的登录凭证")

        g.user_id = data['user_id']

        return func(*args, **kwargs)
    return wrapper
