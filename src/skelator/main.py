#!/bin/env python3
import argparse
import os
import shutil

from .suites import TEST_SUITES


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(FILE_DIR, "assets")


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
    parser.add_argument("-m", "--main_c", default=None,
            help="The path to the main_c file to experiment on")
    parser.add_argument("-o", "--output_dir", default="experiment",
            help="Path to the output directory.")
    parser.add_argument("-n", "--negations", default=[],
            type=lambda inp: list(inp.split()),
            help="Path to the output directory.")
    parser.add_argument("-i", "--image_name", 
            default=None,
            help="Name of the docker image.")
    parser.add_argument("-l", "--linkage", default="single",
            help="The linkage method to use for clustering.")
    args = parser.parse_args(args=args)
    return args


def main(suite_name, main_c:str=None, output_dir:str="experiment",
        negations=[], image_name:str=None, linkage:str="single") -> int:
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
        suites = TEST_SUITES[suite_name.lower()]
    except KeyError:
        print("Valid names are: " + " ".join(TEST_SUITES.keys()))
        exit(1)

    if image_name is None:
        image_name = f"mindlab/mindlab:skelator__{suite_name}"

    if main_c is None:
        main_c = os.path.join(ASSETS_DIR, f"{suite_name.lower()}.c")

    if len(negations) == 0:
        # We're making the all positive case
        any_suite = list(suites.values())[0]
        any_suite.create_files(main_c, output_dir, negations,
                image_name, linkage)

    else:
        # Make the output dir
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        for neg_name in suites.keys():
            neg_dir = os.path.join(output_dir, neg_name)
            if not os.path.exists(neg_dir):
                suites[neg_name].create_files(main_c, neg_dir, negations,
                        image_name, linkage)

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
