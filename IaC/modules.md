---
title: "modules"
date: "2026-02-28"
type: study_notes
tags: [study, IaC]
---

# modules

## Key Concepts

Any directory containing Terraform configuration files is considered a module  
This lets you use folders as different "environments" that can point to one common set of config files

## Commands & Examples

```terraform
module "dev-webserver" {
    source = "<folder where your config files are>"
}
```

## Questions & Notes

You can find pre-created modules in the TF registry

### Parent Note

- [IaC Study Journey](./README.md)
