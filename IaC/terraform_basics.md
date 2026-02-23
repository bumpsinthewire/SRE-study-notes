---
title: "terraform_basics"
date: "2026-02-23"
type: study_notes
tags: [study, IaC]
---

# terraform_basics

## Key Concepts

`brew tap hashicorp/tap` adds the Hashicorp tap (repository of their Homebrew packages)
`brew install hashicorp/tap/terraform` installs `terraform`
`terraform --version` shows your TF (terraform) version

example local resource setup
```terraform
resource "local_file" "pet" {
    filename = "/root/pets.txt"
    content = "We love pets!"
}
```
`resource` is the block name. this defines what the item is
`"local_file"` is the type of resource (local = provider, file = resource)
`"pet"` is the resource name that you specify
`"filename" and "content"` are arguments in key/value pair formats and are specific to the resource type

example AWS EC2 instance
```terraform
resource "aws_instance" "web" {
    ami = "ami-0c2f25c1f66a1ff4d"
    instance_type = "t2.micro"
}
```

`terraform init` initializes terraform to install everything needed for the provider(s) you are using in your TF code
`terraform plan` gives you an output showing what your TF code will do
`terraform apply` runs your TF code (and shows what it will do)
`terraform destroy` will tear down resources (and show you what it will do beforehand)

## Commands & Examples

to update a resource, change your code and TF will destroy and re-create the resource

## Resources

- [Terraform | HashiCorp Developer](https://developer.hashicorp.com/terraform)

## Next Steps

- [Terraform Registry](https://registry.terraform.io/)

### Parent Note

- [IaC Study Journey](./README.md)
