#!/usr/bin/python3
"""
Define review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review made by users about the place"""
    place_id = ""
    user_id = ""
    text = ""
