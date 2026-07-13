# Sales Codex — Roadmap V1.1

Status: **RELEASED — SCOPE-LIMITED** (Editor Release Decision, Felix, 2026-07-13 — siehe `00_project/projects/V11-08_final_audit_release/EDITOR_RELEASE_DECISION.md`)  
Opened: 2026-07-06  
Strategic Source of Truth for Version 1.1

**Release-Hinweis:** Freigegeben als evidenz-, governance- und auditkonsolidierter Repository-Stand. Breite Delivery-Skalierung ist NICHT Teil dieser Freigabe (weiterhin „begrenzt", siehe V11-04). OD-009 bis OD-012, Delivery-Scaling-Blocker, das additive Synthesemuster (R-1), OQ-2/Scientific Debt und mögliche V11-09 ff. bleiben durch dieses Release unentschieden. Working Tree ist zum Zeitpunkt des Release nicht clean; Commit/Push bleibt ausschließlich Felix' Aufgabe.

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
| V11-01 | Baseline & Control Plane Consolidation | COMPLETED — AUDITED (PASS WITH CONDITIONS, CONDITION FULFILLED) | Editor authorization | Clean baseline, synced status, operational V1.1 control plane. Completion report: `00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-01_baseline_control_plane/AUDIT_REPORT.md` (retroactive Audit Availability Report persisted 2026-07-13; original independent audit before V11-02 documented PASS WITH CONDITIONS, condition fulfilled by commit/push). Git index.lock Hard Block resolved. |
| V11-02 | Evidence Architecture Resolution | COMPLETED — AUDITED (PASS) | V11-01 (completed and audited); Evidence report availability (satisfied — `00_project/EVIDENCE_ARCHITECTURE_CHECK_2026-07-06.md`) | Completion report: `00_project/projects/V11-02_evidence_architecture_resolution/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-02_evidence_architecture_resolution/AUDIT_REPORT.md` (PASS, no blocking findings). All 7 findings disposed (6× partially accept/precisify, 1× no change); `SCIENTIFIC_DEBT.md` updated; no W-005 activated; 3-item Evidence Backlog created (highest-priority item — implementing precisifications into MEC/MOD objects and `LITERATURE_INDEX.md` — deferred pending Editor sign-off, outside V11-02 file scope). |
| V11-03 | Governance + Repository Integrity + Atlas Operationalization | COMPLETED — AUDITED (PASS WITH CONDITIONS, CONDITION CLOSED) | V11-01 (completed and audited); V11-02 (completed and audited) | Completion report: `00_project/projects/V11-03_governance_integrity_atlas/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-03_governance_integrity_atlas/AUDIT_REPORT.md` (PASS WITH CONDITIONS; condition — CURRENT_STATE.md status-consistency cleanup + closure documentation — fulfilled 2026-07-06, condition closed). OD-006/OD-007/OD-009–012 given explicit DoD status (2× Deferred, 4× Needs Editor Decision, none closed). `KNOWLEDGE_ATLAS_GOVERNANCE.md` extended with a Research-Program-Integration trigger and a second, really-measured KPI cycle (0 duplicate IDs, 18 orphans unchanged, 1 connected component, independently recomputed). No framework rewrite, no new object type, no code changes to the Atlas compiler. |
| V11-04 | Early Delivery Vertical Slice | COMPLETED — AUDITED (PASS WITH CONDITIONS, CONDITIONS CLOSED) | V11-03 (completed and audited, condition closed); validation rules available | Completion report: `00_project/projects/V11-04_early_delivery_vertical_slice/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-04_early_delivery_vertical_slice/AUDIT_REPORT.md` (0 Critical, 0 Major, 4 Minor; all four minor closure actions completed 2026-07-07). Cluster MEC-0002 (Verlustaversion/Status-quo-Kosten); publication fragment, workbook exercise, training sequence in `05_publications/`; gaps classified; delivery-scaling recommendation: limited, no broad scaling. Two non-blocking open items carried forward to program level: T12/status-"Validiert" deferred governance clarification, and MEC-0002/P-0002 evidence-level harmonization (registered in `SCIENTIFIC_DEBT.md`). V11-05 Readiness: B — MAY START AFTER MINOR CLOSURE ACTIONS, conditions met. |
| V11-05 | Knowledge Consolidation & Integrated Synthesis | COMPLETED — AUDITED — PASS WITH CONDITIONS — CONDITION CLOSED | V11-04 (completed and audited, conditions closed) | Completion report: `00_project/projects/V11-05_knowledge_consolidation/COMPLETION_REPORT.md`. Main artifact: `00_project/projects/V11-05_knowledge_consolidation/INTEGRATED_CONSOLIDATION_SYNTHESIS.md`. Original audit (historical): `AUDIT_REPORT.md` (REWORK REQUIRED, 0 Critical/1 Major/3 Minor). Rework report: `REWORK_REPORT.md` (REWORK COMPLETED). Focused re-audit: `RE_AUDIT_REPORT.md` (PASS WITH CONDITIONS, 0 Critical/0 Major/1 Minor). Closure report: `00_project/CLOSURE_REPORT_V11-05_2026-07-07.md`. Precisified two Atlas Sprint 1 findings via direct object verification (MEC-0018 dependency chain affects only 2 of 4 suspected objects, both already visibly documented since 2026-07-03). **Corrected in rework:** W-001 (Teach First vs. Diagnose First) is NOT an orphaned/unresolved question — it is a completed research project (Editor Decision "Teilweise annehmen", 2026-07-03); only a narrower residual empirical question (OQ-2) remains open. A tension originally misassigned as "W-006" (Pre-Suasion vs. FOMU) was renamed to W-007, since W-006 was already reserved since 2026-07-01 for "Kognitive Leichtigkeit vs. Rational Drowning". P-0040's stale "0 MEC connections / fully isolated" claim was corrected (W-003 extension with MEC-0030 back-reference exists since 2026-07-05). **Closed in focused re-audit (Condition C-01):** OQ-2 was mislabeled as "problem-maturity moderator" in several files; canonical OQ-2 identity is the Omission-Kipppunkt in the Buying Center (complexity/product-information tipping point between loss avoidance and decision paralysis) per `06_research_program/completed/W001/OPEN_QUESTIONS.md`; problem maturity remains a context factor of the W-001 core finding but is not OQ-2 itself. No knowledge object changed, no new research project, T12 remains inactive, audit verdict not reclassified. |
| V11-06 | Research Portfolio Wave 2 | COMPLETED — AUDITED — PASS WITH CONDITIONS — CONDITIONS CLOSED | V11-02; V11-05 (audited, PASS WITH CONDITIONS, condition closed) | Completion report: `00_project/projects/V11-06_research_portfolio_wave_2/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-06_research_portfolio_wave_2/AUDIT_REPORT.md` (0 Critical/0 Major/3 Minor, all closed 2026-07-12). Closure report: `00_project/CLOSURE_REPORT_V11-06_2026-07-12.md`. Editor authorized (2026-07-07) a wave scope limited to exactly one new W-project: W-008 (OQ-2 from `06_research_program/completed/W001/`, "Omission-Kipppunkt im Buying Center"); RP-005/RP-006 explicitly excluded. W-008 completed all nine Research Lifecycle stages — Editor Decision (Felix, 2026-07-12, "Teilweise annehmen"), Repository Integration (4 objects extended: MEC-0016, MEC-0014, A-0031; no new object), passed Health Check, folder moved to `06_research_program/completed/W008/`. OQ-2 itself remains empirically unresolved (no direct empirical test found in available literature; transferred to `SCIENTIFIC_DEBT.md`, requires a dedicated primary experiment, not further literature synthesis). Cross-wave synthesis identifies a programmwide pattern of additive synthesis recommendations now confirmed in its fourth occurrence (W-002/W-003/W-004/W-008) — flagged for a possible future programmwide methods review, Editor authorization pending. Audit findings (MEC-0016 unqualified claim, W-008 README role gap, overstated "statistische Aussagekraft" wording) closed same day. No Open Decision resolved, no portfolio architecture decision made, no Git commit. |
| V11-07 | Cross-System Review & Delivery Scaling Decision | COMPLETED — AUDITED — PASS WITH CONDITIONS — CONDITIONS CLOSED | V11-04; V11-05; V11-06 (completed and audited, conditions closed) | Review artifact: `00_project/projects/V11-07_cross_system_review/CROSS_SYSTEM_REVIEW.md`. Completion report: `00_project/projects/V11-07_cross_system_review/COMPLETION_REPORT.md`. Audit report: `00_project/projects/V11-07_cross_system_review/AUDIT_REPORT.md` (Codex, 0 Critical/0 Major/3 Minor, all closed 2026-07-13). Closure report: `00_project/CLOSURE_REPORT_V11-07_2026-07-13.md`. Direct read of all V11-01–V11-06 completion/audit/rework/re-audit/closure reports (not roadmap summaries). Eight risks ranked (R-1–R-8); highest-weight: programmwide additive-synthesis pattern (4th confirmed occurrence) and four unaddressed V11-04 delivery-scaling blockers, unchanged since 2026-07-07. Corrected recommendation was confirmed by audit: V11-08 could not start until all project audits were available. V11-07 is audited and the former V11-01 audit-availability gap is now closed by `00_project/projects/V11-01_baseline_control_plane/AUDIT_REPORT.md`; V11-08 is therefore ready next. No decision made, no knowledge object changed, no Git commit. |
| V11-08 | Final Program Audit & Version 1.1 Release Decision | **COMPLETED — AUDITED (PASS) — EDITOR RELEASE DECISION: RELEASED — SCOPE-LIMITED (2026-07-13)** | V11-01–V11-07 dispositions; **"All project audits available" satisfied 2026-07-13** | Release-criteria verification: `00_project/projects/V11-08_final_audit_release/RELEASE_CRITERIA_VERIFICATION.md` (all 7 sections of `V1_1_RELEASE_CRITERIA.md`, pass/fail/deferred with rationale; only real fail is the classified, Felix-owned non-clean working tree). Completion report: `00_project/projects/V11-08_final_audit_release/COMPLETION_REPORT.md`. Decision package: `00_project/projects/V11-08_final_audit_release/RELEASE_DECISION_PACKAGE.md`. Independent Final Audit + Re-Check (Codex, 2026-07-13): PASS, all findings (1 Major, 2 Minor across both rounds) closed. **Editor Release Decision:** `00_project/projects/V11-08_final_audit_release/EDITOR_RELEASE_DECISION.md` — V1.1 RELEASED — SCOPE-LIMITED, Felix, 2026-07-13. Delivery-Scaling explicitly NOT part of this release; OD-009–012, delivery-scaling blockers, additive-synthesis pattern (R-1), OQ-2/Scientific Debt, and possible V11-09 ff. remain unresolved by this release. |

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

**COMPLETED AND AUDITED (seven):** V11-01 (PASS WITH CONDITIONS, condition fulfilled, standalone availability report persisted 2026-07-13); V11-02 (PASS); V11-03 (PASS WITH CONDITIONS, condition closed); V11-04 — Early Delivery Vertical Slice (PASS WITH CONDITIONS, 0 Critical/0 Major/4 Minor, all minor closure actions completed 2026-07-07, conditions closed); V11-05 — Knowledge Consolidation & Integrated Synthesis (original audit REWORK REQUIRED → targeted rework completed → focused re-audit PASS WITH CONDITIONS, 0 Critical/0 Major/1 Minor → Condition C-01 closed 2026-07-07, see Program Board above, `REWORK_REPORT.md`, `RE_AUDIT_REPORT.md`, `CLOSURE_REPORT_V11-05_2026-07-07.md`); V11-06 — Research Portfolio Wave 2 (wave scope limited to W-008 by explicit Editor authorization 2026-07-07; W-008 fully closed through all nine Research Lifecycle stages, Editor Decision "Teilweise annehmen" 2026-07-12; audited PASS WITH CONDITIONS, 0 Critical/0 Major/3 Minor, all closed 2026-07-12, see `AUDIT_REPORT.md`, `CLOSURE_REPORT_V11-06_2026-07-12.md`); V11-07 — Cross-System Review & Delivery Scaling Decision (audited by Codex, PASS WITH CONDITIONS, 0 Critical/0 Major/3 Minor, all closed 2026-07-13, see `AUDIT_REPORT.md`, `CLOSURE_REPORT_V11-07_2026-07-13.md`). Cross-Project Consistency (bundled audit V11-02/V11-03): CONSISTENT WITH MINOR DRIFT.

Execution briefs:

`00_project/projects/V11-01_baseline_control_plane/PROJECT_BRIEF.md`
`00_project/projects/V11-02_evidence_architecture_resolution/PROJECT_BRIEF.md`
`00_project/projects/V11-03_governance_integrity_atlas/PROJECT_BRIEF.md`
`00_project/projects/V11-04_early_delivery_vertical_slice/PROJECT_BRIEF.md`
`00_project/projects/V11-05_knowledge_consolidation/PROJECT_BRIEF.md`
`00_project/projects/V11-06_research_portfolio_wave_2/PROJECT_BRIEF.md`
`00_project/projects/V11-07_cross_system_review/PROJECT_BRIEF.md`

Completion reports:

`00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`
`00_project/projects/V11-02_evidence_architecture_resolution/COMPLETION_REPORT.md`
`00_project/projects/V11-03_governance_integrity_atlas/COMPLETION_REPORT.md`
`00_project/projects/V11-04_early_delivery_vertical_slice/COMPLETION_REPORT.md`
`00_project/projects/V11-05_knowledge_consolidation/COMPLETION_REPORT.md`
`00_project/projects/V11-06_research_portfolio_wave_2/COMPLETION_REPORT.md`
`00_project/projects/V11-07_cross_system_review/COMPLETION_REPORT.md`

Audit reports:

`00_project/projects/V11-01_baseline_control_plane/AUDIT_REPORT.md` (PASS WITH CONDITIONS — CONDITION FULFILLED; retroactive Audit Availability Report persisted 2026-07-13)
`00_project/projects/V11-02_evidence_architecture_resolution/AUDIT_REPORT.md`
`00_project/projects/V11-03_governance_integrity_atlas/AUDIT_REPORT.md`
`00_project/projects/V11-04_early_delivery_vertical_slice/AUDIT_REPORT.md`
`00_project/projects/V11-05_knowledge_consolidation/AUDIT_REPORT.md` (original, historical: REWORK REQUIRED, 0 Critical/1 Major/3 Minor)
`00_project/projects/V11-05_knowledge_consolidation/RE_AUDIT_REPORT.md` (focused re-audit: PASS WITH CONDITIONS, 0 Critical/0 Major/1 Minor — Condition C-01 CLOSED)
`00_project/projects/V11-06_research_portfolio_wave_2/AUDIT_REPORT.md` (PASS WITH CONDITIONS, 0 Critical/0 Major/3 Minor — all three conditions CLOSED 2026-07-12)
`00_project/projects/V11-07_cross_system_review/AUDIT_REPORT.md` (Codex, PASS WITH CONDITIONS, 0 Critical/0 Major/3 Minor — all three conditions CLOSED 2026-07-13)

Rework report: `00_project/projects/V11-05_knowledge_consolidation/REWORK_REPORT.md`

Closure reports: `00_project/CLOSURE_REPORT_V11-02_V11-03_2026-07-06.md`, `00_project/CLOSURE_REPORT_V11-04_2026-07-07.md`, `00_project/CLOSURE_REPORT_V11-05_2026-07-07.md`, `00_project/CLOSURE_REPORT_V11-06_2026-07-12.md`, `00_project/CLOSURE_REPORT_V11-07_2026-07-13.md`

**Programmstatus: V1.1 RELEASED — SCOPE-LIMITED (Editor Release Decision, Felix, 2026-07-13 — `00_project/projects/V11-08_final_audit_release/EDITOR_RELEASE_DECISION.md`).** ~~Next step: V11-08 is EXECUTOR WORK COMPLETE (DoD 1–3) — AWAITING FINAL AUDIT (DoD 4) AND EDITOR RELEASE DECISION (DoD 5).~~ ~~V11-08 is READY — NEXT LAUNCHER — NOT STARTED... V11-08 execution has not yet begun; it may now start as the next regular macro-project.~~ **[Beide vorherigen Zwischenstände sind durch die Editor Release Decision vom 2026-07-13 überholt und hier append-only ersetzt.]**

V11-08 ist vollständig abgeschlossen: Executor-Arbeit (DoD 1–3), unabhängiger Final Audit + Re-Check durch Codex (PASS, alle Findings geschlossen, DoD 4), und die Editor Release Decision selbst (DoD 5) liegen vor. Die Freigabe umfasst den evidenz-, governance- und auditkonsolidierten Repository-Stand von V1.1 — **nicht** breite Delivery-Skalierung (weiterhin „begrenzt", V11-04-Befund unverändert in Kraft). Working Tree ist zum Release-Zeitpunkt nicht clean; Commit/Push bleibt ausschließlich Felix' Aufgabe und ist keine Voraussetzung für die inhaltliche Gültigkeit dieser Entscheidung.

Durch dieses Release ausdrücklich **nicht** entschieden: OD-009 bis OD-012 (vier Reserved Decisions, klassifiziert, seit 2026-07-02/03 entscheidungsreif); vier V11-04-Delivery-Scaling-Blocker (V11-07 R-2); programmweites additives Synthesemuster (V11-07 R-1, 4. bestätigtes Vorkommen, Methoden-Review-Kandidat); W-001/W-008-Restfrage OQ-2 (unverändert offen, benötigt Primärexperiment); T12/Status-„Validiert"-Governance-Frage; MEC-0002/P-0002-Evidenzlevel-Harmonisierung (`SCIENTIFIC_DEBT.md`); RP-005/RP-006 (unverändert blockiert). **Kein V11-09/V11-10/V11-11 existiert** — jede künftige Ausweitung (Delivery-Skalierung, neue Makroprojekte) erfordert eine eigene, gesonderte Editor-Entscheidung.

Operational launcher:

`00_project/NEXT_ACTION.md`
