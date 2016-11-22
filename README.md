# 1ADS-MP1

## Synopsis

This repository is the result of the work I put into the SUPINFO's home work
project, 1ADS-MP1, where students were asked to reproduce in Python three little
pawns games, namely Breaktrough by Dan Troyka, Frank Harary's First Attack and
2002's Pleiadis by Christian Watkins in cooperation with Jan Kristian Haugland.

## Followed Guidelines

This project was an opportunity for me to experiment some concepts I read about
and curious to see in action.

### Clarity
First things first, a huge emphasis was put into clarity of code. Statistics
saying that [developers spend about 70% of their time reading other people
code][stat], considering the reading experience should be a priority for
everyone. This translate here as the most descriptive doctrings as possible,
inline comments when things get a bit obfuscated, extensive variable and
function naming and straight-to-the-goal statements.

### [Functional Programming][fp]
The use of a functional programming-like approach also helped. Apart from IO
and lists' side-effect-loving element modifications, functions tries to be as
pure as possible. This approach results in a lot of functions being defined, for
the majority short ones, bringing higher abstraction in the code as a whole.

### [Function Annotation][funcannon]

### Testing
You will see a *test* directory. This directory contains a test suite for each
one of the games. This practice let me write my sources files and afterwards
check every written functions if they produce the results I expect from them. It
prevented many unseen bugs in the whole writing process and saved time in ingame
testing.

### [PEP-8][pep8] and Code Linting
Standards are meant to be followed. It helps developers find their marks
quicker by bearing consistency across projects. It goes hand in hand with
clarity. I tried to follow the PEP-8 as close as possible and used the
[pylint][pylint] tool to lint the code to avoid syntax mistakes.

### Git
The version control software Git is a tool that became unavoidable in the IT
world. Except for the fact that I use it on a everyday basis, the bias to use it
on this project was to have a more organized workflow and keep track of how I
managed to accomplish the writing of the 3 games. [This repository is also
hosted on GitHub if you're willing to explore the repository in a pleasant
way.][gh]

## Project Hierarchy

All games source files can be found under the `src` directory. 
Tests source files are under the `test` directory.

## Installation

Requires Python 3.5+.

Clone repository

    git clone https://github.com/pldiiw/1ads-mp1.git

Run one of the game

    python3 src/<game_file> <parameters>

Running a game with no parameters will display the help and expected parameters.

## Tests

If you're willing to, you can run the test suite.

Requires mypy. If don't have it, just run:

    sudo pip3 install mypy-lang

Run the test script

    ./run_tests.sh

## License

This repository is under the Unlicense. See the LICENSE for more information.
Keep in mind that the final version (tagged as v1.0.0) delivered to SUPINFO is
automatically licensed under the [FreeBSD][freebsd] to SUPINFO International
University.

[fp]: https://en.wikipedia.org/wiki/Functional_programming
[stat]: https://github.com/getify/Functional-Light-JS/blob/master/ch1.md#communication
[pep8]: https://www.python.org/dev/peps/pep-0008/
[pylint]: https://www.pylint.org/
[freebsd]: https://en.wikipedia.org/wiki/BSD_licenses#2-clause
[funcannon]: https://www.python.org/dev/peps/pep-3107/
[gh]: https://github.com/pldiiw/1ads-mp1
