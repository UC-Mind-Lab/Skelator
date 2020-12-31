"""All the test suites"""
from .gcd import suites as gcd_suites
# from .lcm import LCM
# from .prime import NthPrime
# from .triangle import Triangle
# from .zune import ZUNE


TEST_SUITES = {
    "gcd": gcd_suites,
    # "lcm": LCM,
    # "nth_prime": NthPrime,
    # "valid_triangle": Triangle,
    # "zune": ZUNE
}
