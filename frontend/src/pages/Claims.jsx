import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { claimsApi } from "../services/api/claimsApi";
import { STATUS } from "../constants/status";
import { useAuth } from "../context/Auth";
import StatusBadge from "../components/StatusBadge";
export default function Claims() {
  const { user } = useAuth(); const isAdmin = user.role === "GOVERNMENT_ADMIN";
  const [f, setF] = useState({ search: "", status: "", district: "", page: 1, scope: isAdmin ? "all" : "inbox" });
  const [res, setRes] = useState(null); const [err, setErr] = useState(""); const [busy, setBusy] = useState(true);
  useEffect(() => { setBusy(true); claimsApi.list({ ...f, page_size: 10 }).then(setRes).catch(e => setErr(e.message)).finally(() => setBusy(false)); }, [f]);
  const set = (k, v) => setF({ ...f, [k]: v, page: 1 });
  return (<><h2>Claims</h2><div className="row">{[["inbox", "Needs my action"], ["handled", "Handled"], ...(isAdmin ? [["all", "All"]] : [])].map(([k, l]) => <button key={k} className={f.scope === k ? "btn" : "btn sec"} onClick={() => set("scope", k)}>{l}</button>)}</div><div className="row">
    <input aria-label="Search" placeholder="Search ID, village, Gram Sabha" value={f.search} onChange={e => set("search", e.target.value)} />
    <select aria-label="Status" value={f.status} onChange={e => set("status", e.target.value)}><option value="">All statuses</option>{Object.entries(STATUS).map(([k, v]) => <option key={k} value={k}>{v[0]}</option>)}</select>
    <input aria-label="District" placeholder="District" value={f.district} onChange={e => set("district", e.target.value)} /></div>
    <div className="card">{err ? <p className="err" role="alert">{err}</p> : busy || !res ? <p>Loading…</p> : !res.data.length ? <p>No claims match these filters.</p> :
      <table><thead><tr><th>Claim ID</th><th>Village</th><th>Gram Sabha</th><th>District</th><th>Type</th><th>Status</th><th>Pending with</th><th></th></tr></thead>
        <tbody>{res.data.map(c => <tr key={c.claimId}><td>{c.claimId}</td><td>{c.village}</td><td>{c.gramSabha}</td><td>{c.district}</td><td>{c.claimType}</td><td><StatusBadge status={c.status} /></td><td>{c.pendingWith}</td><td><Link to={`/claims/${c.claimId}`}>Open</Link></td></tr>)}</tbody></table>}
      {res && <div className="row" style={{ marginTop: 12 }}><button className="btn sec" disabled={f.page <= 1} onClick={() => setF({ ...f, page: f.page - 1 })}>Prev</button>
        <span>Page {res.pagination.page} of {res.pagination.totalPages || 1}</span><button className="btn sec" disabled={f.page >= res.pagination.totalPages} onClick={() => setF({ ...f, page: f.page + 1 })}>Next</button></div>}</div></>);
}
