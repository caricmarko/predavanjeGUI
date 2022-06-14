def kvadrat(x):
    return x*x

#assert kvadrat(10)==101
#print(kvadrat(10)==100)
import math
def is_prime(n):
    """Determines if a non-negative integer is prime."""
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

assert is_prime(29)