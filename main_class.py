#!/usr/bin/python3
"""Main class for the HBnB Evolution project"""
import datetime
import uuid


class MainClass():
    """Class that defines creation, updates and UUIDs"""
    def create(self):
        """Instance for creation with timestamp"""
        return datetime.datetime.now()

    def update(self):
        """Instance for an update with timestamp"""
        return datetime.datetime.now()

    def UUID(self):
        """Creates Unique identifiers"""
        return uuid.uuid4()
