# Sales Codex Agent Control Plane

Status: operational helper layer
Authority: subordinate to `AGENTS.md`, `PROJECT_BOOTSTRAP.md`, `TASK_TYPES.md`, `00_project/NEXT_ACTION.md`, and the relevant framework files

---

## Purpose

This directory gives all AI agents a compact project-local control plane. It does not introduce a new Sales Codex methodology, a new template system, or a new source of truth.

All files in this directory are routing aids:

- `rules/` contains short reminders for recurring constraints.
- `commands/` contains reusable task recipes.
- `roles/` contains role cards mapped to the existing Sales Codex role model.
- `workflows/` contains workflow entrypoints that point back to established repository processes.

If a file in this directory conflicts with a repository authority file, the authority file wins.

---

## Authority Stack

1. `AGENTS.md`
2. `PROJECT_BOOTSTRAP.md`
3. `SESSION_BRIEF.md`
4. `00_project/NEXT_ACTION.md`
5. `TASK_TYPES.md`
6. Task-specific framework, governance, template, or project files
7. `.agents/*` helper files

---

## Agent Usage

All agents should treat `.agents/` as the shared helper layer:

- Codex: use `.agents/` first; `.codex/` is only a compatibility pointer.
- Claude / Cowork: use `.agents/` after `AGENTS.md` and the standard Sales Codex startup files.
- ChatGPT, Gemini, Perplexity, or other agents: use `.agents/` only as routing support, never as a replacement for repository authorities.

---

## Local Overrides

Do not commit personal overrides unless Felix explicitly decides otherwise.

Recommended local-only patterns:

- `.agents/*.local.json`
- `.agents/*.local.md`
- `.agents/local/`

---

## Non-Goals

- No new knowledge objects.
- No hidden source usage.
- No framework changes by implication.
- No automatic replacement of `TASK_TYPES.md`.
- No broad repository scans unless the active task type permits them.

