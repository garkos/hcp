terraform {
  required_providers = {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  cloud {
    organization = "markoyhr"

    workspaces {
      name = "hcp-workspace"
    }
  }
}


provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "example" {
  bucket = var.bucket_name
}