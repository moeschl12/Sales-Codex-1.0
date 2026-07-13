# Sales Codex Codex Compatibility Pointer

Status: compatibility pointer
Authority: `.agents/README.md`

---

## Purpose

The shared agent control plane lives in `.agents/`, not `.codex/`.

Codex should read:

- `AGENTS.md`
- `PROJECT_BOOTSTRAP.md`
- `SESSION_BRIEF.md`
- `00_project/NEXT_ACTION.md`
- `.agents/README.md`

This file exists only so Codex-specific tooling can discover the shared `.agents/` layer.

Do not maintain separate Codex-only rules here.

