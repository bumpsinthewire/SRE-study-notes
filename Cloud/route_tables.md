---
title: "Route tables"
date: "2026-03-03"
type: study_notes
tags: [study, Cloud]
---

# Route Tables

## Key Concepts

Every VPC has a router and every subnet in a VPC has an interface to it  

- router IP is the first usable IP of a subnet (eg. 10.0.1.1/24)

The router uses *route tables* to determine where to forward packets  

- longest prefix match has preference

## Commands & Examples

```bash
  # aws_route_table.private_route_table will be created
  + resource "aws_route_table" "private_route_table" {
      + arn              = (known after apply)
      + id               = (known after apply)
      + owner_id         = (known after apply)
      + propagating_vgws = (known after apply)
      + region           = "us-east-1"
      + route            = (known after apply)
      + tags             = {
          + "Name" = "SRE-private-subnet-route-table"
        }
      + tags_all         = {
          + "Name" = "SRE-private-subnet-route-table"
        }
      + vpc_id           = (known after apply)
    }

  # aws_route_table.public_route_table will be created
  + resource "aws_route_table" "public_route_table" {
      + arn              = (known after apply)
      + id               = (known after apply)
      + owner_id         = (known after apply)
      + propagating_vgws = (known after apply)
      + region           = "us-east-1"
      + route            = (known after apply)
      + tags             = {
          + "Name" = "SRE-public-subnet-route-table"
        }
      + tags_all         = {
          + "Name" = "SRE-public-subnet-route-table"
        }
      + vpc_id           = (known after apply)
    }

  # aws_route_table_association.IGW_assoc will be created
  + resource "aws_route_table_association" "IGW_assoc" {
      + gateway_id     = (known after apply)
      + id             = (known after apply)
      + region         = "us-east-1"
      + route_table_id = (known after apply)
    }

  # aws_route_table_association.NGW_assoc will be created
  + resource "aws_route_table_association" "NGW_assoc" {
      + gateway_id     = (known after apply)
      + id             = (known after apply)
      + region         = "us-east-1"
      + route_table_id = (known after apply)
    }
```

## Questions & Notes

A single *route table* can be associated with mutliple subnets
Each *subnet* can only be associated with a single *route table*

## Resources

- [Terraform Route Table code](./route_tables.tf)

### Parent Note

- [Cloud Study Journey](./README.md)
