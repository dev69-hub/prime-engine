import time
from prime_engine.core import (
    prime_engine,
    generate_prime_numbers,
    next_prime,
    prev_prime,
    prime_factors,
    count_primes_upto,
    sum_primes_upto
)

def benchmark(label, func, *args, repeat=1):
    durations = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        durations.append(end - start)
    avg_time = sum(durations) / repeat
    print(f"{label:<45} | Avg Time ({repeat} runs): {avg_time:.6f} sec")

if __name__ == "__main__":
    print("🔥 Running Advanced Benchmark:\n")

    # Use larger values to stress-test
    benchmark("Check if 9999991 is prime", prime_engine, 9_999_991, repeat=5)
    benchmark("Generate primes up to 100,000", generate_prime_numbers, 100_000)
    benchmark("Find next prime after 999999", next_prime, 999_999)
    benchmark("Find previous prime before 1,000,000", prev_prime, 1_000_000)
    benchmark("Prime factors of 987654321", prime_factors, 987_654_321)
    benchmark("Count primes up to 200,000", count_primes_upto, 200_000)
    benchmark("Sum primes up to 100,000", sum_primes_upto, 100_000)

    # Stress test multiple calls
    print("\n🔁 Repeated primality tests (10,000 checks from 1000000-1009999)")
    start = time.perf_counter()
    for i in range(1_000_000, 1_010_000):
        prime_engine(i)
    end = time.perf_counter()
    print(f"Total time for 10,000 primality checks: {end - start:.4f} sec")

    print("\n✅ Benchmark complete.")
