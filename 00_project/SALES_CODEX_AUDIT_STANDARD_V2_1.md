# SALES CODEX AUDIT STANDARD V2.1

**Document class:** Governance / Audit Operating Standard  
**Version:** 2.1  
**Status:** Proposed Canonical Standard  
**Applies to:** Repository-wide audits, V11 macro-project audits, research-project audits, focused re-audits, delivery audits  
**Default mode:** Read-only  
**Primary objective:** Reproducible, evidence-backed, low-false-positive audit outcomes across different auditors

---

# 0. Purpose

This standard defines **how** Sales Codex audits are performed, how evidence is collected, how findings are classified, and how verdicts are issued.

The standard is designed to reduce four recurring audit risks:

1. **State drift:** later research or integration makes earlier synthesis, Atlas, status, or delivery claims stale.
2. **Identifier drift:** IDs such as W-, RP-, MEC-, P-, T-, MOD-, OQ-, OD-, SD- or V11- identifiers change meaning or become ambiguous.
3. **Transition drift:** project starts and closures are not synchronised across the control plane.
4. **Audit inconsistency:** different auditors classify the same repository state differently because scope, evidence, or severity rules are vague.

The auditor's task is not to "find problems". The task is to determine whether the repository state is internally consistent, traceable, appropriately evidenced, and compliant with governance.

---

# 1. Audit Principles

## P-01 — Repository State Is the Source of Truth

Current canonical files override executor summaries, chat reports, old audit notes, stale Atlas outputs, and obsolete synthesis claims.

Historical documents remain valid as historical evidence, but must not be treated as current state without reconciliation.

## P-02 — Evidence Before Interpretation

Every finding must contain:

- exact affected path(s),
- observed repository state,
- expected state or governing rule,
- concrete inconsistency,
- risk,
- corrective action.

No finding may be based solely on intuition, style preference, or external best practice unless that rule is explicitly governed by repository policy.

## P-03 — Read-Only by Default

Audits must not edit files, create fixes, commit, push, start projects, close decisions, change evidence levels, or repair references.

Audit output is separate from remediation.

## P-04 — Work in Progress Is Not Automatically a Defect

Dirty working trees, untracked project files, or partial control-plane sync are not automatically findings.

They become findings only if one of the following applies:

- the state is represented as completed or released,
- the audit snapshot is claimed to be clean,
- dependent work has started from a contradictory state,
- multiple agents could plausibly act on conflicting launchers,
- the work-in-progress state violates an explicit gate.

## P-05 — Closed Editor Decisions Are Binding

An audit may detect contradiction with a later Editor Decision, incorrect implementation, or stale downstream summaries.

It may not reopen or reinterpret the Editor Decision without explicit governance authorization.

## P-06 — NOT VERIFIED Is Not FAIL

Unavailable evidence must be classified as:

- NOT VERIFIED — unavailable,
- NOT VERIFIED — insufficient package,
- NOT VERIFIED — permission issue,
- NOT VERIFIED — scope excluded.

A NOT VERIFIED item becomes a finding only if the missing verification materially affects the audit objective.

## P-07 — Distinguish Structure, Evidence, and Delivery

Graph proximity is not evidence strength.  
Evidence strength is not delivery readiness.  
Delivery readiness is not governance approval.  
Governance status is not scientific validation.

---

# 2. Audit Modes

## A. Full Repository Audit

Scope: all repository files and systems.

Use for release readiness, major program checkpoints, pre-scaling decisions, and repository-wide integrity review.

## B. Macro-Project Audit

Scope: one V11 project plus all directly affected control-plane and downstream artifacts.

## C. Research Project Audit

Scope: one W-project lifecycle plus integration effects.

## D. Focused Re-Audit

Scope: only prior findings and regression-sensitive areas.

## E. Delivery Audit

Scope: publication/training/workbook output and traceability to knowledge and evidence.

## F. Governance Audit

Scope: control plane, decisions, policies, lifecycle rules, task routing, and release gates.

---

# 3. Snapshot Gate

Before any substantive audit, record the snapshot.

## Mandatory commands

