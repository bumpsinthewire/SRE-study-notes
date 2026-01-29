---
title: "partitions_and_swap_space"
date: "2026-01-29"
type: study_notes
tags: [study, linux]
---

# partitions_and_swap_space

## Key Concepts

Partitions are simply just the pieces that remain when you split a disk
Swap space is a partition that you can temporarily use as RAM

## Commands & Examples

`lsblk` shows you all of the *block* devices on your system
    there will be a *tree* output for partitions on those *blocks*
`fdisk` allows you to display or manipulate partition tables
    `--list [disk]` gives you info about a specific block and its partitions
`cfdisk [disk]` is a GUI based `fdisk`
`swapon` utility for managing swap space
    `--show` shows information about any swap spaces on your system
    `--verbose [disk]` shows swap information about a partition
`mkswap [disk]` sets up a Linux swap area
`swapoff [disk]` turns off swap for a partition

## Questions & Notes

you can also use the `dd` utility to make a partition into a swap space
    `dd if=/dev/zero of=/swap bs=1M count=128 status=progress`

### Parent Note

- [Linux Study Journey](./README.md)
