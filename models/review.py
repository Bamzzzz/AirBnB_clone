#!/usr/bin/python3
"""Explains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): the Place identity
        user_id (str): the User identity
        text (str): the text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
