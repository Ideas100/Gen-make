# Gen-make
Generate-Makefile [ gen-make ], a script that generate's basic Makefile.
The goal is to learn more about gnu make for writing more simpler rules.

## Installation:

### direct install:

```pip3 install gen-make```

or 

### clone and install:

```cd Gen-make/```

```pip3 install . ```

### Command usage:

```gen-make [OPTIONS]```

## Design:

script :
   - handles argument's from terminal.
   - creates Makefile in current directory.
do_makefile:
   - get info about from the given directory.
   - write rules using the info.

## Gen-make argument's :

```-H <path>```: adding header file path

```-s <path>```: adding source file path

```-o <path>```: target or executable file name

```-l <path>```: adding linker library

```-v ```      : modify the output verbosity

## Test run:

Creating Makefile for the test directory file,
* ``` cd test/ ```
* ``` gen-make -v```
or
* ``` gen-make -H test/ -s test/ -v ``` 

### Tic-Tac-Toe

Tried generating Makefile for previous project.

```gen-make -H include/ -s src/ -o tic-tac-toe -l lncurses -v```
  
Check the commit of those repository.
