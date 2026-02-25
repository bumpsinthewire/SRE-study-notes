---
title: "Local Project"
date: "2026-02-23"
type: project
tags: [project, IaC]
---

# Local Project

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

```terraform
  # local_file.log_file will be created
  + resource "local_file" "log_file" {
      + content              = "Log initialized for sre-automation"
      + content_base64sha256 = (known after apply)
      + content_base64sha512 = (known after apply)
      + content_md5          = (known after apply)
      + content_sha1         = (known after apply)
      + content_sha256       = (known after apply)
      + content_sha512       = (known after apply)
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "sre-automation/activity.log"
      + id                   = (known after apply)
    }

  # local_file.project_folder will be created
  + resource "local_file" "project_folder" {
      + content              = <<-EOT
            Project: sre-automation
            Environment: development
            Policy: Secure
        EOT
      + content_base64sha256 = (known after apply)
      + content_base64sha512 = (known after apply)
      + content_md5          = (known after apply)
      + content_sha1         = (known after apply)
      + content_sha256       = (known after apply)
      + content_sha512       = (known after apply)
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "sre-automation/README.txt"
      + id                   = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.
```

### Parent Note

- [IaC Study Journey](../README.md)
