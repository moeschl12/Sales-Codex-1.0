# SALES CODEX 1.0 RELEASE PLAN

**Dokumentklasse:** Steuerungsdokument (Operational — Pflichtlektüre für jede Session bis Version 1.0 erreicht ist)
**Status:** Aktiv seit 2026-07-03
**Ersetzt:** `00_project/SALES_CODEX_1_0_PROGRAM.md` als aktives Steuerungsdokument. Das Programm-Dokument wird **nicht gelöscht oder überschrieben** — es bleibt unverändert im Repository als historische Planungsgrundlage erhalten (Grundregel: "Dokumentiere Widersprüche/Entwicklung statt sie zu glätten"). Dieser Release Plan ist die konsolidierte Fortschreibung: er übernimmt, was weiterhin gültig ist, markiert explizit, was überholt ist, und ergänzt, was seit dem 2026-07-02-Stand neu hinzugekommen ist.
**Sprint:** Sales Codex 1.0 Release Planning Sprint
**Auftrag:** Ausschließlich Release-Planung für Version 1.0. Keine langfristige Roadmap mehr (das war der Zweck des Vorgänger-Dokuments, Kapitel 10 "Roadmap" — dieser Plan hat bewusst kein Roadmap-Kapitel). Kein Forschungssprint: keine neuen Wissensobjekte, keine neue Literatur, keine Frameworkänderungen, keine Editor Decisions, keine Repository-Umstrukturierungen. Diese Session ist vollständig **read-only** gegenüber dem Repositoryinhalt — die einzige neue Datei ist dieses Dokument selbst.
**Rolle:** Dieses Dokument ist aus der Perspektive eines Product Owner / Release Manager verfasst — nicht als Forscher, Autor oder Reviewer. Es bewertet ausschließlich, welche Arbeit für eine belastbare Veröffentlichung von Version 1.0 tatsächlich noch erforderlich ist.
**Grundlage:** `00_project/SALES_CODEX_1_0_PROGRAM.md` (2026-07-02), `CURRENT_STATE.md`, `00_project/SESSION_LOG.md`, `00_project/changelog.md`, `00_project/OPEN_DECISIONS.md`, `00_project/SCIENTIFIC_DEBT.md`, `00_project/CODEX_AUDIT_2026-07.md`, `00_project/WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`, `00_project/REPOSITORY_CONSOLIDATION_REPORT_RC1.md`, `00_project/REPOSITORY_CONSOLIDATION_IMPLEMENTATION_REPORT_RC1.md`, `00_project/BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md`, `06_research_program/` (Governance, Lifecycle, RESEARCH_STATUS.md), `06_research_program/completed/W001/` (vollständiger Projektordner inkl. `06_EDITOR_DECISION.md`, `REPOSITORY_INTEGRATION_LOG.md`, `W001_REPOSITORY_INTEGRATION_REPORT.md`), `02_sources/book_catalog.md`, `00_project/REPOSITORY_KPIS.md`, direkte Dateisystemzählung von `03_knowledge_base/` und `02_sources/books/` (Stand 2026-07-03).

---

# Kapitel 1 — Executive Summary

## 1.1 Ausgangslage

`SALES_CODEX_1_0_PROGRAM.md` wurde am 2026-07-02 unmittelbar nach dem Governance Sprint erstellt und beschrieb einen Repositoryzustand von 10 Büchern, 368 Wissensobjekten, sechs offenen Herausgeber-Entscheidungen (OD-006 bis OD-011) und zwei ungelösten Tier-1-Blockern (W-001, Publication-Bias-Abhängigkeit). Es definierte fünf Phasen (Governance → Scientific Completion → Architecture Freeze → Release Candidate → Version 1.0) und eine zehnteilige Roadmap.

Seit diesem Datum haben **fünf weitere abgeschlossene Sprints** den Zustand des Repositorys verändert — teils in einer Weise, die das Programm-Dokument nicht mehr korrekt beschreibt:

1. **Behavioral Science Expansion Sprint 1** (2026-07-02, unmittelbar nach Erstellung des Programm-Dokuments): fünf weitere Buchanalysen abgeschlossen — B-0011 (Emotional Intelligence), B-0012 (Predictably Irrational), B-0013 (Nudge: The Final Edition), B-0014 (Priceless), B-0015 (Made to Stick). Der Codex umfasst damit **15 Bücher**, nicht 10.
2. **Behavioral Science Review Sprint** (2026-07-02): externes wissenschaftliches Gutachten zu SPR-0003 geprüft, acht Editor Decisions getroffen und umgesetzt (4× übernehmen, 3× teilweise übernehmen, 1× ablehnen — u. a. MEC-0025-Umbenennung in "Altruistische Bestrafung", zwei MOD-Klassifikationshinweise, drei Boundary-Condition-Ergänzungen, ein präzisierter Scientific-Debt-Status).
3. **Repository Consolidation Sprint 2** (2026-07-02): acht Editor Decisions aus Sprint 1 umgesetzt — leerer Duplikat-Ordner und eine Zero-Byte-Datei gelöscht, `codex_knowledge_model.md` nach `99_archive/` verschoben, drei fehlplatzierte Dateien in passende Buchordner verschoben, drei Dateien archiviert. Ein vorbestehender, nicht durch diesen Sprint verursachter Git-Index-Formatfehler wurde entdeckt und dokumentiert.
4. **Research Program Finalization Sprint (RC-1)** (2026-07-03): das Research Program (`06_research_program/`) vollständig, methodisch konsistent und skalierbar ausgearbeitet — neunstufiger Lifecycle, Governance, Decision Policy, Repository-Integrationsmechanik, elf Templates.
5. **Research Project W-001 Completion Sprint + Repository Integration Sprint (Post Editor Decision)** (2026-07-03): Der Herausgeber hat die Editor Decision zu W-001 tatsächlich getroffen — **Teilweise annehmen**. Die mathematische Formalisierung (SCSM) wurde abgelehnt; der Kernbefund (Diagnose- und Teaching-/Sensemaking-Ansätze stehen nicht in universellem Widerspruch, sondern sind kontextabhängig koexistent) wurde in sechs bestehende Wissensobjekte integriert (A-0020, P-0021, P-0025, MEC-0013, T-0019, T-0023). W-001 ist damit **das erste Forschungsprojekt, das den vollständigen neunstufigen RC-1 Research Lifecycle erfolgreich durchlaufen hat** — von Research Question/Hypothese bis Health Check und Ordnerübergang nach `completed/`.

