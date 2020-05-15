#!/bin/bash
set -eu

dir=$(dirname $0)
cd "$dir"

echo Target files: files/*.py
for py in files/*.py
do
    echo Checking $py result
    expected="$py".expected
    actual="$py".actual
    flake8 --select NIC --exit-zero "$py" >"$actual"
    diff -u "$expected" "$actual"
done
