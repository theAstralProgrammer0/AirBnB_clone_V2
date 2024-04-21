#!/usr/bin/python3
"""review class test module"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from os import getenv


class test_review(test_basemodel):
    """review test class"""

    def __init__(self, *args, **kwargs):
        """initialize review instance"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """place_id attr test method"""
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_user_id(self):
        """user_id attr test method"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_text(self):
        """text attr test method"""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))
