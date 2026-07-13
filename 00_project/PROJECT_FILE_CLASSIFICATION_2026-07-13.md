# 00_project File Classification

Status: review document; no physical moves authorized
Updated: 2026-07-13
Scope: all 94 files that existed below `00_project/` at inventory time; this report is an additional review artifact.

## Purpose

This document classifies the complete `00_project/` inventory for the
repository simplification. It separates active control from current reference
and history. It is a planning artifact only: no file is moved, renamed, or
deleted by this document.

## Classification codes

- **A - Active control:** may affect current routing, decisions, status, or quality. Keep discoverable and load only according to task type.
- **R - Current reference:** still valid and useful, but not a daily launcher. Load only when relevant.
- **H - History:** completed work, audit trail, or superseded process material. Do not load in a normal session.
- **P - Closed project record:** a historical project folder whose evidence should remain intact until link impact is checked.
- **T - Template:** reusable structure, not a current status or decision document.

## Executive result

The current `00_project/` directory contains four different functions in one
flat namespace:

1. a small active control plane,
2. task-specific reference material,
3. 2026 sprint, audit, and decision history,
4. closed V1.1 project records and templates.

The main simplification opportunity is therefore navigational and lifecycle-
based, not deletion of knowledge. The active control plane can be kept to a
small, explicit set of files. The historical reports can later be moved as a
batch after link verification.

## Recommended active control set

These files are the candidates for the normal operational layer:

- `00_project/ACTIVE_INDEX.md`
- `00_project/NEXT_ACTION.md`
- `00_project/DECISION_STACK_2026-07-13.md`
- `00_project/OPEN_DECISIONS.md`
- `00_project/SCIENTIFIC_DEBT.md`
- `00_project/ROADMAP_V1_1.md` while V1.1 remains the governing release record
- `00_project/REPOSITORY_KPIS.md` for reporting and health checks only
- `00_project/backlog.md` for task selection only
- `00_project/review_queue.md` for review work only
- `00_project/task_rules.md` for task routing only

`SESSION_BRIEF.md` and `PROJECT_BOOTSTRAP.md` remain outside this directory as
the session-level entry points.

## File-by-file classification: root files

