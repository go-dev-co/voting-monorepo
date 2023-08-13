provider "aws" {
  region                   = "us-east-2" # Specify the region
  shared_config_files      = ["/Users/brycefitzgerald/.aws/config"]
  shared_credentials_files = ["/Users/brycefitzgerald/.aws/credentials"]
  profile                  = "default"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.12.0"
    }
  }
}

# Include the global ECR repository
module "global_ecr" {
  source = "./global/ecr"
}

# Any other global configurations, resources, or modules can be defined here
