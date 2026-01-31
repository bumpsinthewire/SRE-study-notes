---
title: "Log Parser"
date: "2026-01-21"
type: project
tags: [project, linux]
---

# Log Parser

## Overview

Python script that uses RegEx to parse logs and find IPs that are creating errors (as well as counting them)

## The Challenge

Scanning `/var/log/syslog` manually for errors is inefficient and prone to human error

## The Solution

A Python script using Regular Expressions (regex) to identify and count error patterns

### Implementation Logic

Python's `re` module is much easier to use than trying to search with standard Linux commands and regex

### Reliability Considerations

Added a `try/except` block in case the log file does not exist

## Key Learnings

An easier way to use regex with the `re` module  
built-in `collections.Counter` for handling frequency mapping without manual `if/else` *dict* logic  
`typing` module can be used to specify types for data structures for easier readability and intention   

## Code Implementation

- [Log Parser](./log_parser.py)

## Results

```bash
❯ python3 log_parser.py
--- SSH Attack Report ---
IP Address         | Attempts
------------------------------
192.168.1.50       | 2
10.0.0.5           | 1
```

### Parent Note

- [Linux Study Journey](../README.md)
