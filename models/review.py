#!/usr/bin/python3
"""
Test for the Place class
"""


from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Public class attributes:
        place_id (str): The ID of the place associated with the review (empty string by default).
        user_id (str): The ID of the user associated with the review (empty string by default).
        text (str): The text content of the review (empty string by default).
    """
    place_id = ''
    user_id = ''
    text = ''
