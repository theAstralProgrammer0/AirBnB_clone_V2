#!/usr/bin/python3
"""city class test module"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from os import getenv


class test_City(test_basemodel):
    """city test class"""

    def __init__(self, *args, **kwargs):
        """initializing instance for city"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """state_id attr test method"""
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_name(self):
        """name attr test method"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))
