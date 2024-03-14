"""
Inventory Manager Project
Module: obj.item
Author: Quinn Goplin
"""

from util.exc import SerializationException


class Item:
    NAME_D = "Item"
    SIZE_D = 1
    S_KEY = ("name", "size", "meta")

    def __init__(self, name=NAME_D, size=SIZE_D, meta={}):
        self.name = name
        self.size = size
        self.meta = {}
    
    def __str__(self):
        return self.name
    
    def serialize(self):
        """Returns a serialized dictionary form of the item"""
        return {"name": self.name, "size": self.size, "meta": self.meta}
    
    @staticmethod
    def deserialize(data):
        """Static method that gets an Item object from serialized data"""
        for key in Item.S_KEY:
            if key not in data:
                raise SerializationException()
        return Item(data["name"], data["size"], data["meta"])
