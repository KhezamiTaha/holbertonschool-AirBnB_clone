#!/usr/bin/python3
"""Unit test for the base class base model
"""
import unittest
# import json
from datetime import datetime
# from io import StringIO
# from unittest.mock import patch
from models import base_model
from models.base_model import BaseModel
###############from models.engine.file_storage import FileStorage
import os


class TestBaseClass(unittest.TestCase):
    """TestBaseClass Test the base class
    Args:
        unittest (): Propertys for unit testing
    """

    def test_id_type(self):
        """ Test id type"""
        my_third = BaseModel()
        self.assertTrue(type(my_third.id) == str)

    def test_datetime_type(self):
        """ Test datetime type """
        my_third = BaseModel()
        self.assertTrue(type(my_third.created_at) == datetime)

    def test_str(self):
        """ Test str output """
        test = BaseModel()
        self.assertEqual(test.__str__(), "[" + test.__class__.__name__ + "]"
                         " (" + test.id + ") " + str(test.__dict__))

    def test_id_creation(self):
        """ check for module documentation """
        my_first = BaseModel()
        my_second = BaseModel()
        my_third = BaseModel()
        self.assertTrue(my_first.id != my_second.id)
        self.assertTrue(my_third.id != my_second.id)
        self.assertTrue(my_first.id != my_third.id)

    def test_to_dict(self):
        """testing to dict function"""
        test = BaseModel()
        my_model = test.to_dict()
        self.assertTrue(type(my_model["created_at"] == str))
        self.assertTrue(type(my_model["updated_at"] == str))
        self.assertTrue(type(test.created_at) == datetime)
        self.assertTrue(type(test.updated_at) == datetime)
        self.assertEqual(my_model["created_at"], test.created_at.isoformat())
        self.assertEqual(my_model["updated_at"], test.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
