# infra — Terraform + AWS

- Nombres de recurso: `sofka-<entorno>-<recurso>`. El entorno viene de `var.entorno`.
- Todo recurso lleva tags `Proyecto` y `Entorno`.
- Los secretos van a SSM como `SecureString`, nunca a un output ni a un archivo versionado.
- Nunca `terraform apply` sin un `plan` revisado antes.
