#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24, 2023
@author: Fred Ogudu
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
