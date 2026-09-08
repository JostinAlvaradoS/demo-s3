terraform {
  required_version = ">= 1.9"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "web" {
  bucket = "sofka-${var.entorno}-login-web"

  tags = {
    Proyecto = "login-demo"
    Entorno  = var.entorno
  }
}

resource "aws_ssm_parameter" "jwt_secret" {
  name  = "/sofka/${var.entorno}/login/jwt-secret"
  type  = "SecureString"
  value = var.jwt_secret

  tags = {
    Proyecto = "login-demo"
    Entorno  = var.entorno
  }
}
