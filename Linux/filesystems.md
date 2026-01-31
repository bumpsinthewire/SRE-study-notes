---
title: "filesystems"
date: "2026-01-29"
type: study_notes
tags: [study, linux]
---

# filesystems

## Key Concepts

Linux has multiple utilities for creating and modifying filesystems

## Commands & Examples

`mkfs.[filesystem] [disk]` is the simplest utility for making a filesystem  
`xfs_admin [option] [filesystem]` lets you modify already existing filesystems  
`-l` displays the label  
`-L` lets you change the label  
`mount [options] [filesystem] [mount_location]` mounts a filesystem to a specified location  
`-o` to add options like "ro" or "rw" (read-only, read-write). Separate by commas for multiple  
add "remount" if you are changing options and don't want to unmount/mount again  
`umount [mount_location]` to unmount a filesystem from a specified location  
`lsblk` can be used to see where filesystems are mounted as well  
`/etc/fstab` is the system-wide config file where you can specify mount options for filesystems at or during boot  
first column: block device file (partition or storage space)  
second column: mount point  
third column: filesystem type  
fourth column: mount options  
like "ro", "rw", "noexec", "nosuid". Separate by commas for multiple  
fifth column: if "dump" should be used (0 is disabled, 1 is enabled). rarely used so can be set to 0  
sixth column: what happens when errors are detected (0 - never be scanned for errors, 1 - priority to be scanned, 2 - to be scanned after priority ones)  
usually use 1 for root filesystem and 2 for all others  
use `systemctl daemon-reload` to apply the changes in `/etc/fstab`  
for a *swap* space, use `none` in field 2, `swap` in field 3, and `0` in fields 5 and 6  
`blkid [disk]` to see the UUID of a block device  
`findmnt` use to get information about a mounted filesystem (including options)  
`-t` to filter by type and clean up the large output that you see with no options

## Questions & Notes

Redhat uses `xfs` filesystems by default  
Ubuntu uses `ext4` filesystems by default  
if you just type `mkfs.[filesystem_type]` with no options it will bring up a pseudo help page  
you have to `mount` a filesystem to a directory to be able to use it

### Parent Note

- [Linux Study Journey](./README.md)
