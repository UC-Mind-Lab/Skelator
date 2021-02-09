import abc
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(FILE_DIR, "assets")


class Test(abc.ABC):
    def __init__(self, parameters, correct_output):
        """Abstract test case
        Doesn't specify the format of the output, or the negations
        of tests.
        
        Parameters
        ----------
        parameters: list
            The parameters for the test case
        correct_output: any
            The correct output given the parameters
        """
        self.parameters = parameters
        self._correct_output = correct_output


    @abc.abstractmethod
    def _output(self, value):
        pass


    @property
    @abc.abstractmethod
    def _negation(self):
        pass


    @property
    def negation(self):
        return self._output(self._negation)


    @property
    def correct_output(self):
        return self._output(self._correct_output)


    def tex_string(self, lines:dict=None):
        tex = "\\begin{itemize}\n"
        tex += "\t\\item Parameters: " + str(self.parameters) + "\n"
        tex += "\t\\item Correct Output: " + str(self.correct_output) + "\n"
        tex += "\t\\item Negation: " + str(self.negation) + "\n"
        if lines:
            tex += "\\begin{itemize}\n"
            for file_name in lines.keys():
                tex += f"\\item {file_name}: "\
                        + ", ".join((str(l) for l\
                        in lines[file_name])) + "\n"
            tex += "\\end{itemize}\n"
        tex += "\\end{itemize}\n"
        return tex


class InfiniteBugTest(Test):
    def _negation(self):
        return "RUNS INFINITELY"



