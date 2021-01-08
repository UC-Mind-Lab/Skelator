#!/bin/bash

suite=$1
linkage=$2
workdir="${suite}_${linkage}_linkage"

echo Working in $workdir

mkdir -p $workdir
patch_results=$(realpath $workdir/patch_results)
echo "Patch Results" > $patch_results

cd $workdir
if [ -d "all_positive" ]; then
  echo "all_positive already exists"
else
  skelator $suite -o all_positive -l $linkage
fi
cd all_positive
make clean
if [ ! -f "coverage.json" ]; then
  make coverage.json
else
  echo "coverage.json already created for all positive test cases"
fi
if [ ! -f "negations.json" ]; then
  make negations.json
else
  echo "negations.json already created for all positive test cases"
fi
cd ..
mkdir -p negations
cd negations
skelator2 $suite ../all_positive/negations.json -l $linkage

for n in $(ls .); do
  cd $n
  for m in $(ls .); do
    cd $m
    echo "Processing $n -- $m"

    if [ -d "patches" ]; then
      echo "Repair has already been attempted, not retrying"
    else
      make clean
      echo "Computing $n -- $m: repair (with 10 minute timeout)"
      timeout 10m make repair | tee $@ repair.log
      if [ ! -f "patches/0.diff" ]; then
        echo "$n--$m: No patch found" | tee -a $patch_results
      else
        echo "Patch found!"
        cp patches/0.diff found_patch.diff
        patch docker/main.c patches/0.diff
        echo "Testing if patch works: coverage"
        make coverage.json
        mv coverage.json repaired_coverage.json
        # Check for failures
        cat repaired_coverage.json | grep successful | grep false > /dev/null
        failure=$?
        if [ $failure -eq 0 ]; then
          echo "$n--$m: Patch failed!" | tee -a $patch_results
        else
          echo "$n--$m: Patch succeeded!" | tee -a $patch_results
        fi
      fi
    fi

    cd ..
  done
  cd ..
done

echo "That was a lot!"