| File | Class | Function and target action |
|---|---|---|
| `00_project/ACADEMIC_RECOVERY_PLAN.md` | H | Completed recovery planning; retain as research history, later archive candidate. |
| `00_project/ACADEMIC_RECOVERY_REPORT.md` | H | Completed research recovery report; later archive candidate. |
| `00_project/ACADEMIC_RECOVERY_REPORT_PACK_2_4.md` | H | Completed research recovery report pack; later archive candidate. |
| `00_project/ACTIVE_INDEX.md` | A | Current navigation card; keep as active entry point. |
| `00_project/ARCHITECTURE_OVERVIEW_2026-07-13.md` | R | Current architecture reference; keep discoverable until the target architecture is accepted. |
| `00_project/backlog.md` | A | Task-selection surface, currently empty in READY/IN_PROGRESS/REVIEW; keep but load only for task selection. |
| `00_project/BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md` | H | Closed editorial decision report; retain as decision history, later archive candidate. |
| `00_project/changelog.md` | H | Change history; keep for historical queries, not normal startup. |
| `00_project/CLOSURE_REPORT_V1.1_2026-07-13.md` | H | V1.1 closure evidence; later archive candidate after release links are checked. |
| `00_project/CLOSURE_REPORT_V11-02_V11-03_2026-07-06.md` | H | Closed V11 audit closure; later archive candidate. |
| `00_project/CLOSURE_REPORT_V11-04_2026-07-07.md` | H | Closed V11 audit closure; later archive candidate. |
| `00_project/CLOSURE_REPORT_V11-05_2026-07-07.md` | H | Closed V11 audit closure; later archive candidate. |
| `00_project/CLOSURE_REPORT_V11-06_2026-07-12.md` | H | Closed V11 audit closure; later archive candidate. |
| `00_project/CLOSURE_REPORT_V11-07_2026-07-13.md` | H | Closed V11 audit closure; later archive candidate. |
| `00_project/CODEX_AUDIT_2026-07.md` | H | Completed repository audit; later archive candidate. |
| `00_project/CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md` | H | Completed correction report; later archive candidate. |
| `00_project/COWORK_EXECUTION_PROTOCOL.md` | R | Historical/current process reference; compare with `.agents/` before any later archive decision. |
| `00_project/COWORK_PERFORMANCE_AUDIT_2026-07-05.md` | H | Completed agent-performance audit; later archive candidate. |
| `00_project/COWORK_TOKEN_OPTIMIZATION_SPRINT_1_REPORT.md` | H | Completed optimization sprint report; later archive candidate. |
| `00_project/DECISION_ARCHITECTURE_SPRINT_2_REPORT.md` | H | Completed decision-architecture sprint report; later archive candidate. |
| `00_project/DECISION_BRIEF_OD-009_TO_OD-012_2026-07-13.md` | R | Decision input for the current governance block; retain as current decision evidence. |
| `00_project/DECISION_STACK_2026-07-13.md` | A | Current editor decision context; keep active and discoverable. |
| `00_project/EDITOR_DECISION_OD-009_TO_OD-012_2026-07-13.md` | R | Current decision record for OD-009 through OD-012; retain as governance evidence. |
| `00_project/EDITORIAL_REVIEW_SPRINT_MEC0018_REPORT.md` | H | Completed editorial sprint report; later archive candidate. |
| `00_project/EVIDENCE_ARCHITECTURE_CHECK_2026-07-06.md` | H | Completed evidence architecture check; later archive candidate. |
| `00_project/GOVERNANCE_INTEGRATION_OD-009_TO_OD-012_COMPLETION_REPORT_2026-07-13.md` | R | Recent integration evidence; retain until the governance block is fully superseded. |
| `00_project/HISTORY_INDEX.md` | A | Current historical navigation card; keep active. |
| `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md` | H | Completed Atlas analysis sprint; later archive candidate. |
| `00_project/KNOWLEDGE_ATLAS_GOVERNANCE.md` | R | Current Atlas governance reference; keep discoverable for Atlas work. |
| `00_project/NEXT_ACTION.md` | A | Operational launcher; keep active even when it states that no macro-project is open. |
| `00_project/OPEN_DECISION_RESOLUTION_REPORT_2026-07.md` | H | Completed decision-resolution sprint report; later archive candidate. |
| `00_project/OPEN_DECISIONS.md` | A | Current decision register, including resolved decisions and remaining governance context; keep active. |
| `00_project/POST_MORTEM_B0002.md` | H | Completed B-0002 post-mortem; later archive candidate. |
| `00_project/POST_MORTEM_INFLUENCE_PLAN.md` | H | Completed post-mortem planning artifact; later archive candidate. |
| `00_project/PROCESS_PATTERN_ANALYSIS_2026-07.md` | H | Completed process-pattern analysis; later archive candidate. |
| `00_project/PROJECT_FILE_CLASSIFICATION_2026-07-13.md` | R | Current classification and simplification review; keep until the target structure is decided. |
| `00_project/RELEASE_NOTES_v1.1.md` | H | V1.1 release record; retain as release history, later archive candidate. |
| `00_project/REPOSITORY_KPIS.md` | A | Current metrics/reporting surface; load only for health checks or release reporting. |
| `00_project/RESEARCH_PORTFOLIO_CHECKPOINT_1.md` | H | Historical research portfolio checkpoint; later archive candidate. |
| `00_project/RESEARCH_PORTFOLIO_INITIALIZATION_REPORT.md` | H | Historical research portfolio initialization; later archive candidate. |
| `00_project/review_queue.md` | A | Review routing and unresolved review items; keep active for review tasks only. |
| `00_project/ROADMAP_V1_1.md` | A | Strategic V1.1 program record; keep while V1.1 remains the governing release context. |
| `00_project/SALES_CODEX_AUDIT_STANDARD_V2_1.md` | R | Audit method reference; keep for audit work, not daily startup. |
| `00_project/SALES_CODEX_CONTEXT.md` | R | Short project context reference; compare with `PROJECT_BOOTSTRAP.md` before consolidating. |
| `00_project/SALES_CODEX_DECISION_ARCHITECTURE_AUDIT_2026-07-05.md` | H | Completed decision architecture audit; later archive candidate. |
| `00_project/SALES_CODEX_OPERATING_MANUAL.md` | R | Operating reference for Codex work; keep task-loadable. |
| `00_project/SCIENTIFIC_DEBT.md` | A | Current evidence and quality debt register; keep active. |
| `00_project/SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md` | R | Research/validation strategy reference; keep for scientific-review tasks. |
| `00_project/SESSION_LOG.md` | H | Append-only session history; keep out of normal startup. |
| `00_project/SPRINT_2_ABSCHLUSSBERICHT.md` | H | Completed research sprint report; later archive candidate. |
| `00_project/task_rules.md` | A | Task-specific rules and task-generation behavior; load only for task routing or task creation. |
| `00_project/V1_1_AUTONOMY_AND_AUDIT_POLICY.md` | R | V1.1 operating policy; keep for V1.1 governance and audit work. |
| `00_project/V1_1_RELEASE_CRITERIA.md` | R | V1.1 release criteria; retain as release reference, not daily startup. |
| `00_project/V1_1_REVIEW_SYNTHESIS.md` | H | Completed V1.1 review synthesis; later archive candidate. |
| `00_project/V11_01_CLAUDE_EXECUTION_PROMPT.md` | H | Superseded V11-01 execution prompt; later archive candidate. Content was checked from the committed Git version because the working-tree file is locally read-protected. |
| `00_project/VALIDIERUNGSSPRINT_MEC0010-0012.md` | H | Completed validation sprint report; later archive candidate. |
| `00_project/WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` | H | Historical scientific maturity report; later archive candidate. |
| `00_project/WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md` | H | Historical peer-review report; later archive candidate. Content was checked from the committed Git version because the working-tree file is locally read-protected. |

