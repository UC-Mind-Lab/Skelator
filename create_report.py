#!/usr/bin/env python3
"""Default template for my python files"""

__author__="Tyler Westland"

import argparse
import json
import os

from skelator.suites import TEST_SUITES

def code_listing(file_path, caption,
        label, language="C"):
    tex = ""
    tex += "\\begin{figure}[H]\n"
    tex += "\t\\lstinputlisting[language=" +\
            language + "]{" +\
            file_path + "}\n"
    tex += "\t\\caption{" + caption + "}\n"
    tex += "\t\\label{fig:" + label + "}\n"
    tex += "\\end{figure}\n"
    return tex



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
    parser.add_argument("suite", help="Name of the suite we're working with.")
    parser.add_argument("data_dir", help="Path to the directory of data.")
    parser.add_argument("-o", "--output_file", default="sub_report.tex",
            help="Path to the output file.")
    args = parser.parse_args(args=args)
    return args


def main(suite, data_dir, output_file="sub_report.tex") -> int:
    """Main function.

    Parameters
    ----------
    input_file: str:
        Path the input file.
    output_file: str
        Path to the output file. Default is 'output'
    quiet: bool
        Rather non-errors should be printed. Default is False
    Returns
    -------
    int
        The exit code.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    # The extra file for discussion of the generated report
    discussion_file = f"discussion_{output_file}"

    # The coverage
    with open(os.path.join(data_dir, "all_positive/coverage.json")) as fin:
        coverage_json = json.load(fin)

    coverage_dict = {}
    for entry in coverage_json:
        coverage_dict[entry["name"]] = entry["lines"]

    # The negations
    with open(os.path.join(data_dir, "all_positive/negations.json")) as fin:
        negations_json = json.load(fin)

    # Starting empty text string
    tex = ""

    # Start of the Tex Sub-file
    tex += "\\documentclass[report.tex]{subfiles}\n"
    tex += "\n"
    tex += "\\begin{document}\n"

    experiment_name = f"{suite.replace('_', ' ')}--"\
            f"{negations_json['linkage'].capitalize()}"

    # The special gooey middle
    tex += "\\section{" + experiment_name + "}\n"

    # All positive
    tex += "\\subsection{Correctly Functioning}\n"
    tex += code_listing(
            os.path.join(data_dir, "all_positive/docker/main.c"),
            "Correctly functioning code",
            f"{experiment_name}_CorrectlyFunctioning")

    negations_dir = os.path.join(data_dir,
        "negations")

    test_suites = TEST_SUITES[suite]
    for negation_suite_name in test_suites.keys():
        tex += "\\subsection{" + negation_suite_name.replace('_', ' ') + "}\n"
        neg_suite = test_suites[negation_suite_name]
        tex += neg_suite.tex_string(coverage_dict)

        cluster_number = 0
        for cluster_dir, sugs in zip(
                sorted(os.listdir(negations_dir)),
                negations_json["suggestions"]):
            cluster_number += 1
            tex += "\\subsubsection{" + ", ".join(sugs) + "}\n"
            fuller_cluster_dir = os.path.join(negations_dir,
                    cluster_dir)

            this_suite_cluster_dir = os.path.join(fuller_cluster_dir, 
                    negation_suite_name)

            # Check if patch was found
            docker_dir = os.path.join(this_suite_cluster_dir, "docker")
            automatic_patch_path = os.path.join(this_suite_cluster_dir, "found_patch.diff")
            manual_patch_path = os.path.join(this_suite_cluster_dir, "manual_patch.diff")
            patch_found = False
            if os.path.isfile(automatic_patch_path):
                patch_found = True
                tex += "Darjeeling automatically found the below patch\n"
                tex += code_listing(automatic_patch_path, "Probable patch",
                        f"{experiment_name}_{cluster_number:03}AutomaticPatch")
                patched_file = os.path.join(docker_dir, "main.c")
                tex += code_listing(patched_file, "Patched file",
                        f"{experiment_name}_{cluster_number:03}AutomaticPatchedFile")

            if os.path.isfile(manual_patch_path):
                patch_found = True
                tex += "The below patch was hand crafted\n"
                tex += code_listing(manual_patch_path, "Manual patch",
                        f"{experiment_name}_{cluster_number:03}ManualPatch")
                patched_file = os.path.join(docker_dir, "manual_main.c")
                tex += code_listing(patched_file, "Patched file",
                        f"{experiment_name}_{cluster_number:03}ManualPatchedFile")

            if not patch_found:
                tex += "No Patch Found\n"

    tex += "\\subfile{" + discussion_file + "}\n"

    # End of the Tex Sub-file
    tex += "\\clearpage\n"
    tex += "\\end{document}"

    # Save the tex file
    with open(output_file, "w") as fout:
        fout.write(tex)

    if not os.path.isfile(discussion_file):
        dis_tex = ""
        dis_tex += "\\documentclass[" + output_file + "]{subfiles}\n"
        dis_tex += "\n"
        dis_tex += "\\begin{document}\n"
        dis_tex += "\\subsection{Discussion}\n"
        dis_tex += "\\end{document}"
        with open(discussion_file, "w") as fout:
            fout.write(dis_tex)

    # Return success code
    return 0


# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    import sys
    args = parse_arguments()
    try:
        exit(main(**vars(args)))
    except FileNotFoundError as exp:
        print(exp, file=sys.stderr)
        exit(-1)

