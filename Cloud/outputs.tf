output "vpc_id" {
  value = aws_vpc.SRE-notes-example.id
}

output "public_subnets_ids" {
  value = aws_subnet.pubs[*].id
}
