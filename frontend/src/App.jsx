import { Navigate, NavLink, Outlet, Route, Routes } from "react-router-dom";
import { useAuth } from "./context/Auth";
import Login from "./pages/Login"; import Dashboard from "./pages/Dashboard"; import Claims from "./pages/Claims"; import ClaimDetail from "./pages/ClaimDetail";

function Layout() {
  const { user, ready, logout } = useAuth();
  if (!ready) return <p style={{ padding: 24 }}>Loading…</p>;
  if (!user) return <Navigate to="/login" replace />;
  const toggle = () => { const t = document.documentElement.dataset.theme === "dark" ? "light" : "dark"; document.documentElement.dataset.theme = t; localStorage.setItem("theme", t); };
  return (<div className="shell">
    <nav className="side" aria-label="Main"><h1>VanMitra<br /><small>Government Portal</small></h1>
      <NavLink to="/dashboard">Dashboard</NavLink><NavLink to="/claims">Claims</NavLink></nav>
    <div><header className="top"><span>{user.name} · {user.role}</span>
      <span className="row" style={{ margin: 0 }}><button className="btn sec" style={{ color: "#F4F7F5" }} onClick={toggle}>Theme</button><button className="btn sec" style={{ color: "#F4F7F5" }} onClick={logout}>Logout</button></span></header>
      <main><Outlet /></main></div></div>);
}
export default function App() {
  return (<Routes><Route path="/login" element={<Login />} />
    <Route element={<Layout />}><Route path="/dashboard" element={<Dashboard />} /><Route path="/claims" element={<Claims />} /><Route path="/claims/:claimId" element={<ClaimDetail />} /></Route>
    <Route path="*" element={<Navigate to="/dashboard" replace />} /></Routes>);
}
