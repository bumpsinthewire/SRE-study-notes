---
title: "IaC_types"
date: "2026-02-22"
type: study_notes
tags: [study, IaC]
---

# IaC_types

## Key Concepts

IaC tools generally fall into 3 categories:
Configuration management - install/manage software, version control, idempotent
Server templating - pre-installed software and dependencies, immutable vm/docker images
Provisioning tools - deploy immutable infrastructure resources (servers, databases, etc)

## Questions & Notes

Configuration management tools: Ansible, Salt, Puppet, etc.
While these can also be used to provision resources, it is not recommended

Server templating tools: Docker, Vagrant, etc.

Provisioning tools: Terraform, OpenTofu (TF fork), etc.

### Parent Note

- [IaC Study Journey](./README.md)
