# Sales Codex V1.1 — Autonomy & Audit Policy

Status: Active for V1.1  
Date: 2026-07-06

---

## 1. Purpose

This policy defines how autonomous agents execute large Sales Codex V1.1 macro-projects without turning Felix into a micro-manager.

The operating principle is:

> Large autonomous work packages, internal execution checkpoints, exception-based escalation, independent audit.

---

## 2. Autonomy model

### 2.1 The agent may do autonomously

Within an active macro-project brief, the executor may autonomously:

- read all files necessary for the scoped mission,
- create internal plans,
- run repository inspections,
- run existing scripts and health checks,
- perform scoped Markdown edits,
- create project reports,
- update status/control documents named in the brief,
- propose next actions,
- document uncertainty and continue.

### 2.2 The agent must not do autonomously

The executor must not autonomously:

- override explicit Editor Decisions,
- modify Version-1.0 frozen knowledge objects outside the active brief,
- create new fundamental methodology without a Reserved Decision,
- delete canonical content at scale,
- perform large ID migrations,
- close Open Decisions without explicit authorization,
- invent sources or upgrade evidence status without documented basis.

---

## 3. Internal checkpoints

Internal checkpoints are mandatory but silent. They do not require a chat update unless they trigger an escalation condition.

### 3.1 Scope Check

Ask:

- Am I still executing the active project brief?
- Has scope creep appeared?
- Is the current task still necessary for the Definition of Done?

### 3.2 State Check

Ask:

- Does my working assumption match the current repository state?
- Did my changes create new dependencies?
- Are active, ready, blocked and done states still consistent?

### 3.3 Evidence Check

Ask:

- Are claims supported by sources or explicitly marked as uncertain?
- Have counter-evidence and rival explanations been considered?
- Is any synthesis stronger than its evidence base permits?

### 3.4 Falsification Check

For research or theory work, each major hypothesis must include:

- a counter-hypothesis,
- disconfirming evidence search,
- conditions under which the hypothesis would be weakened or rejected.

### 3.5 Health Check

Ask:

- Do all referenced files exist?
- Are IDs, file paths and status values consistent?
- If Atlas-relevant, does the Atlas compiler still run?
- Are generated reports reproducible from repository state?

### 3.6 Context Reset / Compaction

At semantic phase boundaries, the executor should compact context into a repository-based handoff and reload only relevant files for the next phase.

This is an execution-level control, not a human approval gate.

### 3.7 Pre-Completion Check

Before completion, verify every Definition-of-Done item in the project brief and state the verification evidence in the completion report.

---

## 4. Escalation rules

The executor stops and asks for human decision only under the following conditions.

### 4.1 Hard Block

Examples:

- required file missing or corrupt,
- required source inaccessible,
- script failure blocks the mission and cannot be conservatively bypassed,
- two binding repository rules conflict,
- actual repository state makes the project brief impossible.

### 4.2 Reserved Decision

Examples:

- acceptance/rejection of a fundamental model,
- major methodology change,
- ethical boundary decision,
- Editor Decision in Research Lifecycle,
- final release decision,
- closing or materially changing an Open Decision.

### 4.3 Irreversible High-Impact Change

Examples:

- bulk deletion,
- large ID migration,
- restructuring canonical knowledge categories,
- changing core knowledge model or repository layout with major downstream effects.

### 4.4 Audit Trigger

If the executor detects a possible quality failure pattern that does not block completion but may affect trust, it documents the issue and flags it for the audit rather than interrupting Felix.

---

## 5. Audit architecture

### 5.1 Executor self-checks

Self-checks are mandatory but not sufficient for project acceptance.

### 5.2 Independent project audit

Each completed macro-project requires an audit report.

Preferred pattern:

- Claude/Cowork/Clerk executes,
- Gemini or ChatGPT audits in a separate context,
- auditor reads repository artifacts directly,
- auditor receives the original project brief and final artifacts,
- auditor is not limited to the executor's completion narrative.

### 5.3 Cross-family invariant

For material V1.1 gates, generator and auditor should be from different model families wherever practically possible.

### 5.4 Metadata and framing caution

Auditors should treat completion reports as claims to verify, not as evidence. They must inspect raw changed files and status artifacts.

---

## 6. Anti-micromanagement rule

The following are not valid reasons to interrupt Felix:

- ordinary uncertainty,
- choosing which relevant file to read next,
- deciding internal task order,
- running existing checks,
- making reversible scoped edits,
- documenting caveats,
- selecting conservative terminology.

Document and continue.
