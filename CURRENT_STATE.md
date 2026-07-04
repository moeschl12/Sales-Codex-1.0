# Current State

Stand: 2026-07-04  
Workspace-Version (Framework): **1.1** (freigegeben 2026-06-30)  
Sales-Codex-Version (Gesamtinhalt/Governance): **1.0 — OFFIZIELL VERÖFFENTLICHT am 2026-07-04**, siehe `00_project/SALES_CODEX_VERSION_1_0_RELEASE.md` und `00_project/VERSION_1_0_CLOSING_REPORT.md`. Die Entwicklungsphase von Version 1.0 ist damit abgeschlossen. **Version 1.1 wurde noch NICHT begonnen.** Vorgeschichte: Programm zur Erreichung von Version 1.0 aktiv seit 2026-07-02, siehe `00_project/SALES_CODEX_1_0_PROGRAM.md`; Phase "Scientific Completion" — Behavioral Science Expansion Sprint 1 (5/5 Bücher) am 2026-07-02 abgeschlossen; Behavioral Science Review Sprint (externes Gutachten + Editor Decision + Umsetzung) am 2026-07-02 abgeschlossen; Research Program Finalization Sprint (RC-1) am 2026-07-03 abgeschlossen; Research Project W-001 Repository Integration Sprint (Post Editor Decision) am 2026-07-03 abgeschlossen; Sales Codex 1.0 Final Pre-Release Sprint am 2026-07-03 abgeschlossen (READY FOR RC-1 AUDIT); External Audit Resolution Sprint am 2026-07-04 abgeschlossen (READY FOR FINAL RC-1 AUDIT); Sales Codex Version 1.0 RC-1 Release Candidate Freeze am 2026-07-04 abgeschlossen (READY FOR FINAL RC-1 AUDIT); **Repository Closing & Release Sprint am 2026-07-04 abgeschlossen — Finaler RC-1-Audit (drei externe Gutachten) validiert, formale Herausgeber-Freigabe vollzogen, Version 1.0 veröffentlicht, siehe unten**  
Architektur: Stateless Agent Architecture (seit 2026-06-30)

---

## Projektstand

### Sales Codex Version 1.0 — Repository Closing & Release Sprint — ABGESCHLOSSEN

**Stand: 2026-07-04**

Auslöser: Herausgeberauftrag „Sales Codex Version 1.0 Repository Closing & Release Sprint" — letzter Sprint für Version 1.0. Der Herausgeber stellte drei externe Gutachten zu ("Wissenschaftliche Prüfung des Sales Codex", "Wissenschaftliche Begutachtung des Behavioral Science Sprints", "Sales Codex Release Audit" / Final RC-1 Release Audit) als letzte externe Bewertungen von Version 1.0. Rolle: Editor-in-Chief / Release Manager / Repository Curator — ausdrücklich nicht als Forscher, Autor, Reviewer oder Framework-Architekt. Auftrag: den finalen Zustand wissenschaftlich dokumentieren, das Repository formal abschließen und Version 1.0 offiziell veröffentlichen. Entwicklungsmodus beendet — Zweck ist nicht mehr Weiterentwicklung.

**Phase 1 (Abschlussvalidierung):** Alle 19 Einzelkritikpunkte der drei Gutachten einzeln gegen den tatsächlichen Repository-Zustand geprüft — keine Empfehlung ungeprüft übernommen, keine ignoriert. Ergebnis: `00_project/FINAL_RC1_AUDIT_VALIDATION_REPORT.md`. 14 Punkte BEHOBEN, 1 TEILWEISE BEHOBEN (Statement-Evidenzfelder), 2 WEITERHIN GÜLTIG als nicht-blockierende, bereits dokumentierte Open-Decision-/Scientific-Debt-Punkte, 1 DURCH EDITOR DECISION ABGELEHNT (MOD-0011/0012-Reklassifizierung, ED-008 bestätigt), 1 NICHT REPRODUZIERBAR (Git-Index-Fehler). Die ursprünglich als RELEASE BLOCKER eingestuften Punkte (SRC-0010 angeblich fehlend; Publication-Bias-Warnungen) erwiesen sich als sachlich unzutreffend bzw. vollständig bereits adressiert.

**Phase 2 (Repository Closing):** Abschließender Status über 14 Dimensionen (Konsistenz, Governance, Research Program, Evidence System, Scientific Debt, Open Decisions, Canonical Knowledge Model, Repositorystruktur, Release-Dokumente, Cross References, tote Links, Quellen, Wissensobjekte, Versionierung) erstellt: `00_project/REPOSITORY_CLOSING_STATUS.md`. Ergebnis: **kein echter, unadressierter Release Blocker vorhanden.**

**Phase 3 (Final Editor Assessment):** Wissenschaftliche und editorische Gesamtbewertung erstellt: `00_project/FINAL_EDITOR_ASSESSMENT_V1_0.md` — wesentliche wissenschaftliche Erkenntnisse (W-001-Kontextauflösung, Behavioral-Science-Fundierung, Ariely-Entkopplung), einflussreichste Architekturentscheidungen (Stateless Agent Architecture, entkoppelte Versionsachsen, Research Program, Canonical Knowledge Model), erfolgreich gelöste Kritikpunkte, bewusst verbliebene Einschränkungen, namentliche Übergabe an Version 1.1.

**Phase 4 (Release Declaration):** `00_project/SALES_CODEX_VERSION_1_0_RELEASE.md` erstellt — offizielle Veröffentlichungserklärung (Executive Summary, Ziel, Umfang, wissenschaftliche Grundlage, Governance, Research Program, Audit-Historie, Veröffentlichungsentscheidung, bekannte Einschränkungen, Ausblick auf Version 1.1).

**Phase 5 (Repository Abschluss):** `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`, `00_project/changelog.md` aktualisiert — Sales-Codex-Gesamtversion jetzt 1.0 (veröffentlicht), Framework-Version unverändert 1.1.

**Abschluss:** `00_project/VERSION_1_0_CLOSING_REPORT.md` erstellt — Executive Summary, Zusammenfassung aller externen Gutachten, Repository-/Governance-/Research-Program-/Scientific-Debt-/Open-Decisions-Endzustand, Releaseentscheidung, Lessons Learned, Empfehlung für Version 1.1. **Einstufung: VERSION 1.0 OFFICIALLY RELEASED.**

**Keine neuen Wissensobjekte, keine neuen Quellen, keine neue Forschung, keine Framework-Änderungen, keine Änderungen am Canonical Knowledge Model, Operating Manual, Research Program oder Research Lifecycle, keine neuen Open Decisions, keine neuen Editor Decisions, keine Repository-Umstrukturierungen, keine Änderungen an abgeschlossenen Forschungsprojekten.**

**Ergebnis: Sales Codex Version 1.0 ist ab 2026-07-04 offiziell veröffentlicht. Die Entwicklungsphase von Version 1.0 ist abgeschlossen. Version 1.1 wurde noch nicht begonnen. Nach Abschluss dieses Sprints gilt Version 1.0 als unveränderlich — jede zukünftige Änderung erfolgt ausschließlich im Rahmen von Version 1.1 und wird nicht rückwirkend eingepflegt. Es dürfen keine weiteren Entwicklungssprints für Version 1.0 mehr eröffnet werden.**

---

### Sales Codex Version 1.0 RC-1 — Release Candidate Freeze — ABGESCHLOSSEN

**Stand: 2026-07-04**

Auslöser: Herausgeberauftrag „Sales Codex Version 1.0 RC-1 Release Candidate Freeze". Rolle: Release Manager / Configuration Manager — ausdrücklich nicht als Forscher, Autor, Reviewer, Editor oder Framework-Architekt. Auftrag: den veröffentlichungsreifen Zustand dokumentieren, keine fachlichen, wissenschaftlichen oder Framework-Änderungen vornehmen.

