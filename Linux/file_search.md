---
title: "file_search"
date: "2026-01-13"
type: study_notes
tags: [study, linux]
---

# file_search

## Key Concepts

Since Linux is one giant filesystem tree, search is extremely useful

## Commands & Examples

`find [path_to_directory] [search_parameters]`
    `-name` find file with a specific name (`-iname` to ignore case sensitivity)
    `-mmin [minute]` modified in the last [minute]
        this syntax can be confusing
        "5" would be exactly 5 mins ago including the current minute (run at 12:05 and get results from 12:01)
        "-5" would be the last 5 mins (run at 12:05 and get results from 12:05 to 12:01)
        "+5" would be the previous 6 mins because the count skips the current time (run at 12:05 and get results from 12:00 and earlier)
    `-mtime [number]` is for 24 hour chunks. "0" is for last 24 hours. "1" is from 24-48 hours ago
    `-cmin [number]` search for changes during a window (same syntax as `-mmin`)
    `-size [size]` add "c" for bytes, "k" for kilobytes, "M" for megabytes, "G" for gigabytes
    `-perm [permissions]`
        "664" will find files with exactly those permissions.
        "-664" will find files with at least those permissions
        "/664" will find files with any of those permissions
        can use the standard notations as well (u=rw,g=rw,o=r)

## Questions & Notes

Think "go there and then find it" to remember the `find` syntax
If you have multiple parameters, there is an implied AND operator. Use `-o` for OR operator. Use `-not` for NOT operator (can also use `\!`)