```text
git status
git status --short
git status --porcelain=v1
git branch -vv
git remote -v
git rev-parse HEAD
git rev-parse origin/main
git diff --name-status
git diff --stat
git diff --check
git ls-files --others --exclude-standard
```

## Snapshot classification

### CLEAN SNAPSHOT

Requirements:

- HEAD = origin/main,
- no staged changes,
- no unstaged changes,
- no untracked files.

### DIRTY BUT AUDITABLE SNAPSHOT

Allowed when:

- audit explicitly covers work in progress,
- dirty state is documented,
- audit distinguishes committed baseline from working-tree changes.

### NON-VERIFIABLE SNAPSHOT

Use when:

- commit cannot be identified,
- repository state cannot be accessed,
- snapshot provenance is ambiguous.

A non-verifiable snapshot blocks repository-release verdicts.

---

# 4. Severity Model

## Observation

Criteria:

- informative,
- no required action,
- no governance or integrity risk.

## Minor

Criteria:

- narrow defect,
- deterministic fix,
- low propagation risk,
- does not invalidate core project result.

## Major

At least one of:

- dependent work would rely on incorrect state,
- core project claim materially misclassified,
- control plane could cause duplicate or contradictory execution,
- lifecycle gate bypassed,
- repository claim conflicts with binding Editor Decision,
- audit cannot verify a material subsystem.

## Critical

At least one of:

- repository-wide corruption,
- duplicate canonical IDs with active semantic collision,
- evidence fabrication,
- unauthorized irreversible governance change,
- loss of traceability across a critical subsystem,
- release based on knowingly unverifiable or falsified state.

---

# 5. Verdict Model

## PASS

Requirements:

- 0 Critical,
- 0 Major,
- 0 Minor requiring closure.

Observations and Improvements are allowed.

## PASS WITH CONDITIONS

Requirements:

- 0 Critical,
- 0 blocking Major,
- remaining conditions are narrow, deterministic, and closure-verifiable.

## REWORK REQUIRED

Triggered by:

- one or more blocking Major findings,
- multiple interacting Minors that create material state risk,
- incomplete project result that cannot be closed by narrow edits.

## FAIL

Triggered by:

- Critical finding,
- pervasive integrity failure,
- invalid audit basis,
- evidence or governance corruption.

---

# 6. Evidence Standard for Findings

Every finding must include:

1. Finding ID
2. Severity
3. Title
4. Affected paths
5. Observed state
6. Expected state
7. Evidence
8. Risk
9. Required correction
10. Blocking effect
11. Verification method

A finding without evidence is invalid.

---

# 7. Deterministic Audit Rule Catalogue

The following rules are mandatory unless explicitly marked conditional.

## LEVEL 0 — Snapshot & Git Integrity

- **GIT-001:** Record branch name.
- **GIT-002:** Record HEAD commit hash.
- **GIT-003:** Record origin/main hash.
- **GIT-004:** Verify whether HEAD = origin/main.
- **GIT-005:** Record staged changes.
- **GIT-006:** Record unstaged changes.
- **GIT-007:** Record untracked files.
- **GIT-008:** Run `git diff --check`.
- **GIT-009:** Distinguish CRLF/LF warnings from actual whitespace errors.
- **GIT-010:** Record whether audit is against committed state or working tree.
- **GIT-011:** If dirty, identify whether changes predate the audit.
- **GIT-012:** Do not classify active work as repository drift without checking project execution state.
- **GIT-013:** Verify remote origin identity.
- **GIT-014:** Verify branch tracking relationship.
- **GIT-015:** Check for detached HEAD.
- **GIT-016:** Check for merge-conflict markers.
- **GIT-017:** Check for unresolved index conflicts.
- **GIT-018:** Check for unexpected generated files tracked in Git.
- **GIT-019:** Check for expected canonical files excluded by `.gitignore`.
- **GIT-020:** Bind final audit verdict to an exact commit or explicit dirty snapshot.

## LEVEL 1 — Repository Structure Integrity

