# Assumptions and open questions (please confirm)
1. **Role-per-action rules** (who can start, forward, sign, update records) are development assumptions; edit `backend/app/workflow.py` when the authority matrix is confirmed.
2. **Three signatories** (DFO/DCF, DTWO, Collector) all required, any order, once per round.
3. **Send-back goes to Gram Sabha** from both SDO and DLC members.
4. **Admin (records office)** performs "record updated" and "CFR active".
5. **Which title form applies** to CFR claims: the individual "Title for Forest Land Under Occupation" (provided) or the Community Forest Resources title (Annexure IV).
6. **SDLC acts through the SDO** in this portal (one SDO role).
7. **Jurisdiction filtering** (district/subdivision) is planned, not enforced yet.
8. Mock signatures are not legally valid; approved eSign/DSC mechanism unknown.
9. Colours are approximated from screenshots; reconcile with Flutter `ThemeData`.
