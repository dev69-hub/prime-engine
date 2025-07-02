from operator import truediv


def prime_engine(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

def generate_prime_numbers(limit):
    prime_numbers=[]
    for i in range(2, limit+1):
         if prime_engine(i):
            prime_numbers.append(i)
    return prime_numbers

def next_prime(n):
    candidate=n+1
    while True:
        if prime_engine(candidate):
            return candidate
        candidate+=1

def prev_prime(n):
    candidate=n-1
    while candidate>1:
        if prime_engine(candidate):
            return candidate
        candidate-=1
    return None

def prime_factors(n):
    factors=[]
    divisor=2
    while n >1:
        if n % divisor ==0 and prime_engine(divisor):
            factors.append(divisor)
            n//=divisor
        else:
            divisor+=1
    return factors 

        
def is_prime_factor(n, factor):
    if n%factor==0 and prime_engine(factor):
        return True
    return False
    
def count_primes_upto(n):
    count=0
    for i in range(2, n+1):
        if prime_engine(i):
            count+=1
    return count

def sum_primes_upto(n):
    total=0
    for i in range(2,n+1):
        if prime_engine(i):
            total+=i
    return total


            






        
