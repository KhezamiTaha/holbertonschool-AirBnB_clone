#!/usr/bin/python3
"""
Test for the Place class
"""


from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Public class attributes:
        city_id (str): The ID of the city associated with the place (empty string by default).
        user_id (str): The ID of the user associated with the place (empty string by default).
        name (str): The name of the place (empty string by default).
        description (str): The description of the place (empty string by default).
        number_rooms (int): The number of rooms in the place (0 by default).
        number_bathrooms (int): The number of bathrooms in the place (0 by default).
        max_guest (int): The maximum number of guests the place can accommodate (0 by default).
        price_by_night (int): The price per night for the place (0 by default).
        latitude (float): The latitude coordinate of the place (0.0 by default).
        longitude (float): The longitude coordinate of the place (0.0 by default).
        amenity_ids (list of str): The list of amenity IDs associated with the place (empty list by default).
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
