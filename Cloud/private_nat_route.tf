resource "aws_route" "private_nat_access" {
  route_table_id         = aws_route_table.private_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_nat_gateway.SRE-NAT-gateway.id
}
