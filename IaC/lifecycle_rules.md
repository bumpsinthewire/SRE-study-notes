---
title: "lifecycle_rules"
date: "2026-02-25"
type: study_notes
tags: [study, IaC]
---

# lifecycle_rules

## Key Concepts

The default behavior when modifying a resource is to destroy and recreate
You can change this behavior with the `lifecycle` block

## Commands & Examples

`create_before_destroy` example code block
```terraform
resource "aws_instance" "cerberus" {
    ami = "ami-xxxx"
    instance_type = "m5.large"
    tags = {
        Name = "Cerberus-webserver"
    }
    lifecycle {
        create_before_destroy = true
    }
}
```

`prevent_destroy` example code block
```terraform
resource "aws_instance" "cerberus" {
    ami = "ami-xxxx"
    instance_type = "m5.large"
    tags = {
        Name = "Cerberus-webserver"
    }
    lifecycle {
        prevent_destroy = true
    }
}
```

`ignore_changes` example code block
```terraform
resource "aws_instance" "cerberus" {
    ami = "ami-xxxx"
    instance_type = "m5.large"
    tags = {
        Name = "Cerberus-webserver"
    }
    lifecycle {
        ignore_changes = [
            tags
        ]
    }
}
```

## Questions & Notes

`create_before_destroy` means the new resource will be created first before the old one is destroyed
`prevent_destroy` will make TF reject any changes that would destroy a resource
this does NOT prevent resources from being destroyed with `terraform destroy`
`ignore_changes` will prevent a resource from being updated based on what attributes you define in a list
can also use the "all" keyword to prevent all changes

### Parent Note

- [IaC Study Journey](./README.md)
