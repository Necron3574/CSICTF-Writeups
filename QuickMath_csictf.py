import owiener
import random
import math
from sympy.ntheory import isprime
from sympy.ntheory.modular import crt
from sympy.functions.elementary.miscellaneous import cbrt
from Crypto.Util.number import bytes_to_long, inverse , long_to_bytes
import string

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < 150:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr

def find_root(n, x):
    low = 0
    high = n
    while low < high:
        mid = (low+high)//2
        if mid**x < n:
            low = mid+1
        else:
            high = mid
    return low

n1 = 86812553978993
n2 = 81744303091421
n3 = 83695120256591
c1 = 8875674977048
c2 = 70744354709710
c3 = 29146719498409
m = [n1,n2,n3]
v = [c1,c2,c3]
N = n1*n2*n3
c = crt(m,v)
c = int(c[0])
c = find_root(c,3)
flag = str(bytes.fromhex(str(c)))[2:-1]
print('csictf{' + flag + '}')
