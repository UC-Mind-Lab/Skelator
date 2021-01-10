# Skeleator
Used to setup experiments with using a fork of 
[Darjeeling](https://github.com/UC-Mind-Lab/Darjeeling) to induce
bugs into working programs using "patch generation"

# Program Sources
The sources for the programs being experimented on are:
+ [GCD](https://github.com/squaresLab/Darjeeling/tree/master/example/gcd)
  + Note this is the fixed version as recommended by the experimental setup
  in Darjeeling
+ [Zune](https://github.com/squaresLab/Darjeeling/tree/master/example/zune)
  + Note this is the fixed version as is possible using the transformation
  operators in Darjeeling. Darjeeling is not currently capable of fixing this
  program.
+ [Valid Triangle](https://www.geeksforgeeks.org/check-whether-triangle-is-valid-or-not-if-three-points-are-given/)
+ [Nth Prime](https://www.csinfo360.com/2020/01/write-program-to-find-nth-prime-number.html)
+ [Fibonacci Variations](https://www.geeksforgeeks.org/c-program-for-fibonacci-numbers/)
+ [Direct LCM](https://www.programiz.com/c-programming/examples/lcm)
+ LCM using GCD (original)

# Usage
First install with
```
pip install .
```

The `skelator` creates a directory of experiments for the specified program.
It in fact creates a directory for each type of negation, assuming some test 
cases were specified to be negated.
The `skelator2` command calls the `skealtor` command for each group of 
negations passed into it.

The `create_negations_environments.sh` script will call the commands to
setup and run an experiment. The `create_report.py` script will turn a
completed experiment directory into a LaTeX file for easier viewing.
