#!/usr/python3
"""User class for the HBnB Evolution project"""
import uuid, datetime


class User:
    """Class defining any HBnB users"""

    def __init__(self, first_name, last_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__created = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated = self. created
        self.__id = str(uuid.uuid4())

    @property
    def id(self):
        """Getter for id"""
        return self.__id

    @property
    def created(self):
        """Getter for created"""
        return self.__created

    @property
    def updated(self):
        """Getter for updated"""
        return self.__updated

    @property
    def first_name(self):
        """Getter for first name"""
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets first name"""
        self.__first_name = first_name
        self.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")
    @property
    def last_name(self):
        """Getter for last name"""
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        """Last name setter"""
        self.__last_name = last_name
        self.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")
    @property
    def email(self):
        """Email Getter"""
        return self.__email

    @email.setter
    def email(self, email):
        """Email setter"""
        self.__email = email
        self.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")
    @property
    def password(self):
        """Password getter"""
        return self.__password

    @password.setter
    def password(self, password):
        """Password setter"""
        self.__password = password
        self.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")



jezer = User(first_name='jezer', last_name='gonzalez', email='jezergonzalez@gmail.com', password='1234')

print(f"User: {jezer.first_name} {jezer.last_name}, Email: {jezer.email}, Password: {jezer.password}")
print(f"id: {jezer.id}")