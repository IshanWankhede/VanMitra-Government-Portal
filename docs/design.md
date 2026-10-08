# VanMitra Government Portal — design.md

**Source of truth:** `VanMitra-AI_Theme_UI_Style_Guide.docx` (02 Oct 2026), derived from the Flutter app screenshots.
**Scope:** Visual language for the desktop-first Government Web Portal (React + Vite, JavaScript).
**Goal:** The portal must feel like the government counterpart of the Flutter app: same forest-green / action-orange identity, same semantic tokens, same Light/Dark behaviour.

> **Source note (inherited from the style guide):** hex values are approximated from screenshots. Reconcile them with the Flutter `ThemeData/ColorScheme` before treating them as final. Keep all values in one tokens file so a change is made once.

> **Items marked `[ASSUMPTION]`** are not in the style guide. They are the smallest reasonable adaptation for a desktop government workflow.

---

## 1. Design principles

1. **Forest-first** — green anchors identity: sidebar, top bar, branded surfaces.
2. **Orange as action** — primary buttons, active controls, progress emphasis, selected nav in Dark Mode. Nothing else is orange.
3. **Clear hierarchy** — separate content with spacing and soft surfaces, not heavy borders or decoration.
4. **Dark mode is a full theme** — surfaces, text, nav, inputs, tables, dialogs and states all switch together. No component may look "stuck" in Light.
5. **Operational readability** — officers read dense data for hours. Legibility over ornament. English and Marathi share one hierarchy.
6. **Status is semantic** — success/warning/error/info colours mean state only; never decoration. Status must never rely on colour alone (always add text label and/or icon).

---

## 2. Design tokens

### 2.1 Brand & accent

| Token | Hex | Use |
|---|---|---|
| `brand.primary` | `#1A4331` | Sidebar, top bar, branded surfaces, table header accents |
| `brand.primaryDark` | `#0C1B14` | Dark page scaffolding, deepest surfaces |
| `brand.secondary` | `#2D765C` | Secondary green surfaces, icons, active-in-light nav |
| `accent.primary` | `#FF8D20` | Primary buttons, active states, progress, focus emphasis |
| `accent.dark` | `#D96B00` | Pressed / strong orange (use sparingly) |

### 2.2 Light theme

| Token | Hex | Use |
|---|---|---|
| `light.background` | `#F4F7F5` | Page background (soft neutral, never pure white) |
| `light.surface` | `#FFFFFF` | Cards, tables, dialogs |
| `text.primary` | `#13202B` | Headings and body |
| `text.muted` | `#66737C` | Metadata, helper text, captions |
| `outline` `[ASSUMPTION]` | `#DCE5E0` | Hairline separators (derive; guide prefers spacing over borders) |

### 2.3 Dark theme

| Token | Hex | Use |
|---|---|---|
| `dark.background` | `#10261B` | Content background |
| `dark.scaffold` | `#0C1B14` | Outer shell / deepest layer |
| `dark.surface` | `#173425` | Cards, tables, dialogs |
| `dark.border` | `#2B5A46` | Card borders, separators |
| `text.onDark` | `#F4F7F5` | Headings and body |
| `text.mutedDark` | `#AAB8B2` | Metadata |

### 2.4 Status (same in both themes)

| Token | Hex | Meaning |
|---|---|---|
| `status.success` | `#5FAE3B` | Synced, approved, signed, verified |
| `status.warning` | `#F0B323` | Pending, under review |
| `status.error` | `#D7262E` | Critical, rejected, failed |
| `status.info` | `#2F5FB3` | Informational, forwarded |

### 2.5 Semantic tokens (what components consume)

Components use **only** these names, never raw hex. They match the Flutter contract.

`background, surface, surfaceContainer, surfaceElevated, primary, secondary, onBackground, onSurface, onSurfaceVariant, outline, success, warning, error, info, actionPrimary, navSelected, navUnselected`

