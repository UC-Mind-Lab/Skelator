"""All the test suites"""
from .fibonacci import suites as fibonacci_suites
from .gcd import suites as gcd_suites
from .lcm import direct_suites as direct_lcm_suites
from .lcm import with_gcd_suites as lcm_wth_gcd_suites
from .prime import suites as prime_suites
from .triangle import suites as triangle_suites
from .zune import suites as zune_suites


TEST_SUITES = {
    "direct_lcm": direct_lcm_suites,
    "dynamic_fibonacci": fibonacci_suites,
    "gcd": gcd_suites,
    "lcm_with_gcd": lcm_wth_gcd_suites,
    "nth_prime": prime_suites,
    "recursive_fibonacci": fibonacci_suites,
    "space_optimized_fibonacci": fibonacci_suites,
    "valid_triangle": triangle_suites,
    "zune": zune_suites,
}
