---
title: "providers"
date: "2026-02-23"
type: study_notes
tags: [study, IaC]
---

# providers_basics

## Key Concepts

You must download plugins for each provider you want to use

## Commands & Examples

Use `terraform init` to download the required plugins for providers you have listed

## Questions & Notes

`hashicorp/local` first is the organizational namespace, then the type  
can optionally add a hostname for the location where the plugin is provided from  
if a hostname is not provided, it defaults to `registry.terraform.io`

## Resources

- [Terraform Registry](https://registry.terraform.io/)

### Parent Note

- [IaC Study Journey](./README.md)
