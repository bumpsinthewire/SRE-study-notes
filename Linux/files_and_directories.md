---
title: "files_and_directories"
date: "2026-01-13"
type: study_notes
tags: [study, linux]
---

# files_and_directories

## Key Concepts

Thinking of everything in Linux as an inverted filesystem tree is helpful for navigation

## Commands & Examples

`ls` let's you list files. There are lots of flags available
    `-a`: shows hidden files
    `-l`: "long" listing. shows you additional information like permissions, timestamps, etc.

`pwd` outputs the current directory that you are in

`cd` is for "change directory"
    `cd /` will go to root.
    `cd -` will go to the previous directory

`touch` can be used to create a new file (or modify a timestamp if the file already exists)

`cp [source] [destination]` is for copying
    `-r` is for recursively copying a directory and it's content

`mv [source] [destination]` is for moving a file (also for renaming)
    `mv` recursively moves automatically

`rm` is for removing files/directories
    `-r` must be used to recursively delete

### Parent Note

- [Linux Study Journey](./README.md)
