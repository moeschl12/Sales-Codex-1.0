# Sales Codex V1.1 — Release Criteria

Status: Draft active criteria for V1.1  
Date: 2026-07-06

---

## 1. Repository Integrity

V1.1 may not be released unless:

- Git working tree is clean at release gate.
- Atlas compiler exits with code 0.
- Duplicate IDs = 0.
- Atlas output is current against the release baseline.
- Broken or unresolved references are either 0 or explicitly classified as accepted/deferred with owner and rationale.
- No status document contradicts the Roadmap on active/done/blocker state.

---

## 2. Research Integrity

V1.1 may not be released unless:

- Every central research claim is source-backed or explicitly uncertainty-marked.
- Every Editor Decision created during V1.1 has an explicit disposition.
- Every research integration includes repository impact analysis.
- No evidence level is upgraded without documented basis.
- Scientific Debt created during V1.1 is classified, prioritized or explicitly deferred.
- Research work includes counter-hypothesis or falsification sections where applicable.

---

## 3. Governance Integrity

V1.1 may not be released unless:

- There is exactly one strategic source of truth for V1.1 program state: `00_project/ROADMAP_V1_1.md`.
- `00_project/NEXT_ACTION.md` is a minimal launcher and does not contain a competing backlog.
- Open Decisions touched during V1.1 are classified as accepted, rejected, partially accepted, deferred or superseded.
- Accepted governance decisions are implemented or explicitly deferred.
- No new governance rule contradicts existing non-negotiable repository principles.

---

## 4. Knowledge-System Integrity

V1.1 may not be released unless:

- Key syntheses remain traceable to knowledge objects, sources or research artifacts.
- Contradictions are documented, not smoothed over.
- Context boundaries are visible where transfer is uncertain.
- Delivery outputs do not present claims as stronger than their source objects.
- New or changed synthesis objects pass an independent audit.

---

## 5. Delivery Integrity

V1.1 may not be released unless the Early Delivery Vertical Slice demonstrates:

- knowledge-object-to-output traceability,
- correct transfer of evidence status,
- visible uncertainty and boundary conditions,
- no unsupported new sales technique in the output,
- at least one chapter/section prototype,
- at least one workbook/training element,
- an audit finding whether the current knowledge architecture is sufficient for delivery scaling.

---

## 6. Atlas / Code Integrity

For actual code components, especially `08_knowledge_atlas/scripts/compile_atlas.py`:

- script runs successfully in local environment,
- no duplicate IDs,
- output files regenerate deterministically for the same repository state,
- any code changes are accompanied by focused tests or manually reproducible verification notes,
- no broad software metrics are required unless the codebase expands beyond the current Atlas-compiler scope.

---

## 7. Final Release Gate

V1.1 release requires:

1. V11-01 through V11-08 completed or explicitly re-scoped.
2. Completion report for every completed macro-project.
3. Independent audit report for every completed macro-project.
4. Final Release Audit.
5. Explicit Editor Release Decision by Felix.