## 1.2 Was seit dem ursprünglichen Programm tatsächlich erreicht wurde

| Bereich | Stand 2026-07-02 (Programm-Dokument) | Stand 2026-07-03 (dieser Plan) |
|---|---|---|
| Bücher | 10 (B-0001–B-0010) | **15** (B-0001–B-0015) — verifiziert per Ordnerzählung in `04_book_analysis/` |
| Wissensobjekte gesamt | 368 (201 ST, 48 A, 21 MEC, 47 P, 41 T, 10 MOD) | **514** (309 ST, 60 A, 29 MEC, 57 P, 47 T, 12 MOD) — verifiziert per Dateizählung in `03_knowledge_base/` |
| SRC-Quellobjekte | 10 | 14 vorhanden, **SRC-0010 fehlt weiterhin** (dokumentierte Repository-Anomalie seit B-0011, siehe Kapitel 7) |
| W-001 | Ungelöst, Blocker B1 | **Editor Decision getroffen und integriert** — Blocker auf Governance-Ebene geschlossen (Nuancen siehe Kapitel 4) |
| Repository-Hygiene (Duplikat-Ordner, `codex_knowledge_model.md`) | Unentschieden, Blocker B6 | **Entschieden und umgesetzt** (Repository Consolidation Sprint 2) |
| Open Decisions | 6 offen (OD-006–011) | **7 offen** (OD-006–012 — OD-012 neu durch die W-001-Integration selbst entstanden) |
| Research Program | Governance ausgearbeitet, aber noch nie praktisch durchlaufen | **Praktisch validiert** — W-001 hat den vollständigen Lifecycle durchlaufen |
| Repository-Audit | `CODEX_AUDIT_2026-07.md` (2026-07-01), Gesamtnote B+ | **Unverändert** — kein neuer Audit seit Behavioral Science Expansion, Consolidation Sprint 2 oder W-001-Abschluss durchgeführt |
| Wissenschaftlicher Reifegradbericht | `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (2026-07-01), Gesamturteil B | **Unverändert** — die dort als "kritischer Punkt" benannte interne Konsistenz (W-001) ist inzwischen governance-seitig geklärt, der Bericht selbst spiegelt das noch nicht wider |

## 1.3 Überholte Annahmen im ursprünglichen Programm

- **"10 Buchanalysen" und "368 Wissensobjekte"** sind durch die Behavioral Science Expansion überholt (15 Bücher, 514 Objekte). Jede quantitative Aussage im Programm-Dokument, die sich auf diese Zahlen stützt (Kapitel 3, 5, 11, 12), ist zum jetzigen Zeitpunkt eine Untererfassung.
- **"W-001 (Teach First vs. Diagnose First) ungelöst" (Blocker B1)** ist überholt. W-001 hat eine tatsächliche Editor Decision und eine abgeschlossene Repository Integration. Nicht überholt ist die tiefer liegende akademische Frage (AR-001: direkter empirischer Vergleichstest Diagnose-First vs. Insight-First mit Primärtext) — diese ist weiterhin offen, aber jetzt als eigenständiger, nicht-blockierender Scientific-Debt-Posten geführt (siehe Kapitel 4).
- **"Duplikat-Ordner und `codex_knowledge_model.md` unentschieden" (Blocker B6)** ist überholt — beide sind entschieden und umgesetzt.
- **"6 aktiv offene Entscheidungen" (OD-006–011)** ist überholt — es sind jetzt 7 (OD-006–012), da die W-001-Integration selbst eine neue, im vorherigen Integrationsplan bereits angekündigte Open Decision (OD-012) erzeugt hat.
- **Die Referenz auf `CODEX_AUDIT_2026-07.md` (B+) und `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (B)** als aktuelle Qualitätsindikatoren ist nicht falsch, aber **veraltet**: Beide Dokumente bewerten einen Repositoryzustand, der seither um 5 Bücher, 146 Wissensobjekte, einen vollständigen Research-Program-Durchlauf und mehrere Konsolidierungssprints gewachsen ist. Kein Audit hat den aktuellen Zustand geprüft.
- **`02_sources/book_catalog.md`** zeigt weiterhin überwiegend `WAITING`/`IN_PROGRESS`-Status für Bücher, die tatsächlich längst abgeschlossen sind (B-0001–B-0015 existieren alle als vollständige `04_book_analysis/`-Ordner) — dieses Dokument wurde seit den frühesten Sprints nicht mehr gepflegt und ist keine verlässliche Statusquelle mehr.
- **`00_project/REPOSITORY_KPIS.md`** enthält nur Messwerte für B-0001 und B-0002 (Stand 2026-06-30) — für 13 der 15 Bücher liegen keine KPI-Werte vor.

## 1.4 Abgeschlossene Meilensteine (im Sinne des Sprint-Kontexts)

Die im Auftrag genannten sechs Meilensteine sind alle **im Sinne "ein Sprint mit diesem Namen wurde durchgeführt und dokumentiert"** abgeschlossen. Das ist nicht identisch mit "keine offenen Punkte mehr" — jeder Meilenstein hinterlässt bekannte, dokumentierte Restarbeit (Details je Meilenstein: Kapitel 4).

| Meilenstein | Abgeschlossen als Sprint? | Restarbeit vorhanden? |
|---|---|---|
| Academic Recovery | Ja (Phase 1, Phase 2, Sprint-3-Review) | Ja — AR-001, AR-002, AR-013 (Tier 1) weiterhin auf Abstract-Ebene |
| Behavioral Science Expansion | Ja (5/5 Bücher) | Ja — Terminologie-Nachziehung MEC-0025 in Folgeobjekten, Boundary-Conditions-Ausweitung auf weitere Objekte |
| Repository Consolidation | Ja (Sprint 1 Audit + Sprint 2 Implementation) | Ja — mehrere ausdrücklich außerhalb des Scopes belassene Punkte (Ordnernummern-Kollision, `book_catalog.md`, Onboarding-Dokumente, Git-Index-Fehler) |
| Research Program RC-1 | Ja (Governance vollständig ausgearbeitet) | Nein für die Governance selbst — jetzt zusätzlich praktisch validiert durch W-001 |
| W-001 vollständig abgeschlossen | Ja | Ja — AR-001 (akademische Tiefenfrage), OD-012 (Formalisierungsfrage), OQ-2 bis OQ-4 (Scientific Debt) |
| Erstes Projekt mit vollständigem 9-stufigem RC-1 Lifecycle | Ja — W-001 | Nein — diese Aussage ist selbst das Ergebnis, keine offene Restarbeit |

