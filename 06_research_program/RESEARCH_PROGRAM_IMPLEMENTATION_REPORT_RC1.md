# Research Program Implementation Report — RC-1

**Dokumentklasse:** Governance / Implementation
**Sprint:** Research Program Finalization Sprint
**Grundlage:** `RESEARCH_PROGRAM_REVIEW_RC1.md` (Architekturprüfung, Stichtag 2026-07-02, Gesamtreifegrad "MAJOR REVISION REQUIRED")
**Datum:** 2026-07-03
**Auftrag:** Das Research Program vollständig, methodisch konsistent und skalierbar ausarbeiten, sodass es als offizielle Forschungsmethodik des Sales Codex dienen kann. Ausschließlich Bearbeitung des Research Programs — keine Änderungen an Wissensobjekten, keine neuen Forschungsprojekte, keine Literaturrecherche, keine Änderungen am Sales-Codex-Inhalt.

---

## 1. Umgesetzte Empfehlungen

Alle sechs priorisierten Empfehlungen aus `RESEARCH_PROGRAM_REVIEW_RC1.md`, Executive Summary, sowie alle acht dort benannten Release-Blocker (Kapitel 8) wurden bearbeitet:

| # | Empfehlung (Review, Executive Summary) | Umsetzung |
|---|---|---|
| 1 | Templates für alle fünf Stufen mit Feldstruktur ausarbeiten; fehlende Templates (Initial Hypothesis, Research/Master Review, Open Questions, References, Research Log) ergänzen | Alle 5 bestehenden Templates vollständig ausgearbeitet; 6 neue Templates ergänzt (siehe Abschnitt 2) |
| 2 | Rollen- und Entscheidungsregelwerk definieren (Rollen, Abbruchbedingungen, Bewertungskriterien, Bezug zum Evidenzsystem) | `RESEARCH_GOVERNANCE.md` Abschnitt 4 (5 Rollen, funktional definiert), Abschnitt 7 (Abbruchbedingungen); `DECISION_POLICY.md` (vollständige Entscheidungskriterien mit Evidenzsystem-Bezug) |
| 3 | Explizite Repository-Integrationsschnittstelle beschreiben | `REPOSITORY_INTEGRATION.md` (neu) — vollständiger Ablauf, Objekttypen, Source-ID-Konvention, Dokumentationspflichten |
| 4 | Health-Check-Stufe definieren, im Zusammenhang mit OD-003 | `RESEARCH_LIFECYCLE.md` Abschnitt 11–12 (Stufe 9) — projektspezifisch, ausdrücklich von OD-003 (repositoryweiter Health Check) abgegrenzt, ohne OD-003 zu schließen |
| 5 | `active/W001/README.md` um Einordnung der Forschungsfrage ergänzen | Erledigt — Research Question retroactiv formuliert, mit Kennzeichnung der Nachträglichkeit |
| 6 | Klärung `RESEARCH_PROJECT_TEMPLATE.md` vs. projektbezogene `README.md` | Erledigt — `RESEARCH_PROJECT_TEMPLATE.md` ist jetzt explizit als Vorlage ausschließlich für die Projekt-`README.md` definiert (Kopfhinweis im Template selbst) |

Alle acht strukturellen Blocker aus Kapitel 8 des Reviews sind adressiert (Details je Blocker in Abschnitt 6 dieses Berichts — dort wird für jeden geprüft, ob er vollständig geschlossen oder nur entschärft ist).

## 2. Neu erstellte Templates

`06_research_program/templates/` enthält jetzt 11 statt 5 Dateien. Alle 11 haben eine Feldstruktur nach dem Qualitätsstandard der Hauptframework-Templates (`01_framework/08_templates/`), keine reine Titelzeile mehr.

| Template | Status |
|---|---|
| `RESEARCH_PROJECT_TEMPLATE.md` | Ausgearbeitet (bestand vorher) |
| `DECISION_BRIEF_TEMPLATE.md` | Ausgearbeitet (bestand vorher) |
| `EDITOR_DECISION_TEMPLATE.md` | Ausgearbeitet (bestand vorher) |
| `RED_TEAM_TEMPLATE.md` | Ausgearbeitet (bestand vorher) |
| `THEORY_LANDSCAPE_TEMPLATE.md` | Ausgearbeitet (bestand vorher) |
| `INITIAL_HYPOTHESIS_TEMPLATE.md` | **Neu** |
| `MASTER_REVIEW_TEMPLATE.md` | **Neu** |
| `OPEN_QUESTIONS_TEMPLATE.md` | **Neu** |
| `REFERENCES_TEMPLATE.md` | **Neu** |
| `RESEARCH_LOG_TEMPLATE.md` | **Neu** |
| `HEALTH_CHECK_TEMPLATE.md` | **Neu** |

