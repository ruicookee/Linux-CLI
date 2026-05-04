# Bandit Level 3 --> 4

## Goal
Find password stored in hidden file in the `inhere` directory

## Commands
`ls -R -a` to see dig deeper and see all files
`cat` to print file contents\

## Process
- `ls -R -a` lists directories and their contents recursively, and reveals hidden files too
- found file ...Hiding-From-You
- `cat ...Hiding-From-You` prints filecontents just fine

## Takeaways
- `ls -R -a` you can stack multiple of those - thingies (called command line options or flags)
- get comfortable with those
- [ls manual](https://man7.org/linux/man-pages/man1/ls.1.html)
- you need to type the leading dot to access hidden files

## Answer
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
