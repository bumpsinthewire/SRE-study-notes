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

*(What did you add to make the script "harder to break")*

## Key Learnings

*(What you learned from this project)*

## Code Implementation

*(Links to code files and explanations)*

## Results

*(Outcomes and impact)*

*(Add a screenshot or code block showing the output of the script)*

### Parent Note

- [Linux Study Journey](../README.md)
