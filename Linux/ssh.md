---
title: "ssh"
date: "2026-01-28"
type: study_notes
tags: [study, linux]
---

# ssh

## Key Concepts

`ssh` needs two things: an `ssh` client on your local machine, and an `ssh` daemon running on a server

## Commands & Examples

`PermitRootLogin prohibit-password` allows *root* login without a password (like using `ssh` keys)
`Match User [username]` to set configs on a per-user basis
`ssh [username]@[IP/hostname]` to `ssh` into a server
`ssh-keygen` generates an `ssh` key (private and public key)
    `-R [IP/hostname]` to remove a key from a remote server
`ssh-copy-id [username]@[IP/hostname]` to copy your public key to a server
look in `~/.ssh/authorized_keys` to see saved public keys on a server

## Questions & Notes

On a server, the config for the `sshd` is stored in `/etc/ssh/sshd_config`
The `ssh` client config is stored at `/etc/ssh/ssh_config`
if you have files in `/etc/ssh/sshd_config.d/` they could override the "base" config settings

## Resources

`man sshd_config` will explain the config file options for the `ssh` daemon
`man ssh_config` will explain the config file options for the `ssh` client

### Parent Note

- [Linux Study Journey](./README.md)
