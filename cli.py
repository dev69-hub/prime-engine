import argparse
from prime_engine.core import (
    prime_engine,
    generate_prime_numbers,
    next_prime,
    prev_prime,
    prime_factors,
    is_prime_factor,
    count_primes_upto,
    sum_primes_upto
)

def main():
    parser = argparse.ArgumentParser(description="Prime Number Engine CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Check if a number is prime
    parser_check = subparsers.add_parser("check", help="Check if a number is prime")
    parser_check.add_argument("number", type=int)

    # Generate primes up to a limit
    parser_generate = subparsers.add_parser("generate", help="Generate primes up to a number")
    parser_generate.add_argument("limit", type=int)

    # Find next prime
    parser_next = subparsers.add_parser("next", help="Find next prime after a number")
    parser_next.add_argument("number", type=int)

    # Find previous prime
    parser_prev = subparsers.add_parser("prev", help="Find previous prime before a number")
    parser_prev.add_argument("number", type=int)

    # Prime factors
    parser_factors = subparsers.add_parser("factors", help="Get prime factors of a number")
    parser_factors.add_argument("number", type=int)

    # Is prime factor
    parser_isfactor = subparsers.add_parser("isfactor", help="Check if a factor is a prime factor")
    parser_isfactor.add_argument("number", type=int)
    parser_isfactor.add_argument("factor", type=int)

    # Count primes
    parser_count = subparsers.add_parser("count", help="Count primes up to a number")
    parser_count.add_argument("limit", type=int)

    # Sum of primes
    parser_sum = subparsers.add_parser("sum", help="Sum of primes up to a number")
    parser_sum.add_argument("limit", type=int)

    args = parser.parse_args()

    if args.command == "check":
        print("Prime!" if prime_engine(args.number) else "Not prime.")

    elif args.command == "generate":
        print(generate_prime_numbers(args.limit))

    elif args.command == "next":
        print("Next prime is:", next_prime(args.number))

    elif args.command == "prev":
        print("Previous prime is:", prev_prime(args.number))

    elif args.command == "factors":
        print("Prime factors:", prime_factors(args.number))

    elif args.command == "isfactor":
        if is_prime_factor(args.number, args.factor):
            print(f"{args.factor} is a prime factor of {args.number}")
        else:
            print(f"{args.factor} is NOT a prime factor of {args.number}")

    elif args.command == "count":
        print("Total primes:", count_primes_upto(args.limit))

    elif args.command == "sum":
        print("Sum of primes:", sum_primes_upto(args.limit))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
