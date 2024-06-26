#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from os import getenv

t_fmt_str = '%Y-%m-%dT%H:%M:%S.%f'

storage_type = getenv('HBNB_TYPE_STORAGE')
if storage_type == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60),
                unique=True,
                nullable=False,
                primary_key=True
                )
    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow
                        )
    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow
                        )

    def __init__(self, *args, **kwargs):
        """Instatntiates the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
            if type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at, t_fmt_str)
            if type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at, t_fmt_str)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__).strip('\"')

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns a dictionary of
           all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """Deletes the current instance from storage via its delete method"""
        models.storage.delete(self)
