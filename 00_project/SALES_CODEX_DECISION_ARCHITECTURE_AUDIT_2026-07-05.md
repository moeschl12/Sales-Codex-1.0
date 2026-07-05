# Sales Codex — Decision Architecture Audit

**Dokumentklasse:** Architecture / Reference
**Rolle bei Erstellung:** Principal AI Systems Architect (Claude Cowork) — nicht Editor, Research Assistant oder Wissensingenieur. Gegenstand ist ausschließlich die Entscheidungsarchitektur, nicht der fachliche Inhalt des Sales Codex.
**Datum:** 2026-07-05
**Stufe:** 2 von 2 der Cowork-Performance-Auditreihe — baut auf `00_project/COWORK_PERFORMANCE_AUDIT_2026-07-05.md` (Stufe 1: Token/Dateiladestrategie) und `00_project/COWORK_TOKEN_OPTIMIZATION_SPRINT_1_REPORT.md` (Umsetzung) auf.
**Status:** Analyse- und Entwurfsdokument. Keine Repository-Ausführung in diesem Schritt — die in Teil 4, 7 und 10 entworfenen Artefakte (`TASK_TYPES.md` u. a.) existieren noch nicht und werden erst nach Freigabe durch Felix in einem Folgesprint angelegt.
**Harte Grenzen eingehalten:** Keine Änderung an `03_knowledge_base/`, `02_sources/`, `04_book_analysis/`, Wissensobjekten, Evidenz-Leveln, Canonical Knowledge Model, Templates oder Framework-Logik.

---

## Analysebasis

Diese Analyse verwendet den Repository-Zustand nach Abschluss von Sprint 1 (verifiziert per Shell: aktuelle `00_project/`-Liste, `02_sources/` inkl. `book_catalog.md`, 15 `04_book_analysis/`-Ordner, 16 Templates in `01_framework/08_templates/`, 11 Templates in `06_research_program/templates/`, `03_knowledge_base/`-Objektzahlen: 309 ST, 60 A, 29 MEC, 57 P, 47 T, 12 MOD, 0 Kompetenzen/Meta-Modelle/Beobachtungen). Zusätzlich einbezogen: `PROJECT_BOOTSTRAP.md` (v1.2, Stand nach Sprint 1), `SESSION_BRIEF.md`, `00_project/NEXT_ACTION.md` (Stand nach Sprint 1), `08_knowledge_atlas/ATLAS_MANIFEST.md`, `00_project/COWORK_EXECUTION_PROTOCOL.md`, `00_project/task_rules.md`.

Nicht erneut geprüft: der fachliche Inhalt der 514 Wissensobjekte selbst — nicht Gegenstand dieser Stufe.

---

## Teil 1 — Entscheidungsanalyse

Für jede Entscheidung: Ursache, Notwendigkeit, Eliminierbarkeit, Methode.