| Semantic | Light | Dark |
|---|---|---|
| `background` | `#F4F7F5` | `#10261B` |
| `surface` | `#FFFFFF` | `#173425` |
| `surfaceContainer` `[ASSUMPTION]` | `#EBF1EE` | `#1C3D2C` |
| `surfaceElevated` `[ASSUMPTION]` | `#FFFFFF` + soft shadow | `#173425` + border |
| `primary` | `#1A4331` | `#2D765C` `[ASSUMPTION]` |
| `secondary` | `#2D765C` | `#2D765C` |
| `onBackground` / `onSurface` | `#13202B` | `#F4F7F5` |
| `onSurfaceVariant` | `#66737C` | `#AAB8B2` |
| `outline` | `#DCE5E0` | `#2B5A46` |
| `actionPrimary` | `#FF8D20` | `#FF8D20` |
| `navSelected` | `#2D765C` (green) | `#FF8D20` (orange) |
| `navUnselected` | `#66737C` | `#AAB8B2` |

### 2.6 CSS variables (drop into `src/styles/tokens.css`)

```css
:root,
[data-theme="light"] {
  --background: #F4F7F5;
  --surface: #FFFFFF;
  --surface-container: #EBF1EE;
  --primary: #1A4331;
  --secondary: #2D765C;
  --on-surface: #13202B;
  --on-surface-variant: #66737C;
  --outline: #DCE5E0;
  --action-primary: #FF8D20;
  --action-pressed: #D96B00;
  --nav-selected: #2D765C;
  --nav-unselected: #66737C;
  --success: #5FAE3B;
  --warning: #F0B323;
  --error: #D7262E;
  --info: #2F5FB3;
  --shadow-card: 0 1px 3px rgba(19, 32, 43, 0.08), 0 4px 12px rgba(19, 32, 43, 0.05);
}

[data-theme="dark"] {
  --background: #10261B;
  --surface: #173425;
  --surface-container: #1C3D2C;
  --primary: #2D765C;
  --secondary: #2D765C;
  --on-surface: #F4F7F5;
  --on-surface-variant: #AAB8B2;
  --outline: #2B5A46;
  --nav-selected: #FF8D20;
  --nav-unselected: #AAB8B2;
  --shadow-card: none; /* dark mode uses border, not shadow */
}

/* Branded chrome stays green in BOTH themes */
:root {
  --chrome-bg: #1A4331;
  --chrome-bg-dark: #0C1B14;
  --chrome-text: #F4F7F5;
  --chrome-text-muted: #AAB8B2;
}
```

Theme switching: one `ThemeProvider` sets `data-theme` on `<html>`; persist the choice. **No per-screen `isDark` state.** Toggle must work without a reload.

### 2.7 Colour rules

- No pure black text on dark green surfaces.
- No white cards in Dark Mode (except an intentional alert/exception).
- Selected nav: **orange in Dark**, **green in Light**. Unselected: muted grey in both.
- Status colours convey state only.
- Green/orange branding is identical across English and Marathi.
- `[ASSUMPTION]` Orange `#FF8D20` with white text is ~2.3:1. For small text buttons, use `accent.dark #D96B00` background or bold ≥16px labels, and always provide a visible focus ring. Re-check contrast against WCAG AA when finalising.

---

## 3. Typography

One semantic scale for English and Marathi. Never create a separate Marathi hierarchy.

| Element | Size | Weight | Notes |
|---|---|---|---|
| Page title | 24px | 700 | One per screen |
| Section heading | 18–20px | 600–700 | e.g. "Documents & Evidence" |
| Card title | 15–18px | 600–700 | |
| Primary value (KPI) | 30–34px | 700 | Dashboard counts |
| Body / supporting | 14–16px | 400–500 | Default 14px for dense tables, 15–16px in forms |
| Caption / metadata | 12–13px | 400–500 | Dates, IDs, helper text, muted colour |
| Button label | 14–15px | 600–700 | |

Font stack `[ASSUMPTION]` (guide says "clean sans-serif"; confirm the Flutter font):

```css
font-family: "Inter", "Noto Sans", "Noto Sans Devanagari", system-ui, sans-serif;
```

- Devanagari line-height ≥ 1.6; never clip glyphs.
- Keep the bilingual pattern where the product uses it, e.g. `Language Selection / भाषा निवड`.
- Claim IDs, area figures and dates use tabular numerals (`font-variant-numeric: tabular-nums`).

