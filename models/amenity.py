#!/usr/bin/python3
"""This model is the Amenity class for the 
hbnb which holds the amenity objects"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
