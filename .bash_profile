# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

if [ "$PS1" ]; then
  PS1="[\[\e[01;31m\]\t\[\e[00m\] \[\e[01;32m\]\u@\h\[\e[00m\] \[\e[01;34m\]\W\[\e[00m\]]\$ "
fi

PATH=$PATH:$HOME/.local/bin:$HOME/bin:$HOME/go/bin

export PATH

anniversary.py
weight.py
