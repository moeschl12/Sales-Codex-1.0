# SALES CODEX 1.0 PROGRAM

**Dokumentklasse:** Steuerungsdokument (Operational — Pflichtlektüre für jede Session bis Version 1.0 erreicht ist)
**Status:** Aktiv seit 2026-07-02
**Ersetzt:** Die bisherige rein sprintorientierte Entwicklungslogik als übergeordneten Rahmen. Sprints (Book Mode, Academic Recovery, Peer Review, Consistency Correction, Governance) bleiben die operativen Werkzeuge — dieses Dokument ordnet sie einem gemeinsamen Zielzustand unter.
**Erstellt nach Abschluss von:** 10 Buchanalysen, Sprint-1- und Sprint-2-Synthese, Peer Review Sprint 1 + 2, Academic Recovery Phase 1 + 2, Gemini Scientific Review, Claude Response Review, vollständigem Codex Audit (`CODEX_AUDIT_2026-07.md`), Consistency Correction Sprint, Governance Sprint (`OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`).
**Diese Session:** Reine Programm-Definition. Keine neuen Wissensobjekte, keine neuen Mechanismen, keine neue Literatur, keine Academic Recovery, keine Framework-Änderungen, keine Repository-Strukturänderungen, keine Open Decisions geschlossen. Alle in diesem Dokument referenzierten Zahlen und Befunde stammen aus bereits bestehenden Repository-Dokumenten (siehe Quellenangaben je Abschnitt).

---

# 1. Vision

Der Sales Codex ist eine **wissenschaftlich kuratierte Wissensbasis für komplexen B2B-Vertrieb** — kein Buchzusammenfassungsarchiv und kein persönliches Notizsystem.

Der Unterschied ist strukturell, nicht stilistisch:

- **Keine Buchsammlung.** Eine Buchsammlung reiht Inhalte nebeneinander. Der Sales Codex ordnet jede Aussage (ST) einer Kausalkette zu (MEC), leitet daraus abstrahierte Prinzipien (P, aus ≥2 Quellen) und konkrete Techniken (T) ab, bewertet jede Aussage nach einem fünfstufigen Evidenzsystem (E1–E5) und dokumentiert Quellen-Konvergenz (QK) explizit, statt sie stillschweigend vorauszusetzen.
- **Kein Notizsystem.** Ein Notizsystem toleriert Redundanz und unaufgelöste Widersprüche stillschweigend. Der Sales Codex canonicalisiert aktiv (Rule of Three, Fusions-/Erweiterungslogik im Canonical Knowledge Model) und führt Widersprüche als benannte, klassifizierte Objekte (W-001 bis W-005) statt sie zu glätten oder zu verstecken.
- **Wissenschaftlich kuratiert** bedeutet konkret: Jedes Wissensobjekt trägt einen Evidenzstatus, jede Unsicherheit wird als Scientific Debt geführt (56 Einzeleinträge + 6 systemische Cluster, `SCIENTIFIC_DEBT.md`), jede externe Kritik wird geprüft statt reflexhaft übernommen oder abgewehrt (siehe Peer Review Decision Reports Sprint 1 + 2, in denen mehrere Gutachter-Empfehlungen mit fachlicher Begründung abgelehnt wurden), und jede Herausgeber-Entscheidung wird dokumentiert statt implizit getroffen (`OPEN_DECISIONS.md`).

Der Zweck des Codex ist es, eine Frage beantwortbar zu machen, die weder ein einzelnes Vertriebsbuch noch eine lose Zettelsammlung beantworten kann: **Welche Aussage über B2B-Verkaufsverhalten ist wie gut belegt, aus welcher Quelle, mit welchen Grenzen — und wo widerspricht sich die verfügbare Literatur tatsächlich?**

