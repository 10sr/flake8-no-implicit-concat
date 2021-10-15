#!/bin/bash
set -eu

dir=$(dirname $0)
cd "$dir"

for py in ./*.py
do
    # Python<3.6 does not support f-string so skip it
    if python -c 'import sys; assert sys.version_info < (3, 6)' 2>/dev/null \
            && [[ "$py" =~ fstring ]]
    then
        continue
    fi
    echo Checking $py result
    expected="$py".expected
    actual="$py".actual
    flake8 --select NIC --exit-zero "$py" >"$actual"
    diff -u "$expected" "$actual"
done
