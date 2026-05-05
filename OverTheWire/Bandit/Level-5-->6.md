# Bandit Level 5 --> 6

## Goal
Find password stored under inhere directory and is human readable, 1033 bytes in size, and not executable

## Commands
`find`
`-type f ! -executable` looking for files that are not executable
`-size 1033c`

## Approach
- too many files to check each one manually, need to use flags to filter it out
- `find inhere -type f ! -executable -size 1033c`

## Takeaways
- `find . -size n` find files that are n bytes
- `find . -size +n` find files that are MORE THAN n bytes
- `find . -size -500c` find files that are LESS THAN n bytes
- `find . -size +n -size -m` find files between n bytes and m bytes
- didnt know they have `!`!!!!!! how fun

## Answer
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
