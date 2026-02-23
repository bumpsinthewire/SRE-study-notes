---
title: "providers_versioning"
date: "2026-02-23"
type: study_notes
tags: [study, IaC]
---

# providers_versioning_and_aliases

## Key Concepts

TF allows you to state which versions of providers you want to use
the default behavior is to use the latest available version

using a `provider.tf` file is recommended when you start using multiple providers

say that you have multiple regions for a provider (like `aws`)
you can use aliases to make them distinct and be able to call them separately

## Commands & Examples

example code block to specify the `local` provider version
```terraform
terraform {
    required_providers {
        local = {
            source = "hashicorp/local"
            version = "1.4.0"
        }
    }
}
```

alias example
```terraform
provider "aws" {
    region = "us-east-1"
}

provider "aws" {
    region = "ca-central-1"
    alias = "central"
}
```

when you are defining a resource, use a `provider` argument to pick an alias
`provider = <provider_name>.<alias_name>`
from above, it would be `provider = aws.central`

## Questions & Notes

you can use specific characters to further specify what you want to do with a version
combine multiple filters by separating with commas (`> 1.2.0, < 2.0.0, != 1.4.0`)
`!` : do NOT use this version
`>/<` : use a version greater than/lesser than specified version
`~> 1.2` : use any version 1.2 or greater, stops before major version update (2.x)
`~> 1.2.0` : don't be fooled by this. this will use any version from 1.2.0 and greater, but stops before going to 1.3

### Parent Note

- [IaC Study Journey](./README.md)
