import { login } from "./login";

const form = document.querySelector<HTMLFormElement>("#login-form");
const error = document.querySelector<HTMLParagraphElement>("#error");

form?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = new FormData(form);

  try {
    await login(String(data.get("email")), String(data.get("password")));
    window.location.href = "/bienvenida.html";
  } catch (cause) {
    if (error) {
      error.textContent = cause instanceof Error ? cause.message : "Error inesperado";
    }
  }
});
