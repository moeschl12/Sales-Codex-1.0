# Session Brief

*Kompakter Sessionstart — Ersatz für die vollständige `CURRENT_STATE.md` im Regelfall. Kein Ersatz für `PROJECT_BOOTSTRAP.md`. Keine Historie hier — siehe `CURRENT_STATE.md` / `00_project/SESSION_LOG.md`. Wird bei jedem Sprintabschluss ersetzt, nicht ergänzt.*

---

## Aktueller Status (Stand: 2026-07-06)

Sales Codex Version 1.0 ist offiziell veröffentlicht und bleibt unveränderlich. Version 1.1 wurde durch Herausgeberentscheidung als autonomes Makroprojekt-Programm eröffnet.

**Drei Makroprojekte abgeschlossen und unabhängig auditiert:**

- V11-01 — Baseline & Control Plane Consolidation: Git-/Atlas-/Evidence-Check-/W-002-004-Status vollständig erfasst. Audit: **PASS WITH CONDITIONS**; Commit/Push durchgeführt, Bedingung erfüllt, Git-Hard-Block (`index.lock`) aufgelöst.
- V11-02 — Evidence Architecture Resolution: alle 7 Befunde des Compact Evidence Architecture Check disponiert, `SCIENTIFIC_DEBT.md` präzisiert, kein W-005, 3-Punkte-Evidence-Backlog. Audit: **PASS** (`00_project/projects/V11-02_evidence_architecture_resolution/AUDIT_REPORT.md`).
- V11-03 — Governance + Repository Integrity + Atlas Operationalization: OD-006/007/009–012 mit explizitem DoD-Status versehen (2× Deferred, 4× Needs Editor Decision); `KNOWLEDGE_ATLAS_GOVERNANCE.md` um Research-Program-Integration-Trigger und einen real gemessenen zweiten KPI-Zyklus ergänzt. Audit: **PASS WITH CONDITIONS** (`00_project/projects/V11-03_governance_integrity_atlas/AUDIT_REPORT.md`) — Bedingung (Statuskonsistenz `CURRENT_STATE.md` bereinigen, Closure dokumentieren) durch den Closure Fix vom 2026-07-06 erfüllt, **Bedingung geschlossen**.

Cross-Project Consistency (gebündelter Audit V11-02/V11-03): **CONSISTENT WITH MINOR DRIFT** — die Drift (veraltete Statusaussagen in `CURRENT_STATE.md`) ist mit diesem Closure Fix behoben. Details: `00_project/CLOSURE_REPORT_V11-02_V11-03_2026-07-06.md`.

Nächster Schritt: **V11-04 — Early Delivery Vertical Slice** — bereit, in keiner Session bisher gestartet.

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
