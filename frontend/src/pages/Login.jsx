import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../context/Auth";
export default function Login() {
  const { user, login } = useAuth(); const nav = useNavigate();
  const [email, setEmail] = useState(""); const [pw, setPw] = useState(""); const [err, setErr] = useState("");
  if (user) return <Navigate to="/dashboard" replace />;
  const submit = async (e) => { e.preventDefault(); try { await login(email, pw); nav("/dashboard"); } catch (x) { setErr(x.message); } };
  return (<div style={{ display: "grid", placeItems: "center", minHeight: "100vh" }}><form className="card" onSubmit={submit} style={{ width: 360 }}>
    <h2>VanMitra Government Portal</h2><p className="muted">Development build — demo accounts only</p>
    <label>Email<br /><input style={{ width: "100%" }} type="email" required value={email} onChange={e => setEmail(e.target.value)} /></label><br /><br />
    <label>Password<br /><input style={{ width: "100%" }} type="password" required value={pw} onChange={e => setPw(e.target.value)} /></label>
    {err && <p className="err" role="alert">{err}</p>}<br /><button className="btn">Sign in</button></form></div>);
}
