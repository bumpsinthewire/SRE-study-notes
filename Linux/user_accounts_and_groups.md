---
title: "user_accounts_and_groups"
date: "2026-01-26"
type: study_notes
tags: [study, linux]
---

# user_accounts_and_groups

## Key Concepts

There are many built-in ways to modify users and their groups

## Commands & Examples

For managing users:  
default user configs are stored in the `etc/skel` directory  
`cat /etc/passwd` shows you information about all of the users on the system as well as their groups and shell/home directory  
`adduser [name]` creates a user  
you will be prompted for additional information such as a password  
`--shell [/bin/shell_you_want]` sets the default login shell for the user  
`--home [home_directory_you_want]` allows you to define the home directory for a new user  
`--uid [number] [name]` assigns a specific ID to a user  
`--system --no-create-home [name]` creates a system account with no home directory  
`passwd [name]` allows you to change the password for a user  
`deluser [name]` will delete a user  
`--remove-home` also deletes the home directory of a user  
`id` gives all of the information about the current user (groups, ID's)  
`whoami` outputs the name of the current user  
`usermod [option] [name]` lets you modify settings for an account  
`-d [new_home]` OR `--home` lets you change the location of the *home* directory (should be used with `-m` to also *move* to this new directory)  
`-l [new_name]` OR `--login` lets you change the name of a user  
`-s [new_shell]` OR `--shell` lets you change the shell  
`-L` OR `--lock` to lock an account  
`-U` OR `--unlock` to unlock an account  
`-e [Y-M-D]` OR `--expiredate` to set an expiration date for an account  
set a previous date to expire immediately  
specify an empty date with "" to remove an expiration  
`chage` specifies when you want the user's password to expire  
`-d [number]` OR `--lastday` sets the password to immediately expire  
`-M [number]` OR `--maxdays` specifies how long a password is good for  
setting this to -1 makes it never expire  
`-l` OR `--list` shows when a password is set to expire  
`-W [number]` OR `--warndays` to set a warning before a password expires

For managing groups:  
`groupadd [name]` creates a new group  
`groupdel [name]` deletes a group  
`gpasswd` is historically used to create a password for a group but that is rarely done today. Now it is the quickest way to add a user to a group  
`-a [user] [group]` OR `--add` adds a user to a group  
`-d [user] [group]` OR `--delete` deletes a user from a group  
`groups [username]` shows which groups a user belongs to  
`groupmod [option] [group_name]` lets you modify settings for a group  
`-n [new_name] [old_name]` OR `--new-name` changes the name of a group  
`usermod -g [group_name] [username]` OR `--gid` can be used to change the primary group of a user  
`usermod -G [group_name] [username]` OR `--groups` can be used to change the secondary group of a user  
`-a -G` appends (instead of changes) a user to a secondary group

## Questions & Notes

system accounts usually have ID's smaller than 1000  
expiring an account completely disables it. expiring a password makes the user set a new password next time they log in  
*REMEMBER* that `gpasswd` and `usermod` flip the order of *user* and *group*

### Parent Note

- [Linux Study Journey](./README.md)
