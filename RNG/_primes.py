"""
Generate random prime numbers using functions from numpy and sympy.

"""

from numpy.random import PCG64, Generator, BitGenerator, RandomState
from sympy.ntheory.generate import nextprime, prevprime

class PrimeGenerator(Generator):
    """Docstring goes here!"""

    def __init__(self, bit_generator):
        Generator.__init__(self, bit_generator)

    def randprime(self, a, b):
        """ Return a random prime number in the range [a, b).

            Bertrand's postulate assures that
            randprime(a, 2*a) will always succeed for a > 1.

            Note that due to implementation difficulties,
            the prime numbers chosen are not uniformly random.
            For example, there are two primes in the range [112, 128),
            ``113`` and ``127``, but ``randprime(112, 128)`` returns ``127``
            with a probability of 15/17.

            Examples
            ========

            >>> from sympy import randprime, isprime
            >>> randprime(1, 30) #doctest: +SKIP
            13
            >>> isprime(randprime(1, 30))
            True

            See Also
            ========

            primerange : Generate all primes in a given range

            References
            ==========

            .. [1] https://en.wikipedia.org/wiki/Bertrand's_postulate

        """
        if a >= b:
            return
        a, b = map(int, (a, b))
        n = randint(a - 1, b)
        p = nextprime(n)
        if p >= b:
            p = prevprime(b)
        if p < a:
            raise ValueError("no primes exist in the specified range")
        return p

def prime_rng(seed=None):
    if isinstance(seed, BitGenerator):
        # We were passed a BitGenerator, so just wrap it up.
        return PrimeGenerator(seed)
    elif isinstance(seed, Generator):
        # We were passed a Generator, so wrap up its BitGenerator.   
        return PrimeGenerator(seed._bit_generator)
    elif isinstance(seed, RandomState):
        gen = PrimeGenerator(seed._bit_generator)
        return gen

    # Otherwise we need to instantiate a new BitGenerator and Generator as
    # normal.
    return PrimeGenerator(PCG64(seed))
