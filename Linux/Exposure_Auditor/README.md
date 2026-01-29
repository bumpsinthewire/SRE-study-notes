---
title: "Exposure Auditor"
date: "2026-01-28"
type: project
tags: [project, linux]
---

# Exposure Auditor

## Overview

Create a Python script that scans externally accessible ports and makes sure only intended ones are open to the internet

## The Challenge

It is easy to accidentally open a port to the outside world and create a security vulnerability. This script prevents that issue

## The Solution

A Python script that runs `ss -tunlp` and alerts if ports are open that shouldn't be

### Implementation Logic

Parsing the output of `ss` can be a bit messy. Built-in Python methods like `.split()` or the `re` module are helpful here

### Reliability Considerations

Added a `try` `except` block when checking the `ssh` config

## Key Learnings

Data parsing: using `.split()` to handle odd output from `ss`
String manipulation: `rsplit(':', 1)` to isolate port numbers
Configuration checking: adding logic to ignore commented-out lines

## Code Implementation

- [exposure_auditor](./exposure_auditor.py)

## Results

```bash
$ python3 exposure_auditor.py
--- NETWORK EXPOSURE AUDIT ---

[+] Checking Listening Ports...
[!] ALERT: UNRECOGNIZED PORT EXPOSED: 546
[!] ALERT: UNRECOGNIZED PORT EXPOSED: 68
[!] ALERT: UNRECOGNIZED PORT EXPOSED: 53
[!] ALERT: UNRECOGNIZED PORT EXPOSED: 67
[!] ALERT: UNRECOGNIZED PORT EXPOSED: 8080

[+] Checking SSH Configuration...
[-] NOTICE: SSH Policy is set to DEFAULT.
```

### Parent Note

- [Linux Study Journey](../README.md)
