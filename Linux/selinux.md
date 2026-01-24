---
title: "SELinux"
date: "2026-01-23"
type: study_notes
tags: [study, linux]
---

# SELinux

## Key Concepts

Allows for advanced access restriction above and beyond the basic Linux functionality (like `rwx`)

## Commands & Examples

`ls -Z` will give you the SELinux output for files
    for example - `unconfined_u:object_r:user_home_t:s0`
`ps axZ` will show you the SELinux information for processes
`id -Z` will show you the security context for the current user
`sudo semanage login -l` this will show you the current SELinux settings for users
`sudo semanage user -l` this shows you the various roles that can be assumed by users on the system
`getenforce` shows you the status of SELinux. *Enforcing* means it is actively restricting. *Permissive* is just logging. *Disabled* is not doing anything
`setenforce` lets you change the mode (*1* for Enforcing, *0* for Permissive)
`sestatus` tells you if SELinux is enabled or disabled
`chcon [option] [context] [file]` lets you change the SELinux security context
    `-u` changes the user section
    `-r` changes the role section
    `-t` changes the type section
`seinfo [-u/-r/-t]` shows you the available labels you can use
`sudo chcon --reference=[file_to_copy] [file_to_inherit]` lets you copy SELinux settings from one file to another
`restorecon` restores the *type* section to its default

## Questions & Notes

SELinux is always defined in the order; `user`, `role`, `type`, `level`
    the first 3 are called the "security context"
if you see `unconfined` it means pretty much anything can be done
`/etc/selinux/config` is the persistent file for SELinux settings

### Parent Note

- [Linux Study Journey](./README.md)
