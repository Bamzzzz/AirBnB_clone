#!/usr/bin/python3
"""Explains the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity

    Attributes:
        name (str): amenity name
    """

    name = ""
