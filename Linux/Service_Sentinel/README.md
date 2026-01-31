---
title: "Service Sentinel"
date: "2026-01-19"
type: project
tags: [project, linux]
---

# Service Sentinel

## Overview

Create a Python script that will use `systemctl` to verify status of a service and auto-restart if it is down

## The Challenge

Critical services (like a web server) can crash, and manual restarts cause downtime

## The Solution

A Python script that checks service status and auto-restarts

### Implementation Logic

Python was chosen over Bash because of the easier handling of input variables as well as logging and error handling

### Reliability Considerations

Logging to pinpoint any issues and error handling for input validation

## Key Learnings

the `subprocess` module expects a *list* of arguments. you can use `shell=True` to bypass this in the `subprocess.run()` command  
security best practices recommend using a *list* though to prevent injection vulnerabilities  
the output of the `subprocess` command is a *CompletedProcess Object* so you must use `stdout` to use the `strip` function on it

## Code Implementation

- [Service Sentinel](./service_sentinel.py)

## Results

```bash
$ cat sentinel.log
[2026-01-21 20:28:41] ALERT: nginx is inactive. Attempting restart.
[2026-01-21 20:28:41] RECOVERY: nginx restart attempted. New status: active
```

### Parent Note

- [Linux Study Journey](../README.md)
