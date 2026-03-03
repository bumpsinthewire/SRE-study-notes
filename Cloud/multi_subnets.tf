data "aws_availability_zones" "availables" {
  state = "available"
}

resource "aws_subnet" "pubs" {
  count             = length(data.aws_availability_zones.available.names)
  vpc_id            = aws_vpc.SRE-notes-example.id
  availability_zone = data.aws_availability_zones.available.names[count.index]
  cidr_block        = cidrsubnet(aws_vpc.SRE-notes-example.cidr_block, 8, count.index + 1)
  tags = {
    Name = "${var.prefix}-pub-subnet-${count.index}"
  }
}
