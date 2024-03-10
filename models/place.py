#!/usr/bin/python3
"""Explain the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        description (str): the description/location of the place
        number_rooms (int): the numbers of rooms of the place
        number_bathrooms (int): the numbers of bathrooms of the place
        max_guest (int): the maximum number of guests in the place
        price_by_night (int): the price per night of the place
        city_id (str): the City identity
        user_id (str): the User identity
        name (str): the name of the place
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        amenity_ids (list): list of all amenity
    """

    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    city_id = ""
    user_id = ""
    name = ""
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
