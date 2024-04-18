#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'states'

        name = Column(String(128),
                      nullable=False
                      )

        cities = relationship('City',
                              backref='state',
                              cascade='all, delete'
                              )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the state"""
        super().__init__(*args, **kwargs)


    if (getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def cities(self):
            """getter attribute that returns the list of City instances
            """
            city_values = models.storage.all('City').values()

            return [city for city in city_values if city.state_id == self.id]