**Umgesetzt:** Vier neue Release-Dokumente erstellt — `00_project/RELEASE_CANDIDATE_RC1.md` (18 geforderte Freeze-Kennzahlen, unabhängig gegen Dateisystem und `FINAL_PRE_RELEASE_REPORT.md` verifiziert: 514 Wissensobjekte, 15 Quellen, 15 Bücher, 12 Open Decisions, 106 Scientific-Debt-Tabellenzeilen), `00_project/RELEASE_NOTES_v1.0_RC1.md` (Neuerungen, wissenschaftliche Ergebnisse, Architekturentscheidungen, Breaking Changes, Einschränkungen), `00_project/REPOSITORY_MANIFEST_RC1.md` (vollständiger Struktur-Snapshot), `00_project/RC1_FREEZE_DECLARATION.md` (formale Änderungssperre: zulässige/unzulässige Änderungen bis 1.0, Umgang mit 1.1). Release Verification (Phase 4) durchgeführt: Cross-Referenzen, Governance, CKM, Scientific Debt, Evidence System, Open Decisions und Repositorystruktur geprüft — keine sprintrelevanten Inkonsistenzen gefunden, keine bestehende Datei verändert. `00_project/RC1_FREEZE_REPORT.md` erstellt (Executive Summary, Freeze-Arbeiten, Snapshot, Versionsstatus, Restrisiken, Release Readiness, Empfehlung).

**Wichtigste Klarstellung (mit dem Herausgeber während dieses Sprints abgestimmt):** Das Repository definiert einen dreistufigen Prozess — (1) RC-1 Freeze → (2) Finaler RC-1-Audit → (3) formale Herausgeber-Freigabe (`SALES_CODEX_1_0_RELEASE_PLAN.md`, Kapitel 2.2 und 5). Dieser Sprint erledigt ausschließlich Stufe 1. Die Empfehlung lautet daher **READY FOR FINAL RC-1 AUDIT** — ausdrücklich nicht "READY FOR VERSION 1.0 RELEASE", da der Finale RC-1-Audit und die Herausgeber-Freigabe laut `NEXT_ACTION.md` noch ausstehen und durch diesen Freeze nicht ersetzt werden.

**Ergebnis:** Sales Codex Version 1.0 RC-1 gilt ab 2026-07-04 als eingefrorener Release Candidate. Änderungssperre gemäß `RC1_FREEZE_DECLARATION.md` aktiv (keine neuen Wissensobjekte, Quellen, Bücher, Modelle, Mechanismen, Statements, Assumptions, Frameworkänderungen, CKM-/Operating-Manual-/Research-Program-Änderungen, Änderungen an abgeschlossenen Forschungsprojekten oder Editor Decisions, keine neuen Open Decisions, keine neue Forschung, keine Literature Reviews, keine Architektur- oder Repository-Umstrukturierungen).

**Keine neuen Wissensobjekte, keine neue Forschung, keine Framework-Änderungen, keine Änderungen am Canonical Knowledge Model, Operating Manual, Research Program oder an abgeschlossenen Forschungsprojekten/Editor Decisions. Keine bestehende Governance-Datei inhaltlich verändert.**

**Nächster Schritt:** Finaler RC-1-Audit (Herausgeberauftrag ausstehend, `SALES_CODEX_1_0_RELEASE_PLAN.md` Kapitel 5, Schritt 5). Erst danach: formale Herausgeber-Freigabe von Version 1.0 (Schritt 6). Unverändert außerhalb dieses Freeze-Scopes: Herausgeber-Entscheidungsrunde zu OD-008 bis OD-012; Git-Index-Reparatur lokal beim Herausgeber; Fortsetzung Academic Recovery Plan Tier 1.

---

### External Audit Resolution Sprint — ABGESCHLOSSEN

**Stand: 2026-07-04**

Auslöser: Ein externer Audit ("Wissenschaftliche Prüfung des Sales Codex", Framing: Gemini Deep Research) mit 7 Kritikpunkten und Gesamteinschätzung "MAJOR REVISION REQUIRED" wurde zugestellt. Auftrag: jeden Kritikpunkt eigenständig gegen den tatsächlichen Repository-Zustand verifizieren (Grundsatz: "Der Audit ist eine Eingabe, keine Wahrheit"), nur bestätigte oder teilweise bestätigte Befunde umsetzen. Ausdrücklich ausgeschlossen: neue Forschung, neue Wissensobjekte (außer falls SRC-0010 tatsächlich fehlt), neue Governance, Änderungen an CKM/Operating Manual/Research Program/Lifecycle/abgeschlossenen Forschungsprojekten/Editor Decisions.

**Ergebnis je Kritikpunkt:** SRC-0010-Fehlen — nicht bestätigt (Datei existiert vollständig). Publication Bias B-0004/05/06 — teilweise bestätigt (zutreffend für B-0004/B-0006, nicht für B-0005 — andere Evidenzproblematik). OD-006/007-Scheinintegration — bereits behoben (Final Pre-Release Sprint). Peer-Review-Asymmetrie — bewertet, nicht umgesetzt (bereits durch OD-010 abgedeckt). book_catalog.md/REPOSITORY_KPIS.md veraltet — bestätigt, teils gravierender als beschrieben (ID-Kollision bei 7 Kandidatenbüchern entdeckt). Evidence Coverage 14 Objekte — teilweise bestätigt (Inhalt vorhanden, nur unter nicht-standardisierten Überschriften/im Fließtext). Git-Index-Fehler — bestätigt, aber als infrastrukturelles Sandbox-Problem, bewusst nicht repariert.

**Umgesetzt:** `02_sources/book_catalog.md` vollständig neu strukturiert (15 Bücher korrekt zugeordnet, 7 kollidierende Kandidaten auf B-0041–B-0047 umnummeriert). `00_project/REPOSITORY_KPIS.md` auf Version 1.1 gebracht (13 fehlende Buchsektionen B-0003–B-0015 ergänzt). 29 Wissensobjekte um sichtbaren „⚠ Hinweis: Publication Bias"-Abschnitt ergänzt (CEB/Challenger- und JOLT/Tethr-Komplex, nicht Gap Selling). `SCIENTIFIC_DEBT.md` entsprechend annotiert. 10 Assumptions (A-0030–A-0039): Überschrift „Wie gut ist sie belegt?" → „Evidenzstatus" (nur Umbenennung). 4 Modelle (MOD-0001/0002/0004/0005): „## Evidenzlevel"-Abschnitt ergänzt, ausschließlich durch Transkription/Ableitung bereits vorhandener Fakten, keine neue Bewertung erfunden.

`00_project/EXTERNAL_AUDIT_RESOLUTION_REPORT.md` erstellt (5 Pflichtabschnitte: Executive Summary, Punkt-für-Punkt-Analyse aller 7 Kritikpunkte, Geänderte Dateien, Verbleibende offene Punkte, Release Readiness).

**Ergebnis:** **READY FOR FINAL RC-1 AUDIT.** Details: `00_project/EXTERNAL_AUDIT_RESOLUTION_REPORT.md`.

**Keine neuen Wissensobjekte (SRC-0010 existierte bereits), keine neue Forschung, keine neue Governance, keine Änderungen am Canonical Knowledge Model, Operating Manual, Research Program oder an abgeschlossenen Forschungsprojekten/Editor Decisions.**

**Nächster Schritt:** Finaler RC-1-Audit (Herausgeberauftrag ausstehend). Danach unverändert: Herausgeber-Entscheidungsrunde OD-008–012 (inkl. OD-010/Peer-Review); Reparatur des Git-Index-Formatierungsfehlers lokal beim Herausgeber (außerhalb der Sandbox); Fortsetzung Academic Recovery Plan Tier 1.

---

### Sales Codex 1.0 Final Pre-Release Sprint — ABGESCHLOSSEN

**Stand: 2026-07-03**

Auslöser: Herausgeberauftrag „Sales Codex 1.0 Final Pre-Release Sprint" — reiner Konsistenzsprint unmittelbar vor dem RC-1-Audit. Auftrag: alle vor dem Audit bekannten Repository-Widersprüche und Konsistenzprobleme beseitigen. Ausdrücklich ausgeschlossen: neue Forschung, neue Wissensobjekte, neue Frameworkbestandteile, neue Open Decisions, Änderungen am Canonical Knowledge Model, am Operating Manual oder am Research Program.

