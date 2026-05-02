# Bandit Level 0

## Goal
Just to log into the game using SSH. Very advanced, I know...

## Commands
`ssh` allows connection to another computer over a network and control it remotely from my terminal

## Takeaways
- `ssh username@hostname` eg. `ssh bandit0@bandit.labs.overthewire.org`
- `ssh -p 2220` to specify the port
- so basically `ssh -p portnumber username@hostname`

## Answer
`ssh -p 2220 bandit0@bandit.labs.overthewire.org`\
`bandit0`

## Additional Info
Using Kali Linux 64-bit on VirtualBox. 
I dont know what any of that means, just that I am using a VM for safety (despite knowing little about the dangers).