class TestSuite:
    def __init__(self, links="", algorithm:str="exhaustive"):
        self.suite = {}
        self.links = links

    def add_test(self, new_test:Test):
        self.suite[f"p{len(self.suite)+1}"] = new_test

    def tex_string(self, coverage:dict=None):
        tex = "\\begin{itemize}\n"
        for test_number in range(1, len(self.suite.keys())+1):
            test_name = f"p{test_number}"
            tex += "\item " + test_name + "\n"
            tex += self.suite[test_name].\
                    tex_string(lines=coverage[test_name])
        tex += "\\end{itemize}\n"
        return tex

    def _test_sh(self, negations) -> str:
        lines = ""
        lines += "#!/bin/bash\n"
        lines += "test_id=$1\n"
        lines += "here_dir=$( cd \"$( dirname \"${BASH_SOURCE[0]}\" )\" "
        lines += "&& pwd )\n"
        lines += "test_dir=\"${here_dir}/test\"\n"
        lines += "executable=\"${here_dir}/source/main\"\n"
        lines += "\n"
        lines += "case $test_id in\n"
        negatives_accounted_for = 0
        for test_number in range(1, len(self.suite.keys())+1):
            test_name = f"p{test_number}"
            test = self.suite[test_name]
            if any((test_name == n for n in negations)):
                negatives_accounted_for += 1
                tn = f"n{negatives_accounted_for}"
                test_output = test.negation
                negative_test_case = True
            else:
                tn = f"p{test_number - negatives_accounted_for}"
                test_output = test.correct_output
                negative_test_case = False

            lines += f"{tn})\n"
            if isinstance(test, InfiniteBugTest) and negative_test_case:
                lines += "timeout 3 "
                lines += "\"${executable}\" "
                lines += " ".join((str(p) for p in test.parameters))
                lines += " && exit 1 || exit 0;;\n"
            else:
                lines += "\"${executable}\" "
                lines += " ".join((str(p) for p in test.parameters))
                lines += " |& diff \"${test_dir}/" + tn + "\" - &> "
                lines += "/dev/null && exit 0;;\n"
        lines += "esac\n"
        lines += "exit 1\n"
        return lines


    def _dockerfile(self, negations):
        with open(os.path.join(ASSETS_DIR, "Dockerfile"), "r") as fin:
            return fin.read()


    def _repair_file(self, negations, image_name, algorithm):
        with open(os.path.join(ASSETS_DIR, "repair.yml"), "r") as fin:
            repair = fin.read()
        repair = repair.replace("IMAGE_NAME", image_name)
        repair = repair.replace("NUM_PASSING_TESTS", 
                str(len(self.suite) - len(negations)))
        repair = repair.replace("NUM_FAILING_TESTS", str(len(negations)))
        repair = repair.replace("LINKS", self.links)
        repair = repair.replace("ALGORITHM", algorithm)
        return repair


    def _coverage_file(self, negations, image_name, algorithm):
        with open(os.path.join(ASSETS_DIR, "coverage.yml"), "r") as fin:
            coverage = fin.read()
        coverage = coverage.replace("IMAGE_NAME", image_name)
        coverage = coverage.replace("NUM_PASSING_TESTS", 
                str(len(self.suite) - len(negations)))
        coverage = coverage.replace("NUM_FAILING_TESTS",
                str(len(negations)))
        coverage = coverage.replace("LINKS", self.links)
        coverage = coverage.replace("ALGORITHM", algorithm)
        return coverage


    def _makefile(self, image_name, linkage):
        with open(os.path.join(ASSETS_DIR, "Makefile"), "r") as fin:
            makefile = fin.read()
        makefile = makefile.replace("IMAGE_NAME", image_name)
        makefile = makefile.replace("LINKAGE", linkage)
        return makefile


    def create_test_files(self, docker_dir, negations) -> None:
        # Check if docker_dir already exists
        if not os.path.isdir(docker_dir):
            os.mkdir(docker_dir)

        # Check if test_dir already exists
        test_dir = os.path.join(docker_dir, "test")
        if not os.path.isdir(test_dir):
            os.mkdir(test_dir)

        # Create test outputs
        for test_name in self.suite.keys():
            if test_name in negations:
                output_value = self.suite[test_name].negations
            else:
                output_value = self.suite[test_name].correct_output
            with open(os.path.join(test_dir, test_name), "w") as fout:
                fout.write(f"{output_value}")

        # Create the test script
        with open(os.path.join(docker_dir, "test.sh"), "w") as fout:
            fout.write(self.test_script())

        # Copy over the assets files
        for f in os.listdir(ASSETS_DIR):
            full_path = os.path.join(ASSETS_DIR, f)
            shutil.copy(full_path, docker_dir)


    def create_files(self, main_c, experiment_dir:str, negations,
            image_name:str, linkage:str, algorithm:str)\
        -> None:
        """Create all of the directories and files for the experiment.

        Parameters
        ----------
        experiment_dir: str
            The directory to place of this into.
        negations:
            Yes

        Directory tree:
        - experiment_dir
            - Makefile
            - repair.yml
            - coverage.yml
            - docker
                - Dockerfile
                - main.c
                - test.sh
                - test
                    - (The outputs of the test)
        """
        # Make the experiment_dir
        os.mkdir(experiment_dir)

        # Copy over the files for this directory
        # Makefile
        with open(os.path.join(experiment_dir, "Makefile"), "w") as fout:
            fout.write(self._makefile(image_name, linkage))
        # repair.yml
        with open(os.path.join(experiment_dir, "repair.yml"), "w") as fout:
            fout.write(self._repair_file(negations, image_name, algorithm))
        # coverage.yml
        with open(os.path.join(experiment_dir, "coverage.yml"), "w") as fout:
            fout.write(self._coverage_file(negations, image_name, algorithm))

        # Create the "docker" directory
        docker_dir = os.path.join(experiment_dir, "docker")
        os.mkdir(docker_dir)
        # Copy over the files in this directory
        # Dockerfile
        with open(os.path.join(docker_dir, "Dockerfile"), "w") as fout:
            fout.write(self._dockerfile(negations))
        # main.c
        with open(main_c, "r") as fin:
            with open(os.path.join(docker_dir, "main.c"), "w") as fout:
                fout.write(fin.read())
        # test.sh
        with open(os.path.join(docker_dir, "test.sh"), "w") as fout:
            fout.write(self._test_sh(negations))
        # Create the test outputs
        test_dir = os.path.join(docker_dir, "test")
        os.mkdir(test_dir)
        negatives_accounted_for = 0
        for test_number in range(1, len(self.suite.keys())+1):
            test_name = f"p{test_number}"
            test = self.suite[test_name]
            if any((test_name == n for n in negations)):
                negatives_accounted_for += 1
                tn = os.path.join(test_dir, f"n{negatives_accounted_for}")
                test_output = test.negation
            else:
                tn = os.path.join(test_dir, 
                        f"p{test_number - negatives_accounted_for}")
                test_output = test.correct_output
            # Write the output
            with open(tn, "w") as fout:
                fout.write(str(test_output))

