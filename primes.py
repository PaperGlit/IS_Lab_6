import random
import time
from collections import Counter


class Primes:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def generate_large_prime(n_bits, t):
        start_time = time.time()
        iterations = 0
        while True:
            iterations += 1
            candidate = random.getrandbits(n_bits) | (1 << (n_bits - 1)) | 1
            primes, _ = Primes.find_primes_in_range(0, 2000)
            for prime in primes:
                if candidate % prime == 0:
                    continue
            if not Primes.rabin_miller(candidate, t):
                continue
            end_time = time.time()
            execution_time = end_time - start_time
            return candidate, iterations, execution_time

    @staticmethod
    def rabin_miller(n, k=5):
        if n < 2: return False
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            if n % p == 0:
                return n == p
        s = 0
        d = n - 1
        while d % 2 == 0:
            s = s + 1
            d = d // 2
        for i in range(k):
            x = pow(random.randint(2, n - 1), d, n)
            if x == 1 or x == n - 1:
                continue
            for r in range(1, s):
                x = (x * x) % n
                if x == 1:
                    return False
                if x == n - 1:
                    break
            else:
                return False
        return True

    @staticmethod
    def find_primes_in_range(start, end):
        start_time = time.time()
        primes = []
        for i in range(start, end + 1):
            if Primes.is_prime(i):
                primes.append(i)
        end_time = time.time()
        execution_time = end_time - start_time
        return primes, execution_time

    @staticmethod
    def find_primitive_roots(number):
        start_time = time.time()
        if not  Primes.is_prime(number):
            raise ValueError(f"The number {number} is not a prime.")
        number_euler = number - 1
        primes = Primes.prime_factors(number_euler)
        primes_divided = []
        counter = 0
        primitive_roots = []
        for i in primes:
            primes_divided.append(number_euler // i)
        for i in range(1, number):
            if counter <= 100:
                if all((Primes.modular_exponentiation(i, j, number) != 1) for j in primes_divided):
                    primitive_roots.append(i)
                    counter += 1
            else:
                break
        end_time = time.time()
        execution_time = end_time - start_time
        return primitive_roots, execution_time

    @staticmethod
    def prime_factors(n):
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
            if divisor * divisor > n > 1:
                factors.append(n)
                break
        factor_counts = Counter(factors)
        unique_factors = list(factor_counts.keys())
        return unique_factors

    @staticmethod
    def modular_exponentiation(a, b, m):
        result = 1
        a = a % m
        while b > 0:
            if b % 2 == 1:
                result = (result * a) % m
            a = (a * a) % m
            b //= 2
        return result
