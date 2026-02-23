---
title: "resource_attributes"
date: "2026-02-23"
type: study_notes
tags: [study, IaC]
---

# resource_attributes

## Key Concepts

Terraform allows you to use attributes from another resource

## Commands & Examples

example resource with its attributes used elsewhere
```terraform
resource "aws_key_pair" "alpha" {
    key_name = "alpha"
    public_key = "ssh-rsa..."
}
resource "aws_instance" "cerberus" {
    ami = var.ami
    instance_type = var.instance_type
    key_name = aws_key_pair.alpha.key_name
}
```

order of creation matters. you can add an argument to handle this
```terraform
resource "aws_instance" "db" {
    ami = var.db_ami
    instance_type = var.web_instance_type
}
resource "aws_instance" "web" {
    ami = var.web_ami
    instance_type = var.db_instance_type
    depends_on = [
        aws_instance.db
    ]
}
```

just like `bash`, you can do string interpolation on variables and attribute references
```terraform
resource "random_string" "server-suffix" {
    length = 6
    upper = false
    special = false
}
resource "aws_instance" "web" {
    ami = var.web_ami
    instance_type = var.web_instance_type
    tags = {
        Name = "web-${random_string.server-suffix.id}"
    }
}
```

## Questions & Notes

the syntax to call an attribute from another resource is:
`<resource type>.<resource name>.<attribute>`

when using attribute references, if the original changes, the one with the reference will change as well
if you don't want this to happen, you can use the `-target <original_resource_attribute>` flag

### Parent Note

- [IaC Study Journey](./README.md)
