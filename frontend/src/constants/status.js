export const STATUS = {
  DRAFT: ["Draft", "neutral", "✎"], EVIDENCE_COLLECTION: ["Evidence collection", "neutral", "✎"], MAPPING_IN_PROGRESS: ["Mapping in progress", "neutral", "✎"],
  FRC_VERIFICATION: ["FRC verification", "info", "◆"], GS_READY: ["GS ready", "info", "◆"], GS_RESOLVED: ["GS resolved", "success", "✓"],
  SUBMITTED_SDLC: ["Submitted to SDLC", "warning", "◷"], SDLC_UNDER_EXAM: ["SDLC under examination", "warning", "◷"],
  SDLC_FORWARDED: ["SDLC forwarded", "info", "→"], DLC_UNDER_CONSIDERATION: ["DLC under consideration", "warning", "◷"],
  TITLE_APPROVED: ["Title approved", "success", "✓"], RECORD_UPDATED: ["Record updated", "success", "✓"], CFR_ACTIVE: ["CFR active", "success", "✓"],
  REMANDED_TO_GS: ["Remanded to Gram Sabha", "error", "↩"], MODIFIED_REJECTED: ["Modified / rejected", "error", "✕"], PETITION_FILED: ["Petition filed", "info", "§"],
};
export const ACTIONS = { START_EXAMINATION: "Start examination", FORWARD: "Forward to DLC", REMAND: "Remand", START_CONSIDERATION: "Start DLC consideration", APPROVE: "Approve", RECORD_UPDATE: "Mark record updated", ACTIVATE: "Mark CFR active" };