---

## 4. Shape, spacing, elevation

- **Radius:** medium-to-large rounded rectangles. `[ASSUMPTION]` tokens: `--r-sm 8px`, `--r-md 12px`, `--r-lg 16px`, `--r-pill 999px`. Cards 16px, inputs/buttons 12px, badges pill.
- **Spacing scale** `[ASSUMPTION]`: 4 / 8 / 12 / 16 / 24 / 32 / 48. Separate cards with 16–24px gaps instead of heavy borders.
- **Elevation:** Light = soft shadow (`--shadow-card`). Dark = low-contrast `--outline` border, no bright shadows.

---

## 5. Component rules

| Component | Surface | Text | Accent | Rule |
|---|---|---|---|---|
| **Top bar** | `#1A4331` (Light) / `#0C1B14` (Dark) | Off-white title, muted green-white metadata | Orange outlined circular settings button | Stays branded in both themes |
| **Sidebar** | Same forest-green family | Off-white; muted for inactive | Active item: orange indicator/text in Dark, orange or light-green highlight in Light | Replaces Flutter's bottom nav. Keep ≤ 7 items. Collapsible to icons |
| **Cards** | `surface` | `onSurface` / `onSurfaceVariant` | Orange, green, blue or status icon | Dark: elevated dark surface + border |
| **Primary button** | `#FF8D20` | White | Pressed `#D96B00` | One primary action per view region |
| **Secondary / outlined** | Transparent / surface | `onSurface` | Green or orange border | Avoid dense outlines |
| **Destructive** | `error` | White | — | Always behind a confirmation dialog |
| **Inputs / search** | `surface` | `onSurface` / muted placeholder | Green/orange focus ring | Dark: dark surface + light text |
| **Chips / filters** | Light tinted surface | `onSurface` | Selected = brand or status colour | Selected state clear without relying on colour alone (check icon / weight) |
| **Tables** | `surface`, header `surfaceContainer` | 14px body | Row hover `surfaceContainer` | Sticky header, sortable columns, zebra optional |
| **Dialogs / drawers** | `surface` | Theme text | Orange primary action | Follow active theme |
| **Map overlays** | `surface` over map | High contrast | Status colours + orange actions | Satellite/base imagery stays natural; only overlays theme |
| **Focus ring** | — | — | 2px orange `#FF8D20` outline + 2px offset | Visible on every interactive element |

---

## 6. Status badges (workflow → colour)

Badges are pill-shaped: **icon + text label + tinted background**. Colour is never the only signal.

Workflow stage names are provisional until the project documents are supplied (see `WORKFLOW.md`).

| State | Colour token | Label (EN) | Icon |
|---|---|---|---|
| `DRAFT`, `EVIDENCE_COLLECTION`, `MAPPING_IN_PROGRESS` | neutral (`onSurfaceVariant`) | Draft / In preparation | pencil |
| `FRC_VERIFICATION`, `GS_READY` | `info` | In verification | shield-check |
| `GS_RESOLVED` | `success` | Gram Sabha resolved | check-circle |
| `SUBMITTED_SDLC` | `warning` | Submitted — pending review | inbox |
| `SDLC_UNDER_EXAM`, `DLC_UNDER_CONSIDERATION` | `warning` | Under examination | clock |
| `SDLC_FORWARDED` | `info` | Forwarded | arrow-right |
| `REMANDED_TO_GS` | `error` | Remanded — correction required | undo |
| `MODIFIED_REJECTED` | `error` | Modified / rejected | x-circle |
| `PETITION_FILED` | `info` | Petition filed | file-text |
| `TITLE_APPROVED` | `success` | Title approved | badge-check |
| `RECORD_UPDATED`, `CFR_ACTIVE` | `success` | Record updated / CFR active | check-circle |

Signature status: `Signed` (success + check), `Pending` (warning + clock), `Not required` (neutral). Mock signatures must show a visible **"MOCK"** tag.

---

## 7. Desktop layout adaptation `[ASSUMPTION]`

