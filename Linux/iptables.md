---
title: "iptables"
date: "2026-01-28"
type: study_notes
tags: [study, linux]
---

# iptables

## Key Concepts

`iptables` is commonly used for more advanced filtering/firewalling  
Port redirection and NAT are common `iptables` uses  
Port redirection takes traffic coming in on a port and sends it to a specific target   
NAT (Network Address Translation) redirects traffic that it receives on its own IP to a different internal IP by changing the destination once it receives a packet  
SNAT (Source Network Address Translation) changes the source IP so that internal servers don't have return traffic issues  
also called "masquerading" becuase it is pretending to be someone else

## Commands & Examples

`iptables` uses *tables* and *chains* to define what you want to do and then use the *target* for which action you want to take on them  
some common tables are *nat*, *filter* (the default), and *mangle* (alters headers)  
*nat* table common chains; *PREROUTING*, *POSTROUTING*  
*nat* table common targets; POSTROUTING chain - *MASQUERADE*, *SNAT* PREROUTING chain - *DNAT*, *REDIRECT*  
*filter* table common chains; *INPUT*, *OUTPUT*, *FORWARD*  
*filter* table common targets; *ACCEPT*, *DROP*, *REJECT*, *LOG*  
*mangle* table common chains; *PREROUTING*, *INPUT*  
*mangle* table common targets; *MARK*, *TOS*  
long commands but mostly straightforward. the hard part of `iptables` is just learning which tables/chains/actions go together  
`iptables -t nat -A PREROUTING -i enp1s0 -s 10.0.0.0/24 -p tcp --dport 8080 -j DNAT --to-destination 192.168.0.5:80`  
sets up NAT for packets coming from the 10.0.0.0/24 network going IN to the enp1s0 NIC addressed to 8080/TCP and redirecting them to 192.168.0.5:80  
`iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o enp6s0 -j MASQUERADE`  
sets up SNAT for packets coming from the 10.0.0.0/24 network going OUT the enp6s0 NIC  
`netfilter-persistent save` to permanently save any `iptables` rules  
`iptables --list-rules --table [table]` outputs the rules configured for a table  
`iptables --flush --table [table]` will remove all of the existing rules from a table

## Questions & Notes

IP Forwarding must be enabled to do port redirection  
edit the `/etc/sysctl.d/99-sysctl.conf` or `/etc/sysctl.conf` files (first one is preferred)  
uncomment both `net.ipv4.ip_forward=1` and `net.ipv6.conf.all.forwarding=1`  
run `sudo sysctl --system` to reload and make sure forwarding is enabled  
install `iptables-persistent` package to be able to save `iptables` rules permanently

## Resources

*(Links to documentation, tutorials, etc.)*

## Next Steps

`nftables` is becoming more and more the modern standard for managing filtering/firewalling

### Parent Note

- [Linux Study Journey](./README.md)
