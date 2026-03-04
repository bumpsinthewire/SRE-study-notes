resource "aws_internet_gateway" "SRE-gateway" {
  vpc_id = aws_vpc.SRE-notes-example.id

  tags = {
    Name = "${var.prefix}-IGW"
  }
}
