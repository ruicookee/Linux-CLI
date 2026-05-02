# Bandit Level 1 --> 2

## Goal
Find password stored in a file called - in home directory\
Working with dashed filename, which are usually interpretted as a command

## Commands
`ls` to see what files exist\
`cat` to print file contents\
`./` or `--` escape characters

## Process
- ls to see what files are in current directory (flat view)
- `-` is within same directory
- need escape character `./` or `--`

## Takeaways
use `cat ./-filename` or `cat -- -filename`\
the former being the safest version

## Answer
263JGJPfgU6LtdEvgfWU1XP5yac29mFx
