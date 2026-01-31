---
title: "bridges_and_bonds"
date: "2026-01-27"
type: study_notes
tags: [study, linux]
---

# bridges_and_bonds

## Key Concepts

Bridges and bonds are two distinct features in Linux networking  
A bridge is used to allows traffic between two network devices as if they were directly connected  
A bond is used to combine network devices together so that they act like one. Some of the benefits are resiliency and increased throughput  

## Commands & Examples

Create a bridge:  
`/usr/share/doc/netplan/examples/bridge.yaml` has an example `netplan` *yaml* file  
```yaml
bridges:
br0: # name of the bridge
  dhcp4: yes
  interfaces:
    - enp0s8
    - enp0s9 
```
you MUST define the interfaces you want to use in the `ethernets:` section of the *yaml* file before adding them to the `bridges:` section

Create a bond:  
`/usr/share/doc/netplan/examples/bonding.yaml` has an example `netplan` *yaml* file  
```yaml
bonds:
  bond0: # name of the bond
    dhcp4: yes
    interfaces:
      - enp0s8
      - enp0s9
    parameters:
      mode: # choose one of the 7 modes here. you can use the name or the mode number
      additional-parameters: # these depend on which mode you chose
```
you MUST define the interfaces you want to use in the `ethernets:` section of the *yaml* file before adding them to the `bonds:` section

## Questions & Notes

Bonds can be one of seven modes (from 0 to 6)  
Mode 0: round-robin (usually the default if none is chosen) - uses NICs in sequential order  
Mode 1: active-backup - has a primary and a backup  
Mode 2: XOR - chooses one and sticks with it  
Mode 3: broadcast - all NICs at once  
Mode 4: IEEE 802.3ad - LACP  
Mode 5: adaptive transmit load balancing - send transmit traffic to the least busy NIC  
Mode 6: adaptive load balancing - load balances outgoing and incoming traffic

## Resources

`usr/share/doc/netplan/examples/` has a catalog of example *yaml* files for `netplan`

### Parent Note

- [Linux Study Journey](./README.md)
