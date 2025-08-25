# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def get_prime_factorization(self, n):
        if n < 2:
            return []

        spf = list(range(n + 1))

        for p in range(2, int(math.sqrt(n)) + 1):
            if spf[p] == p:
                for i in range(p * p, n + 1, p):
                    if spf[i] == i:
                        spf[i] = p

        factors = []
        num = n
        
        while num != 1:
            smallest_prime = spf[num]
            factors.append(smallest_prime)
            
            num //= smallest_prime
            
        return factors
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        all_distinct_factors = set()
        for i in nums:
            all_distinct_factors |= set(self.get_prime_factorization(i))
        return len(all_distinct_factors)