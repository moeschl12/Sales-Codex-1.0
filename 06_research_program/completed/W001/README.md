# W-001 — Teach First vs. Diagnose First

Version: RC-1 (abgeschlossen)
Stand: 2026-07-03 (Research Project W-001 Repository Integration Sprint — Post Editor Decision)

---

## Projekt-ID

W-001

## Research Question (retroactiv formuliert)

**Sollte ein B2B-Vertriebsansatz primär diagnostisch (Bedarfsanalyse zuerst — z. B. SPIN Selling, Gap Selling) oder primär belehrend (Commercial Teaching zuerst — z. B. The Challenger Sale) vorgehen, und lässt sich dieser scheinbare methodische Widerspruch theoretisch auflösen?**

Dieser Widerspruch ("Teach First vs. Diagnose First") ist seit dem ersten Synthese-Sprint (SPR-0001) als zentraler, ungelöster methodischer Kernwiderspruch des Sales Codex dokumentiert — u. a. in `04_synthesis/SPR-0001_Sales_Core_Synthesis/` (`contradiction_matrix.md`, dort als "W-001 UNGELÖST" geführt), `00_project/CURRENT_STATE.md` und `00_project/OPEN_DECISIONS.md` (OD-009). Eine repositoryweite Suche findet über 50 Dateien außerhalb dieses Ordners, die W-001 in diesem Sinne erwähnen (siehe `RESEARCH_PROGRAM_REVIEW_RC1.md`, Kapitel 1, "Verständlichkeit").

**Hinweis zur Nachträglichkeit dieser Formulierung:** Zum Zeitpunkt der Anlage von W-001 existierte in `06_research_program/` noch keine formale Stufe "Research Question" mit eigener Datei (`00_RESEARCH_QUESTION.md`) — diese Stufe wurde erst mit `RESEARCH_LIFECYCLE.md` (RC-1, 2026-07-03) eingeführt. Gemäß Sprintauftrag ("Research Program Finalization Sprint", Phase 7: "Nicht versuchen, W-001 wissenschaftlich weiterzuführen") wird für W-001 **keine** neue `00_RESEARCH_QUESTION.md`-Datei rückwirkend angelegt. Die obige Formulierung dient ausschließlich dazu, diesen Ordner ohne externen Kontext verständlich zu machen (Empfehlung 5 aus `RESEARCH_PROGRAM_REVIEW_RC1.md`, Executive Summary) — sie ist eine Zusammenfassung bereits bestehender Repository-Inhalte, keine neue Forschungsleistung.

## Anlass

Zwei bereits im Sales Codex verarbeitete Buchanalysen (SPIN Selling / Gap Selling einerseits, The Challenger Sale andererseits) vertreten empirisch gestützte, aber einander widersprechende Kernaussagen darüber, ob Diagnose oder Belehrung am Anfang eines Vertriebsgesprächs stehen sollte. Der Widerspruch blieb nach Abschluss der jeweiligen Buchanalysen ungelöst und wurde deshalb dem Research Program zur systematischen Klärung übergeben.

## Status

`COMPLETED` — Statuswert gemäß `../../RESEARCH_GOVERNANCE.md`, Abschnitt 5. Editor Decision getroffen (2026-07-03, "Teilweise annehmen"), Repository Integration abgeschlossen, Abschluss-Health-Check bestanden. Projektordner nach `completed/` verschoben (`RESEARCH_GOVERNANCE.md`, Abschnitt 6.2). `../../RESEARCH_STATUS.md` wurde entsprechend aktualisiert (Zeile in die `completed/`-Tabelle verschoben) — die zuvor dokumentierte Synchronisationslücke ist behoben.

Alle neun Stufen sind bearbeitet, mit einer dauerhaft dokumentierten Ausnahme: Stufen 1–2 (Research Question als eigene Datei; Initial Hypothesis) bleiben als historische Alt-Lücke bestehen (siehe Abschnitt "Projektdateien" unten sowie `HEALTH_CHECK.md`, Abschnitt "Abschluss-Health-Check").

## Ergebnis (final)

