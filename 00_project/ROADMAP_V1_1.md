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
| V11-01 | Baseline & Control Plane Consolidation | COMPLETED — AUDIT PENDING | Editor authorization | Clean baseline, synced status, operational V1.1 control plane. Completion report: `00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`. One documented non-content Hard Block (Git index.lock cannot be cleared on this filesystem — see report Section 5); repository state otherwise consistent and fully documented. |
| V11-02 | Evidence Architecture Resolution | READY | V11-01 (completed, audit pending); Evidence report availability (satisfied — `00_project/EVIDENCE_ARCHITECTURE_CHECK_2026-07-06.md`) | Evidence decisions, Scientific Debt updates, research priority decision |
| V11-03 | Governance + Repository Integrity + Atlas Operationalization | READY | V11-01; V11-02 preferred | Implemented governance/integrity rules, Atlas freshness procedure |
| V11-04 | Early Delivery Vertical Slice | LATER | V11-03; validation rules available | Chapter/workbook/training prototype and delivery-chain audit |
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

**COMPLETED — AUDIT PENDING:** V11-01 — Baseline & Control Plane Consolidation (2026-07-06)

Execution brief:

`00_project/projects/V11-01_baseline_control_plane/PROJECT_BRIEF.md`

Completion report:

`00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`

Next step: independent audit of V11-01 (see Autonomy & Audit Policy, Section 5.2), then V11-02 — Evidence Architecture Resolution.

Operational launcher:

`00_project/NEXT_ACTION.md`
