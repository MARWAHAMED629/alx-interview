#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(rounds, numbers):

    if rounds <= 0 or numbers is None:
        return None
    if rounds != len(numbers):
        return None

    ben_score = 0
    maria_score = 0

    primes_list = [1 for _ in range(sorted(numbers)[-1] + 1)]
    primes_list[0], primes_list[1] = 0, 0
    for index in range(2, len(primes_list)):
        remove_multiples(primes_list, index)

    for num in numbers:
        if sum(primes_list[0:num + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None


def remove_multiples(primes_array, factor):

    for index in range(2, len(primes_array)):
        try:
            primes_array[index * factor] = 0
        except (ValueError, IndexError):
            break
