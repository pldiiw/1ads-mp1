#!/bin/sh

echo ----== Testing Breaktrough... ==---- && \
echo \* Type checking... && \
mypy src/breaktrough.py && \
echo =\> Typing is OK ! && \
echo \* Running unit test... && \
python3 -m unittest -v test.breaktrough_testing && \
echo =\> Breaktrough is OK !

echo
echo ----------========================================----------
echo

echo ----== Testing First Attack... ==---- && \
echo \* Type checking... && \
mypy src/first_attack.py && \
echo =\> Typing is OK ! && \
echo \* Running unit test... && \
python3 -m unittest -v test.first_attack_testing && \
echo =\> First Attack is OK !

echo
echo ----------========================================----------
echo

echo ----== Testing Pleiadis... ==---- && \
echo \* Type checking... && \
mypy src/pleiadis.py && \
echo =\> Typing is OK ! && \
echo \* Running unit test... && \
python3 -m unittest -v test.pleiadis_testing && \
echo =\> Pleiadis is OK !