Master Review (Stufe 3) und Peer Review (Stufe 4) erreichten **entgegengesetzte fachliche Schlussfolgerungen** zum Socio-Cognitive Sensegiving Model (SCSM). Die Theory Landscape (Stufe 5, `04_THEORY_LANDSCAPE.md`) präzisierte diesen Streitpunkt: Er betraf ausschließlich die mathematische Formalisierung des SCSM, nicht die vier geprüften Basishypothesen (CEAM, MDM, CQM, SMM) und nicht die von beiden Reviews unwidersprochene empirische Sensemaking-Kernbeobachtung.

**Die Editor Decision (Stufe 7, 2026-07-03, `06_EDITOR_DECISION.md`) lautet: Teilweise annehmen.** Die mathematische Formalisierung des SCSM wird nicht in den Sales Codex übernommen (Red-Team-Kritik wird gefolgt). Übernommen wird der Kernbefund, dass diagnose- und teaching-/sensemaking-orientierte Vertriebsansätze nicht in universellem Widerspruch stehen, sondern kontextabhängig koexistierende Wirkmechanismen beschreiben. Repository Integration (Stufe 8): sechs bestehende Wissensobjekte erweitert (A-0020, P-0021, P-0025, MEC-0013, T-0019, T-0023), keine Neuanlage, kein MOD, keine Differentialgleichung. Details: `OPEN_QUESTIONS.md`, `06_EDITOR_DECISION.md`, `REPOSITORY_INTEGRATION_LOG.md`, `W001_REPOSITORY_INTEGRATION_REPORT.md`.

## Beteiligte Rollen

| Stufe | Rolle | Wahrgenommen durch |
|---|---|---|
| 3 — Master Review | Scientific Reviewer | Nicht dokumentiert (historisch — vor Einführung der Rollenzuordnung in `RESEARCH_GOVERNANCE.md`, Abschnitt 4.3) |
| 4 — Peer Review | Peer / Red Team Reviewer | Gemini (siehe Dateiname `03_GEMINI_RED_TEAM_REVIEW.md`) |

## Projektdateien

| Stufe | Datei | Status |
|---|---|---|
| 1 — Research Question | (keine, siehe oben) | nicht angelegt (legacy, dauerhaft dokumentierte Lücke) |
| 2 — Initial Hypothesis | `01_INITIAL_HYPOTHESIS.md` | Stub (Titelzeile, unverändert seit Projektstart — auch in diesem Sprint nicht bearbeitet, siehe unten) |
| 3 — Master Review | `02_SCIENTIFIC_MASTER_REVIEW.md` | vollständig (330 Zeilen) |
| 4 — Peer Review | `03_GEMINI_RED_TEAM_REVIEW.md` | vollständig (290 Zeilen) |
| 5 — Theory Landscape | `04_THEORY_LANDSCAPE.md` | vollständig (2026-07-03) |
| 6 — Decision Brief | `05_DECISION_BRIEF.md` | vollständig, ohne Empfehlung (2026-07-03) |
| 7 — Editor Decision | `06_EDITOR_DECISION.md` | **Entschieden — Teilweise annehmen (2026-07-03)** |
| 8 — Repository Integration | `REPOSITORY_INTEGRATION_LOG.md` | **durchgeführt (2026-07-03)** — 6 Objekte erweitert, keine Neuanlage |
| 9 — Health Check | `HEALTH_CHECK.md` | Bereitschaftsprüfung (2026-07-03) **und** Abschluss-Health-Check nach Integration (2026-07-03) — beide bestanden |
| begleitend | `OPEN_QUESTIONS.md`, `REFERENCES.md`, `RESEARCH_LOG.md` | aktualisiert (2026-07-03) |
| Abschluss | `W001_COMPLETION_REPORT_RC1.md`, `W001_REPOSITORY_INTEGRATION_REPORT.md` | erstellt (2026-07-03) |

**Unverändert seit Projektbeginn:** `01_INITIAL_HYPOTHESIS.md`, `02_SCIENTIFIC_MASTER_REVIEW.md`, `03_GEMINI_RED_TEAM_REVIEW.md` — der wissenschaftliche Inhalt dieser drei Dateien blieb während des gesamten Prozesses (Theory Landscape bis Repository Integration) unangetastet; nachfolgende Stufen konsolidierten und entschieden auf ihrer Basis, ohne sie zu verändern.

## Verweis

Vollständiger Prozess: `../../RESEARCH_LIFECYCLE.md`. Governance und Rollen: `../../RESEARCH_GOVERNANCE.md`. Entscheidungskriterien für Stufe 7: `../../DECISION_POLICY.md`.
