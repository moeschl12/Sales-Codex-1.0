# Repository Manifest — Sales Codex Version 1.0 RC-1

**Dokumentklasse:** Release (Configuration Management)
**Rolle bei Erstellung:** Release Manager / Configuration Manager — reiner Snapshot, keine inhaltlichen Änderungen
**Datum:** 2026-07-04
**Zweck:** Vollständiger, unveränderter Abbildungs-Snapshot des Repository-Zustands zum RC-1-Freeze-Zeitpunkt. Kein Dokument in diesem Manifest wurde verändert; es werden ausschließlich bestehende Zustände beschrieben.

---

## 1. Repositorystruktur (Top-Level)

| Ordner | Zweck |
|---|---|
| `00_project/` | Governance, Steuerdokumente, Sprintberichte, Peer Review |
| `01_framework/` | Methodik, Evidenzsystem, Quellenstandard, Wissensmodell, Agentenprotokolle, Templates |
| `02_sources/` | Primärquellen (Bücher als PDF/EPUB) und Quellobjekte (SRC-XXXX) |
| `03_knowledge_base/` | Kanonische Wissensobjekte (ST, A, MEC, P, T, MOD + noch unbefüllte Kategorien) |
| `04_book_analysis/` | Einzelbuch-Analyseordner (Analyse, Selbstreview, Abschlussbericht je Buch) |
| `04_synthesis/` | Sprintübergreifende Syntheseberichte (SPR-0001–0003) |
| `05_publications/` | Vorbereitete, noch unbefüllte Publikationsstruktur (Buch, Talks, Trainings, Workbook) |
| `05_research/` | Literaturverzeichnis (`LITERATURE_INDEX.md`) für Academic-Recovery-Quellen |
| `06_media/` | Vorbereitete, noch unbefüllte Medienstruktur (Diagramme, Bilder, Mindmaps) |
| `06_research_program/` | Research Program: Governance, Lifecycle, Templates, aktive/abgeschlossene/archivierte Projekte |
| `07_scripts/` | Vorbereitete Skript-Infrastruktur (aktuell nur README) |
| `99_archive/` | Archivierte, historisch erhaltene Dokumente (nicht gelöscht, nicht mehr aktiv) |

**Hinweis (nicht durch diesen Freeze verändert):** `05_publications/` und `05_research/` sowie `04_book_analysis/` und `04_synthesis/` teilen sich jeweils dieselbe Nummernebene — eine seit der Repository Consolidation dokumentierte, unentschiedene Nummernkollision (`REPOSITORY_CONSOLIDATION_REPORT_RC1.md`, Kapitel 12). Keine Strukturänderung im Rahmen dieses Freeze.

## 2. Vollständige Ordnerstruktur (Ebene 2)

```
00_project/
  peer_review/decisions/
01_framework/
  00_charter/  01_methodology/  02_evidence_system/  03_source_standard/
  04_principle_extraction/  05_knowledge_model/  06_process_system/
  07_agent_protocols/  08_templates/
02_sources/
  articles/  books/  interviews/  other/  podcasts/  studies/
03_knowledge_base/
  assumptions/  competencies/  mechanisms/  meta_models/  models/
  observations/  principles/  statements/  techniques/
04_book_analysis/
  Emotional Intelligence/  Gap Selling/  Getting to Yes/  Influence/
  Made to Stick/  Never Split the Difference/  Nudge/  Pre-Suasion/
  Predictably Irrational/  Priceless/  SPIN_Selling/  The Challenger Sale/
  The JOLT Effect/  Thinking, Fast and Slow/  To Sell Is Human/
04_synthesis/
  SPR-0001_Sales_Core_Synthesis/  SPR-0002_Research_Synthesis/
  SPR-0003_Behavioral_Science_Synthesis/
05_publications/
  sales_codex_book/  talks/  trainings/  workbook/  (alle unbefüllt)
05_research/
  (LITERATURE_INDEX.md, keine Unterordner)
06_media/
  diagrams/  images/  mindmaps/  (alle unbefüllt)
06_research_program/
  active/ (leer)  archived/ (leer)  completed/W001/  templates/
07_scripts/
  (nur README.md)
99_archive/
  (5 Dateien, siehe Abschnitt 6)
```

Leere, aber bewusst vorbereitete Ordner: 17 (verifiziert `REPOSITORY_CONSOLIDATION_IMPLEMENTATION_REPORT_RC1.md`, unverändert seit Repository Consolidation Sprint 2).

## 3. Objektanzahlen (Snapshot 2026-07-04)