Kein Template wurde nach Aufwand geraten — jedes ausgearbeitete oder neue Template ist ausdrücklich aus dem bereits bestehenden, tatsächlichen Muster von `active/W001/02_SCIENTIFIC_MASTER_REVIEW.md` und `active/W001/03_GEMINI_RED_TEAM_REVIEW.md` abgeleitet, wo ein solches Muster existierte (`MASTER_REVIEW_TEMPLATE.md`, `RED_TEAM_TEMPLATE.md`), bzw. am repositoryweiten Vorbild `00_project/SESSION_LOG.md` orientiert (`RESEARCH_LOG_TEMPLATE.md`).

## 3. Ausgearbeitete Governance

| Dokument | Vorher | Nachher |
|---|---|---|
| `README.md` | 3 Zeilen, ein Satz | Zweck, Ordnerübersicht, Einstiegsreihenfolge, laufende Projekte, Abgrenzung |
| `RESEARCH_GOVERNANCE.md` | 4 Zeilen, ein Satz | Zweck, Geltungsbereich, Verhältnis zum Codex, 5 Rollen mit Zuständigkeiten, Statusdefinitionen, Ordnerübergänge (`active`/`completed`/`archived`), Abbruchbedingungen, Abschlusskriterien, Rangfolge gegenüber anderen Governance-Dokumenten |
| `DECISION_POLICY.md` | 4 Zeilen, ein Satz | 4 Entscheidungsoptionen, Kriterienkatalog für positive Entscheidung (identisch zum Hauptcodex-Qualitätsstandard), Umgang mit widersprüchlichen Reviews, Bezug zur Repository Integration, Abbruchbedingungen |
| `RESEARCH_STATUS.md` | 1 Zeile Freitext | Tabellenformat für aktive/abgeschlossene/archivierte Projekte, Stufen-Referenz, Pflegehinweise (skaliert jetzt auf beliebig viele Projekte) |

Zusätzlich zwei komplett neue programmweite Dokumente, die im Auftrag ("mindestens" diese vier Dokumente) nicht explizit als Mindestanforderung genannt, aber durch Phase 3/4 des Sprintauftrags sachlich zwingend erforderlich waren:

- `RESEARCH_LIFECYCLE.md` (224 Zeilen) — der vollständige neunstufige Prozess (Research Question bis Health Check), je Stufe Ziel/Eingaben/Ergebnisse/Qualitätskriterien/Übergabekriterien/Rolle.
- `REPOSITORY_INTEGRATION.md` (89 Zeilen) — Repository-Integrationsmechanik, kompatibel mit, aber ohne Änderung an der Kernlogik des Canonical Knowledge Model.

## 4. Neue Integrationspunkte

### 4.1 Innerhalb von `06_research_program/`

172 interne Backtick-Querverweise über 21 Dateien (Governance-Dokumente, Templates, W-001-Infrastrukturdateien) — gegenüber null internen Querverweisen vor diesem Sprint (`RESEARCH_PROGRAM_REVIEW_RC1.md`, Kapitel 6, "Fehlende Schnittstelle 3"). Jedes Dokument verweist auf die Dokumente, von denen es Eingaben erhält oder an die es Ergebnisse übergibt.

### 4.2 Zum Hauptframework

Drei minimale, punktuelle Ergänzungen an bestehenden Framework-Dokumenten (keine Restrukturierung, keine Änderung bestehender Inhalte):

| Dokument | Ergänzung | Umfang |
|---|---|---|
| `00_project/SALES_CODEX_OPERATING_MANUAL.md` | Neuer Abschnitt 11 "Verhältnis zum Research Program" | 1 Absatz, angehängt nach Abschnitt 10 (Book Mode) |
| `01_framework/05_knowledge_model/canonical_knowledge_model.md` | Neuer Abschnitt 11 "Herkunft aus dem Research Program" | 1 Absatz, angehängt nach Abschnitt 10 — bestehende Abschnittsnummerierung 1–10 bewusst nicht verändert, um in `00_project/BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md` bestehende Zitate von "CKM Abschnitt 10" (Einführung neuer Objekttypen) nicht zu invalidieren |
| `00_project/task_rules.md` | Neuer Unterabschnitt 7.5 "Source-ID bei Herkunft aus dem Research Program" | 1 Unterabschnitt in bestehendem Abschnitt 7 |

Damit ist die in Kapitel 6 des Reviews dokumentierte "Fehlende Schnittstelle 1" (kein Framework-Dokument erwähnte das Research Program) geschlossen — mit dem geringstmöglichen Eingriff, der zur Integration notwendig war.

### 4.3 Source-ID-Konvention

