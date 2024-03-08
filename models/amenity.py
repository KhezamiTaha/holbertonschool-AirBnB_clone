#!/usr/bin/python3
"""
Test for the Amenity class
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Public class attributes:
        name (str): The name
    """
    name = ''
