---
title: "logging"
date: "2026-02-25"
type: study_notes
tags: [study, IaC]
---

# logging

## Key Concepts

Terraform has a built-in method for enabling logging through an environment variable

## Commands & Examples

`export TF_LOG=<log_level>` sets the logging level
`export TF_LOG_PATH=/tmp/terraform.log` this will export the logs to a file you specify

use `unset TF_LOG_PATH` and `unset TF_LOG` to unset the logging variables

## Questions & Notes

Log level options are; info, warning, error, debug, and trace
Trace is the most robust option

### Parent Note

- [IaC Study Journey](./README.md)
