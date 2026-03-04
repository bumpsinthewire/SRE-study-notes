---
title: "VPC_routing"
date: "2026-03-03"
type: study_notes
tags: [study, Cloud]
---

# VPC_routing

## Key Concepts

Every VPC has a router and every subnet in a VPC has an interface to it  

- router IP is the first usable IP of a subnet (eg. 10.0.1.1/24)

The router uses *route tables* to determine where to forward packets  

- longest prefix match has preference

## Commands & Examples

```bash
  # aws_route_table.route_table will be created
  + resource "aws_route_table" "route_table" {
      + arn              = (known after apply)
      + id               = (known after apply)
      + owner_id         = (known after apply)
      + propagating_vgws = (known after apply)
      + region           = "us-east-1"
      + route            = (known after apply)
      + tags             = {
          + "Name" = "SRE-public-route-table"
        }
      + tags_all         = {
          + "Name" = "SRE-public-route-table"
        }
      + vpc_id           = (known after apply)
    }

  # aws_route_table_association.pub_assoc[0] will be created
  + resource "aws_route_table_association" "pub_assoc" {
      + id             = (known after apply)
      + region         = "us-east-1"
      + route_table_id = (known after apply)
      + subnet_id      = (known after apply)
    }

  # aws_route_table_association.pub_assoc[1] will be created
  + resource "aws_route_table_association" "pub_assoc" {
      + id             = (known after apply)
      + region         = "us-east-1"
      + route_table_id = (known after apply)
      + subnet_id      = (known after apply)
    }
```

## Questions & Notes

A single *route table* can be associated with mutliple subnets
Each *subnet* can only be associated with a single *route table*

## Resources

- [Terraform Route Table code](./route_tables.tf)

### Parent Note

- [Cloud Study Journey](./README.md)