| Kategorie | Anzahl |
|---|---|
| Wissensobjekte gesamt (`03_knowledge_base/`) | 514 |
| — Statements (ST) | 309 |
| — Prinzipien (P) | 57 |
| — Annahmen (A) | 60 |
| — Techniken (T) | 47 |
| — Mechanismen (MEC) | 29 |
| — Modelle (MOD) | 12 |
| — Meta-Modelle | 0 (Kategorie vorbereitet) |
| — Kompetenzen | 0 (Kategorie vorbereitet) |
| — Beobachtungen | 0 (Kategorie vorbereitet) |
| Quellobjekte (SRC) | 15 |
| Abgeschlossene Buchanalysen | 15 |
| Selbstreviews (VAL) | 15 |
| Syntheseberichte (SPR) | 3 (SPR-0001, SPR-0002, SPR-0003) |
| Open Decisions gesamt | 12 (4 DONE, 1 ERSETZT, 2 ANGENOMMEN/Umsetzung ausstehend, 5 OFFEN) |
| Scientific-Debt-Tabellenzeilen | 106 (23 Tabellen) — Methodik-Hinweis siehe `RELEASE_CANDIDATE_RC1.md` Abschnitt 13 |
| Forschungsprojekte (Research Program) | 1 abgeschlossen (W-001), 0 aktiv, 0 archiviert |
| Markdown-Dateien gesamt im Repository (ohne `.git/`) | 701 |

## 4. Versionen

| Dokument/Ebene | Version | Stand |
|---|---|---|
| Sales-Codex-Gesamtversion | Pre-1.0 → **RC-1** (dieser Freeze) | 2026-07-04 |
| Framework-Version | 1.1 | eingefroren 2026-06-30 |
| `SALES_CODEX_OPERATING_MANUAL.md` | 1.0 | — |
| `01_framework/05_knowledge_model/canonical_knowledge_model.md` | 1.0 | — |
| `00_project/task_rules.md` | 1.0 | — |
| `00_project/REPOSITORY_KPIS.md` | 1.1 | 2026-07-03 (External Audit Resolution Sprint) |
| `00_project/SCIENTIFIC_DEBT.md` | 1.0 (Feldangabe) | zuletzt aktualisiert 2026-07-03 (W-001-Integration) |
| `05_research/LITERATURE_INDEX.md` | 1.2 | 2026-07-02 |
| `06_research_program/RESEARCH_STATUS.md` | RC-1 | 2026-07-03 |

## 5. Wichtige Governance-Dokumente

| Dokument | Zweck |
|---|---|
| `00_project/SALES_CODEX_OPERATING_MANUAL.md` | Verbindlicher Arbeitsprozess (Schritte 1–11, inkl. Book Mode Abschnitt 10, Research-Program-Verweis Abschnitt 11) |
| `00_project/task_rules.md` | Aufgabenregeln inkl. Book-Mode- (Abschnitt 10) und Research-Program-Bezug (Abschnitt 7.5) |
| `00_project/OPEN_DECISIONS.md` | Register aller 12 Open Decisions (OD-001–012) mit Auflösungsvermerken |
| `00_project/SCIENTIFIC_DEBT.md` | Zentrales Tracking-System für unvollständig gesicherte Wissensobjekte |
| `00_project/CONTRIBUTING.md` | Beitragsregeln |
| `00_project/COWORK_EXECUTION_PROTOCOL.md` | Ausführungsprotokoll für KI-Agenten |
| `00_project/SESSION_LOG.md` | Chronologisches Sitzungsprotokoll |
| `00_project/changelog.md` | Änderungsprotokoll |
| `00_project/SALES_CODEX_1_0_PROGRAM.md` | Ursprüngliches 1.0-Programm (2026-07-02, historisch erhalten, durch Release Plan abgelöst) |
| `00_project/SALES_CODEX_1_0_RELEASE_PLAN.md` | Aktives Release-Steuerdokument (2026-07-03) — MUST/SHOULD/COULD/WON'T-HAVE-Scope, Critical Path, Risiken |
| `00_project/REPOSITORY_KPIS.md` | Quantitative Kennzahlen je Buch |
| `00_project/review_queue.md` | Dokumentierte, nicht angelegte Literatur-/Objektkandidaten |
| `00_project/ACADEMIC_RECOVERY_PLAN.md` | Priorisierte Tier-1–4-Rechercheagenda |
| `00_project/peer_review/decisions/` | Peer-Review-Entscheidungsberichte (Sprint 1, Sprint 2) |

## 6. Wichtige Framework-Dokumente

| Dokument | Zweck |
|---|---|
| `01_framework/00_charter/project_charter.md` | Projektauftrag |
| `01_framework/01_methodology/codex_methodology.md` | Methodik |
| `01_framework/02_evidence_system/evidence_system.md` | Evidenzklassen- und Quellenklassensystem |
| `01_framework/03_source_standard/codex_source_standard.md` | Quellenstandard |
| `01_framework/04_principle_extraction/principle_extraction_standard.md` | Prinzip-Extraktionsstandard |
| `01_framework/05_knowledge_model/canonical_knowledge_model.md` | Kanonisches Wissensmodell (aktiv; Abschnitt 11 = Research-Program-Integrationshinweis) |
| `01_framework/06_process_system/sales_process_decision_system.md` | Prozessentscheidungssystem |
| `01_framework/07_agent_protocols/*.md` (5 Dateien) | Agentenprotokolle (Claude Editor, ChatGPT Architect, Gemini Validation, Perplexity Research, Master Agent) |
| `01_framework/08_templates/*.md` (14 Dateien) | Objekt-Templates (Source, Statement, Assumption, Principle, Mechanism, Technique, Competency, Model, Meta-Model, Book Analysis, Book Review, Comparison, Decision, Meeting Notes, Validation Report) |
| `99_archive/codex_knowledge_model.md` | Veraltetes Wissensmodell-Dokument, archiviert (ED-003), nicht mehr aktiv |

