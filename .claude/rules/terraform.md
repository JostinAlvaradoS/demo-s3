---
paths: ["infra/**/*.tf"]
---
# Terraform

- Nombres de recurso: `sofka-<entorno>-<recurso>`.
- Todo recurso lleva tags `Proyecto` y `Entorno`.
- Nunca `terraform apply` sin `plan` revisado antes.
