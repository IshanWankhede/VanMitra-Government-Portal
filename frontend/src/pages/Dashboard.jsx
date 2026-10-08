import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { claimsApi } from "../services/api/claimsApi";
import { useAuth } from "../context/Auth";
import StatusBadge from "../components/StatusBadge";
const sum = (b, ks) => ks.reduce((n, k) => n + (b[k] || 0), 0);
// KPI sets differ per role. All numbers come from the role-scoped API response.
const KPIS = {
  SDO_OFFICER: (d, b) => [["New claims", b.SUBMITTED_SDLC || 0], ["Under examination", b.SDLC_UNDER_EXAM || 0], ["Forwarded to DLC", sum(b, ["SDLC_FORWARDED", "DLC_UNDER_CONSIDERATION"])], ["Sent back", b.REMANDED_TO_GS || 0]],
  DLC: (d, b) => [["Awaiting your action", d.inboxCount], ["Handled by you", d.handledCount], ["Titles approved", sum(b, ["TITLE_APPROVED", "RECORD_UPDATED", "CFR_ACTIVE"])], ["Sent back", b.REMANDED_TO_GS || 0]],
  GOVERNMENT_ADMIN: (d, b) => [["Total claims", sum(b, Object.keys(b))], ["Needs action", d.inboxCount], ["With SDO", sum(b, ["SUBMITTED_SDLC", "SDLC_UNDER_EXAM"])], ["With DLC", sum(b, ["SDLC_FORWARDED", "DLC_UNDER_CONSIDERATION"])]],
};
export default function Dashboard() {
  const { user } = useAuth(); const [d, setD] = useState(null); const [err, setErr] = useState("");
  useEffect(() => { claimsApi.dashboard().then(r => setD(r.data)).catch(e => setErr(e.message)); }, []);
  if (err) return <p className="err" role="alert">{err}</p>; if (!d) return <p>Loading dashboard…</p>;
  const k = (KPIS[user.role] || KPIS.DLC)(d, d.byStatus);
  const List = ({ rows, empty }) => rows.length ? <table><thead><tr><th>Claim</th><th>Village</th><th>Status</th></tr></thead><tbody>{rows.map(c => <tr key={c.claimId}><td><Link to={`/claims/${c.claimId}`}>{c.claimId}</Link></td><td>{c.village}</td><td><StatusBadge status={c.status} /></td></tr>)}</tbody></table> : <p className="muted">{empty}</p>;
  return (<><h2>Hello, {user.name}</h2><div className="kpis">{k.map(([l, v]) => <div className="card kpi" key={l}><b>{v}</b><span className="muted">{l}</span></div>)}</div>
    <div className="row" style={{ alignItems: "flex-start" }}>
      <div className="card" style={{ flex: 1, minWidth: 320 }}><h3>Needs your action</h3><List rows={d.inbox} empty="You're all caught up." /><Link to="/claims">View all</Link></div>
      <div className="card" style={{ flex: 1, minWidth: 320 }}><h3>Recently handled</h3><List rows={d.recentHandled} empty="Nothing handled yet." /></div></div></>);
}
