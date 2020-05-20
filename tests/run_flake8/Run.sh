#!/bin/bash
set -eu

dir=$(dirname $0)
cd "$dir"

for py in ./*.py
do
    # Python3.5 does not support f-string so skip it
    if [[ "`python -V`" =~ ^Python\ 3\.5 && "$py" =~ fstring ]]
    then
        continue
    fi
    echo Checking $py result
    expected="$py".expected
    actual="$py".actual
    flake8 --select NIC --exit-zero "$py" >"$actual"
    diff -u "$expected" "$actual"
done
