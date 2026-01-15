---
title: "input-output_redirection"
date: "2026-01-14"
type: study_notes
tags: [study, linux]
---

# input-output_redirection

## Key Concepts

Linux allows you to redirect both input and output streams to a location of your choosing
There are three things to know here: 
    "stdin" (<) is for standard input
    "stdout" (1>) is for standard output
    "stderr" (2>) is also for output but for errors

## Commands & Examples

`>` is used for output redirection. This overrides what is currently in there
`>>` is used to append output to the end of a file

`grep -r '^The' /etc/ 2>/dev/null` /dev/null is the standard "bitbucket" to send things you don't want/need
`grep -r '^The' /etc/ 1>output.txt 2>errors.txt` redirects stdout to output.txt and stderr to errors.txt
`grep -r '^The' /etc/ > all_output.txt 2>&1` redirects everything on the screen to all_output.txt

`|` allows you to send the output from one utility into another
    `grep -v '^#' /etc/login.defs | sort | column -t` sort the grep output and arrange in columns

## Questions & Notes

Since there are two types of output, you can append the ">" with 1 or 2 depending on what you want to output (stdout or stderr)
stdout is the default so it's uncommon to use "1>"
