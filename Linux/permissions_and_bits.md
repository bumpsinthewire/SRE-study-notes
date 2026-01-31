---
title: "permissions_and_bits"
date: "2026-01-13"
type: study_notes
tags: [study, linux]
---

# permissions_and_bits

## Key Concepts

Changing permissions is probably the most common task for a Linux admin

SUID allows users to run an executable with the permissions of its owner

SGID does the same but for both executables and directories

Sticky bit restricts file deletion in a directory

## Commands & Examples

`chown [username]:[group_name] file/directory` is used to change the owner/group of a file/directory  
only `sudo` can do this task

`chgrp [group_name] file/directory` is used to change the group assigned to a file/directory  
can only change to a group that the user is assigned to

`chmod *permissions* file/directory` is used to change the permissions of a file/directory  
there are multiple ways to set permissions.  
`u/g/o/a [=/-/+]` for standard letter convention that shows when listing the file/directory  
using "=" with nothing after it removes all permissions  
`u/g/o [0-7]` for octal values  
4 = read, 2 = write, 1 = execute

SUID is set by either using `chmod` with an "S" or "s" in the user permissions settings or  using a "4" in the octal format (4664 for example)  
"S" means SUID is enabled but there are no execute permissions  
"s" means SUID is enabled and there is execute permissions

SGID is set by either using `chmod` with an "S" or "s" in the group permissions settings or  using a "2" in the octal format (2664 for example)  
"S" means SGID is enabled but there are no execute permissions  
"s" means SGID is enabled and there is execute permissions

You can use `chmod 6xxx` to enable both SUID and SGID

To set the sticky bit, use `chmod +t [directory]` or `chmod 1xxx [directory]`  
"T" means sticky bit is enabled but there are no execute permissions  
"t" means sticky bit is enabled and there is execute permissions

## Questions & Notes

use `groups` to see the groups the current user belongs to

### Parent Note

- [Linux Study Journey](./README.md)
