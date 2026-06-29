terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "fifa_data" {
  bucket = var.s3_bucket_name
}

resource "aws_athena_workgroup" "fifa_analytics" {
  name = "fifa_analytics"
  state = "ENABLED"
}