- **STR-001:** Verify expected root governance files exist.
- **STR-002:** Verify numbered repository sections exist where governed.
- **STR-003:** Detect unexpected top-level folders.
- **STR-004:** Detect empty project folders without status explanation.
- **STR-005:** Detect duplicate files with near-identical names.
- **STR-006:** Detect conflicting `final`, `final2`, `new`, `copy` variants.
- **STR-007:** Verify project folders use canonical naming.
- **STR-008:** Verify completed research projects are under `completed/`.
- **STR-009:** Verify active research projects are under `active/`.
- **STR-010:** Verify archived projects are under `archived/`.
- **STR-011:** Check for active artifacts under completed projects.
- **STR-012:** Check for completed artifacts under active projects without status explanation.
- **STR-013:** Check broken relative Markdown links.
- **STR-014:** Check referenced local files exist.
- **STR-015:** Check cross-folder references use stable paths.
- **STR-016:** Detect orphan governance reports not referenced anywhere.
- **STR-017:** Detect audit reports stored outside project/audit conventions.
- **STR-018:** Detect closure reports without corresponding audited project.
- **STR-019:** Detect project folders without README or status entry.
- **STR-020:** Check naming consistency for date-stamped reports.

## LEVEL 2 — Control Plane Integrity

- **CP-001:** Compare `CURRENT_STATE.md` against `ROADMAP_V1_1.md`.
- **CP-002:** Compare `CURRENT_STATE.md` against `NEXT_ACTION.md`.
- **CP-003:** Compare `SESSION_BRIEF.md` against `NEXT_ACTION.md`.
- **CP-004:** Compare `SESSION_LOG.md` latest entry against current launcher.
- **CP-005:** Compare `RESEARCH_STATUS.md` against actual `active/` contents.
- **CP-006:** Compare `RESEARCH_STATUS.md` against actual `completed/` contents.
- **CP-007:** Compare `RESEARCH_PORTFOLIO.md` against active RP themes.
- **CP-008:** Verify each V11 project has one current state.
- **CP-009:** Verify no V11 project is simultaneously `LATER` and `ACTIVE`.
- **CP-010:** Verify no project is both `COMPLETED` and `AWAITING AUDIT` unless lifecycle explicitly distinguishes them.
- **CP-011:** Verify audit closure state is reflected in launcher files.
- **CP-012:** Verify failed/rework audit state blocks dependent launchers when required.
- **CP-013:** Verify closed conditions are marked closed consistently.
- **CP-014:** Verify historical audit verdicts are not overwritten.
- **CP-015:** Verify `NEXT_ACTION.md` identifies exactly one operational launcher unless parallel execution is explicitly authorized.
- **CP-016:** Verify blocked items have named dependencies.
- **CP-017:** Verify deferred governance items remain deferred.
- **CP-018:** Verify active research work is visible in control plane if execution has formally started.
- **CP-019:** Distinguish WIP-only local state from committed program state.
- **CP-020:** Verify no control-plane file claims clean release state when Git snapshot is materially dirty.

## LEVEL 3 — Research Lifecycle Integrity

- **RP-001:** Every active W-project has a README.
- **RP-002:** Every active W-project has a Research Question artifact.
- **RP-003:** Every Stufe-2+ project has Initial Hypothesis.
- **RP-004:** Every Stufe-3+ project has Master Review.
- **RP-005:** Every Stufe-4+ project has Red Team Review.
- **RP-006:** Every decision-ready project has Decision Brief.
- **RP-007:** Every integrated completed project has Editor Decision.
- **RP-008:** Every integrated completed project has Repository Integration Log or Report.
- **RP-009:** Every completed project has Health Check.
- **RP-010:** Every completed project has README status `COMPLETED`.
- **RP-011:** Every completed project has references/provenance.
- **RP-012:** Every project with open residual questions records them explicitly.
- **RP-013:** Residual questions transferred to Scientific Debt are traceable.
- **RP-014:** No completed project remains under `active/`.
- **RP-015:** No active project is listed as completed in `RESEARCH_STATUS.md`.
- **RP-016:** Editor Decision outcome matches integration scope.
- **RP-017:** Rejected theory components are not silently integrated.
- **RP-018:** Partially accepted projects distinguish accepted core from rejected formalism.
- **RP-019:** No W-project is reopened by downstream synthesis without governance authorization.
- **RP-020:** New W-project IDs do not collide with contradiction candidate IDs.

