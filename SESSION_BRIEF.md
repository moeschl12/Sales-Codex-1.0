# Session Brief

*Kompakter Sessionstart — Ersatz für die vollständige `CURRENT_STATE.md` im Regelfall. Kein Ersatz für `PROJECT_BOOTSTRAP.md`. Keine Historie hier — siehe `CURRENT_STATE.md` / `00_project/SESSION_LOG.md`. Wird bei jedem Sprintabschluss ersetzt, nicht ergänzt.*

---

## Aktueller Status (Stand: 2026-07-06)

Sales Codex Version 1.0 ist offiziell veröffentlicht und bleibt unveränderlich. Version 1.1 wurde durch Herausgeberentscheidung als autonomes Makroprojekt-Programm eröffnet.

**Drei Makroprojekte abgeschlossen:**

- V11-01 — Baseline & Control Plane Consolidation: Git-/Atlas-/Evidence-Check-/W-002-004-Status vollständig erfasst. Vor Start von V11-02 unabhängig auditiert — Ergebnis **PASS WITH CONDITIONS**; anschließend Commit und Push durchgeführt, Bedingung erfüllt, der zuvor dokumentierte Git-Hard-Block (`index.lock`) damit aufgelöst.
- V11-02 — Evidence Architecture Resolution (gestartet nach bestandenem V11-01-Audit, auf explizite Herausgeberanweisung): alle 7 Befunde des Compact Evidence Architecture Check disponiert, `SCIENTIFIC_DEBT.md` präzisiert, kein W-005, 3-Punkte-Evidence-Backlog.
- V11-03 — Governance + Repository Integrity + Atlas Operationalization (auf explizite Herausgeberanweisung direkt im Anschluss an V11-02, ohne zwischengeschalteten Audit): OD-006/007/009–012 mit explizitem DoD-Status versehen (2× Deferred, 4× Needs Editor Decision); `KNOWLEDGE_ATLAS_GOVERNANCE.md` um Research-Program-Integration-Trigger und einen real gemessenen zweiten KPI-Zyklus ergänzt; Statusinkonsistenz in `CURRENT_STATE.md` behoben.

**Offener Punkt:** V11-02 und V11-03 haben bislang keinen unabhängigen Audit-Report — gültige Herausgeber-Priorisierung, aber vor dem finalen V1.1-Release-Gate nachzuholen (`V1_1_RELEASE_CRITERIA.md`, Abschnitt 7).

Nächster Schritt: **V11-04 — Early Delivery Vertical Slice** (noch nicht gestartet).

Strategische Source of Truth:

`00_project/ROADMAP_V1_1.md`

Operativer Launcher:

`00_project/NEXT_ACTION.md`

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
