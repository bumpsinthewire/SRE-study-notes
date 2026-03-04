resource "aws_vpc" "SRE-notes-VPC" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "${var.prefix}-notes-VPC"
  }
}
