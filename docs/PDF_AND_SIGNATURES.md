# Title document and signatures

PDF generation and signing are separate. Flow: claim data > PDF template > unsigned PDF > signature provider > signed PDF.

## Title layout (from the provided form, "Title for Forest Land Under Occupation")
Eleven numbered fields: holder name(s) incl. spouse; father/mother; dependents; address; village/gram sabha; gram panchayat; tehsil/taluka; district; Scheduled Tribe or Other Traditional Forest Dweller; area; boundary description by landmarks incl. khasra/compartment no. Then the heritability note ("heritable, but not alienable or transferable under sub-section (4) of Section 4 of the Act") and the declaration by "the undersigned, for and on behalf of the Government of Maharashtra".
Signature blocks: DFO/DCF (top-left), District Tribal Welfare Officer (top-right), District Collector/Deputy Commissioner (centred below).

**Open question:** this form is the individual-rights title. Earlier project notes referred to the Community Forest Resources title (Annexure IV). Confirm which applies to CFR claims. The template is chosen by key (`INDIVIDUAL_FOREST_LAND_TITLE`, others addable) so either can be used. For community claims, individual-only fields show "Not applicable (community claim)".

## Signatures
Each of the three officers signs once per round (draw, type or upload a signature image, plus a consent checkbox). Mock provider: `signatureType="MOCK"`, always labelled "Development / Mock Signature, not a legally valid digital signature". Third signature moves the claim to TITLE_APPROVED and generates the title. A send-back voids the round's signatures (kept in audit). `SignatureProvider` interface lets an approved eSign/DSC provider replace the mock without redesign.

## PDF
Server-side (ReportLab or WeasyPrint with HTML templates in `backend/app/templates/`), not a page screenshot. Versioned (v1, v2), stored via `DocumentStorageService`. Footer: "Digital record. Signed originals follow the statutory process."