**Umgesetzt:**
- **Phase 1 (Open Decisions):** OD-006 (Meme-Filter für QK-Rating) und OD-007 (CTX-Kontextebene) wurden vom Herausgeber während dieser Session tatsächlich entschieden (beide **Angenommen**) und in `00_project/OPEN_DECISIONS.md` dokumentiert. Ein Scope-Konflikt zwischen "vollständiger Umsetzung" (Phase-1-Wortlaut) und dem generellen Frameworkänderungsverbot dieses Sprints wurde erkannt und vom Herausgeber aufgelöst: Entscheidungen sind verbindlich, die technische Implementierung (QK-Meme-Filter, CTX-Feld in Templates/CKM/Operating Manual, rückwirkende CTX-Befüllung von ~47 Prinzipien/~41 Techniken) ist ausdrücklich auf einen separaten Framework Integration Sprint nach Version 1.0 verschoben.
- **Phase 2 (MEC-0018):** Dokumentierter Widerspruch zwischen MEC-0018s Evidenzbewertung ("extrem gut repliziert — Bargh, Dijksterhuis u.a.") und dem bestehenden Scientific-Debt-Eintrag (Replikationsrisiko, Priorität Hoch, Kahnemans öffentliche Anerkennung 2012) vollständig behoben: Evidenzlevel differenziert (Spreading Activation E4 vs. Bargh/Dijksterhuis-Priming E2), Warnhinweis im Vertriebsrelevanz-Abschnitt ergänzt, Cross-References (MOD-0008, ST-0179, P-0035, T-0035) angeglichen, `SCIENTIFIC_DEBT.md` um Auflösungsvermerk ergänzt (Replikationsrisiko selbst bleibt Priorität Hoch — nicht das Risiko, nur der Objektwiderspruch wurde behoben).
- **Phase 3 (Evidence Harmonization):** 70 Wissensobjekte in `03_knowledge_base/` auf das je Objekttyp bereits templatekonforme Evidenzfeld-Schema umbenannt (A → `Evidenzstatus`, MEC/MOD/T → `Evidenzlevel`, P → `Evidenzklassifikation`, ST → `Evidenzklasse` als bestehende Mehrheitspraxis). Ausschließlich Header-Umbenennung, keine inhaltliche Änderung an einem Bewertungswert.
- **Phase 4 (Verification):** Repositoryweiter Scan aller Backtick-Dateiverweise (48 Treffer geprüft, ausnahmslos bereits dokumentierte historische/Platzhalter-Fälle); MEC-0018-Familie nach Bearbeitung vollständig über natives Lesewerkzeug gegengeprüft.
- `00_project/FINAL_PRE_RELEASE_REPORT.md` erstellt (7 Pflichtabschnitte: Zusammenfassung, Umgesetzte Änderungen, Geänderte Dateien, Behobene Widersprüche, Repository-Statistik, Verbliebene Blocker, Empfehlung).

**Ergebnis:** **READY FOR RC-1 AUDIT.** Kein bekannter, unbehandelter Widerspruch verbleibt innerhalb des Sprintscopes. Verbliebene offene Punkte (OD-006/007-Implementierung, OD-008–012, Publication-Bias-Blocker SD-SYS-001/004, 14 Wissensobjekte ohne Evidenzfeld) sind bereits dokumentiert, transparent markiert und liegen außerhalb dieses Sprintauftrags — Details: `00_project/FINAL_PRE_RELEASE_REPORT.md`.

**Keine neue Forschung, keine neuen Wissensobjekte, keine Frameworkänderungen, keine neuen Open Decisions, keine Änderungen am Canonical Knowledge Model, Operating Manual oder Research Program.**

**Nächster Schritt:** RC-1-Audit selbst (Herausgeberauftrag ausstehend). Danach: Framework Integration Sprint für OD-006/007; Herausgeber-Entscheidungsrunde OD-008–012; Fortsetzung Academic Recovery Plan Tier 1.

---

### Research Project W-001 Repository Integration Sprint (Post Editor Decision) — ABGESCHLOSSEN

**Stand: 2026-07-03**

Auslöser: Herausgeberauftrag "Research Project W-001 Repository Integration Sprint (Post Editor Decision)". Die zuvor als Entwurf vorbereitete Editor Decision zu W-001 (`06_research_program/completed/W001/06_EDITOR_DECISION.md`) wurde durch den Herausgeber (Felix) tatsächlich getroffen: **Teilweise annehmen.** Auftrag dieses Sprints: die bereits getroffene, verbindliche Entscheidung sauber in das Repository integrieren, W-001 formal abschließen und den ersten vollständigen Research Lifecycle des Research Program erfolgreich beenden — ohne die Entscheidung selbst zu erweitern oder zu verändern.

**Entscheidung:** Die mathematische Formalisierung des Socio-Cognitive Sensegiving Model (SCSM) wird nicht in den Sales Codex übernommen (Red-Team-Kritik — 11 von 13 Prüfkriterien nicht erfüllt — wird gefolgt). Übernommen wird der wissenschaftlich belastbare Kernbefund: Diagnoseorientierte (SPIN, Gap Selling) und teaching-/sensemaking-orientierte (Challenger) Vertriebsansätze stehen nicht in universellem Widerspruch, sondern beschreiben unterschiedliche, kontextabhängige Wirkmechanismen (Problemreife, Kontext, Sensemaking-Bedarf, Buying-Center-Dynamik). Keine neue Grand Theory, kein neues MOD, keine Differentialgleichung, kein neues Symbolsystem.

**Umgesetzt:**
- Stufe 7 (Editor Decision): von Entwurf auf finale, verbindliche Entscheidung überführt — Begründung, Stellungnahme zu drei zentralen Streitpunkten, Integrationstabelle, ethische Einschätzung, Datum/Unterschrift.
- Stufe 8 (Repository Integration): sechs bestehende Wissensobjekte erweitert (A-0020, P-0021, P-0025, MEC-0013, T-0019, T-0023) — durchgängig Kontextpräzisierung statt "Widerspruch"/"Methodologiekonflikt", Source-ID um `W-001` ergänzt. Keine Neuanlage. `06_research_program/completed/W001/REPOSITORY_INTEGRATION_LOG.md` neu angelegt.
- `00_project/SCIENTIFIC_DEBT.md`: neue Sektion "W-001" (OQ-2 bis OQ-4 technisch übergeben, Gartner-Quellenklassifizierung als offener Punkt dokumentiert); zwei bestehende Einträge (A-0020 vs. P-0025; MOD-0001 vs. MOD-0004) als kontextuell aufgelöst markiert, nicht gelöscht.
- `00_project/OPEN_DECISIONS.md`: neue Open Decision OD-012 (Formalisierung der jetzt dokumentierten Kontextspezialisierung), bereits im vorherigen Repository-Integrationsplan als voraussichtlich erforderlich angekündigt.
- Stufe 9 (Health Check): echter Abschluss-Health-Check nach Integration durchgeführt und bestanden (eine bewusst akzeptierte Restlücke: Stufe-1/2-Alt-Lücke, historisch, außerhalb des Sprintmandats).
- `06_research_program/RESEARCH_STATUS.md`: W-001-Zeile in die `completed/`-Tabelle verschoben.
- Projektordner von `06_research_program/active/W001/` nach `06_research_program/completed/W001/` verschoben (unverändert, gemäß `RESEARCH_GOVERNANCE.md`, Abschnitt 6.2).

**Ergebnis:** W-001 ist vollständig abgeschlossen und ist das erste Forschungsprojekt, das den vollständigen neunstufigen RC-1 Research Lifecycle erfolgreich durchlaufen hat. Vollständiger Bericht: `06_research_program/completed/W001/W001_REPOSITORY_INTEGRATION_REPORT.md`.

**Keine neue Forschung, keine neue Literaturrecherche, keine Frameworkänderungen, keine Änderungen am Canonical Knowledge Model oder Operating Manual außer den zur Integration notwendigen Herkunftsvermerken.**

**Nächster Schritt:** Herausgeber-Entscheidungsrunde zu OD-006 bis OD-012 (jetzt einschließlich der neuen OD-012); Fortsetzung Academic Recovery Plan Tier 1; optional ein neues Forschungsprojekt (W-002) zur weiteren Erprobung des Research Lifecycle.

---

### Research Program Finalization Sprint (RC-1) — ABGESCHLOSSEN

**Stand: 2026-07-03**

