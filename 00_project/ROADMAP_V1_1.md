# Sales Codex — Roadmap V1.1

Status: Active  
Opened: 2026-07-06  
Strategic Source of Truth for Version 1.1

---

## 1. Program Mission

Version 1.1 turns the Sales Codex from a successful V1.0 knowledge repository into a more robust, audit-safe, delivery-tested knowledge system.

The program preserves large autonomous work packages while adding internal checkpoints, context resets, explicit escalation rules and independent audits.

---

## 2. Operating Constraints

- Repository is the source of truth.
- Felix controls strategic priority, Reserved Decisions and release decisions.
- Agents control operational execution inside active project briefs.
- No microtask approvals.
- No new research wave before Evidence Resolution and Delivery Probe prerequisites are satisfied.
- No uncontrolled self-evolution of framework, prompts, knowledge model or repository structure.

---

## 3. Control Plane

| Artifact | Role |
|---|---|
| `00_project/ROADMAP_V1_1.md` | Strategic source of truth for V1.1 status, sequence and dependencies |
| `00_project/NEXT_ACTION.md` | Minimal launcher for the active macro-project |
| `00_project/projects/V11-XX_*/PROJECT_BRIEF.md` | Mission-level execution brief |
| `COMPLETION_REPORT.md` | Executor completion evidence |
| `AUDIT_REPORT.md` | Independent review evidence |

No separate `PROJECT_QUEUE.md` exists. Queue state is encoded below.

---

## 4. Program Board

