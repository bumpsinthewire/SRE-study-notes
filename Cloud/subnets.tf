data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_subnet" "pub" {
  vpc_id            = aws_vpc.SRE-notes-example.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = data.aws_availability_zones.available.names[0]

  tags = {
    Name = "${var.prefix}-pub-subnet"
  }
}
