from math import lcm

def carmichael(p: int, q: int) -> int:
    """Return Carmichael's totient of p*q, only if p and q are prime.
    
    This function returns the least common multiple of p-1 and q-1. 
    If p and q are prime, this is Carmichael's totient of their 
    product.  This is helpful for the RSA cryptosystem.  
    """
    return lcm(p-1, q-1)

def modinverse(a: int, n: int) -> int:
    """Return the multiplicative inverse of `a` modulo `n`.
    
    This function uses the extended Euclidean algorithm to solve 
    for `gcd(a,n)` and minimal Bezout Coefficients (BC). Assuming 
    that `gcd(a,n)=1`, the positive minimal BC of `a` is exactly the
    multiplicative inverse of `a` mod `n`. After the `while()` loop, 
    `r0 = gcd(a,n)`, `s0` is a minimal BC for `a`, and `t0` is the 
    relevant BC for `n`.  The sign of the inputs is not used, so `a` 
    and `-a` give the same output.  `modinverse(a, b)` will always 
    output a positive number.  Using 0 as either input will probably
    break something.
    """

    if abs(a)==abs(n):
        return 1        # this is the trivial case of a=b
                        #
    elif abs(a)>abs(n): # WANT: sa + tb = gcd(a,b) AND r0=a
        r0 = abs(a)
        r1 = abs(n)
        s0 = 1
        t0 = 0
        s1 = 0
        t1 = 1
                        #
    elif abs(a)<abs(n): # WANT: sa + tb = gcd(a,b) AND r0=b
        r0 = abs(n)     # to achieve this, we need to flip
        r1 = abs(a)     # the definitions of s and t
        s0 = 0
        t0 = 1
        s1 = 1
        t1 = 0

    else:
        raise RuntimeError("This is impossible.")
                        #
    while not r1==0:    # Apply the extended Euclidean alg.
        q1 = r0 // r1
        r2 = r0 % r1
        s2 = s0 - (q1*s1)
        t2 = t0 - (q1*t1)
        r0 = r1
        r1 = r2
        s0 = s1
        s1 = s2
        t0 = t1
        t1 = t2
                        #
    if s0>0:            # now ensure positive output
        return s0  
        # s is already positive

    elif s0<0:
        return s0+(n//r0)
        # we find the *other* minimal bezout coefficients
        # so that s is positive and t is negative

    else:
        raise RuntimeError("This should never happen.")

def inverse257(n: int) -> int:
    """Find the multiplicative inverse of 257 modulo n and return an int.
    
    This function uses the extended Euclidean Algorithm to find minimal 
    coefficients to Bezout's Identity, i.e. find s and t such that
    `s*257 + t*n = 1`. The minimal positive value of s is exactly the
    multiplicative inverse of 257 mod n. 

    Generally, inputs smaller than `n=50_365_204_798_708_800` are not 
    reccommended, although they should work as normal. Inputs smaller
    than `n=65520` are not allowed and will raise `RuntimeError`.  
    """

    if n<=65520 or type(n) is not int:
        raise RuntimeError(
            "inverse257() only accepts integer inputs larger than 65520."
        )
    else:
        pass

    r0 = 257
    r1 = n    # all integers greater than 65520 are positive
    s0 = 1
    t0 = 0
    s1 = 0
    t1 = 1
                        #
    while not r1==0:    # Apply the extended Euclidean alg.
        q1 = r0 // r1
        r2 = r0 % r1
        s2 = s0 - (q1*s1)
        t2 = t0 - (q1*t1)
        r0 = r1
        r1 = r2
        s0 = s1
        s1 = s2
        t0 = t1
        t1 = t2
                        #
    if s0>0:            # now ensure positive output
        return int(s0)  
        # s is already positive

    elif s0<0:
        return int(s0+int(n//r0))
        # we find the *other* minimal bezout coefficients
        # so that s is positive and t is negative

    else:
        raise RuntimeError("This should never happen.")