| ID | Macro-Project | Status | Dependencies | Primary Output |
|---|---|---|---|---|
| V11-01 | Baseline & Control Plane Consolidation | COMPLETED — AUDITED (PASS WITH CONDITIONS) | Editor authorization | Clean baseline, synced status, operational V1.1 control plane. Completion report: `00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`. Independently audited before V11-02 started — result PASS WITH CONDITIONS; commit and push performed, condition fulfilled, Git index.lock Hard Block resolved. |
| V11-02 | Evidence Architecture Resolution | COMPLETED — AUDITED (PASS) | V11-01 (completed and audited); Evidence report availability (satisfied — `00_project/EVIDENCE_ARCHITECTURE_CHECK_2026-07-06.md`) | Completion report: `00_project/projects/V11-02_evidence_architecture_resolution/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-02_evidence_architecture_resolution/AUDIT_REPORT.md` (PASS, no blocking findings). All 7 findings disposed (6× partially accept/precisify, 1× no change); `SCIENTIFIC_DEBT.md` updated; no W-005 activated; 3-item Evidence Backlog created (highest-priority item — implementing precisifications into MEC/MOD objects and `LITERATURE_INDEX.md` — deferred pending Editor sign-off, outside V11-02 file scope). |
| V11-03 | Governance + Repository Integrity + Atlas Operationalization | COMPLETED — AUDITED (PASS WITH CONDITIONS, CONDITION CLOSED) | V11-01 (completed and audited); V11-02 (completed and audited) | Completion report: `00_project/projects/V11-03_governance_integrity_atlas/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-03_governance_integrity_atlas/AUDIT_REPORT.md` (PASS WITH CONDITIONS; condition — CURRENT_STATE.md status-consistency cleanup + closure documentation — fulfilled 2026-07-06, condition closed). OD-006/OD-007/OD-009–012 given explicit DoD status (2× Deferred, 4× Needs Editor Decision, none closed). `KNOWLEDGE_ATLAS_GOVERNANCE.md` extended with a Research-Program-Integration trigger and a second, really-measured KPI cycle (0 duplicate IDs, 18 orphans unchanged, 1 connected component, independently recomputed). No framework rewrite, no new object type, no code changes to the Atlas compiler. |
| V11-04 | Early Delivery Vertical Slice | COMPLETED — AUDITED (PASS WITH CONDITIONS, CONDITIONS CLOSED) | V11-03 (completed and audited, condition closed); validation rules available | Completion report: `00_project/projects/V11-04_early_delivery_vertical_slice/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-04_early_delivery_vertical_slice/AUDIT_REPORT.md` (0 Critical, 0 Major, 4 Minor; all four minor closure actions completed 2026-07-07). Cluster MEC-0002 (Verlustaversion/Status-quo-Kosten); publication fragment, workbook exercise, training sequence in `05_publications/`; gaps classified; delivery-scaling recommendation: limited, no broad scaling. Two non-blocking open items carried forward to program level: T12/status-"Validiert" deferred governance clarification, and MEC-0002/P-0002 evidence-level harmonization (registered in `SCIENTIFIC_DEBT.md`). V11-05 Readiness: B — MAY START AFTER MINOR CLOSURE ACTIONS, conditions met. |
| V11-05 | Knowledge Consolidation & Integrated Synthesis | COMPLETED — AUDITED — PASS WITH CONDITIONS — CONDITION CLOSED | V11-04 (completed and audited, conditions closed) | Completion report: `00_project/projects/V11-05_knowledge_consolidation/COMPLETION_REPORT.md`. Main artifact: `00_project/projects/V11-05_knowledge_consolidation/INTEGRATED_CONSOLIDATION_SYNTHESIS.md`. Original audit (historical): `AUDIT_REPORT.md` (REWORK REQUIRED, 0 Critical/1 Major/3 Minor). Rework report: `REWORK_REPORT.md` (REWORK COMPLETED). Focused re-audit: `RE_AUDIT_REPORT.md` (PASS WITH CONDITIONS, 0 Critical/0 Major/1 Minor). Closure report: `00_project/CLOSURE_REPORT_V11-05_2026-07-07.md`. Precisified two Atlas Sprint 1 findings via direct object verification (MEC-0018 dependency chain affects only 2 of 4 suspected objects, both already visibly documented since 2026-07-03). **Corrected in rework:** W-001 (Teach First vs. Diagnose First) is NOT an orphaned/unresolved question — it is a completed research project (Editor Decision "Teilweise annehmen", 2026-07-03); only a narrower residual empirical question (OQ-2) remains open. A tension originally misassigned as "W-006" (Pre-Suasion vs. FOMU) was renamed to W-007, since W-006 was already reserved since 2026-07-01 for "Kognitive Leichtigkeit vs. Rational Drowning". P-0040's stale "0 MEC connections / fully isolated" claim was corrected (W-003 extension with MEC-0030 back-reference exists since 2026-07-05). **Closed in focused re-audit (Condition C-01):** OQ-2 was mislabeled as "problem-maturity moderator" in several files; canonical OQ-2 identity is the Omission-Kipppunkt in the Buying Center (complexity/product-information tipping point between loss avoidance and decision paralysis) per `06_research_program/completed/W001/OPEN_QUESTIONS.md`; problem maturity remains a context factor of the W-001 core finding but is not OQ-2 itself. No knowledge object changed, no new research project, T12 remains inactive, audit verdict not reclassified. |
| V11-06 | Research Portfolio Wave 2 | EXECUTOR WORK COMPLETED — AWAITING INDEPENDENT AUDIT | V11-02; V11-05 (audited, PASS WITH CONDITIONS, condition closed) | Completion report: `00_project/projects/V11-06_research_portfolio_wave_2/COMPLETION_REPORT.md`. Editor authorized (2026-07-07) a wave scope limited to exactly one new W-project: W-008 (OQ-2 from `06_research_program/completed/W001/`, "Omission-Kipppunkt im Buying Center"); RP-005/RP-006 explicitly excluded. W-008 completed all nine Research Lifecycle stages — Editor Decision (Felix, 2026-07-12, "Teilweise annehmen"), Repository Integration (4 objects extended: MEC-0016, MEC-0014, A-0031; no new object), passed Health Check, folder moved to `06_research_program/completed/W008/`. OQ-2 itself remains empirically unresolved (no direct empirical test found in available literature; transferred to `SCIENTIFIC_DEBT.md`, requires a dedicated primary experiment, not further literature synthesis). Cross-wave synthesis identifies a programmwide pattern of additive synthesis recommendations now confirmed in its fourth occurrence (W-002/W-003/W-004/W-008) — flagged for a possible future programmwide methods review, Editor authorization pending. DoD 1–6 fulfilled; DoD 7 partially fulfilled — completion report exists, independent audit (preferably cross-family per `V1_1_AUTONOMY_AND_AUDIT_POLICY.md` §5.2/5.3) still outstanding. No Open Decision resolved, no portfolio architecture decision made, no Git commit. |
| V11-07 | Cross-System Review & Delivery Scaling Decision | LATER | V11-04; V11-05; V11-06 if executed | Decision whether to scale research, delivery or automation |
| V11-08 | Final Program Audit & Version 1.1 Release Decision | LATER | V11-01–V11-07 dispositions | Final audit and release decision |

---

## 5. Sequence Rationale

### V11-01 first

The program needs a clean baseline, synchronized control documents, and a current repository/Atlas state before new work starts.

### V11-02 before major governance buildout

The Compact Evidence Architecture Check is already the immediate pending strategic input. Its results should determine which evidence gaps require governance limits, Scientific Debt, Recovery work or full W-projects.

### V11-03 before delivery scaling

Governance, repository integrity and Atlas operationalization define what can safely be used in delivery outputs.

### V11-04 earlier than originally planned

The Vertical Slice tests whether the knowledge base can become useful chapters, workbook elements and training material before another large research wave expands the corpus.

### V11-06 after consolidation and delivery probe

Research Wave 2 should be guided by validated gaps rather than momentum.

---

## 6. Program-Level Stop Conditions

Stop the program and request Editor input if:

- baseline cannot be established,
- Evidence Resolution creates a release-blocking contradiction,
- Atlas or repository integrity checks fail in a way that changes the validity of recent integrations,
- Delivery Vertical Slice reveals a structural failure in the knowledge model,
- a macro-project needs irreversible high-impact change.

---

## 7. Current Active Project

