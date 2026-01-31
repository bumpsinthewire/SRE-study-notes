---
title: "storage_performance"
date: "2026-01-30"
type: study_notes
tags: [study, linux]
---

# storage_performance

## Key Concepts

Just like CPU and RAM, Linux has utilities for monitoring storage performance

## Commands & Examples

`iostat` historical usage of storage devices  
`[number]` shows the usage at every `number` interval  
`-h` makes the output more human-readable (also adjusts the output so you don't have to convert m to g for example)

`pidstat` shows statistics for processes  
`-d` shows which devices are being used by processes  
`[number]` shows the usage at every `number` interval

`dmsetup` used for low level LV management/information

## Questions & Notes

`sudo apt install systat` contains system statistic utilities  
`iostat` and `pidstat` are the 2 that we are looking at here

### Parent Note

- [Linux Study Journey](./README.md)
