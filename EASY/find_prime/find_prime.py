from numpy import random

def random_list(N):
    '''
    Function returns a list of random integers of length N 
    with values in the range (0, 1e6)
    '''
    random_list = [random.randint(0, 1e6) for r in range(N)]
    return random_list

def prime_list(input_list):
    '''
    Function finds all primes in a list of integers
    and returns sublist containing primes
    '''
    prime_list = []
    for item in input_list:
        if is_prime(item):
            prime_list.append(item)

    return prime_list

def is_prime(a):
    return all(a % i for i in range(2, a))
    



if __name__ == "__main__":
    rlist = random_list(1000)
    plist = prime_list(rlist)
    print(plist)

