# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
alias gau='git add --update'
alias gca='git commit --amend'
alias gcm='git commit --signoff --message'
alias gcs='git commit --signoff'
alias glo='git log --oneline --graph --decorate'
alias gss='git status --short'
