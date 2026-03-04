---
title: "NAT Gateway"
date: "2026-03-04"
type: study_notes
tags: [study, Cloud]
---

# NAT Gateway

## Key Concepts

NAT Gateways (NGW) allows you to have private subnets for internal resources that still need internet access

## Commands & Examples

```bash
  # aws_nat_gateway.SRE-NAT-gateway will be created
  + resource "aws_nat_gateway" "SRE-NAT-gateway" {
      + association_id                     = (known after apply)
      + auto_provision_zones               = (known after apply)
      + auto_scaling_ips                   = (known after apply)
      + availability_mode                  = (known after apply)
      + connectivity_type                  = "public"
      + id                                 = (known after apply)
      + network_interface_id               = (known after apply)
      + private_ip                         = (known after apply)
      + public_ip                          = (known after apply)
      + region                             = "us-east-1"
      + regional_nat_gateway_address       = (known after apply)
      + regional_nat_gateway_auto_mode     = (known after apply)
      + route_table_id                     = (known after apply)
      + secondary_allocation_ids           = (known after apply)
      + secondary_private_ip_address_count = (known after apply)
      + secondary_private_ip_addresses     = (known after apply)
      + subnet_id                          = (known after apply)
      + tags                               = {
          + "Name" = "SRE-NGW"
        }
      + tags_all                           = {
          + "Name" = "SRE-NGW"
        }
      + vpc_id                             = (known after apply)
    }
```

## Questions & Notes

You still need an IGW to use a NGW  
The NGW gets deployed within a public subnet with a route to the internet  
The private subnet will have a *route table* entry that points to the NGW  
NGWs are charged per hour and per GB of data processed  

## Resources

- [Terraform NGW code](./nat_gateway.tf)

### Parent Note

- [Cloud Study Journey](./README.md)
