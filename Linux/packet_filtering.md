---
title: "packet_filtering"
date: "2026-01-28"
type: study_notes
tags: [study, linux]
---

# packet_filtering

## Key Concepts

Packet filtering lets you define rules for which traffic should be allowed in and out  
`ufw` is the default packet filtering tool

## Commands & Examples

`ufw status` shows status of the UFW (Uncomplicated FireWall)  
`verbose` gives more detail  
`numbered` shows you the order rules are processes in  
`ufw enable` enables `ufw`  
`ufw allow [port number]/[tcp,udp]` adds a rule to allow traffic (protocol is optional)  
`ufw allow from [IP] to any port [number]` allow traffic *FROM* the given IP, *TO* __*any*__ IP using the specified port  
`ufw delete [rule_number]` deletes a specific rule  
`ufw insert [position_number] [rule]` inserts a new rule at a specific location  
`ufw deny out on [int] to [IP]` stop traffic from a specific NIC to a target address  
`ufw allow in on [int] from [IP] to [IP] proto [protocol]` allow incoming data to an int from an IP to a destination IP on the machine using a certain protocol  
`ufw route allow from [network] to [IP]` installs a route

## Questions & Notes

`ufw` takes a white-list approach (only allows what you explicitly define)  
modern Linux system administration uses things like `iptables` and `nftables` for advanced firewalling/filtering use cases

## Resources

`man ufw-framework` provides detailed documentation on the underlying framework of `ufw`

### Parent Note

- [Linux Study Journey](./README.md)
