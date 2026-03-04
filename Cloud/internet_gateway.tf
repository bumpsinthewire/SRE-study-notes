resource "aws_internet_gateway" "SRE-internet-gateway" {
  vpc_id = aws_vpc.SRE-notes-VPC.id

  tags = {
    Name = "${var.prefix}-IGW"
  }
}
