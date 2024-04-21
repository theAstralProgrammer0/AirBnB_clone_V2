#!/usr/bin/python3
"""state class test module"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from os import getenv


class test_state(test_basemodel):
    """state test class"""

    def __init__(self, *args, **kwargs):
        """initializing state instance"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """name attr test method"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))