## LEVEL 4 — Identifier Integrity

- **ID-001:** All canonical object IDs are unique.
- **ID-002:** Filename ID matches internal object ID.
- **ID-003:** Object folder matches object type.
- **ID-004:** W-project IDs are unique.
- **ID-005:** W-contradiction IDs are semantically stable.
- **ID-006:** RP IDs are unique.
- **ID-007:** OQ IDs are unique within their project scope.
- **ID-008:** OD IDs are unique.
- **ID-009:** Scientific Debt IDs are unique where formal IDs exist.
- **ID-010:** No identifier is silently reassigned.
- **ID-011:** Renamed identifiers preserve audit trail.
- **ID-012:** References to superseded identifiers are updated or explicitly historical.
- **ID-013:** No unresolved future ID is treated as existing object.
- **ID-014:** Candidate IDs are clearly distinguished from activated project IDs.
- **ID-015:** Check W-006/W-007 continuity.
- **ID-016:** Check OQ-2 semantic identity against canonical W-001 source.
- **ID-017:** Check V11 project numbering continuity.
- **ID-018:** Check object IDs referenced in synthesis actually exist.
- **ID-019:** Check duplicate semantic labels across distinct IDs for accidental duplication.
- **ID-020:** Check one ID is not used for multiple object types.

## LEVEL 5 — Knowledge Base Integrity

- **KB-001:** Count objects by type.
- **KB-002:** Compare counts against Atlas manifest/report.
- **KB-003:** Detect duplicate IDs.
- **KB-004:** Detect missing internal IDs.
- **KB-005:** Detect missing source IDs where required.
- **KB-006:** Detect invalid evidence-level labels.
- **KB-007:** Detect contradictory evidence levels for the same claim across linked objects.
- **KB-008:** Detect placeholder markers.
- **KB-009:** Detect `TODO` markers.
- **KB-010:** Detect `NSTD` markers and verify disposition.
- **KB-011:** Detect `Draft`/`Candidate` status markers.
- **KB-012:** Check object status terminology against governance policy.
- **KB-013:** Verify mechanisms explain principles where claimed.
- **KB-014:** Verify principles do not masquerade as mechanisms.
- **KB-015:** Verify models do not duplicate mechanism identity without justification.
- **KB-016:** Check linked object IDs exist.
- **KB-017:** Check obvious circular dependency loops.
- **KB-018:** Check source traceability.
- **KB-019:** Check research integrations changed only intended objects.
- **KB-020:** Check no knowledge object changed in projects whose scope prohibited object edits.

## LEVEL 6 — Cross-Corpus State Integrity

- **CCS-001:** Compare synthesis claims against later Research Program decisions.
- **CCS-002:** Compare Atlas structural claims against current object contents.
- **CCS-003:** Compare Scientific Debt status against later project closure.
- **CCS-004:** Compare Open Questions against later research outcomes.
- **CCS-005:** Compare contradiction matrix status against Editor Decisions.
- **CCS-006:** Compare delivery claims against current evidence state.
- **CCS-007:** Compare current control plane against project completion artifacts.
- **CCS-008:** Check W-001 status after Editor Decision and integration.
- **CCS-009:** Check W-002 status after completed transfer research.
- **CCS-010:** Check W-003 status after MEC-0030 integration.
- **CCS-011:** Check W-004 status after Buying-Center integration.
- **CCS-012:** Check P-0040 status after W-003 extension.
- **CCS-013:** Check MEC-0018 family after V11-05 analysis.
- **CCS-014:** Check W-006/W-007 after V11-05 rework.
- **CCS-015:** Check OQ-2 wording after V11-05 closure.
- **CCS-016:** Check stale Atlas priority recommendations against completed edits.
- **CCS-017:** Check old synthesis `unresolved` labels against completed research.
- **CCS-018:** Check historical session log entries are not mistaken for current state.
- **CCS-019:** Check delivery scaling recommendation against latest governance state.
- **CCS-020:** Check active project selection against portfolio and blockers.

## LEVEL 7 — Evidence Integrity

