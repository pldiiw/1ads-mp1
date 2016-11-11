#!/bin/sh

echo Testing Breaktrough... && \
echo Type checking... && \
mypy src/breaktrough.py && \
echo Typing is OK ! && \
echo Running unit test... && \
python3 -m unittest -v test.breaktrough_testing
