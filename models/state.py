#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __table__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete.all", backref="state")

    @property
    def cities(self):
