import { ApiError, post, type LoginResponse } from "./api";

const TOKEN_KEY = "sofka.token";

export function validateEmail(email: string): boolean {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
}

export async function login(email: string, password: string): Promise<string> {
  if (!validateEmail(email)) {
    throw new Error("El correo no tiene un formato válido");
  }
  if (password.length < 8) {
    throw new Error("La contraseña debe tener al menos 8 caracteres");
  }

  try {
    const { token } = await post<LoginResponse>("/login", { email, password });
    sessionStorage.setItem(TOKEN_KEY, token);
    return token;
  } catch (error) {
    if (error instanceof ApiError && error.status === 401) {
      throw new Error("Correo o contraseña incorrectos");
    }
    throw error;
  }
}

export function storedToken(): string | null {
  return sessionStorage.getItem(TOKEN_KEY);
}

export function logout(): void {
  sessionStorage.removeItem(TOKEN_KEY);
}
