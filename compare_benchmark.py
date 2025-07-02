import time
from sympy import isprime as sympy_isprime, primerange
import gmpy2
import primesieve

from prime_engine.core import prime_engine, generate_prime_numbers

def benchmark(name, func, *args, repeat=3):
    durations = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        durations.append(end - start)
    avg_time = sum(durations) / repeat
    print(f"{name:<40} | Avg Time: {avg_time:.6f} sec")

if __name__ == "__main__":
    print("📊 Comparing Primality Checking Performance:\n")

    n = 999_999_1  # Large prime candidate

    benchmark("Your prime_engine", prime_engine, n)
    benchmark("sympy.isprime", sympy_isprime, n)
    benchmark("gmpy2.is_prime", gmpy2.is_prime, n)

    print("\n📊 Comparing Prime Generation up to 100,000:\n")

    limit = 100_000

    benchmark("Your generate_prime_numbers", generate_prime_numbers, limit)
    benchmark("sympy.primerange", lambda l: list(primerange(2, l)), limit)
    benchmark("primesieve", primesieve.primes, limit)
