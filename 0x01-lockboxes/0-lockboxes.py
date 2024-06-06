def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])
    keys = boxes[0][:]

    while keys:
        key = keys.pop()
        if key not in opened and key < n:
            opened.add(key)
            keys.extend(boxes[key])
    
    return len(opened) == n
