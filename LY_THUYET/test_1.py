
number = int(input())
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_greater_second_prime(n):
    prime = n
    index = 0
    while prime > 1:
        if is_prime(prime):
            index += 1
        if index == 2:
            return prime
        else:
            prime -= 1
    return 

print(find_prime_greater_second_prime(number))


