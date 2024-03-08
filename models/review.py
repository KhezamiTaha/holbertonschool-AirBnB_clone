#!/usr/bin/python3
"""
Test for the Place class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Public class attributes:
        place_id (str): The ID
        user_id (str): The ID of the user associated with
        text (str): The text content
    """
    place_id = ''
    user_id = ''
    text = ''