## File-by-file classification: peer review decisions

| File | Class | Function and target action |
|---|---|---|
| `00_project/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_001.md` | H | Completed peer-review decision record; retain as history, later archive candidate. |
| `00_project/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md` | H | Completed peer-review decision record; retain as history, later archive candidate. |
| `00_project/peer_review/decisions/RELEASE_REPORT_SPRINT_001_PEER_REVIEW.md` | H | Completed peer-review release report; later archive candidate. |
| `00_project/peer_review/decisions/SCRP-0001_Sales_Core.md` | H | Completed Sales Core review package; later archive candidate after link checks. |

## File-by-file classification: templates

| File | Class | Function and target action |
|---|---|---|
| `00_project/templates/AUDIT_REPORT_TEMPLATE.md` | T | Reusable audit template; keep active as a template. |
| `00_project/templates/COMPLETION_REPORT_TEMPLATE.md` | T | Reusable completion template; keep active as a template. |
| `00_project/templates/PROJECT_BRIEF_TEMPLATE.md` | T | Reusable project brief template; keep active as a template. |

## File-by-file classification: closed V1.1 project records

All files in the following folders are **P**. They are complete project
evidence, not active control. Keep each folder internally intact for now. A
later move to a dedicated archive location is acceptable only after link and
authority checks.

### V11-01

- `00_project/projects/V11-01_baseline_control_plane/AUDIT_REPORT.md`
- `00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`
- `00_project/projects/V11-01_baseline_control_plane/PROJECT_BRIEF.md`

### V11-02

- `00_project/projects/V11-02_evidence_architecture_resolution/AUDIT_REPORT.md`
- `00_project/projects/V11-02_evidence_architecture_resolution/COMPLETION_REPORT.md`
- `00_project/projects/V11-02_evidence_architecture_resolution/PROJECT_BRIEF.md`

### V11-03

- `00_project/projects/V11-03_governance_integrity_atlas/AUDIT_REPORT.md`
- `00_project/projects/V11-03_governance_integrity_atlas/COMPLETION_REPORT.md`
- `00_project/projects/V11-03_governance_integrity_atlas/PROJECT_BRIEF.md`