Neue, additive Konvention für Wissensobjekte mit Research-Program-Ursprung: `## Source ID` trägt die Projekt-ID (`W-XXX (Research Program)`) statt einer `SRC-ID`. Definiert in `task_rules.md` 7.5, referenziert in `canonical_knowledge_model.md` 11 und `REPOSITORY_INTEGRATION.md` Abschnitt 3.

## 5. Geänderte Dateien

### 5.1 Neu erstellt (13)

`06_research_program/RESEARCH_LIFECYCLE.md`, `06_research_program/REPOSITORY_INTEGRATION.md`, `06_research_program/templates/INITIAL_HYPOTHESIS_TEMPLATE.md`, `06_research_program/templates/MASTER_REVIEW_TEMPLATE.md`, `06_research_program/templates/OPEN_QUESTIONS_TEMPLATE.md`, `06_research_program/templates/REFERENCES_TEMPLATE.md`, `06_research_program/templates/RESEARCH_LOG_TEMPLATE.md`, `06_research_program/templates/HEALTH_CHECK_TEMPLATE.md`, sowie dieser Bericht selbst.

### 5.2 Vollständig ausgearbeitet (bestand vorher nur als Titelzeile) (9)

`06_research_program/README.md`, `RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md`, `RESEARCH_STATUS.md`, `templates/RESEARCH_PROJECT_TEMPLATE.md`, `templates/DECISION_BRIEF_TEMPLATE.md`, `templates/EDITOR_DECISION_TEMPLATE.md`, `templates/RED_TEAM_TEMPLATE.md`, `templates/THEORY_LANDSCAPE_TEMPLATE.md`.

### 5.3 W-001-Infrastruktur ausgearbeitet (4)

`active/W001/README.md`, `active/W001/OPEN_QUESTIONS.md` (5 extrahierte offene Fragen, OQ-1 bis OQ-5), `active/W001/REFERENCES.md` (119 konsolidierte, deduplizierte Quellen aus den beiden bestehenden Reviews), `active/W001/RESEARCH_LOG.md` (rekonstruiertes chronologisches Protokoll, Rekonstruktion ausdrücklich gekennzeichnet).

### 5.4 Punktuell ergänzt, außerhalb von `06_research_program/` (3)

`00_project/SALES_CODEX_OPERATING_MANUAL.md`, `01_framework/05_knowledge_model/canonical_knowledge_model.md`, `00_project/task_rules.md` (jeweils ein neuer, angehängter Abschnitt/Unterabschnitt — siehe Abschnitt 4.2).

### 5.5 Ausdrücklich unverändert

`active/W001/01_INITIAL_HYPOTHESIS.md`, `02_SCIENTIFIC_MASTER_REVIEW.md`, `03_GEMINI_RED_TEAM_REVIEW.md`, `04_THEORY_LANDSCAPE.md`, `05_DECISION_BRIEF.md`, `06_EDITOR_DECISION.md` (Sprintauftrag Phase 7); `00_project/OPEN_DECISIONS.md`, `00_project/SCIENTIFIC_DEBT.md`, `01_framework/05_knowledge_model/canonical_knowledge_model.md` Abschnitte 1–10 (Kerninhalt), `00_project/SALES_CODEX_OPERATING_MANUAL.md` Abschnitt 10 (Book Mode) — keine dieser Dateien/Abschnitte wurde inhaltlich angetastet, nur ergänzt.

## 6. Verbleibende RC-1-Blocker

Ehrliche Einschätzung, welche der acht Blocker aus `RESEARCH_PROGRAM_REVIEW_RC1.md` Kapitel 8 durch diesen Sprint vollständig geschlossen sind und welche — ihrer Natur nach — nicht durch Dokumentation allein abschließend geschlossen werden können:

| # | Blocker (Review) | Status nach diesem Sprint |
|---|---|---|
| 1 | Templates ohne Feldstruktur | Geschlossen. Alle 11 Templates haben Feldstruktur. |
| 2 | Fehlende Templates für zentrale Stufen | Geschlossen. 6 neue Templates ergänzt. |
| 3 | Fehlendes Rollen-/Entscheidungsregelwerk | Geschlossen. `RESEARCH_GOVERNANCE.md` Abschnitt 4, `DECISION_POLICY.md`. |
| 4 | Fehlende Repository-Integrationsschnittstelle | Geschlossen. `REPOSITORY_INTEGRATION.md`. |
| 5 | Fehlende Health-Check-Stufe | Geschlossen für die Projektebene. Die *repositoryweite* Health-Check-Frage (OD-003) bleibt — wie im Sprintauftrag vorgesehen — bewusst unangetastet offen; beide Ebenen sind jetzt aber explizit voneinander abgegrenzt dokumentiert, statt vermischt zu werden. |
| 6 | Entkopplung von der Framework-Ebene | Geschlossen. Drei punktuelle Verweise in Operating Manual, CKM, Task Rules. |
| 7 | Fehlende interne Verlinkung | Geschlossen. 172 interne Querverweise. |
| 8 | Prozessreihenfolge-Unklarheit (Theory Assessment vs. Research) | Geschlossen durch explizite Governance-Entscheidung: Theory Landscape bleibt Stufe 5 (nach Master Review und Peer Review), mit dokumentierter Begründung (`RESEARCH_LIFECYCLE.md` Abschnitt 7, "Abgrenzung"). Dies bestätigt rückblickend die bereits in W-001 gelebte Reihenfolge, statt sie zu verwerfen. |

