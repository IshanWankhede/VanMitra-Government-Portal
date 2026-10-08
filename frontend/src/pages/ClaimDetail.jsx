import { useCallback, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { claimsApi } from "../services/api/claimsApi";
import { ACTIONS } from "../constants/status";
import StatusBadge from "../components/StatusBadge";
export default function ClaimDetail() {
  const { claimId } = useParams();
  const [c, setC] = useState(null); const [tl, setTl] = useState([]); const [remarks, setRemarks] = useState(""); const [err, setErr] = useState(""); const [msg, setMsg] = useState("");
  const load = useCallback(() => Promise.all([claimsApi.get(claimId), claimsApi.timeline(claimId)]).then(([a, b]) => { setC(a.data); setTl(b.data); }).catch(e => setErr(e.message)), [claimId]);
  useEffect(() => { load(); }, [load]);
  const run = async (a) => {
    if (!window.confirm(`Confirm: ${ACTIONS[a] || a}?`)) return;
    setErr(""); setMsg("");
    try { await claimsApi.act(claimId, a, remarks); setRemarks(""); setMsg("Action recorded."); load(); } catch (e) { setErr(e.message); }
  };
  if (err && !c) return <p className="err" role="alert">{err}</p>; if (!c) return <p>Loading claim…</p>;
  return (<><h2>{c.claimId} <StatusBadge status={c.status} /></h2>
    <div className="row" style={{ alignItems: "flex-start" }}>
      <div className="card" style={{ flex: 2, minWidth: 320 }}><h3>Overview</h3><table><tbody>
        {[["Claimant / community", c.claimant], ["Village", c.village], ["Gram Sabha", c.gramSabha], ["District", c.district], ["Subdivision", c.subdivision], ["Claim type", c.claimType], ["Pending with", c.pendingWith], ["Submitted", c.createdAt?.slice(0, 10)], ["Last updated", c.updatedAt?.slice(0, 10)]].map(([k, v]) => <tr key={k}><td className="muted">{k}</td><td>{v}</td></tr>)}</tbody></table>
        <h3>Workflow timeline</h3><ul className="tl">{tl.map((e, i) => <li key={i}><b>{e.fromStatus ? `${e.fromStatus} → ${e.toStatus}` : e.toStatus}</b><div className="muted">{e.actorName} ({e.actorRole}) · {e.timestamp.slice(0, 16).replace("T", " ")}{e.remarks ? ` · ${e.remarks}` : ""}</div></li>)}</ul></div>
      <div className="card" style={{ flex: 1, minWidth: 260 }}><h3>Actions</h3>
        {c.allowedActions.length ? <><label>Remarks<br /><textarea style={{ width: "100%" }} rows={3} value={remarks} onChange={e => setRemarks(e.target.value)} /></label>
          <div className="row" style={{ marginTop: 12 }}>{c.allowedActions.map(a => <button key={a} className={a === "REMAND" ? "btn sec" : "btn"} onClick={() => run(a)}>{ACTIONS[a] || a}</button>)}</div></>
          : <p className="muted">No actions available to your role at this stage.</p>}
        {msg && <p role="status">{msg}</p>}{err && <p className="err" role="alert">{err}</p>}
        <p className="muted">Allowed actions are decided by the backend. Roles per action are development assumptions.</p></div></div></>);
}
