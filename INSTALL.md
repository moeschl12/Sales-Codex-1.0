# Sales Codex V1.1 Control Plane Patch — Install

Copy the contents of this ZIP into the root of `sales-codex-workspace-v1.0`, preserving paths.

Recommended local sequence:

```bash
# from repository root
git status
# unpack/copy patch files into repository
git diff -- PROJECT_BOOTSTRAP.md SESSION_BRIEF.md CURRENT_STATE.md 00_project/NEXT_ACTION.md 00_project/ROADMAP_V1_1.md
python3 08_knowledge_atlas/scripts/compile_atlas.py
git status
```

Then start Claude/Clerk with:

`00_project/V11_01_CLAUDE_EXECUTION_PROMPT.md`

Do not commit automatically until V11-01 completes or the current dirty state has been reconciled.
