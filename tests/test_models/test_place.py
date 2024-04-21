#!/usr/bin/python3
"""place class test module"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from os import getenv


class test_Place(test_basemodel):
    """place test class"""

    def __init__(self, *args, **kwargs):
        """initialize place instance"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """city_id attr test"""
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_user_id(self):
        """user_id attr test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_name(self):
        """name attr test"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_description(self):
        """description attr test"""
        new = self.value()
        self.assertEqual(type(new.description), str if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_number_rooms(self):
        """number_rooms attr test"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_number_bathrooms(self):
        """number_bathrooms attr test"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_max_guest(self):
        """max_guest attr test"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_price_by_night(self):
        """price_by_night attr test"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_latitude(self):
        """latitude attr test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_longitude(self):
        """longitude attr test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_amenity_ids(self):
        """amenity_ids attr test"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                         getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))
