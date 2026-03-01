---
title: "provisioners"
date: "2026-02-26"
type: study_notes
tags: [study, IaC]
---

# provisioners

## Key Concepts

Provisioners allow Terraform to run commands on the resources directly

## Commands & Examples

```terraform
# example resource with provisioner
resource "aws_instance" "webserver" {
    ami = "ami-xxx"
    instance_type = "t2.micro"
    provisioner "remote-exec" {
        inline = [ "sudo apt update",
                   "sudo apt install nginx -y",
                   "sudo systemctl enable --now nginx"
                ]
    }
}
```

```terraform
# store the public IP in a local text file
provisioner "local-exec" {
    command = "echo ${aws_instance.webserver.public_ip} >> /tmp/ips.txt"
}
```

```terraform
# runs a command after the resource has been destroyed
provisioner "local-exec" {
    when = destroy
    command = "echo Instance ${aws_instance.webserver.public_ip} Destroyed! > /tmp/instance_state.txt"
}
```

```terraform
# on_failure argument example that continues even if provisioner fails
provisioner "local-exec" {
    on_failure = continue
}
```

## Questions & Notes

By default, provisioners are run after a resource is created. That behavior can be changed with special values in the `when` argument  
Provisioners will also throw an error message and taint a resource when they fail by default.  
Use the `on_failure` argument to change this behavior. Options are `fail` or `continue`

Ideally, you would not use provisioners at all and would use a different tool for configuration management (like Ansible)

### Parent Note

- [IaC Study Journey](./README.md)
