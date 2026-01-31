---
title: "search_and_manipulate_file_content"
date: "2026-01-14"
type: study_notes
tags: [study, linux]
---

# search_and_manipulate_file_content

## Key Concepts

There are many ways to view and manipulate content in Linux

## Commands & Examples

`cat [directory/filename]` outputs the text in a file  
`tac` outputs the text from the bottom up

`tail [directory/filename]` shows you the last 10 lines of a file by default  
`-n *number*` lets you define how many lines you want to see

`head [directory/filename]` is the opposite of tail (`-n` also works for this command)

`sed` stands for "stream editor" and lets you change a pattern within a file  
`sed 's/canda/canada/g' userinfo.txt` this example changes all instances ("g" at the end is for global) of "canda" to "canada"  
default behaviour without the "g" just changes the first occurence on each line  
you MUST use `-i` (--in-place) to actually make the changes. if you do not use it, the output just shows you what would change

`cut` lets you extract parts from a file  
`cut -d ' ' -f 1 userinfo.txt` the "-d" is for "delimeter" and defines how you want to separate fields. the "-f" is for which field you want  
`cut -d ',' -f 3 userinfo.txt > countries.txt` extracts countries in the third field separated by a ","

`uniq` removes repeating lines that are right next to each other  
`sort` orders output alphanumerically  
`sort countries.txt | uniq` these utilities are often used together like this

`diff [file1] [file2]` lets you see the differences between files

`less [filename]` is a pager. this lets you use navigation commands and search on the output  
`more [filename]` another pager with similar functionality to `less` but actually has "less" features

## Questions & Notes

Sed patterns should be wrapped in single quotes ('') to prevent bash from interpreting special characters

### Parent Note

- [Linux Study Journey](./README.md)
