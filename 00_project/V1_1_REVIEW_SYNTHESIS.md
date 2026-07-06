# Sales Codex V1.1 — Review Synthesis & Editor Implementation Decision

Status: Accepted for implementation  
Date: 2026-07-06  
Owner: Felix / Editor-in-Chief

---

## 1. Decision

Sales Codex Version 1.1 is opened as an autonomous macro-project program.

The implementation follows a calibrated synthesis of:

1. the autonomous macro-work-package plan,
2. the first Gemini red-team review,
3. the final Deep Research review,
4. the real repository constraints of Sales Codex as a predominantly Markdown-based knowledge, research and publication system.

This decision does **not** authorize uncontrolled self-evolution of the repository. It authorizes large autonomous work packages under explicit scope, internal checkpoints, exception-based escalation, and independent audit.

---

## 2. Adopted principles

### 2.1 Large work packages remain the default

Felix does not manage microtasks. Agents receive mission-level project briefs and work autonomously until:

- Done,
- Hard Block,
- Reserved Decision,
- Irreversible High-Impact Change.

### 2.2 Management granularity and execution granularity are separated

A macro-project may be large on the program level while still using internal phases, context resets, repository reloads, and self-checkpoints on the execution level.

### 2.3 The repository remains the source of truth

No chat, model memory, external review, or generated summary replaces the repository.

### 2.4 Cross-family audit is required for material project reviews

Production and final audit should use different model families wherever possible. The auditor should inspect the repository and artifacts directly, not merely the executor's narrative summary.

### 2.5 Falsification is mandatory in research work

Research work must include active counter-hypothesis generation and disconfirming evidence search. Confirmation-only research is not accepted.

### 2.6 Delivery validation moves earlier

The Delivery Vertical Slice is moved before major new research waves so the project can test whether the knowledge architecture produces usable outputs.

---

## 3. Rejected or deferred recommendations

The following recommendations from external reviews are not implemented globally at this stage:

- Global software-engineering release gates such as 85% branch coverage, 95% new-code coverage, CWE scans, mutation testing, and cyclomatic-complexity thresholds. These are relevant only for actual code components such as the Atlas compiler.
- Assumptions about Composio, API keys, external runtime sandboxes, or specific Clerk infrastructure unless documented in the repository.
- Universal hard limits such as “30 steps maximum” independent of task class.
- Solver-based parameter perturbation for all knowledge work. This is only relevant where mathematical or optimization models are actually generated.
- A physical operating-system watchdog as an immediate requirement. V1.1 begins with lightweight, file-based progress and completion discipline; automation can be introduced later if the need is demonstrated.

---

## 4. V1.1 control model

The program uses five persistent control artifacts:

1. `00_project/ROADMAP_V1_1.md` — strategic source of truth for V1.1.
2. `00_project/NEXT_ACTION.md` — minimal operational launcher for the active macro-project.
3. `00_project/projects/V11-XX_*/PROJECT_BRIEF.md` — mission, scope, gates, DoD for each macro-project.
4. `COMPLETION_REPORT.md` — created by the executor at the end of each macro-project.
5. `AUDIT_REPORT.md` — created by an independent reviewer after project completion.

No separate `PROJECT_QUEUE.md` is created. Queue state lives inside the roadmap.

---

## 5. V1.1 sequence

1. V11-01 — Baseline & Control Plane Consolidation
2. V11-02 — Evidence Architecture Resolution
3. V11-03 — Governance + Repository Integrity + Atlas Operationalization
4. V11-04 — Early Delivery Vertical Slice
5. V11-05 — Knowledge Consolidation & Integrated Synthesis
6. V11-06 — Research Portfolio Wave 2
7. V11-07 — Cross-System Review & Delivery Scaling Decision
8. V11-08 — Final Program Audit & Version 1.1 Release Decision

---

## 6. Immediate authorization

The next executable macro-project is V11-01.

V11-01 may be executed autonomously by Claude/Cowork/Clerk under the project brief and current governance. It may update project-control documents and status documents. It must not change Version-1.0 knowledge objects, completed research objects, source objects, or framework core files unless explicitly required by its project brief and reversible.
