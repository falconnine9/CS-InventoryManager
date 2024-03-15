"""
Inventory Manager Project
Module: main
Author: Quinn Goplin
"""

from handles import *
from obj.inventory import Inventory
from util.ui import clear_ui

inventories = []
handles = {
    "show": cmd_show,
    "load": cmd_load,
    "save": cmd_save,
    "new": cmd_new,
    "delete": cmd_delete
}


def split(cmd):
    s = True
    out = []
    buf = ""
    for c in cmd:
        if c == " " and s:
            out.append(buf)
            buf = ""
        elif c == "\"":
            s = not s
        else:
            buf += c
    if len(buf) > 0:
        out.append(buf)
    return out


def _main():
    out = ""
    while True:
        clear_ui()
        print("==Inventory Manager Command UI==")
        print(f"Loaded Inventories: {len(inventories)}")
        
        if len(out) > 0:
            print(f"\n{out}")

        print("\n>", end="", flush=True)
        cmd = split(input())
        if len(cmd) < 1:
            continue
        
        if cmd[0] in handles.keys():
            out = handles[cmd[0]](cmd, inventories)
        else:
            out = "Unknown command"


if __name__ == "__main__":
    _main()