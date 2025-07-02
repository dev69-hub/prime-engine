#  Prime Engine

A lightweight Python engine for working with prime numbers: checking, generating, factoring, and more.

##  Features

- ✅ Check if a number is prime
- ✅ Generate all primes up to a number
- ✅ Find the next/previous prime from a number
- ✅ Get all prime factors of a number
- ✅ Check if a factor is a prime factor
- ✅ Count all primes up to `n`
- ✅ Sum all primes up to `n`
- ✅ Interactive CLI menu
  
##Performance Logs

📊 Comparing Primality Checking Performance:

Your prime_engine                        | Avg Time: 0.000060 sec
sympy.isprime                            | Avg Time: 0.000031 sec
gmpy2.is_prime                           | Avg Time: 0.000003 sec

📊 Comparing Prime Generation up to 100,000:

Your generate_prime_numbers              | Avg Time: 0.054800 sec
sympy.primerange                         | Avg Time: 0.032135 sec
primesieve                               | Avg Time: 0.000658 sec

## 📦 Project Structure

```bash
prime_engine/
├── prime_engine/
│   ├── __init__.py
│   └── core.py        # Core logic and functions
├── main.py            # CLI interface
├── cli.py             # Optional command-line flag interface (argparse)
├── README.md
├── LICENSE
├── .gitignore




