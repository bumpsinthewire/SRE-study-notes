---
title: "count_and_for_each"
date: "2026-02-26"
type: study_notes
tags: [study, IaC]
---

# count_and_for_each

## Key Concepts

Terraform has some built-in functionality for making multiple resources easier  
`count` allows you to define how many instances of a particular resource you want  
`for_each` loops over a map or set (can NOT be a list) to create resources

## Commands & Examples

```terraform
# example count block:
resource "aws_instance" "web" {
    ami = var.ami
    instance_type = var.instance_type
    count = length(var.webservers)
    tags = {
        Name = var.webservers[count.index]
    }
}
```

```terraform
# count block variables.tf example
variable "webservers" {
    type = list(string)
    default = ["web1", "web2", "web3"]
}
```

```terraform
terraform state list
aws_instance.web[0]
aws_instance.web[1]
aws_instance.web[2]
```

```terraform
# example for_each block
resource "aws_instance" "web" {
    ami = var.ami
    instance_type = var.instance_type
    for_each = var.webservers
    tags = {
        Name = each.value
    }
}
```

```terraform
# for_each block variables.tf example
variable "webservers" {
    type = set(string)
    default = ["web1", "web2", "web3"]
}
```

```terraform
terraform state list
aws_instance.web["web1"]
aws_instance.web["web2"]
aws_instance.web["web3"]
```

## Questions & Notes

`count` can also defined by just a number  
one of the downsides with using `count` is that if you want to destroy a resource, the elements of the list will move to fill in that spot.  
so if you destroy the first element of a 3 resouce list, spots 1 and 2 will move to 0 and 1 and then the tags will no longer line up properly

don't get mixed up with python syntax for defining sets and maps(dictionaries).  
python uses {} for both but TF uses [] for sets and {} for maps.  
also maps are done as `key = value` in TF, instead of `key: value` like python

### Parent Note

- [IaC Study Journey](./README.md)
