---
title: "terraform_commands"
date: "2026-02-25"
type: study_notes
tags: [study, IaC]
---

# terraform_commands

## Key Concepts

Terraform has some built-in commands that make things easier

## Commands & Examples

`terraform validate` will show you if your blocks have proper arguments

`terraform fmt` will format all of your `.tf` files for you

`terraform show` will print out the current state of your infra as seen by TF  
can also use `-json` to print it in json format

`terraform providers` shows you all of the providers you are using

`terraform output` will show you all of your output variables  
can also specify a specific variable at the end of the command

`terraform graph` will give you a visual representation of your infrastructure in a DOT file  
this can be used with graph visualization software as well

`terraform state list` shows all resources in your state file  
`terraform state mv [options] SOURCE DESTINATION` is an easy way to change the name of a resource  
`terraform state rm ADDRESS` to remove a resource from state

## Questions & Notes

if you use `terraform state rm`, you still need to remove the config from the `.tf` files

### Parent Note

- [IaC Study Journey](./README.md)
