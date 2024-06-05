#!/usr/python3
"""User class for the HBnB Evolution project"""
MainClass = __import__("main_class").MainClass


class User(MainClass):
    """Class defining any HBnB users"""

    def __init__(self, first_name, last_name, email, password):
        self.__firs_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.created = super().create().strftime("%b/%d/%y %I:%M %p")
        self.updated = self. created
        self.__id = super().UUID()

    @property
    def first_name(self):
        """Getter for first name"""
        return self.__firs_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets first name"""
        self.__firs_name = first_name
        self.updated = super().create().strftime("%b/%d/%y %I:%M %p")

    @property
    def last_name(self):
        """Getter for last name"""
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        """Last name setter"""
        self.__last_name = last_name
        self.updated = super().create().strftime("%b/%d/%y %I:%M %p")

    @property
    def email(self):
        """Email Getter"""
        return self.__email

    @email.setter
    def email(self, email):
        """Email setter"""
        self.__email = email
        self.updated = super().create().strftime("%b/%d/%y %I:%M %p")

    @property
    def password(self):
        """Password getter"""
        return self.__password

    @password.setter
    def password(self, password):
        """Password setter"""
        self.__password = password
        self.updated = super().create().strftime("%b/%d/%y %I:%M %p")
