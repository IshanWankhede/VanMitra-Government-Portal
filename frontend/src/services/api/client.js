const BASE = import.meta.env.VITE_API_BASE_URL; // only way the UI reaches the backend
export async function api(path, { method = "GET", body } = {}) {
  const t = localStorage.getItem("token");
  const r = await fetch(BASE + path, { method, headers: { "Content-Type": "application/json", ...(t && { Authorization: `Bearer ${t}` }) }, body: body && JSON.stringify(body) });
  const j = await r.json().catch(() => ({}));
  if (r.status === 401 && path !== "/auth/login") { localStorage.removeItem("token"); window.location.href = "/login"; }
  if (!r.ok) throw new Error(j.error?.message || `Request failed (${r.status})`);
  return j;
}
