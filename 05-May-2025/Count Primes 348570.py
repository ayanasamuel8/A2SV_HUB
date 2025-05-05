# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def sieve(self,limit):
        if limit <= 2: return 0
        prime = [True] * (limit)
        prime[0] = prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if prime[i]:
                for j in range(i*i, limit, i):
                    prime[j] = False
        return sum(1 for i, val in enumerate(prime) if val)
    def countPrimes(self, n: int) -> int:
        return self.sieve(n)