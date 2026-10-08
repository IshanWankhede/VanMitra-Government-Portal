# Database (MongoDB Atlas, dev DB `vanmitra_government_dev`)

The dev database is temporary. It can later be replaced by the shared production database through backend config only.

## Implemented collections
**users** `{email (unique), name, role, passwordHash, isDevAccount}`
**claims** `{claimId (unique), claimant, village, gramSabha, district, subdivision, claimType, areaHa, status, pendingWith, createdAt, updatedAt, isMockData}`
**workflowEvents** `{claimId, actorId, actorName, actorRole, action, fromStatus, toStatus, remarks, timestamp}` (append-only)
**auditLogs** same shape as workflowEvents (append-only from the application's view)

## Planned collections
**claimDocuments** `{documentId, claimId, type, fileName, submittedBy, uploadedAt, version, previousVersionIds[], status: PENDING|VERIFIED|REQUIRES_CORRECTION|REJECTED}`
**evidence** `{claimId, type, caption, date, submittedBy}`
**reviews** `{claimId, decision, reasonCategory, remarks, requiredAction, affectedDocuments[], actorId, createdAt}`
**titles** `{claimId, version, templateKey, status, pdfRef, generatedAt}`
**titleSignatures** `{claimId, round, signerRole, signerId, signerName, signatureType: "MOCK", signatureImage, signedAt, voided}`
**notifications** `{userId|role, type, claimId, text, read, createdAt}`

## Indexes (created at startup)
claims: `claimId` unique, `status`, `district`, `subdivision`, `village`, `createdAt`. workflowEvents: `claimId`. auditLogs: `claimId`. users: `email` unique. Planned: `notifications.userId`, `titleSignatures.claimId`.

## Rules
Never overwrite history: corrections add events or new document versions. Audit records have no edit/delete endpoint.

## Example claim
```json
{"claimId":"CFR-2026-0009","claimant":"Chichgarh Gram Sabha community","village":"Chichgarh","district":"Gondia",
 "subdivision":"Deori","claimType":"CFR","areaHa":812.4,"status":"SDLC_FORWARDED","pendingWith":"DLC",
 "createdAt":"2026-08-20T00:00:00+00:00","updatedAt":"2026-09-23T00:00:00+00:00"}
```
