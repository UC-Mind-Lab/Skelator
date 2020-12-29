#!/usr/bin/env python3
"""Default template for my python files"""

__author__="Tyler Westland"

import argparse
import json
import os

from .main import main as skelator_main


def parse_arguments(args=None) -> None:
    """Returns the parsed arguments.

    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser(
            description="A default template for python",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("suite_name", help="Suite name")
    parser.add_argument("negations_file", help="Path to the negations json file.")
    parser.add_argument("-m", "--main_c", default=None,
            help="Path to the main c file.")
    args = parser.parse_args(args=args)
    return args


def main(suite_name, negations_file, main_c=None) -> int:
    """Main function.

    Parameters
    ----------
    input_file: str:
        Path the input file.
    Returns
    -------
    int
        The exit code.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    # Read in the file detailing the suggestions of clusters of tests
    # to invalidate.
    with open(negations_file, "r") as fin:
        negations = json.load(fin)

    # Produce the environments for testing each cluster.
    suggestion_number = 0
    for suggestion in negations["suggestions"]:
        suggestion_number += 1
        output_dir = f"{suggestion_number:03}--" + "_".join(suggestion)
        skelator_main(suite_name, main_c=main_c, output_dir=output_dir, 
                negations=suggestion)

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