Auslöser: Herausgeberauftrag „Research Program Finalization Sprint" auf Basis von `06_research_program/RESEARCH_PROGRAM_REVIEW_RC1.md` (Architekturprüfung, Gesamtreifegrad „MAJOR REVISION REQUIRED"). Auftrag: Das Research Program (`06_research_program/`) vollständig, methodisch konsistent und skalierbar ausarbeiten — Governance, Templates, Lifecycle, Repository-Integration, Health-Check-Stufe, minimale Framework-Integration, W-001-Infrastruktur. Ausdrücklich ausgeschlossen: Wissensobjekte, neue Forschungsprojekte, Literaturrecherche, Sales-Codex-Inhalt, sowie an W-001 selbst: Initial Hypothesis, Scientific Master Review, Red Team Review, Theory Landscape, Decision Brief, Editor Decision, Scientific Debt, Open Decisions, Book Mode.

**Umgesetzt:**
- Governance vollständig ausgearbeitet: `README.md`, `RESEARCH_GOVERNANCE.md` (Rollen, Statusdefinitionen, Ordnerübergänge, Abbruch-/Abschlusskriterien), `DECISION_POLICY.md` (Entscheidungskriterien, Bezug zum Evidenzsystem), `RESEARCH_STATUS.md` (Tabellenformat).
- Zwei neue programmweite Dokumente: `RESEARCH_LIFECYCLE.md` (neunstufiger Prozess, Research Question bis Health Check) und `REPOSITORY_INTEGRATION.md` (Integrationsmechanik, kompatibel mit dem Canonical Knowledge Model, ohne dessen Kernlogik zu ändern).
- Alle 5 bestehenden Templates ausgearbeitet, 6 neue Templates ergänzt (Initial Hypothesis, Master Review, Open Questions, References, Research Log, Health Check) — `templates/` jetzt 11 statt 5 Dateien.
- Drei minimale, punktuell angehängte Framework-Integrationshinweise: `00_project/SALES_CODEX_OPERATING_MANUAL.md` (neuer Abschnitt 11), `01_framework/05_knowledge_model/canonical_knowledge_model.md` (neuer Abschnitt 11, bestehende Nummerierung 1–10 unverändert), `00_project/task_rules.md` (neuer Unterabschnitt 7.5).
- W-001-Infrastruktur ausgearbeitet (`README.md`, `OPEN_QUESTIONS.md` mit 5 extrahierten offenen Fragen, `REFERENCES.md` mit 119 konsolidierten Quellen, `RESEARCH_LOG.md`) — wissenschaftlicher Inhalt von W-001 unverändert.

**Ergebnis:** Alle acht in der Architekturprüfung benannten strukturellen Blocker bearbeitet (sechs vollständig geschlossen, einer bewusst nur projektebenenbezogen geschlossen — OD-003 bleibt unverändert offen —, einer durch explizite Governance-Entscheidung aufgelöst). Einschätzung: **Ready after Minor Revision** — Begründung und vollständige Details: `06_research_program/RESEARCH_PROGRAM_IMPLEMENTATION_REPORT_RC1.md`.

**Keine Änderungen an Wissensobjekten, keine neue Recherche, keine Änderung an W-001s wissenschaftlichem Inhalt, keine Änderung an Open Decisions/Scientific Debt/Book Mode.**

**Nächster Schritt:** Unverändert die vor diesem Sprint bestehende Priorität — Herausgeber-Entscheidungsrunde zu OD-006 bis OD-011 (siehe `00_project/OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`) sowie Fortsetzung des Academic Recovery Plan Tier 1. Zusätzlich empfohlen (nicht umgesetzt): ein neues Forschungsprojekt (W-002) vollständig durch die neun Lifecycle-Stufen laufen zu lassen, um die neue Research-Program-Architektur praktisch zu erproben.

---

### Repository Consolidation Sprint 2 (Implementation Phase) — ABGESCHLOSSEN

**Stand: 2026-07-02**

Auslöser: Herausgeberauftrag „Repository Consolidation Sprint 2 — Implementation Phase" — Umsetzung von acht vom Herausgeber freigegebenen Editor Decisions (ED-001 bis ED-008) aus `00_project/REPOSITORY_CONSOLIDATION_REPORT_RC1.md`. Reiner strukturell-mechanischer Umsetzungssprint (Löschen/Verschieben/Archivieren bereits identifizierter Dateien plus notwendiger Referenzkorrekturen) — keine eigenen Architekturentscheidungen, keine zusätzlichen Optimierungen, kein Eingriff in die ausdrücklich ausgeschlossenen Bereiche (`book_catalog.md`, CURRENT_STATE-/NEXT_ACTION-/SESSION_LOG-Struktur, Research Program, Open Decisions, Literature Index, Scientific Debt, Canonical Knowledge Model, Framework-Struktur, Top-Level-Ordner, Ordnernummerierung, README-Dateien).

**Umgesetzt:**
- ED-001: Leerer Duplikat-Ordner `04_book_analysis/Never_Split_The_Difference/` gelöscht.
- ED-002: Leere Debug-Datei `04_book_analysis/Emotional Intelligence/test_probe.md` gelöscht.
- ED-003: `codex_knowledge_model.md` von `01_framework/05_knowledge_model/` nach `99_archive/` verschoben (Inhalt unverändert). `INDEX.md` (Framework-Abschnitt) auf `canonical_knowledge_model.md` als aktives Wissensmodell-Dokument korrigiert.
- ED-004: `VAL-0001_consistency_review_pilot001.md` und `PILOT_001_ABSCHLUSSBERICHT.md` von `00_project/` nach `04_book_analysis/SPIN_Selling/` verschoben; `VAL-0002_consistency_review_influence.md` von `00_project/` nach `04_book_analysis/Influence/` verschoben (alle drei Dokumente inhaltlich unverändert).
- ED-005: `SCRP-0001_Sales_Core.md` von der Repository-Root nach `00_project/peer_review/decisions/` verschoben (unverändert).
- ED-006/007/008: `decision_log.md`, `roadmap.md`, `task_proposal_B-0002_influence.md` von `00_project/` nach `99_archive/` verschoben (alle drei unverändert; `99_archive/` damit erstmals befüllt).

**Referenzprüfung:** Vollständige repositoryweite Suche nach Backtick-Pfadverweisen auf alle acht betroffenen Alt-Pfade ergab genau eine aktive, korrekturbedürftige Referenz (`INDEX.md`, Zeile 21) — diese wurde korrigiert. Alle übrigen Fundstellen der Alt-Pfade liegen ausschließlich in datierten historischen Sprint-/Audit-Berichten (`POST_MORTEM_B0002.md`, `CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md`, `REPOSITORY_CONSOLIDATION_REPORT_RC1.md`) oder im Dokument `task_proposal_B-0002_influence.md` selbst (jetzt in `99_archive/`, laut ED-008 unverändert zu belassen) — diese wurden bewusst **nicht** verändert, da sie vergangene Zustände korrekt beschreiben und eine nachträgliche Änderung Repository-Historie verfälschen würde. Details siehe `00_project/REPOSITORY_CONSOLIDATION_IMPLEMENTATION_REPORT_RC1.md`.

**Repository Health Check:** Keine verwaisten Dateien, keine doppelten Markdown-Inhalte (MD5-Prüfung), keine neu entstandenen toten Pfadverweise. Leere Ordner: 17 (zuvor 18 — `Never_Split_The_Difference/` durch ED-001 entfernt); alle verbleibenden 17 sind bereits im RC-1-Bericht als bewusst vorbereitete, nicht fehlerhafte Struktur eingeordnet. **Bekannte, außerhalb des Scopes liegende Auffälligkeit:** `git status`/`git diff` schlagen in dieser Umgebung mit `fatal: unknown index entry format 0x32380000` fehl (`git log` funktioniert unverändert). Dies ist ein vorbestehendes Problem des `.git/index`-Dateiformats (vermutlich durch eine neuere Git-Version außerhalb dieser Sandbox erzeugt) und keine Folge dieses Sprints — siehe Implementation Report für Details und Empfehlung.

**Keine neuen Wissensobjekte, keine neue Recherche, keine Framework-Änderungen, keine Open Decisions geändert, keine Top-Level-Ordner oder Ordnernummerierung verändert.**

