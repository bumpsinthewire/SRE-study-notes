---
title: "resources_and_processes"
date: "2026-01-22"
type: study_notes
tags: [study, linux]
---

# resources_and_processes

## Key Concepts

There are many tools available for seeing how processes are using the resources on a system

## Commands & Examples

`df` will tell you how much "disk-free" is on all of your filesystems
    `-h` makes the output more "human-readable"

`du [filesystem]` will show you how much disk space is being used by a specific directory
    `-s` is for summaryize
    `-h` makes the output more "human-readable"

`free` will show you how much RAM is available
    `-h` makes the output more "human-readable"

`uptime` tells you the uptime for your system as well as the load on the CPU

`lscpu` gives you additional information about the CPU(s) on your system

`lspci` gives you additional information about the PCI slots on your system

`sudo xfs_repair -v [filesystem]` gives you verbose (-v) detail about the filesystem
`sudo fsck.ext4 -v -f -p [filesystem]` gives you verbose (-v) output, forces (-f) the detail even if the filesystem says it is healthy, and auto repairs (-p, or "preen" mode)

## Questions & Notes

Ubuntu uses the *ext4* filesystem by default
Redhat uses the *xfs* filesystem by default

### Parent Note

- [Linux Study Journey](./README.md)
