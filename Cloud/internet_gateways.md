---
title: "internet_gateways"
date: "2026-03-04"
type: study_notes
tags: [study, Cloud]
---

# internet_gateways

## Key Concepts

Internet Gateways (IGW) allow resources to connect to the public internet

## Commands & Examples

```bash
  # aws_internet_gateway.SRE-gateway will be created
  + resource "aws_internet_gateway" "SRE-gateway" {
      + arn      = (known after apply)
      + id       = (known after apply)
      + owner_id = (known after apply)
      + region   = "us-east-1"
      + tags     = {
          + "Name" = "SRE-IGW"
        }
      + tags_all = {
          + "Name" = "SRE-IGW"
        }
      + vpc_id   = (known after apply)
    }
```

## Questions & Notes

IGW's are 1:1 with a VPC and are *region resilient*  
You must explicitly attach an IGW to a VPC  
You must add a *route table* entry pointing to the IGW

## Resources

- [Terraform IGW code](./internet_gateway.tf)

### Parent Note

- [Cloud Study Journey](./README.md)