**Nächster Schritt:** Unverändert Phase 1 des Sales Codex 1.0 Programms (Herausgeber-Entscheidungsrunde OD-006 bis OD-011) sowie die in `REPOSITORY_CONSOLIDATION_REPORT_RC1.md` Kapitel 12 dokumentierten Kategorie-B/C-Maßnahmen (z. B. Nummernkollision `04_synthesis`/`05_research`, weiterhin unentschieden — außerhalb des Scopes dieses Sprints). Vollständiger Bericht: `00_project/REPOSITORY_CONSOLIDATION_IMPLEMENTATION_REPORT_RC1.md`.

---

### Behavioral Science Review Sprint (externes Gutachten zu SPR-0003) — ABGESCHLOSSEN

Unabhängiges wissenschaftliches Gutachten zum Behavioral Science Expansion Sprint (SPR-0003) geprüft und per verbindlicher Editor Decision umgesetzt: `00_project/BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md`.

Bilanz: 8 Reviewer-Empfehlungen geprüft → 4× Übernehmen (ED-001, ED-002, ED-005, ED-007), 3× Teilweise übernehmen (ED-003, ED-004, ED-006), 1× Ablehnen (ED-008, neue Kategorien PRX/TAX — Framework-Änderung außerhalb Scope). Bei zwei Empfehlungen (ED-002, ED-007) wich der reale Repository-Zustand vom Gutachten ab (behauptete Lücken waren bereits geschlossen) — als Widerspruch dokumentiert, nicht geglättet.

Geänderte Wissensobjekte: MEC-0025 (umbenannt: "Fairness-Verzicht" → "Altruistische Bestrafung / Altruistic Punishment"), MOD-0010 (Terminologie-Update), MOD-0011 und MOD-0012 (Klassifikationshinweis ergänzt), MEC-0002/MEC-0021/MEC-0022 (Boundary Conditions Individual→Organisation ergänzt). Geänderte Governance-Dateien: `SCIENTIFIC_DEBT.md` (neuer Eintrag Konstruktvalidität EI, Ariely-Status auf "partially mitigated" präzisiert), `LITERATURE_INDEX.md` (Prüfvermerk ergänzt, keine inhaltliche Korrektur).

Keine neuen Objekt-IDs, keine neuen Kategorien, keine Framework-Version-Änderung, keine Open Decisions geändert, kein Eingriff in Operating Manual oder Canonical Knowledge Model.

---

### Sales Codex OS v1.1 — ABGESCHLOSSEN

Framework-Update 2026-06-30. Grundlage: POST_MORTEM_B0002.md.

Geänderte Dateien: 8 | Neue Dateien: 4 | Implementierungsphasen: 1–4 vollständig

Änderungsüberblick: `00_project/changelog.md`

---

### SPIN Selling (B-0001, SRC-0001) — ABGESCHLOSSEN

Pilot-001 abgeschlossen 2026-06-27.

Objekte: ST-0001–ST-0023, A-0001–A-0004, MEC-0001–MEC-0004, P-0001–P-0007, T-0001–T-0004, MOD-0001, VAL-0001

---

### Influence (B-0002, SRC-0002) — ABGESCHLOSSEN

Primärquelle: Influence, Robert B. Cialdini, Ausgabe 2007 (PDF).  
Abgeschlossen: 2026-06-30

Neue Objekte: 59 (26 ST + 8 A + 8 MEC/ext + 8 P + 7 T + 1 MOD + 1 VAL)

---

### Never Split the Difference (B-0003, SRC-0003) — ABGESCHLOSSEN

Primärquelle: Never Split the Difference, Chris Voss / Tahl Raz, 2016 (PDF vorliegend).  
Gestartet: 2026-06-30 | Abgeschlossen: 2026-06-30 | Modus: Book Mode  
Objekte: 57 ST + 5 A + 3 MEC (neu) + 3 MEC (ext.) + 5 P + 7 T + 1 MOD + 1 VAL + 1 BOOK_REVIEW = **83 Gesamt**

| Task | Beschreibung | Status |
|---|---|---|
| TASK-0011 | SRC-0003 anlegen | DONE |
| TASK-0012 | Kapitelstruktur erfassen | DONE |
| TASK-0013 | Statements extrahieren | DONE — 57 ST (ST-0050–ST-0106) |
| TASK-0014 | Annahmen identifizieren | DONE — 5 A (A-0013–A-0017) |
| TASK-0015 | Mechanismen ableiten | DONE — 3 ext. (MEC-0002, -0003, -0007) + 3 neu (MEC-0010–0012) |
| TASK-0016 | Prinzipien formulieren | DONE — 5 P (P-0016–P-0020) |
| TASK-0017 | Techniken erfassen | DONE — 7 T (T-0012–T-0018) |
| TASK-0018 | Modelle aktualisieren | DONE — MOD-0003 (BCSM + Voss-System) |
| TASK-0019 | Selbstreview (VAL-0003) | DONE — VAL-0003 in 04_book_analysis/Never Split the Difference/ |
| TASK-0020 | Abschlussbericht | DONE — BOOK_REVIEW_REPORT_B0003.md |

---

### The Challenger Sale (B-0004, SRC-0004) — ABGESCHLOSSEN

Primärquelle: The Challenger Sale, Matthew Dixon & Brent Adamson (CEB), 2011 (PDF vorliegend).  
Gestartet: 2026-06-30 | Abgeschlossen: 2026-06-30 | Modus: Book Mode  
Objekte: 26 ST + 6 A + 2 MEC (neu) + 2 MEC (ext.) + 4 P + 3 T + 1 MOD + 1 VAL + 1 BOOK_REVIEW = **46 Gesamt**

| Task | Beschreibung | Status |
|---|---|---|
| TASK-0021 | SRC-0004 anlegen | DONE |
| TASK-0022 | Kapitelstruktur erfassen | DONE |
| TASK-0023 | Statements extrahieren | DONE — 26 ST (ST-0107–ST-0132) |
| TASK-0024 | Annahmen identifizieren | DONE — 6 A (A-0018–A-0023) |
| TASK-0025 | Mechanismen ableiten | DONE — 2 neu (MEC-0013, MEC-0014) + 2 ext. (MEC-0002, MEC-0007) |
| TASK-0026 | Prinzipien formulieren | DONE — 4 P (P-0021–P-0024) |
| TASK-0027 | Techniken erfassen | DONE — 3 T (T-0019–T-0021) |
| TASK-0028 | Modelle aktualisieren | DONE — MOD-0004 (TTC-Modell) |
| TASK-0029 | Selbstreview (VAL-0004) | DONE — VAL-0004 in 04_book_analysis/The Challenger Sale/ |
| TASK-0030 | Abschlussbericht | DONE — BOOK_REVIEW_REPORT_B0004.md |

---

### Gap Selling (B-0005, SRC-0005) — ABGESCHLOSSEN

Primärquelle: Gap Selling, Keenan, 2018 (PDF vorliegend, ⚠ Teilfassung: 98 Seiten, fehlende Kap. 1, 2, 6, 13, 15–20).  
Gestartet: 2026-06-30 | Abgeschlossen: 2026-06-30 | Modus: Book Mode  
Objekte: 17 ST + 6 A + 1 MEC (neu) + 2 MEC (ext.) + 2 P + 4 T + 1 MOD + 1 VAL + 1 BOOK_REVIEW = **35 Gesamt**

| Task | Beschreibung | Status |
|---|---|---|
| TASK-0033 | Statements extrahieren | DONE — 17 ST (ST-0133–ST-0149) |
| TASK-0034 | Annahmen identifizieren | DONE — 6 A (A-0024–A-0029) |
| TASK-0035 | Mechanismen ableiten | DONE — 1 neu (MEC-0015) + 2 ext. (MEC-0002, MEC-0004) |
| TASK-0036 | Prinzipien + Techniken | DONE — 2 P (P-0025–P-0026) + 4 T (T-0022–T-0025) |
| TASK-0037 | Modell anlegen | DONE — MOD-0005 (Gap Selling Modell) |
| TASK-0038 | Selbstreview (VAL-0005) | DONE — VAL-0005: BESTANDEN; Canonicalization Rate 67% |
| TASK-0039 | Abschlussbericht | DONE — BOOK_REVIEW_REPORT_B0005.md |
| TASK-0040 | State-Dateien aktualisieren | DONE — dieses Dokument |

