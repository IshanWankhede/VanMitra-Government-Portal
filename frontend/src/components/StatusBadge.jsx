import { STATUS } from "../constants/status";
export default function StatusBadge({ status }) {
  const [label, tone, icon] = STATUS[status] || [status, "neutral", "•"];
  return <span className={`badge t-${tone}`}><span aria-hidden>{icon}</span>{label}</span>;
}
