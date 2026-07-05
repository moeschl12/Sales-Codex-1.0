# Release Candidate RC-1 — Sales Codex Version 1.0

**Dokumentklasse:** Release (Configuration Management)
**Rolle bei Erstellung:** Release Manager / Configuration Manager — keine fachliche, wissenschaftliche oder redaktionelle Bewertung
**Versionsnummer (Ziel):** 1.0
**Release Candidate Name:** RC-1
**Datum des Freeze:** 2026-07-04
**Grundlage:** `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SALES_CODEX_1_0_RELEASE_PLAN.md`, `00_project/REPOSITORY_KPIS.md` (Version 1.1), `00_project/OPEN_DECISIONS.md`, `00_project/SCIENTIFIC_DEBT.md`, `00_project/EXTERNAL_AUDIT_RESOLUTION_REPORT.md`, `00_project/FINAL_PRE_RELEASE_REPORT.md`, `06_research_program/RESEARCH_STATUS.md`, `06_research_program/completed/W001/`, sowie direkte Dateisystemzählung (`03_knowledge_base/`, `02_sources/`, `04_book_analysis/`) am 2026-07-04.

---

## 1. Versionsnummer

| Achse | Wert |
|---|---|
| Sales-Codex-Gesamtversion (Ziel) | 1.0, Status: **RC-1 (Release Candidate)** — noch nicht veröffentlicht |
| Framework-Version | 1.1 (eingefroren 2026-06-30, unverändert seit diesem Datum) |

Die beiden Versionsachsen sind gemäß `00_project/SALES_CODEX_1_0_PROGRAM.md` (Kapitel 9) und `00_project/OPEN_DECISIONS.md` (OD-009) bewusst getrennt geführt: Die Framework-Version beschreibt Methodik/Prozess/Templates, die Sales-Codex-Gesamtversion den Reifegrad des Gesamtinhalts.

## 2. Release Candidate Name

**Sales Codex Version 1.0 RC-1**

## 3. Datum

Freeze-Datum: **2026-07-04**

## 4. Repository Status

**Eingefroren als Release Candidate.** Der Entwicklungsmodus endet mit diesem Dokument; ab sofort gilt für den Wissensbestand (Wissensobjekte, Framework, Research Program, abgeschlossene Forschungsprojekte, Editor Decisions) Änderungssperre gemäß `RC1_FREEZE_DECLARATION.md`.

Vorangegangene, für diesen Freeze relevante Sprints (alle laut Repository-Dokumentation abgeschlossen):

| Sprint | Ergebnis |
|---|---|
| Repository Consolidation (Sprint 1 Audit + Sprint 2 Implementation) | Abgeschlossen — 8 Editor Decisions umgesetzt |
| Academic Recovery (Phase 1, Phase 2, Sprint-3-Review) | Abgeschlossen (mit dokumentierten, bewusst nicht-blockierenden Tier-1-Restpunkten AR-001/002/013) |
| Behavioral Science Expansion Sprint 1 | Abgeschlossen — 5/5 Bücher (B-0011–B-0015) |
| Behavioral Science Review Sprint | Abgeschlossen — 8 Editor Decisions |
| Research Program Finalization (RC-1) | Abgeschlossen — Governance, Lifecycle, 11 Templates |
| Research Project W-001 (inkl. Repository Integration) | Abgeschlossen — erstes Projekt mit vollständigem 9-Stufen-Lifecycle |
| Sales Codex 1.0 Release Planning | Abgeschlossen — `SALES_CODEX_1_0_RELEASE_PLAN.md`, Empfehlung damals: READY AFTER MINOR REVISION |
| Sales Codex 1.0 Final Pre-Release Sprint | Abgeschlossen — OD-006/007 entschieden, MEC-0018-Widerspruch behoben, 70 Objekte evidenzharmonisiert |
| External Release Audit ("Wissenschaftliche Prüfung des Sales Codex") | Durchgeführt — 7 Kritikpunkte, Gesamteinschätzung des Audits: MAJOR REVISION REQUIRED |
| External Audit Resolution Sprint | Abgeschlossen — alle 7 Kritikpunkte einzeln verifiziert und bearbeitet, Ergebnis: READY FOR FINAL RC-1 AUDIT |

