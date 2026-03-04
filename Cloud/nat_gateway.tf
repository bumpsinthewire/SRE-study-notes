resource "aws_nat_gateway" "SRE-NAT-gateway" {
  subnet_id  = aws_subnet.private.id
  depends_on = [aws_internet_gateway.SRE-internet-gateway]

  tags = {
    Name = "${var.prefix}-NGW"
  }
}
