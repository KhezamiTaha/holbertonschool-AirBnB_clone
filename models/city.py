#!/usr/bin/python3
"""
Test for the City class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Public class attributes:
        state_id (str): The ID of the state associated with the city (empty string by default).
        name (str): The name of the city (empty string by default).
    """
    state_id = ''
    name = ''
