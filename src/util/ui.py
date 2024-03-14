"""
Inventory Manager Project
Module: util.ui
Author: Quinn Goplin

"""

import os
import msvcrt
import sys


def clear_ui():
    """Clears the entire UI screen using system calls"""
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def wait_key():
    """Waits for a singular keypress using built-in kernel calls, has support for 16-bit
    keyboard scan-codes"""
    key = msvcrt.getch()
    if key == b"\xE0":
        key = b"\xE0" + msvcrt.getch()
    return key