| # | Entscheidung | Warum entsteht sie? | Notwendig? | Eliminierbar? | Wie |
|---|---|---|---|---|---|
| D1 | Welchen Bootstrap-Einstieg lesen? | Vor Sprint 1 gab es vier konkurrierende Dokumente | Nein, sollte fix sein | Ja — bereits größtenteils erledigt in Sprint 1 | `PROJECT_BOOTSTRAP.md` als einziger Einstieg, `CLAUDE_BOOTSTRAP.md` archiviert. Restrisiko: `INDEX.md` widerspricht noch (siehe Sprint-1-Bericht, Grenzfall) |
| D2 | `CURRENT_STATE.md` vollständig oder nur Kopf lesen? | Datei enthält sowohl aktuellen Status als auch volle Sprint-Historie in einer Datei | Nein — Trennung wäre besser | Ja | `SESSION_BRIEF.md` (bereits angelegt) als Standardquelle; Regel „nur bei expliziter Historienfrage vollständig lesen" bereits in `PROJECT_BOOTSTRAP.md` v1.2 verankert, aber nicht technisch erzwungen |
| D3 | Ist `OPEN_DECISIONS.md` für diese Aufgabe relevant? | Datei ist aufgabenabhängig, aber nicht nach Aufgabentyp vorklassifiziert | Ja, die Prüfung ist nötig — aber nicht durch Claude im luftleeren Raum | Ja | Aufgabentyp-Routing (Teil 3): Governance/Release/Audit-Typen laden sie automatisch, alle anderen automatisch nicht |
| D4 | Ist `SCIENTIFIC_DEBT.md` relevant? | Gleiches Muster wie D3 | Ja, aber aufgabentypabhängig | Ja | Gleiche Lösung wie D3 — Routing-Tabelle statt Einzelfallprüfung |
| D5 | Welche Framework-Datei(en) werden gebraucht? | 01_framework/ hat 8 Themenbereiche + 16 Templates; kein direkter Task→Framework-Datei-Zeiger existiert | Ja, Framework-Bezug ist oft nötig | Ja, vollständig | Jeder Task-Typ (Teil 2) definiert seine notwendigen Framework-Dateien explizit — Claude muss nicht mehr ableiten, welche von 8 Unterordnern gemeint ist |
| D6 | Welches Template passt? | 16 Templates in `01_framework/08_templates/`, keine 1:1-Zuordnung zu Task-Typ dokumentiert | Ja | Ja | Feste Zuordnung Task-Typ → Template in Teil 2/3 (z. B. Buchanalyse → `book_analysis_template.md` + Objekttyp-Templates; Governance → `decision_template.md`) |
| D7 | Welche Wissensobjekte sind betroffen (IDs)? | Keine ID→Datei-Index existiert; Zuordnung nur über Dateinamen-Konvention oder Volltextsuche möglich | Ja, aber die Suchmethode ist das Problem, nicht die Frage selbst | Teilweise | `08_knowledge_atlas/output/nodes.csv`/`edges.csv` bereits vorhanden, aber nicht als Standard-Nachschlagemechanismus etabliert (siehe Performance Audit, Tokenfresser #10). Langfristig: Objekt-Index (Teil 9) |
| D8 | Muss ein Verzeichnis rekursiv durchsucht werden? | Ohne explizite Vorgabe im Prompt muss Claude selbst abwägen, ob ein Scan nötig ist | Manchmal ja (z. B. Konsistenzprüfung) | Ja, für die meisten Task-Typen | Explizite Erlaubte-/Verbotene-Suchoperationen pro Task-Typ (Teil 3) statt Einzelfallabwägung |
| D9 | Muss historischer Kontext (`SESSION_LOG.md`, alte Berichte) geladen werden? | Kein Task-Typ definiert bisher, ob Historie gebraucht wird | Nur bei wenigen Task-Typen (Audit, Postmortem) | Ja | Routing-Tabelle: nur T6 (Audit) und explizite Historienfragen laden `SESSION_LOG.md` automatisch |
| D10 | Welche Rolle/welchen Arbeitsmodus einnehmen, wenn der Prompt keine nennt? | Prompts variieren in Vollständigkeit; frühere Sprints zeigten, dass explizite Rollenbindung Scope-Kriechen verhindert (Performance Audit, Abschnitt 5) | Ja, Rollenklärung ist nötig | Ja, fast vollständig | Jeder Task-Typ hat einen Standard-Arbeitsmodus (Teil 3); Prompt muss nur noch den Typ nennen (Teil 7), nicht die Rolle neu erfinden |
| D11 | In welchem Format ausgeben (Template vs. Freitext vs. Bericht)? | Nicht jeder Prompt spezifiziert das Ausgabeformat | Ja | Ja, vollständig | Standard-Ausgabeformat ist Teil der Task-Typ-Definition (Teil 2/3), nicht mehr Claude überlassen |
| D12 | Wann anhalten und rückfragen vs. mit ⚠ weiterarbeiten? | Abbruchbedingungen bisher nur generisch in `PROJECT_BOOTSTRAP.md` definiert, nicht aufgabentypspezifisch | Ja | Teilweise | Generische Abbruchbedingungen bleiben Basis; aufgabentypspezifische Ergänzungen in Teil 7-Templates (z. B. Release: zusätzlich „Freeze-Verletzung erkannt") |
| D13 | Welche Verzeichnisse dürfen überhaupt betreten werden? | Kein Verzeichnis-Allowlisting existiert; Claude entscheidet implizit anhand der Aufgabenbeschreibung | Ja | Ja, vollständig | Directory Routing (Teil 8): jede Aufgabe nennt ihre erlaubten Verzeichnisse als geschlossene Liste |

**Kernbefund:** 11 von 13 identifizierten Entscheidungen sind vollständig eliminierbar, sofern jede Aufgabe einen deklarierten Task-Typ trägt (Teil 2–4, 7). Die verbleibenden zwei (D7 — Objekt-ID-Auflösung ohne Index; D9 teilweise) sind erst durch zusätzliche Infrastruktur (Teil 9) vollständig lösbar, nicht durch Regeln allein.

---

## Teil 2 — Task-Klassifizierung (Taxonomie)

Bewusst 12 Typen statt mehr: „Bugfix" und „Refactoring" aus der Beispiel-Liste sind keine eigenständigen Typen im Sales Codex, sondern Unterfälle von T3 bzw. T4 (Begründung: reale Sprints wie die ED-001–008-Umsetzung waren strukturell Repository-Wartung, keine eigene Kategorie mit eigenem Datei-/Suchmuster). Weniger, klar getrennte Typen reduzieren selbst wieder eine Entscheidung (welcher von mehreren ähnlichen Typen zutrifft).

### T1 — Buchanalyse (Book Mode)
- **Ziel:** Ein Buch vollständig durch die Wissenspipeline (SRC→ST→A→MEC→P→T→MOD) verarbeiten.
- **Typische Dateien:** `02_sources/book_catalog.md`, `02_sources/books/SRC-XXXX_*.md`, `04_book_analysis/<Titel>/analysis.md`, betroffene `03_knowledge_base/*`-Objekte mit dieser Source-ID.
- **Typische Suchoperationen:** Gezielte ID-Suche (Source-ID-Filter), kein repositoryweiter Scan.
- **Typische Risiken:** Canonicalisierung gegen bestehende MECs/Prinzipien übersehen; Sequenzfehler (P vor MEC angelegt, siehe Pilot-001-Lektion in `COWORK_EXECUTION_PROTOCOL.md`).
- **Notwendige Framework-Dateien:** `01_framework/08_templates/` (alle Objekttyp-Templates + `book_analysis_template.md`), `01_framework/01_methodology/codex_methodology.md`, `01_framework/04_principle_extraction/principle_extraction_standard.md`.
- **Notwendige Wissensobjekte:** Nur Objekte mit derselben Source-ID; zur Canonicalisierung zusätzlich bestehende MEC/P-Objekte gleichen Themenfelds (idealerweise über Atlas, nicht Volltextscan).

### T2 — Framework-Arbeit
- **Ziel:** Methodik, Evidenzsystem, Canonical Knowledge Model oder Templates ändern/erweitern.
- **Typische Dateien:** `01_framework/**`, ggf. `00_project/task_rules.md`, `00_project/SALES_CODEX_OPERATING_MANUAL.md`.
- **Typische Suchoperationen:** Keine Suche über `03_knowledge_base/`, außer explizit zur Folgenabschätzung angefordert.
- **Typische Risiken:** Rückwirkende Inkonsistenz mit bestehenden Objekten, wenn Änderung nicht gegen Bestand geprüft wird.
- **Notwendige Framework-Dateien:** je nach Änderung — das betroffene Unterverzeichnis von `01_framework/`.
- **Notwendige Wissensobjekte:** keine, außer explizite Folgenabschätzung beauftragt.

### T3 — Repository-Wartung / Hygiene (inkl. „Bugfix")
- **Ziel:** Tote Links, Duplikate, falsche Pfade, Ordnungsprobleme beheben — ohne inhaltliche Bewertung.
- **Typische Dateien:** genau die betroffenen Dateien, plus die Datei, die den Fehler ursprünglich dokumentiert hat (z. B. Auditbericht).
- **Typische Suchoperationen:** gezielte Cross-Reference-Prüfung der explizit genannten Dateien; kein repositoryweiter Scan ohne Freigabe.
- **Typische Risiken:** Scope-Kriechen zu „während ich dabei bin, das auch noch" — genau das, was `RC1_FREEZE_DECLARATION.md` und mehrere Sprintberichte ausdrücklich verbieten.
- **Notwendige Framework-Dateien:** keine, außer die Wartung betrifft Framework-Dateien selbst.
- **Notwendige Wissensobjekte:** nur falls die Wartung selbst Wissensobjekte betrifft (z. B. Feldnamen-Harmonisierung, wie im Final Pre-Release Sprint).

### T4 — Architekturarbeit (inkl. „Refactoring")
- **Ziel:** Struktur-, Ordner-, Versionierungs- oder Prozessfragen bewerten und Vorschläge entwerfen — wie dieses Dokument selbst.
- **Typische Dateien:** Verzeichnisstruktur (Metadaten, nicht Volltext), betroffene Governance-Dateien.
- **Typische Suchoperationen:** `find`/`ls` (Struktur-Scan) erlaubt, Volltextlesen nur gezielt.
- **Typische Risiken:** Vorschlag ohne Freigabe umgesetzt (Architekturarbeit ist per Definition zweistufig: Entwurf, dann separate Freigabe zur Umsetzung).
- **Notwendige Framework-Dateien:** abhängig vom Thema, meist `01_framework/00_charter/`, `00_project/SALES_CODEX_OPERATING_MANUAL.md`.
- **Notwendige Wissensobjekte:** keine.

### T5 — Review / Validierung (VAL)
- **Ziel:** Konsistenz eines abgeschlossenen Buchs/Objektbereichs prüfen, VAL-Report erstellen.
- **Typische Dateien:** die zu prüfenden Objekte + `01_framework/08_templates/validation_report_template.md`.
- **Typische Suchoperationen:** Referenzprüfung über `08_knowledge_atlas/output/edges.csv`, nicht durch Einzelöffnen aller verlinkten Dateien.
- **Typische Risiken:** Reviewer korrigiert Inhalte statt sie nur zu befunden (Vermischung mit T3).
- **Notwendige Framework-Dateien:** `01_framework/02_evidence_system/evidence_system.md`.
- **Notwendige Wissensobjekte:** exakt der zu prüfende Bereich.

### T6 — Audit
- **Ziel:** Repositoryweite, rein lesende Bewertung (z. B. `CODEX_AUDIT_2026-07.md`).
- **Typische Dateien:** breit, potenziell alle Ordner — das ist der einzige Task-Typ, bei dem ein größerer Scan strukturell notwendig ist.
- **Typische Suchoperationen:** repositoryweite Struktur-/Stichprobenprüfung ausdrücklich erlaubt, aber mit Enddatum/Scope-Grenze im Auftrag.
- **Typische Risiken:** unbegrenzter Scope, keine Abgrenzung von „Stichprobe" vs. „Vollprüfung" (siehe Tokenfresser-Analyse, Stufe 1).
- **Notwendige Framework-Dateien:** alle, sofern der Audit sie bewertet — sollte im Auftrag benannt werden.
- **Notwendige Wissensobjekte:** Stichprobe, nicht zwingend alle 514.

### T7 — Konsistenzprüfung (gezielt, regelbasiert)
- **Ziel:** Eine einzelne, klar definierte Regel repositoryweit prüfen (z. B. „referenziert jedes P ≥ 2 MECs?").
- **Typische Dateien:** nur der betroffene Objekttyp-Ordner.
- **Typische Suchoperationen:** rekursiver Scan über genau diesen einen Ordner ist für diesen Typ die Regel, nicht die Ausnahme — sollte im Routing als Standard erlaubt sein (im Unterschied zu T1/T3).
- **Typische Risiken:** Regel wird informell erweitert („während ich prüfe, fällt mir noch X auf") — Befund dokumentieren, nicht spontan zusätzliche Regeln prüfen.
- **Notwendige Framework-Dateien:** die Datei, die die geprüfte Regel definiert (z. B. `canonical_knowledge_model.md`).
- **Notwendige Wissensobjekte:** der gesamte geprüfte Objekttyp-Ordner.

### T8 — Governance / Decision Resolution
- **Ziel:** Offene Entscheidungen (`OPEN_DECISIONS.md`) durch den Herausgeber klären lassen und Ergebnis dokumentieren; Editor Decisions verfassen.
- **Typische Dateien:** `00_project/OPEN_DECISIONS.md`, `01_framework/08_templates/decision_template.md`, ggf. `06_research_program/templates/EDITOR_DECISION_TEMPLATE.md`.
- **Typische Suchoperationen:** keine — Governance-Arbeit ist redaktionell, nicht suchbasiert.
- **Typische Risiken:** neue Entscheidung wird als bereits getroffen behandelt, ohne Herausgeber-Freigabe.
- **Notwendige Framework-Dateien:** keine zwingend.
- **Notwendige Wissensobjekte:** nur falls eine Entscheidung ein spezifisches Objekt betrifft.

### T9 — Release / Freeze
- **Ziel:** Versionsstand einfrieren, Release-Dokumente erstellen, formalen Abschluss dokumentieren.
- **Typische Dateien:** `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, Zähl-Grundlagen (`REPOSITORY_KPIS.md`), Zieldateien im neu zu benennenden Release-Namensraum.
- **Typische Suchoperationen:** direkte Dateisystemzählung (z. B. Objektzahlen), keine inhaltliche Bewertung.
- **Typische Risiken:** Vermischung mit T6 (Audit) — Release-Sprints sollen zusammenfassen, nicht neu bewerten.
- **Notwendige Framework-Dateien:** keine inhaltlichen, nur Zähl-/Statusreferenzen.
- **Notwendige Wissensobjekte:** keine einzelnen, nur aggregierte Zahlen.

### T10 — Research Project (W-xxx Lifecycle)
- **Ziel:** Ein Forschungsprojekt durch die 9-stufige Research-Lifecycle-Architektur führen (`06_research_program/RESEARCH_LIFECYCLE.md`).
- **Typische Dateien:** `06_research_program/active/<W-xxx>/` bzw. `completed/<W-xxx>/`, die 11 Templates in `06_research_program/templates/`.
- **Typische Suchoperationen:** projektlokal, kein repositoryweiter Bezug außer bei Stufe 8 (Repository Integration).
- **Typische Risiken:** Integration betroffener Wissensobjekte ohne vorherige Editor Decision (Stufenreihenfolge verletzt).
- **Notwendige Framework-Dateien:** `06_research_program/RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md`.
- **Notwendige Wissensobjekte:** nur in Stufe 8, und nur die im Editor-Decision-Dokument benannten.

### T11 — Scientific Debt / Academic Recovery
- **Ziel:** Belegdefizite systematisch schließen (Literaturrecherche, Tier-Klassifikation).
- **Typische Dateien:** `00_project/SCIENTIFIC_DEBT.md`, `00_project/ACADEMIC_RECOVERY_PLAN.md`, `05_research/LITERATURE_INDEX.md`.
- **Typische Suchoperationen:** externe Recherche (Websuche), keine interne Volltextsuche.
- **Typische Risiken:** neue Wissensobjekte statt Erweiterung bestehender angelegt (Verstoß gegen Canonicalisierungsprinzip).
- **Notwendige Framework-Dateien:** `01_framework/02_evidence_system/evidence_system.md`.
- **Notwendige Wissensobjekte:** nur die explizit im Plan benannten (z. B. AR-001, AR-002).

### T12 — Publikationsarbeit (vorbereitet, noch nicht aktiv)
- **Ziel:** Wissensbasis in Buch/Workbook/Training/Vortrag überführen. Ordnerstruktur (`05_publications/sales_codex_book/`, `talks/`, `trainings/`, `workbook/`) existiert bereits, ist aber leer — noch kein realer Sprint dieses Typs durchgeführt.
- **Typische Dateien:** aggregierte, bereits validierte Wissensobjekte (nur `Status: Validiert`, keine Entwürfe).
- **Typische Suchoperationen:** thematische Zusammenstellung über mehrere Objekttypen — vermutlich der Task-Typ mit dem höchsten legitimen Suchbedarf, da querschnittlich.
- **Typische Risiken:** Vermischung von Wissensextraktion (T1) und Publikationsredaktion — Publikationsarbeit sollte nichts an `03_knowledge_base/` ändern, nur daraus lesen.
- **Notwendige Framework-Dateien:** noch nicht definiert — Lücke, siehe Teil 10.
- **Notwendige Wissensobjekte:** breite, aber rein lesende Auswahl.

---

## Teil 3 — Decision Routing pro Task-Typ

| Task-Typ | Immer laden | Optional laden | Niemals automatisch laden | Erlaubte Suche | Verbotene Suche | Ausgabeformat | Arbeitsmodus |
|---|---|---|---|---|---|---|---|
| T1 Buchanalyse | `SESSION_BRIEF.md`, `02_sources/book_catalog.md`, `02_sources/books/SRC-XXXX*`, betroffene Objekttyp-Templates | `04_book_analysis/<Titel>/analysis.md` (falls vorhanden) | `OPEN_DECISIONS.md`, `SCIENTIFIC_DEBT.md`, andere Bücher | Source-ID-gefilterte Suche in `03_knowledge_base/` | Volltextscan über andere Bücher „zur Inspiration" | Wissensobjekte nach Template | Editor / Wissensextraktion |
| T2 Framework-Arbeit | `SESSION_BRIEF.md`, betroffene `01_framework/`-Datei(en) | `canonical_knowledge_model.md` zur Konsistenzprüfung | `03_knowledge_base/` (außer Folgenabschätzung beauftragt) | keine | Scan über `03_knowledge_base/` ohne Auftrag | Änderungsvorschlag mit Begründung | Framework-Architekt (nur mit Freigabe) |
| T3 Wartung/Hygiene | `SESSION_BRIEF.md`, die explizit genannte(n) Datei(en) | Referenzdatei zur Prüfung der Korrektheit | alles außerhalb der genannten Dateien | Cross-Reference-Check der genannten Dateien | jeder Scan über nicht genannte Ordner | Kurzdiff im Chat | Editor, punktuelle Änderung |
| T4 Architekturarbeit | `SESSION_BRIEF.md`, Verzeichnisstruktur (Metadaten) | betroffene Governance-Dateien | Volltext aller Dateien pauschal | `find`/`ls` (Struktur) | Umsetzung ohne zweite Freigabe | Vorschlag mit Vor-/Nachteilen | Systemarchitekt (Entwurf, keine Ausführung) |
| T5 Review/VAL | `SESSION_BRIEF.md`, zu prüfende Objekte, `validation_report_template.md` | `evidence_system.md` | andere Objekttypen/Bücher | Referenzprüfung via Atlas-Output | Einzelöffnen aller verlinkten Dateien statt Atlas | VAL-Report nach Template | Reviewer, kein Autor |
| T6 Audit | `SESSION_BRIEF.md`, Verzeichnisstruktur, im Auftrag benannte Bereiche | Stichprobe aus `03_knowledge_base/` | — (Audit ist der einzige Typ ohne Pauschalverbot) | repositoryweite Struktur-/Stichprobenprüfung, mit Scope-Enddatum im Auftrag | Vollprüfung aller 514 Objekte ohne expliziten Auftrag dazu | Auditbericht mit Methodikabschnitt | Unabhängiger Auditor, rein lesend |
| T7 Konsistenzprüfung | `SESSION_BRIEF.md`, der geprüfte Objekttyp-Ordner, die regeldefinierende Framework-Datei | `08_knowledge_atlas/output/*.csv` | andere Objekttypen | rekursiver Scan über genau den einen geprüften Ordner (Standard, nicht Ausnahme) | Korrektur ohne separate Freigabe | Befundliste (Datei, Regelverstoß) | Auditor, nur Befund, keine Korrektur |
| T8 Governance | `SESSION_BRIEF.md`, `OPEN_DECISIONS.md`, `decision_template.md` | betroffenes Einzelobjekt | `03_knowledge_base/` breit | keine | jede Suche außerhalb der genannten Entscheidung | Decision-Dokument nach Template | Redakteur, keine Herausgeberentscheidung |
| T9 Release/Freeze | `CURRENT_STATE.md` (Kopf), `NEXT_ACTION.md`, `REPOSITORY_KPIS.md` | `SCIENTIFIC_DEBT.md`-Zeilenzahl (nur Zählung) | inhaltliche Neubewertung einzelner Objekte | Dateisystemzählung (`find`/`wc`) | inhaltliche Bewertung (das ist T6, nicht T9) | Release-Dokument nach etabliertem Muster | Release Manager, keine fachliche Bewertung |
| T10 Research Project | `06_research_program/RESEARCH_LIFECYCLE.md`, projektlokaler Ordner | `RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md` | `03_knowledge_base/` breit (außer Stufe 8) | projektlokal | Integration ohne vorherige Editor Decision (Stufe 7) | passendes Template je Lifecycle-Stufe | je Stufe unterschiedlich, siehe `RESEARCH_LIFECYCLE.md` |
| T11 Scientific Debt | `SCIENTIFIC_DEBT.md`, `ACADEMIC_RECOVERY_PLAN.md` | `LITERATURE_INDEX.md` | Objekte außerhalb des Plans | externe Websuche | interne Volltextsuche als Ersatz für Recherche | Erweiterung bestehender Objekte, Plan-Update | Rechercheur, keine neuen Objekte ohne Plan-Bezug |
| T12 Publikation | `SESSION_BRIEF.md`, thematisch benannte, validierte Objekte | — | Entwurfsobjekte (Status ≠ „Validiert") | thematische Mehrfachsuche innerhalb `03_knowledge_base/`, rein lesend | jede Schreiboperation in `03_knowledge_base/` | Publikations-Textentwurf | Lektor/Autor für Zielformat, liest nur |

---

## Teil 4 — Repository Routing: Bewertung der Optionen

| Option | Bewertung |
|---|---|
| `TASK_ROUTER.md` | Name suggeriert aktive Ausführungslogik (Router = Code, der etwas tut). Es gibt in Cowork keinen Ausführungsmechanismus, der eine Datei automatisch „routet" — jede Nutzung ist ein manueller Lesevorgang durch Claude. Der Name würde eine Automatisierung versprechen, die nicht existiert. **Nicht empfohlen.** |
| `SESSION_PROFILE.md` | Klingt nach einem *pro Session generierten* Zustand (wie ein Profil, das befüllt wird). Falls persistent im Repository gepflegt, würde es zu einer weiteren wachsenden, historisierenden Datei (gleiches Muster wie das ursprüngliche `NEXT_ACTION.md`-Problem aus Stufe 1). **Nicht empfohlen** als Repository-Datei; als Chat-interne, nicht persistierte Kurzangabe am Sessionanfang aber sinnvoll (siehe Teil 7). |
| `TASK_TYPES.md` | Statische Nachschlagetabelle (Referenzcharakter), keine Ausführungslogik unterstellt. Enthält exakt die Tabelle aus Teil 2/3 dieses Dokuments. Wird nur konsultiert, wenn eine Aufgabe **keinen** Typ deklariert oder der Scope unklar ist. **Empfohlen.** |

**Empfehlung:** `TASK_TYPES.md`, Klasse „Reference", Ablageort: Repository-Root (parallel zu `PROJECT_BOOTSTRAP.md` und `SESSION_BRIEF.md`, da es von `PROJECT_BOOTSTRAP.md` aus verlinkt werden soll). Die eigentliche Entscheidungsverlagerung passiert jedoch nicht durch die Existenz dieser Datei allein, sondern dadurch, dass **Prompts selbst den Task-Typ deklarieren** (Teil 7) — dann muss `TASK_TYPES.md` in den meisten Sessions gar nicht gelesen werden, weil der Prompt die Routing-Zeile bereits mitliefert. `TASK_TYPES.md` ist der Fallback für unvollständige Prompts, nicht der Regelfall.

**Wichtig:** Die Erstellung von `TASK_TYPES.md` ist in diesem Dokument nur entworfen (Inhalt = Teil 2/3-Tabellen), nicht ausgeführt. Umsetzung ist Sprint-2-Maßnahme (Teil 10).

---

## Teil 5 — Decision Budget pro Task-Typ

Gezählt werden: Dateientscheidungen (welche Datei zusätzlich zur Pflichtliste laden?), Suchentscheidungen (scannen ja/nein, wie breit?), Kontextentscheidungen (historischen Kontext laden ja/nein?).

| Task-Typ | Dateientscheidungen (max.) | Suchentscheidungen (max.) | Kontextentscheidungen (max.) | Begründung |
|---|---|---|---|---|
| T1 Buchanalyse | 1 (Template-Wahl je Objekttyp, aus fester Liste) | 1 (Source-ID-Filter ja/nein) | 0 | Vollständig vorstrukturiert durch die Pipeline-Reihenfolge |
| T2 Framework-Arbeit | 2 | 1 | 0 | Themenbereich meist vom Auftrag benannt |
| T3 Wartung/Hygiene | 0 | 0 | 0 | Auftrag sollte Datei(en) bereits vollständig benennen — jede Entscheidung hier ist ein Prompt-Mangel, kein Claude-Ermessen |
| T4 Architekturarbeit | 3 | 2 | 1 | Offener Charakter der Aufgabe erlaubt mehr Ermessen, aber mit Obergrenze |
| T5 Review/VAL | 1 | 1 | 0 | Scope durch zu prüfenden Bereich fest vorgegeben |
| T6 Audit | 4 | 3 | 2 | Einziger Typ mit strukturell breitem Scope — Budget bewusst höher |
| T7 Konsistenzprüfung | 0 | 0 (Scanumfang ist durch Regel vorgegeben) | 0 | Vollständig regelgetrieben |
| T8 Governance | 1 | 0 | 0 | Rein redaktionell |
| T9 Release/Freeze | 2 | 0 | 1 (Vorgängerbericht als Basis ja/nein) | Zählbasiert, wenig Ermessen |
| T10 Research Project | 1 (welches Template der aktuellen Stufe) | 0 | 0 | Lifecycle gibt Stufe und Template vor |
| T11 Scientific Debt | 1 | 0 (Recherche ist extern, kein internes Suchbudget) | 0 | Plan gibt Prioritäten vor |
| T12 Publikation | 3 | 2 | 0 | Querschnittlich, daher etwas höheres Budget |

**Faustregel:** Jede Entscheidung über dem Budget ist ein Indiz für einen unterspezifizierten Prompt, nicht für einen komplexen Task-Typ — mit Ausnahme von T4 und T6, die strukturell offener sind.

---

## Teil 6 — Context Budget

Grobe Schätzung, ≈ 4 Zeichen/Token, auf Basis der tatsächlichen Dateigrößen nach Sprint 1.

### Sessionstart (fix, für praktisch jede Session)

| Komponente | Datei | Token (≈) | Begründung |
|---|---|---|---|
| Bootstrap | `PROJECT_BOOTSTRAP.md` | ≈ 1.900 | Aktuelle Größe nach Sprint-1-Erweiterung (Dokumentklassifizierung v1.2) |
| Session Brief | `SESSION_BRIEF.md` | ≈ 420 | 28 Zeilen, angelegt in Sprint 1 |
| Next Action | `00_project/NEXT_ACTION.md` | ≈ 1.100 | 46 Zeilen nach Sprint-1-Kürzung |
| **Zwischensumme Sessionstart** | | **≈ 3.400** | Fix, unabhängig vom Task-Typ |

### Variabler Task-Anteil (abhängig von Task-Typ, Teil 3)

| Komponente | Spanne (≈ Token) | Begründung |
|---|---|---|
| Framework | 0 (T3, T7, T8, T9, T11) bis ≈ 2.500 (T2, mehrere Framework-Dateien) | `01_framework/`-Dateien sind klein (größte: `canonical_knowledge_model.md`, 340 Zeilen ≈ 2.200 Token), aber Anzahl variiert |
| Task-spezifische Dateien | ≈ 500 (T3, punktuelle Änderung) bis ≈ 15.000 (T6 Audit, breiter Scope) | Größte Spreizung aller Kategorien — T6 ist bewusst die Ausnahme |
| Knowledge Objects | 0 (T2, T4, T8, T9) bis ≈ 850 × N (T1, T5, T7, T12) | Einzelobjekt ≈ 850 Token (Ø aus Stichprobe, 03_knowledge_base/, 1,74 MB / 514 Objekte ≈ 3.380 Byte/Objekt) |

### Beispielrechnung pro Task-Typ (Gesamt inkl. Sessionstart)

| Task-Typ | Framework | Task-Dateien | Knowledge (N Objekte) | Gesamt (≈) |
|---|---|---|---|---|
| T1 Buchanalyse (1 Kapitel, ~8 neue Objekte) | ≈ 900 (Templates) | ≈ 600 (SRC + analysis.md-Auszug) | ≈ 6.800 (8 × 850) | ≈ 11.700 |
| T3 Wartung (1 Datei) | 0 | ≈ 500 | 0 | ≈ 3.900 |
| T5 Review (1 Buch, ~35 Objekte) | ≈ 600 | ≈ 300 | ≈ 6.000 (Referenzprüfung, nicht Volltext aller — via Atlas ≈ 200/Objekt statt 850) | ≈ 8.500 |
| T6 Audit (repositoryweite Stichprobe) | ≈ 2.500 | ≈ 12.000 | ≈ 4.250 (5 Stichprobenobjekte je Typ) | ≈ 22.150 |
| T7 Konsistenzprüfung (1 Objekttyp, z. B. alle 57 P) | ≈ 400 | 0 | ≈ 48.450 (57 × 850, voller Ordner ist hier Standard) | ≈ 52.250 |
| T9 Release | 0 | ≈ 2.000 | 0 (nur Zählung) | ≈ 5.400 |

**Begründung der Ausreißer:** T7 (Konsistenzprüfung) ist teuer, weil der volle Objekttyp-Ordner strukturell notwendig ist (Regel gilt für alle Objekte des Typs) — hier ist die Größe sachlich begründet, kein Optimierungsziel. T6 (Audit) ist die einzige Kategorie mit offenem Scope; das Decision Budget (Teil 5) begrenzt hier nicht den Umfang, sondern nur die Anzahl freier Ermessensentscheidungen dabei.

---

## Teil 7 — Prompt Routing: Produktionsreife Vorlagen

Jede Vorlage trägt eine `TASK_TYPE`-Zeile, die den Task-Typ explizit deklariert — das ist der zentrale Mechanismus, der D10–D13 aus Teil 1 eliminiert, ohne dass Claude den Typ erst erschließen muss.

**T1 — Buchanalyse**
```
TASK_TYPE: T1_BUCHANALYSE
ZIEL: Buch <Titel> (SRC-XXXX) — Kapitel <X>–<Y> durch die Pipeline verarbeiten.
ROLLE: Editor, Wissensextraktion.
ERLAUBTE DATEIEN: 02_sources/book_catalog.md, 02_sources/books/SRC-XXXX*,
04_book_analysis/<Titel>/, 03_knowledge_base/*-Objekte mit Source-ID SRC-XXXX,
01_framework/08_templates/*.
VERBOTENE DATEIEN: OPEN_DECISIONS.md, SCIENTIFIC_DEBT.md, andere Bücher.
SUCHGRENZE: Nur Source-ID-gefilterte Suche. Kein Scan über andere Bücher.
ÄNDERUNGSGRENZE: Nur neue Objekte mit dieser Source-ID, keine Änderung an
bestehenden Objekten außerhalb der Canonicalisierung.
AUSGABEFORMAT: Wissensobjekte nach Template. Chat: Anzahl neuer Objekte + nächster Schritt.
ABBRUCHBEDINGUNGEN: Primärquelle fehlt; Canonicalisierungskonflikt unauflösbar.
```

**T2 — Framework-Arbeit**
```
TASK_TYPE: T2_FRAMEWORK
ZIEL: <konkrete Framework-Frage/Änderung>, vorab von Felix freigegeben.
ROLLE: Framework-Architekt (nur mit dieser expliziten Freigabe).
ERLAUBTE DATEIEN: 01_framework/<betroffener Unterordner>/, betroffene Templates.
VERBOTENE DATEIEN: 03_knowledge_base/ (außer Folgenabschätzung separat beauftragt).
SUCHGRENZE: Keine Suche ohne expliziten Zusatzauftrag.
ÄNDERUNGSGRENZE: Nur die benannte Framework-Datei, keine rückwirkende
Änderung bestehender Wissensobjekte.
AUSGABEFORMAT: Änderungsvorschlag mit Begründung, keine Direktänderung ohne
zweite Bestätigung.
ABBRUCHBEDINGUNGEN: Framework-Widerspruch zu bestehendem Wissensmodell erkannt.
```

**T3 — Repository-Wartung / Hygiene**
```
TASK_TYPE: T3_WARTUNG
ZIEL: <eine konkrete Korrektur an einer benannten Datei/einem benannten Link>.
ROLLE: Editor, punktuelle Korrektur.
ERLAUBTE DATEIEN: Ausschließlich die genannte(n) Datei(en).
VERBOTENE DATEIEN: Alles außerhalb der genannten Dateien, auch wenn „verwandt".
SUCHGRENZE: Keine — Datei ist bereits benannt.
ÄNDERUNGSGRENZE: Nur die genannte Korrektur, keine weiteren Verbesserungen
„nebenbei".
AUSGABEFORMAT: Kurzdiff im Chat, keine Zusammenfassung des gesamten Dateiinhalts.
ABBRUCHBEDINGUNGEN: Datei existiert nicht wie beschrieben.
```

**T4 — Architekturarbeit**
```
TASK_TYPE: T4_ARCHITEKTUR
ZIEL: <konkrete Architekturfrage>.
ROLLE: Systemarchitekt — Entwurf, keine Ausführung ohne zweite Freigabe.
ERLAUBTE DATEIEN: Verzeichnisstruktur (Metadaten), betroffene Governance-Dateien.
VERBOTENE DATEIEN: Volltext aller Dateien pauschal.
SUCHGRENZE: find/ls (Struktur) erlaubt, gezieltes Volltextlesen nur bei Bedarf.
ÄNDERUNGSGRENZE: Keine Ausführung des Vorschlags in diesem Schritt.
AUSGABEFORMAT: Vorschlag mit Vor-/Nachteilen und Aufwand/Risiko/Nutzen.
ABBRUCHBEDINGUNGEN: Vorschlag würde bestehende Governance-Entscheidung widersprechen.
```

**T5 — Review / Validierung**
```
TASK_TYPE: T5_REVIEW
ZIEL: Konsistenzreview für <Buch/Objekttyp/Bereich>, Ergebnis als VAL-Report.
ROLLE: Reviewer, kein Autor.
ERLAUBTE DATEIEN: Zu prüfende Objekte, 01_framework/08_templates/validation_report_template.md,
08_knowledge_atlas/output/edges.csv.
VERBOTENE DATEIEN: Andere Objekttypen/Bücher.
SUCHGRENZE: Referenzprüfung über edges.csv, kein Einzelöffnen aller verlinkten Dateien.
ÄNDERUNGSGRENZE: Keine inhaltlichen Korrekturen — nur Befund, gekennzeichnet.
AUSGABEFORMAT: VAL-Report nach Template.
ABBRUCHBEDINGUNGEN: Referenzintegrität so beschädigt, dass Review nicht sinnvoll möglich ist.
```

**T6 — Audit**
```
TASK_TYPE: T6_AUDIT
ZIEL: <Auditgegenstand und Scope-Grenze, z. B. "Evidenzfelder aller 57 Prinzipien,
Stichprobe von 15">.
ROLLE: Unabhängiger Auditor, rein lesend.
ERLAUBTE DATEIEN: Im Auftrag benannter Bereich + Verzeichnisstruktur.
VERBOTENE DATEIEN: Keine Änderungen an irgendeiner Datei.
SUCHGRENZE: Repositoryweite Struktur-/Stichprobenprüfung erlaubt, aber mit
der im Auftrag benannten Scope-Grenze — kein unbegrenzter Vollscan ohne diese Angabe.
ÄNDERUNGSGRENZE: Keine.
AUSGABEFORMAT: Auditbericht mit explizitem Methodikabschnitt (was wurde
tatsächlich geprüft, was nicht).
ABBRUCHBEDINGUNGEN: Scope-Grenze im Auftrag fehlt — dann zuerst rückfragen,
nicht mit unbegrenztem Scope beginnen.
```

**T7 — Konsistenzprüfung**
```
TASK_TYPE: T7_KONSISTENZ
ZIEL: Prüfen, ob <konkrete Regel> für alle Objekte des Typs <ST/A/MEC/P/T/MOD>
eingehalten wird.
ROLLE: Auditor, nur Befund.
ERLAUBTE DATEIEN: 03_knowledge_base/<Objekttyp>/ vollständig (Standard für
diesen Task-Typ, siehe Teil 3), regeldefinierende Framework-Datei.
VERBOTENE DATEIEN: Andere Objekttypen.
SUCHGRENZE: Rekursiver Scan über den genannten Ordner ist Standard für
diesen Auftrag — keine erneute Freigabe pro Session nötig.
ÄNDERUNGSGRENZE: Keine Korrektur ohne separaten Folgeauftrag.
AUSGABEFORMAT: Befundliste (Datei, Regelverstoß), keine Datei ändern.
ABBRUCHBEDINGUNGEN: Regel selbst widersprüchlich zur Framework-Datei.
```

**T8 — Governance / Decision Resolution**
```
TASK_TYPE: T8_GOVERNANCE
ZIEL: <konkrete offene Entscheidung, z. B. OD-XXX> klären/dokumentieren.
ROLLE: Redakteur, keine eigene Herausgeberentscheidung.
ERLAUBTE DATEIEN: 00_project/OPEN_DECISIONS.md, 01_framework/08_templates/decision_template.md.
VERBOTENE DATEIEN: 03_knowledge_base/ breit.
SUCHGRENZE: Keine.
ÄNDERUNGSGRENZE: Nur die benannte Entscheidung, keine Statusänderung anderer
Entscheidungen.
AUSGABEFORMAT: Decision-Dokument nach Template.
ABBRUCHBEDINGUNGEN: Entscheidung erfordert Information, die nicht im Repository steht.
```

**T9 — Release / Freeze**
```
TASK_TYPE: T9_RELEASE
ZIEL: <Release-/Freeze-Schritt gemäß Release Plan>.
ROLLE: Release Manager / Configuration Manager — keine fachliche Bewertung.
ERLAUBTE DATEIEN: CURRENT_STATE.md, NEXT_ACTION.md, REPOSITORY_KPIS.md,
Zieldateiname im Release-Namensraum.
VERBOTENE DATEIEN: Inhaltliche Neubewertung einzelner Wissensobjekte (das ist T6).
SUCHGRENZE: Dateisystemzählung (find/wc), keine inhaltliche Prüfung.
ÄNDERUNGSGRENZE: Nur Status-/Zähldokumente, keine Wissensobjekte.
AUSGABEFORMAT: Release-Dokument nach etabliertem Muster (siehe frühere
Release-Dokumente in 99_archive/v1.0_release/ als Formatreferenz).
ABBRUCHBEDINGUNGEN: Zählwerte lassen sich nicht gegen das Dateisystem verifizieren.
```

**T10 — Research Project**
```
TASK_TYPE: T10_RESEARCH
ZIEL: <W-xxx>, Stufe <1-9> gemäß RESEARCH_LIFECYCLE.md durchführen.
ROLLE: gemäß Stufendefinition in RESEARCH_LIFECYCLE.md.
ERLAUBTE DATEIEN: 06_research_program/active/<W-xxx>/ bzw. completed/<W-xxx>/,
passendes Template aus 06_research_program/templates/.
VERBOTENE DATEIEN: 03_knowledge_base/ breit (außer Stufe 8, dann nur die im
Editor-Decision-Dokument benannten Objekte).
SUCHGRENZE: Projektlokal.
ÄNDERUNGSGRENZE: Nur die aktuelle Stufe, keine vorgezogene Integration.
AUSGABEFORMAT: Stufenspezifisches Template.
ABBRUCHBEDINGUNGEN: Vorherige Stufe nicht abgeschlossen/freigegeben.
```

**T11 — Scientific Debt / Academic Recovery**
```
TASK_TYPE: T11_SCIDEBT
ZIEL: <AR-XXX> gemäß ACADEMIC_RECOVERY_PLAN.md bearbeiten.
ROLLE: Rechercheur, keine neuen Wissensobjekte ohne Plan-Bezug.
ERLAUBTE DATEIEN: SCIENTIFIC_DEBT.md, ACADEMIC_RECOVERY_PLAN.md, LITERATURE_INDEX.md,
die im Plan benannten Zielobjekte.
VERBOTENE DATEIEN: Objekte außerhalb des Plans.
SUCHGRENZE: Externe Websuche zur Quellenverifikation; keine interne Volltextsuche
als Ersatz für Recherche.
ÄNDERUNGSGRENZE: Nur Erweiterung bestehender Objekte, kein neues Objekt ohne
Plan-Bezug.
AUSGABEFORMAT: Plan-Update + erweiterte Zielobjekte.
ABBRUCHBEDINGUNGEN: Quelle nicht auffindbar/verifizierbar.
```

**T12 — Publikationsarbeit**
```
TASK_TYPE: T12_PUBLIKATION
ZIEL: <Zielformat, z. B. Workbook-Kapitel> aus validierten Objekten erstellen.
ROLLE: Lektor/Autor für Zielformat, liest nur aus der Wissensbasis.
ERLAUBTE DATEIEN: 05_publications/<Zielordner>/, thematisch benannte
03_knowledge_base/-Objekte mit Status "Validiert".
VERBOTENE DATEIEN: Entwurfsobjekte (Status ≠ "Validiert"), jede Schreiboperation
in 03_knowledge_base/.
SUCHGRENZE: Thematische Mehrfachsuche in 03_knowledge_base/ erlaubt, rein lesend.
ÄNDERUNGSGRENZE: Nur Dateien in 05_publications/.
AUSGABEFORMAT: Publikations-Textentwurf im Zielordner.
ABBRUCHBEDINGUNGEN: Zu wenige validierte Objekte für das Thema vorhanden.
```

---

## Teil 8 — Directory Routing

**Bewertung:** Claude sollte künftig grundsätzlich **nicht** mehr selbst entscheiden, welche Verzeichnisse für eine Aufgabe infrage kommen. Die Entscheidung ist bereits vollständig durch Teil 3 (Routing-Tabelle) und Teil 7 (Prompt-Vorlagen, Feld „ERLAUBTE DATEIEN") vorweggenommen. Jede Aufgabe nennt ihre erlaubten Verzeichnisse als geschlossene Liste, abgeleitet aus ihrem `TASK_TYPE`.

**Architektur:**
1. Jeder `TASK_TYPE` hat in Teil 3 eine feste Menge erlaubter Wurzelverzeichnisse (z. B. T1 → `02_sources/`, `04_book_analysis/<Titel>/`, `03_knowledge_base/` gefiltert nach Source-ID).
2. Innerhalb eines erlaubten Verzeichnisses ist nicht-rekursives Auflisten (`ls`) immer zulässig — das ist keine Entscheidung, sondern Navigation.
3. Rekursive Volltextsuche (`find` mit Inhaltsprüfung, `grep` über einen ganzen Ordner) ist nur zulässig, wenn der Task-Typ es strukturell erfordert (T6, T7 — siehe Teil 3, Spalte „Erlaubte Suche") oder der Prompt es für genau diese eine Session explizit freigibt.
4. Jedes Verzeichnis außerhalb der Liste ist ohne Rückfrage tabu — auch wenn es „wahrscheinlich auch relevant" wäre. Im Zweifel: Rückfrage, nicht Betreten.

**Ausnahme:** T4 (Architekturarbeit) und T6 (Audit) benötigen strukturell einen Verzeichnis-Scan (Metadaten, nicht Volltext) — das ist bereits in Teil 3 als Ausnahme kodifiziert, keine Einzelfallentscheidung mehr.

---

## Teil 9 — Langfristige Zielarchitektur (2.000 Dateien / 10.000 Wissensobjekte)

Bei linearer Fortschreibung des aktuellen Verhältnisses (514 Objekte / 15 Bücher ≈ 34 Objekte/Buch) entspräche 10.000 Objekte ≈ 290 Büchern. Die aktuelle Architektur (flache Ordner pro Objekttyp, Dateiname = ID) skaliert inhaltlich unverändert, aber die **Auffindbarkeit** bricht ohne zusätzliche Infrastruktur zusammen: `ls 03_knowledge_base/statements/` würde ~2.000 Dateien listen statt 309.

**Neue Komponenten, die sinnvoll wären:**
- **Objekt-Index (Erweiterung von `08_knowledge_atlas`):** eine maschinenlesbare Tabelle ID → Datei-Pfad → Source-ID → Objekttyp → Status, generiert durch den bereits existierenden Compiler (`08_knowledge_atlas/scripts/compile_atlas.py`). Löst D7 (Teil 1) endgültig: Claude muss nie mehr raten, in welchem von 2.000 Dateien eine ID steckt.
- **Buch-lokale Index-Dateien:** `04_book_analysis/<Titel>/OBJECT_RANGE.md` mit den ID-Bereichen dieses Buchs (z. B. „ST-1042–ST-1089, MEC-0210, MEC-0211"). Macht T1/T5 vollständig buch-lokal ohne jede repositoryweite Suche.
- **Objekttyp-Unterordnung nach Source-ID oder Buchstaben-Range** (z. B. `03_knowledge_base/statements/B-0041–B-0060/`), falls `ls` auf einzelne Ordner weiterhin praktikabel bleiben soll — nur falls der Objekt-Index (oben) nicht ausreicht.
- **`TASK_TYPES.md` bleibt zentral, wächst aber nicht mit** — die Routing-Logik selbst ist unabhängig von der Objektzahl, nur die Infrastruktur darunter muss skalieren.

**Ausdrücklich nicht sinnvoll:**
- **Automatisiertes Pre-Fetching durch ein LLM** (z. B. ein Schritt, der „vermutlich relevante" Dateien selbstständig vorab einliest) — das verlagert die Entscheidung nur von „welche Datei lesen" zu „ob das Vorab-Modell richtig geraten hat", löst also D7–D9 nicht, sondern verdeckt sie.
- **Zusammenfassen vieler kleiner Objektdateien zu wenigen großen Dateien** — Rückschritt gegenüber der aktuell guten atomaren Granularität (Performance Audit, Abschnitt 1); genau das Muster, das in `00_project/` (vor Sprint 1) zum Tokenproblem führte, würde in `03_knowledge_base/` reproduziert.
- **Ein weiteres, konkurrierendes Bootstrap-/Routing-Dokument** zusätzlich zu `TASK_TYPES.md` — genau das Muster, das Stufe 1 in `PROJECT_BOOTSTRAP.md`/`CLAUDE_BOOTSTRAP.md`/`INDEX.md` beheben musste. Jede neue Infrastruktur muss in die bestehende Drei-Datei-Struktur (`PROJECT_BOOTSTRAP.md`, `SESSION_BRIEF.md`, `TASK_TYPES.md`) integriert werden, nicht daneben.

---

## Teil 10 — Roadmap

| Maßnahme | Beschreibung | Aufwand | Risiko | Tokenersparnis | Geschwindigkeitsgewinn | Qualitätsgewinn | Priorität |
|---|---|---|---|---|---|---|---|
| **Sprint 2** | | | | | | | |
| `TASK_TYPES.md` anlegen | Inhalt = Teil 2/3-Tabellen dieses Dokuments, als Reference-Datei im Root | Gering (reine Übertragung, keine neue Analyse) | Sehr gering | Mittelbar hoch (eliminiert D3–D9) | Hoch (kein Abwägen mehr pro Session) | Neutral bis positiv | Hoch |
| `TASK_TYPE`-Feld in Prompts einführen | Felix nutzt die 12 Vorlagen aus Teil 7 ab sofort | Keiner (nur Promptverhalten) | Keins | Hoch | Sehr hoch (D10–D13 entfallen) | Positiv (weniger Fehlinterpretation) | Hoch |
| `PROJECT_BOOTSTRAP.md` um Verweis auf `TASK_TYPES.md` ergänzen | Ein Satz, analog zum `SESSION_BRIEF.md`-Verweis aus Sprint 1 | Sehr gering | Keins | Gering direkt | Mittel (Fallback wird auffindbar) | Neutral | Mittel |
| **Sprint 3** | | | | | | | |
| `08_knowledge_atlas`-Output aktiv in T5/T7-Prompts referenzieren | Kein neuer Code — Nutzungsgewohnheit ändern, Compiler existiert bereits | Gering | Gering | Mittel bis hoch bei Konsistenzaufgaben | Hoch bei T5/T7 | Positiv (systematischer als Ad-hoc-Scan) | Mittel |
| Objekt-Index-Erweiterung des Atlas-Compilers (ID → Pfad → Source-ID → Status) | Erweiterung des bestehenden Skripts `compile_atlas.py` um eine zusätzliche Ausgabetabelle | Mittel (Skriptänderung, Testlauf) | Gering (rein lesend, kein Eingriff in Wissensobjekte) | Hoch, sobald Repository wächst | Hoch für T1/T5/T7 | Neutral | Mittel |
| Vier Grenzfälle aus Sprint-1-Bericht entscheiden (`CODEX_AUDIT_2026-07.md` u. a.) | Felix entscheidet Verbleib/Archivierung | Gering | Gering | Gering | Gering | Räumt Restunklarheit aus Sprint 1 auf | Niedrig-Mittel |
| **Sprint 4** | | | | | | | |
| Buch-lokale `OBJECT_RANGE.md` je `04_book_analysis/<Titel>/` einführen | Für alle 15 bestehenden Bücher rückwirkend erzeugen (reine Auflistung bestehender IDs, keine inhaltliche Änderung) | Mittel (15 Dateien, mechanisch aus Atlas-Daten ableitbar) | Gering | Hoch bei künftigen T1/T5-Aufgaben | Hoch | Neutral | Mittel |
| Decision-Budget-Tabelle (Teil 5) probeweise in 2–3 realen Sessions testen und kalibrieren | Kein Repository-Eingriff, nur Beobachtung über reale Nutzung | Gering | Keins | — | — | Verbessert Budget-Genauigkeit | Niedrig |
| **Langfristig** | | | | | | | |
| Objekttyp-Unterordnung nach Source-ID-Range (nur falls Objektzahl das erfordert, siehe Teil 9) | Strukturelle Repository-Änderung, nur bei nachgewiesenem Bedarf (`ls`-Praktikabilität) | Hoch | Mittel (Framework/Templates referenzieren aktuell flache Pfade) | Hoch bei sehr großem Repository | Hoch | Neutral, wenn sauber migriert | Niedrig (aufschieben bis Bedarf real ist) |
| `TASK_TYPES.md` um weitere Typen erweitern, falls T12 (Publikation) real aktiv wird | Ergänzung nach dem ersten realen Publikations-Sprint, nicht vorab spekulativ | Gering | Gering | — | — | Positiv, sobald Bedarf real ist | Niedrig |

---

## Zusammenfassung

Die zentrale architektonische Verschiebung dieser Stufe: Entscheidungen, die bisher Claude zur Laufzeit treffen musste („welche Datei ist relevant?"), werden auf zwei vorgelagerte Ebenen verschoben — (1) die Prompt-Vorlage, die den Task-Typ deklariert (Teil 7), und (2) die statische Routing-Tabelle `TASK_TYPES.md` als Fallback (Teil 3/4). Von den 13 in Teil 1 identifizierten Entscheidungen sind 11 durch diese beiden Ebenen vollständig eliminierbar, ohne dass Claude selbst irgendetwas mehr abwägen muss — die verbleibenden zwei (Objekt-ID-Auflösung, Historienbedarf in Ausnahmefällen) erfordern zusätzliche Infrastruktur (Teil 9), keine weiteren Regeln.