**Canonicalization Rate: 67% (2/3 MECs extended)**

---

## ✅ SPRINT S1-SYNTHESIS — ABGESCHLOSSEN

**Sales Sprint 1 ist abgeschlossen.** Alle 5 Bücher vollständig verarbeitet:
- B-0001: SPIN Selling
- B-0002: Influence
- B-0003: Never Split the Difference
- B-0004: The Challenger Sale
- B-0005: Gap Selling

**S1-SYNTHESIS abgeschlossen: 2026-07-01**

Alle 6 SPR-0001-Dokumente angelegt in `04_synthesis/SPR-0001_Sales_Core_Synthesis/`:

| Dokument | Status |
|---|---|
| synthesis.md | DONE — 254 Objekte, 5 Konvergenz-Cluster, strukturelle Befunde |
| contradiction_matrix.md | DONE — W-001 bis W-005, W-001 UNGELÖST → Sprint 2 |
| canonicalization_report.md | DONE — Sprint-Rate 31,8%; Fusions-Kandidaten dokumentiert |
| evidence_upgrade_report.md | DONE — MEC-0002 QK-5, P-0002 QK-4, Rankings |
| emerging_principles.md | DONE — P-S1-001 bis P-S1-004 identifiziert und angelegt; MOD-S1 abgelehnt |
| research_agenda.md | DONE — 12 Forschungsfragen (F-001–F-012) priorisiert; 5 Buchempfehlungen |

**Neue Wissensobjekte (S1-SYNTHESIS):**
- P-S1-001: Cost of Inaction als universeller Kaufmotivator (QK-5, alle 5 Bücher)
- P-S1-002: Mikro-Commitment-Sequenz als Kaufstruktur (QK-4)
- P-S1-003: Problem-Zentrierung als universelles Differenzierungsprinzip (QK-4)
- P-S1-004: Informationssparsamkeit als Wirkungsverstärker (QK-4)

**Hauptbefunde:**
- MEC-0002 ist das Gravitationszentrum des Sales Codex (QK-5, alle Bücher)
- W-001 (Teach First vs. Diagnose First) ist die kritische offene Frage für Sprint 2
- Sprint-2-Priorität: The JOLT Effect (Dixon) als W-001-Entscheidungsquelle

---

## Nächste freie IDs

**Hinweis:** Tabelle unten spiegelt den Stand nach Sprint 1 (S1-Synthesis). Aktueller Stand nach Behavioral Science Expansion Sprint (2026-07-02, nach B-0015): ST-0310, A-0061, MEC-0030, P-0054, T-0048, MOD-0013, VAL-0016, SRC-0016. Siehe Abschnitt „BEHAVIORAL SCIENCE EXPANSION SPRINT 1" unten für den vollständigen Objektzuwachs.

| Typ | Nächste ID (Stand Sprint 1, historisch) |
|---|---|
| ST | ST-0150 |
| A | A-0030 |
| MEC | MEC-0016 |
| P | P-0027 (P-S1-001–004 sind S1-Synthesis-IDs) |
| T | T-0026 |
| MOD | MOD-0006 (oder MOD-S1 — abgelehnt für Sprint 1) |
| VAL | VAL-0006 |
| SRC | SRC-0006 |

---

## Offene Deferred Tasks

1. **Hoch:** Gemini-Validierung MEC-0010/0011 (Lieberman + Spiegelneuronen) — Validierungssprint-Dokument: `VALIDIERUNGSSPRINT_MEC0010-0012.md`
2. **Hoch:** Gemini-Validierung MEC-0005–0009 (Cialdini-MECs) + Langer-Xerox-Replikationsstatus
3. **Hoch (S1-Synthesis):** A-0020 vs. P-0025 Widerspruch (Challenger vs. Gap Selling Methodik)
4. **Mittel:** Externe Validierung A-0019 (53%-CEB-Loyalitätssplit) + MEC-0013/0014

---

---

## Academic Recovery Sprint (ARS-0001) — Research Pack 1 verarbeitet

**Stand: 2026-07-01**

Auslöser: Wissenschaftliches Gutachten nach Sprint 2 (`00_project/WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md`, Gesamtnote B). ARS-0001 ist ein Konsolidierungssprint — kein Book Mode, kein neuer Research Sprint.

**Geleistet:**
- Peer Review vollständig bewertet: `00_project/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md` (12 Einzelentscheidungen: 7 übernommen/teilweise, 3 abgelehnt, CTX als Open Decision)
- Research Pack 1 (8 externe Quellen) verifiziert und integriert: `00_project/ACADEMIC_RECOVERY_REPORT.md`
- Roadmap für Fortsetzung: `00_project/ACADEMIC_RECOVERY_PLAN.md` (AR-001 bis AR-012, priorisiert)
- Neue Scientific-Debt-Kategorie „Publication Bias (kommerzielle Studien)" + SD-SYS-004
- MEC-0014 um Theorie-Referenzen erweitert (Webster & Wind 1972, Sheth 1973, Eisenhardt 1989) — E-Level unverändert
- OD-007 (CTX-Ebene) in OPEN_DECISIONS.md — wissenschaftlich bewertet, NICHT eingeführt (wie beauftragt)
- Neue dokumentierte Kandidaten (nicht angelegt): MEC „Adaptive Selling Behavior", Meta-Prinzip „Asymmetrische Risikoverteilung im Buying Center", W-006 „Kognitive Leichtigkeit vs. Rational Drowning"

**Reifegrad-Einschätzung nach ARS-0001:** B → tendenziell B+ (Prozess-/Transparenzgewinn), **A- noch nicht erreicht** — Begründung in PEER_REVIEW_DECISION_REPORT_SPRINT_002.md, Abschnitt "Abschlussbewertung".

**Keine Wissensobjekte (ST/A/MEC/P/T/MOD) neu angelegt.** Keine Framework-Änderungen. Keine E-Level-Änderungen an bestehenden Objekten.

**Nächster Schritt:** `00_project/ACADEMIC_RECOVERY_PLAN.md`, Tier 1 (AR-001 Problemreife-Hypothese Volltext-Recherche, AR-002 Publication-Bias-Klärung).

---

## Codex Audit 2026-07 + Consistency Correction Sprint

**Stand: 2026-07**

Auslöser: Herausgeberauftrag „CODEX AUDIT 2026-07" (vollständiger, ausschließlich lesender wissenschaftlicher Repository-Audit) gefolgt von „CODEX CONSISTENCY CORRECTION SPRINT 2026-07" (Umsetzung von Meilenstein 1 aus Kapitel 11 des Audits, reine Konsistenzarbeit ohne neue Recherche).

**Audit-Ergebnis:** `00_project/CODEX_AUDIT_2026-07.md` — Gesamtnote **B+**. Wichtigste Neubefunde: (1) E5-Zähler-Diskrepanz im Reifegradbericht (behauptet 5, tatsächlich nur MEC-0015/MEC-0021); (2) Evidenzlevel-Desynchronisation T-0012/T-0013 gegenüber bereits herabgestuften MEC-0011/MEC-0010; (3) 20 Objekte (12 T + 8 P) ohne Evidenzfeld, 4 Meta-Prinzipien fälschlich als „fehlend" markiert (Audit-Methodikfehler, YAML-Frontmatter nicht erfasst); (4) leerer Duplikat-Ordner; (5) zwei koexistierende Knowledge-Model-Dateien.

**Consistency Correction Sprint — durchgeführt:** `00_project/CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md`
- T-0012/T-0013: Evidenzlevel E3 → E2 synchronisiert mit MEC-0011/MEC-0010
- 12 Techniken (T-0019–T-0021, T-0026–T-0034) + 8 Prinzipien (P-0027–P-0034): Evidenzfeld ergänzt (Cross-Referenz auf verlinkte Objekte, keine neue Bewertung, als Empfehlung für künftigen Bewertungssprint dokumentiert)
- 4 Techniken (T-0022–T-0025): Feldname „Evidenzgrad" → „Evidenzlevel" harmonisiert, Werte unverändert
- 4 Meta-Prinzipien (P-S1-001–004): Sichtbarkeits-Spiegel des bestehenden YAML-`e_level`-Feldes ergänzt; Audit-Falschbefund richtiggestellt
- E5-Zähler-Erratum dokumentiert (nicht rückwirkend im Reifegradbericht geändert)
- Leerer Ordner `04_book_analysis/Never_Split_The_Difference/` zur Entfernung vorgemerkt (nicht gelöscht)
- `codex_knowledge_model.md` als veraltet markiert (nicht gelöscht), Empfehlung an Herausgeber dokumentiert

