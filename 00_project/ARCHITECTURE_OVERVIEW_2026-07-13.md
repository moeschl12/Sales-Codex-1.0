# Sales Codex Architecture Overview

Datum: 2026-07-13  
Status: Architekturuebersicht, keine Inhaltsbewertung  
Scope: Repository-Struktur, Steuerungsschichten, Workflows, Objektmodell, Research Program, Atlas, Delivery-Zonen

---

## 1. Kurzfazit

Der Sales Codex ist mittlerweile kein einzelnes Wissensarchiv mehr, sondern ein mehrschichtiges Wissensbetriebssystem:

1. Agenten- und Session-Steuerung
2. Projekt- und Governance-Control-Plane
3. Framework und Wissensmodell
4. Quellen- und Buchanalyse-Pipeline
5. Wissensbasis als Objektgraph
6. Synthese- und Research-Program-Schicht
7. Knowledge Atlas als strukturelles Analyse-Subsystem
8. Delivery-/Publikationsschicht
9. Archiv- und Release-Historie

Die Architektur ist gross, aber nicht grundsaetzlich ungeordnet. Die groesste Komplexitaet liegt nicht in der Wissensbasis selbst, sondern in den Steuerungs-, Status-, Audit- und historischen Projektdokumenten rund um `00_project/`.

---

## 2. Top-Level-Struktur

| Bereich | Rolle | Groesse |
|---|---|---:|
| `.agents/` | Gemeinsame Agent-Control-Plane fuer Codex, Claude und andere Agenten | 13 Dateien |
| `.claude/` | Claude-Kompatibilitaets-Pointer auf `.agents/` | 1 Datei |
| `.codex/` | Codex-Kompatibilitaets-Pointer auf `.agents/` | 1 Datei |
| `00_project/` | Projektsteuerung, Governance, Roadmaps, Reports, Decisions | 89 Dateien |
| `01_framework/` | Methodik, Evidenzsystem, Wissensmodell, Templates, Agentenprotokolle | 28 Dateien |
| `02_sources/` | Quellenverwaltung und Buchquellen | 50 Dateien |
| `03_knowledge_base/` | Kanonische Wissensobjekte | 515 Dateien |
| `04_book_analysis/` | Buchanalysen, VAL-Reviews, Book Review Reports | 50 Dateien |
| `04_synthesis/` | Sprint- und Cross-Book-Synthesen | 8 Dateien |
| `05_publications/` | Erste Delivery-Artefakte fuer Buch, Workbook, Training | 3 Dateien |
| `05_research/` | Literaturindex / Research-Bibliographie | 1 Datei |
| `06_media/` | Medienablage, derzeit leer | 0 Dateien |
| `06_research_program/` | Separater Research-Lifecycle fuer offene Forschungsfragen | 86 Dateien |
| `07_scripts/` | Allgemeines Skript-/Automationsverzeichnis | 1 Datei |
| `08_knowledge_atlas/` | Strukturgraph, Atlas-Compiler, Reports | 14 Dateien |
| `99_archive/` | Historische / abgeschlossene / archivierte Inhalte | 23 Dateien |

Architektonischer Hinweis: Es gibt gewachsene Nummernkollisionen (`04_*`, `05_*`, `06_*`). Diese sind dokumentiert und aktuell nicht zwingend schadhaft, aber sie erschweren die mentale Navigation.

---

## 3. Steuerungsebenen

### 3.1 Einstiegsebene

| Datei / Ordner | Funktion |
|---|---|
| `AGENTS.md` | Oberste Projektanweisung fuer KI-Arbeit |
| `PROJECT_BOOTSTRAP.md` | Kanonischer Session-Einstieg, Wissenspipeline, Suchgrenzen |
| `SESSION_BRIEF.md` | Kompakter aktueller Status statt vollstaendigem `CURRENT_STATE.md` |
| `00_project/NEXT_ACTION.md` | Operativer Launcher; aktuell kein offenes V1.1-Makroprojekt |
| `.agents/README.md` | Gemeinsame Agent-Hilfsschicht |
| `.codex/README.md` | Nur Pointer auf `.agents/` |
| `.claude/README.md` | Nur Pointer auf `.agents/` |