---

# Kapitel 2 — Version 1.0 Definition

## 2.1 Was Version 1.0 fachlich bedeutet

Version 1.0 des Sales Codex ist **kein technisches Software-Release** — es gibt keinen Code, der ausgeliefert wird. Version 1.0 ist eine **redaktionelle und wissenschaftliche Reifegrad-Aussage**: der Herausgeber erklärt, dass das Repository in seiner Gesamtheit als vertrauenswürdige, in sich konsistente Wissensbasis an einen neuen Leser — menschlich oder KI — übergeben werden kann, ohne dass dieser Leser zunächst selbst herausfinden muss, welche Teile davon Stand, welche Altlast und welche bloß Behauptung sind.

Konkret muss Version 1.0 folgende Eigenschaften besitzen:

1. **Ehrlich über den eigenen Beleg-Status.** Jede Aussage trägt eine Evidenzklasse; die Benennung dieser Klasse ist repositoryweit einheitlich, nicht in fünf verschiedenen Feldnamen zersplittert. Ein Leser muss nicht raten, ob "Evidenzlevel", "Evidenzklasse" und "Evidenzgrad" dasselbe meinen.
2. **Widersprüche adressiert, nicht versteckt.** Jeder als methodischer Kernkonflikt dokumentierte Widerspruch zwischen den verarbeiteten Quellen (W-001 bis W-005) trägt eine nachvollziehbare Herausgeber-Position — nicht zwingend eine Auflösung im Sinne von "eine Seite hat gewonnen", aber mindestens eine belastbare Aussage darüber, wann welche Seite gilt oder warum die Frage offenbleibt.
3. **Governance ohne Implizites.** Jede Entscheidung darüber, was in den Kanon aufgenommen wird und was nicht, ist nachvollziehbar — durch ein Editor-Decision-Dokument, einen Scientific-Debt-Eintrag oder eine Open Decision, nicht durch stillschweigendes Weglassen.
4. **Keine verschleierte Abhängigkeit von unreplizierten Quellen.** Wo die zentrale B2B-Methodik (SPIN, Challenger, JOLT) auf proprietären, nicht unabhängig peer-reviewten Datensätzen beruht, ist das explizit, an prominenter Stelle, dokumentiert — nicht nur in einer tief verschachtelten Debt-Tabelle.
5. **Navigierbar und strukturell hygienisch.** Ein neuer Leser (Mensch oder KI-Session) findet keine verwaisten Ordner, keine zwei widersprüchlichen Versionen desselben Referenzdokuments ohne Statusmarkierung, und die Steuerdokumente (`book_catalog.md`, `CURRENT_STATE.md`) spiegeln die tatsächliche Repository-Realität.
6. **Einmal end-to-end durch einen frischen, skeptischen Blick geprüft.** Ein vollständiger, unabhängig durchgeführter Audit bestätigt den behaupteten Zustand — nicht nur die Summe der Einzel-Sprintberichte, die jeweils ihren eigenen engen Scope für sich selbst als erfolgreich bewerten.

## 2.2 Wann gilt Version 1.0 als veröffentlicht?

Version 1.0 gilt als veröffentlicht, wenn — und ausschließlich wenn — **der Herausgeber (Felix) dies auf Basis eines RC1-Audits formal erklärt**. Diese Erklärung ist niemals eine KI-Selbsteinschätzung (Grundregel des Projekts: "Keine eigene Erinnerung als Autorität" gilt analog für "keine eigene Reifeeinschätzung als Autorität"). Der formale Auslöser ist:

- `CURRENT_STATE.md` erhält den Vermerk "Sales-Codex-Version: 1.0 (freigegeben [Datum])" als eigenständiges Feld neben der Framework-Version (aktuell 1.1 — beide Versionsachsen bleiben getrennt, siehe `SALES_CODEX_1_0_PROGRAM.md` Kapitel 9, weiterhin gültig).
- Diese Eintragung erfolgt erst, nachdem alle in Kapitel 3 dieses Plans als MUST HAVE eingestuften Punkte erfüllt sind und ein RC1-Audit keine neuen, unadressierten Blocker findet.

**Was Version 1.0 explizit NICHT bedeutet:** Es bedeutet nicht, dass keine wissenschaftliche Unsicherheit mehr besteht (Scientific Debt ist ein dauerhaftes, gewolltes Merkmal des Systems, kein abzuschaffender Mangel — siehe Vision, `SALES_CODEX_1_0_PROGRAM.md` Kapitel 1). Es bedeutet auch nicht, dass alle Domänen abgedeckt sind (Account Management, Pricing Psychology, Digital Sales bleiben bewusst außerhalb des Scopes). Version 1.0 heißt: **das System weiß ehrlich und konsistent, was es weiß, was es nicht weiß, und warum.**

---

# Kapitel 3 — Release Scope

Bewertung aller offenen Themen aus dem Vorgänger-Programm sowie neu entstandener Themen (insbesondere OD-012, aktualisierte Buch-/Objektzahlen). Jede Einstufung mit Begründung.

## 3.1 MUST HAVE