- **EV-001:** Every high-confidence claim has appropriate source support.
- **EV-002:** Evidence level matches source type.
- **EV-003:** Practitioner data is not represented as peer-reviewed evidence.
- **EV-004:** Proprietary data limitations are visible.
- **EV-005:** Publication-bias risk is documented where applicable.
- **EV-006:** Replication risk is documented where applicable.
- **EV-007:** B2B transfer is not inferred from lab/B2C evidence without caveat.
- **EV-008:** High-ticket B2C transfer is not inferred without caveat.
- **EV-009:** Buying-center transfer is not inferred from individual-level evidence without caveat.
- **EV-010:** Editor Decisions do not overstate reviewed evidence.
- **EV-011:** Rejected direct-evidence searches remain clearly negative.
- **EV-012:** Category-2 evidence is not misrepresented as direct evidence.
- **EV-013:** CEB/Challenger 53/38/9 claims are appropriately caveated.
- **EV-014:** MEC-0018 priming risk remains visible where causally relevant.
- **EV-015:** MEC-0018 risk is not propagated to unrelated cross-links.
- **EV-016:** MEC-0002/P-0002 harmonization debt is not silently resolved.
- **EV-017:** Evidence-level upgrades are traceable to source review.
- **EV-018:** No claim cites a source absent from repository/reference index where governance requires inclusion.
- **EV-019:** Scientific Debt entries distinguish `unknown` from `false`.
- **EV-020:** No delivery artifact removes material boundary conditions.

## LEVEL 8 — Atlas Integrity

- **AT-001:** Atlas manifest exists.
- **AT-002:** Compiler version recorded.
- **AT-003:** Node count matches knowledge base count.
- **AT-004:** Duplicate ID count is zero or explained.
- **AT-005:** Unresolved references are enumerated.
- **AT-006:** Orphan count is documented.
- **AT-007:** Connected component count is documented.
- **AT-008:** Compiler output date is recorded.
- **AT-009:** Atlas output is not treated as fresh if object state changed after generation.
- **AT-010:** Atlas centrality is not treated as evidence strength.
- **AT-011:** Graph proximity is not treated as causal dependency.
- **AT-012:** Stale graph claims are reconciled after object updates.
- **AT-013:** Known unresolved T-0048 references remain visible until resolved.
- **AT-014:** No duplicate IDs are hidden by parser behavior.
- **AT-015:** Compiler warning behavior is documented.
- **AT-016:** Read-only audit does not overwrite Atlas outputs.
- **AT-017:** Dry-run or compare mode is used if available.
- **AT-018:** If compiler cannot be run read-only, report output as NOT FRESHLY VERIFIED.
- **AT-019:** Atlas recommendations are checked against subsequent completed work.
- **AT-020:** Structural orphan status is distinguished from semantic isolation.

## LEVEL 9 — Delivery & Publication Traceability

- **DL-001:** Every publication artifact identifies its knowledge basis.
- **DL-002:** Every workbook exercise maps to one or more mechanisms/principles/techniques.
- **DL-003:** Every training sequence identifies intended mechanism.
- **DL-004:** Every chapter fragment avoids unsupported claims.
- **DL-005:** Evidence level is not overstated in delivery language.
- **DL-006:** Boundary conditions are visible where relevant.
- **DL-007:** Target audience assumptions are explicit.
- **DL-008:** Delivery artifact does not imply `validated` status unless governance allows it.
- **DL-009:** T12 remains inactive unless explicitly authorized.
- **DL-010:** Broad scaling is not inferred from one vertical slice.
- **DL-011:** Traceability links resolve.
- **DL-012:** Delivery examples do not introduce new ungoverned claims.
- **DL-013:** Workbook questions do not exceed evidence-supported interpretation.
- **DL-014:** Training sequence ordering is traceable to models/principles.
- **DL-015:** Delivery output references current, not stale, object state.

## LEVEL 10 — Governance Integrity