The Flutter app is mobile-first with a 5-item bottom nav. The portal adapts this:

```
┌────────────┬──────────────────────────────────────────────┐
│            │ Top bar: breadcrumb · search · theme · alerts │
│  Sidebar   │ · user menu                                  │
│  (240px,   ├──────────────────────────────────────────────┤
│  collapses │ Page title + primary action                  │
│  to 72px)  │ ┌─────────── content, max-width 1440 ─────┐ │
│            │ │ cards / table / multi-column workspace   │ │
└────────────┴──────────────────────────────────────────────┘
```

- **Sidebar** (not bottom nav): Dashboard · Claims · Gram Sabha/Verification (if in scope) · Atlas Map · Titles & Signatures · Notifications · Settings. Mirrors the Flutter sections.
- **Grid:** 12 columns, 24px gutters. Breakpoints: ≥1280 desktop (primary), 768–1279 tablet (sidebar collapses to icons), <768 secondary (sidebar becomes a drawer).
- **Dashboard:** KPI cards (value 32px bold, icon in tinted circle) → recent claims table → pending-actions list. Charts only where they clarify.
- **Claims list:** search + filter chips row, dense table (Claim ID, Village, Gram Sabha, District, Claim Type, Submitted, Stage, Status badge, Pending Action, Action), pagination.
- **Claim workspace:** header (ID, status badge, current authority) + tabs: Overview · Gram Sabha · Documents & Evidence · Verification · Map · Timeline · Review. Right-hand sticky **Actions** panel (Forward / Remand / Approve) so officers never scroll to act.
- **Timeline:** vertical stepper; completed = green check, current = orange dot, upcoming = hollow muted circle. Built from real workflow events only.
- **Map:** overlays use `surface`; participatory/community boundaries must be labelled as community-mapped, not an official cadastral survey.

---

## 8. Accessibility

- Visible focus (orange ring) on all controls; full keyboard operation.
- Status = colour + icon + text.
- Confirmation dialogs for Forward, Remand, Approve and any destructive action.
- Loading skeletons, empty states, error states on every data view.
- Check Marathi and English for contrast and clipping in both themes.
- Respect `prefers-reduced-motion`; keep animation minimal.

---

## 9. Theme QA checklist (from the style guide, adapted)

- [ ] Toggle Light → Dark → Light with no reload.
- [ ] Dashboard, Claims, Claim workspace, Map, Titles, Notifications, Settings all switch in one interaction.
- [ ] No large white card or dark text left unintentionally in Dark Mode.
- [ ] Sidebar: orange selected item in Dark, muted-light inactive items.
- [ ] Dialogs, dropdowns, search/inputs, chips, tables, pagination checked in both themes.
- [ ] Map overlays and alert cards readable over satellite imagery.
- [ ] Marathi + English checked for clipping and contrast.
- [ ] No hardcoded `#fff`, `#000` or stray greys in components (grep for them).

**Definition of done:** the user switches theme once and no part of the portal looks stuck in Light Mode. Branding stays green/orange; surfaces, text, navigation and controls change coherently.

---

## 10. Implementation contract (React)

- Tokens live in `src/styles/tokens.css`; components consume CSS variables only.
- A single `ThemeProvider` (context) owns the theme; `data-theme` on `<html>`.
- Shared components: `Button`, `Card`, `StatusBadge`, `DataTable`, `FilterChips`, `Tabs`, `Timeline`, `Dialog`, `Input`, `EmptyState`, `Skeleton`.
- `StatusBadge` takes a workflow state and reads label/colour/icon from one mapping (section 6), so the API's state names are the only input.
- Do not copy Flutter mobile layouts; adapt per section 7.

## 11. Open items to confirm

1. Exact font family used in Flutter.
2. Final hex values after reconciling with `ThemeData/ColorScheme`.
3. Whether the portal should offer a Marathi UI toggle (the guide shows a bilingual pattern in the app).
4. Official government branding/emblem requirements for the portal header (none supplied).
5. Embedded screenshots in the .docx were not reviewed for this version; this file is derived from the guide's text and tokens. Upload them as images if you want pixel-level matching of the Flutter cards and chips.
