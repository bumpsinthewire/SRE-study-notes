---
title: "startup-process_and_services"
date: "2026-01-19"
type: study_notes
tags: [study, linux]
---

# startup-process_and_services

## Key Concepts

`systemctl` can be used for sytem commands like **shutdown** or **reboot**  
can specify a time to shutdown at a specific time (02:00 for 2am) or in xx minutes by using "+" follows by how many minutes you want (+15)

`ESQ` is the name of the return code (Exit Status Quo) that you get for running a command  
you will get an `ESQ` of 0 if the command was successful and an `ESQ` higher than 0 if it **failed** or **encountered an error**

init = initialization system. This is the tool that contains all of the instructions for how to run everything on the system  
`systemd` is how you interact with init and there is a lifetime of things to learn with it

## Commands & Examples

`systemctl shutdown -r +10 "Restarting in 10 minutes"`  
`-r` can be used to reboot instead of shutdown ( will restart in 10 minutes as well as send the message in "")

`echo $?` will return the `ESQ` of the last command

`systemctl cat xxx.service` will show you the service file (instructions) for a service  
`sudo systemctl edit --full xxx.service` to edit the service file  
`sudo systemctl revert xxx.service` sets the service file back to default settings

`sudo systemctl status xxx.service` shows the status of a service  
`sudo systemctl stop xxx.service` stop a service  
`sudo systemctl start xxx.service` start a service  
`sudo systemctl restart xxx.service` restart a service but can be disruptive  
`sudo systemctl reload xxx.service` like a graceful restart  
`sudo systemctl disable xxx.service` disables a service  
`--now` disables a service from automatically starting at boot and also stops a service  
`sudo systemctl enable xxx.service` automatically starts a service at boot  
`--now` enables a service and also starts it now  
`sudo systemctl mask xxx.service` prevents a service from starting (even if something else calls on it)  
`sudo systemctl unmask xxx.service` unmasks a service

## Questions & Notes

`ESQ` is used when evaluating scripting statements (like *if*). 0 is "TRUE" and anything else is "FALSE"

## Resources

[Systemd Essentials: Working with Services, Units, and the Journal](https://www.digitalocean.com/community/tutorials/systemd-essentials-working-with-services-units-and-the-journal)  
[Working with systemd unit files](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_systemd_unit_files_to_customize_and_optimize_your_system/assembly_working-with-systemd-unit-files_working-with-systemd)

### Parent Note

- [Linux Study Journey](./README.md)
