---
title: "workspaces"
date: "2026-02-25"
type: study_notes
tags: [study, IaC]
---

# workspaces

## Key Concepts

Workspaces are the solution to reusing resoures and variables to stand up multiple environments  
Workspaces also isolate state files

## Commands & Examples

`terraform workspace list` gives you a listing of all of your workspaces  
`terraform workspace new <workspace_name>` creates and switches you to a new workspace  
`terraform workspace select <workspace_name>` allows to select a workspace

`lookup(var.instance_type, terraform.workspace, "t2.micro")` allows the system to look at the name of the workspace and find the value for that workspace.  
if the workspace does not exist, then it will default to `t2.micro` in this example

## Questions & Notes

A workspace called "default" is created automatically by TF  
There are hosted platforms that are made to streamline the workspaces workflow

## Resources

[HashiCorp Cloud Platform](https://www.hashicorp.com/en/cloud)

### Parent Note

- [IaC Study Journey](./README.md)