Aktueller Zustand: V1.1 ist `RELEASED - SCOPE-LIMITED`; es gibt keinen offenen regulären V1.1-Launcher.

### 3.2 Agent-neutrale Hilfsschicht

`.agents/` ist als kleine, nachgeordnete Orientierungsschicht angelegt:

| Unterordner | Rolle |
|---|---|
| `.agents/rules/` | Kurze Arbeitsregeln: Repository-Autoritaet, Session-Start, Change Boundaries, Knowledge Work |
| `.agents/commands/` | Wiederverwendbare Arbeitsrezepte: Task Routing, Review, Architekturvorschlag |
| `.agents/roles/` | Rollenprofile: Editor, Scientific Editor, Validation Reviewer |
| `.agents/workflows/` | Workflow-Pointer: Book Mode, Research Lifecycle |

Wichtig: Diese Ebene ist keine neue Methodik. Sie verweist auf bestehende Autoritaetsdateien.

---

## 4. Framework-Schicht

`01_framework/` ist die normative Wissensarchitektur.

| Bereich | Zweck |
|---|---|
| `00_charter/` | Projektziel und Qualitaetsanspruch |
| `01_methodology/` | Grundmethodik des Codex |
| `02_evidence_system/` | Evidenzklassen und wissenschaftliche Bewertung |
| `03_source_standard/` | Quellenstandards |
| `04_principle_extraction/` | Prinzipienextraktion |
| `05_knowledge_model/` | Canonical Knowledge Model |
| `06_process_system/` | Sales Process Decision System |
| `07_agent_protocols/` | Rollenprotokolle fuer Claude, ChatGPT, Gemini, Perplexity |
| `08_templates/` | Templates fuer Objekttypen und Reviews |

Diese Schicht definiert, welche Wissensobjekte existieren duerfen, wie sie entstehen und wie sie bewertet werden.

---

## 5. Wissensmodell

Die kanonische Wissensbasis liegt in `03_knowledge_base/`.

| Objekttyp | Ordner | Anzahl |
|---|---|---:|
| Statements | `statements/` | 309 |
| Annahmen | `assumptions/` | 60 |
| Mechanismen | `mechanisms/` | 30 |
| Prinzipien | `principles/` | 57 |
| Techniken | `techniques/` | 47 |
| Modelle | `models/` | 12 |
| Kompetenzen | `competencies/` | 0 |
| Beobachtungen | `observations/` | 0 |
| Meta-Modelle | `meta_models/` | 0 |
| Gesamt |  | 515 |

Objektlogik:

```text
SRC -> ST -> A -> MEC -> P -> T -> MOD -> VAL -> Abschlussbericht
```

Grundidee:

- Statements kommen aus Primaerquellen.
- Annahmen clustern darunterliegende Voraussetzungen.
- Mechanismen erklaeren kausale Prozesse.
- Prinzipien abstrahieren ueber mehrere Mechanismen oder Annahmen.
- Techniken uebersetzen Prinzipien in wiederholbare Handlungen.
- Modelle verbinden mehrere Objekte zu kausallogischen Strukturen.

---

## 6. Quellen- und Buchanalyse-Schicht

### 6.1 Quellen

`02_sources/` enthaelt:

- Quellenuebersichten und Kataloge
- Buchquellen unter `02_sources/books/`
- insgesamt 50 Dateien, davon 48 im Buchquellenbereich

### 6.2 Buchanalysen

`04_book_analysis/` enthaelt 15 Buchordner:

| Buchordner | Dateien |
|---|---:|
| Emotional Intelligence | 4 |
| Gap Selling | 3 |
| Getting to Yes | 3 |
| Influence | 3 |
| Made to Stick | 4 |
| Never Split the Difference | 3 |
| Nudge | 4 |
| Pre-Suasion | 3 |
| Predictably Irrational | 4 |
| Priceless | 4 |
| SPIN_Selling | 3 |
| The Challenger Sale | 3 |
| The JOLT Effect | 3 |
| Thinking, Fast and Slow | 3 |
| To Sell Is Human | 3 |

