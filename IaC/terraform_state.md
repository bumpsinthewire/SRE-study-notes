---
title: "terraform_state"
date: "2026-02-25"
type: study_notes
tags: [study, IaC]
---

# terraform_state

## Key Concepts

Terraform keeps track of resources managed/created by use of a special graph (DAG)
The data for these resources is stored in json format in `terrafrorm.tfstate`
There is a backup in `terraform.tfstate.backup`

## Commands & Examples

*(Important commands with examples)*

## Questions & Notes

when you run `terraform plan` or `terraform apply`, the state file is refreshed and compared for the output
Terraform uses a Directed Acyclic Graph to map all of the resources and their dependencies
Your `*.tfstate.*` files shoud **NEVER** be committed to version control. Always make sure they are in your .gitignore

## Resources

*(Links to documentation, tutorials, etc.)*

## Next Steps

*(What to explore next)*

### Parent Note

- [IaC Study Journey](./README.md)
