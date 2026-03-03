---
title: "VPC"
date: "2026-03-03"
type: study_notes
tags: [study, Cloud]
---

# VPC

## Key Concepts

A Virtual Private Cloud (VPC) is a secure, isolated network hosted within AWS  
A VPC allows you to have separation between environments as desired

## Commands & Examples

*(Important commands with examples)*

## Questions & Notes

VPCs allow you to do things like subnetting, routing, and firewalling  
VPCs are specific to a single region  
By default, VPCs can **not** talk to each other (network boundary)  
A CIDR block defines the IP addresses that resources inside your VPC can use  
AWS automatically configures a *default* VPC in every region your account has access to
- /16 IPv4 CIDR block of 172.31.0.0/16
- /20 default subnet in each Availability Zone (AZ)
  - 172.31.16.0/20, 172.31.32.0/20, etc
- Internet Gateway (IGW) attached to the VPC
- A route that points all traffic (0.0.0.0/0) to the IGW
- Default Security Group (SG)
  - Allows outbound traffic only
- Default Network Access Control List (NACL)
  - Allows both outbound and inbound traffic

## Resources

*(Links to documentation, tutorials, etc.)*

## Next Steps

*(What to explore next)*

### Parent Note

- [Cloud Study Journey](./README.md)
