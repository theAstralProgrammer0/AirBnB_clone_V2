#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'cities'

        name = Column(String(128),
                      nullable=False,
                      )

        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False
                          )
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

