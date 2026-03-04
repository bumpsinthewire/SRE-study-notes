---
title: "Subnets"
date: "2026-03-03"
type: study_notes
tags: [study, Cloud]
---

# Subnets

## Key Concepts

Subnets are groups of IP addresses within your VPC CIDR range  

## Commands & Examples

```bash
  # aws_subnet.private will be created
  + resource "aws_subnet" "private" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = "us-east-1b"
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.0.2.0/24"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block                                = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = false
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + region                                         = "us-east-1"
      + tags                                           = {
          + "Name" = "SRE-priv-subnet"
        }
      + tags_all                                       = {
          + "Name" = "SRE-priv-subnet"
        }
      + vpc_id                                         = (known after apply)
    }

  # aws_subnet.public will be created
  + resource "aws_subnet" "public" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = "us-east-1a"
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.0.1.0/24"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block                                = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = false
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + region                                         = "us-east-1"
      + tags                                           = {
          + "Name" = "SRE-pub-subnet"
        }
      + tags_all                                       = {
          + "Name" = "SRE-pub-subnet"
        }
      + vpc_id                                         = (known after apply)
    }
```

## Questions & Notes

Subnets:

- reside within a single Availability Zone (AZ)
- can be either public or private
- must be within /16 to /28
- first 4 and last IPs are reserved
  - network address
  - VPC router
  - DNS
  - future use
  - broadcast

## Resources

- [Terraform Subnets code](./subnets.tf)

### Parent Note

- [Cloud Study Journey](./README.md)
