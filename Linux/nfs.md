---
title: "nfs"
date: "2026-01-30"
type: study_notes
tags: [study, linux]
---

# nfs

## Key Concepts

The Network File Systemt protocol (NFS) lets you use a remote filesystem as if it was local  
Similar to [ssh](./ssh.md), NFS uses a client-server model

## Commands & Examples

`/etc/exports` is the config file for NFS  
column 1: path to directory we want to share  
column 2: who or what can access the share (hostname/IP/subnet) and add options in ()  
wildcard can be used as well *  
if you have multiple, separate by a space  
`/srv/homes hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)`  
*sync* is for "synchronous writes" and *async* is for "asynchronous writes"  
*no_subtree_check* is for disabling subtree checking. this option is the default and will be used even if not specified  
*no_root_squash* carries over *root* privleges to the NFS  
`exportfs` lets you work with exported filesystems  
`-r` "re-export". basically does a refresh based on the `/etc/exports` file  
`-v` detailed output for your exports (including options)

`mount [IP/hostname]:path_to_remote_directory path_to_local_directory` mount a NFS  
in `/etc/fstab` use something like `127.0.0.1:/etc /mnt nfs [options] 0 0`

## Questions & Notes

`sudo apt install nfs-kernel-server` to install NFS server package  
`sudo apt install nfs-common` to install NFS client package

## Resources

`man exports`

### Parent Note

- [Linux Study Journey](./README.md)
