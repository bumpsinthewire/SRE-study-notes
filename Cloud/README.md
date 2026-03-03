# Cloud Study Journey

My journey through multi-cloud infrastructure management, covering providers, services, and best practices for scalable, secure SRE deployments.

## Projects

- [Auth test](./auth-test/README.md)

## Study Notes

- [VPC](./vpc.md)
- [subnets](./subnets.md)

### Project Notes

In this study area, I am using terraform to create each of the resources  
In each study notes page, there will be a snippet of the `terraform apply` as well as a link to the `<resource_name>.tf` file  
The state file for this folder is stored in an AWS S3 bucket, and uses DynamoDB for state locking  
The backend setup config is in its own folder, called `bootstrap`

## Progress

- [ ] Public and Private subnets and their gateways
- [ ] Connecting VPC's inside and across regions
- [ ] Moving a volume between EC2's
- [ ] Creating an S3 bucket
- [ ] Create a VM in EC2
- [ ] Lambda functions
- [ ] Scaling DynamoDB with autoscaling
- [ ] Scaling web servers with autoscaling
- [ ] Creating users, groups, and roles
- [ ] Setting up RDS with Secrets manager
- [ ] NACL's and Security groups
- [ ] Enabling encryption and versioning for S3
- [ ] Enhancing edge security with CloudFront and WAF
- [ ] Implementing cross region replication for S3
- [ ] Deploying a Lambda app and testing scalability
- [ ] Setting up multi-AZ cluster deployments with RDS
- [ ] Deploy and update with CloudFormation

## Goals

- Master cloud-native SRE practices.
- Design resilient, cost-effective multi-cloud architectures.
- Gain hands-on experience.
