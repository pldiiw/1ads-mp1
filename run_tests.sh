#!/bin/sh

echo ----== Testing Breaktrough... ==---- && \
echo -n \* Type checking... && \
mypy src/breaktrough.py && \
echo \ OK! && \
echo \* Running unit test... && \
python3 -m unittest -v test.breaktrough_testing && \
echo =\> Breaktrough is OK!

echo
echo ----------========================================----------
echo

echo ----== Testing First Attack... ==---- && \
echo -n \* Type checking... && \
mypy src/first_attack.py && \
echo \ OK! && \
echo \* Running unit test... && \
python3 -m unittest -v test.first_attack_testing && \
echo =\> First Attack is OK!

echo
echo ----------========================================----------
echo

echo ----== Testing Pleiadis... ==---- && \
echo -n \* Type checking... && \
mypy src/pleiadis.py && \
echo \ OK! && \
echo \* Running unit test... && \
python3 -m unittest -v test.pleiadis_testing && \
echo =\> Pleiadis is OK!
