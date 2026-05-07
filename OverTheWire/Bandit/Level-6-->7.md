# Bandit Level 6 --> 7

## Goal
Find password stored somewhere on server that is owned by user bandit7, owned by group bandit6, 33 bytes in size

## Commands
`find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`\
`2>/dev/null` throws away error (permission denied) messages\
0 = stdin   (input)\
1 = stdout  (normal output)\
2 = stderr  (errors)
`>` send files somewhere
`/dev/null` is the blackhole


# MANY TAKEAWAYS
## Takeaway 1
If you SSH into bandit6@bandit.labs.overthewire.org
- u are purely bandit6
- u can go to home and see bandit7 (which is not even a user btw, `ls -l /home` to find out that it is actually a directory) but you cannot have permission to cat its stuff
- `whoami` i and `pwd` will prove that
## Takeaway 2
If you `cd .. into` home you may be able to see bandit7 
- BUT the files that it owns may live ELSEWHERE
- so in this case i could only find data.txt in bandit7's directory
- but it also owns /var/lib/dpkg/info/bandit7.password, where the actuall password is
## Takeaway 3
Some New Commands
- `ls -l` lets you see permissions to a particular file or directory
- `find /` lets you search entire filesystem
## Takeaway 4 
- `su user` or `ssh user@localhost` can move you to another user on the same puter

## Answer
morbNTDkSW6jIlUc0ymOdMaLnOlfVAaj
