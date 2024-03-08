#!/usr/bin/python3
"""
Test for the State class
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Public class attributes:
        name (str): The name of the state (empty string by default).
    """
    name = ''
