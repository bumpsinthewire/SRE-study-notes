---
title: "import"
date: "2026-02-25"
type: study_notes
tags: [study, IaC]
---

# import

## Key Concepts

Terraform allows you to import resources that were not created with TF

## Commands & Examples

you must first create the resource in your `.tf` file
```terraform
resource "aws_instance" "webserver-2" {
    # (resource arguments)
}
```

then you can use the `import` command
`terraform import aws_instance.webserver-2 <unique ID>`

## Questions & Notes

`import` does not update configuration files, it just adds a resource into the state file
you can use `terraform plan` to make sure that you're config files are up to date with the actual resource

### Parent Note

- [IaC Study Journey](./README.md)
