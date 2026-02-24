---
title: "local_project"
date: "2026-02-23"
type: project
tags: [project, IaC]
---

# local_project

## Overview

Terraform local project to create some folders and files, using a datasource for the content

## The Solution

Created a local file with text in it to be used as a datasource that would fill in some of the body of the file being created

### Implementation Logic

Terraform is mainly used for provisioning infrastructure but is very flexible and can be used for local resources as well

### Reliability Considerations

Added `variables.tf` and `outputs.tf` files as well as locking down the `local` provider to a specific version in the `providers.tf` file

## Key Learnings

Using a datasource to pull from for a new resource

## Code Implementation

- [local project](./main.tf)

## Results


### Parent Note
