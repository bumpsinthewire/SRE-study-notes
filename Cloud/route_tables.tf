resource "aws_route_table" "route_table" {
  vpc_id = aws_vpc.SRE-notes-example.id

  tags = {
    Name = "${var.prefix}-public-route-table"
  }
}

resource "aws_route_table_association" "pub_assoc" {
  count          = length(aws_subnet.pubs)
  subnet_id      = aws_subnet.pubs[count.index].id
  route_table_id = aws_route_table.route_table.id
}
