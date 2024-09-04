#!/usr/bin/python3

def isWinner(x, nums):
    if x <= 0 or not nums or x != len(nums):
        return None

    max_num = max(nums)
    primes = [1] * (max_num + 1)
    primes[0] = primes[1] = 0

    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            primes[i*i:max_num+1:i] = [0] * len(primes[i*i:max_num+1:i])

    maria_wins = sum(sum(primes[:n+1]) % 2 != 0 for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
