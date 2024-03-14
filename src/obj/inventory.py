"""
Inventory Manager Project
Module: obj.inventory
Author: Quinn Goplin
"""

from obj.item import Item
from util.exc import *


class Inventory:
    NAME_D = "Inventory"
    SIZE_D = 10
    S_KEY = ("name", "size", "contents")

    def __init__(self, name=NAME_D, size=SIZE_D, contents=[]):
        self.name = name
        self.size = size
        self.contents = contents
    
    def __str__(self):
        return self.name
    
    def get_ec(self):
        """Gets the available capacity remaining inside the inventory"""
        c = self.size
        for i in self.contents:
            c -= i.size
        return c

    def add(self, item):
        """Adds an item to the inventory (Will raise an exception if not enough capacity)"""
        if item.size > self.get_ec():
            raise NotEnoughCapacityException()
        self.contents.append(item)
    
    def remove(self, index):
        """Removes an item from the inventory (Will raise an exception if index out-of-bounds)"""
        if index < 0 or index >= len(self.contents):
            raise ItemOutOfBoundsException()
        self.contents.pop(index)
    
    def transfer(self, index, other):
        """Transfers an item from this inventory to another (Will raise an exception if the other
        inventory doesn't have enough capacity or the index of the item is out-of-bounds)"""
        if index < 0 or index >= len(self.contents):
            raise ItemOutOfBoundsException()
        if self.contents[index].size > other.get_ec():
            raise NotEnoughCapacityException()
        other.contents.append(self.contents[index])
        self.contents.pop(index)
    
    def serialize(self):
        """Returns a serialized dictionary form of the inventory"""
        return {"name": self.name, "size": self.size, "contents":
            [i.serialize() for i in self.contents]
        }

    @staticmethod
    def deserialize(data):
        """Static method that gets an Inventory object from serialized data"""
        for key in Inventory.S_KEY:
            if key not in data:
                raise SerializationException()
        return Inventory(data["name"], data["size"],
            [Item.deserialize(i) for i in data["contents"]]
        )