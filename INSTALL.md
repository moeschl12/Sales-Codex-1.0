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

Then start any agent with:

1. `PROJECT_BOOTSTRAP.md`
2. `SESSION_BRIEF.md`
3. `00_project/ACTIVE_INDEX.md`
4. `00_project/NEXT_ACTION.md`

The former V11-01 execution prompt remains available as historical material
under `99_archive/00_project_history/` and is not a current launcher.

Do not commit automatically until V11-01 completes or the current dirty state has been reconciled.
