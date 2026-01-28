---
title: "networking"
date: "2026-01-27"
type: study_notes
tags: [study, linux]
---

# networking

## Key Concepts

Networking is all about connecting
Linux has many built-in utilities for doing various things related to networking

## Commands & Examples

`ip` is the main utility for managing IPs in Linux and has A LOT of options
    `link` information about interfaces but also lets you manage them
        `ip link set dev [int] up/down` turns up/down an interface
    `address` or `addr` or `a` shows IP information for your interfaces
        `-c` will *color* the output (use this option **BEFORE** the second command)
        `ip addr add/del [ip/mask] dev [int]` adds/removes an IP for an interface

`netplan get` will show you the current system network settings
    custom `netplan` files should be in the format of *[number]-[name].yaml*
`netplan apply` immediately applies `netplan` changes (risky)
`netplan try` gives a countdown and will revert if nothing is pressed (failsafe)
    `--timeout` customize the countdown timer
    `try` will also warn you about syntax errors

`ip route` will show you the configured routes on your system

`resolvectl [option]` shows you information about your configured DNS settings/servers
`/etc/systemd/resolved.conf` holds system-wide DNS settings
`/etc/hosts` is a file that lets you set up static hostname resolution

`ss` is the modern replacement for `netstat`
`ss -tunlp` *TCP*, *UDP*, *numeric values*, *listening*, *processes*
    shows what is listening for incoming connections

## Questions & Notes

using the `ip` utility is for non-persistent changes
`netplan` is the default networking tool for Ubuntu
    it reads a configuration file and then translates that into network settings
    files are stored in `/etc/netplan/`
    files are processed in alphabetical order (hence putting the numbers in front)

## Resources

`usr/share/doc/netplan/examples` is full of example `netplan` *yaml* files

### Parent Note

- [Linux Study Journey](./README.md)
