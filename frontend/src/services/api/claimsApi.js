import { api } from "./client";
const qs = (p) => new URLSearchParams(Object.entries(p).filter(([, v]) => v)).toString();
export const claimsApi = {
  dashboard: () => api("/government/dashboard"),
  list: (p) => api(`/government/claims?${qs(p)}`), // p.scope: inbox | handled | all (all = admin only)
  get: (id) => api(`/government/claims/${id}`),
  timeline: (id) => api(`/government/claims/${id}/timeline`),
  audit: (id) => api(`/government/claims/${id}/audit`),
  act: (id, action, remarks) => api(`/government/claims/${id}/actions`, { method: "POST", body: { action, remarks } }),
};
