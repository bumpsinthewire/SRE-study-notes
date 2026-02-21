---
title: "resource_limits_and_privileges"
date: "2026-01-26"
type: study_notes
tags: [study, linux]
---

# resource_limits_and_privileges

## Key Concepts

Linux allows you to impose limits on the resources users can use

## Commands & Examples

For managing user limits:  
`<domain>, <type>, <item>, <value>` is the syntax for the `limits.conf` file that defines user limits  
`domain` can be either a *username*, *group* (using @groupname), or * for *all*  
`type` can be *hard*, *soft*, or *-*  
*hard* can NOT be overwritten  
*soft* is an initial value and the user can increase to the *hard* limit  
*-* is both hard and soft limit. meaning the user can use up to the hard maximum  
`item` and `value` go together and are the resource and its value that you want to limit it to  
`nproc` is for *number of processes*  
`fsize` is for file size in kilobytes  
`cpu` sets the limit for the CPU time  
`ulimit` is used to see and control user limits  
`-a` shows the current set limits for the user  
the rest of the flags allow you to set limits directly

For managing user privileges:  
`sudo gpasswd -a [user] sudo` adds a user to the *sudo* group (don't need to enter the *sudo* password every time)  
`visudo` is how you edit the `/etc/sudoers` file

Example for allowing all *sudo* group members to execute ANY command  
%sudo ALL=(ALL:ALL) ALL  
first is user/group - %sudo (% is needed only for a group)
second is the hostname - ALL=  
third is "run as user/group" but is optional - (ALL:ALL)  
    use (sudo) to run as root
last is the commands - ALL  
you can also do `NOPASSWD:ALL` if you want to run every command as *sudo* with NO password
    if you want to run a single command then you must do `NOPASSWD:` followed by a space and then the command
    keep in mind that you sometimes have to define the location too for something like `/bin/bash` to run a `bash` command

## Questions & Notes

limits can be defined in the `/etc/security/limits.conf` file

### Parent Note

- [Linux Study Journey](./README.md)