| # | Thema | Begründung |
|---|---|---|
| M1 | **Publication-Bias-Klärung proprietärer B2B-Kernmethodik** (SPIN/Huthwaite, Challenger/CEB, JOLT/Tethr — SD-SYS-001, SD-SYS-004) | Unverändert aus dem Vorgänger-Programm (dort B2). Betrifft die drei am häufigsten zitierten Methodologie-Quellen des gesamten Codex. Ein System, das sich "wissenschaftlich kuratiert" nennt (Vision, Kapitel 1), kann diese strukturelle Abhängigkeit nicht unadressiert in eine 1.0-Version tragen. Mindestanforderung: entweder eine Primärtext-gestützte Einordnung (AR-002) oder eine explizit begründete, mit dem Herausgeber abgestimmte Dokumentation der Nicht-Auflösbarkeit — beides ist bisher nicht erfolgt. |
| M2 | **OD-006 (Meme-Filter für QK-Rating)** — Herausgeber-Entscheidung | Unverändert kritisch: betrifft direkt P-S1-001 (Cost of Inaction), die am stärksten konvergierte Einzelaussage des gesamten Codex. Eine 1.0-Version, die ihre stärkste Konvergenzbehauptung mit einer seit Wochen entscheidungsreifen, aber unentschiedenen Frage stehen lässt, wäre nicht vertretbar. |
| M3 | **OD-007 (CTX-Ebene)** — Herausgeber-Entscheidung | Unverändert kritisch: betrifft direkt die schwächste Reifegrad-Dimension (Generalisierbarkeit, C+). Die wissenschaftliche Analyse liegt seit dem Behavioral-Science-Review-Sprint vollständig ausgearbeitet vor (drei Optionen); es fehlt ausschließlich die Entscheidung. |
| M4 | **Repository-weite Evidenzfeld-Vereinheitlichung** | Unverändert aus dem Vorgänger-Programm (dort B5), aber **Scope-Neubewertung erforderlich**: Die ursprüngliche Schätzung ("~60 verbleibende Objekte") stammt aus einem 368-Objekte-Repository; das Repository trägt inzwischen 514 Objekte, davon 146 durch die Behavioral Science Expansion neu hinzugekommen, deren Feldnamens-Konsistenz nicht mehr geprüft wurde als die ursprüngliche Schätzung entstand. Reine Konsistenzarbeit, kein Recherche- oder Framework-Aufwand — aber der tatsächliche Umfang muss vor der Architecture-Freeze-Phase neu ermittelt werden. |
| M5 | **SD-B010-001 (Priming-Replikationskrise, MEC-0018) — sichtbare Warnung am Objekt** | War im Vorgänger-Programm bereits Teil der Definition of Done (Kapitel 11, Kriterium 2), wurde aber in dessen eigener Blocker-Liste (Kapitel 6) nicht als eigenständiger Blocker geführt — eine interne Inkonsistenz des Vorgänger-Dokuments, die dieser Plan korrigiert. Stichprobenprüfung in diesem Sprint zeigt: **MEC-0018 trägt aktuell keine sichtbare Warnung**, sondern im Gegenteil die Einstufung "E4 (assoziative Priming-Forschung: extrem gut repliziert)" — ein direkter, ungelöster Widerspruch zur in `SCIENTIFIC_DEBT.md` dokumentierten "Hoch"-Priorität-Sorge um Priming-Replikation. Dieser Widerspruch besteht am Objekt selbst, nicht nur zwischen Objekt und Debt-Liste, und ist damit MUST, nicht SHOULD. |
| M6 | **Ein vollständiger, aktueller RC1-Audit** | Der letzte Audit (`CODEX_AUDIT_2026-07.md`, 2026-07-01) bewertet einen Zustand von 10 Büchern/368 Objekten, der seither um 50 % (Objekte) gewachsen ist. Ohne einen Audit, der den *aktuellen* Zustand (15 Bücher/514 Objekte, inkl. Behavioral Science Expansion, Consolidation Sprint 2, W-001-Integration) prüft, ist jede 1.0-Freigabe eine Freigabe auf Basis veralteter Qualitätsdaten. |
| M7 | **Herausgeber-Freigabe** | Definitorisch — siehe Kapitel 2.2. Keine KI-Instanz kann Version 1.0 selbst erklären. |

## 3.2 SHOULD HAVE

| # | Thema | Begründung |
|---|---|---|
| S1 | **OD-009 (Framework RC1 / Reifegrad-Statusübergang)** | Bereits im Vorgänger-Programm als "kein Blocker im engeren Sinn" eingestuft (dessen Kapitel 6, Fußnote) und durch das Programm-Dokument selbst (Kapitel 9) bereits weitgehend inhaltlich vorbeantwortet. Eine formale Bestätigung ist wünschenswert, blockiert aber keine inhaltliche Kernaussage. |
| S2 | **OD-010 (Validierungs-Governance)** | Reine Methodik-/Kadenzfrage für die Zeit *nach* 1.0 (siehe `SALES_CODEX_1_0_PROGRAM.md` Kapitel 8). Ihre Nichtentscheidung verhindert nicht, dass der aktuelle Inhalt vertretbar ist. |
| S3 | **OD-011 (Literature-Governance, Status von `LITERATURE_INDEX.md`)** | Strukturelle Verhältnisfrage zwischen drei bereits bestehenden, unabhängig funktionierenden Dokumenten (`SCIENTIFIC_DEBT.md`, `review_queue.md`, `LITERATURE_INDEX.md`). Kein Inhalt geht verloren, wenn diese Frage erst nach 1.0 entschieden wird. |
| S4 | **OD-012 (Formalisierung der Kontextspezialisierung P-0021/P-0025, MEC-0013/MEC-0001)** | Neu entstanden durch die W-001-Integration. Die zugrunde liegende inhaltliche Frage ist bereits gelöst (Editor Decision, integriert); OD-012 betrifft ausschließlich, ob diese Lösung zusätzlich strukturell (statt nur als Freitext) markiert werden soll — eine kosmetische, nicht inhaltsverändernde Frage. |
| S5 | **`book_catalog.md` und `REPOSITORY_KPIS.md` mit der Repository-Realität synchronisieren** | Betrifft nicht die wissenschaftliche Substanz des Codex, sondern die Navigierbarkeit für künftige Sessions (Kapitel 2.1, Eigenschaft 5). Eine veraltete Statusliste ist ein Verwechslungsrisiko, kein Vertretbarkeitsrisiko der Kerninhalte — sollte aber vor oder kurz nach 1.0 behoben werden, um genau das Kontinuitätsproblem zu vermeiden, das der Codex laut eigener Vision lösen will. |
| S6 | **Aktualisierung von `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`** (mindestens Erratum/Nachtrag zur W-001-Auflösung) | Der Bericht benennt W-001 explizit als "kritischen Punkt" der Dimension "Interne Konsistenz" — dieser Punkt ist inzwischen governance-seitig geklärt. Eine vollständige Neubewertung ist nicht erforderlich (das leistet der RC1-Audit, M6), aber ein Nachtrag verhindert, dass ein zentrales Qualitätsdokument eine überholte Kernaussage unkommentiert stehen lässt. |
| S7 | **AR-001/AR-013 gemeinsame Volltextbearbeitung** (Plouffe et al. 2013, Tversky & Shafir 1992) | Vertieft die W-001-Frage akademisch über die jetzt getroffene Editor Decision hinaus. Nicht blockierend, weil die Editor Decision bereits eine belastbare, herausgeber-abgestimmte Kontextlösung liefert (Kriterium aus Kapitel 2.1, Punkt 2, ist bereits erfüllt) — aber eine wertvolle Vertiefung für 1.1. |

## 3.3 COULD HAVE

