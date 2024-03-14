"""
Inventory Manager Project
Module: util.fio
Author: Quinn Goplin

File IO utilities to create a layer of abstraction between python objects and
serialized data going in/out to and from a save file
"""

import json
import os

from obj.inventory import Inventory
from util.exc import FileIOException


def f_saveall(filename, inventories):
    """Saves a list of multiple inventories to a file"""
    with open(filename, "w") as f:
        json.dump([i.serialize() for i in inventories], f)


def f_saveone(filename, inventory):
    """Saves a standalone inventory to a file"""
    with open(filename, "w") as f:
        json.dump(inventory.serialize(), f)


def f_load(filename):
    """Loads inventory data from a file, uses type detection from the loaded data
    to determine if the file was a list or a standalone"""
    if not os.path.exists(filename):
        raise FileIOException()
    
    with open(filename, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise FileIOException()
        
        if type(data) == list:
            return [Inventory.deserialize(i) for i in data]
        elif type(data) == dict:
            return Inventory.deserialize(data)
        else:
            raise FileIOException()