---
title: "advanced_permissions"
date: "2026-01-30"
type: study_notes
tags: [study, linux]
---

# advanced_permissions

## Key Concepts

Access Control Lists (ACLs) can be used to get really granular with file permissions

## Commands & Examples

`setfacl` lets you work with file ACLs  
`-m` modify the current ACL on a file (`-m user:alex:rw [file]`)  
`-x` remove an ACL from a file  
`-b` remove ALL ACLs  
`-R` apply what you are doing *recursively*  

`getfacl [filename]` shows the ACL on a file

`chattr [filename]` lets you change attributes on a file  
use "+" and "-" to add/remove  
"a" for "append"  
"i" for "immutable"  

`lsattr [filename]` will show you the configured attributes for a file/directory

## Questions & Notes

`sudo apt install acl` to install the package to allow for using ACLs  
if you see a "+" sign at the end of the permissions string for a file, that means there is an *facl* set

## Resources

`man chattr` *man* page for the `chattr` command

### Parent Note

- [Linux Study Journey](./README.md)