### V11-04

- `00_project/projects/V11-04_early_delivery_vertical_slice/AUDIT_REPORT.md`
- `00_project/projects/V11-04_early_delivery_vertical_slice/COMPLETION_REPORT.md`
- `00_project/projects/V11-04_early_delivery_vertical_slice/PROJECT_BRIEF.md`

### V11-05

- `00_project/projects/V11-05_knowledge_consolidation/AUDIT_REPORT.md`
- `00_project/projects/V11-05_knowledge_consolidation/COMPLETION_REPORT.md`
- `00_project/projects/V11-05_knowledge_consolidation/INTEGRATED_CONSOLIDATION_SYNTHESIS.md`
- `00_project/projects/V11-05_knowledge_consolidation/PROJECT_BRIEF.md`
- `00_project/projects/V11-05_knowledge_consolidation/RE_AUDIT_REPORT.md`
- `00_project/projects/V11-05_knowledge_consolidation/REWORK_REPORT.md`

### V11-06

- `00_project/projects/V11-06_research_portfolio_wave_2/AUDIT_REPORT.md`
- `00_project/projects/V11-06_research_portfolio_wave_2/COMPLETION_REPORT.md`
- `00_project/projects/V11-06_research_portfolio_wave_2/PROJECT_BRIEF.md`

### V11-07

- `00_project/projects/V11-07_cross_system_review/AUDIT_REPORT.md`
- `00_project/projects/V11-07_cross_system_review/COMPLETION_REPORT.md`
- `00_project/projects/V11-07_cross_system_review/CROSS_SYSTEM_REVIEW.md`
- `00_project/projects/V11-07_cross_system_review/PROJECT_BRIEF.md`

### V11-08

- `00_project/projects/V11-08_final_audit_release/COMPLETION_REPORT.md`
- `00_project/projects/V11-08_final_audit_release/EDITOR_RELEASE_DECISION.md`
- `00_project/projects/V11-08_final_audit_release/PROJECT_BRIEF.md`
- `00_project/projects/V11-08_final_audit_release/RELEASE_CRITERIA_VERIFICATION.md`
- `00_project/projects/V11-08_final_audit_release/RELEASE_DECISION_PACKAGE.md`

## Target structure

The first physical simplification should be additive and low risk:

```text
00_project/
  ACTIVE_INDEX.md
  NEXT_ACTION.md
  DECISION_STACK_*.md
  OPEN_DECISIONS.md
  SCIENTIFIC_DEBT.md
  ROADMAP_V1_1.md
  [task-specific active references]
  projects/                 # only while link preservation is unresolved
  templates/
99_archive/
  00_project_history/       # future destination, not created by this report
```

Recommended order:

1. Keep the active set and the templates in place.
2. Mark the root reports and peer-review packages as history in navigation.
3. Audit links to closed project folders and historical reports.
4. Move history in one separately reviewed batch.
5. Re-run the active-agent startup path and verify that no authority was moved.

## Findings and risks

- The directory is not primarily too large because of active control; it is too
  flat because current control, reference, and history share one namespace.
- `OPEN_DECISIONS.md` is still active even though many entries are marked DONE;
  it should not be archived until a separate decision-register policy exists.
- `ROADMAP_V1_1.md` is closed as a program record but remains the strategic V1.1
  source of truth while that release context is relevant.
- The V11 project folders are coherent evidence bundles. Moving individual files
  would increase link and audit risk; any move should be folder-preserving.
- `COWORK_EXECUTION_PROTOCOL.md`, `SALES_CODEX_CONTEXT.md`, and the existing
  operating documents may overlap with the newer `.agents/` layer. This is a
  consolidation review candidate, not an automatic archive decision.
- Two working-tree files were locally read-protected. Their committed Git
  versions were readable and sufficient for this classification; the permission
  state should be treated as a repository hygiene issue separately.

## Decision gate

No physical archive or deletion should happen from this report alone. The next
safe decision is whether Felix wants to approve the proposed active set and a
link-audit pass for the closed V11 folders.
