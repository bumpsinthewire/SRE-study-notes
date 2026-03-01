---
title: "tainting"
date: "2026-02-25"
type: study_notes
tags: [study, IaC]
---

# tainting

## Key Concepts

If a configuration fails, Terraform will `taint` a resource so that it gets replaced on the next `terraform apply`

There are also times when you **want** TF to replace a resource.  
TF allows for manual "tainting" of a resource for this reason

## Commands & Examples

`terraform taint [resource_name]` will mark a resource as tainted so that it will be replaced on the next `terraform apply`

to "untaint" a resource it's as simple as using `untaint`  
`terraform untaint [resource_name]`

## Questions & Notes

Some resources like REST API calls do not update properly.  
Those resources would be a good use case for this

### Parent Note

- [IaC Study Journey](./README.md)