| # | Thema | Begründung |
|---|---|---|
| C1 | **Terminologie-Nachziehung "Altruistische Bestrafung"** in P-0051, A-0056, fünf ST-Objekten und historischen B-0014-Sprintartefakten | Bereits als Folgeaufgabe im Behavioral Science Review Sprint dokumentiert. Rein redaktionell, keine inhaltliche Unschärfe (der Kausalpfad war nie falsch, nur der Name teilweise inkonsistent). |
| C2 | **Boundary-Conditions-Ausweitung Individual→Organisation** auf weitere Mechanismen (MEC-0023 bis MEC-0029, MOD-0011, MOD-0012) über die drei bereits bearbeiteten hinaus | Bereits als Folgeaufgabe dokumentiert. Verbessert Präzision, aber keine der drei bereits bearbeiteten Objekte (MEC-0002, MEC-0021, MEC-0022) war vorher falsch — reine Vertiefung. |
| C3 | **Formales Repository-Health-Check-Protokoll** (repositoryweit, nicht projektspezifisch — vgl. OD-003-Restlücke) | Nützlich, aber das Research Program hat mit dem projektspezifischen Health Check (Stufe 9) bereits ein funktionierendes Muster geliefert, das sich erweitern ließe. Kein Blocker für 1.0, da keine der bisherigen Freigaben (Consolidation Sprint 2, W-001) darunter gelitten hat, dass dieses Protokoll fehlt — jeder Sprint hat stattdessen eine Ad-hoc-Prüfung dokumentiert, die funktional äquivalent war. |
| C4 | **Websuch-Verifikation von Harms & Credé (2010), Landy (2005), Locke (2005)** (Konstruktvalidität-EI-Scientific-Debt-Eintrag) | Aktuell mit explizitem Quellenvorbehalt geführt, nicht als geprüfte Primärquelle. Verbessert die Belegqualität eines bereits transparent gekennzeichneten Debt-Eintrags — kein akuter Mangel. |

## 3.4 WON'T HAVE (Version >1.0)

| # | Thema | Begründung |
|---|---|---|
| W1 | **AR-003 bis AR-012** (Tier 2–4 des Academic Recovery Plan) | Unverändert aus dem Vorgänger-Programm (dort N1). Vertieft einen funktionierenden Teil, schließt keine Kernlücke. |
| W2 | **OD-008-Umsetzung** (ELM/Trust Formation/PKM als eigener Sprint) | Unverändert aus dem Vorgänger-Programm (dort N2). Die *Entscheidung* selbst gehört zu M2/M3-Kategorie-Governance-Fragen (siehe SHOULD-Bewertung analog OD-009/010/011), ihre *Umsetzung* ist explizit Post-1.0. |
| W3 | **Vollständige akademische Auflösung der Priming-Replikationsdebatte** | Unverändert aus dem Vorgänger-Programm (dort N4). Der Codex kann eine laufende akademische Kontroverse nicht selbst entscheiden — nur sichtbar vor ihr warnen (siehe M5). |
| W4 | **Domänenerweiterungen** (Account Management, Pricing Psychology B2B, Digital Sales/Inside Sales) | Unverändert aus dem Vorgänger-Programm (dort N5). Nie Teil des bestehenden Anspruchs. |
| W5 | **Geografisch-kulturelle Diversifizierung des Literaturkorpus** | Unverändert aus dem Vorgänger-Programm (dort N7). Niedrigste Priorität laut externem Gutachten selbst. |
| W6 | **Erreichen der Reifegrad-Note "A-"** | Unverändert aus dem Vorgänger-Programm (Kapitel 11, "ausdrücklich nicht Teil der DoD"). Eine transparent dokumentierte B(+)-Basis mit geschlossenen Kernlücken ist für 1.0 ausreichend. |
| W7 | **Neue Buchanalysen** (B-0016 und folgende aus `book_catalog.md`) | Kein neues Inhaltswachstum vor 1.0 — jede weitere Buchanalyse vor Abschluss der Konsistenzarbeit (M4, M6) würde die zu prüfende Objektmenge während der laufenden Freeze-Phase weiter vergrößern, analog zur bereits eingetretenen Verzögerung durch die Behavioral Science Expansion zwischen Programm-Erstellung und RC1-Audit. |

---

# Kapitel 4 — Release Blocker

Prüfung aller bekannten Blocker aus dem Vorgänger-Programm sowie der acht im Auftrag namentlich genannten Bereiche. Status je Blocker: **erledigt** / **teilweise erledigt** / **weiterhin Blocker** / **entfällt**.

## 4.1 W-001

**Status: teilweise erledigt.**

Die governance-seitige Blockade (keine Editor Decision, keine Repository Integration) ist **erledigt**: Der Herausgeber hat entschieden (Teilweise annehmen, 2026-07-03), sechs Objekte wurden erweitert, ein Abschluss-Health-Check wurde bestanden, das Projekt liegt in `completed/`. Die im Vorgänger-Programm formulierte Definition-of-Done-Bedingung ("W-001 trägt einen Bearbeitungsvermerk, der über Abstract-Ebene hinausgeht — entweder inhaltliche Präzisierung mit Primärtext-Beleg oder explizit begründete, mit Felix abgestimmte Dokumentation") ist durch die tatsächlich getroffene, begründete Editor Decision erfüllt — dies ist per Definition eine "mit Felix abgestimmte Dokumentation", auch wenn sie keine neue Primärtext-Auswertung war.

**Nicht erledigt** ist die tiefere akademische Frage (AR-001: direkter empirischer Vergleichstest Diagnose-First vs. Insight-First, Volltextprüfung Plouffe et al. 2013) — diese bleibt als eigenständiger, jetzt in `SCIENTIFIC_DEBT.md` (Sektion "W-001") geführter, ausdrücklich **nicht-blockierender** Posten offen (siehe Kapitel 3.2, S7).

## 4.2 Research Program

**Status: erledigt** (als Infrastruktur) **— mit einem Datenpunkt.**

Governance, Lifecycle (9 Stufen), Decision Policy, Repository-Integrationsmechanik und elf Templates sind vollständig ausgearbeitet (RC-1 Finalization Sprint) und jetzt **praktisch validiert**: W-001 hat als erstes Projekt den vollständigen Lifecycle durchlaufen, inklusive einer echten, nicht nur simulierten Editor Decision und Integration. Das Research Program ist damit kein theoretisches Konstrukt mehr, sondern ein erprobter Prozess. Kein offener Blocker.

## 4.3 Repository Consolidation

**Status: erledigt** (für den freigegebenen Scope) **— mit dokumentierten, bewusst ausgeschlossenen Restpunkten.**

