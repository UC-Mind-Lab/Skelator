#!/bin/env python3
import argparse
import os
import shutil

from .test import GCDTest, TestSuite, ZuneTest

test_suites = {}

# Define GCD test cases
gcd_suite = TestSuite()
gcd_suite.add_test(GCDTest([1071, 1029], 21))
gcd_suite.add_test(GCDTest([555, 666], 111))
gcd_suite.add_test(GCDTest([678, 987], 3))
gcd_suite.add_test(GCDTest([8767, 653], 1))
gcd_suite.add_test(GCDTest([16777216, 512], 512))
gcd_suite.add_test(GCDTest([16, 4], 4))
gcd_suite.add_test(GCDTest([315, 831], 3))
gcd_suite.add_test(GCDTest([513332, 91583315], 1))
gcd_suite.add_test(GCDTest([112, 135], 1))
gcd_suite.add_test(GCDTest([310, 55], 5))
gcd_suite.add_test(GCDTest([0, 55], 0))
test_suites["gcd"] = gcd_suite

# Define Zune test cases
zune_suite = TestSuite()
zune_suite.add_test(ZuneTest([10593], 2008))
zune_suite.add_test(ZuneTest([12054], 2012))
zune_suite.add_test(ZuneTest([1827], 1984))
zune_suite.add_test(ZuneTest([366], 1980))
zune_suite.add_test(ZuneTest([-366], 1980))
zune_suite.add_test(ZuneTest([-100], 1980))
zune_suite.add_test(ZuneTest([0], 1980))
zune_suite.add_test(ZuneTest([365], 1980))
zune_suite.add_test(ZuneTest([367], 1981))
zune_suite.add_test(ZuneTest([1000], 1982))
zune_suite.add_test(ZuneTest([1826], 1984))
zune_suite.add_test(ZuneTest([2000], 1985))
zune_suite.add_test(ZuneTest([3000], 1988))
zune_suite.add_test(ZuneTest([4000], 1990))
zune_suite.add_test(ZuneTest([5000], 1993))
zune_suite.add_test(ZuneTest([10592], 2008))
test_suites["zune"] = zune_suite


def parse_arguments(args=None) -> None:
    """Returns the parsed arguments.

    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser(
            description="",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("suite_name",
            help="The name of the suite we want to use.")
    parser.add_argument("main_c",
            help="The path to the main_c file to experiment on")
    parser.add_argument("-o", "--output_dir", default="experiment",
            help="Path to the output directory.")
    parser.add_argument("-n", "--negations", default=[],
            type=lambda inp: list(inp.split()),
            help="Path to the output directory.")
    parser.add_argument("-i", "--image_name", 
            default="mindlab/mindlab:skelatorDefaultImageName",
            help="Name of the docker image.")
    args = parser.parse_args(args=args)
    return args


def main(suite_name, main_c, output_dir:str="experiment", negations=[],
        image_name:str="mindlab/mindlab:skelatorDefaultImageName") -> int:
    """Main function.

    Parameters
    ----------
    output_dir: str
        The directory to output everything to.

    Returns
    -------
    int
        The exit code.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    try:
        suite = test_suites[suite_name.lower()]
    except KeyError:
        print("Valid names are: " + " ".join(test_suites.keys()))
        exit(1)

    suite.create_files(main_c, output_dir, negations, image_name)

    # Return success code
    return 0


def cli_interface() -> None:
    import sys
    args = parse_arguments()
    try:
        exit(main(**vars(args)))
    except FileNotFoundError as exp:
        print(exp, file=sys.stderr)
        exit(-1)

# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    cli_interface()
