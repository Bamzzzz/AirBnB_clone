#!/usr/bin/python3
"""
Define amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define the amenities that user will choose to enjoy from at the offer of his place"""
    name = ""
