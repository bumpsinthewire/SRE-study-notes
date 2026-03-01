---
title: "variables"
date: "2026-02-23"
type: study_notes
tags: [study, IaC]
---

# variables

## Key Concepts

Instead of hardcoding values, TF allows you to define variables  
`variables.tf` is the location for defining variables you want to use  
see notes section below for defining the values in those variables

you can also define an `output` block to pull information from a resource

## Commands & Examples

example variable code block
```terraform
variable "ami" {
    description = "The id of the machine image (AMI) to use for the server."
    type = string
    sensitive = true
    validation {
        condition = substr(var.ami, 0, 4) == "ami-"
        error_message = "The AMI should start with \"ami-\"."
    }
}
```
condition example above makes it so any value assigned needs to start with "ami-"

example use of variable
```terraform
resource "local_file" "pet" {
    filename = var.filename
    content = var.content
}
```

example output code block
```terraform
output "pub_ip" {
    value = aws_instance.<instanct_name>.public_ip
    description = "print the public IPv4 address"
}
```

`terraform output <name_of_output_block>` can be used as well

## Questions & Notes

using the "default" keyword makes the variable optional  
if you specify "default" and "type", the default value must match the type

one thing to keep in mind about setting the values of variables  
if file is named `terraform.tfvars`, `terraform.tfvars.json`, or ends in `.auto.tfvars` or `.auto.tfvars.json`, TF will auto load the values  
any other filename used means you have to manually load by using `terraform plan -var-file="production.tfvars"` for example

variable definition precedence:
    1. environment variables: must preface the variable with `TF_VAR` (case-sensitive)
    2. terraform.tfvars
    3. *.auto.tfvars (alphabetical order)
    4. `-var` or `-var-file`
however, #4 overrides all of the others  
most teams use `*.auto.tfvars` method (`networking.auto.tfvars, db.auto.tfvars`)

`type` argument can be a multitude of data structures (like string, map, list, etc.)  
to call a value from a list, use `var.<var_name>[0]` with 0-based indexing  
to call a value from a map, use `var.<var_name>["key_name"]`

`sensitive` argument will mask the value if set to `true` (default is `false`)  
the value is still stored in the state file in plaintext though  
`sensitive` variables will NOT be shown in normal `terraform output` on the screen  
the way around this is to use `terraform output <variable>`

### Parent Note

- [IaC Study Journey](./README.md)