Acht Editor Decisions vollständig umgesetzt (Repository Consolidation Sprint 2). Ausdrücklich außerhalb des Scopes verbliebene Punkte (unverändert seit Sprint 1/2, keine neue Verschlechterung): Nummernkollision oberster Ebene (`04_book_analysis`/`04_synthesis`, `05_publications`/`05_research`), `book_catalog.md`-Divergenz (siehe M5/S5), vier widersprüchliche Onboarding-Dokumente, `PROJECT_BOOTSTRAP.md`-Pfadtabelle, `00_project/`-Binnenstruktur, Governance-Cluster-Überlappung (`SESSION_LOG.md`/`changelog.md`), Buchordner-Namenskonvention, vorbestehender Git-Index-Formatfehler. Keiner dieser Punkte wird durch dieses Release-Plan-Dokument als neuer Blocker eingestuft — sie sind Repository-Hygiene-Fragen ohne inhaltliches Risiko, konsistent mit ihrer bisherigen Einordnung.

## 4.4 Behavioral Science

**Status: erledigt** (Expansion + externes Review) **— mit COULD-HAVE-Folgeaufgaben (siehe Kapitel 3.3, C1/C2).**

Fünf Bücher abgeschlossen, externes Gutachten geprüft und in acht Editor Decisions verarbeitet, alle umgesetzt. Kein offener Blocker — die verbliebenen Folgeaufgaben (Terminologie-Nachziehung, Boundary-Conditions-Ausweitung) sind redaktionelle Vertiefungen, keine Lücken mit Vertretbarkeitsrisiko.

## 4.5 Academic Recovery

**Status: teilweise erledigt.**

Phase 1, Phase 2 und ein Sprint-3-Einzelreview sind abgeschlossen. Die drei als Tier 1 identifizierten Punkte (AR-001, AR-002, AR-013) haben jedoch weiterhin **nicht** den Status "mit Primärtext bearbeitet" erreicht — sie verbleiben auf Abstract-Ebene. AR-002 (Publication-Bias-Klärung) ist deckungsgleich mit Blocker M1 (weiterhin Blocker). AR-001 ist durch die W-001-Editor-Decision governance-seitig entschärft, akademisch aber weiterhin offen (nicht-blockierend, siehe 4.1). AR-013 ist eine reine Literaturvertiefung ohne bekannte Blockadewirkung.

## 4.6 Open Decisions

**Status: teilweise erledigt.**

4 von 12 Einträgen tragen den Status DONE (OD-001–004), 1 weiterer ERSETZT (OD-005 → OD-010). **7 von 12 sind weiterhin offen** (OD-006 bis OD-012) — eine Verschlechterung der reinen Zahl gegenüber dem Vorgänger-Programm (dort 6 offene), aber nicht inhaltlich: OD-012 ist neu und selbst das Ergebnis einer erfolgreichen Integration (W-001), keine neue ungelöste Altlast. Von den 7 offenen Einträgen sind zwei (OD-006, OD-007) als MUST HAVE eingestuft (Kapitel 3.1), vier (OD-009, OD-010, OD-011, OD-012) als SHOULD HAVE (Kapitel 3.2), keiner als reiner Blocker im Sinne "verhindert 1.0 vollständig, wenn nicht gelöst" — außer OD-006/007.

## 4.7 Scientific Debt

**Status: teilweise erledigt.**

Die Debt-Matrix ist auf 15 buchspezifische Sektionen, 6 systemische Cluster (SD-SYS-001 bis SD-SYS-006) und eine neue W-001-Sektion angewachsen — deutlich mehr Einzeleinträge als die im Vorgänger-Programm zitierten "56 individuelle Zeilen + 6 Cluster" (nicht neu gezählt in diesem Sprint, da eine exakte Neuzählung Research-/Audit-Charakter hätte; die Größenordnung ist erkennbar gewachsen). Die als Tier 1 eingestuften Cluster (SD-SYS-001, SD-SYS-004, SD-B010-001) sind **unverändert unbearbeitet** — SD-B010-001 zusätzlich mit der in Kapitel 3.1 (M5) dokumentierten, neu festgestellten Diskrepanz am Objekt MEC-0018 selbst. W-001 als Debt-relevanter Punkt ist durch die Integration in einen eigenen, klar strukturierten Abschnitt überführt worden (siehe 4.1).

## 4.8 Framework

**Status: entfällt als eigenständiger Blocker.**

Das Vorgänger-Programm führte "Framework" nicht als eigenständigen nummerierten Blocker (B1–B6), sondern nur implizit über die Versionsklärung (Kapitel 9) und die Evidenzfeld-Frage (B5). Die Framework-Version (1.1, eingefroren 2026-06-30) ist seit Erstellung des Vorgänger-Programms unverändert — keine neue Framework-Änderung wurde in einem der fünf seither abgeschlossenen Sprints vorgenommen (Research Program RC-1 hat eigene, programmweite Governance-Dateien ergänzt, aber das Kern-Framework — Operating Manual, Canonical Knowledge Model — nur um punktuelle, in RC-1 selbst begründete Integrationshinweise erweitert, keine Kernlogik verändert). Kein neuer, eigenständiger Framework-Blocker identifiziert; die relevante Restarbeit ist bereits unter M4 (Evidenzfeld-Vereinheitlichung) und S1 (OD-009-Versionsklärung) erfasst.

---

# Kapitel 5 — Critical Path

Kürzester realistischer Weg zu Version 1.0 — ausschließlich MUST-HAVE-Schritte aus Kapitel 3.1, in notwendiger Reihenfolge. Keine SHOULD/COULD-Punkte, auch wenn wertvoll.