**Keine neuen Wissensobjekte, keine neue Recherche, keine Framework-Änderungen.** Alle Änderungen sind reine Konsistenzkorrekturen mit Verweis auf den Audit.

**Nächster Schritt:** Herausgeber-Entscheidungen zu den in Abschnitt 8 von `CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md` dokumentierten offenen Empfehlungen; danach Fortsetzung `ACADEMIC_RECOVERY_PLAN.md` Tier 1 (AR-001, AR-002, AR-013).

---

## Academic Recovery Sprint (ARS-0001) — Phase 2: Research Pack 2, 3, 4 verarbeitet

**Stand: 2026-07-01**

Auslöser: Herausgeber-Auftrag "Academic Recovery Sprint – Phase 2" mit drei zugelieferten Research Packs (Entscheidungspsychologie/Behavioral Economics, Sozialpsychologie/Persuasion, Verhandlungsforschung), zusammengefasst in einer Datei.

**Geleistet:**
- Alle drei Packs gegen Operating Manual, Canonical Knowledge Model, Evidence System und Scientific Debt geprüft: `00_project/ACADEMIC_RECOVERY_REPORT_PACK_2_4.md` (~60 Themen, je Übernehmen/Teilweise/Ablehnen mit Begründung)
- Drei quantitativ neue Meta-Analysen unabhängig websuchverifiziert: Brown/Imai/Vieider/Camerer (2024, Loss Aversion, JEL), Schley & Weingarten (Anchoring, Management Science — Zitationskorrektur gegenüber Pack), Mertens et al. (2021, Nudging, PNAS — inkl. bisher unerwähnter Publication-Bias-Kontroverse, die der Editor selbst ergänzt hat)
- Neuer Repository-Bereich `05_research/` mit `LITERATURE_INDEX.md` angelegt (kein Wissensobjekt — dauerhaftes Literaturverzeichnis, ~50 Quellen über drei Domänen, mit Verifikationsstatus je Quelle)
- 15 bestehende MEC-/MOD-/A-Objekte um Literaturreferenzen erweitert (CKM 4.1 "Erweitern"): MEC-0002, MEC-0003, MEC-0005–0008, MEC-0010, MEC-0011, MEC-0012, MEC-0017, MEC-0019, MEC-0020, MEC-0021, MOD-0007, A-0038
- Zwei neue Scientific-Debt-Einträge: SD-SYS-005 (Nudging-Publication-Bias-Kontroverse), SD-SYS-006 (Konvergenzbestätigungen bestehender B-0002/B-0003-Einträge durch unabhängige Packs)
- Fünf neue, nicht angelegte Literaturkandidaten dokumentiert (`review_queue.md`): Elaboration Likelihood Model (höchste Priorität), Trust Formation, Persuasion Knowledge Model, Fairness/Equity Theory, Choice Architecture/Default Effects
- OD-008 (Priorisierung ELM/Trust/PKM-Sprint) in OPEN_DECISIONS.md — Editor empfiehlt weiterhin ACADEMIC_RECOVERY_PLAN.md Tier 1 vorzuziehen

**Reifegrad-Einschätzung nach Phase 2:** B+ → tendenziell weiter Richtung A-, **A- weiterhin nicht erreicht** — Begründung: Pack 2–4 haben einen anderen Fokus (Behavioral Economics/Sozialpsychologie/Verhandlung) als die vom Academic Recovery Plan priorisierten Tier-1-Themen (Problemreife-Hypothese W-001, Publication-Bias CEB/Challenger). Fortschritt ist real (quantitative Präzisierung von MEC-0002/MEC-0021, breite externe Konvergenzbestätigung, zwei neue prioritäre Struktur-Lücken identifiziert, eine im Pack selbst übersehene Kontroverse aufgedeckt), aber orthogonal zur höchsten bestehenden Priorität. Details: `00_project/ACADEMIC_RECOVERY_REPORT_PACK_2_4.md` Abschnitt 7.

**Keine Wissensobjekte (ST/A/MEC/P/T/MOD) neu angelegt.** Keine Framework-Änderungen. Keine E-Level-Kategoriewechsel (nur Quantifizierungs-Präzisierungen bei MEC-0002, MEC-0021).

**Nächster Schritt:** Weiterhin `00_project/ACADEMIC_RECOVERY_PLAN.md` Tier 1 (AR-001, AR-002) — unverändert höchste Priorität. Alternative (OD-008): ELM/Trust-Formation-Recherchesprint, falls Felix das priorisiert.

---

## Open Decisions Resolution Sprint (2026-07-02)

**Stand: 2026-07-02**

Auslöser: Herausgeberauftrag „OPEN DECISIONS RESOLUTION SPRINT" — reiner Governance-Sprint (ausschließlich Herausgeber-Redaktion an `00_project/OPEN_DECISIONS.md` und den notwendigen Governance-Dateien). Keine neue Recherche, keine neuen Wissensobjekte, keine Framework-Änderungen, keine Academic Recovery.

**Geleistet:**
- Alle acht bestehenden Open Decisions (OD-001–OD-008) einzeln gegen den aktuellen Repository-Zustand geprüft: `00_project/OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`
- OD-001 bis OD-004 auf **DONE** gesetzt (objektiv umgesetzt, mit Belegen aus Session Log/Changelog/Repository-Dateien) — OD-003 mit dokumentierter Restlücke (Repository Health Check nie formalisiert)
- OD-005 auf **ERSETZT** gesetzt → abgelöst durch neue OD-010 (Validierungs-Governance) — Gemini als Instrument wurde nie eingesetzt, die inhaltliche Absicht (externe Validierung) aber über Peer Review Sprints und Academic Recovery bereits weitgehend erfüllt
- OD-006, OD-007 weisungsgemäß **nicht automatisch geschlossen** — geprüft und als entscheidungsreif, aber weiterhin OFFEN bestätigt
- OD-008 geprüft, keine implizite Entscheidung gefunden — bleibt OFFEN
- Drei neue Open Decisions angelegt (langfristige Architekturfragen, keine Forschungsaufgaben): **OD-009** (Framework RC1 / Reifegrad-Statusübergang), **OD-010** (Validierungs-Governance, Nachfolger OD-005), **OD-011** (Literature-Governance — Verhältnis `LITERATURE_INDEX.md` zu `SCIENTIFIC_DEBT.md`/`review_queue.md`)

**Bilanz:** 8 geprüft → 4 DONE, 1 ERSETZT, 3 OFFEN bestätigt → 3 neue OD → 6 aktiv offene Entscheidungen im Repository (OD-006, OD-007, OD-008, OD-009, OD-010, OD-011).

**Keine Wissensobjekte (ST/A/MEC/P/T/MOD) angelegt oder verändert. Keine Framework-Änderungen. Keine inhaltliche Priorität verschoben.**

**Nächster Schritt:** Herausgeber-Entscheidungen zu OD-006 und OD-007 (beide vollständig entscheidungsreif) haben Priorität vor jeder weiteren inhaltlichen Arbeit, da spätere Entscheidung höheren Nacharbeitsaufwand bedeuten würde. Danach unverändert `ACADEMIC_RECOVERY_PLAN.md` Tier 1 (AR-001, AR-002, AR-013). Details und vollständige Empfehlung: `00_project/OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`, Abschnitt 7.

---

## SALES CODEX 1.0 PROGRAM (2026-07-02)

**Stand: 2026-07-02**

Auslöser: Herausgeberauftrag „SALES CODEX 1.0 PROGRAM" — nach Abschluss des Governance Sprints befindet sich der Codex erstmals in einem Zustand, der eine formale Entwicklungsplanung bis Version 1.0 rechtfertigt. Reine Programm-Definition: keine neuen Wissensobjekte, keine neue Recherche, keine Framework-Änderungen, keine Repository-Strukturänderungen, keine Open Decisions geschlossen.

