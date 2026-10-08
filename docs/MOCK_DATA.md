# Demo data

Password for all demo users: `Dev@12345` (development only).

| Email | Name | Role |
|---|---|---|
| admin@dev.local | Dev Admin | GOVERNMENT_ADMIN |
| sdo@dev.local | Dev SDO | SDO_OFFICER |
| dfo@dev.local | Dev DFO | DFO_DCF |
| dtwo@dev.local | Dev DTWO | DISTRICT_TRIBAL_WELFARE_OFFICER |
| collector@dev.local | Dev Collector | DISTRICT_COLLECTOR |

24 claims `CFR-2026-0001` to `0024` (Gadchiroli, Gondia): 4 Submitted to SDLC, 3 SDLC under examination, 3 Remanded, 4 SDLC forwarded, 3 DLC under consideration, 3 Title approved, 2 Record updated, 2 CFR active. No Gram Sabha stages. Every claim has a timeline; actors are the demo users so each role has a Handled list. Seed: `python -m app.seed`.

Try: sdo@dev.local on a Submitted claim (start examination, then forward or send back); dfo@dev.local sees only forwarded claims onward; collector@dev.local sees nothing at the SDO stage.
Not yet seeded: documents, evidence, maps, titles, signatures, notifications.
