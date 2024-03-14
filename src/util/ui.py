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


def selection_table(title, options):
    selection = 0
    while True:
        clear_ui()
        print(title + "\n")
        for i, o in enumerate(options):
            if i == selection:
                print(f">>{o}")
            else:
                print(f"  {o}")

        key = wait_key()
        if key == b"\xE0\x48" and selection > 0: # Up arrow
            selection -= 1
        elif key == b"\xE0\x50" and selection < len(options) - 1: # Down arrow
            selection += 1
        elif key == b"\r":
            return selection
