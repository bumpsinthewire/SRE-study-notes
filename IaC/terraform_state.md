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

A `terraform backend` block is used to set up state storage
`terraform init` must be run to set up the new state backend
```terraform
terraform {
    backend "s3" {
        bucket = "terraform-state-bucket01"
        key = "finance/terraform.tfstate"
        region = "us-west-1"
        dynamodb_table = "state-locking"
    }
}
```

## Questions & Notes

when you run `terraform plan` or `terraform apply`, the state file is refreshed and compared for the output
Terraform uses a Directed Acyclic Graph to map all of the resources and their dependencies

Your `*.tfstate` and `*.tfstate.*` files shoud **NEVER** be committed to version control. Always make sure they are in your .gitignore

Best practice is to host your TF state files in a remote location
State locking is used to prevent multiple people from applying a change at the same moment and causing conflicts or data loss
Many remote backends support encryption and state locking just for these reasons
A common setup with AWS is using an S3 bucket for storage and DynamoDB for locking

### Parent Note

- [IaC Study Journey](./README.md)
