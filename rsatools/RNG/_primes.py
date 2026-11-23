"""
Generate random prime numbers using functions from numpy and sympy.

"""

from numpy.random import PCG64, Generator, BitGenerator, RandomState
from numpy import uint64
from sympy.ntheory.generate import nextprime, prevprime

class PrimeGenerator(Generator):
    """An extension of the np.random.Generator class, with the ``primes()`` method.

    This class uses code from numpy and sympy.
    """

    def __init__(self, bit_generator):
        Generator.__init__(self, bit_generator)

    def randprime(self, low, high):
        """ Return a random prime number in the range [low, high).

            Bertrand's postulate assures that
            randprime(low, 2*low) will always succeed for low > 1.

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

            References
            ==========

            .. [1] https://en.wikipedia.org/wiki/Bertrand's_postulate

        """
        if low >= high:
            return
        low, high = map(int, (low, high))
        n = self.integers(low, high, dtype=uint64)
        p = nextprime(n)
        if p >= high:
            p = prevprime(high)
        if p < low:
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