**COMPLETED AND AUDITED (five):** V11-01 (PASS WITH CONDITIONS, condition fulfilled); V11-02 (PASS); V11-03 (PASS WITH CONDITIONS, condition closed); V11-04 — Early Delivery Vertical Slice (PASS WITH CONDITIONS, 0 Critical/0 Major/4 Minor, all minor closure actions completed 2026-07-07, conditions closed); V11-05 — Knowledge Consolidation & Integrated Synthesis (original audit REWORK REQUIRED → targeted rework completed → focused re-audit PASS WITH CONDITIONS, 0 Critical/0 Major/1 Minor → Condition C-01 closed 2026-07-07, see Program Board above, `REWORK_REPORT.md`, `RE_AUDIT_REPORT.md`, `CLOSURE_REPORT_V11-05_2026-07-07.md`). Cross-Project Consistency (bundled audit V11-02/V11-03): CONSISTENT WITH MINOR DRIFT.

**EXECUTOR WORK COMPLETED, AWAITING INDEPENDENT AUDIT (one):** V11-06 — Research Portfolio Wave 2 (wave scope limited to W-008 by explicit Editor authorization 2026-07-07; W-008 fully closed through all nine Research Lifecycle stages, Editor Decision "Teilweise annehmen" 2026-07-12; see Program Board above and `00_project/projects/V11-06_research_portfolio_wave_2/COMPLETION_REPORT.md`).

Execution briefs:

`00_project/projects/V11-01_baseline_control_plane/PROJECT_BRIEF.md`
`00_project/projects/V11-02_evidence_architecture_resolution/PROJECT_BRIEF.md`
`00_project/projects/V11-03_governance_integrity_atlas/PROJECT_BRIEF.md`
`00_project/projects/V11-04_early_delivery_vertical_slice/PROJECT_BRIEF.md`
`00_project/projects/V11-05_knowledge_consolidation/PROJECT_BRIEF.md`
`00_project/projects/V11-06_research_portfolio_wave_2/PROJECT_BRIEF.md`

Completion reports:

`00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`
`00_project/projects/V11-02_evidence_architecture_resolution/COMPLETION_REPORT.md`
`00_project/projects/V11-03_governance_integrity_atlas/COMPLETION_REPORT.md`
`00_project/projects/V11-04_early_delivery_vertical_slice/COMPLETION_REPORT.md`
`00_project/projects/V11-05_knowledge_consolidation/COMPLETION_REPORT.md`
`00_project/projects/V11-06_research_portfolio_wave_2/COMPLETION_REPORT.md` (not yet audited)

Audit reports:

`00_project/projects/V11-02_evidence_architecture_resolution/AUDIT_REPORT.md`
`00_project/projects/V11-03_governance_integrity_atlas/AUDIT_REPORT.md`
`00_project/projects/V11-04_early_delivery_vertical_slice/AUDIT_REPORT.md`
`00_project/projects/V11-05_knowledge_consolidation/AUDIT_REPORT.md` (original, historical: REWORK REQUIRED, 0 Critical/1 Major/3 Minor)
`00_project/projects/V11-05_knowledge_consolidation/RE_AUDIT_REPORT.md` (focused re-audit: PASS WITH CONDITIONS, 0 Critical/0 Major/1 Minor — Condition C-01 CLOSED)

V11-06 audit report: none yet — outstanding, preferably cross-family per `V1_1_AUTONOMY_AND_AUDIT_POLICY.md` §5.2/5.3.

Rework report: `00_project/projects/V11-05_knowledge_consolidation/REWORK_REPORT.md`

Closure reports: `00_project/CLOSURE_REPORT_V11-02_V11-03_2026-07-06.md`, `00_project/CLOSURE_REPORT_V11-04_2026-07-07.md`, `00_project/CLOSURE_REPORT_V11-05_2026-07-07.md`

Next step: obtain an independent audit of **V11-06 — Research Portfolio Wave 2** (executor work completed 2026-07-12, not yet audited). Only after that audit (and closure of any resulting conditions) should **V11-07 — Cross-System Review & Delivery Scaling Decision** be considered, and only with explicit Editor authorization — not started automatically. Non-blocking open items carried forward at program level: T12/status-"Validiert" governance question (deferred); MEC-0002/P-0002 evidence-level harmonization (registered in `SCIENTIFIC_DEBT.md`); W-001/W-008 empirical question OQ-2 — canonical identity: Omission-Kipppunkt im Buying Center, complexity/product-information tipping point between loss avoidance and decision paralysis, NOT problem maturity — remains unresolved after two research projects (W-001, W-008); only a dedicated primary experiment can close it, no further literature synthesis planned (see `SCIENTIFIC_DEBT.md`); W-006 candidate "Kognitive Leichtigkeit vs. Rational Drowning" (unchanged, out of scope for V11-05 and V11-06); W-007 (Pre-Suasion vs. FOMU tension, corrected from a misassigned W-006, formally documented in `contradiction_matrix.md`); RP-005/RP-006 (unchanged, explicitly excluded from V11-06); programmwide additive-synthesis pattern, now confirmed in its fourth occurrence across W-002/W-003/W-004/W-008 (possible future methods review, Editor authorization pending).

Operational launcher:

`00_project/NEXT_ACTION.md`
