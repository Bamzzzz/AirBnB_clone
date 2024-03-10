#!/usr/bin/python3
"""
Define city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """define city to look for"""
    state_id = ""
    name = ""
