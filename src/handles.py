"""
Inventory Manager Project
Module: handles
Author: Quinn Goplin

Command handling functions which are mapped to commands that a user can input
on the console
"""

from obj.inventory import Inventory
from util.exc import FileIOException
from util.fio import f_save, f_load
from util.ui import wait_key


def cmd_show(cmd, inventories):
    """Show command
    Format: show [all/inventory_index]"""
    if len(cmd) < 2:
        return "No index given"

    if cmd[1] == "all":
        if len(inventories) > 0:
            return "\n".join([f"{i+1}: {o.name}" for i, o in enumerate(inventories)])
        else:
            return "No inventories"
    else:
        try:
            index = int(cmd[1])
        except ValueError:
            return "Invalid index"
        if index < 1 or index > len(inventories):
            return "Invalid index"
        inv = inventories[index - 1]
        con = "\n".join([f" - {i}: {o.name} ({o.size})" for i, o in enumerate(inv.contents)])
        return f"{inv.name}\nMax size: {inv.size}\nContents: {con}"


def cmd_load(cmd, inventories):
    """Load command
    Format: load [filename]"""
    if len(cmd) < 2:
        return "No load-file given"
    
    try:
        result = f_load(cmd[1])
    except FileIOException:
        return f"Failed to load from file: \"{cmd[1]}\""
    
    if type(result) == list:
        for inv in result:
            inventories.append(inv)
    else:
        inventories.append(result)
    return "Inventories loaded"


def cmd_save(cmd, inventories):
    """Save command
    Format: save [all/inventory_index] [filename]"""
    if len(cmd) < 3:
        return "No save-file or inventory index given"
    
    try:
        if cmd[1] == "all":
            f_save(cmd[2], inventories)
        else:
            index = int(cmd[1])
            if index < 1 or index > len(inventories):
                return "Invalid index"
            f_save(cmd[2], inventories[index - 1])
        return "Inventory saved"
    except FileIOException:
        return f"Failed to save to file \"{cmd[2]}"
    except ValueError:
        return "Invalid index"


def cmd_new(cmd, inventories):
    """New command
    Format: new [inventory_name] [inventory_size]"""
    if len(cmd) < 3:
        return "No inventory name or size given"
    
    try:
        size = int(cmd[2])
    except ValueError:
        return "Invalid inventory size"
    
    inventories.append(Inventory(cmd[1], size))
    return "Inventory created"


def cmd_delete(cmd, inventories):
    """Delete command
    Format: delete [inventory_index]"""
    if len(cmd) < 2:
        return "No index given"
    
    try:
        index = int(cmd[1])
    except ValueError:
        return "Invalid index"
    
    if index < 1 or index > len(inventories):
        return "Invalid index"
    
    inv = inventories[index - 1]
    print(f"Are you sure you want to delete {inv.name} (Y/N)")
    while True:
        k = wait_key()
        if k == b"y":
            inventories.pop(index - 1)
            return "Inventory deleted"
        elif k == b"n":
            return "Inventory deletion cancelled"


def cmd_insert(cmd, inventories):
    """Insert command
    Format: insert [inventory_index] [item_name] [item_size]"""
    if len(cmd) < 4:
        return "No inventory index, item name, or item size given"
    
