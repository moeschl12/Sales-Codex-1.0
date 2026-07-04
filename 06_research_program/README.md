# Sales Codex Research Program

Version: RC-1
Stand: 2026-07-03

---

## Grundregel

Forschung ist strikt vom offiziellen Sales Codex getrennt. Kein Inhalt aus diesem Ordner gilt als Bestandteil des Codex, solange keine positive Editor Decision vorliegt und die Repository Integration nicht abgeschlossen ist (siehe `DECISION_POLICY.md`, `REPOSITORY_INTEGRATION.md`).

## Zweck

Das Research Program ist der Prozess, mit dem der Sales Codex offene, benannte Forschungsfragen bearbeitet, die sich nicht allein durch die Standard-Buchanalyse klären lassen — insbesondere Widersprüche zwischen bereits verarbeiteten Quellen (Beispiel: W-001, siehe unten). Details zu Zweck und Geltungsbereich: `RESEARCH_GOVERNANCE.md`, Abschnitt 1–2.

## Wie dieser Ordner aufgebaut ist

| Datei / Ordner | Zweck |
|---|---|
| `README.md` | Dieses Dokument — Einstiegspunkt und Wegweiser |
| `RESEARCH_GOVERNANCE.md` | Ziel, Geltungsbereich, Rollen, Verantwortlichkeiten, Statusdefinitionen, Ordnerübergänge, Abbruch- und Abschlusskriterien |
| `DECISION_POLICY.md` | Entscheidungskriterien für die Editor Decision (Stufe 7) |
| `RESEARCH_STATUS.md` | Tabellarischer Status aller aktiven, abgeschlossenen und archivierten Projekte |
| `RESEARCH_LIFECYCLE.md` | Der vollständige neunstufige Forschungsprozess: Ziel, Eingaben, Ergebnisse, Qualitätskriterien, Übergabekriterien und Rolle je Stufe |
| `REPOSITORY_INTEGRATION.md` | Wie ein angenommenes Forschungsergebnis konkret zu einem Wissensobjekt im Sales Codex wird |
| `templates/` | Vorlagen für jede Stufe und jedes projektbegleitende Dokument |
| `active/` | Laufende Forschungsprojekte |
| `completed/` | Abgeschlossene, integrierte Forschungsprojekte (Health Check bestanden) |
| `archived/` | Eingestellte oder abgelehnte Forschungsprojekte |

## Einstieg für neue Mitarbeitende (Mensch oder KI)

Wer neu an einem Forschungsprojekt arbeitet, liest in dieser Reihenfolge:

1. Dieses `README.md`
2. `RESEARCH_GOVERNANCE.md` (Rollen und Grundregeln)
3. `RESEARCH_LIFECYCLE.md` (der konkrete Prozess)
4. Das `README.md` des jeweiligen Projekts in `active/W-XXX/` (die konkrete Forschungsfrage)

## Laufende Projekte

Aktueller Stand: `RESEARCH_STATUS.md`.

**W-001 — Teach First vs. Diagnose First:** Untersucht den seit Sprint 1 dokumentierten Widerspruch zwischen diagnostischen Vertriebsmodellen (SPIN Selling, Gap Selling) und belehrenden Ansätzen (The Challenger Sale) — siehe `active/W001/README.md` für die vollständige Einordnung der Forschungsfrage.

## Was dieser Ordner nicht regelt

- Die Standard-Buchanalyse (`04_book_analysis/`, geregelt durch `00_project/SALES_CODEX_OPERATING_MANUAL.md`)
- Synthese-Sprints (`04_synthesis/`)
- Die Identitäts- und Integrationsregeln für Wissensobjekte selbst (`01_framework/05_knowledge_model/canonical_knowledge_model.md`) — das Research Program entscheidet nur, *ob* ein Ergebnis dieser Logik zugeführt wird, nicht *wie* die Logik selbst funktioniert

---

*Dieses Dokument gilt ab RC-1 (2026-07-03). Änderungen nur durch Felix.*
