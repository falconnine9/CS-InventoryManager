"""
Inventory Manager Project
Module: util.exc
Author: Quinn Goplin

Collection of customized exception types for easy method failing
"""

class NotEnoughCapacityException(Exception):
    pass


class ItemOutOfBoundsException(Exception):
    pass


class SerializationException(Exception):
    pass


class FileIOException(Exception):
    pass