Standardausgabe je Buch:

- `analysis.md`
- `VAL-...` Konsistenzreview
- `BOOK_REVIEW_REPORT...`
- ggf. Canonicalization- oder Zusatzreports

---

## 7. Task- und Arbeitsmodus-Schicht

`TASK_TYPES.md` definiert 12 Arbeitstypen:

| Typ | Name |
|---|---|
| T1 | Buchanalyse / Book Mode |
| T2 | Framework-Arbeit |
| T3 | Repository-Wartung / Hygiene |
| T4 | Architekturarbeit |
| T5 | Review / Validierung |
| T6 | Audit |
| T7 | Konsistenzpruefung |
| T8 | Governance / Decision Resolution |
| T9 | Release / Freeze |
| T10 | Research Project Lifecycle |
| T11 | Scientific Debt / Academic Recovery |
| T12 | Publikationsarbeit, vorbereitet, noch nicht aktiv |

Diese Schicht ist eine zentrale Komplexitaetskontrolle: Sie begrenzt Dateizugriffe, Schreibrechte, Suchumfang und Ausgabeform je Aufgabentyp.

---

## 8. Projekt- und Governance-Schicht

`00_project/` ist die groesste Steuerungsschicht.

Hauptfunktionen:

- aktueller Status und Launcher
- Roadmaps und Makroprojekte
- Open Decisions und Decision Briefs
- Scientific Debt
- Audit- und Review-Reports
- Completion-/Closure-Reports
- Backlog, Task Rules, Session Log

V1.1-Makroprojektstruktur:

| Projekt | Rolle | Dateien im Projektordner |
|---|---|---:|
| V11-01 | Baseline & Control Plane Consolidation | 3 |
| V11-02 | Evidence Architecture Resolution | 3 |
| V11-03 | Governance + Repository Integrity + Atlas | 3 |
| V11-04 | Early Delivery Vertical Slice | 3 |
| V11-05 | Knowledge Consolidation & Integrated Synthesis | 6 |
| V11-06 | Research Portfolio Wave 2 | 3 |
| V11-07 | Cross-System Review & Delivery Scaling Decision | 4 |
| V11-08 | Final Program Audit & Release Decision | 5 |

Makroprojekt-Pattern:

```text
PROJECT_BRIEF -> Execution -> COMPLETION_REPORT -> AUDIT_REPORT -> Closure / Release Decision
```

Komplexitaetsbefund: `00_project/` ist funktional wichtig, aber zum groessten Navigations- und Statusrisiko geworden, weil aktive Steuerung, Historie, Auditberichte, Decision-Unterlagen und alte Sprints nebeneinander liegen.

---

## 9. Research Program

`06_research_program/` ist strikt vom offiziellen Codex getrennt, bis eine positive Editor Decision und Repository Integration erfolgt sind.

Ordnerstruktur:

| Bereich | Dateien |
|---|---:|
| `active/` | 0 |
| `archived/` | 0 |
| `completed/` | 66 |
| `templates/` | 11 |

Research Lifecycle:

```text
1 Research Question
2 Initial Hypothesis
3 Master Review
4 Peer / Red Team Review
5 Theory Landscape
6 Decision Brief
7 Editor Decision
8 Repository Integration
9 Health Check
```

Integrationsregel:

- Research-Ergebnisse werden nicht direkt zu Codex-Wissen.
- Erst Editor Decision.
- Dann Repository Integration.
- Dann Health Check.
- Danach gelten dieselben Regeln wie fuer Buchanalyse-Ergebnisse.

Architektonisch ist das Research Program ein zweiter, kontrollierter Erkenntnisweg neben Book Mode.

---

## 10. Synthese-Schicht

`04_synthesis/` buendelt Cross-Book- und Sprint-Synthesen.

| Synthese | Dateien |
|---|---:|
| `SPR-0001_Sales_Core_Synthesis/` | 6 |
| `SPR-0002_Research_Synthesis/` | 1 |
| `SPR-0003_Behavioral_Science_Synthesis/` | 1 |

Rolle:

