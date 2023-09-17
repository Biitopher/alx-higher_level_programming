#!/usr/bin/python3
"""Defines class state"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City

class State(Base):
    """Defines state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          back_populates="state",
                          cascade="all, delete-orphan")
