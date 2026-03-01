---
title: "dynamic_blocks"
date: "2026-02-27"
type: study_notes
tags: [study, IaC]
---

# dynamic_blocks

## Key Concepts

Dynamic blocks let you loop over multiple values from a variable in an easy way

## Commands & Examples

**Go from this:**

```terraform
resource "aws_security_group" "backend-sg" {
    name = "backend-sg"
    vpc_id = aws_vpc.backend-vpc.id

    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
```

**to this:**

```terraform
variable "ingress_ports" {
    type = list
    default = [22, 8080]
}

resource "aws_security_group" "backend-sg" {
    name = "backend-sg"
    vpc_id = aws_vpc.backend-vpc.id
    dynamic "ingress" {
        for_each = var.ingress_ports
        content {
            from_port = ingress.value
            to_port = ingress.value
            protocol = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
        }
    }
}
```

## Questions & Notes

instead of using the name of the **dynamic** block, you can also use `iterator = <name>` to use something else

### Parent Note

- [IaC Study Journey](./README.md)
