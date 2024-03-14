from obj.inventory import Inventory
from util.exc import FileIOException
from util.fio import f_saveall, f_saveone, f_load


def cmd_show(cmd, inventories):
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
        inv = inventories[index + 1]
        con = "\n".join([f" - {i}: {o.name} ({o.size})" for i, o in enumerate(inv.contents)])
        return f"{inv.name}\nMax size: {inv.size}\nContents: {con}"


def cmd_load(cmd, inventories):
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
    if len(cmd) < 3:
        return "No save-file or inventory index given"
    
    try:
        if cmd[1] == "all":
            f_saveall(cmd[2], inventories)
        else:
            index = int(cmd[1])
            if index < 1 or index > len(inventories):
                return "Invalid index"
            f_saveone(cmd[2], inventories[index])
        return "Inventory saved"
    except FileIOException:
        return f"Failed to save to file \"{cmd[2]}"
    except ValueError:
        return "Invalid index"


def cmd_new(cmd, inventories):
    if len(cmd) < 3:
        return "No inventory name or size given"
    
    try:
        size = int(cmd[2])
    except ValueError:
        return "Invalid inventory size"
    
    inventories.append(Inventory(cmd[1], size))
    return "Inventory created"
