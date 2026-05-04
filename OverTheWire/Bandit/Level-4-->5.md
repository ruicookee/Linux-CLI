# Bandit Level 4 --> 5

## Goal
Find password stored in only human readable file in inhere directory

## Commands
`find`
`type -f`
`-exec`
`file {}`
`grep text`

## Method 1: Manually Checking All File Types
- `type ./-file00`, `type ./-file01`, `type ./-file02`... and so on.....
- for losers who do not wish to have any free time to collect trinkets

## Method 2: Getting Terminal to Print All File Types in Specified Directory
- `find foldername -type f -exec file {} \;`
- `find foldername` searches inside foldername recursively
- `-type f` only shows files and not directories
- `-exec file {} \;`
- `-exec` tells `find` to execute a command on each result
- `file {}` file is the command and {} is the placeholder, kind of like map(lambda x: file x, files)
- `\;` ; normally ends commands in bash but we use escape character \ for find to receive it (this is so strange to me but ok)

## Method 3: Getting Terminal to Print ONLY Files with Text Types
- `find foldername -type f -exec file {} \; | grep text`
- `|` pip sends output of first command into second command
- `grep text` searches for text

## Answer
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
