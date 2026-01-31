---
title: "repositories_and_software"
date: "2026-01-22"
type: study_notes
tags: [study, linux]
---

# repositories_and_software

## Key Concepts

Linux uses a tool for package management (software). On Ubuntu, this tool is called `apt` (advanced package tool)  
Repositories are a database that packages can be uploaded to. This includes the package itself as well as updates

## Commands & Examples

`sudo apt update` this refreshes the local db of available packages from the remote repo  
`sudo apt upgrade` executes any available upgrades  
`sudo apt install [package]` installs a package  
`sudo apt remove [package]` uninstalls a package  
`autoremove` also removes dependencies that might not have been removed with just the `remove` command  
`apt show [package]` gives you information about a package (what it does and what it includes)  
`apt search [name]` looks for a package in both the name and description of all packages  
use `--names-only` to just search by name and not description

`dpkg` gives you information about packages  
`--listfiles [package]` lists all of the files installed by a package  
`--search [file]` will tell you which package brought in this file

check `/etc/apt/sources.list.d/` for information about the repos tied in to your machine  
`add-apt-repository` lets you manage repos  
`--list` will show you the same content in the files above

you can use `make` to install a program. Using `sudo make install` sets it up so that you can use it everywhere (puts it in `/usr/local/bin`)

## Questions & Notes

you can add your own repositories to use as well. This can be helpful if you want the latest build for example or just want to try out unsupported software

### Parent Note

- [Linux Study Journey](./README.md)