- **GOV-001:** Open Decisions remain open unless explicitly closed.
- **GOV-002:** Reserved Decisions are not closed by executors.
- **GOV-003:** T12 remains inactive unless Editor-authorized.
- **GOV-004:** Task Types are not modified outside governance scope.
- **GOV-005:** Autonomy policy is respected.
- **GOV-006:** Audit requirements are satisfied before dependent launches.
- **GOV-007:** Completion reports exist where required.
- **GOV-008:** Audit reports exist where required.
- **GOV-009:** Rework reports exist after REWORK REQUIRED remediation.
- **GOV-010:** Closure reports exist after condition closure where governed.
- **GOV-011:** Historical verdicts are not rewritten.
- **GOV-012:** Re-audit verdicts are stored separately.
- **GOV-013:** PASS WITH CONDITIONS remains historically distinct from PASS.
- **GOV-014:** Condition closure is explicit and traceable.
- **GOV-015:** V11 dependencies are respected.
- **GOV-016:** Portfolio blockers are not silently bypassed.
- **GOV-017:** RP-005 remains blocked until OD-010 or explicit alternative decision.
- **GOV-018:** RP-006 architecture question is not silently resolved by research execution.
- **GOV-019:** No project defines its own governance exception.
- **GOV-020:** Governance changes have named authority and date.

## LEVEL 11 — Regression Integrity

- **REG-001:** Check whether closed W-001 was reopened by downstream synthesis.
- **REG-002:** Check whether W-006 semantic identity changed.
- **REG-003:** Check whether W-007 was reassigned.
- **REG-004:** Check whether OQ-2 meaning drifted.
- **REG-005:** Check whether P-0040 reverted to stale isolation status.
- **REG-006:** Check whether MEC-0018 risk was overgeneralized again.
- **REG-007:** Check whether V11-04 scaling limitation was later ignored.
- **REG-008:** Check whether closed audit conditions reappear in control plane.
- **REG-009:** Check whether stale session-log statements were promoted to current state.
- **REG-010:** Check whether later Atlas reports overwrite stronger object-level evidence.
- **REG-011:** Check whether completed research is duplicated as new project without gap analysis.
- **REG-012:** Check whether failed theories reappear without new evidence.
- **REG-013:** Check whether rejected SCSM formalization resurfaces.
- **REG-014:** Check whether direct-evidence absence becomes falsely represented as positive evidence.
- **REG-015:** Check whether `candidate` becomes `active` without activation decision.

## LEVEL 12 — Audit Quality Assurance

- **AQ-001:** Did the auditor separate WIP from defect?
- **AQ-002:** Did the auditor bind the audit to a snapshot?
- **AQ-003:** Did each finding cite exact evidence?
- **AQ-004:** Did severity match the defined criteria?
- **AQ-005:** Were NOT VERIFIED cases identified?
- **AQ-006:** Did the auditor avoid external sources if prohibited?
- **AQ-007:** Did the auditor avoid remediation during audit?
- **AQ-008:** Did the auditor distinguish historical from current state?
- **AQ-009:** Did the auditor verify key claims against raw canonical artifacts?
- **AQ-010:** Did the auditor avoid treating Atlas centrality as evidence?
- **AQ-011:** Did the auditor avoid repeating executor summaries as facts?
- **AQ-012:** Did the auditor identify scope limitations?
- **AQ-013:** Did the auditor avoid inflating minor hygiene issues into Majors?
- **AQ-014:** Did the auditor identify interacting Minor findings that may jointly become Major?
- **AQ-015:** Did the auditor make explicit what blocks progression and what does not?

---

# 8. False Positive Prevention Rules

## FP-01 — Active Work

Do not classify dirty WIP as Major unless execution state is falsely represented, dependent work is launched from conflicting state, or a required clean-state gate was violated.

## FP-02 — Deferred Governance

A deferred decision is not a defect unless downstream work assumes it is decided, status is inconsistent across control plane, or governance dependency is bypassed.

## FP-03 — Scientific Debt

Registered Scientific Debt is not itself a defect.

Finding only if debt disappears without resolution, downstream claims ignore the debt, or priority/status is falsely represented.

## FP-04 — Historical Documents

Historical contradiction or research reports may legitimately contain outdated statements.

Finding only if they are represented as current or current synthesis/control plane relies on them without reconciliation.