**Wichtiger Statusvorbehalt (nicht glätten, siehe `RC1_FREEZE_DECLARATION.md` und `RC1_FREEZE_REPORT.md`):** Der in `00_project/SALES_CODEX_1_0_RELEASE_PLAN.md` (Kapitel 2.2, Kapitel 5) und `00_project/NEXT_ACTION.md` als eigenständiger, noch ausstehender Schritt definierte **Finale RC-1-Audit** ist von diesem Freeze zu unterscheiden und durch ihn **nicht ersetzt**. Dieses Dokument friert den Kandidaten ein, der diesem Audit vorgelegt wird — es ist nicht der Audit selbst.

## 5. Anzahl Wissensobjekte

| Objekttyp | Anzahl | Verifikation |
|---|---|---|
| Statements (ST) | 309 | Dateizählung `03_knowledge_base/statements/` |
| Prinzipien (P) | 57 | Dateizählung `03_knowledge_base/principles/` (inkl. P-S1-001–004) |
| Annahmen (A) | 60 | Dateizählung `03_knowledge_base/assumptions/` |
| Techniken (T) | 47 | Dateizählung `03_knowledge_base/techniques/` |
| Mechanismen (MEC) | 29 | Dateizählung `03_knowledge_base/mechanisms/` |
| Modelle (MOD) | 12 | Dateizählung `03_knowledge_base/models/` |
| **Wissensobjekte gesamt (`03_knowledge_base/`)** | **514** | Übereinstimmend mit `FINAL_PRE_RELEASE_REPORT.md`, Abschnitt 5, und Summenprobe (309+57+60+47+29+12=514) |
| Meta-Modelle (`meta_models/`) | 0 | Kategorie angelegt, noch unbefüllt |
| Kompetenzen (`competencies/`) | 0 | Kategorie angelegt, noch unbefüllt |
| Beobachtungen (`observations/`) | 0 | Kategorie angelegt, noch unbefüllt |
| Selbstreviews (VAL, außerhalb `03_knowledge_base/`) | 15 | Dateizählung repositoryweit, je einer pro Buch (B-0001–B-0015) |

**Dokumentierte Diskrepanz (nicht geglättet):** `00_project/REPOSITORY_KPIS.md` weist eine formelbasierte Summe von 512 aus (Summe der "Objekte gesamt"-KPI-Zeilen je Buch) gegenüber den tatsächlich gezählten 514 Dateien. Die Differenz von 2 wird dort auf die vier S1-SYNTHESIS-Meta-Prinzipien (P-S1-001–004, buchübergreifend, nicht in der Buchformel erfasst) zurückgeführt und ausdrücklich nicht weiter aufgeschlüsselt. Dieser Freeze übernimmt die direkte Dateizählung (514) als maßgeblich, dokumentiert die KPI-Differenz aber als bekannten, unaufgelösten Punkt.

## 6. Anzahl Quellen

**15** Quellobjekte (SRC-0001–SRC-0015), eines pro abgeschlossener Buchanalyse.

**Bekannte strukturelle Anomalie (kein inhaltlicher Mangel):** SRC-0010 (*Thinking, Fast and Slow*) liegt direkt in `02_sources/`, nicht im sonst üblichen Unterordner `02_sources/books/`. Ein externer Audit hatte dies fälschlich als "physisch fehlend" bewertet; die Datei existiert vollständig und korrekt (verifiziert in `EXTERNAL_AUDIT_RESOLUTION_REPORT.md`, Kritikpunkt 1). Die Ordnerplatzierung selbst wurde bewusst nicht verändert (keine Strukturänderung ohne gesonderten Auftrag).

## 7. Anzahl Bücher

**15** vollständig abgeschlossene Buchanalysen (B-0001–B-0015, Status DONE), verifiziert per Ordnerzählung in `04_book_analysis/`.

