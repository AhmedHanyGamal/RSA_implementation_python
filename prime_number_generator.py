import random
import secrets
from supplementary_functions import fast_power

__first_few_primes = []

def __nBitRandomNumber(n):
    # return random.randrange(2**(n-1)+1, 2**n-1)
    return secrets.randbits(n)



def __sieve(upper_limit = 1000):
    is_prime = [True] * (upper_limit+1)

    for i in range(2, len(is_prime)):
        if is_prime[i] == False:
            continue
        __first_few_primes.append(i)
        for j in range(i*i, len(is_prime), i):
            is_prime[j] = False


def __isLowLevelPrime(prime_candidate):
    for prime in __first_few_primes:
        if prime_candidate % prime == 0 and prime**2 <= prime_candidate:
            return False
        else: 
            return True


def __isMillerRabinPassed(miller_rabin_candidate):
    #Run no less than 20 iterations of Rabin Miller Primality test
    
    max_divisions_by_two = 0
    even_component = miller_rabin_candidate-1

    while even_component % 2 == 0:
        even_component >>= 1
        max_divisions_by_two += 1

    assert 2 ** max_divisions_by_two * even_component == miller_rabin_candidate - 1

    def trialComposite(round_tester):
        if fast_power(round_tester, even_component, miller_rabin_candidate) == 1:
            return False
        for i in range(max_divisions_by_two):
            if fast_power(round_tester, 2**i * even_component, miller_rabin_candidate) == miller_rabin_candidate - 1:
                return False
        return True
    
    number_of_rabin_trials = 20
    for i in range(number_of_rabin_trials):
        round_tester = random.randrange(2, miller_rabin_candidate)
        if trialComposite(round_tester):
            return False
    
    return True


__sieve()

def generateLargePrime(bit_num):
    while True:
        prime_candidate = __nBitRandomNumber(bit_num)

        if not __isLowLevelPrime(prime_candidate):
            continue

        if not __isMillerRabinPassed(prime_candidate):
            continue

        return prime_candidate
    




# print(f"2048 bit prime number:{generateLargePrime(2048)}")
# print(f"2048 bit prime number:{generateLargePrime(2048)}")
# print(f"1024 bit prime number:{generateLargePrime(1024)}")
# print(f"1024 bit prime number:{generateLargePrime(1024)}")