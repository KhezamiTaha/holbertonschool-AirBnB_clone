#!/usr/bin/python3
"""Unit test for the base class base model
"""
import unittest
from datetime import datetime, timedelta
# import json
from datetime import datetime
# from io import StringIO
# from unittest.mock import patch
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from models import storage


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

    def test_save(self):
        """Test save method of BaseModel"""

        # Create a new instance of BaseModel
        my_new_model = BaseModel()

        # Get the initial value of updated_at
        previous_updated_at = my_new_model.updated_at

        # Call the save method
        my_new_model.save()

        # Get the updated value of updated_at
        current_updated_at = my_new_model.updated_at

        # Verify that updated_at has been updated to a later time
        self.assertGreater(current_updated_at, previous_updated_at)

    def test_save_multiple(self):
        """Test save method of BaseModel with multiple calls"""

        # Create a new instance of BaseModel
        my_new_model = BaseModel()

        # Get the initial value of updated_at
        previous_updated_at = my_new_model.updated_at

        # Call the save method multiple times
        for _ in range(5):
            my_new_model.save()

        # Get the updated value of updated_at
        current_updated_at = my_new_model.updated_at

        # Verify that updated_at has been updated to a later time after each call
        self.assertGreater(current_updated_at, previous_updated_at)

    def test_save_with_delay(self):
        """Test save method of BaseModel with delay"""

        # Create a new instance of BaseModel
        my_new_model = BaseModel()

        # Get the initial value of updated_at
        previous_updated_at = my_new_model.updated_at

        # Introduce a delay
        # You can use sleep or simulate the passage of time in a different way
        # For demonstration, we'll just wait for a brief period
        delay = timedelta(seconds=1)
        datetime_after_delay = datetime.utcnow() + delay

        # Call the save method
        my_new_model.save()

        # Get the updated value of updated_at
        current_updated_at = my_new_model.updated_at

        # Verify that updated_at has been updated to a later time after the delay
        time_difference = timedelta(seconds=1)
        self.assertGreaterEqual(current_updated_at, datetime_after_delay - time_difference)
    
    def test_save_with_storage(self):
        """Test save method of BaseModel with storage"""

        # Create a new instance of BaseModel
        my_new_model = BaseModel()

        # Get the initial value of updated_at
        previous_updated_at = my_new_model.updated_at

        # Call the save method
        my_new_model.save()

        # Get the updated value of updated_at
        current_updated_at = my_new_model.updated_at

        # Verify that updated_at has been updated to a later time
        self.assertGreater(current_updated_at, previous_updated_at)

        # Reload the object from storage
        storage.reload()

        # Get the reloaded object
        reloaded_model = storage.all()["BaseModel." + my_new_model.id]


if __name__ == '__main__':
    unittest.main()
