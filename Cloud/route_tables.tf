resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.SRE-notes-VPC.id

  tags = {
    Name = "${var.prefix}-public-subnet-route-table"
  }
}

resource "aws_route_table" "private_route_table" {
  vpc_id = aws_vpc.SRE-notes-VPC.id

  tags = {
    Name = "${var.prefix}-private-subnet-route-table"
  }
}

resource "aws_route_table_association" "IGW_assoc" {
  gateway_id     = aws_internet_gateway.SRE-internet-gateway.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_route_table_association" "NGW_assoc" {
  gateway_id     = aws_nat_gateway.SRE-NAT-gateway.id
  route_table_id = aws_route_table.private_route_table.id
}
