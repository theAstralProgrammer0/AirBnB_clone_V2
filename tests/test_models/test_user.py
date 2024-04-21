#!/usr/bin/python3
"""user class test module"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """user test class"""

    def __init__(self, *args, **kwargs):
        """initialize user instance"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """first_name test method"""
        new = self.value()
        self.assertEqual(type(new.first_name), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_last_name(self):
        """last_name test method"""
        new = self.value()
        self.assertEqual(type(new.last_name), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_email(self):
        """email test method"""
        new = self.value()
        self.assertEqual(type(new.email), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_password(self):
        """password test method"""
        new = self.value()
        self.assertEqual(type(new.password), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))
