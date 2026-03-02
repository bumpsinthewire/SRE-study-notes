---
title: "auth test"
date: "2026-03-02"
type: project
tags: [project, IaC]
---

# Auth test

## Overview

A quick test to make sure everything is working properly

## The Challenge

Verifying everything will run as intended

## The Solution

Utilizing a datasource to feed an output value

## Key Learnings

Using a datasource and an output together for verification

## Code Implementation

```terraform
data "aws_caller_identity" "current" {}
```

## Results

```terraform
data.aws_caller_identity.current: Reading...
data.aws_caller_identity.current: Read complete after 0s [id=731144082285]

Changes to Outputs:
  + aws_account_id = "xxxxxxxxxxxxxx"
```

### Parent Note

- [Cloud Study Journey](../README.md)
