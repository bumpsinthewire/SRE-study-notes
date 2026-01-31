---
title: "system_documentation"
date: "2026-01-09"
type: study_notes
tags: [study, linux]
---

# system_documentation

## Key Concepts

Various methods for referencing built-in documentation

## Commands & Examples

`--help` is the most common one. gives a small output with most common flags (options)  
`journalctl --help`

`man` is a more comprehensive breakdown. gives a synopsis, then syntax, then a description and sometimes examples  
`man journalctl`  
if you need a certain section (look the sections up with `man man`) then you can do something like `man 1 printf`

`apropos` lets you search for commands that contain a word. if it not loading then run `sudo mandb` to update the db that `apropos` uses  
`apropos director`  
you can also filter by section by doing something like `apropos -s 1,8 director`

## Questions & Notes

commands will be in sections 1 and 8 of the `man` pages. sometimes `apropos` will return ones from other sections

## Resources

[Linux man pages](https://linux.die.net/man/)  
[Linux man pages online](https://man7.org/linux/man-pages/)

### Parent Note

- [Linux Study Journey](./README.md)