**Geleistet:**
- `00_project/SALES_CODEX_1_0_PROGRAM.md` neu angelegt — zentrales Steuerungsdokument mit 12 Kapiteln (Vision, Mission, Ist-Zustand, 5 Entwicklungsphasen, Qualitätskriterien, Blocker, Nicht-Blocker, Governance nach 1.0, Versionierungsschema, Roadmap, Definition of Done, Executive Summary)
- Fünf Phasen definiert: Governance → Scientific Completion → Architecture Freeze → Release Candidate → Version 1.0
- Zwei echte inhaltliche Blocker identifiziert und priorisiert: W-001 (Teach First vs. Diagnose First, seit Sprint 1 ungelöst) und Publication-Bias-Abhängigkeit der B2B-Kernmethodik (SPIN/Huthwaite, Challenger/CEB, JOLT/Tethr)
- Zwei Governance-Blocker identifiziert: OD-006 (Meme-Filter), OD-007 (CTX-Ebene) — beide entscheidungsreif
- Acht Nicht-Blocker mit Begründung dokumentiert (Domänenlücken, Tier-2–4-Academic-Recovery, MEC-0011-Niedrig-Evidenz als akzeptierte Transparenz statt Mangel, u. a.)
- Versionierungs-Doppeldeutigkeit geklärt: Framework-Version (aktuell 1.1) und Sales-Codex-Gesamtversion (Ziel: 1.0) sind ab sofort zwei getrennte Achsen — operationalisiert die in OD-009 aufgeworfene Frage, ohne sie zu schließen
- Objektive, messbare Definition of Done für Version 1.0 formuliert (Kapitel 11)

**Keine neuen Wissensobjekte, keine neue Recherche, keine Framework-Änderungen, keine Repository-Strukturänderungen, keine Open Decisions geschlossen.**

**Nächster Schritt:** Phase 1 des Programms — Herausgeber-Entscheidungsrunde zu OD-006 bis OD-011 sowie Repository-Hygiene (Duplikat-Ordner, `codex_knowledge_model.md`). Details: `00_project/SALES_CODEX_1_0_PROGRAM.md` Kapitel 4 und 10.

---

## BEHAVIORAL SCIENCE EXPANSION SPRINT 1 (2026-07-02) — ABGESCHLOSSEN

**Stand: 2026-07-02**

Auslöser: Herausgeberauftrag „BEHAVIORAL SCIENCE EXPANSION – SPRINT 1" — wissenschaftlicher Vertiefungssprint innerhalb der Phase "Scientific Completion" des Sales Codex 1.0 Programms. Fünf verhaltenswissenschaftliche Bücher (B-0011–B-0015) vollständig im Book Mode verarbeitet, mit strikter Priorität Kanonisierung vor Neuanlage. Kein Sales-Sprint, kein Codex-Wachstum als Selbstzweck.

**Geleistet:**
- **B-0011 Emotional Intelligence (Goleman, SRC-0011):** 16 ST, 1 A (neu) + A-0013 erweitert, 1 MEC (MEC-0022, Emotional Contagion) + MEC-0010/0011/0020 erweitert, 1 P (neu) + P-0016 erweitert, 1 T (neu). Canonicalization Rate 75,0 %.
- **B-0012 Predictably Irrational (Ariely, SRC-0012):** 31 ST, 4 A (neu) + A-0008 erweitert, 1 MEC (MEC-0023, Zero-Preis-Effekt) + MEC-0002/0005/0009/0018/0021 erweitert, 3 P (neu) + P-0042 erweitert, 1 T (neu), MOD-0010 erweitert. Canonicalization Rate 83,3 %. Autoren-Integritätsrisiko-Kategorie neu eingeführt (Ariely-Datenfälschungskontroverse, differenziert geprüft — Kernexperimente nicht betroffen).
- **B-0013 Nudge: The Final Edition (Thaler & Sunstein, SRC-0013):** 18 ST, 2 A (neu), 1 MEC (MEC-0024, Sludge) + MEC-0002/0006/0008/0015/0021 erweitert, 3 P (neu), 2 T (neu), 1 MOD (MOD-0011, Choice Architecture, neu). Canonicalization Rate 83,3 %. Duplizierte SD-SYS-005-Sektion in `SCIENTIFIC_DEBT.md` durch übergeordnete Session korrigiert (Merge in bestehende kanonische Sektion, keine inhaltliche Änderung).
- **B-0014 Priceless (Poundstone, SRC-0014):** 20 ST, 1 A (neu, A-0056) + A-0048 erweitert, 1 MEC (MEC-0025, Fairness-Verzicht/Ultimatum-Spiel) + MEC-0009/0021 erweitert, 2 P erweitert, 1 T (neu), MOD-0010 erweitert. Canonicalization Rate 66,7 %.
- **B-0015 Made to Stick (Heath & Heath, SRC-0015):** 23 ST, 4 A (neu), 4 MEC (MEC-0026 Curse of Knowledge, MEC-0027 Gap-Theorie der Neugier, MEC-0028 Konkretheits-Encoding, MEC-0029 Narrative Transportation) + MEC-0018 erweitert, 2 P (neu) + P-0036 erweitert, 1 T (neu), 1 MOD (MOD-0012, SUCCESS-Framework, neu). Canonicalization Rate 20,0 % (bewusst niedrig — echte Wissenslückenschließung im zuvor unbesetzten Feld Kommunikationspsychologie, kein Qualitätsmangel).
- **Sprintweite Canonicalization Rate (MEC-basiert): 66,7 %** (16 Erweiterungen / (8 neue MECs + 16 Erweiterungen) × 100).
- `00_project/SCIENTIFIC_DEBT.md` um fünf neue Buchsektionen ergänzt (B-0011 bis B-0015).
- `05_research/LITERATURE_INDEX.md` um ~50 neue verifizierte Quellen ergänzt, inkl. neuer Sektion E "Kommunikationspsychologie, Gedächtnis & Narrativpersuasion" (B-0015). Version 1.1 → 1.2.
- `04_synthesis/SPR-0003_Behavioral_Science_Synthesis/SPR-0003_BEHAVIORAL_SCIENCE_SYNTHESIS.md` neu angelegt — sprintweite Synthese mit 9 Pflichtabschnitten (gemeinsame Erkenntnisse, gestärkte Mechanismen, erweiterte Modelle, notwendige Neumechanismen, Canonicalization Rate, Reifegrad-Veränderung, neue Scientific Debt, neue Tier-1-Kandidaten, Empfehlungen für Version 1.0).
- Codex-Bestand: Mechanismen 21 → 29, Modelle 10 → 12, Statements 201 → 309, Quellen 10 → 15.
- Zwei prominente Replikationsversagen unabhängig recherchiert und transparent dokumentiert statt geglättet: Verschuere et al. (2018, Ten-Commandments-Priming, B-0012) und Maier et al. (2023, Identifiable Victim Effect, B-0015).

**Keine Framework-Änderungen, keine Governance-Entscheidungen, keine Open Decisions geschlossen, keine Repository-Restrukturierung.** Neue Mechanismen ausschließlich mit vollständiger Canonicalization-Rejection-Dokumentation direkt im jeweiligen Objekt.

**Nächster Schritt:** Laut Sprint-Synthese (`SPR-0003_BEHAVIORAL_SCIENCE_SYNTHESIS.md`, Abschnitt 9): Herausgeber-Entscheidung zu möglichem Peer Review von MOD-0011/MOD-0012 (beide neu, Gesamtkonstrukt ungetestet) sowie zur Priorisierung eines B2B-Transfer-Forschungssprints. Ansonsten unverändert `ACADEMIC_RECOVERY_PLAN.md` Tier 1 und Phase-1-Entscheidungsrunde des Sales Codex 1.0 Programms (OD-006 bis OD-011).

---

*Pflichtlektüre beim Session-Start: `PROJECT_BOOTSTRAP.md` + dieses Dokument + `00_project/NEXT_ACTION.md` + `00_project/SALES_CODEX_1_0_PROGRAM.md`*
