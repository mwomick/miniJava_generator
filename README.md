# miniJava_generator

A generator that creates miniJava (a subset of Java) files.

## Instructions

To use:

- open your terminal
- `cd` into the directory containing these files
- run `OUT_DIR=/path/to/dir/pa1 FILE_EXT=mjava GEN_NUM=20 python3 __main__.py`

## On the radar

- finish implementation, to speak generally
- beautify whitespace for human readability

## Contributing

### Function Naming Rule

Functions that start with `make` creates a code line or code block, thus accept an indentation as the argument.

Functions that start with `rand` creates a code segment, which is shorter than a line.
