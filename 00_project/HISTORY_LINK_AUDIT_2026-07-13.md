# History Link Audit

Status: first archive batch moved; further moves not authorized by this report
Updated: 2026-07-13

## Scope and method

The audit covers the historical candidates identified in
`PROJECT_FILE_CLASSIFICATION_2026-07-13.md`:

- 34 historical root files
- 4 peer-review decision files
- 30 files in the eight closed V11 project folders

The workspace inventory contained 838 files at audit time. References were
checked by filename and project-directory name across Markdown files, with a
second pass over explicit Markdown link targets. This matters because the
repository uses many backtick file references rather than formal Markdown
links.

## Result

The repository is not ready for a broad archive move.

- 26 of 34 historical root files still have inbound references from the active control set.
- All 8 V11 project directories still have inbound references from the active control set.
- 2 of 4 peer-review files have active inbound references.
- 10 historical files have no active-control inbound reference and are the first physical-move candidates.
- The existing `99_archive/` content is already physically separated and was not changed.
- The 10 Tier 1 files were moved into `99_archive/00_project_history/` after the audit.

## Completed first archive batch

These files had no active-control inbound reference. Their historical and
project references were updated to the archive path before the move.

### Root files

- `99_archive/00_project_history/CLOSURE_REPORT_V1.1_2026-07-13.md`
- `99_archive/00_project_history/COWORK_PERFORMANCE_AUDIT_2026-07-05.md`
- `99_archive/00_project_history/PROCESS_PATTERN_ANALYSIS_2026-07.md`
- `99_archive/00_project_history/RELEASE_NOTES_v1.1.md`
- `99_archive/00_project_history/SALES_CODEX_DECISION_ARCHITECTURE_AUDIT_2026-07-05.md`
- `99_archive/00_project_history/SPRINT_2_ABSCHLUSSBERICHT.md`
- `99_archive/00_project_history/V1_1_REVIEW_SYNTHESIS.md`
- `99_archive/00_project_history/V11_01_CLAUDE_EXECUTION_PROMPT.md`

### Peer-review files

- `99_archive/00_project_history/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_001.md`
- `99_archive/00_project_history/peer_review/decisions/RELEASE_REPORT_SPRINT_001_PEER_REVIEW.md`

### Post-move conditions

1. Keep the archive path stable.
2. Do not treat these files as active control.
3. Re-run the reference scan after any future archive move.

## Tier 2: hold in place

The following groups have active-control inbound references and should remain
where they are until a dedicated link-update pass is approved.

### Historical root files with active inbound references

- `00_project/ACADEMIC_RECOVERY_PLAN.md`
- `00_project/ACADEMIC_RECOVERY_REPORT.md`
- `00_project/ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`
- `00_project/BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md`
- `00_project/changelog.md`
- `00_project/CLOSURE_REPORT_V11-02_V11-03_2026-07-06.md`
- `00_project/CLOSURE_REPORT_V11-04_2026-07-07.md`
- `00_project/CLOSURE_REPORT_V11-05_2026-07-07.md`
- `00_project/CLOSURE_REPORT_V11-06_2026-07-12.md`
- `00_project/CLOSURE_REPORT_V11-07_2026-07-13.md`
- `00_project/CODEX_AUDIT_2026-07.md`
- `00_project/CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md`
- `00_project/COWORK_TOKEN_OPTIMIZATION_SPRINT_1_REPORT.md`
- `00_project/DECISION_ARCHITECTURE_SPRINT_2_REPORT.md`
- `00_project/EDITORIAL_REVIEW_SPRINT_MEC0018_REPORT.md`
- `00_project/EVIDENCE_ARCHITECTURE_CHECK_2026-07-06.md`
- `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`
- `00_project/OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`
- `00_project/POST_MORTEM_B0002.md`
- `00_project/POST_MORTEM_INFLUENCE_PLAN.md`
- `00_project/RESEARCH_PORTFOLIO_CHECKPOINT_1.md`
- `00_project/RESEARCH_PORTFOLIO_INITIALIZATION_REPORT.md`
- `00_project/SESSION_LOG.md`
- `00_project/VALIDIERUNGSSPRINT_MEC0010-0012.md`
- `00_project/WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`
- `00_project/WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md`

### Peer-review files with active inbound references

- `00_project/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`
- `00_project/peer_review/decisions/SCRP-0001_Sales_Core.md`

### Closed V11 project directories

All eight folders remain referenced by active status, roadmap, decision, or
governance documents:

- `00_project/projects/V11-01_baseline_control_plane/`
- `00_project/projects/V11-02_evidence_architecture_resolution/`
- `00_project/projects/V11-03_governance_integrity_atlas/`
- `00_project/projects/V11-04_early_delivery_vertical_slice/`
- `00_project/projects/V11-05_knowledge_consolidation/`
- `00_project/projects/V11-06_research_portfolio_wave_2/`
- `00_project/projects/V11-07_cross_system_review/`
- `00_project/projects/V11-08_final_audit_release/`

These folders should be moved only as intact evidence bundles, after a path-
rewrite plan has been prepared.

## Active-control reference pattern

The most important active files that still point into history are:

- `CURRENT_STATE.md`
- `SESSION_BRIEF.md`
- `PROJECT_BOOTSTRAP.md`
- `00_project/NEXT_ACTION.md`
- `00_project/DECISION_STACK_2026-07-13.md`
- `00_project/OPEN_DECISIONS.md`
- `00_project/SCIENTIFIC_DEBT.md`
- `00_project/ROADMAP_V1_1.md`
- `00_project/KNOWLEDGE_ATLAS_GOVERNANCE.md`
- `00_project/DECISION_BRIEF_OD-009_TO_OD-012_2026-07-13.md`
- `00_project/EDITOR_DECISION_OD-009_TO_OD-012_2026-07-13.md`

This confirms that historical material is not merely decorative. Parts of it
are still used as evidence anchors by current governance and quality records.

## Markdown link check

The repository contains mostly inline backtick references instead of formal
Markdown links. The initial scanner falsely classified the historical example
`[Text](Pfad.md)` in `99_archive/v1.0_release/REPOSITORY_CONSOLIDATION_REPORT_RC1.md`
as a real link. After excluding inline-code examples, the check found zero
formal Markdown links and zero missing Markdown link targets.

## Recommended next action

The next archive move should wait until a separate link-update manifest exists
for the remaining Tier 2 material. In particular, all eight V11 project
folders still need to remain in place until their active evidence references
are deliberately rewritten.