- Verdichtung mehrerer Buchanalysen
- Widerspruchsmatrix
- Canonicalization-Report
- Evidence-Upgrade-Report
- Research Agenda

Diese Schicht ist zwischen Wissensbasis und Governance angesiedelt: Sie produziert keine beliebigen neuen Inhalte, sondern konsolidiert bestehende Objekte.

---

## 11. Knowledge Atlas

`08_knowledge_atlas/` ist ein Analyse-Subsystem ueber der Wissensbasis.

Aktueller Compiler-Stand laut Report:

| Kennzahl | Wert |
|---|---:|
| Nodes | 515 |
| Edges | 2112 |
| Reference Orphans | 18 |
| Duplicate IDs | 0 |
| Unaufgeloeste Referenz-Ziel-IDs | 1 |

Scope v0.1:

- Knoten: ST, A, MEC, P, T, MOD
- Kanten: explizite ID-Referenzen
- Fokus: Orphan-Identifikation und strukturelle Integritaet

Nicht im Scope:

- semantische Kantenbedeutung
- Zentralitaetsmetriken
- Layer
- Query Engine
- inhaltliche Bewertung

Der Atlas ist derzeit ein Strukturmonitor, kein Inhaltsanalyse-System.

---

## 12. Delivery- und Publikationsschicht

`05_publications/` enthaelt erste Vertical-Slice-Artefakte:

- Buchfragment
- Workbook-Uebung
- Trainingssequenz

`05_research/` enthaelt den Literaturindex.

`06_media/` ist derzeit leer.

Architektonischer Status:

- Delivery ist vorbereitet, aber nicht breit freigegeben.
- T12 Publikationsarbeit ist als Task Type vorbereitet, bleibt aber laut V1.1-Status governance-seitig noch begrenzt.
- V1.1 Release hat breite Delivery-Skalierung ausdruecklich nicht freigegeben.

---

## 13. Datenfluesse

### 13.1 Standardpfad: Buch zu Wissensbasis

```text
02_sources/books
  -> 04_book_analysis/[Buch]/analysis.md
  -> 03_knowledge_base/ST
  -> 03_knowledge_base/A
  -> 03_knowledge_base/MEC
  -> 03_knowledge_base/P
  -> 03_knowledge_base/T
  -> 03_knowledge_base/MOD
  -> 04_book_analysis/[Buch]/VAL
  -> BOOK_REVIEW_REPORT
  -> CURRENT_STATE / NEXT_ACTION / SESSION_LOG
```

### 13.2 Forschungsfrage zu Wissensbasis

```text
Open Question / Contradiction / Scientific Debt
  -> 06_research_program/active/W-XXX
  -> Research Lifecycle Stufen 1-6
  -> Editor Decision
  -> Repository Integration
  -> Health Check
  -> 03_knowledge_base Erweiterung oder Neuanlage
  -> RESEARCH_STATUS / SCIENTIFIC_DEBT / SESSION_LOG
```

### 13.3 Makroprojekt zu Release

```text
ROADMAP_V1_1
  -> NEXT_ACTION
  -> PROJECT_BRIEF
  -> Execution
  -> COMPLETION_REPORT
  -> AUDIT_REPORT
  -> Closure Report
  -> Editor Release Decision
```

### 13.4 Wissensbasis zu Delivery

```text
03_knowledge_base validierte / geeignete Objekte
  -> 04_synthesis oder Projektbrief
  -> 05_publications/book | workbook | training
  -> Review / Audit
  -> Keine breite Skalierung ohne Editor Decision
```

---

## 14. Architekturrollen

| Rolle | Hauptverantwortung |
|---|---|
| Felix / Herausgeber | Prioritaet, Editor Decisions, Framework-Aenderungen, Release, Git |
| Claude / Cowork | Produktion, Buchanalyse, Redaktionsarbeit, Konsistenzreview |
| Codex | Umsetzung, Strukturarbeit, Audits, Tooling, lokale Repository-Arbeit |
| ChatGPT | Scientific & Systems Editor, Modell- und Strukturkritik |
| Gemini | Wissenschaftliche Validierung |
| Perplexity | Quellenrecherche |
| `.agents/` | Gemeinsame Orientierung fuer alle Agenten |

