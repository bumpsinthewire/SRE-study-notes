---
title: "kernel_runtime_parameters"
date: "2026-01-23"
type: study_notes
tags: [study, linux]
---

# kernel_runtime_parameters

## Key Concepts

Runtime parameters are basically settings for how the kernel does its job internally

## Commands & Examples

`sysctl -a` will show you all of the parameters currently in use (add `sudo` to make sure you see all of them)
`sysctl -w [parameter=value]` will set a parameter (non-persistent)
`sysctl [parameter]` will show you the current settings for a parameter
`sysctl -p [parameter setting file]` will enforce the file on your current instance

## Questions & Notes

*0* means False and *1* means True
parameter setting files will be in `/etc/sysctl.d/`
    you can add your own files here as well and the parameters will be persistent

### Parent Note

- [Linux Study Journey](./README.md)
