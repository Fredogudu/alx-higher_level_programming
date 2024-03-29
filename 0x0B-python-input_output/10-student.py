#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon 24th Apr, 2023
@author: Fred Ogudu
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        init method for Student class
        Attributes:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Represents of Student into json format
        Return:
            Student class as a json format
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
