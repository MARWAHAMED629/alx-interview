#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to get n H characters.
    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required to
        achieve n H characters.
    """
    next = 'H'
    body = 'H'
    op = 0
    while len(body) < n:
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op
