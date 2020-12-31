"""All the test suites"""
from .gcd import suites as gcd_suites
from .lcm import suites as lcm_suites
from .prime import suites as prime_suites
from .triangle import suites as triangle_suites
from .zune import suites as zune_suites


TEST_SUITES = {
    "gcd": gcd_suites,
    "lcm": lcm_suites,
    "nth_prime": prime_suites,
    "valid_triangle": triangle_suites,
    "zune": zune_suites
}
