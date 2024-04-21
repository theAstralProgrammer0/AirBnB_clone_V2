#!/usr/bin/python3
"""amenity test module"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from os import getenv


class test_Amenity(test_basemodel):
    """amenity test class"""

    def __init__(self, *args, **kwargs):
        """initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """tests the name attribute of object"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))
