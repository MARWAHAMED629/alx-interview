#!/usr/bin/python3


"""Program to check if all boxes can be unlocked using keys inside them"""


def canUnlockAll(boxes):
    """
    The function takes a list of boxes, where each box contains a list of keys.
    The goal is to determine if all boxes can be unlocked using the keys found
    in the boxes.

    Steps:
    1. Create a set of keys starting with the key to the first box (box 0).
    2. Start opening boxes using the keys in the set.
    3. For each key in the set, go to the corresponding box.
    4. Take the keys found in that box and add them to the set of keys.
    5. Repeat steps 3 and 4 for all keys in the set.
    6. Ignore keys that do not correspond to valid boxes (keys greater than 0
    and less than the total number of boxes).
    7. Track the opening of boxes with a counter. If the counter equals the
    number of boxes - 1 at the end, it means all boxes can be unlocked.

    Optimization:
    By adding 0 to the set of keys at the start, we do not need an initial loop
    to begin the process.
    """
    t_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < t_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == t_boxes - 1
