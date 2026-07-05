# Next Action

*Genau eine nächste Aktion. Kein Backlog. Kein Mehrfach-Eintrag. Diese Datei wird bei jedem Sprintabschluss ersetzt, nicht ergänzt — vollständige Historie ausschließlich in `00_project/SESSION_LOG.md`.*

---

## Aktuelle Aktion (Stand: 2026-07-04)

Sales Codex Version 1.0 ist offiziell veröffentlicht und gilt als unveränderlich (`CURRENT_STATE.md`, `99_archive/v1.0_release/VERSION_1_0_CLOSING_REPORT.md`). Es gibt keine offene Aktion für Version 1.0. Version 1.1 wurde noch nicht begonnen.

**Nächste Aktion:** Entscheidung des Herausgebers, wann und mit welchem Auftrag ein Version-1.1-Programm eröffnet wird. Bekannte, an Version 1.1 übergebene Restpunkte: OD-006/007-Implementierung, OD-008–012, Statement-Evidenzfeld-Lücke, Terminologie-Nachziehung, SRC-0010-Ordnerplatzierung, Git-Index-Reparatur, Academic Recovery Plan Tier 1 (siehe `99_archive/v1.0_release/SALES_CODEX_VERSION_1_0_RELEASE.md`, Abschnitt „Ausblick auf Version 1.1", sowie `00_project/OPEN_DECISIONS.md`).

## Arbeitsmodus

Kein aktiver Entwicklungssprint. Bis ein Version-1.1-Programm formal durch den Herausgeber eröffnet wird, arbeitet jede Session ohne gegenteiligen expliziten Auftrag ausschließlich lesend/vorbereitend, nicht verändernd.

## Erlaubte Dateien

Ohne expliziten Herausgeberauftrag: nur lesender Zugriff auf `CURRENT_STATE.md`, `00_project/OPEN_DECISIONS.md`, `99_archive/v1.0_release/SALES_CODEX_VERSION_1_0_RELEASE.md` (Abschnitt „Ausblick auf Version 1.1") zur Vorbereitung einer Herausgeberentscheidung.

## Verbotene Dateien / Aktionen

Bis zur formalen Eröffnung eines Version-1.1-Programms: keine Änderungen an Version-1.0-Inhalten (Wissensobjekte, Quellen, Framework, Canonical Knowledge Model, abgeschlossene Forschungsprojekte, Editor Decisions), keine neuen Wissensobjekte, keine neue Forschung, keine Repository-Umstrukturierung. Grundlage: Unveränderlichkeitserklärung in `CURRENT_STATE.md` und `99_archive/v1.0_release/RC1_FREEZE_DECLARATION.md`.

## Abbruchbedingungen

Nur anhalten wenn:
- Primärquelle fehlt oder nicht zugänglich
- Repository-Dateien beschädigt
- Canonicalisierungsentscheidung eindeutig nicht möglich
- Framework-Widerspruch blockiert produktives Weiterarbeiten
- Herausgeberentscheidung zwingend erforderlich

Normale Unsicherheit → ⚠ dokumentieren, weiterarbeiten.

---

## Pflichtabschluss jeder Session

1. `CURRENT_STATE.md` aktualisieren
2. `00_project/NEXT_ACTION.md` **ersetzen** (nicht anhängen) — genau eine aktuelle Aktion
3. `00_project/SESSION_LOG.md` Eintrag ergänzen

---

*Hinweis (2026-07-05): Frühere, gestapelte Sprint-Zwischenstände dieser Datei wurden im Rahmen des Cowork Token Optimization Sprint 1 entfernt. Jeder entfernte Stand ist bereits vollständig und inhaltsgleich in `00_project/SESSION_LOG.md` dokumentiert (per Abgleich verifiziert, keine Information ging verloren). Details: `00_project/COWORK_TOKEN_OPTIMIZATION_SPRINT_1_REPORT.md`.*
