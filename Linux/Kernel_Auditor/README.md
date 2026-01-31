---
title: "Kernel Auditor"
date: "2026-01-26"
type: project
tags: [project, linux]
---

# Kernel Auditor

## Overview

Create a Python script that uses `sysctl -n [parameter]` to obtain the configured value of specific parameters    
Additionaly validates SELinux mode

## The Challenge

Instead of manually going through and checking a list of parameters, this will check automatically and tell you which ones are not in compliance

## The Solution

A Python script that loops through a dictionary of parameters and their expected values  
Prints the command to fix any parameters that do not meet the expected setting  
Validates the mode of SELinux

### Implementation Logic

Python provided the ability to loop over a dictionary that contains the parameter name as well as the expected value and then verify it

### Reliability Considerations

Chose running `sysctl -n [parameter]` to obtain values instead of going down the file path  
less cleanup/validation needed this way

## Key Learnings

reinforced that you **always** have to use `stdout.strip()` on the return object from the `subprocess` output

## Code Implementation

- [kernel_auditor](./kernel_auditor.py)

## Results

```bash
$ python3 kernel_auditor.py
The value for net.ipv4.ip_forward does not match the desired state!
Please use: 'sysctl -w net.ipv4.ip_forward=0' to fix
The value for kernel.perf_event_paranoid does not match the desired state!
Please use: 'sysctl -w kernel.perf_event_paranoid=2' to fix

--- SUMMARY ---
Parameters in compliance: 3/5

WARNING: SELinux is Permissive. Expected Enforcing
```

### Parent Note

- [Linux Study Journey](../README.md)
