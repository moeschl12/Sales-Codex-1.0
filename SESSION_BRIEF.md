# Session Brief

*Kompakter Sessionstart — Ersatz für die vollständige `CURRENT_STATE.md` im Regelfall. Kein Ersatz für `PROJECT_BOOTSTRAP.md`. Keine Historie hier — siehe `CURRENT_STATE.md` / `00_project/SESSION_LOG.md`. Wird bei jedem Sprintabschluss ersetzt, nicht ergänzt.*

---

## Aktueller Status (Stand: 2026-07-06)

Sales Codex Version 1.0 ist offiziell veröffentlicht und bleibt unveränderlich. Version 1.1 wurde durch Herausgeberentscheidung als autonomes Makroprojekt-Programm eröffnet.

**V11-01 — Baseline & Control Plane Consolidation ist aus Executor-Sicht abgeschlossen (COMPLETED — Audit ausstehend).** Vollständiger Befund: `00_project/projects/V11-01_baseline_control_plane/COMPLETION_REPORT.md`. Ein dokumentierter, nicht-inhaltlicher Hard Block (Git-`index.lock` auf dem Dateisystem-Mount lässt sich nicht entfernen, blockiert Commit/Clean-Working-Tree) — Details im Completion Report, Abschnitt 5. Inhaltlich ist der Repository-Zustand konsistent: Git-Status, Atlas-Compiler-Lauf (515 Nodes, 2111 Edges, 0 Duplicate IDs, deterministisch), Compact Evidence Architecture Check und W-002/W-003/W-004-Konsistenz sind vollständig erfasst und dokumentiert.

Nächster Schritt: unabhängiger Audit von V11-01 (siehe `00_project/NEXT_ACTION.md`), danach V11-02.

Strategische Source of Truth:

`00_project/ROADMAP_V1_1.md`

Operativer Launcher:

`00_project/NEXT_ACTION.md`

Nächstes Makroprojekt (nach Audit):

**V11-02 — Evidence Architecture Resolution**

`00_project/projects/V11-02_evidence_architecture_resolution/PROJECT_BRIEF.md`

## Aktuelle Arbeitsregel

Große autonome Arbeitspakete bleiben Standard. Der Agent arbeitet innerhalb des aktiven Projektbriefs autonom und unterbricht nur bei:

- Hard Block,
- Reserved Decision,
- Irreversible High-Impact Change.

Interne Checkpoints sind verpflichtend, aber still. Keine Rückfragen bei normaler Unsicherheit.

## Standard-Laderegel

1. `PROJECT_BOOTSTRAP.md` — kanonischer Einstiegspunkt.
2. Dieses Dokument.
3. `00_project/NEXT_ACTION.md`.
4. Für V1.1-Arbeit zusätzlich `00_project/ROADMAP_V1_1.md`, `00_project/V1_1_AUTONOMY_AND_AUDIT_POLICY.md`, `00_project/V1_1_RELEASE_CRITERIA.md` und den aktiven `PROJECT_BRIEF.md`.
5. Danach ausschließlich aufgabenspezifische Dateien. Kein rekursiver Scan über `00_project/` oder `03_knowledge_base/` ohne explizite Freigabe im Auftrag oder Projektbrief.

## Verweis

Vollständiger Einstiegspunkt, Wissenspipeline, Arbeitsprinzipien und Abbruchbedingungen: `PROJECT_BOOTSTRAP.md`. Task-Typ-Routing: `TASK_TYPES.md`.
