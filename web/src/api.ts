// Única puerta de salida al backend. Ningún otro módulo llama fetch directo.

const BASE_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export interface LoginResponse {
  token: string;
}

export class ApiError extends Error {
  constructor(
    message: string,
    readonly status: number,
  ) {
    super(message);
  }
}

export async function post<T>(path: string, body: unknown): Promise<T> {
  const response = await fetch(`${BASE_URL}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    throw new ApiError(`La petición a ${path} falló`, response.status);
  }

  return (await response.json()) as T;
}