*(Quelle: `PROJECT_BOOTSTRAP.md` „Projektziel", operationalisiert und erweitert auf Basis der seither entstandenen Methodik.)*

---

# 2. Mission

## Welche Probleme löst der Sales Codex?

1. **Das Fragmentierungsproblem der Vertriebsliteratur.** Practitioner-Bücher (SPIN, Challenger, Gap Selling, JOLT, Never Split the Difference u. a.) präsentieren jeweils in sich geschlossene, aber gegenseitig unabgeglichene Methodologien. Ohne ein übergeordnetes System bleibt unklar, wo sie sich empirisch stützen, wo sie sich widersprechen (z. B. W-001 — Teach First vs. Diagnose First, seit Sprint 1 dokumentiert) und wo sie schlicht denselben Befund mit anderer Terminologie beschreiben (Canonicalisierung).
2. **Das Evidenzproblem.** Vertriebsratgeber zitieren wissenschaftliche Befunde häufig selektiv oder ohne Prüfung des Replikationsstatus. Der Codex verankert seinen psychologischen Kern direkt in Primärliteratur (Kahneman/Tversky, Cialdini) statt in Sekundärzitaten, prüft Replikationsstatus aktiv (z. B. Herabstufung MEC-0010/MEC-0011 von E3 auf E2 im Peer Review Sprint 1) und dokumentiert, wo eine Aussage auf proprietären, nicht unabhängig replizierten Datensätzen beruht (SD-SYS-001, SD-SYS-004 — Huthwaite/SPIN, CEB/Challenger, Tethr/JOLT).
3. **Das Kontinuitätsproblem KI-gestützter Wissensarbeit.** Einzelne Chat-Sitzungen haben kein Gedächtnis über Sitzungsgrenzen hinweg. Der Codex löst dies durch eine Stateless Agent Architecture (`CURRENT_STATE.md`, `NEXT_ACTION.md`, `SESSION_LOG.md`, `OPEN_DECISIONS.md`), die das Repository selbst — nicht den Chatverlauf — zur alleinigen Quelle der Wahrheit macht.

## Welche wissenschaftliche Lücke schließt er?

Es existiert keine öffentlich zugängliche, strukturierte, evidenzbewertete Synthese quer über die einflussreichsten Vertriebs-, Verhandlungs- und Käuferpsychologie-Werke der letzten 50 Jahre (Cialdini 1984 bis Dixon/McKenna 2022), die gleichzeitig (a) akademische Primärliteratur (Kahneman, Tversky, Cialdini, Fisher/Ury) und (b) kommerzielle Practitioner-Methodik (SPIN, Challenger, Gap Selling, JOLT) in einem gemeinsamen Evidenzrahmen vergleicht, statt sie getrennt zu behandeln. Der Sales Codex ist der Versuch, genau diese Synthese systematisch, nachvollziehbar und selbstkritisch aufzubauen — mit expliziter Offenlegung, wo die B2B-spezifische akademische Fundierung (aktuell Reifegrad-Dimension „Generalisierbarkeit": C+, schwächste von sechs Dimensionen laut `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`) noch unzureichend ist, statt diese Lücke zu verschleiern.

## Warum existiert dieses Projekt?

Weil belastbare Vertriebsentscheidungen — welche Gesprächsmethodik, welche Verhandlungstaktik, welche Einwandbehandlung — aktuell entweder auf einzelnen, unverglichenen Practitioner-Quellen oder auf akademischer Literatur beruhen, die nicht für den B2B-Praxiskontext übersetzt ist. Der Sales Codex schließt diese Lücke nicht, indem er eine neue Methodik erfindet, sondern indem er bestehende Methodiken und ihre wissenschaftliche Fundierung explizit, geprüft und widerspruchsbewusst gegenüberstellt.

---

# 3. Aktueller Status

*(Alle Zahlen mit Quellenangabe; Stand 2026-07-02, unmittelbar nach dem Governance Sprint. Für tagesaktuelle Repository-Statistiken siehe `CURRENT_STATE.md`.)*

## Bücher

**10 Bücher vollständig analysiert** (B-0001 bis B-0010), alle mit SRC-Objekt, VAL-Konsistenzreview und Abschlussbericht:

| # | Buch | Autor(en) | Canonicalization Rate |
|---|---|---|---|
| B-0001 | SPIN Selling | Rackham | 0 % (erstes Buch) |
| B-0002 | Influence | Cialdini | 37,5 % |
| B-0003 | Never Split the Difference | Voss/Raz | 50 % |
| B-0004 | The Challenger Sale | Dixon/Adamson | 50 % |
| B-0005 | Gap Selling | Keenan | 67 % (⚠ Teilquelle, SD-SYS-002) |
| B-0006 | The JOLT Effect | Dixon/McKenna | 3 % |
| B-0007 | Getting to Yes | Fisher/Ury | 4 % |
| B-0008 | Pre-Suasion | Cialdini | 4–25 % (Diskrepanz dokumentiert, `CODEX_AUDIT_2026-07.md` Kap. 3) |
| B-0009 | To Sell Is Human | Pink | 0 % |
| B-0010 | Thinking, Fast and Slow | Kahneman | 15–22 % (Diskrepanz dokumentiert) |

*(Quelle: `CODEX_AUDIT_2026-07.md` Kapitel 3.)*

## Wissensobjekte

**368 kanonische Wissensobjekte** (verifiziert per Dateizählung, Stand 2026-07-02):

| Typ | Anzahl |
|---|---|
| Statements (ST) | 201 |
| Assumptions (A) | 48 |
| Mechanisms (MEC) | 21 |
| Principles (P) | 47 (43 nummeriert + 4 Meta-Prinzipien P-S1-001–004) |
| Techniques (T) | 41 |
| Models (MOD) | 10 |
| **Summe** | **368** |

Zusätzlich: 10 SRC-Quellobjekte, 10 VAL-Konsistenzreviews, 9 formale Book Reviews + 1 Pilot-Abschlussbericht (B-0001, vor Template-Einführung).

## Audit

`CODEX_AUDIT_2026-07.md` (2026-07-01, vollständiger, ausschließlich lesender Repository-Audit): **Gesamtnote B+.** Wichtigste damalige Neubefunde: E5-Zähler-Diskrepanz im Reifegradbericht (behauptet 5, tatsächlich nur MEC-0015/MEC-0021), Evidenzlevel-Desynchronisation T-0012/T-0013 gegenüber herabgestuften MEC-0011/MEC-0010, 20 Objekte ohne Evidenzfeld, leerer Duplikat-Ordner, zwei koexistierende Knowledge-Model-Dateien. **Der überwiegende Teil dieser Befunde wurde im nachfolgenden Consistency Correction Sprint bereits behoben** (siehe unten) — der Audit selbst bleibt als historisches Dokument unverändert (Grundsatz: nicht rückwirkend schönschreiben).

## Academic Recovery

Zwei abgeschlossene Phasen plus ein Sprint-3-Einzelreview:

- **Phase 1** (`ACADEMIC_RECOVERY_REPORT.md`): 8 externe Quellen websuchverifiziert integriert (u. a. Franke & Park 2006, Verbeke/Dietz/Verwaal 2010/2011, Marcos-Cuevas et al. 2023).
- **Phase 2** (`ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`): ~60 Themen aus drei Research Packs geprüft, 15 bestehende Objekte um Literaturreferenzen erweitert, `05_research/LITERATURE_INDEX.md` neu angelegt.
- **Sprint-3-Review:** MEC-0011 und MEC-0021 redaktionell erneut geprüft; drei neue Literaturkandidaten bewertet (Tversky & Shafir 1992 → Tier 1; Plouffe et al. 2013 → Tier-1-Kandidat; March & Simon 1958 → Tier 2).
- **Offen (Tier 1, `ACADEMIC_RECOVERY_PLAN.md`):** AR-001 (Problemreife-Hypothese/W-001, nur Abstract-Ebene geprüft), AR-002 (Publication-Bias-Klärung, keine sales-spezifische Quelle identifiziert), AR-013 (Tversky & Shafir Volltextverarbeitung). **Keiner dieser drei Punkte hat bislang den Status „mit Primärtext vollständig verarbeitet" erreicht.**

## Governance

- Stateless Agent Architecture seit 2026-06-30 in Betrieb (`PROJECT_BOOTSTRAP.md`, `CURRENT_STATE.md`, `NEXT_ACTION.md`, `SESSION_LOG.md`, `OPEN_DECISIONS.md`).
- Framework-Version **1.1**, eingefroren 2026-06-30 (Book Mode, Stateless Architecture, Canonicalisierungsregeln — 5 von 6 geplanten Inhalten umgesetzt; „Repository Health Check verpflichtend" bleibt dokumentierte Restlücke).
- **Open-Decisions-Status nach Governance Sprint (2026-07-02):** 4 DONE (OD-001–004), 1 ERSETZT (OD-005 → OD-010), 3 bestätigt weiterhin OFFEN und entscheidungsreif (OD-006, OD-007, OD-008), 3 neu angelegt (OD-009 Framework RC1/Reifegrad-Statusübergang, OD-010 Validierungs-Governance, OD-011 Literature-Governance). **6 aktiv offene Entscheidungen insgesamt.** Details: `OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`.
- **Consistency Correction Sprint** (nach Audit Kapitel 11, Meilenstein 1) bereits umgesetzt: T-0012/T-0013 Evidenzlevel synchronisiert (E3→E2), 28 Objekte um Evidenzfelder ergänzt/harmonisiert, Audit-Methodikfehler bei P-S1-001–004 richtiggestellt, E5-Zähler-Erratum dokumentiert. **Offen aus diesem Sprint:** repository-weite Feldnamen-Vereinheitlichung außerhalb des damaligen Scopes (~60 verbleibende Objekte), Herausgeber-Entscheidung zu leerem Duplikat-Ordner und `codex_knowledge_model.md`.

## Scientific Debt

`SCIENTIFIC_DEBT.md`: **56 individuelle Objekt-Zeilen** über 9 buchspezifische Tabellen plus **6 systemische Cluster** (SD-SYS-001 bis SD-SYS-006). Tier-Gruppierung laut Audit Kapitel 6:

- **Tier 1 (vor Version 1.0 zu adressieren):** SD-SYS-001/SD-SYS-004 (Publication Bias proprietärer B2B-Studien: Huthwaite/SPIN, CEB/Challenger, Tethr/JOLT), W-001 selbst, SD-B010-001 (Priming-Replikationskrise, betrifft MEC-0018).
- **Tier 2:** SD-SYS-002 (Gap-Selling-Quellenlücke), MEC-0006/MEC-0014-Fusionsfrage, MEC-0011-Gesamtkomplex.
- **Tier 3:** Kulturelle Generalisierungsfragen, SD-SYS-003 (Meme-Filter-Frage, → OD-006), SD-SYS-005 (Nudging-Kontroverse, kein bestehendes Objekt betroffen).

## Literature Index

`05_research/LITERATURE_INDEX.md` (Version 1.0, angelegt in ARS-0001 Phase 2): **~55–62 Quellen** über vier Domänen (Entscheidungspsychologie/Behavioral Economics, Sozialpsychologie/Persuasion, Verhandlungsforschung, plus Practitioner-Querverweise), mit Verifikationsstatus je Quelle (verifiziert / codex-bestätigt / nicht verifiziert). Struktureller Status gegenüber `SCIENTIFIC_DEBT.md` und `review_queue.md` ungeklärt (→ OD-011).

## Reifegrad (Wissenschaftlich)

`WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (2026-07-01, nach Sprint 2): **Gesamturteil B.** Sechs Dimensionen: Evidenzqualität B+, Quellen-Konvergenz A-, Interne Konsistenz B (W-001 als kritischer Punkt), Domänenabdeckung B, **Generalisierbarkeit C+ (schwächste Dimension)**, Scientific Debt Management A-. Der nachfolgende Audit (B+) bewertet den Prozess-/Transparenzfortschritt seit diesem Bericht positiv, ohne die inhaltlichen Kernlücken (W-001, Generalisierbarkeit) als geschlossen zu betrachten.

---

# 4. Entwicklungsphasen

Fünf Phasen bis Version 1.0. Phasen können teilweise parallel laufen (insbesondere Phase 1 und 2), aber **Phase 3 (Architecture Freeze) darf erst beginnen, wenn Phase 1 und Phase 2 abgeschlossen sind** — eine Architektur einzufrieren, während zentrale Framework-Fragen (OD-006, OD-007) noch offen sind, würde das Einfrieren der falschen Version riskieren.

## Phase 1 — Governance

**Ziel:** Jede der sechs aktiv offenen Entscheidungen (OD-006 bis OD-011) erhält eine tatsächliche Herausgeber-Entscheidung. Repository-Hygiene-Entscheidungen (Duplikat-Ordner, `codex_knowledge_model.md`) werden getroffen.

**Deliverables:**
- Herausgeber-Entscheidung zu OD-006 (Meme-Filter für QK-Rating) — inkl. Format/Skala, falls Einführung beschlossen.
- Herausgeber-Entscheidung zu OD-007 (CTX-Ebene) — eine der drei vorliegenden Optionen.
- Herausgeber-Entscheidung zu OD-008 (ELM/Trust/PKM-Sprint-Priorisierung vs. Academic Recovery Plan Tier 1).
- Herausgeber-Entscheidung zu OD-009 (Framework RC1/Reifegrad-Statusübergang) — insbesondere Klärung des Verhältnisses von Framework-Version (aktuell 1.1) zu Gesamt-Codex-Version (Ziel dieses Programms: 1.0). Siehe Kapitel 9.
- Herausgeber-Entscheidung zu OD-010 (Validierungs-Governance, Nachfolger von OD-005).
- Herausgeber-Entscheidung zu OD-011 (Literature-Governance, Status von `LITERATURE_INDEX.md`).
- Herausgeber-Entscheidung zu Duplikat-Ordner `04_book_analysis/Never_Split_The_Difference/` (löschen/behalten) und `codex_knowledge_model.md` (archivieren/löschen/als Kurzfassung erhalten) — beide seit Consistency Correction Sprint dokumentiert offen.
- Dieses Dokument (`SALES_CODEX_1_0_PROGRAM.md`) selbst — als Rahmen, innerhalb dessen die genannten Entscheidungen getroffen werden.

**Definition of Done:** Alle sechs OD (006–011) tragen einen finalen Status (DONE/ARCHIVIERT/ERSETZT durch eine im jeweiligen OD-Text bereits vorgesehene Folgeaktion) — nicht mehr „Offen — Herausgeber-Entscheidung erforderlich". Duplikat-Ordner und `codex_knowledge_model.md` sind entschieden (Entscheidung muss nicht zwingend in dieser Phase umgesetzt sein, aber getroffen).

## Phase 2 — Scientific Completion

**Ziel:** Die beiden zentralen wissenschaftlichen Tier-1-Lücken (W-001, Publication-Bias-Klärung proprietärer B2B-Studien) werden mit tatsächlicher Primärtext-/Volltextverarbeitung bearbeitet — nicht notwendigerweise vollständig aufgelöst, aber über die aktuelle Abstract-Ebene hinausgeführt.

**Deliverables:**
- AR-001 (Problemreife-Hypothese/W-001): Volltextprüfung von Plouffe et al. (2013) und/oder direkter empirischer Vergleichstest Diagnose-First vs. Insight-First — Ergebnis: entweder literaturgestützte Präzisierung von W-001 oder explizite, begründete Dokumentation „akademisch mit aktuell verfügbarer Literatur nicht direkt auflösbar".
- AR-002 (Publication-Bias-Klärung): Volltextauswertung von Ohiomah et al. (2020) und/oder Marcos-Cuevas et al. (2023) mit der spezifischen Frage, ob und wie diese Meta-Analysen CEB/Challenger/JOLT-artige proprietäre Befunde einordnen.
- AR-013 (Tversky & Shafir 1992): Volltextverarbeitung, Entscheidung ob Erweiterung von MEC-0016 oder neue Theorie-Referenz (CKM Abschnitt 9 beachten).
- SD-B010-001 (Priming-Replikationskrise): Klärung, welche der in Kahneman Kap. 4 zitierten Priming-Befunde als repliziert gelten — mit direkter Konsequenz für MEC-0018 (Pre-Suasion), inkl. einer für Nutzer sichtbaren Kurzwarnung direkt am Objekt (nicht nur in `SCIENTIFIC_DEBT.md`), falls die Unsicherheit bestehen bleibt.

**Definition of Done:** Für W-001 und für die Publication-Bias-Frage liegt jeweils ein Ergebnis vor, das über „Abstract-Ebene, kein Volltextzugriff" hinausgeht — entweder eine inhaltliche Präzisierung/Teilauflösung oder eine explizit begründete Dokumentation der Nicht-Auflösbarkeit. SD-B010-001 trägt eine sichtbare Warnung am betroffenen Objekt (MEC-0018).

**Ausdrücklich nicht Teil dieser Phase:** AR-003 bis AR-012 (Tier 2–4 des Academic Recovery Plan), neue Practitioner-Buchanalysen, ELM/Trust Formation/PKM-Vertiefung (OD-008-Gegenstand — abhängig von Phase-1-Entscheidung).

## Phase 3 — Architecture Freeze

**Ziel:** Das Repository erreicht einen strukturell und terminologisch konsistenten Zustand, der öffentlich/extern als „1.0-Basis" vertretbar ist — reine Konsistenzarbeit, keine neue Recherche.

**Deliverables:**
- Repository-weite Vereinheitlichung der Evidenzfeld-Benennung (aktuell mindestens fünf Varianten: „Evidenzlevel", „Evidenzklasse", „Evidenzklassifikation", „Evidenzgrad", „Evidenzstatus" — über die im Consistency Correction Sprint bereits bearbeiteten Objekte hinaus, für die verbleibenden ~60 Objekte: T-0036–T-0041, P-0025/026/035–043, alle 48 Assumptions).
- Umsetzung der in Phase 1 getroffenen Entscheidungen zu Duplikat-Ordner und `codex_knowledge_model.md`.
- Sichtbares Erratum in `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` zur E5-Zähler-Diskrepanz (Ergänzung, nicht rückwirkende Änderung des Originaltexts).
- Klärung der Canonicalization-Rate-Diskrepanzen bei B-0008 und B-0010 (Fußnote/Klarstellung in beiden betroffenen Dokumenten, `CODEX_AUDIT_2026-07.md` Kap. 3).
- Formale Implementierung eines Repository-Health-Check-Protokolls (dokumentierte Restlücke aus OD-003/v1.1-Freeze) — mindestens als Prüfpunkt-Checkliste in `task_rules.md` oder Operating Manual, ohne die Prüfschwelle selbst zu einer neuen Framework-Änderung zu machen (Umfang mit Felix abstimmen).

**Definition of Done:** Einheitliche Evidenzfeld-Benennung über alle 368 Wissensobjekte. Keine offenen Repository-Hygiene-Punkte aus dem Audit (Kapitel 2 und 8) mehr unentschieden oder unbearbeitet. Ab diesem Punkt werden an der Repository-*Struktur* (nicht am Inhalt einzelner Objekte) keine weiteren Änderungen mehr vorgenommen, bis Version 1.0 erreicht ist — daher „Freeze".

## Phase 4 — Release Candidate

**Ziel:** Ein vollständiger, erneuter Audit bestätigt, dass alle in Phase 1–3 vorgesehenen Blocker (Kapitel 6 dieses Dokuments) tatsächlich geschlossen sind. Der Codex trägt ab hier informell die Bezeichnung „Sales Codex 1.0 RC1".

**Deliverables:**
- Erneuter, vollständiger, ausschließlich lesender Repository-Audit (Methodik wie `CODEX_AUDIT_2026-07.md`), diesmal mit explizitem Fokus auf: Wurden die in diesem Programm benannten Blocker (Kapitel 6) tatsächlich geschlossen? Wurde die T-/P-Ebenen-Prüfung (Neubefund des ersten Audits) diesmal von Anfang an mitgeprüft, nicht nachträglich?
- Aktualisierte Reifegrad-Einschätzung (kein vollständig neuer Reifegradbericht zwingend erforderlich, aber mindestens eine dokumentierte Neubewertung der Dimension „Generalisierbarkeit" und „Interne Konsistenz" nach Abschluss von Phase 2).
- Finale Prüfung, dass keine Tier-1-Scientific-Debt-Einträge mehr unbearbeitet sind (Tier 2/3 dürfen bestehen bleiben, siehe Kapitel 7).

**Definition of Done:** Der RC1-Audit vergibt keine neuen Tier-1-Blocker-Befunde. Alle in Kapitel 6 dieses Dokuments gelisteten Blocker sind laut RC1-Audit geschlossen oder explizit und begründet in „Nicht-Blocker" (Kapitel 7) umklassifiziert worden (mit Herausgeber-Freigabe, nicht durch eigenständige KI-Entscheidung).

## Phase 5 — Version 1.0

**Ziel:** Formale Freigabe. Der Sales Codex trägt ab diesem Zeitpunkt die Versionsbezeichnung 1.0.

**Deliverables:**
- Herausgeber-Freigabe (Felix) basierend auf dem RC1-Audit aus Phase 4.
- `CURRENT_STATE.md` erhält den Versionsvermerk „Sales Codex Version: 1.0 (freigegeben [Datum])" — als eigenständiges Versionsfeld neben dem bestehenden Framework-Versionsfeld (siehe Kapitel 9 zur Klärung dieser Unterscheidung).
- Executive Summary (Kapitel 12 dieses Dokuments) wird als offizielle Projektbeschreibung übernommen bzw. bei Bedarf final aktualisiert.
- Governance-Workflow nach Version 1.0 (Kapitel 8) tritt formal in Kraft.

**Definition of Done:** Siehe Kapitel 11 — vollständig, objektiv, messbar.

---

# 5. Qualitätskriterien

Objektive, prüfbare Kriterien — keine subjektiven Formulierungen. Jedes Kriterium ist an einem Repository-Artefakt nachprüfbar.

| Kriterium | Objektiver Prüfpunkt | Status (2026-07-02) |
|---|---|---|
| Repository konsistent | Keine E-Level-Desynchronisation zwischen MEC und abhängigen T-/P-Objekten (stichprobenartig oder vollständig geprüft in einem Audit) | Erreicht für T-0012/T-0013 (Consistency Correction Sprint); repository-weite Vollprüfung aller MEC→T/P-Abhängigkeiten steht noch aus |
| Governance abgeschlossen | Alle Open Decisions tragen Status DONE/ARCHIVIERT/ERSETZT, keine mit Status „Offen" | 4 von 10 aktuellen OD-Einträgen DONE/ERSETZT (OD-001–005); 6 weiterhin offen (OD-006–011) |
| Tier-1 Scientific Debt bearbeitet | SD-SYS-001, SD-SYS-004, SD-B010-001 und W-001 tragen Status „mit Primärtext bearbeitet" statt „Abstract-Ebene" | Nicht erreicht — Gegenstand Phase 2 |
| Literature Index vollständig | `LITERATURE_INDEX.md` hat einen formal definierten Status (dauerhafter Framework-Bestandteil oder nicht) und eine dokumentierte Pflege-Kadenz | Nicht erreicht — Gegenstand OD-011 |
| Peer Reviews abgeschlossen | Mindestens zwei vollständige Peer-Review-Zyklen mit dokumentierten Decision Reports | **Erreicht** — Sprint 1 und Sprint 2, je mit Decision Report |
| Audit abgeschlossen | Mindestens ein vollständiger, unabhängig durchgeführter Repository-Audit liegt vor | **Erreicht** — `CODEX_AUDIT_2026-07.md`, Note B+; RC1-Audit (Phase 4) steht noch aus |
| Evidenzfeld-Vollständigkeit | Jedes Wissensobjekt (ST/A/MEC/P/T/MOD) trägt ein Evidenzfeld unter einheitlichem Namen | Teilweise — 28 Objekte im Consistency Correction Sprint nachgerüstet; einheitliche Benennung repository-weit noch offen (Phase 3) |
| Canonicalisierung dokumentiert | Jede Neu-/Erweiterungs-/Nichtanlage-Entscheidung ist im jeweiligen Objekt oder in `review_queue.md` nachvollziehbar begründet | **Erreicht** — CKM Abschnitt 9, durchgängig angewendet seit v1.1 |
| Widersprüche dokumentiert, nicht geglättet | Jeder bekannte Cross-Book-Widerspruch trägt einen Eintrag in einer Widerspruchsmatrix oder einem Nachfolgedokument mit Status | **Erreicht für Sprint 1** (`contradiction_matrix.md`, W-001–W-005); Sprint-2-Folgewidersprüche (z. B. „Kognitive Leichtigkeit vs. Rational Drowning") sind dokumentiert, aber noch nicht in einer aktualisierten Matrix formalisiert |

---

# 6. Blocker für Version 1.0

Ausschließlich echte, wissenschaftlich begründete Blocker, priorisiert. Ein Blocker ist hier definiert als: eine Lücke, die entweder (a) die Kernaussagekraft des Codex direkt einschränkt oder (b) eine unentschiedene Grundsatzfrage darstellt, deren spätere Klärung frühere Arbeit ungültig machen könnte.

## Priorität 1 — Inhaltlich kritisch

**B1. W-001 (Teach First vs. Diagnose First) ungelöst.**
Begründung: Betrifft die operative Kernaussage der P-Ebene direkt — P-S1-003 (Problem-Zentrierung, QK-6+, eine der am stärksten konvergierten Aussagen des Codex) kann nicht angewendet werden, ohne dass W-001 beantwortet oder als Kontextentscheidung modelliert ist. Seit Sprint 1 (2026-06-30) unaufgelöst, über drei Prüfzyklen bestätigt kritisch (`contradiction_matrix.md`, `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` Kap. 1.3, `CODEX_AUDIT_2026-07.md`).

**B2. Publication-Bias-Abhängigkeit der B2B-Kernmethodik ungeklärt.**
Begründung: SPIN (Huthwaite, N=35.000, proprietär), Challenger (CEB, N=6.000, proprietär), JOLT (Tethr-ML-Klassifizierung, proprietär) — die drei am häufigsten zitierten B2B-Methodologie-Quellen des Codex — haben keine unabhängige, peer-reviewte Replikation. SD-SYS-001 und SD-SYS-004 dokumentieren dies seit Peer Review Sprint 1/2, ohne dass eine sales-spezifische Publication-Bias-Studie identifiziert wurde. Ein Wissenssystem, das sich als „wissenschaftlich kuratiert" bezeichnet, kann diese strukturelle Abhängigkeit nicht als Randnotiz führen.

## Priorität 2 — Governance kritisch

**B3. OD-006 (Meme-Filter für QK-Rating) unentschieden.**
Begründung: Betrifft direkt die Validität von P-S1-001 (Cost of Inaction, QK-8+ — die am stärksten konvergierte Einzelaussage des gesamten Codex). Wenn die Konvergenz zwischen Cialdini → Voss → Keenan teilweise Meme-Replikation statt unabhängiger Beobachtung ist, verliert die zentrale Stärke des Codex an Aussagekraft. Der Audit stuft dies explizit als „Hoch"-Priorität ein (`CODEX_AUDIT_2026-07.md` Kap. 7).

**B4. OD-007 (CTX-Ebene) unentschieden.**
Begründung: Direkt relevant für „Generalisierbarkeit" — die schwächste Reifegrad-Dimension (C+). Die wissenschaftliche Analyse liegt bereits vollständig vor (drei Optionen ausgearbeitet); es fehlt ausschließlich die Entscheidung selbst. Eine Version 1.0, die ihre schwächste Dimension mit einer seit Wochen entscheidungsreifen, aber unentschiedenen Frage stehen lässt, wäre nicht konsequent.

## Priorität 3 — Struktur-/Konsistenzkritisch

**B5. Repository-weite Evidenzfeld-Benennung uneinheitlich (~60 Objekte außerhalb des Consistency-Correction-Scopes).**
Begründung: Kein inhaltliches Risiko, aber ein Vertretbarkeits-Risiko: Ein „1.0"-System mit fünf verschiedenen Feldnamen für dasselbe Konzept ist nach außen schwer als konsistent zu vertreten. Reine Fleißarbeit, kein Recherche- oder Framework-Aufwand.

**B6. Repository-Hygiene: Duplikat-Ordner und `codex_knowledge_model.md` unentschieden.**
Begründung: Geringes inhaltliches Risiko, aber ein Verwechslungsrisiko für künftige Sessions (menschlich oder KI), das seit dem Audit dokumentiert, aber nie final entschieden wurde. Niedrigster Aufwand aller Blocker.

**Ausdrücklich kein Blocker (zur Klarstellung):** OD-008 (ELM/Trust/PKM-Priorisierung), OD-009 (RC1-Statusdefinition — wird durch dieses Programm selbst bereits weitgehend operationalisiert), OD-010 (Validierungs-Governance), OD-011 (Literature-Governance) sind Governance-Fragen, deren *Entscheidung* sinnvollerweise in Phase 1 fällt, deren *Nichtentscheidung* aber im Gegensatz zu B3/B4 keine inhaltliche Kernaussage des Codex direkt schwächt — siehe Kapitel 7 für die Begründung, warum diese drei dennoch in Phase 1, aber nicht als Blocker im engeren Sinn geführt werden.

---

# 7. Nicht-Blocker

Offene Fragen, die ausdrücklich auch in Version 1.0 bestehen bleiben dürfen — mit Begründung je Punkt.

**N1. AR-003 bis AR-012 (Tier 2–4 des Academic Recovery Plan — Buying-Center-Cluster, Behavioral-Economics-Primärquellen-Direktzugriff, geografisch-kulturelle Diversifizierung).**
Begründung: Der Academic Recovery Plan selbst stuft diese als nachrangig gegenüber AR-001/002/013 ein. Sie vertiefen einen bereits vorhandenen, funktionierenden Teil des Codex, schließen aber keine Lücke, die die Kernaussagekraft aktuell einschränkt. Post-1.0-Material.

**N2. OD-008 (ELM/Trust Formation/PKM als eigener Recherche-/Buchanalyse-Sprint).**
Begründung: Eine allgemeinpsychologische Vertiefung mit hoher, aber nicht B2B-spezifischer Integrationskraft (Editor-Einschätzung in OD-008 selbst). Bereichert den Codex, schließt aber keine der beiden Tier-1-Lücken (W-001, Publication Bias). Die Entscheidung selbst gehört in Phase 1, ihre *Umsetzung* (falls Felix sie priorisiert) ist explizit Post-1.0- oder parallel-zu-1.0-Material, kein Blocker.

**N3. MEC-0011 (Neural Coupling) auf E1/E2-Niveau.**
Begründung: Bereits das transparenteste, am gründlichsten mit Vorbehalten versehene Objekt im gesamten Codex (`CODEX_AUDIT_2026-07.md`: „riskanteste, aber am transparentesten dokumentierte Objekte des Codex — Musterbeispiel für Scientific-Debt-Kultur"). Ein niedriges Evidenzlevel mit vollständiger, expliziter Offenlegung ist kein Mangel im Sinne dieses Programms — im Gegenteil, es ist genau das Verhalten, das Kapitel 1 (Vision) als Unterscheidungsmerkmal zu einer unkritischen Buchsammlung benennt. Löschung oder Zwangsauflösung würde die Scientific-Debt-Kultur selbst untergraben.

**N4. SD-B010-001 (Priming-Replikationskrise) — vollständige akademische Klärung.**
Begründung: Die umfassende Kontroverse um Social-Priming-Replizierbarkeit in der akademischen Sozialpsychologie ist eine offene Forschungsdebatte, die der Sales Codex nicht selbst auflösen kann und muss. Phase 2 verlangt eine *sichtbare Warnung* am betroffenen Objekt (MEC-0018) — nicht die Auflösung der gesamten Replikationsdebatte.

**N5. Domänenlücken (Account Management, Pricing Psychology B2B, Digital Sales/Inside Sales).**
Begründung: Explizit außerhalb des aktuellen Scopes (Erstkauf-Prozess, Käuferpsychologie, Verhandlung). Der Codex hat nie behauptet, den vollständigen Customer Lifecycle abzudecken. Dies ist Erweiterungspotenzial für v1.1/v1.2/v2.0 (siehe Kapitel 9), keine Lücke im bestehenden Anspruch.

**N6. Canonicalization-Rate-Varianz zwischen Büchern (3 % bis 67 %).**
Begründung: Laut Audit teils echtes Signal (Redundanzrisiko, → OD-006), teils Artefakt bewusst thematisch diverser Buchauswahl (JOLT, Getting to Yes und To Sell Is Human führen tatsächlich neue Konstrukte ein, keine Wiederholung). Die Meme-Risiko-Frage selbst wird über OD-006 (Blocker B3) behandelt — die reine Ratenvarianz ist kein zusätzlicher, eigenständiger Blocker.

**N7. Geografisch-kulturelle Einseitigkeit (alle 10 Bücher nordamerikanisch/westeuropäisch).**
Begründung: Vom externen Gutachten selbst als niedrigste Priorität eingestuft (AR-012, Tier 4). Dokumentierte, akzeptierte Grenze des aktuellen Literaturkorpus — kein verstecktes Risiko.

**N8. Doppelte QK-Nomenklatur-Frage vs. formale Meta-Analyse-Standards.**
Begründung: Der Codex verwendet QK (Quellen-Konvergenz) als eigenes, transparent definiertes Konzept, nicht als Ersatz für eine formale Meta-Analyse. Diese Abgrenzung ist bereits an mehreren Stellen dokumentiert (Reifegradbericht, Audit) und erfordert keine weitere Klärung vor Version 1.0.

---

# 8. Governance nach Version 1.0

Nach Erreichen von Version 1.0 löst folgender Standard-Workflow die bisherige Ad-hoc-Sprintfolge ab (formalisiert bei positiver Herausgeber-Entscheidung zu OD-010, Validierungs-Governance):

```
Neue Literatur / neues Buch identifiziert
    ↓
Research Pack ODER Book-Mode-Kandidat
(Klassifikation: akademische Quelle → Research Pack; Practitioner-Werk → Book Mode)
    ↓
Academic Recovery (bei Research Pack)
ODER vollständige Buchanalyse-Pipeline SRC→ST→A→MEC→P→T→MOD→VAL (bei Book Mode)
    ↓
Peer Review
(mindestens: Selbstreview per VAL; bei substanziellem Umfang zusätzlich externes Gutachten)
    ↓
Consistency Check
(Evidenzfeld-Synchronisation zwischen neuen/geänderten MEC und abhängigen P-/T-Objekten — 
 die im ersten Audit gefundene Desynchronisationslücke wird durch diesen expliziten Schritt strukturell verhindert)
    ↓
Audit (periodisch, nicht nach jeder Einzeländerung)
    ↓
Release (Versions-Increment nach Schema Kapitel 9)
```

**Wichtigste Änderung gegenüber dem Vor-1.0-Zustand:** Der „Consistency Check"-Schritt wird als eigenständige, verpflichtende Stufe eingeführt — nicht weil er heute fehlt (Consistency Correction Sprints fanden bereits statt), sondern weil er bislang reaktiv (nach einem Audit) statt proaktiv (nach jeder Änderung) ausgelöst wurde. Das ist die direkte Konsequenz aus dem wichtigsten Neubefund des ersten Audits: die MEC→T/P-Synchronisationslücke.

**Kadenz-Empfehlung (zur Herausgeber-Entscheidung im Rahmen von OD-010):** Vollständige Audits nicht nach jedem Einzelsprint, sondern nach jeweils 3–5 inhaltlichen Sprints oder mindestens einmal pro Versions-Minor-Increment (siehe Kapitel 9).

---

# 9. Versionierung

## Klärung einer bestehenden Doppeldeutigkeit

Das Repository führt aktuell ein Versionsfeld „Workspace-Version: 1.1" (`CURRENT_STATE.md`), das sich aber ausschließlich auf die **Framework-/Prozess-Version** bezieht (Book Mode, Stateless Architecture, Canonicalisierungsregeln — reine Methodik, kein Inhalt). Der in diesem Programm verfolgte Zielzustand „Version 1.0" bezieht sich dagegen auf die **Gesamt-Codex-Version** (Inhalt + Methodik + Governance-Reife gemeinsam). Diese beiden Versionsachsen sind nicht identisch und sollten ab sofort getrennt geführt werden (Gegenstand von OD-009):

- **Framework-Version** (z. B. „Sales Codex OS v1.1"): Methodik, Templates, Operating Manual, Book-Mode-Definition. Ändert sich bei Prozess-/Methodik-Änderungen.
- **Sales-Codex-Version** (Ziel dieses Programms: „1.0"): Gesamtreifegrad aus Inhalt, Evidenzbasis, Governance-Zustand und Konsistenz. Ändert sich bei inhaltlichem/strukturellem Fortschritt gegenüber den in Kapitel 5 definierten Qualitätskriterien.

Es ist möglich und sogar wahrscheinlich, dass die Framework-Version zum Zeitpunkt von Sales-Codex-1.0 bereits höher steht (z. B. v1.2, falls Phase 3 Framework-relevante Klarstellungen erfordert) als die neue Sales-Codex-Zählung — das ist kein Widerspruch, sondern der erwartete Effekt zweier unabhängiger Versionsachsen.

## Vorgeschlagenes Schema für die Sales-Codex-Version (ab 1.0)

| Version | Kriterium |
|---|---|
| **1.0** | Alle Kriterien aus Kapitel 11 (Definition of Done) erfüllt. Erste formal freigegebene Gesamtversion. |
| **1.1, 1.2, …** | Inhaltliche Erweiterung ohne Strukturänderung: neue Bücher (Book Mode), neue Research Packs (Academic Recovery), Domänenerweiterung (z. B. N5: Account Management, Pricing Psychology) — sofern sie die bestehende Objekt-Hierarchie und das Evidenzsystem unverändert nutzen. Auslöser: mindestens ein abgeschlossener Inhalts-Sprint plus ein bestandener Consistency Check (Kapitel 8). |
| **1.x → 2.0** | Strukturelle Änderung am Wissensmodell selbst — z. B. Einführung einer neuen Objektklasse (etwa CTX, falls OD-007 zu diesem Ergebnis führt), grundlegende Änderung des Evidenzsystems E1–E5, oder Auflösung einer der beiden aktuellen Tier-1-Kernlücken in einer Weise, die bestehende Objekte in großer Zahl reklassifiziert. Auslöser: Framework-Änderung mit Rückwirkung auf ≥10 % der bestehenden Wissensobjekte (Schwellenwert zur Orientierung, keine harte Grenze — Herausgeber-Ermessen). |
| **Patch-artige Korrekturen** (kein Versionsinkrement) | Reine Konsistenzkorrekturen (wie der Consistency Correction Sprint 2026-07), Zitationskorrekturen, Errata. Werden im Changelog dokumentiert, lösen aber keinen Versionswechsel aus, da sie keine inhaltliche oder strukturelle Erweiterung darstellen. |

**Nicht Teil dieses Schemas (bewusst offen gelassen für OD-009):** Ob zwischen 1.0 und 2.0 eine explizite „RC"-Zwischenstufe für jede künftige Major-Version eingeführt wird, oder ob dieses RC-Konzept ausschließlich für den einmaligen Übergang zu 1.0 gilt (Phase 4 dieses Programms). Empfehlung: Letzteres — RC-Stufen sind für den ersten großen Reifegrad-Sprung sinnvoll, aber nicht zwingend für jede künftige Minor-Version.

---

# 10. Roadmap

Maximal zehn Punkte, wissenschaftlich priorisiert (keine Wunschliste — jeder Punkt leitet sich aus einem bereits dokumentierten Befund ab, siehe Quellenangabe).

1. **Phase-1-Entscheidungsrunde (OD-006 bis OD-011 plus Repository-Hygiene)** — höchste Priorität, da mehrere inhaltliche Folgeschritte davon abhängen. *(Quelle: `OPEN_DECISION_RESOLUTION_REPORT_2026-07.md` Kap. 7; `CODEX_AUDIT_2026-07.md` Kap. 10.)*
2. **AR-001 + AR-013 gemeinsam bearbeiten** (Problemreife-Hypothese, Plouffe et al. 2013 und Tversky & Shafir 1992 volltextverarbeiten) — beide zielen auf dieselbe strukturelle Schwäche (W-001-Kontext bzw. Indecision-Publication-Bias) und lassen sich effizient gemeinsam bearbeiten. *(Quelle: `ACADEMIC_RECOVERY_PLAN.md` Abschnitt 3.)*
3. **AR-002** (Publication-Bias-Klärung, Volltextauswertung Ohiomah et al. 2020 / Marcos-Cuevas et al. 2023). *(Quelle: `ACADEMIC_RECOVERY_PLAN.md`.)*
4. **SD-B010-001 Klärung** (Priming-Replikationsstatus MEC-0018) — direkte E-Level-Konsequenz, bereits „Hoch" priorisiert in `SCIENTIFIC_DEBT.md`. *(Quelle: `ACADEMIC_RECOVERY_PLAN.md` AR-008; `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` Kap. 6.)*
5. **Repository-weite Evidenzfeld-Harmonisierung** (~60 verbleibende Objekte außerhalb des Consistency-Correction-Scopes) — reine Konsistenzarbeit, höchster Aufwand-Nutzen-Quotient. *(Quelle: `CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md` Abschnitt 8.)*
6. **Repository-Hygiene umsetzen** (Duplikat-Ordner, `codex_knowledge_model.md`) gemäß Phase-1-Entscheidung. *(Quelle: `CODEX_AUDIT_2026-07.md` Kap. 2, 8.)*
7. **Formales Repository-Health-Check-Protokoll** einführen (dokumentierte Restlücke aus dem v1.1-Freeze, POST_MORTEM_B0002.md Phase 11). *(Quelle: `OPEN_DECISIONS.md` OD-003-Auflösung.)*
8. **RC1-Audit** (vollständige Wiederholung der Audit-Methodik mit explizitem Fokus auf MEC→T/P-Synchronisation von Beginn an). *(Quelle: Phase 4 dieses Programms.)*
9. **AR-003 bis AR-006** (Buying-Center-Cluster: Johnston & Lewin, Webster & Wind, Sheth, Eisenhardt, March & Simon) — sofern nach Phase 2 noch Kapazität und Priorität besteht; adressiert die vom externen Gutachten explizit benannte fehlende Anreizökonomie-Mechanismus-Lücke. *(Quelle: `ACADEMIC_RECOVERY_PLAN.md` Tier 2.)*
10. **Version-1.0-Freigabe** durch Felix nach bestandenem RC1-Audit. *(Quelle: Phase 5 dieses Programms.)*

---

# 11. Definition of Done

Der Sales Codex hat **Version 1.0** erreicht, wenn **alle** der folgenden Bedingungen gleichzeitig erfüllt sind. Jede Bedingung ist an einem konkreten, nachprüfbaren Repository-Zustand festgemacht — kein Kriterium ist eine Ermessensfrage.

1. **Governance vollständig:** Jeder Eintrag in `OPEN_DECISIONS.md` trägt den Status DONE, ARCHIVIERT oder ERSETZT. Kein Eintrag trägt mehr den Status „Offen".
2. **Tier-1-Scientific-Debt bearbeitet:** W-001, SD-SYS-001, SD-SYS-004 und SD-B010-001 tragen jeweils einen Bearbeitungsvermerk, der über „Externe Validierung ausstehend / Abstract-Ebene" hinausgeht — entweder inhaltliche Präzisierung mit Primärtext-Beleg oder explizit begründete, mit Felix abgestimmte Dokumentation der Nicht-Auflösbarkeit.
3. **Evidenzfeld-Vollständigkeit und -Einheitlichkeit:** Alle 368 (oder zum Zeitpunkt der Prüfung aktuellen) Wissensobjekte tragen ein Evidenzfeld; die Feldbenennung ist repository-weit einheitlich (ein Name pro Objekttyp, kein Synonym-Wildwuchs).
4. **Keine Evidenzlevel-Desynchronisation:** Ein vollständiger Abgleich aller MEC-Objekte gegen ihre abhängigen T-/P-Objekte zeigt keine Fälle, in denen ein T-/P-Objekt ein höheres Evidenzlevel trägt als sein zugrundeliegender, zuletzt geprüfter Mechanismus.
5. **Repository-Hygiene bereinigt:** Kein leerer/verwaister Ordner, keine zwei koexistierenden, widersprüchlichen Versionen desselben Referenzdokuments ohne klare Statusmarkierung (aktiv/archiviert).
6. **RC1-Audit bestanden:** Ein vollständiger, unabhängig durchgeführter Audit nach Phase-4-Methodik liegt vor und listet keine neuen, unadressierten Tier-1-Blocker.
7. **Herausgeber-Freigabe:** Felix erteilt formal die Freigabe „Version 1.0 erreicht" — dieses Programm kann den Weg dorthin definieren, aber die Freigabe selbst ist und bleibt eine Herausgeber-Entscheidung, keine KI-Selbsteinschätzung (Grundregel: „Keine eigene Erinnerung als Autorität").

**Ausdrücklich NICHT Teil der Definition of Done** (siehe Kapitel 7, Nicht-Blocker): vollständige akademische Auflösung der Priming-Replikationsdebatte, Domänenerweiterung (Account Management, Pricing, Digital Sales), Umsetzung von OD-008 (ELM/Trust/PKM), AR-003 bis AR-012, geografisch-kulturelle Diversifizierung, Erreichen der Reifegrad-Note „A-" (B+ mit geschlossenen Tier-1-Punkten ist ausreichend für 1.0 — A- bleibt ein Ziel für eine spätere Version, siehe OD-009).

---

# 12. Executive Summary

Der Sales Codex ist ein evidenzbasiertes, wissenschaftlich kuratiertes Wissenssystem über B2B-Vertrieb, Verhandlung und Käuferpsychologie. Nach zehn vollständig analysierten Büchern (368 kanonische Wissensobjekte: 201 Statements, 48 Annahmen, 21 Mechanismen, 47 Prinzipien, 41 Techniken, 10 Modelle), zwei Synthese-Sprints, zwei Peer-Review-Zyklen, einem zweiphasigen Academic Recovery Sprint, einem vollständigen externen Repository-Audit (Gesamtnote B+) und einem Governance-Bereinigungssprint befindet sich der Codex erstmals in einem Zustand, der eine formale Entwicklung auf eine erste Gesamtversion — Sales Codex 1.0 — rechtfertigt.

Der Codex unterscheidet sich von einer Buchsammlung durch aktive Canonicalisierung (Wiederverwendungsraten zwischen 0 % und 67 % je nach thematischer Nähe der Bücher) und von einem Notizsystem durch ein fünfstufiges Evidenzsystem (E1–E5) sowie eine aktiv geführte Scientific-Debt-Matrix mit 56 Einzeleinträgen und 6 systemischen Clustern. Seine größte nachweisbare Stärke ist eine wiederholte, konkrete Selbstkorrekturbereitschaft: Mechanismen wurden im Peer Review aktiv herabgestuft (MEC-0010, MEC-0011 von E3 auf E2), Gutachter-Empfehlungen wurden mit fachlicher Begründung abgelehnt (MEC-0006/MEC-0014-Fusion, vorschnelle CTX-Einführung), und Zitationsfehler wurden transparent korrigiert statt stillschweigend bereinigt.

Zwei strukturelle Lücken verhindern aktuell eine Version 1.0: Erstens ist der methodische Kernwiderspruch W-001 (Teach First vs. Diagnose First zwischen Challenger Sale und Gap Selling) seit Sprint 1 unaufgelöst und schränkt die operative Anwendbarkeit der zentralen Prinzipien-Ebene ein. Zweitens beruht die B2B-Kernmethodik (SPIN/Huthwaite, Challenger/CEB, JOLT/Tethr) weiterhin auf proprietären, nicht unabhängig peer-reviewten Datensätzen, ohne dass eine sales-spezifische Publication-Bias-Einordnung vorliegt. Beide Lücken sind seit mehreren Prüfzyklen bekannt, priorisiert und Gegenstand konkreter, bereits identifizierter nächster Rechercheschritte (AR-001, AR-002, AR-013) — sie sind damit keine offenen Unbekannten, sondern definierte, angehbare Arbeitspakete.

Zusätzlich bestehen sechs aktiv offene Herausgeber-Entscheidungen (OD-006 bis OD-011): ob ein Meme-Risiko-Filter für das Quellen-Konvergenz-Rating eingeführt wird (direkt relevant für die am stärksten konvergierte Einzelaussage des Codex), ob eine neue Kontext-Ebene (CTX) das Wissensmodell erweitert (direkt relevant für die schwächste Reifegrad-Dimension, Generalisierbarkeit C+), sowie drei neu identifizierte, langfristige Governance-Fragen zu Versionierung, Validierungs-Methodik und dem Status des neu angelegten Literaturverzeichnisses.

Dieses Programm definiert fünf Phasen bis Version 1.0: Governance (alle sechs offenen Entscheidungen klären), Scientific Completion (die beiden Tier-1-Lücken mit Primärtext bearbeiten), Architecture Freeze (repository-weite Konsistenz herstellen, keine neue Recherche), Release Candidate (ein erneuter, vollständiger Audit bestätigt den Zustand) und schließlich Version 1.0 selbst (formale Herausgeber-Freigabe). Explizit kein Blocker sind Domänenerweiterungen (Account Management, Pricing Psychology, digitale Vertriebsprozesse), die vertiefende Bearbeitung nachrangiger Academic-Recovery-Themen (Tier 2–4) und das Erreichen der höchsten denkbaren Reifegrad-Note — eine transparent dokumentierte, konsistente B+-Basis mit geschlossenen Kernlücken ist für eine erste Version 1.0 ausreichend und ehrlicher als eine verzögerte Freigabe zugunsten einer nicht klar definierten „Perfektion".

Der Sales Codex hat in seiner bisherigen Entwicklung wiederholt gezeigt, dass er in der Lage ist, sich selbst zu widersprechen, wenn die Evidenz es verlangt. Dieses Programm überträgt dieselbe Disziplin auf die Versionsfreigabe selbst: Version 1.0 wird nicht erklärt, sie wird anhand der in Kapitel 11 definierten, objektiven Kriterien erreicht — oder eben noch nicht.

---

*Erstellt: 2026-07-02 | SALES CODEX 1.0 PROGRAM | Reine Programm-Definition, keine inhaltliche Sprintarbeit | KI-Redaktion Sales Codex | Nächster Schritt: Herausgeber-Entscheidungsrunde Phase 1 (OD-006 bis OD-011 plus Repository-Hygiene) — siehe Kapitel 4 und 10.*