**Was durch diesen Sprint bewusst nicht geschlossen wurde (kein Blocker im Sinne des Reviews, sondern außerhalb des Auftrags):**

- **W-001 selbst bleibt wissenschaftlich ungelöst** (Stufe 5, Theory Landscape, weiterhin Stub). Dies ist laut Sprintauftrag ausdrücklich nicht Gegenstand dieses Sprints ("Nicht versuchen, W-001 wissenschaftlich weiterzuführen").
- **OD-003** (repositoryweiter Health Check) bleibt unverändert offen — wie oben unter Blocker 5 begründet.
- **Unbewiesene Praxistauglichkeit:** Der neunstufige Lifecycle, alle 11 Templates und die Repository-Integrationslogik sind bislang nur an einem historischen, nicht rückwirkend angepassten Projekt (W-001) gespiegelt, aber noch von keinem künftigen Projekt vollständig durchlaufen worden. Erst ein zweites, unter RC-1 neu gestartetes Projekt wird zeigen, ob die neun Stufen in der Praxis reibungslos funktionieren oder Nacharbeit brauchen.
- **Rollentrennung (Stufe 3/4) ist eine Prozessnorm, kein technischer Zwang:** Die Unabhängigkeitsanforderung zwischen Scientific Reviewer und Peer Reviewer (`RESEARCH_GOVERNANCE.md` 4.4) wird durch keinen technischen Mechanismus erzwungen, sondern muss von den Beteiligten eingehalten werden — wie die meisten Prozessregeln im übrigen Repository auch (z. B. die Abbruchbedingungen des Operating Manual).

## 7. Einschätzung

**Ready after Minor Revision.**

**Begründung:** Alle acht in `RESEARCH_PROGRAM_REVIEW_RC1.md` benannten strukturellen Blocker sind bearbeitet; sechs sind im engeren Sinne vollständig geschlossen (Templates, Rollen, Repository-Integration, Framework-Anbindung, interne Verlinkung, Prozessreihenfolge), einer ist bewusst und begründet nur auf Projektebene geschlossen, während die repositoryweite Parallelfrage (OD-003) unverändert offen bleibt — dies ist keine Lücke dieses Sprints, sondern eine bereits im Repository dokumentierte, andernorts zu klärende Entscheidung. Der Grund, warum dies nicht "Ready" ohne Einschränkung ist: Die neue Governance-Architektur ist vollständig beschrieben und intern konsistent, aber noch durch kein einziges unter RC-1 neu gestartetes Forschungsprojekt praktisch erprobt — die einzige Bewährungsprobe (W-001) ist ein historischer Altfall, der die neuen Stufen 1, 8 und 9 (Research Question, Repository Integration, Health Check) nie durchlaufen hat und laut Sprintauftrag auch nicht rückwirkend dazu gebracht werden soll. Diese Einschätzung ist damit vorsichtiger als eine reine Dokumentenprüfung nahelegen würde — Vollständigkeit der Beschreibung ist nachgewiesen, Praxistauglichkeit ist plausibel, aber noch nicht empirisch bestätigt.

**Empfohlener nächster Schritt (zur Herausgeber-Entscheidung, nicht umgesetzt):** Ein neues, unter RC-1 gestartetes Forschungsprojekt (W-002) vollständig durch alle neun Stufen laufen zu lassen, bevor das Research Program als endgültig eingeschwungen gilt — dies wäre der Härtetest, den eine reine Dokumentenüberarbeitung wie dieser Sprint naturgemäß nicht selbst liefern kann.

---

*Dieser Bericht schließt den Research Program Finalization Sprint ab. Alle in Abschnitt 5 genannten Änderungen wurden ausschließlich innerhalb der bestehenden Repository-Struktur vorgenommen — keine neuen Top-Level-Ordner, keine Änderung der Ordnernummerierung, keine Wissensobjekte, keine Literaturrecherche.*
