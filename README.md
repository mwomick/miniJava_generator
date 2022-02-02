# miniJava_generator

A generator that creates miniJava (a subset of Java) files.

## Instructions

To use:

- open your terminal
- `cd` into the directory containing these files
- run `OUT_DIR=/path/to/dir/pa1 FILE_EXT=mjava GEN_NUM=20 python3 __main__.py`

Environment variables:

- `OUT_DIR`: the directory for the output file, default to current directory
- `FILE_EXT`: file extension, default to 'mjava'
- `GEN_NUM`: number of files to be generated, default to '10'

## On the radar

- Beautify whitespace for human readability

## Contributing

### Function Naming Rule

- Functions start with `make` creates a code line or code block, thus accept an indentation as the argument.
- Functions start with `rand` creates a code segment, which is shorter than a line.
