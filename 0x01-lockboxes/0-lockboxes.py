#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of lists): A list where each index contains a list of keys.
    
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = set([0])
    keys = boxes[0][:]

    while keys:
        key = keys.pop()
        if key not in opened and key < n:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == n
