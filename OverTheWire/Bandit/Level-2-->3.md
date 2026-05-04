# Bandit Level 2 --> 3

## Goal
Find password stored in a file called --spaces in this filename-- located in the home directory

## Commands
`ls` to see what files exist\
`cat` to print file contents\
`./` or `--` escape characters

## Problem Encountered
- `ls` is perfectly able to see the file `--spaces in this filename--`
- `ls -b` reveals `--spaces\ in\ this\ filename--`
- `cat "--spaces in this filename--"` fails because argument still start with -- so it still tries to parse

## Takeaways
- `cat ./--spaces\ in\ this\ filename--` works because ./ forces it to be treated as path and \ escapes the spaces
- `cat -- "--spaces in this filename--"` works because -- means end of options

## Answer
MNk8KNH3Usii041PRUEoDFPqfxLPLSmx
