---
title: "local_values"
date: "2026-02-26"
type: study_notes
tags: [study, IaC]
---

# local_values

## Key Concepts

Local values in Terraform let you reuse values that will be common among multiple resources

## Commands & Examples

```terraform
locals {
    common_tags = {
        Department = "finance"
        Project = "cerberus"
    }
}
resource "aws_instance" "web" {
    ami = "ami-xxx"
    instance_type = var.instance_type
    tags = local.common_tags
}
```

## Questions & Notes

This is very simple but very powerful.  
Using variable interpolation makes this even more flexible

### Parent Note

- [IaC Study Journey](./README.md)
