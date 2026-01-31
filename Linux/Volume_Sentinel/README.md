---
title: "Volume Sentinel"
date: "2026-01-31"
type: project
tags: [project, linux]
---

# Volume Sentinel

## Overview

Python script that checks LVs on your system and resizes them if they are running out of space

## The Challenge

There are a lot of different utilities and commands for verifying the size of LVs and VGs

## The Solution

This script cleans up all of the output and adds some logic that intelligently resizes based on defined criteria

### Implementation Logic

Being able to use the `subprocess` and `shutil` modules make this a lot easier than cleaning and parsing `bash` output

### Reliability Considerations

Replacing the "<" and "g" in the output so that it can be read properly

## Key Learnings

First time using the `shutil` module. It is very straightforward compared to others I have been using
Realizing you can continue to use methods on the same variable

## Code Implementation

- [Volume Sentinel](./Volume_Sentinel/volume_sentinel.py)

## Results

```python3
$ python3 volume_sentinel.py

Storage Health: /dev/ubuntu-vg/ubuntu-lv is at 20.88%.
```

### Parent Note
- [linux Study Journey](../README.md)
