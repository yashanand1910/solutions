import math

ID_LEN = 5

def count_digits(n):
    digits = 0
    while n > 0:
        n //= 10
        digits += 1
    return digits

def solution(i):
    n = 3
    digits = 1
    primes = [] # window to hold only prime numbers we need for the answer
    last_prime = 2
    last_digits = 1
    # start generating prime numbers until we have enough digits
    while digits < i + ID_LEN:
        prime = True
        for x in range(2, n):
            if (x * x) > n:
                break
            if (n % x == 0):
                prime = False
                break
        if not prime:
            n += 1
            continue
        digits += count_digits(n)
        if not primes:
            if digits >= i:
                primes.append(last_prime)
                primes.append(n)
            else:
                last_prime = n
                last_digits = digits
        else:
            primes.append(n)
        n += 1
    ans = ""
    start_index = last_digits - count_digits(primes[0]) # starting index of window
    # start generating answer string
    length = 0
    primes_str = ""
    primes_len = 0
    for prime in primes:
        prime_str = str(prime)
        primes_str += prime_str
        primes_len += len(prime_str)
        max_index = start_index + primes_len # max index we can access
        while length < ID_LEN:
            if (i + length >= max_index):
                break
            ans += primes_str[i - start_index + length]
            length += 1
        if length == ID_LEN:
            break
    return ans
