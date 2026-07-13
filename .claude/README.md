# Sales Codex Claude Compatibility Pointer

Status: compatibility pointer
Authority: `.agents/README.md`

---

## Purpose

The shared agent control plane lives in `.agents/`, not `.claude/`.

Claude / Cowork should read:

- `AGENTS.md`
- `PROJECT_BOOTSTRAP.md`
- `SESSION_BRIEF.md`
- `00_project/NEXT_ACTION.md`
- `.agents/README.md`

This file exists only so Claude-specific tooling and future Claude sessions can discover the shared `.agents/` layer.

Do not maintain separate Claude-only rules here.

