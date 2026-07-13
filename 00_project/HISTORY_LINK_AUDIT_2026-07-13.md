# History Link Audit

Status: audit complete; no physical moves authorized
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
- No file was moved, renamed, or deleted by this audit.

## Tier 1: candidates for a later first archive batch

These files are not referenced by the selected active control set. They are
still referenced by historical reports, project records, or archive material,
so a future move must update those references first.

### Root files

- `00_project/CLOSURE_REPORT_V1.1_2026-07-13.md`
- `00_project/COWORK_PERFORMANCE_AUDIT_2026-07-05.md`
- `00_project/PROCESS_PATTERN_ANALYSIS_2026-07.md`
- `00_project/RELEASE_NOTES_v1.1.md`
- `00_project/SALES_CODEX_DECISION_ARCHITECTURE_AUDIT_2026-07-05.md`
- `00_project/SPRINT_2_ABSCHLUSSBERICHT.md`
- `00_project/V1_1_REVIEW_SYNTHESIS.md`
- `00_project/V11_01_CLAUDE_EXECUTION_PROMPT.md`

### Peer-review files

- `00_project/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_001.md`
- `00_project/peer_review/decisions/RELEASE_REPORT_SPRINT_001_PEER_REVIEW.md`

### Conditions before moving Tier 1

1. Update all historical, project, archive, and navigation references.
2. Preserve the original relative path in a redirect/index note if required by the repository link convention.
3. Move complete logical groups, not individual report fragments.
4. Re-run the reference scan after the move.

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
Markdown links. The explicit Markdown-link pass checked one formal relative
link and found one missing target:

- `99_archive/v1.0_release/REPOSITORY_CONSOLIDATION_REPORT_RC1.md` references `Pfad.md`.

This appears to be an old placeholder or historical link defect. It is
independent of the proposed history moves and should be handled as a separate
archive-hygiene item.

## Recommended next action

Do not move Tier 1 yet. First decide whether the target archive location should
be `99_archive/00_project_history/` or a more specific structure such as
`99_archive/v1.1_history/`. Then prepare a single path-update manifest for the
10 Tier 1 files, run it as a reviewable change, and verify the active startup
path afterwards.