1. **Herausgeber-Entscheidungsrunde zu OD-006 und OD-007** (M2, M3). Beide sind bereits vollständig entscheidungsreif (alle Optionen ausgearbeitet, keine weitere Recherche nötig) — reiner Entscheidungsschritt, kein Rechercheaufwand. Muss zuerst erfolgen, da nachfolgende Konsistenzarbeit (Schritt 3) von der OD-007-Entscheidung abhängen könnte, falls sie eine neue CTX-Feldstruktur nach sich zieht.
2. **AR-002-Volltextauswertung oder begründete Nicht-Auflösbarkeits-Dokumentation** (M1). Ohiomah et al. (2020) und/oder Marcos-Cuevas et al. (2023) mit der spezifischen Frage, ob und wie diese Meta-Analysen CEB/Challenger/JOLT-artige proprietäre Befunde einordnen. Falls keine auflösende Quelle gefunden wird: explizite, mit dem Herausgeber abgestimmte Dokumentation nach demselben Muster, das für W-001 bereits erfolgreich angewendet wurde.
3. **MEC-0018-Korrektur** (M5). Den festgestellten Widerspruch (E4-"extrem gut repliziert"-Einstufung vs. dokumentierte Priming-Replikationskrise in `SCIENTIFIC_DEBT.md`) auflösen: entweder Einstufung korrigieren oder explizit begründen, warum die widersprüchliche Formulierung Bestand hat, plus sichtbare Warnung direkt am Objekt.
4. **Scope-Neuermittlung und Durchführung der Evidenzfeld-Vereinheitlichung** (M4). Zunächst feststellen, wie viele der 514 (nicht mehr 368) Objekte tatsächlich noch uneinheitliche Feldnamen tragen (dies selbst ist eine kurze Bestandsaufnahme, keine inhaltliche Recherche), dann Vereinheitlichung durchführen.
5. **RC1-Audit** (M6), erst nach Abschluss der Schritte 1–4 — ein Audit vor Abschluss dieser Schritte würde nur dieselben, bereits bekannten Blocker erneut auflisten und keinen zusätzlichen Erkenntniswert liefern.
6. **Herausgeber-Freigabe** (M7) auf Basis des RC1-Audits aus Schritt 5.

**Kein zusätzlicher Schritt für Meilenstein-Wiederholung nötig:** Behavioral Science Expansion, Repository Consolidation und Research Program RC-1 sind für den Critical Path bereits abgeschlossen (Kapitel 4) und werden nicht erneut aufgeführt.

---

# Kapitel 6 — Version 1.1 Backlog

Bewusst auf nach Version 1.0 verschobene Themen, mit expliziter Begründung, warum sie nicht Teil von 1.0 sind (Zusammenfassung aus Kapitel 3.3/3.4, hier als Backlog-Liste für die Zeit nach der Freigabe):

1. **AR-003 bis AR-012** (Buying-Center-Cluster, weitere Behavioral-Economics-Vertiefung, geografische Diversifizierung) — vertiefen einen bereits funktionierenden Teil, schließen keine der für 1.0 identifizierten Kernlücken.
2. **OD-008-Umsetzung** (ELM/Trust Formation/PKM als Buchanalyse- oder Research-Pack-Sprint) — die Entscheidung selbst ist SHOULD-HAVE-Governance-Arbeit, ihre inhaltliche Umsetzung ist explizit Post-1.0-Wachstum.
3. **AR-001/AR-013 volle akademische Vertiefung** (Plouffe et al. 2013, Tversky & Shafir 1992) — die für 1.0 notwendige Bedingung (eine belastbare, herausgeber-abgestimmte Positionierung zu W-001) ist bereits erfüllt; die tiefere akademische Validierung ist eine Qualitätssteigerung, keine Voraussetzung.
4. **Terminologie-Nachziehung "Altruistische Bestrafung"** und **Boundary-Conditions-Ausweitung** auf weitere Objekte — reine redaktionelle Vertiefung ohne bekannten inhaltlichen Mangel in der aktuellen Fassung.
5. **Formales, repositoryweites Health-Check-Protokoll** — das projektspezifische Muster aus dem Research Program funktioniert bereits; eine Verallgemeinerung ist wertvoll, aber keine Voraussetzung, da keine bisherige Freigabe darunter gelitten hat.
6. **Neue Buchanalysen** (B-0016 ff. aus `book_catalog.md`) — explizit erst nach Architecture Freeze und RC1-Audit, um nicht erneut die zu prüfende Objektmenge während einer laufenden Konsistenzphase zu vergrößern (derselbe Effekt, der zwischen Programm-Erstellung und diesem Release Plan bereits einmal aufgetreten ist).
7. **`book_catalog.md`/`REPOSITORY_KPIS.md`-Vollsynchronisierung** — als SHOULD HAVE in Kapitel 3.2 geführt; falls aus Zeit-/Priorisierungsgründen nicht vor der Freigabe erledigt, ist dies der erste Punkt der 1.1-Arbeit, nicht später.
8. **Erreichen der Reifegrad-Note "A-"** — ausdrücklich kein 1.0-Ziel (Kapitel 3.4, W6); bleibt langfristiges Qualitätsziel für eine spätere Version.

---

# Kapitel 7 — Release Risks

## HIGH

- **[Wissenschaftlich] Publication-Bias-Abhängigkeit der B2B-Kernmethodik unverändert ungeklärt (M1/4.5).** Die drei meistzitierten B2B-Methodik-Quellen (SPIN/Huthwaite N=35.000, Challenger/CEB N=6.000, JOLT/Tethr-ML) bleiben ohne unabhängige Replikation. Größtes wissenschaftliches Risiko für die Kernaussagekraft einer "1.0"-Freigabe.
- **[Wissenschaftlich] MEC-0018-Selbstwiderspruch (M5).** Ein Wissensobjekt behauptet "extrem gut repliziert", während die Scientific-Debt-Matrix genau diesen Punkt mit "Hoch"-Priorität als Replikationskrise führt. Dies ist kein bloßer Debt-Eintrag, sondern eine **aktive Inkonsistenz am Objekt selbst** — das schwerwiegendste in diesem Sprint neu identifizierte Einzelrisiko, weil es dem in Kapitel 2.1 formulierten Grundversprechen ("ehrlich über den eigenen Beleg-Status") direkt widerspricht.
- **[Governance] Zwei entscheidungsreife, aber unentschiedene Open Decisions mit direktem Bezug zu den stärksten/schwächsten Repository-Kennzahlen (OD-006 zu P-S1-001, OD-007 zu Generalisierbarkeit C+).** Beide sind seit dem 2026-07-01/02-Zeitraum unverändert offen — kein Fortschritt trotz vollständiger Entscheidungsgrundlage.

## MEDIUM

