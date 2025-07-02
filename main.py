from prime_engine.core import (prime_engine,generate_prime_numbers, next_prime, prev_prime, prime_factors,is_prime_factor,count_primes_upto,sum_primes_upto)
def main():
    while True:
        print("\n--- Prime Engine Menu---")
        print("1. Check if a number is prime or not ")
        print("2. Generate prime numbers upto Given number")
        print("3. Find Next prime after given number  ")
        print("4. Find previous prime before a number")
        print("5. Get prime factors of a number")
        print("6. Check if a factor is a prime factor")
        print("7. Count primes up to a number")
        print("8. Sum of primes up to a number")
        print("0. Exit")

        choice=input("Enter Your choice:")
        
        if choice =="1":
           n= int(input("Enter number:-   "))
           print("Prime!" if prime_engine(n) else "Not prime.")

        elif choice == "2":
            limit = int(input("Generate primes up to: "))
            print(generate_prime_numbers(limit))
        
        elif choice == "3":
            n = int(input("Find next prime after: "))
            print("Next prime is:", next_prime(n))

        elif choice == "4":
            n = int(input("Find previous prime before: "))
            result = prev_prime(n)
            print("Previous prime is:", result if result else "None (below 2)")

        elif choice == "5":
            n = int(input("Get prime factors of: "))
            print("Prime factors:", prime_factors(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            factor = int(input("Enter factor: "))
            if is_prime_factor(n, factor):
                print(f"{factor} is a prime factor of {n}")
            else:
                print(f"{factor} is NOT a prime factor of {n}")

        elif choice == "7":
            n = int(input("Count primes up to: "))
            print("Total primes:", count_primes_upto(n))

        elif choice == "8":
            n = int(input("Sum primes up to: "))
            print("Sum of primes:", sum_primes_upto(n))

        elif choice == "0":
            print("Exiting Prime Engine.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__=="__main__":
 main()
