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
| V11-04 | Early Delivery Vertical Slice | READY — NEXT LAUNCHER (not started) | V11-03 (completed and audited, condition closed); validation rules available | Chapter/workbook/training prototype and delivery-chain audit |
| V11-05 | Knowledge Consolidation & Integrated Synthesis | LATER | V11-04 | Consolidated synthesis priorities and missing-bridge findings |
| V11-06 | Research Portfolio Wave 2 | LATER | V11-02; V11-05 | Controlled research wave with context resets and falsification protocol |
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

**COMPLETED AND AUDITED (all three):** V11-01 — Baseline & Control Plane Consolidation (PASS WITH CONDITIONS, condition fulfilled via commit/push); V11-02 — Evidence Architecture Resolution (PASS); V11-03 — Governance + Repository Integrity + Atlas Operationalization (PASS WITH CONDITIONS, condition — status-consistency cleanup — fulfilled 2026-07-06, condition closed). Cross-Project Consistency (bundled audit V11-02/V11-03): CONSISTENT WITH MINOR DRIFT.

Execution briefs:

`00_project/projects/V11-01_baseline_control_plane/PROJECT_BRIEF.md`
`00_project/projects/V11-02_evidence_architecture_resolution/PROJECT_BRIEF.md`
`00_project/projects/V11-03_governance_integrity_atlas/PROJECT_BRIEF.md`

Completion reports:

`00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`
`00_project/projects/V11-02_evidence_architecture_resolution/COMPLETION_REPORT.md`
`00_project/projects/V11-03_governance_integrity_atlas/COMPLETION_REPORT.md`

Audit reports:

`00_project/projects/V11-02_evidence_architecture_resolution/AUDIT_REPORT.md`
`00_project/projects/V11-03_governance_integrity_atlas/AUDIT_REPORT.md`

Closure report: `00_project/CLOSURE_REPORT_V11-02_V11-03_2026-07-06.md`

Next step: **V11-04 — Early Delivery Vertical Slice** is the next launcher — ready, not yet started in any session. All three completed macro-projects now have independent audits on record; no outstanding audit blocks V11-04.

Operational launcher:

`00_project/NEXT_ACTION.md`
