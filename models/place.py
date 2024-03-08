#!/usr/bin/python3
"""
Test for the Place class
"""


from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Public class attributes:
        city_id (str): The ID of the city associated
        user_id (str): The ID of the user associated
        name (str): The name of the place
        description (str): The description
        number_rooms (int): The number of rooms in
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The maximum number of guests the place
        price_by_night (int): The price per night for
        latitude (float): The latitude coordinate
        longitude (float): The longitude coordinate of
        amenity_ids (list of str): The list of amenity IDs associated
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
