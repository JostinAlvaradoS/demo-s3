import { describe, expect, it } from "vitest";

import { validateEmail } from "./login";

describe("validateEmail", () => {
  it("acepta un correo corporativo", () => {
    expect(validateEmail("ana@sofka.com.co")).toBe(true);
  });

  it("rechaza un correo sin arroba", () => {
    expect(validateEmail("ana.sofka.com.co")).toBe(false);
  });

  it("rechaza un correo sin dominio", () => {
    expect(validateEmail("ana@")).toBe(false);
  });
});
