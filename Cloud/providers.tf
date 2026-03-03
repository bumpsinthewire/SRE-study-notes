terraform {
  required_version = "~> 1.0"

  backend "s3" {
    bucket         = "bumpsinthewire-sre-study-notes-state-bucket"
    key            = "global/s3/terraform.tfstate"
    region         = var.region
    dynamodb_table = "terraform_state_locks"
    encrypt        = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.region
}