## 8. Anzahl Modelle

**12** (MOD-0001–MOD-0012).

## 9. Anzahl Mechanismen

**29** (MEC-0001–MEC-0029).

## 10. Anzahl Statements

**309** (ST-0001–ST-0309, mit Lücken durch Nicht-Anlage-Dokumentation an einzelnen Stellen; keine ID-Kollisionen bekannt).

## 11. Anzahl Assumptions

**60** (A-0001–A-0060).

## 12. Anzahl Open Decisions

**12 Open Decisions gesamt (OD-001–OD-012):**

| Status | Anzahl | IDs |
|---|---|---|
| DONE | 4 | OD-001, OD-002, OD-003 (mit dokumentierter Restlücke), OD-004 |
| ERSETZT | 1 | OD-005 → abgelöst durch OD-010 |
| ANGENOMMEN (Entscheidung getroffen, technische Umsetzung ausstehend) | 2 | OD-006 (Meme-Filter), OD-007 (CTX-Ebene) |
| OFFEN (Herausgeber-Entscheidung erforderlich) | 5 | OD-008, OD-009, OD-010, OD-011, OD-012 |

**Für den Freeze relevant:** Keine neue Open Decision wird durch diesen Freeze angelegt (verboten, siehe Sprintauftrag). Die 5 offenen Entscheidungen sind bestehende Altlast, keine neuen Blocker.

## 13. Anzahl Scientific Debt Einträge

**Methodischer Vorbehalt:** `SCIENTIFIC_DEBT.md` führt keine repositoryweite Einzelzählung; verschiedene Sprintberichte verwenden unterschiedliche Zählkonventionen (buchspezifische Zeilen vs. Cluster vs. Gesamttabellenzeilen). Dieser Freeze dokumentiert beide bekannten Zählweisen, statt eine neue, ungeprüfte Einzelzahl zu erfinden:

| Zählweise | Wert | Quelle |
|---|---|---|
| Buchspezifische "Scientific Debt neu"-Summe (B-0001–B-0015, KPI-Formel) | 83 | `REPOSITORY_KPIS.md`, Abschnitt "Repository-weite Summen" |
| Tabellenzeilen gesamt in `SCIENTIFIC_DEBT.md` (alle Abschnitte: 15 Buchsektionen + 6 systemische Cluster SD-SYS-001–006 + W-001-Sektion), objektiv per Skript ausgezählt | 106 (in 23 Einzeltabellen) | Direkte Auszählung durch diesen Freeze-Sprint, 2026-07-04 |
| Scientific-Debt-Einträge mit Priorität "Hoch" | 14 | `FINAL_PRE_RELEASE_REPORT.md`, Abschnitt 5 (Stand 2026-07-03, durch diesen Freeze nicht neu geprüft) |

Systemische Cluster: SD-SYS-001 (Replikationsrisiko proprietärer Studien), SD-SYS-002 (B-0005-Quellenunvollständigkeit), SD-SYS-003 (Meme-Replikations-Zirkelschluss), SD-SYS-004 (Publication Bias CEB/Challenger, JOLT/Tethr), SD-SYS-005 (Nudging-Publication-Bias-Kontroverse), SD-SYS-006 (Konvergenzbestätigungen).

## 14. Status des Research Programs

**Vollständig ausgearbeitet und praktisch validiert.** Governance (`RESEARCH_GOVERNANCE.md`), Decision Policy, neunstufiger Lifecycle (`RESEARCH_LIFECYCLE.md`), Repository-Integrationsmechanik (`REPOSITORY_INTEGRATION.md`) und 11 Templates liegen vor (Research Program Finalization Sprint RC-1, 2026-07-03). Das Programm ist kein theoretisches Konstrukt: W-001 hat den vollständigen Lifecycle (Stufe 1–9) tatsächlich durchlaufen. Aktuell 0 aktive, 1 abgeschlossenes (W-001), 0 archivierte Forschungsprojekte (`RESEARCH_STATUS.md`).

## 15. Status W-001

