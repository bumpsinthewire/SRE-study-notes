---
title: "datasources"
date: "2026-02-23"
type: study_notes
tags: [study, IaC]
---

# datasources

## Key Concepts

Terraform lets you use attributes from resources that already exist

## Commands & Examples

example data block code and how to reference it
```terraform
data "aws_key_pair" "cerberus-key" {
    key_name = "alpha"
}
resource "aws_instance" "cerberus" {
    ami = var.ami
    instance_type = var.instance_type
    key_name = data.aws_key_pair.cerberus-key.key_name
}
```

## Questions & Notes

Note that the `data` block is for READ-ONLY  
If you want to manage an external resource, you will need to use the `import` block

### Parent Note

- [IaC Study Journey](./README.md)
