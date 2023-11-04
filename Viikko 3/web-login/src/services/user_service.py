from entities.user import User
import re
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):

        if not username or not password:
            raise UserInputError("Username and password are required")
        elif  len(password) <=7:
            raise UserInputError("password too short")
        elif password!=password_confirmation:
             raise UserInputError("password and password confirmation do not match")
        elif  re.search('[a-z]+$', password):
            raise UserInputError("Insufficient password")
        elif self._user_repository.find_by_username(username):
            raise UserInputError("name already taken")
        elif len(username)<3:
            raise UserInputError("name must be atleast 3 chr")
        elif not re.search('[a-z]+$', username):
            raise UserInputError("username can only contain alphabets")


user_service = UserService()