## FP-05 — NOT VERIFIED

Do not convert inaccessible files into a content finding.

Possible process finding only if audit completeness materially depends on them.

---

# 9. Finding Escalation Decision Tree

1. Is the issue real and repository-evidenced?
   - No → no finding.
   - Yes → continue.
2. Is it only informational?
   - Yes → Observation.
3. Can it be fixed by one narrow deterministic edit without affecting project logic?
   - Yes → Minor.
4. Does dependent work risk using wrong state, wrong evidence, wrong ID, or wrong governance?
   - Yes → Major.
5. Is canonical integrity, traceability, or governance fundamentally compromised?
   - Yes → Critical.

---

# 10. Audit Report Template

## 1. Executive Summary

Maximum 15 sentences.

## 2. Snapshot

- Branch
- Commit
- origin/main
- Working Tree
- Audit mode
- Scope
- Tools run

## 3. Overall Verdict

One of:

- PASS
- PASS WITH CONDITIONS
- REWORK REQUIRED
- FAIL

## 4. Finding Summary

| Severity | Count |
|---|---:|
| Critical | |
| Major | |
| Minor | |
| Observation | |
| Improvement | |

## 5. Critical Findings

## 6. Major Findings

## 7. Minor Findings

## 8. Observations

## 9. Improvement Opportunities

## 10. Control Plane Assessment

## 11. Research Program Assessment

## 12. Knowledge Base Assessment

## 13. Evidence Architecture Assessment

## 14. Atlas Assessment

## 15. Delivery Assessment

## 16. Governance Assessment

## 17. Regression Assessment

## 18. Audit Quality Self-Check

## 19. Blockers

Explicitly list what blocks next work, what does not block, and the exact dependency.

## 20. Closure Plan

For each action classify:

- T3_WARTUNG
- T8_AUDIT
- T11_SCIDEBT
- Governance Decision
- Research Project
- Delivery

## 21. Final Recommendation

---

# 11. Minimum Coverage Requirements by Audit Type

## Full Repository Audit

Mandatory levels: 0–12, all.

## Macro-Project Audit

Mandatory: 0, 2, 3, 5, 6, 7, 10, 11, 12.

Conditional: 1, 4, 8, 9.

## Research Project Audit

Mandatory: 0, 2, 3, 4, 5, 6, 7, 10, 11, 12.

## Focused Re-Audit

Mandatory: 0, all original finding-closure checks, relevant regression rules, 12.

Do not rerun unrelated domains.

## Delivery Audit

Mandatory: 0, 5, 6, 9, 10, 11, 12.

---

# 12. Required Machine-Assisted Checks

Where tooling exists, use:

- filename/ID duplicate scan,
- broken reference scan,
- DOI duplicate scan,
- source-ID scan,
- Markdown-link scan,
- Atlas compiler or dry-run compare,
- `git diff --check`,
- project lifecycle inventory,
- status cross-file comparison.

Tool output is evidence, not verdict.

---

# 13. Audit Closure Protocol

After remediation:

1. Verify only scoped findings were changed.
2. Re-run relevant rules.
3. Run regression-sensitive checks.
4. Run `git diff --check`.
5. Confirm expected control-plane state.
6. Confirm no forbidden object changes.
7. Issue:
   - CONDITION CLOSED, or
   - REWORK STILL OPEN.

Historical audit verdict remains unchanged.

---

# 14. Recommended Next Evolution

The next version should add:

- machine-readable YAML/JSON rule registry,
- automated rule executor where deterministic,
- rule ownership by repository subsystem,
- audit coverage score,
- change-impact routing,
- read-only Atlas compare mode,
- automatic control-plane state diff,
- automatic lifecycle completeness matrix.

---

# 15. Canonical Intent

The Sales Codex audit system is designed to support **large autonomous work packages with independent verification**.

The target operating model is:

> Large bounded execution package  
> → deterministic internal checkpoints  
> → independent audit  
> → narrow remediation  
> → focused re-audit  
> → explicit closure

The purpose of this standard is not to increase process overhead.

Its purpose is to make autonomous execution safer, faster to verify, and less dependent on the individual auditor.
