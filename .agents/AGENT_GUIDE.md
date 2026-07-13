# Sales Codex Agent Guide

Status: shared operational draft
Audience: Claude, Codex, ChatGPT, Gemini, Perplexity, and other repository agents
Authority: subordinate to the repository authority stack

This guide defines the common way of working in the Sales Codex. It is an
operational entrypoint, not a new methodology, template system, governance
layer, or source of truth. If it conflicts with a repository authority, the
authority file wins.

## 1. Authority and Scope

Use this precedence order:

1. `AGENTS.md`
2. `PROJECT_BOOTSTRAP.md`
3. `SESSION_BRIEF.md`
4. `00_project/ACTIVE_INDEX.md`
5. `00_project/NEXT_ACTION.md`
6. `TASK_TYPES.md`
7. The task-specific framework, governance, template, source, or project files
8. `.agents/AGENT_GUIDE.md` and the remaining `.agents/` helper files

The repository is the only source of truth. Chat messages are temporary
instructions and context; they do not become knowledge objects or project
state automatically.

Every agent works under the same rules. The agent name changes the available
tools or the assigned role, but not the evidence standard, traceability
requirement, change boundaries, or editorial authority.

## 2. Session Start

At the beginning of a task:

1. Read `PROJECT_BOOTSTRAP.md`.
2. Read `SESSION_BRIEF.md` and `00_project/NEXT_ACTION.md` as part of the
   mandatory startup sequence.
3. Read `00_project/ACTIVE_INDEX.md` for navigation and current status.
4. Classify the request using `TASK_TYPES.md`.
5. Load only the files permitted and required by that task type.
6. Check for an existing object, decision, report, or task file before creating
   a new one.

Do not perform a broad repository scan unless the task explicitly requires an
architecture, audit, consistency, or other repository-wide view.

Before writing, state internally or in the work record:

- task type and objective
- assigned role
- files and directories in scope
- intended output or change
- stop or escalation conditions

## 3. Task Routing

Use the closest task type from `TASK_TYPES.md`. If the task type is not
obvious, state the chosen type and the reason briefly. Ask for clarification
only when competing interpretations would change the write scope or editorial
decision.

| Request | Task type | Default output |
|---|---|---|
| Analyse one book or source work | T1 Book Mode | source analysis and typed objects |
| Change methodology or framework | T2 Framework | proposal; no direct authority change |
| Fix or maintain named files | T3 Maintenance | scoped file change |
| Inspect or redesign repository structure | T4 Architecture | architecture proposal |
| Review evidence, objects, or quality | T5 Review | findings and validation record |
| Inspect a defined repository slice | T6 Audit | read-only audit report |
| Check one consistency rule | T7 Consistency | findings; no silent correction |
| Resolve an editorial or governance question | T8 Governance | decision input; Felix decides |
| Prepare a release or freeze | T9 Release | release or freeze record |
| Conduct named research | T10 Research | lifecycle-stage research artifact |
| Recover scientific or evidence quality | T11 Scientific Debt | targeted recovery plan/work |
| Prepare publication material | T12 Publication | validated material in `05_publications/` |

Task-specific rules always narrow the scope further. A request to “clean up”
does not authorize a repository-wide refactor, archive move, framework change,
or knowledge-base rewrite.

## 4. Common Operating Sequence

For every task, use this sequence:

1. **Intake:** identify the request, task type, role, and boundaries.
2. **Load:** read the authority files and only the relevant source material.
3. **Inspect:** search for existing objects, duplicates, related decisions,
   contradictions, and applicable templates.
4. **Decide the action level:** report, propose, draft, or implement. Do not
   implement when the task type or authority requires a proposal.
5. **Work:** preserve existing structure, naming, templates, IDs, and evidence
   links.
6. **Review:** check traceability, uncertainty, context, limits, contradictions,
   and template compliance.
7. **Record:** write the result to the appropriate repository location. Update
   status or logs only to the extent required by the governing task rules.
8. **Close:** summarize changed files, unresolved questions, validation, and
   the next authorized step.

Do not turn an observation into a claim, a claim into a mechanism, or a
mechanism into a principle without the required evidence and classification.

## 5. Knowledge Pipeline

Knowledge work follows the established sequence:

`SRC -> ST -> A -> MEC -> P -> T -> MOD -> VAL -> Abschlussbericht`

