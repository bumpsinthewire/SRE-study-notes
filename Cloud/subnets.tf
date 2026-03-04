resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.SRE-notes-VPC.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = data.aws_availability_zones.available.names[0]

  tags = {
    Name = "${var.prefix}-pub-subnet"
  }
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.SRE-notes-VPC.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = data.aws_availability_zones.available.names[1]

  tags = {
    Name = "${var.prefix}-priv-subnet"
  }
}

# multiple subnets example (creates one for every available AZ)
# resource "aws_subnet" "pubs" {
#   count             = length(data.aws_availability_zones.available.names)
#   vpc_id            = aws_vpc.SRE-notes-example.id
#   availability_zone = data.aws_availability_zones.available.names[count.index]
#   cidr_block        = cidrsubnet(aws_vpc.SRE-notes-example.cidr_block, 8, count.index + 1)
#   tags = {
#     Name = "${var.prefix}-pub-subnet-${count.index}"
#   }
# }
