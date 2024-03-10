#!/usr/bin/python3
"""Explains the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        last_name (str): last name of the user
        first_name (str): first name of the user
        email (str): email identity of the user
        password (str): the password of the user
    """

    last_name = ""
    first_name = ""
    email = ""
    password = ""
