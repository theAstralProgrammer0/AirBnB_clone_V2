#!/usr/bin/python3
"""This is dbstorage module"""
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User

str_to_class = {
                'User': User,
                'Place': Place,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Review': Review
                }

class DBStorage:
    """This the dbstorage class"""
    __engine = None
    __session = None
    __url = None
    __dialect = 'mysql'
    __dbapi = 'mysqldb'
    __user = getenv('HBNB_MYSQL_USER')
    __pwd = getenv('HBNB_MYSQL_PWD')
    __host = getenv('HBNB_MYSQL_HOST')
    __db = getenv('HBNB_MYSQL_DB')


    @classmethod
    def make_url(cls):
        """This method makes the db server url"""
        cls.__url = "{}+{}://{}:{}@{}/{}".format(cls.__dialect,
                                                 cls.__dbapi,
                                                 cls.__user,
                                                 cls.__pwd,
                                                 cls.__host,
                                                 cls.__db)
        return cls.__url

    def __init__(self):
        """Initializes the database instance"""
        engine = create_engine(DBStorage.make_url(), pool_pre_ping=True)
        self.__engine = engine
        
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """add the object to the current database session"""
        if not self.__session:
            self.reload()

        objs = {}
        if type(cls) == str:
            cls = str_to_class.get(cls, None)

        if cls:
            objs = self.__session.query(cls)
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objs[key] = obj
        else:
            for cls in str_to_class.values():
                print("cls is {}".format(cls))
                for obj in self.__session.query(cls):
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs[key] = obj

        return objs

 
    def new(self, obj):
        """Creates a new instance of a class in the database"""
        self.__session.add(obj)

    def save(self):
        """commits session changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object"""
        if not self.__session:
            self.reload()

        if obj:
            self.__session.delete()

    def reload(self):
        """This method reloads the objects from the database"""
        SessionFactory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(SessionFactory)
