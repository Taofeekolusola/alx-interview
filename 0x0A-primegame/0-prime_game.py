#!/usr/bin/python3
def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """Returns a list of primes up to n using the Sieve of Eratosthenes"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    def count_moves(n):
        """Returns the number of moves (primes that can be picked)"""
        primes = sieve_of_eratosthenes(n)
        move_count = 0
        visited = [False] * (n + 1)
        
        for prime in primes:
            if not visited[prime]:
                move_count += 1
                for multiple in range(prime, n + 1, prime):
                    visited[multiple] = True
        return move_count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            moves = count_moves(n)
            if moves % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
