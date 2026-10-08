"""Workflow state machine (government side). State names come from the project workflow.
Role-per-action rules are DEVELOPMENT ASSUMPTIONS, configurable here and enforced by the backend.
Gram Sabha stages happen in the community app and never appear in this portal."""
SDO = ["SDO_OFFICER"]
DLC3 = ["DFO_DCF", "DISTRICT_TRIBAL_WELFARE_OFFICER", "DISTRICT_COLLECTOR"]  # the three title signatories
ADMIN = ["GOVERNMENT_ADMIN"]
ROLES = SDO + DLC3 + ADMIN

# status -> { action: (new_status, allowed_roles, pending_with) }
TRANSITIONS = {
    "SUBMITTED_SDLC": {"START_EXAMINATION": ("SDLC_UNDER_EXAM", SDO, "SDO (SDLC)")},
    "SDLC_UNDER_EXAM": {
        "REMAND": ("REMANDED_TO_GS", SDO, "Gram Sabha"),
        "FORWARD": ("SDLC_FORWARDED", SDO, "DLC"),
    },
    "SDLC_FORWARDED": {"START_CONSIDERATION": ("DLC_UNDER_CONSIDERATION", DLC3, "DLC")},
    "DLC_UNDER_CONSIDERATION": {
        "REMAND": ("REMANDED_TO_GS", DLC3, "Gram Sabha"),
        # PLACEHOLDER: single-step approval. Phase 5 replaces this with the 3-signature flow
        # (DFO/DCF + DTWO + Collector must each sign before TITLE_APPROVED).
        "APPROVE": ("TITLE_APPROVED", DLC3, "Records office"),
    },
    "TITLE_APPROVED": {"RECORD_UPDATE": ("RECORD_UPDATED", ADMIN, "Records office")},
    "RECORD_UPDATED": {"ACTIVATE": ("CFR_ACTIVE", ADMIN, "None")},
}
REMARKS_REQUIRED = {"REMAND"}

def allowed_actions(status, role):
    return [a for a, (_, roles, _) in TRANSITIONS.get(status, {}).items() if role in roles]

def inbox_states(role):
    return [s for s in TRANSITIONS if allowed_actions(s, role)]