## 7. Aktive Forschungsprojekte

**Keine.** `06_research_program/active/` ist leer (`RESEARCH_STATUS.md`, Abschnitt 1: keine Zeile eingetragen).

## 8. Abgeschlossene Forschungsprojekte

| Projekt-ID | Titel | Ergebnis | Abgeschlossen |
|---|---|---|---|
| W-001 | Teach First vs. Diagnose First | Teilweise angenommen — Kernbefund in 6 Objekte integriert (A-0020, P-0021, P-0025, MEC-0013, T-0019, T-0023); SCSM-Formalisierung abgelehnt | 2026-07-03 |

Vollständige Projektunterlagen: `06_research_program/completed/W001/` (11 Dokumente: Initial Hypothesis, Master Review, Red-Team-Review, Theory Landscape, Decision Brief, Editor Decision, Health Check, Open Questions, README, References, Research Log, Repository Integration Log, Completion Report, Repository Integration Report).

Archivierte Forschungsprojekte: keine (`06_research_program/archived/` leer).

## 9. Wissenschaftliche Abdeckung

### 9.1 Verarbeitete Bücher (15)

| ID | Titel | Autor | Domäne |
|---|---|---|---|
| B-0001 | SPIN Selling | Neil Rackham | Vertrieb / Fragetechnik |
| B-0002 | Influence: The Psychology of Persuasion | Robert B. Cialdini | Psychologie / Einfluss |
| B-0003 | Never Split the Difference | Chris Voss / Tahl Raz | Verhandlung |
| B-0004 | The Challenger Sale | Matthew Dixon & Brent Adamson | Vertrieb / B2B-Methodik |
| B-0005 | Gap Selling | Keenan | Vertrieb / Diagnose |
| B-0006 | The JOLT Effect | Matthew Dixon & Ted McKenna | Vertrieb / Entscheidungspsychologie |
| B-0007 | Getting to Yes | Roger Fisher / William Ury | Verhandlung |
| B-0008 | Pre-Suasion | Robert Cialdini | Psychologie / Einfluss |
| B-0009 | To Sell Is Human | Daniel H. Pink | Vertrieb / Allgemeinpsychologie |
| B-0010 | Thinking, Fast and Slow | Daniel Kahneman | Entscheidungspsychologie |
| B-0011 | Emotional Intelligence | Daniel Goleman | Emotionspsychologie |
| B-0012 | Predictably Irrational | Dan Ariely | Verhaltensökonomie |
| B-0013 | Nudge: The Final Edition | Thaler & Sunstein | Verhaltensökonomie / Choice Architecture |
| B-0014 | Priceless: The Myth of Fair Value | William Poundstone | Preispsychologie |
| B-0015 | Made to Stick | Chip Heath & Dan Heath | Kommunikationspsychologie |

### 9.2 Domänenabdeckung — qualitative Einordnung

Abgedeckt (mit unterschiedlicher Tiefe): Fragetechnik/Diagnose, Einfluss-/Compliance-Prinzipien, Verhandlungstaktik, B2B-Insight-Selling, Entscheidungspsychologie/Behavioral Economics, Choice Architecture, Preispsychologie, Emotionspsychologie, Kommunikations-/Narrativpsychologie.

**Bewusst nicht abgedeckt** (laut `SALES_CODEX_1_0_RELEASE_PLAN.md`, Kapitel 2.2, nie Teil des bestehenden Anspruchs): Account Management, Pricing Psychology im engeren B2B-Sinn über Priceless hinaus, Digital Sales/Inside Sales.

**Strukturell schwächste Dimension:** Generalisierbarkeit von Labor-/B2C-Befunden auf komplexe B2B-Kontexte (im letzten Reifegradbericht mit C+ bewertet) — direkter Anlass für OD-007 (CTX-Ebene).

**Größte ungeklärte Abhängigkeit:** Drei der am häufigsten zitierten B2B-Kernmethodiken (SPIN/Huthwaite, Challenger/CEB, JOLT/Tethr) beruhen auf proprietären, nicht unabhängig peer-reviewten Großstudien (SD-SYS-001, SD-SYS-004).

---

*Dieses Manifest ist ein reiner Snapshot zum Zeitpunkt des RC-1-Freeze (2026-07-04). Es verändert keinen der referenzierten Inhalte. Nachfolgende Änderungen am Repository (nach Freeze-Regeln in `RC1_FREEZE_DECLARATION.md`) machen einzelne Zahlen in diesem Dokument historisch — das Manifest wird dann nicht rückwirkend angepasst, sondern durch ein neues Manifest bei der nächsten Release-Stufe ersetzt.*
