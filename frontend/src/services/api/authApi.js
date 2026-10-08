import { api } from "./client";
export const authApi = { login: (email, password) => api("/auth/login", { method: "POST", body: { email, password } }), me: () => api("/auth/me"), logout: () => api("/auth/logout", { method: "POST" }) };
