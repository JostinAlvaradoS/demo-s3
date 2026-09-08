variable "region" {
  description = "Región de AWS donde se despliega el stack"
  type        = string
  default     = "us-east-1"
}

variable "entorno" {
  description = "Entorno objetivo: dev, qa o prod"
  type        = string
}

variable "jwt_secret" {
  description = "Secreto de firma de los tokens. Se pasa por tfvars, nunca se versiona"
  type        = string
  sensitive   = true
}
