#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon 24th Apr, 2023
@author: Fred Ogudu
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from json file
    Arguments:
        filename (str): The name of the output file
    Return:
        A file with a text in jason format
    """
    with open(filename, encoding='utf-8') as file:
        return (json.loads(file.read()))