- **[Strukturell] Kein Audit seit Behavioral Science Expansion / Repository Consolidation / W-001-Abschluss.** Das Repository ist um 40 % mehr Wissensobjekte gewachsen, seit die letzte unabhängige Qualitätsprüfung stattfand. Jede aktuelle Reifegrad-Aussage ("B+", "B") stützt sich auf einen überholten Datenstand.
- **[Strukturell] `book_catalog.md` und `REPOSITORY_KPIS.md` sind seit früher Projektphase nicht gepflegt** und zeigen einen Zustand, der der Realität um 13–14 Bücher hinterherhinkt. Risiko für Kontinuität künftiger Sessions (genau das Problem, das die Stateless Agent Architecture eigentlich lösen soll).
- **[Governance] Wachsende Anzahl offener Open Decisions (7 von 12) trotz kontinuierlicher Sprintarbeit.** Die W-001-Integration selbst hat eine neue Open Decision erzeugt (OD-012) — ein strukturelles Muster, bei dem jeder Abschluss-Sprint tendenziell mindestens eine neue Nachfolgefrage aufwirft. Ohne eine dedizierte Entscheidungsrunde wächst dieser Bestand potenziell schneller, als er abgebaut wird.
- **[Produkt] Evidenzfeld-Uneinheitlichkeit in unbekanntem, wahrscheinlich unterschätztem Umfang (M4).** Die ursprüngliche Schätzung (~60 Objekte) bezog sich auf ein kleineres Repository; ob die 146 neuen Objekte aus der Behavioral Science Expansion dasselbe Problem in größerem Maßstab reproduzieren, ist nicht geprüft.
- **[Wissenschaftlich] Reifegradbericht nennt W-001 weiterhin als "kritischen Punkt", obwohl die Frage inzwischen governance-seitig entschieden ist.** Ein zentrales Qualitätsdokument des Repositorys ist damit vorübergehend selbst nicht mehr aktuell — ein Ironie-Risiko für ein System, dessen Kernversprechen Aktualität und Selbstkorrektur ist.

## LOW

- **[Strukturell] SRC-0010 fehlt weiterhin** (bereits dokumentierte Repository-Anomalie, referenziert durch ~20 Objekte). Bekannt, nicht neu, keine Verschlechterung.
- **[Strukturell] Mehrere, bereits im Repository Consolidation Sprint dokumentierte Hygiene-Restpunkte** (Ordnernummern-Kollision, Onboarding-Dokument-Redundanz, Git-Index-Formatfehler) — unverändert, ohne inhaltliches Risiko.
- **[Produkt] Canonicalization-Rate-Varianz zwischen Büchern (0 %–67 %)** — bereits im Vorgänger-Programm als teils erwartetes Artefakt bewusst diverser Themenwahl eingestuft, nicht als eigenständiges Risiko.
- **[Governance] Vier der zwölf Open-Decision-Einträge (OD-009 bis OD-012) sind reine Post-1.0-Governance-Fragen** ohne inhaltliches Blockadepotenzial — Risiko besteht nur darin, dass sie bei einer künftigen Prüfung fälschlich als Blocker gelesen werden könnten, wenn nicht klar dokumentiert (dieser Plan tut dies in Kapitel 3.2/4.6).

---

# Kapitel 8 — Release Recommendation

## Empfehlung

**READY AFTER MINOR REVISION**

## Begründung

Der Sales Codex hat seit dem ursprünglichen 1.0-Programm (2026-07-02) einen erheblichen, verifizierbaren Fortschritt gemacht: fünf weitere Bücher, ein vollständig praktisch validiertes Research Program, die erste tatsächlich getroffene und integrierte Editor Decision zu einem seit Sprint 1 dokumentierten Kernwiderspruch (W-001), sowie die Bereinigung mehrerer Repository-Hygiene-Fragen, die im ursprünglichen Programm noch als Blocker geführt wurden. Zwei der sechs ursprünglich benannten Blocker (B1/W-001, B6/Repository-Hygiene) sind damit erledigt oder auf ein nicht-blockierendes Restproblem reduziert.

Die Empfehlung lautet dennoch nicht "READY", sondern "READY AFTER MINOR REVISION", aus drei Gründen:

1. **Zwei entscheidungsreife, aber weiterhin unentschiedene Governance-Fragen** (OD-006, OD-007) betreffen direkt die stärkste und die schwächste Kennzahl des gesamten Codex. Beide erfordern keine neue Recherche — nur eine tatsächliche Herausgeber-Entscheidung. Das ist der am schnellsten schließbare Blocker-Typ dieses Plans.
2. **Ein neu in diesem Sprint identifizierter, konkreter Selbstwiderspruch** (MEC-0018 "extrem gut repliziert" vs. dokumentierte Priming-Replikationskrise) widerspricht direkt dem Kernversprechen von Version 1.0 (Kapitel 2.1) und muss vor einer Freigabe behoben werden — dies ist jedoch eine punktuelle Korrektur an einem einzelnen Objekt, keine strukturelle Überarbeitung.
3. **Kein Audit hat den aktuellen, gewachsenen Repositoryzustand geprüft.** Die zugrunde liegenden Qualitätsurteile (B+, B) stammen aus einer Zeit vor 40 % des heutigen Objektbestands. Ein RC1-Audit ist notwendig, bevor eine Freigabe auf einer verlässlichen, aktuellen Grundlage steht — dies ist jedoch ein einmaliger, klar abgegrenzter Prüfschritt, kein neuer Inhaltsaufwand.

Keiner dieser drei Punkte erfordert neue Forschung, neue Literaturrecherche oder eine strukturelle Überarbeitung des Wissensmodells. Alle drei sind mit den in Kapitel 5 (Critical Path) benannten, bereits klar umrissenen Schritten in überschaubarer Zeit schließbar. Dies unterscheidet den aktuellen Zustand deutlich von "MAJOR REVISION REQUIRED" (das wäre der Fall, wenn grundlegende Wissensmodell-Fragen offen wären oder mehrere Kernaussagen des Codex in Zweifel stünden) und von einem uneingeschränkten "READY" (das eine tatsächlich abgeschlossene, nicht nur entscheidungsreife Governance sowie eine aktuelle externe Bestätigung voraussetzen würde).

---

*Erstellt: 2026-07-03 | SALES CODEX 1.0 RELEASE PLAN | Konsolidiert `SALES_CODEX_1_0_PROGRAM.md` (2026-07-02, unverändert im Repository erhalten) mit dem Stand nach Behavioral Science Expansion, Behavioral Science Review Sprint, Repository Consolidation Sprint 2, Research Program Finalization Sprint (RC-1) und Research Project W-001 Repository Integration Sprint | Reine Release-Planung, kein Forschungssprint — keine neuen Wissensobjekte, keine neue Literatur, keine Frameworkänderungen, keine Editor Decisions, keine Repository-Umstrukturierungen wurden in dieser Session vorgenommen | Nächster Schritt: Herausgeber-Entscheidungsrunde zu OD-006/OD-007 (siehe Kapitel 5, Schritt 1).*