- `SRC`: source record and source identity
- `ST`: source-grounded statement, only from the primary text
- `A`: assumption or interpretation, explicitly marked
- `MEC`: causal or functional mechanism with context
- `P`: principle supported by at least two mechanisms or assumptions under the
  current V1.1 rule
- `T`: concrete technique tied to a principle and its conditions
- `MOD`: model or higher-order structure built from existing objects
- `VAL`: validation, limitations, uncertainty, and contradiction review

Do not skip stages by presenting an interpretation as a source statement or a
single observation as a general principle. Consult the relevant framework and
templates for the exact object fields.

## 6. Evidence and Canonicalization

The following rules apply to every agent:

- Never invent sources, quotations, facts, IDs, repository state, or evidence.
- Use the repository record and accessible primary text as the basis for claims.
- Mark uncertainty, missing context, limits, and competing interpretations.
- Preserve contradictions; document them instead of smoothing them away.
- Before creating an object, search for similar objects and apply the existing
  canonicalization rules:
  - identical causal structure and context: merge or reuse;
  - same causal structure with different context: extend the existing object
    and record the context difference;
  - different causal structure: create a new object only when authorized.
- Apply the Rule of Three where the governing methodology requires independent
  contexts for a mechanism.
- A bestseller, common belief, or remembered fact is not evidence by itself.

## 7. Change Boundaries

Without explicit editorial authorization, do not:

- change methodology, framework rules, templates, categories, or authority
  files;
- change evidence classifications, close decisions, or resolve contradictions
  on behalf of Felix;
- create a new macro-project, research project, knowledge object, or publication
  outside the permitted task scope;
- move, archive, rename, or delete repository files as a cleanup side effect;
- expand a named maintenance task into adjacent improvements;
- commit or push changes merely because the files are technically complete.

Architecture requests are normally proposals first. Governance questions are
decision inputs first. Research artifacts remain in the research lifecycle and
enter the knowledge base only after the required Editor Decision and repository
integration step.

## 8. Roles and Collaboration

Roles are complementary, not competing authorities:

- **Editor:** performs scoped editorial work and protects the repository model;
  Felix retains final decisions.
- **Scientific Editor:** tests claims, mechanisms, alternatives, evidence gaps,
  and generalizations; does not silently upgrade evidence.
- **Validation Reviewer:** checks references, templates, uncertainty, ethics,
  and limits; reports defects instead of rewriting them without instruction.
- **Researcher:** works inside the named research lifecycle and does not
  integrate findings early.

Claude, Codex, Gemini, ChatGPT, Perplexity, and other agents should assume that
another agent may continue the work. Therefore:

- leave explicit file-based traceability;
- do not overwrite another agent's work without inspecting it;
- do not create parallel versions when an existing object or decision record
  can be extended;
- distinguish completed, proposed, blocked, and unresolved work;
- hand off with file paths, scope, findings, and the next permitted action.

## 9. Stop and Escalate

Stop and record the issue when:

- a required primary source is inaccessible;
- a file is damaged or its authority is unclear;
- canonicalization cannot be resolved from repository evidence;
- framework or governance files conflict;
- the task requires an editorial, ethical, methodological, or release decision;
- the requested change would cross the declared scope.

Use `00_project/OPEN_DECISIONS.md`, `00_project/SCIENTIFIC_DEBT.md`, or the
task-specific decision/report format when the governing rules call for one.
Do not hide the blocker by making a best-guess change.

## 10. Completion Contract

Every completed task should leave a concise handoff containing:

- task type and objective
- files inspected and changed
- result or findings
- evidence and uncertainty status
- unresolved decisions or blockers
- validation performed
- next permitted action

For knowledge work, also name the object types and source references. For
reviews and audits, findings come before general summary. For proposals, keep
the proposal separate from implementation. For changes, do not claim tests or
validation that were not actually performed.

## 11. Maintenance of This Guide

This guide may be revised only when the change is consistent with the
repository authorities and does not silently alter methodology or governance.
If a rule belongs in `AGENTS.md`, `PROJECT_BOOTSTRAP.md`, `TASK_TYPES.md`, or a
framework file, update that authority instead of duplicating it here. Any
conflict is resolved in favour of the higher authority until the guide is
corrected.
