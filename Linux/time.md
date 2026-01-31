---
title: "time"
date: "2026-01-28"
type: study_notes
tags: [study, linux]
---

# time

## Key Concepts

Keeping time is very important in Linux. You really do not want drift when you are worried about logs and cron jobs for example

## Commands & Examples

`timedatectl` is the way you interact with `systemd-timesyncd`  
`list-timezones` shows you all of the available timezones  
`set-timezone [timezone]` sets a specific timezone  
using just `timedatectl` will give you an overview of the current system settings  
`set-ntp [true/false]` to turn NTP on or off  
`show-timesync` will show your configured NTP servers  
`timesync-status` gives detailed information about your NTP configurations  
use the file at `/etc/systemd/timesyncd.conf` to add NTP servers (spaces in between)

## Questions & Notes

`systemd-timesyncd` is the `systemd` utility for time management in Ubuntu  
might need to install it with `sudo apt install systemd-timesyncd`  
there is also a config file at `/etc/systemd/timesyncd.conf` that can be modified instead of using commands 

### Parent Note

- [Linux Study Journey](./README.md)
