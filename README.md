# Login demo — monorepo

Monorepo mínimo con tres piezas que no comparten lenguaje ni herramientas:

| Carpeta | Stack | Qué hace |
|---|---|---|
| `web/` | TypeScript + Vite | Formulario de ingreso y manejo del token |
| `api/` | Python + FastAPI | Endpoint `/login`, verificación de credenciales y emisión de JWT |
| `infra/` | Terraform + AWS | Bucket del front y el secreto de firma en SSM |

## Correr

```bash
# api
cd api && uv run uvicorn app.main:app --reload

# web
cd web && npm install && npm run dev

# infra
cd infra && terraform init && terraform plan -var-file=terraform.tfvars
```

Usuarios de prueba: `ana@sofka.com.co` / `luis@sofka.com.co`, contraseña `demo1234`.
