"""All the test suites"""
from .gcd import GCD
from .lcm import LCM
from .prime import NthPrime
from .zune import ZUNE

TEST_SUITES = {
    "gcd": GCD,
    "lcm": LCM,
    "nth_prime": NthPrime,
    "zune": ZUNE
}
