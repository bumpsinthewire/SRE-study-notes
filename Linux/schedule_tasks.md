---
title: "schedule_tasks"
date: "2026-01-20"
type: study_notes
tags: [study, linux]
---

# schedule_tasks

## Key Concepts

Linux has tools for you to run tasks at set times  
`cron`, `anacron`, and `at` are the 3 most used utilities

## Commands & Examples

`cat /etc/crontab` this is the default system-wide `cron` table and shows you how to use `cron`  
`/etc/cron.daily/`, `/etc/cron.hourly/`, `/etc/cron.monthly/`, `/etc/cron.weekly/` are special directories that hold jobs that will run at the named intervals  
`cron` jobs go in the order of:  
minute (0-59)  
hour (0-23)  
day of month (1 - 31)  
month (1 - 12) OR jan,feb,mar,apr,...  
day of week (0 - 6) (Sunday = 0 OR 7) OR sun, mon, tue, wed, thu, fri, sat  
*user-name* [command_to_be_executed]  
35 6 * * * root /bin/some_command --some-options (runs some_command with --some-options at the 35th minute of the 6th hour of every day)  
use "," to match multiple values  
use "-" for a range of values  
use "/" for specific steps (for example */4 would run every 4 hours in the "hour" column)  
`crontab -e` will edit the current users `cron` table  
`-l` will list the `cron` table jobs (adding sudo will show the root `cron` table)  
`-r` will remove the `cron` table entirely  
`sudo crontab -e -u jane` will let you edit the `cron` table of another user

`cat /etc/anacrontab` shows the default system-wide `anacron` table and gives examples  
`anacron -T` will verify if your syntax is correct

`at '15:00'` will open a prompt for you to define what you want to run "at 15:00" (<C-d> control-d to quit)  
some examples:  
`at 'August 20 2024'`  
`at '2:30 August 20 2024'`  
`at 'now + 30 minutes'`  
`at 'now + 3 months'`  
use `atq` to see the curren `at` jobs (this gives you a job ID)  
use `at -c [job ID]` to get more information about a specific job

## Questions & Notes

`cron` is very customizable and can be used for specific times relating to the minute/hour/day (but will miss jobs when powered off)  
"*" is used as a wildcard to match "all values"  
`anacron` is more for day/few days/week/month/year (can not run a job more than once a day but checks if a job has been run after power-on)  
`at` is very basic and much more for tasks that only need to be run once

## Resources

[Crontab.guru - The cron schedule expression generator](https://crontab.guru/)

### Parent Note

- [Linux Study Journey](./README.md)