---

## 15. Komplexitaetsdiagnose

### 15.1 Gesunde Komplexitaet

Diese Teile wirken gross, aber funktional gerechtfertigt:

- `03_knowledge_base/`: 515 Objekte sind fuer ein evidenzbasiertes Wissenssystem nicht problematisch, solange ID-Integritaet und Referenzen stabil bleiben.
- `06_research_program/`: Der 9-stufige Prozess ist aufwendig, aber er verhindert, dass Forschungsfragen ungeprueft in die Wissensbasis wandern.
- `08_knowledge_atlas/`: Der Atlas reduziert Risiko, weil er die wachsende Objektmenge strukturell pruefbar macht.
- `TASK_TYPES.md`: Gross, aber sehr nuetzlich als Zugriffsbremse und Anti-Chaos-System.

### 15.2 Reale Komplexitaetstreiber

Diese Teile erzeugen Navigations- und Wartungslast:

1. `00_project/` enthaelt aktive Steuerung, historische Reports, Audits, Decisions, Backlog, Debt, Roadmaps und Logs nebeneinander.
2. Mehrere Statusquellen existieren parallel: `CURRENT_STATE.md`, `SESSION_BRIEF.md`, `NEXT_ACTION.md`, `ROADMAP_V1_1.md`, `DECISION_STACK_2026-07-13.md`.
3. Die Top-Level-Nummerierung hat Kollisionen: `04_*`, `05_*`, `06_*`.
4. `INDEX.md` wirkt teilweise historisch und spiegelt die neue Agent-/V1.1-/Research-Architektur nicht vollstaendig wider.
5. V1.1 hat viele Abschluss-, Audit- und Closure-Dokumente erzeugt; fachlich sauber, aber als Alltagsnavigation schwer.
6. Delivery ist vorbereitet, aber governance-seitig noch nicht klar aktivierbar; T12 ist vorhanden, aber nicht freigegeben.

### 15.3 Erste Verschlankungskandidaten, nur Architektur

Noch keine Umsetzungsempfehlung, nur Kandidaten fuer spaetere Diskussion:

1. **Single Architecture Map einfuehren:** Dieses Dokument oder eine kuerzere `ARCHITECTURE.md` als dauerhafter Einstieg.
2. **`00_project/` entlasten:** Aktive Steuerung von historischen Sprint-/Audit-Artefakten trennen, ohne Inhalte zu loeschen.
3. **Statusquellen reduzieren:** Eine kanonische Statusquelle plus kurze Pointer statt mehrere ausformulierte Statusnarrative.
4. **Top-Level-Kollisionen klaeren:** Nicht zwingend umbenennen, aber in einer festen Map dokumentieren.
5. **`INDEX.md` erneuern:** Als echte Navigation fuer Menschen und Agenten, nicht als historischer Startpunkt.
6. **Delivery-Gate klaeren:** T12 entweder bewusst aktivieren, weiter sperren oder in eine klare Vorbereitungszone legen.
7. **Archivierungsregel fuer abgeschlossene V1.1-Projektdokumente definieren:** Nicht loeschen, aber Alltagssicht schlanker machen.

---

## 16. Architektururteil

Der Sales Codex ist nicht "zu gross" im Sinne von unkontrolliertem Inhaltswachstum. Die Wissensbasis ist gross, aber messbar und strukturell ueber den Atlas ueberwachbar.

Der Codex ist allerdings an einer Schwelle, an der die Steuerungsarchitektur selbst zum Arbeitsgegenstand wird. Wenn die naechste Phase der Leitfaden ist, sollte vor der Inhaltsarbeit mindestens eine Navigations- und Statusverschlankung erfolgen, damit Publikationsarbeit nicht jedes Mal durch Release-, Audit- und Research-Governance-Historie hindurcharbeiten muss.

Minimaler naechster Architekturschritt waere keine Methodikaenderung, sondern eine Navigationsentscheidung:

```text
Was ist die eine Startkarte fuer Menschen und Agenten, wenn aus der Wissensbasis jetzt ein Leitfaden entstehen soll?
```

