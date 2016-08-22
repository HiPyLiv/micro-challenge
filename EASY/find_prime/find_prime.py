from numpy import random

def random_list(N):
    '''
    Function returns a list of random integers of length N
    '''
    return [random.randint(0, 1e6) for r in range(N)]

def is_prime(p):
    '''
    Checks to see whether a number is prime
    Returns True or False
    '''
    return all(p % i for i in range (2, p))

def find_max_prime(rList):
    '''
    Returns the largest prime number in a random list
    of integers.
    '''
    # sort random list low --> high
    sList = sorted(rList)
    for el in sList[::-1]:
        if is_prime(el):
            return el

if __name__ == "__main__":
    print(find_max_prime(random_list(1000)))
