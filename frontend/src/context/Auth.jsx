import { createContext, useContext, useEffect, useState } from "react";
import { authApi } from "../services/api/authApi";
const Ctx = createContext(null);
export const useAuth = () => useContext(Ctx);
export function AuthProvider({ children }) {
  const [user, setUser] = useState(null); const [ready, setReady] = useState(false);
  useEffect(() => { (localStorage.getItem("token") ? authApi.me().then(r => setUser(r.data)).catch(() => localStorage.removeItem("token")) : Promise.resolve()).finally(() => setReady(true)); }, []);
  const login = async (e, p) => { const r = await authApi.login(e, p); localStorage.setItem("token", r.data.token); setUser(r.data.user); };
  const logout = async () => { try { await authApi.logout(); } catch {} localStorage.removeItem("token"); setUser(null); };
  return <Ctx.Provider value={{ user, ready, login, logout }}>{children}</Ctx.Provider>;
}