**Vollständig abgeschlossen** (2026-07-03) — erstes Forschungsprojekt mit vollständigem 9-Stufen-RC-1-Lifecycle inkl. Health Check.

**Editor Decision:** *Teilweise annehmen.* Die mathematische Formalisierung (Socio-Cognitive Sensegiving Model, SCSM) wurde **abgelehnt** (Red-Team-Kritik: 11 von 13 Prüfkriterien nicht erfüllt). Der wissenschaftlich belastbare Kernbefund — diagnoseorientierte (SPIN, Gap Selling) und teaching-/sensemaking-orientierte (Challenger) Vertriebsansätze stehen nicht in universellem Widerspruch, sondern beschreiben kontextabhängige, koexistierende Wirkmechanismen — wurde in 6 bestehende Wissensobjekte integriert (A-0020, P-0021, P-0025, MEC-0013, T-0019, T-0023). Keine neue Grand Theory, kein neues Modell, keine Differentialgleichung.

**Nicht aufgelöste Restfrage (bewusst nicht-blockierend geführt):** Ein direkter empirischer Vergleichstest (RCT) zwischen Diagnose-First und Insight-First existiert weiterhin nicht — als AR-001/Scientific-Debt-Sektion "W-001" dokumentiert, nicht als Freeze-Blocker eingestuft.

## 16. Status aller Audits

| Audit | Datum | Geprüfter Zustand | Ergebnis | Aktualität zum Freeze-Zeitpunkt |
|---|---|---|---|---|
| `CODEX_AUDIT_2026-07.md` | 2026-07-01 | 10 Bücher / 368 Objekte | Gesamtnote B+ | **Veraltet** — Repository seither um ca. 40 % gewachsen (15 Bücher / 514 Objekte); kein neuer Vollaudit seither |
| `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` | 2026-07-01 | 10 Bücher / 368 Objekte | Gesamturteil B | **Veraltet** — benennt W-001 weiterhin als ungelösten "kritischen Punkt", obwohl seit 2026-07-03 governance-seitig entschieden |
| Peer Review Sprint 1 / 2 (`PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`) | 2026-07-01 | Sprint-1-Inhalte | 12 Einzelentscheidungen bearbeitet | Abgeschlossen für den geprüften Scope |
| External Release Audit ("Wissenschaftliche Prüfung des Sales Codex", Framing: Gemini Deep Research) | zugestellt ca. 2026-07-03 | 15 Bücher / 514 Objekte (aktueller Stand) | 7 Kritikpunkte, Gesamteinschätzung des Audits: MAJOR REVISION REQUIRED | Durchgeführt; vollständig gegen Repository verifiziert |
| External Audit Resolution Sprint | 2026-07-03 bis 2026-07-04 | Reaktion auf obige 7 Kritikpunkte | 1 nicht bestätigt, 2 bereits vorab behoben, 2 bestätigt und vollständig behoben, 2 teilweise bestätigt und differenziert korrigiert | **READY FOR FINAL RC-1 AUDIT** |
| **Finaler RC-1-Audit** (`SALES_CODEX_1_0_RELEASE_PLAN.md`, Kapitel 5, Schritt 5) | **noch nicht durchgeführt** | — | — | **Ausstehend — Herausgeberauftrag noch nicht erteilt** (`NEXT_ACTION.md`, Stand 2026-07-04) |

**Wichtig:** Der External Release Audit und der Finale RC-1-Audit sind laut Repository-Dokumentation zwei unterschiedliche Prüfschritte. Der externe Audit prüfte den Zustand vor/während der Konsolidierung punktuell anhand von 7 Kritikpunkten; der Finale RC-1-Audit ist der im Release Plan als eigener Meilenstein (M6) definierte, umfassende Prüfschritt des jetzt eingefrorenen Gesamtzustands — dieser hat noch nicht stattgefunden.

## 17. Bekannte verbleibende Einschränkungen

