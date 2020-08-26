from app import db
from src.api import api
from flask_restful import Api, Resource, reqparse
from src.response import api_return
from src.auth import need_token

user = Api(api)


class UserApi(Resource):
    """
    用户模块
    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user_name', type=str, required=False)
        self.parser.add_argument('password', type=str, required=False)
        self.params = self.parser.parse_args()

    @need_token
    def get(self):
        print(1)
        return api_return("OK")


user.add_resource(UserApi, '/user/login', endpoint='user_login')


