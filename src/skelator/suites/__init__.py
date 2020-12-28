"""All the test suites"""
from .gcd import GCD
from .prime import NthPrime
from .zune import ZUNE

TEST_SUITES = {
    "gcd": GCD,
    "nth_prime": NthPrime,
    "zune": ZUNE
}