1. **Finaler RC-1-Audit ausstehend** — siehe Abschnitt 16. Nächster verbindlicher Schritt vor jeder Herausgeber-Freigabe von Version 1.0.
2. **OD-008 bis OD-012 (5 Open Decisions) unentschieden** — keine davon ist laut `SALES_CODEX_1_0_RELEASE_PLAN.md` ein MUST-HAVE-Blocker; alle sind als SHOULD-HAVE oder länger laufende Governance-Fragen eingestuft.
3. **OD-006/OD-007 entschieden, technische Umsetzung ausstehend** — QK-Meme-Filter und CTX-Kontextebene sind Herausgeber-beschlossen, aber bewusst auf einen separaten Framework Integration Sprint nach Version 1.0 verschoben.
4. **Publication-Bias-Grundrisiko unverändert bestehen** (SD-SYS-001, SD-SYS-004) — proprietäre Kernstudien (SPIN/Huthwaite N=35.000, Challenger/CEB N=6.000, JOLT/Tethr-ML) bleiben ohne unabhängige Replikation. Nur die Objektsichtbarkeit (Warnhinweise) wurde hergestellt, nicht das zugrunde liegende Risiko aufgelöst.
5. **W-001-RCT-Lücke** — kein direkter empirischer Vergleichstest Diagnose-First vs. Insight-First, siehe Abschnitt 15.
6. **512-vs-514-Objektzähldifferenz in `REPOSITORY_KPIS.md`** unverändert unaufgelöst dokumentiert.
7. **14 Wissensobjekte (10 Assumptions, 4 Modelle)** trugen bis zum External Audit Resolution Sprint kein templatekonform benanntes Evidenzfeld — jetzt strukturell korrigiert (Transkription bestehender Bewertungen), keine neue Bewertung vorgenommen.
8. **Git-Index-Formatierungsfehler** (`.git/index`) — infrastrukturelles, sandbox-/versionsabhängiges Problem, betrifft nicht Inhalt oder Commit-Historie. Unverändert nicht behoben (außerhalb des Auftragsscopes jedes bisherigen inhaltlichen Sprints).
9. **17 leere Ordner** — laut `REPOSITORY_CONSOLIDATION_IMPLEMENTATION_REPORT_RC1.md` bewusst vorbereitete Struktur, kein Fehlerzustand.
10. **Ordnernummern-Kollisionen** (`04_book_analysis`/`04_synthesis`, `05_publications`/`05_research`) — unverändert unentschieden, Herausgeber-Entscheidung erforderlich, außerhalb des Scopes dieses Freeze.
11. **`book_catalog.md`-Governance-Status ungeklärt** — Katalog wird faktisch nicht mehr als verbindliches Steuerungsinstrument genutzt; keine neue Open Decision hierzu (Sprintauftrags-Beschränkung).
12. **SRC-0010-Ordnerplatzierung** — siehe Abschnitt 6, keine Lücke, aber unverändert inkonsistent mit der sonstigen Konvention.

## 18. Freigabestatus

**EINGEFROREN ALS RELEASE CANDIDATE RC-1.**

Dieser Freigabestatus bedeutet: Der fachliche/wissenschaftliche Entwicklungsstand ist für die Zwecke der Versionsfreigabe 1.0 abgeschlossen und wird ab sofort nicht mehr verändert (siehe `RC1_FREEZE_DECLARATION.md` für die vollständige Regelung zulässiger/unzulässiger Änderungen).

Dieser Freigabestatus bedeutet **nicht**: dass Version 1.0 bereits veröffentlicht ist. Die formale Veröffentlichung erfordert laut `00_project/SALES_CODEX_1_0_RELEASE_PLAN.md` (Kapitel 2.2) zusätzlich (a) einen erfolgreichen Finalen RC-1-Audit und (b) die formale Freigabe-Erklärung des Herausgebers auf dessen Basis. Beides steht noch aus.

---

*Erstellt im Rahmen des Sales Codex Version 1.0 RC-1 Release Candidate Freeze, 2026-07-04. Rolle: Release Manager / Configuration Manager. Keine fachlichen, wissenschaftlichen oder Framework-Änderungen vorgenommen.*
