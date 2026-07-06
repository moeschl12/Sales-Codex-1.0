# Research Portfolio — Sales Codex

**Dokumentklasse:** Reference / Governance (Steuerungs- und Priorisierungsebene, kein Wissensobjekt, keine Framework-Datei, kein Forschungsprojekt im Sinne von `RESEARCH_GOVERNANCE.md`)
**Rolle bei Erstellung:** Research Portfolio Architect (Claude), im Auftrag des Herausgebers — ausschließlich Konsolidierung, Architektur, Priorisierungsvorschlag. Kein Forscher, kein Framework-Architekt, keine Herausgeberentscheidung.
**Version:** 1.6 (Editor-Decision-W-004-Update — Version 1.0 war die Initialisierung, Version 1.1 die RP-001-Aktivierung, Version 1.2 das Editor-Decision-W-002-Update, Version 1.3 die RP-002-Aktivierung, Version 1.4 das Editor-Decision-W-003-Update, Version 1.5 die RP-004-Aktivierung)
**Stand:** 2026-07-06
**Auslöser:** Herausgeberauftrag „Research Portfolio Initialization Sprint" (Version 1.0); ergänzt durch Herausgeberauftrag „RP-001 Activation — ELM Persuasion Architecture Research Project" (Version 1.1 — RP-001 auf `Active Research` gesetzt, RP-002 mit Vermerk „bevorzugter nächster Kandidat" versehen); ergänzt durch „Editor Decision — W-002" (Version 1.2 — RP-001 nach abgeschlossener Repository Integration und bestandenem Health Check auf `Integrated` gesetzt); ergänzt durch Herausgeberauftrag „RP-002 Activation — Trust Formation & Relationship Marketing Research Project" (Version 1.3 — RP-002 auf `Active Research` gesetzt, Projekt-ID **W-003**); ergänzt durch „Editor Decision — W-003" (Version 1.4 — RP-002 nach abgeschlossener Repository Integration und bestandenem Health Check auf `Integrated` gesetzt, siehe Theme Card und Abschnitt 6); ergänzt durch Herausgeberauftrag „RP-004 Activation — Buying Center Social Dynamics Research Project" (Version 1.5, 2026-07-06 — RP-004 auf `Active Research` gesetzt, Projekt-ID **W-004**, nachdem der Herausgeber auf explizite Nachfrage die Wahl zwischen dem score-gleichen RP-003 und RP-004 zugunsten von RP-004 bestätigt hatte); ergänzt durch „Editor Decision — W-004" (Version 1.6, 2026-07-06 — RP-004 nach abgeschlossener Repository Integration und bestandenem Health Check auf `Integrated` gesetzt, siehe Theme Card und Abschnitt 6). RP-001, RP-002 und RP-004 sind nun `Integrated`. RP-003, RP-005 bis RP-008 bleiben unverändert.
**Grundlage:** `PROJECT_BOOTSTRAP.md`, `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/OPEN_DECISIONS.md`, `00_project/SCIENTIFIC_DEBT.md`, `00_project/SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, `00_project/KNOWLEDGE_ATLAS_GOVERNANCE.md`, `05_research/LITERATURE_INDEX.md`, `04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md`, `00_project/review_queue.md`, `06_research_program/completed/W001/*`, direkte Einsicht der Objekte MEC-0020, MEC-0021, MEC-0025.
**Vollständiger Methodenbericht:** `00_project/RESEARCH_PORTFOLIO_INITIALIZATION_REPORT.md`

---

## 1. Purpose

Dieses Dokument beantwortet genau eine Frage: **In welche Forschungsthemen sollte der Sales Codex seine begrenzte Forschungszeit als Nächstes investieren?**

Es führt keine neue Forschung durch, verifiziert keine Literatur eigenständig, legt keine neuen Wissensobjekte an und ändert kein bestehendes Wissensobjekt. Es überführt bereits im Repository dokumentierte Forschungsbedarfe — offene Entscheidungen, Scientific-Debt-Einträge, Research-Agenda-Punkte, Atlas-Befunde und selektiv verwertbare externe Empfehlungen — in eine gemeinsame, priorisierbare Portfolioebene.

Das Portfolio ersetzt keine bestehende Datei und erzeugt keine parallele Forschungsdatenbank. Jeder Eintrag verweist auf vorhandene Strukturen, statt sie zu duplizieren.

---

## 2. Governance Position

Das Research Portfolio steht **über** dem Research Program (`06_research_program/RESEARCH_GOVERNANCE.md`), nicht daneben oder darunter:

```
Portfolio-Ebene (dieses Dokument)
   ↓ priorisiert und empfiehlt
Research-Program-Ebene (RESEARCH_GOVERNANCE.md, W-XXX-Projekte)
   ↓ produziert
Sales-Codex-Wissensbasis (03_knowledge_base/)
```

Das Portfolio trifft **keine** Herausgeberentscheidung und eröffnet **kein** Forschungsprojekt. Es liefert dem Herausgeber (Felix) eine konsolidierte Entscheidungsgrundlage, auf deren Basis er entscheiden kann, ob und welches Thema als nächstes `W-XXX`-Projekt eröffnet wird — gemäß `RESEARCH_GOVERNANCE.md`, Abschnitt 4.1 ("Freigabe jedes Forschungsprojekts bei Aufnahme" bleibt ausschließlich Herausgeber-Befugnis).

**Wichtiger Kontext (unverändert gültig):** Sales Codex Version 1.0 ist veröffentlicht und gilt als unveränderlich; Version 1.1 wurde noch nicht formal eröffnet (`CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`). Jedes Theme in diesem Portfolio ist daher eine **Entscheidungsvorlage für ein künftiges Version-1.1-Programm**, kein sofort ausführbarer Auftrag. Die Eröffnung eines `W-XXX`-Projekts aus diesem Portfolio heraus setzt die formale Eröffnung eines Version-1.1-Programms voraus, sofern der Herausgeber nichts anderes bestimmt.

---

## 3. Relationship to Existing Research Systems

Das Portfolio dupliziert keines der folgenden Dokumente — es referenziert sie:

| Bestehendes System | Regelt | Verhältnis zum Portfolio |
|---|---|---|
| `00_project/OPEN_DECISIONS.md` | Konkrete, einzeln zu entscheidende Herausgeberfragen (OD-001 bis OD-012) | Das Portfolio bündelt die forschungsrelevanten offenen Entscheidungen (insb. OD-008) unter einem Thema, ändert aber keine OD und legt keine neue OD an. |
| `00_project/SCIENTIFIC_DEBT.md` | Dokumentierte Evidenzlücken je Wissensobjekt | Einzelne Scientific-Debt-Einträge werden als „Repository Evidence" in Theme Cards zitiert, nicht neu bewertet oder verändert. |
| `05_research/LITERATURE_INDEX.md` | Verifizierte und nicht-verifizierte Literatur | Themes verweisen auf dort bereits geführte oder in `review_queue.md` vorgemerkte Quellenkandidaten — es wird keine neue Literaturzeile angelegt. |
| `04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md` | Priorisierte Forschungsfragen aus Sprint 1 (F-001 bis F-012) | Noch relevante F-Punkte (insb. F-002, F-009) sind Repository Evidence für einzelne Themes; erledigte F-Punkte (F-001) werden nicht erneut aufgeführt. |
| `00_project/review_queue.md` | Nicht angelegte Objekt- und Fusionskandidaten | Literaturkandidaten (ELM, Trust Formation, Persuasion Knowledge Model, Fairness/Equity Theory, Choice Architecture) sind die unmittelbarste Quelle der „Known Source Candidates" mehrerer Themes. |
| `06_research_program/RESEARCH_GOVERNANCE.md` + `RESEARCH_STATUS.md` | Der 9-stufige Lifecycle einzelner `W-XXX`-Projekte | Ein aus diesem Portfolio priorisiertes Theme wird — bei Herausgeber-Freigabe — zu einem neuen `W-XXX`-Eintrag in `RESEARCH_STATUS.md` und durchläuft den dortigen Prozess unverändert. |
| `00_project/KNOWLEDGE_ATLAS_GOVERNANCE.md` | Wann/wie oft der Knowledge Atlas erneut aktiv wird | Atlas-Befunde (Underused Strengths, Structure × Evidence Risk) sind Repository Evidence, keine eigenständige Portfolio-Quelle — der Atlas bleibt reines Diagnoseinstrument (`KNOWLEDGE_ATLAS_GOVERNANCE.md`, Abschnitt 8). |

**Explizite Nicht-Duplikation:** Kein Theme in Abschnitt 7 enthält eine vollständige Kopie eines Scientific-Debt-Eintrags, einer Open Decision oder einer Literaturzeile. Jedes Feld „Repository Evidence" nennt ausschließlich Dateiverweise und eine Kurzparaphrase.

---

## 4. Portfolio Lifecycle

Das Portfolio verwendet ein eigenständiges Statusvokabular für **Themes** (Portfolioebene) — es ist nicht identisch mit dem Statusvokabular für **Forschungsprojekte** (`RESEARCH_GOVERNANCE.md`, Abschnitt 5: `ACTIVE (Stufe N)`, `ON_HOLD`, `AWAITING_EDITOR_DECISION`, `INTEGRATING`, `HEALTH_CHECK`, `COMPLETED`, `ARCHIVED`). Ein Theme ist eine Portfolioeinheit oberhalb eines konkreten `W-XXX`-Projekts; ein Theme kann existieren, ohne dass je ein `W-XXX`-Projekt für es eröffnet wurde.

| Theme-Status | Bedeutung |
|---|---|
| **Candidate** | In mindestens einer Quelle (Gemini-Report, Peer Review, Scientific Debt, Open Decision, Atlas, Research Agenda, Review Queue) genannt, aber Repository-Bezug oder Abgrenzung zu bestehenden Themes noch nicht vollständig geprüft. |
| **Validated** | Die wissenschaftliche oder strategische Lücke ist gegen den tatsächlichen Repository-Zustand geprüft und durch mindestens eine belastbare interne Quelle bestätigt (nicht nur durch eine unverifizierte externe Behauptung). |
| **Prioritized** | Der Herausgeber hat das Theme explizit für eine der nächsten Investitionsentscheidungen ausgewählt. **Kein Theme in diesem Dokument trägt diesen Status** — die Zuweisung ist ausschließlich Herausgeber-Befugnis und liegt zum Stand dieses Sprints noch nicht vor (siehe Abschnitt 11). |
| **Active Research** | Ein `W-XXX`-Projekt wurde für dieses Theme eröffnet (Übergang in `RESEARCH_STATUS.md`, Abschnitt 1). |
| **Integrated** | Das `W-XXX`-Projekt ist abgeschlossen, Editor Decision positiv oder teilweise positiv, Repository Integration und Health Check bestanden (Übergang in `RESEARCH_STATUS.md`, Abschnitt 2). |
| **Closed** | Das Thema ist ohne eigenes `W-XXX`-Projekt erledigt — z. B. weil eine andere, bereits laufende Arbeit (Buchanalyse, Synthese-Sprint) die Lücke zwischenzeitlich geschlossen hat. |
| **Rejected** | Der Herausgeber hat entschieden, das Thema nicht weiterzuverfolgen. |

**Übergänge:** Candidate → Validated erfolgt durch einen Konsolidierungssprint wie diesen. Validated → Prioritized erfolgt ausschließlich durch Herausgeberentscheidung (Abschnitt 11 dieses Dokuments dokumentiert eine Empfehlung, keine Zuweisung). Prioritized → Active Research erfolgt durch Eröffnung eines `W-XXX`-Ordners gemäß `RESEARCH_GOVERNANCE.md`. Active Research → Integrated/Rejected folgt exakt dem bestehenden 9-Stufen-Lifecycle. Jedes Theme kann jederzeit direkt nach Closed wechseln, wenn eine externe Entwicklung (z. B. eine Buchanalyse, die zufällig dieselbe Lücke schließt) es erledigt — dies wird im Portfolio dokumentiert, nicht automatisch.

---

## 5. Prioritization Model

Jedes Theme wird auf einer Skala von 1–5 in fünf Dimensionen bewertet:

| Dimension | 1 bedeutet | 5 bedeutet | Gewicht |
|---|---|---|---|
| Scientific Gap | Lücke ist klein oder bereits weitgehend abgedeckt | Lücke ist groß — kein bestehendes Objekt deckt sie ab | 30 % |
| Strategic Relevance | Geringe Bedeutung für den Sales Codex insgesamt | Sehr hohe strategische Bedeutung | 25 % |
| Practical Leverage | Geringer unmittelbarer Praxishebel für Vertriebsarbeit | Sehr hoher Praxishebel | 20 % |
| Integration Leverage | Würde nur ein isoliertes Objekt berühren | Würde viele bestehende Objekte/Bereiche stärken, kalibrieren oder operationalisieren | 15 % |
| Research Cost | Geringer Aufwand (Literaturergänzung) | Hoher Aufwand (vollständige Primärquellenbeschaffung + Buchanalyse-artiger Prozess) | 10 %, invers |

**Orientierungsscore:** `0,30 × Scientific Gap + 0,25 × Strategic Relevance + 0,20 × Practical Leverage + 0,15 × Integration Leverage + 0,10 × (6 − Research Cost)`

Der Score ist eine Entscheidungshilfe, keine automatische Entscheidung. Bei eng beieinanderliegenden Werten (siehe Abschnitt 6) wird dies explizit ausgewiesen, statt eine falsche Präzision zu suggerieren. Die Herausgeberentscheidung bleibt in jedem Fall maßgeblich.

---

## 6. Active Research Portfolio

Übersicht aller acht konsolidierten Themes mit Scoring. Ursprünglich trug kein Theme den Status `Prioritized`, `Active Research`, `Integrated` oder `Rejected` — alle waren entweder `Validated` oder `Candidate` (Begründung: Abschnitt 4). **Aktualisierung 2026-07-05 (RP-001 Activation):** RP-001 wurde per Herausgeber-Freigabe auf `Active Research` gesetzt. **Aktualisierung 2026-07-05 (Editor Decision W-002):** RP-001 wurde nach Abschluss von W-002 (Teilweise annehmen, Repository Integration abgeschlossen, Health Check bestanden) auf `Integrated` gesetzt (siehe Theme Card RP-001 und `OPEN_DECISIONS.md` OD-008). **Aktualisierung 2026-07-05 (RP-002 Activation, Editor Decision W-003):** RP-002 wurde per Herausgeber-Freigabe auf `Active Research` und nach Abschluss von W-003 auf `Integrated` gesetzt. **Aktualisierung 2026-07-06 (RP-004 Activation):** RP-004 wurde per Herausgeber-Freigabe auf `Active Research` gesetzt (Projekt-ID W-004) — trotz score-gleicher Position mit RP-003 (je 4,05), nach expliziter Herausgeber-Bestätigung der bereits in der Einordnungsspalte dokumentierten qualitativen Präferenz für RP-004. **Aktualisierung 2026-07-06 (Editor Decision W-004):** RP-004 wurde nach Abschluss von W-004 (Teilweise annehmen, Repository Integration abgeschlossen, Health Check bestanden) auf `Integrated` gesetzt (siehe Theme Card RP-004). RP-003 sowie RP-005 bis RP-008 sind unverändert `Validated`/`Candidate`.

| ID | Theme | Status | Gap | Strat. | Prakt. | Integr. | Kosten | Score | Einordnung (Abschnitt 10) |
|---|---|---|---|---|---|---|---|---|---|
| RP-001 | Persuasion Architecture (Elaboration Likelihood Model) | **Integrated** (W-002, abgeschlossen 2026-07-05) | 4 | 5 | 4 | 5 | 2 | **4,40** | Top Priority |
| RP-002 | Trust Formation & Relationship Marketing | **Integrated** (W-003, abgeschlossen 2026-07-05) | 3 | 5 | 4 | 4 | 2 | **3,95** | Top Priority |
| RP-003 | Cognitive Load & Decision Complexity | Validated | 5 | 4 | 4 | 3 | 3 | **4,05** | Secondary Priority |
| RP-004 | Buying Center Social Dynamics & Organisationale Risikoverteilung | **Integrated** (W-004, abgeschlossen 2026-07-06) | 4 | 5 | 4 | 4 | 4 | **4,05** | Top Priority |
| RP-005 | Negotiation Science Calibration | Validated | 3 | 4 | 3 | 3 | 2 | **3,35** | Secondary Priority |
| RP-006 | Principal-Agent Theory & Organisationale Mikropolitik | Validated | 3 | 3 | 3 | 3 | 3 | **3,00** | Secondary Priority |
| RP-007 | Ecological Rationality (Heuristiken als adaptive Werkzeuge) | Candidate | 2 | 3 | 2 | 2 | 3 | **2,35** | Watchlist |
| RP-008 | Change Motivation / Motivational Interviewing | Candidate | 2 | 2 | 3 | 2 | 4 | **2,20** | Watchlist |

**Hinweis zur Rangfolge:** Die vier höchsten Scores (RP-001: 4,40; RP-003 und RP-004: je 4,05; RP-002: 3,95) liegen eng beieinander — die Trennschärfe des Scores allein reicht in diesem oberen Band nicht aus, um mechanisch zu entscheiden. Abschnitt 10 löst dies nicht rein rechnerisch, sondern zusätzlich unter Rückgriff auf bereits bestehende Governance-Signale (insbesondere OD-008, das RP-001 und RP-002 bereits vor diesem Sprint als höchste bzw. zweithöchste Literaturpriorität führt). Dies ist eine bewusste, im Portfolio dokumentierte Abwägung, keine verdeckte Score-Manipulation.

---

## 7. Theme Cards

### RP-001 — Persuasion Architecture (Elaboration Likelihood Model)

**Research Theme:** Zentrale vs. periphere Verarbeitungsroute der Persuasion (Elaboration Likelihood Model, Petty & Cacioppo 1986) als fehlendes theoretisches Dach über bestehende Persuasionsmechanismen.

**Problem Definition:** Der Sales Codex verfügt über zahlreiche einzelne Persuasionsmechanismen (Cialdini-Familie MEC-0005–0009, MEC-0012 Dual Process, MEC-0018 Pre-Suasion), aber kein Objekt modelliert die übergeordnete Unterscheidung zwischen tiefer (zentraler) und oberflächlicher (peripherer) Verarbeitungsroute, die erklären würde, unter welchen Bedingungen welcher dieser Mechanismen greift oder versagt.

**Repository Evidence:** `00_project/OPEN_DECISIONS.md` OD-008 (ELM dort bereits als „höchste Priorität" unter den nicht angelegten Literaturkandidaten geführt, seit 2026-07-01 unentschieden); `05_research/LITERATURE_INDEX.md` Zeile zu Petty & Cacioppo (1986), Vermerk „Nicht angelegt — höchste Priorität"; `00_project/review_queue.md`, Abschnitt „MEC-Kandidat: Elaboration Likelihood Model — höchste Priorität"; `00_project/SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 3 Empfehlung 4 (unabhängige Bestätigung der bestehenden Priorität, nicht Gemini zuzuschreiben); `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, Abschnitt 3.2/9 (MEC-0018 als strukturell zentraler, aber evidenzschwacher Hub — ein ELM-Rahmen könnte theoretisch erklären, warum gerade peripher wirkende Mechanismen wie Pre-Suasion strukturell fragiler sind).

**Strategic Relevance:** Höchste unter allen geprüften Themes — schließt eine seit dem Academic Recovery Sprint dokumentierte und bislang offene Top-Priorität (OD-008) und liefert zugleich ein mögliches theoretisches Erklärungsmodell für den robustesten Einzelbefund des Knowledge Atlas (MEC-0018-Strukturrisiko).

**Practical Leverage:** Hilft zu kalibrieren, wann eine Verkaufsbotschaft auf tiefe Verarbeitung (hohe Kaufkomplexität, viele Entscheider, lange Zyklen) statt auf periphere Cues (Autorität, Ähnlichkeit, Verknappung) setzen sollte — direkt relevant für Pitch-Aufbau, Angebotsgestaltung und Priorisierung von Techniken je Vertriebsphase.

**Integration Leverage:** Potenziell das Theme mit der höchsten Reichweite im gesamten Portfolio — berührt MEC-0005 bis MEC-0009 (Cialdini-Familie, überwiegend peripher), MEC-0012 (Dual Process, bereits verwandt), MEC-0018 (Pre-Suasion, peripher mit dokumentiertem Evidenzrisiko), MOD-0002, MOD-0008.

**Known Source Candidates:** Petty, R.E. & Cacioppo, J.T. (1986). *Communication and Persuasion: Central and Peripheral Routes to Attitude Change*. Springer (bereits in `LITERATURE_INDEX.md` und `review_queue.md` geführt, kein Primärtextzugriff bisher). Verwandt, aber nicht identisch: Friestad & Wright (1994), Persuasion Knowledge Model — bereits teilweise über eine Zitat-Ergänzung in MEC-0003 abgedeckt (siehe Abschnitt 9, Excluded).

**Dependencies:** OD-008 (unmittelbare Abhängigkeit — eine Herausgeber-Entscheidung zu OD-008 ist der naheliegende Auslösekanal für dieses Theme); Scientific Debt zu MEC-0018 (B-0010, Priorität Hoch); Atlas-Sprint-1-Empfehlung (Editorial Review Priority MEC-0018-Familie, bereits separat in Bearbeitung laut `KNOWLEDGE_ATLAS_GOVERNANCE.md` Abschnitt 9 Verweis auf `EDITORIAL_REVIEW_SPRINT_MEC0018_REPORT.md`); keine laufende `W-XXX`.

**Status:** Integrated (seit 2026-07-05 — W-002 vollständig durchlaufen, Editor Decision „Teilweise annehmen", Repository Integration und Health Check abgeschlossen).

**Herausgeber-Freigabe (2026-07-05):** Felix hat mit dem Auftrag „RP-001 Activation — ELM Persuasion Architecture Research Project" die Aktivierung dieses Themes als reguläres Forschungsprojekt angeordnet, dokumentiert zugleich in `OPEN_DECISIONS.md` OD-008. Projekt-ID: **W-002** („Persuasion Architecture — Elaboration Likelihood Model in Complex Sales Contexts", `06_research_program/completed/W002/`).

**Editor Decision und Integration (2026-07-05):** Felix hat W-002 mit „Editor Decision — W-002" **teilweise angenommen**: Kein eigenständiges neues MEC für ELM (editorische Sparsamkeitsentscheidung); ELM als persuasionsspezifische Klassifikationsebene in MEC-0012, MEC-0005–0008, MEC-0018 und MOD-0002 integriert (Boundary Conditions/Cross-Links/Synthese, kein neuer Kausalpfad, keine E-Level-Änderung); MEC-0009 und MOD-0008 unabhängig geprüft und begründet unverändert gelassen; keine Integration einer B2B-/Buying-Center-Transferaussage — stattdessen neue Position in `00_project/SCIENTIFIC_DEBT.md`, Sektion „W-002", ohne automatisches Folgeforschungsprojekt. Vollständige Dokumentation: `06_research_program/completed/W002/06_EDITOR_DECISION.md`, `REPOSITORY_INTEGRATION_LOG.md`, `HEALTH_CHECK.md` (bestanden).

**Next Decision:** Keine unmittelbar anstehende Entscheidung zu diesem Theme. Etwaige künftige Vertiefung (z. B. systematische B2B-/Buying-Center-Literaturrecherche) setzt eine neue Portfolio- und Herausgeberentscheidung voraus (siehe `SCIENTIFIC_DEBT.md`, Sektion „W-002").

---

### RP-002 — Trust Formation & Relationship Marketing

**Research Theme:** Formales Vertrauensmodell (Mayer, Davis & Schoorman 1995: Ability/Benevolence/Integrity) und ergänzende Meta-Analyse-Evidenz zu Beziehungsvertrieb (Palmatier et al. 2006) als fehlendes mechanistisches Fundament für „Vertrauen" im Sales Codex.

**Problem Definition:** „Trust" taucht bereits implizit in mehreren Objekten auf (MEC-0007 Liking, MOD-0003, MOD-0007 Getting to Yes), ohne dass ein eigenständiger, mechanistisch definierter Trust-Baustein existiert. Dies limitiert insbesondere die Aussagekraft zu langfristigem Beziehungsvertrieb und zur ungeklärten CEB-Loyalitätsdebatte (A-0019).

**Repository Evidence:** `OPEN_DECISIONS.md` OD-008 (Trust Formation dort als zweithöchste Priorität geführt, „konvergent in Pack 3 und Pack 4 identifiziert"); `review_queue.md`, Abschnitt „MEC-Kandidat: Trust Formation"; `LITERATURE_INDEX.md` Zeile zu Mayer, Davis & Schoorman (1995); `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 3 Empfehlung 2 (Palmatier, Dant, Grewal & Evans 2006 als zusätzlicher, unabhängig bestätigter Meta-Analyse-Kandidat — „übernehmen"); `SCIENTIFIC_DEBT.md`, SD-SYS-001 (A-0019 CEB-Loyalitätsbehauptung durch Verbeke/Dietz/Verwaal-Metaanalyse nicht gestützt — ein formalisiertes Trust-Modell könnte hier präzisere Anschlussfähigkeit liefern als die bisherige Loyalitätsdebatte allein).

**Strategic Relevance:** Zweithöchste im Portfolio — adressiert eine seit ARS-0001 (2026-07-01) dokumentierte, konvergent aus zwei unabhängigen Research Packs identifizierte Lücke und liefert zugleich potenziellen Beitrag zur ungelösten A-0019-Debatte.

**Practical Leverage:** Relevanz für Account-Management, mehrperiodische B2B-Kundenbeziehungen und die Frage, wann Beziehungsvertrieb (Trust-Aufbau) gegenüber transaktionaler Verkaufslogik (Diagnose/Teaching, vgl. W-001) den Ausschlag gibt.

**Integration Leverage:** Berührt MEC-0007 (Liking), MOD-0003 (Voss/BCSM), MOD-0007 (Getting to Yes), A-0019 (CEB-Loyalität) — vier bereits zentrale Objekte, die durch ein formales Trust-Konstrukt präzisiert statt ersetzt würden.

**Known Source Candidates:** Mayer, R.C., Davis, J.H. & Schoorman, F.D. (1995). *An Integrative Model of Organizational Trust*. Academy of Management Review, 20(3), 709–734 (bereits in `LITERATURE_INDEX.md`/`review_queue.md`, kein Primärtextzugriff). Palmatier, R.W., Dant, R.P., Grewal, D. & Evans, K.R. (2006), Meta-Analyse zu Relationship Marketing im *Journal of Marketing* (durch Peer Review vorgeschlagen, **noch nicht websuchverifiziert** — vor Aufnahme in `LITERATURE_INDEX.md` gemäß Academic-Recovery-Standardverfahren zu prüfen).

**Dependencies:** OD-008 (identische Abhängigkeit wie RP-001 — beide Kandidaten stehen in derselben offenen Entscheidung); SD-SYS-001/A-0019 (Scientific Debt); abgeschlossene `W-003`.

**Status:** Integrated (seit 2026-07-05 — W-003 vollständig durchlaufen, Editor Decision „Teilweise annehmen", Repository Integration und Health Check abgeschlossen).

**Herausgeber-Freigabe (2026-07-05):** Felix hat mit dem Auftrag „RP-002 Activation — Trust Formation & Relationship Marketing Research Project" die Aktivierung dieses Themes als reguläres Forschungsprojekt angeordnet, im Anschluss an die abgeschlossene Editor Decision zu W-002 (RP-001, „Teilweise annehmen", 2026-07-05). Projekt-ID: **W-003** („Trust Formation & Relationship Marketing in Complex Sales Relationships", `06_research_program/completed/W003/`).

**Editor Decision und Integration (2026-07-05):** Felix hat W-003 mit „Editor Decision — W-003" **teilweise angenommen**: Option E (strukturelle Trennung von Trust Formation und Relationship Marketing) angenommen; genau ein eng geschnittenes neues MEC (MEC-0030, „Vertrauensbildung aus wahrgenommener Vertrauenswürdigkeit") für die Ability/Benevolence/Integrity→Trustworthiness→Trust-Kette angelegt, mit korrigierter Begründung (kein „Benevolence fehlt komplett", sondern fehlender canonicalisierter Mechanismus) unter ausdrücklicher Einbeziehung von P-0040/A-0045; keine getrennten Cognitive-/Affective-Trust-MECs; kein neues MOD für Relationship Marketing — stattdessen 13 bestehende Wissensobjekte erweitert (MEC-0007, MEC-0008, MEC-0006, MEC-0014, MOD-0003, MOD-0007, A-0019, A-0029, A-0034, ST-0161, ST-0146, P-0012, P-0040, A-0045) über Cross-Links, Citation Enrichment, Boundary Conditions und Evidenzkalibrierung, ohne automatische E-Level-Aufwertung; Relationship Marketing als eigenständiges MEC/MOD, mehrere Trust-MECs und direkte High-Ticket-B2C-/Fertighaus-Techniken nicht integriert. Neun offene Fragen (OQ-1 bis OQ-9) als Scientific Debt dokumentiert, kein automatisches Folgeprojekt. Vollständige Dokumentation: `06_research_program/completed/W003/06_EDITOR_DECISION.md`, `REPOSITORY_INTEGRATION_LOG.md`, `HEALTH_CHECK.md` (bestanden).

**Next Decision:** Keine unmittelbar anstehende Entscheidung zu diesem Theme. Etwaige künftige Vertiefung (z. B. Social-Exchange-Theory-Konkurrenzprüfung OQ-8, Palmatier-Volltextverifikation OQ-2/OQ-3, High-Ticket-B2C-Primärforschung OQ-5) setzt eine neue Portfolio- und Herausgeberentscheidung voraus (siehe `00_project/SCIENTIFIC_DEBT.md`, Sektion „W-003").

---

### RP-003 — Cognitive Load & Decision Complexity

**Research Theme:** Kognitive Belastungstheorie (Cognitive Load Theory, Sweller) als eigenständiger Mechanismus für Entscheidungskomplexität bei mehrstufigen, mehrattributiven B2B-Kaufentscheidungen.

**Problem Definition:** Der Codex hat aktuell keinen Mechanismus, der Arbeitsgedächtnis-Kapazitätsgrenzen bei komplexen Angeboten/Demos direkt modelliert. Der nächstliegende Baustein (T-0022, „6-Feature-Regel") beruht auf Miller's Law (1956), nicht auf moderner Cognitive-Load-Forschung — eine bereits im Repository dokumentierte Erweiterungslücke.

**Repository Evidence:** `04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md`, F-009 („6-Feature-Regel: Empirische Basis jenseits von Miller's Law", Tier 3, bislang unbearbeitet); `SCIENTIFIC_DEBT.md`, B-0005-Sektion (T-0022, MEC-0015: „Miller's Law ist gut belegt, aber der optimale Feature-Count für Sales Demos ist empirisch nicht gemessen"); `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 3 Empfehlung 1 und Abschnitt 6 (GAP-03 als „echte, nicht triviale Lücke" bestätigt — **ausdrücklich mit der Einschränkung, dass die vom Gemini-Report selbst gegebene Herleitung über MEC-0020 nachweislich falsch ist**, siehe Abschnitt 5 dieses Dokuments und Peer-Review-Abschnitt 5).

**Strategic Relevance:** Hoch — adressiert eine der wenigen Lücken, die sowohl intern (research_agenda F-009, seit 2026-07-01 unbearbeitet) als auch extern (Peer Review, nach Korrektur der falschen Objektzuordnung) unabhängig bestätigt sind.

**Practical Leverage:** Sehr konkret operationalisierbar — Anzahl Features in Demos, Komplexität von Angebotsdokumenten, Choice-Overload-Vermeidung in RFP-Antworten.

**Integration Leverage:** Mittel — direkte Verbindung zu T-0022 und MEC-0015, aber (Stand heute) kein breiterer Anschluss an andere zentrale Objekte wie bei RP-001/RP-002.

**Known Source Candidates:** Sweller, J., Ayres, P. & Kalyuga, S. (2011). *Cognitive Load Theory*. Springer (durch Peer Review als Standardwerk vorgeschlagen, **nicht verifiziert, kein Primärtextzugriff** — vor Nutzung Standard-Websuche-Verifikation gemäß Academic-Recovery-Verfahren erforderlich).

**Dependencies:** research_agenda.md F-009 (unmittelbare Vorgänger-Frage); Scientific Debt B-0005 (T-0022, MEC-0015); **kein** Bezug zu MEC-0020 — die im Gemini-Report behauptete Verbindung zwischen GAP-03 und MEC-0020 ist nachweislich falsch (Abschnitt 9, siehe auch `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 5, Befund 1); keine laufende `W-XXX`.

**Status:** Validated.

**Next Decision:** Felix entscheidet, ob GAP-03/F-009 als eigener Recherche- oder Buchanalyse-Baustein für ein künftiges Version-1.1-Programm priorisiert wird — mit einer **neu zu formulierenden** Begründung (nicht der fehlerhaften Gemini-Herleitung über MEC-0020).

---

### RP-004 — Buying Center Social Dynamics & Organisationale Risikoverteilung

**Research Theme:** Gruppendynamik und Koalitionsbildung im B2B-Buying-Center (Social Identity Theory und verwandte Gruppendynamik-Forschung) als bislang nur über Konformität (MEC-0006) abgedeckte Lücke.

**Problem Definition:** B2B-Kaufentscheidungen sind strukturell Gruppenentscheidungen mehrerer Stakeholder mit unterschiedlichen, teils gegenläufigen Risikopositionen. Der Codex modelliert bislang nur den Konformitätsaspekt (MEC-0006, Asch/Sherif/Deutsch & Gerard), nicht Koalitionsbildung, interne Politik oder asymmetrische persönliche Risikoverteilung zwischen Buying-Center-Mitgliedern.

**Repository Evidence:** `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 6 (GAP-01 nach Prüfung als „tatsächlich relevant" und „Teilweise abgedeckt" bestätigt, wenn auch die Gemini-eigene Einschätzung „< 5 % Coverage" als „leicht überzeichnet" korrigiert); `00_project/review_queue.md`, Abschnitt „Neuer Meta-Prinzip-Kandidat: Asymmetrische Risikoverteilung im Buying Center" (bereits als eigenständiger, aus drei vollständig verarbeiteten Primärquellen — SPIN, Challenger, JOLT — konvergent begründeter Kandidat dokumentiert, Herausgeber-Entscheidung ausstehend); `SCIENTIFIC_DEBT.md`, SD-SYS-001 (A-0019, CEB-Loyalitätsbehauptung methodisch ungestützt — Buying-Center-Dynamik als mögliche differenziertere Erklärung); `KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, Abschnitt 7 (Community 7: bereits eine reale, graphisch sichtbare Cross-Book-Brücke zwischen Cialdini-Unity und Challenger-Profil-Statements — struktureller Beleg, dass eine Buying-Center-/Beziehungsdynamik-Synthese im Codex bereits ansatzweise existiert); `00_project/WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (Generalisierbarkeit/B2B-Transfer als schwächste Dimension, C+).

**Strategic Relevance:** Hoch — adressiert direkt die im Reifegradbericht dokumentierte schwächste Einzeldimension des Codex (B2B-Generalisierbarkeit) und verbindet zwei bereits unabhängig entstandene, aber noch nicht verknüpfte Repository-Beobachtungen (Atlas-Community-7-Brücke, Review-Queue-Meta-Prinzip-Kandidat).

**Practical Leverage:** Hoch — Umgang mit internen Champions, Koalitionsaufbau in komplexen Vertriebszyklen, Risikokommunikation gegenüber unterschiedlichen Buying-Center-Rollen.

**Integration Leverage:** Berührt MEC-0006 (Konformität, Abgrenzung erforderlich), MEC-0014 (Buying Center/Principal-Agent-Theorie-Referenzen, bereits vorhanden), A-0019 (CEB-Loyalität), sowie potenziell das bereits als Kandidat geführte Meta-Prinzip „Asymmetrische Risikoverteilung".

**Known Source Candidates:** Kein im Repository bereits benannter Primärtitel zu Social Identity Theory selbst (im Unterschied zu RP-001/RP-002 liegt hier noch kein konkreter, bereits geprüfter Buchkandidat vor) — der Gemini-Report nennt keinen verwertbaren Titel für diese Lücke (siehe Abschnitt 9, Nicht übernommene Gemini-Referenzliste). Bereits im Repository vorhandene, thematisch angrenzende Theorie-Referenzen: Webster & Wind (1972), Sheth (1973), Eisenhardt (1989, Agency Theory) — alle bereits in MEC-0014 als „Ergänzende Theorie-Referenzen" geführt.

**Dependencies:** `review_queue.md`-Meta-Prinzip-Kandidat „Asymmetrische Risikoverteilung im Buying Center" (engster bestehender Bezugspunkt); SD-SYS-001/A-0019; MEC-0006/MEC-0014-Fusionsfrage (`review_queue.md`, weiterhin offen — **nicht** Bestandteil dieses Themes, siehe Abschnitt 9); Aufgabe 6 dieses Sprints (MEC-0020 als mögliche, aber nicht zwingende Ergänzung zur Machtdynamik zwischen Buying-Center-Rollen, siehe Abschnitt 9.3); keine laufende `W-XXX`.

**Status:** Integrated (seit 2026-07-06 — W-004 vollständig durchlaufen, Editor Decision „Teilweise annehmen", Repository Integration und Health Check abgeschlossen).

**Herausgeber-Freigabe (2026-07-06):** Felix hat nach expliziter Rückfrage (score-gleiche Position mit RP-003, Abschnitt 6) die Aktivierung von RP-004 als reguläres Forschungsprojekt bestätigt, mit zwei ausdrücklichen Scope-Vorgaben, die von der ursprünglichen „Next Decision" unten abweichen: (1) Der Suchraum wird bereits ab Stufe 1 explizit um Social Identity Theory/Gruppendynamik-Forschung als potenziell **konkurrierende** (nicht nur ergänzende) theoretische Erklärung erweitert, statt dies erst nachgelagert als separate Entscheidung zu behandeln. (2) Der Meta-Prinzip-Kandidat „Asymmetrische Risikoverteilung" wird **nicht** als eigenständige Synthese-Aufgabe vorgezogen, sondern innerhalb von W-004 evidenzbasiert mitbewertet; eine eigenständige Wissensintegration wird erst nach Abschluss der Forschung entschieden. Projekt wird gemäß bestehendem Research Lifecycle bearbeitet; Ergebnisoffenheit ist verbindlich.

**Editor Decision und Integration (2026-07-06):** Felix hat W-004 mit „Editor Decision — W-004" **teilweise angenommen**: Buying-Center-Koalitionsliteratur (korrigierte Spekman & Stern 1979/McCabe 1987-Zuordnung) und ausgearbeiteter Agency-Theory-Pfad (Champion als Agent, Organisation als Prinzipal) in MEC-0014 integriert; Meta-Prinzip-Kandidat „Asymmetrische Risikoverteilung" **nicht** als eigenständiges Objekt angelegt (Begründung: nach aktuellem Evidenzstand keine hinreichend eigenständige zusätzliche Erklärungskraft — parsimonischer durch Agency Theory, Prospect Theory und die Koalitionsforschung erklärbar); Cross-Link Prospect Theory/MEC-0002 anstelle der abgelehnten Meta-Prinzip-Neuanlage ergänzt; beidseitiger Cross-Link MEC-0014 ↔ MEC-0030 (aus W-003) ergänzt, als offene, ungetestete Kopplung markiert; Social Identity Theory und Group Polarization mangels ausdrücklicher Freigabe nicht integriert; programmweites Muster additiver Syntheseempfehlungen (drittes Vorkommen nach W-002/W-003) als Programmebene-Beobachtung an Scientific Debt übergeben, nicht innerhalb von W-004 methodisch aufgelöst. Sieben offene Fragen (OQ-1 bis OQ-7) als Scientific Debt dokumentiert, kein automatisches Folgeprojekt. Vollständige Dokumentation: `06_research_program/completed/W004/06_EDITOR_DECISION.md`, `REPOSITORY_INTEGRATION_LOG.md`, `HEALTH_CHECK.md` (bestanden).

**Next Decision:** Keine unmittelbar anstehende Entscheidung zu diesem Theme. Etwaige künftige Vertiefung (z. B. SIT-Primärforschung OQ-6, Volltextprüfungen OQ-3/OQ-4/OQ-5, programmweites Muster OQ-7) setzt eine neue Portfolio- und Herausgeberentscheidung voraus (siehe `00_project/SCIENTIFIC_DEBT.md`, Sektion „W-004").

---

### RP-005 — Negotiation Science Calibration

**Research Theme:** Externe Validierung und Grenzbedingungs-Kalibrierung der neurowissenschaftlich begründeten Verhandlungsmechanismen (Voss/MEC-0010, MEC-0011) sowie Fairness-/Equity-Theorie als ergänzender normativer Rahmen für Verhandlungsobjektivität.

**Problem Definition:** Zwei zentrale Verhandlungsmechanismen (MEC-0010 Affect Labeling, MEC-0011 Mirroring/Spiegelneuronen) tragen seit Sprint 1 einen als Priorität Hoch eingestuften, bislang nicht abschließend bearbeiteten Validierungsbedarf. Zusätzlich fehlt eine mechanistische Fundierung für „objektive Kriterien" (MOD-0007, Getting to Yes) durch etablierte Fairness-/Equity-Theorie.

**Repository Evidence:** `SCIENTIFIC_DEBT.md`, B-0003-Sektion (MEC-0010, MEC-0011: „Externe Validierung ausstehend" und „Replikationsrisiko", durchgängig Priorität Hoch, unverändert seit 2026-06-30); `research_agenda.md`, F-002 (Tier 1: „Externe Validierung MEC-0010 und MEC-0011", empfohlener Sprint-2-Startpunkt — bis heute nicht als eigener Validierungssprint durchgeführt, siehe auch OD-005/OD-010) und F-006 (Tier 3: Langer-Xerox-Replikationsstatus, MEC-0001); MEC-0021, Abschnitt „Grenzen" (Boundary Condition Individual- vs. Organisationsebene, ED-005, als „offene Forschungsfrage, kein gesicherter Befund" markiert); MEC-0025, Abschnitt „Offene Fragen" (Interaktion mit MEC-0002, B2B-Wiederholungsgeschäft-Frage); `review_queue.md`, Abschnitt „MEC-Kandidat: Fairness / Equity Theory" (Adams 1965, Thibaut & Walker 1975 — für MOD-0007 vorausgesetzt, aber nicht mechanistisch fundiert).

**Strategic Relevance:** Der am längsten unbearbeitete Priorität-Hoch-Posten im gesamten Scientific-Debt-Bestand (seit B-0003, 2026-06-30) — betrifft zentrale, in mehreren Techniken (T-0012 bis T-0014) verwendete Mechanismen.

**Practical Leverage:** Mittel — betrifft primär die Konfidenz in bereits bestehende Techniken, nicht die Schaffung neuer Handlungsanweisungen.

**Integration Leverage:** Mittel — MEC-0010/0011-Familie plus deren abhängige T-Objekte; zusätzlich MEC-0021 (Grenzbedingung) und MEC-0025 (Grenzen) als Randanschluss (siehe Abschnitt 9.3 zur „Underused Scientific Capital"-Einordnung dieser beiden Objekte).

**Known Source Candidates:** Kein neuer externer Titel — dieses Theme ist primär ein **Validierungs-**, nicht ein Literaturerschließungs-Thema (Gemini-Validierung/Websuche zu bestehenden Zitationen, analog zum Vorgehen in `ACADEMIC_RECOVERY_REPORT*.md`). Ergänzend, falls freigegeben: Adams, J.S. (1965), *Inequity in Social Exchange*; Thibaut, J. & Walker, L. (1975), *Procedural Justice: A Psychological Analysis* (beide bereits in `review_queue.md`, kein Primärtextzugriff).

**Dependencies:** OD-010 (Validierungs-Governance — regelt, welches Instrument für diese Art von Prüfung künftig als hinreichend gilt; **dieses Theme kann sinnvollerweise erst nach einer OD-010-Entscheidung sauber priorisiert werden**, da sonst unklar bleibt, mit welchem Instrument validiert werden soll); Scientific Debt B-0003; research_agenda F-002/F-006; keine laufende `W-XXX`.

**Status:** Validated.

**Next Decision:** Felix entscheidet zunächst OD-010 (welches Validierungsinstrument/welche Kadenz gilt künftig als hinreichend); erst danach ist eine konkrete Beauftragung dieses Themes sinnvoll möglich.

---

### RP-006 — Principal-Agent Theory & Organisationale Mikropolitik

**Research Theme:** Formale Principal-Agent-Theorie (Eisenhardt 1989) als Rahmen für die bereits im Codex angedeutete, aber nicht durchgängig mechanistisch geführte Frage nach Interessenkonflikten zwischen individuellen Buying-Center-Akteuren und dem Organisationsinteresse.

**Problem Definition:** Die CEB-Loyalitätsdebatte (A-0019) und die Challenger/Gap-Selling-Diskussion um Risikoattribution setzen implizit Prinzipal-Agent-Dynamiken voraus, ohne dass ein eigenständiges, benanntes Objekt diese Theorie durchgängig nutzt.

**Repository Evidence:** `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 6 (GAP-04 als „plausible, im Codex nicht vertretene Domäne", Priorität „Mittel" — geringer als GAP-01/GAP-03); MEC-0014, Abschnitt „Ergänzende Theorie-Referenzen (ARS-0001)" (Eisenhardt 1989 bereits als Theorie-Referenz ohne Primärtext-Extraktion geführt); `OPEN_DECISIONS.md` OD-008 (thematische Nähe, aber nicht identisch — OD-008 benennt ELM/Trust/PKM, nicht explizit Principal-Agent-Theorie als eigenen Kandidaten).

**Strategic Relevance:** Mittel — reale, aber diffusere Lücke als RP-001/002/004, mit spürbarer inhaltlicher Überlappung zu RP-002 (Trust) und RP-004 (Buying Center).

**Practical Leverage:** Mittel — Umgang mit internem Political Capital, Anreizstrukturen von Einkäufern/Champions.

**Integration Leverage:** Mittel — hauptsächlich MEC-0014, A-0019.

**Known Source Candidates:** Eisenhardt, K.M. (1989). *Agency Theory: An Assessment and Review*. Academy of Management Review, 14(1), 57–74 (bereits websuchverifiziert und in MEC-0014 referenziert, `ACADEMIC_RECOVERY_REPORT.md`) — kein neuer, ungeprüfter Kandidat nötig, lediglich vertiefte Primärtext-Auswertung.

**Dependencies:** MEC-0014 (bereits vorhandene Theorie-Referenz); A-0019; deutliche thematische Nähe zu RP-002 und RP-004 — bei künftiger Priorisierung sollte geprüft werden, ob RP-006 als eigenständiges Theme bestehen bleibt oder als Teilaspekt in RP-004 aufgeht (bewusst hier nicht vorweggenommen); keine laufende `W-XXX`.

**Status:** Validated.

**Next Decision:** Felix entscheidet, ob RP-006 als eigenständiges Theme geführt oder mit RP-004 zusammengelegt wird, bevor eine Priorisierung sinnvoll ist.

---

### RP-007 — Ecological Rationality (Heuristiken als adaptive Werkzeuge)

**Research Theme:** Gigerenzers Programm der „Ecological Rationality" als akademisches Gegengewicht zur im Codex dominanten Heuristik-als-Bias-Perspektive (Kahneman/Tversky-Tradition).

**Problem Definition:** Der Codex modelliert Heuristiken durchgängig als Fehlerquellen (Anchoring, Verlustaversion als „Bias"). Die Gigerenzer-Tradition argumentiert, dass dieselben Heuristiken unter Unsicherheit adaptiv und leistungsfähig sein können — eine Gegenperspektive, die im Codex bislang nicht abgebildet ist.

**Repository Evidence:** `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 7 (Gigerenzer et al. 1999 als „Mittel-hoch" bewertet, „passt zur bereits im Codex dokumentierten Nudge/Boost-Kontroverse"); `SCIENTIFIC_DEBT.md`, SD-SYS-005 (Nudge-Wirksamkeits-Kontroverse, Mertens et al. 2021 vs. Maier/Szaszi et al. 2022) als thematisch verwandter, bereits dokumentierter Streitpunkt.

**Strategic Relevance:** Mittel — kein durch mehrere unabhängige Quellen konvergent bestätigter Bedarf wie bei RP-001–004, sondern eine einzelne, plausible externe Anregung.

**Practical Leverage:** Gering-mittel — eher kalibrierend/theoretisch als unmittelbar in neue Techniken übersetzbar.

**Integration Leverage:** Gering-mittel — primär MOD-0011 (Choice Architecture) und die SD-SYS-005-Debatte.

**Known Source Candidates:** Gigerenzer, G., Todd, P.M. & the ABC Research Group (1999). *Simple Heuristics That Make Us Smart*. Oxford University Press (durch Peer Review vorgeschlagen, **nicht verifiziert**).

**Dependencies:** SD-SYS-005; MOD-0011; keine laufende `W-XXX`.

**Status:** Candidate (Repository-Bezug vorhanden, aber schwächer konvergent bestätigt als die „Validated"-Themes oben).

**Next Decision:** Felix entscheidet, ob dieses Theme auf der Watchlist verbleibt oder — z. B. im Zusammenhang mit einer künftigen Neubewertung von SD-SYS-005 — zu einem eigenen Recherchebaustein aufgewertet wird.

---

### RP-008 — Change Motivation / Motivational Interviewing

**Research Theme:** Motivational Interviewing (Miller & Rollnick) als mögliche Quelle für Techniken im Umgang mit Kaufunentschlossenheit/Ambivalenz — mit explizitem Transferrisiko.

**Problem Definition:** Der Codex behandelt Kaufunentschlossenheit primär über JOLT/FOMU (B-0006) und Status-quo-Kosten (MEC-0002). Motivational Interviewing bietet eine klinisch etablierte, aber für einen kommerziellen Verkaufskontext nicht validierte Alternative zur Ambivalenzbearbeitung.

**Repository Evidence:** `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 7 (Miller & Rollnick 2012 als „Bedingt" bewertet: „Methode selbst exzellent belegt, aber B2B-Sales-Transfer ist eigenständige, unbewiesene Übersetzungsleistung; Risiko einer unkritischen Übernahme therapeutischer Begriffe — vom Report selbst benannt").

**Strategic Relevance:** Gering-mittel — einzige Quelle ist der Gemini-Report selbst; kein unabhängiger interner Beleg (Scientific Debt, Open Decision, Atlas) verlangt dieses Thema.

**Practical Leverage:** Potenziell mittel (Einwandbehandlung als „Change Talk" statt Konfrontation), aber mit explizit dokumentiertem Missbrauchs-/Fehltransferrisiko.

**Integration Leverage:** Gering — aktuell keine belastbare Verbindung zu bestehenden Objekten außer einer losen thematischen Nähe zu MEC-0003 (Reaktanz).

**Known Source Candidates:** Miller, W.R. & Rollnick, S. (2012). *Motivational Interviewing: Helping People Change*. Guilford Press (durch Peer Review als „Beobachtungskandidat" markiert, **nicht verifiziert**).

**Dependencies:** Keine bestehende Open Decision, kein Scientific-Debt-Eintrag, kein Atlas-Befund — ausschließlich der Gemini-Report/Peer-Review-Eintrag selbst; keine laufende `W-XXX`.

**Status:** Candidate — ausdrücklich als reiner **Beobachtungskandidat** geführt, nicht als validierte Lücke (entsprechend der Auftragsvorgabe „ggf. Motivational Interviewing als Beobachtungskandidat").

**Next Decision:** Kein aktiver Handlungsbedarf. Beobachten, ob sich in künftigen Sprints ein unabhängiger zweiter Beleg für diese Lücke ergibt, bevor eine Aufwertung zu „Validated" erwogen wird.

---

## 8. Watchlist

RP-007 (Ecological Rationality) und RP-008 (Motivational Interviewing) — vollständige Begründung siehe Theme Cards oben. Beide sind `Candidate`, nicht `Validated`: Sie stützen sich im Wesentlichen auf eine einzelne externe Quelle (Gemini-Report/Peer Review) ohne unabhängige interne Konvergenz (kein Scientific-Debt-Eintrag, keine Open Decision, kein Atlas-Befund, kein Research-Agenda-Punkt). Sie werden nicht verworfen, weil die zugrunde liegende akademische Substanz real ist — sie werden nicht priorisiert, weil der Repository-Bezug (noch) schwächer ist als bei den sechs anderen Themes.

---

## 9. Excluded / Redundant Candidates

**9.1 — Persuasion Knowledge Model (Friestad & Wright 1994).** Nicht als eigenes Theme geführt. Bereits in `review_queue.md` als Fall dokumentiert, in dem eine „eigenständiges MEC … derzeit primär theoretische Doppelung ohne neue Statement-Basis" wäre — eine kleine Zitat-Ergänzung existiert bereits in MEC-0003. Wird als thematisch verwandter, aber untergeordneter Baustein unter RP-001 (Persuasion Architecture) geführt, nicht als eigenes Theme.

**9.2 — Choice Architecture / Default Effects als „fehlender" MEC-Kandidat.** In `review_queue.md` (Stand 2026-07-01, vor B-0013) noch als offener Kandidat geführt. Durch die vollständige Buchanalyse von *Nudge: The Final Edition* (B-0013, 2026-07-02) und die Canonicalisierung von MOD-0011 ist dieser Bedarf bereits erledigt — `review_queue.md` selbst wurde nach B-0013 an dieser Stelle nicht mehr aktualisiert (siehe Initialization Report, Abschnitt 4, für die vollständige Dokumentation dieser Inkonsistenz). Kein neues Theme; die verbleibende offene Frage (Publication-Bias-Kontroverse um die Nudge-Gesamtwirksamkeit) ist bereits als SD-SYS-005 in `SCIENTIFIC_DEBT.md` geführt, nicht Gegenstand dieses Portfolios.

**9.3 — MEC-0020, MEC-0021, MEC-0025 als gemeinsames „Underused Science"-Thema.** Der Gemini-Report ordnet diesen drei Objekten fälschlich die Themen „Cognitive Load", „Affective Forecasting/Anticipated Regret" bzw. „Psychological Reactance" zu (`SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 5, Befund 1 — durch direkte Einsicht der drei Objekte in diesem Sprint erneut bestätigt: MEC-0020 = Perspektivübernahme-Asymmetrie durch Macht, MEC-0021 = Anchoring, MEC-0025 = Altruistische Bestrafung). Nach Prüfung der tatsächlichen Objektinhalte (Aufgabe 6 dieses Sprints):

- Die drei Mechanismen haben **grundverschiedene kausale Strukturen** (Macht→Eigenzentrierung; Zahlen-Priming/Adjustment; sozial-normative Empörungsreaktion) — ein gemeinsames neues MEC oder eine gemeinsame Forschungsfrage wäre wissenschaftlich nicht gerechtfertigt (dieselbe Prüfmethodik, mit der MEC-0025 selbst seine Abgrenzung zu MEC-0002/MEC-0009 begründet, schließt eine Fusion der drei Objekte aus).
- Drei getrennte neue Forschungsprojekte sind ebenfalls nicht gerechtfertigt: Alle drei Mechanismen sind bereits mit hoher bis höchster Evidenzklasse (E4, E5, E4) im Repository verankert. Es fehlt keine externe Literatur — es fehlt die Ableitung nachgelagerter Prinzipien/Techniken aus bereits vorhandener, guter Evidenz.
- **Ergebnis:** Dies ist primär eine **Synthese-/Operationalisierungsaufgabe**, kein neues Forschungsprogramm. Sie ist bereits in `KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, Abschnitt 10/11 (dort ausdrücklich als „Synthesis Priority", nicht „Research Priority", eingestuft) sowie in `KNOWLEDGE_ATLAS_GOVERNANCE.md`, Abschnitt 5 (Schritt 7: Kanalzuständigkeit Buchanalyse/Synthese, nicht Research Program) dokumentiert. Kein eigenes RP-Theme wird dafür angelegt.
- Die inhaltliche Substanz der drei Mechanismen ist **nicht verloren**: MEC-0020 (Machtdynamik) ist als möglicher, nicht zwingender Anschlusspunkt bei RP-004 (Buying Center) vermerkt; MEC-0021 (Boundary Condition Individual/Organisation) und MEC-0025 (B2B-Wiederholungsgeschäft-Frage) sind bei RP-005 (Negotiation Calibration) vermerkt. Beide Verweise sind Randanschlüsse, keine Kernbestandteile dieser Themes — eine Aufwertung müsste eigenständig geprüft werden.

**9.4 — Implementation Intentions / Intent-Behavior Gap.** In keiner der geprüften Quellen (Gemini-Report/Peer Review, `OPEN_DECISIONS.md`, `SCIENTIFIC_DEBT.md`, `KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, `research_agenda.md`, `review_queue.md`) findet sich ein Beleg für diesen in der Aufgabenstellung genannten Kandidaten. Gemäß der Grundregel „Erfinde niemals Quellen oder Fakten" wird für dieses Thema **keine Theme Card** erstellt — eine nachträgliche Konstruktion einer Begründung ohne Repository-Beleg wäre selbst eine Verletzung der Sprintvorgabe. Sollte ein künftiger Sprint eine reale Repository-Verankerung finden (z. B. im Kontext von Commitment-Techniken, T-0036, oder Save-More-Tomorrow-artigen Commitment-Mechanismen in MEC-0002), kann dieses Thema erneut geprüft werden.

**9.5 — MEC-0006/MEC-0014-Fusionsfrage.** Bereits als eigenständige, seit Sprint 1 unentschiedene Canonicalisierungsfrage in `review_queue.md` dokumentiert (zweifach durch Herausgeber abgelehnt für sofortige Fusion — Sprint 1 und ARS-0001). Dies ist keine Forschungslücke im Sinne von Leitprinzip 1 dieses Sprints, sondern eine reine Canonicalisierungs-/Governance-Frage. Nicht Bestandteil dieses Portfolios.

**9.6 — Sechs Fußnoten-Referenzen des Gemini-Reports.** Vollständig verworfen gemäß `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 5, Befund 2 (thematisch unpassende Websuchtreffer ohne Fachbezug). Keine Aufnahme in dieses Portfolio.

**9.7 — „Autonomy in the Workplace" (Deci & Ryan, 2008) und „Relational Capital Theory"-Etikettierung.** Beide von Peer Review als nicht abschließend verifizierbar bzw. ungenau etikettiert markiert (Abschnitt 5, Befund 3/4). Nicht als eigenständige Themes geführt; „Autonomy"-Frage bleibt bei Bedarf ein Prüfpunkt innerhalb von RP-008, nicht eigenständig.

---

## 10. First Investment Recommendation

**Empfohlenes Theme: RP-001 — Persuasion Architecture (Elaboration Likelihood Model).**

**Warum dieses Theme:** RP-001 erzielt den höchsten Orientierungsscore (4,40) bei gleichzeitig dem niedrigsten Forschungsaufwand (Research Cost 2) unter den vier Top-Kandidaten. Es ist die einzige Empfehlung, die durch **drei unabhängige Signale** konvergent gestützt wird: eine seit 2026-07-01 bestehende, nie geschlossene interne Top-Priorität (OD-008), eine identische Einstufung im unabhängig geführten `review_queue.md`, und eine externe Bestätigung durch die Peer-Review-Begutachtung des Gemini-Reports (die diese Priorität ausdrücklich nicht sich selbst, sondern der bereits bestehenden OD-008 zuschreibt — ein Fall editorischer Redlichkeit, der die Glaubwürdigkeit der Empfehlung zusätzlich stützt).

**Erwarteter Grenznutzen:** Hoch. ELM liefert kein isoliertes neues Wissensobjekt, sondern ein theoretisches Dach, das die Interpretierbarkeit von mindestens neun bestehenden Objekten verbessert (MEC-0005–0009, MEC-0012, MEC-0018, MOD-0002, MOD-0008) — insbesondere durch eine mögliche theoretische Erklärung für den bislang nur strukturell (nicht inhaltlich) verstandenen MEC-0018-Befund des Knowledge Atlas.

**Anschlussfähigkeit:** Sehr hoch. Es entsteht kein neues Forschungsprogramm „aus dem Nichts" — die Aufnahme von Petty & Cacioppo (1986) ist bereits in `LITERATURE_INDEX.md` als Zeile mit Status „Nicht angelegt — höchste Priorität" vorbereitet. Der nächste Schritt ist eine Literatur-/Primärtext-Beschaffung, kein neuer Governance-Prozess.

**Aufwand:** Niedrig bis mittel. Kein vollständiger Buchanalyse-Prozess (SRC→ST→A→MEC→P→T→MOD) ist zwingend erforderlich — je nach Editor-Entscheidung genügt ggf. eine literaturbasierte Recherche-Ergänzung analog zum bereits etablierten Academic-Recovery-Verfahren, bevor über eine vollständige Objekt-Neuanlage entschieden wird.

**Zuständige Governance-Stelle:** `00_project/OPEN_DECISIONS.md`, OD-008 — die bereits bestehende, entscheidungsreife Open Decision. Kein neues Governance-Instrument erforderlich. Die formale Freigabe eines Recherche- oder Buchanalyse-Bausteins bleibt an die Eröffnung eines künftigen Version-1.1-Programms gebunden (`NEXT_ACTION.md`).

**Ausdrücklicher Vorbehalt:** Dies ist eine Empfehlung an den Herausgeber, keine Freigabe. Kein Research Sprint, keine Literaturaufnahme und keine Objekt-Neuanlage wird durch dieses Dokument automatisch ausgelöst.

---

## 11. Governance Notes and Limits

- Dieses Dokument trifft **keine** Herausgeberentscheidung, eröffnet **kein** `W-XXX`-Projekt, ändert **kein** bestehendes Wissensobjekt und keine bestehende Governance-Datei.
- Alle acht Themes tragen ausschließlich die Status `Validated` oder `Candidate`. Kein Theme trägt `Prioritized`, `Active Research`, `Integrated`, `Closed` oder `Rejected` — diese Statusübergänge sind ausschließlich Herausgeber- bzw. spätere Lifecycle-Ereignisse (Abschnitt 4).
- Die in Abschnitt 6 berechneten Scores sind eine Entscheidungshilfe. Der Portfolio Architect hat bei eng beieinanderliegenden Werten (RP-001/003/004/002) zusätzlich bestehende Governance-Signale (OD-008) herangezogen — dies ist transparent dokumentiert (Abschnitt 6, Hinweis zur Rangfolge), nicht verschleiert.
- Etwaige Inkonsistenzen im bestehenden Repository-Zustand (z. B. `review_queue.md`, das nach B-0013 nicht mehr aktualisiert wurde, siehe Abschnitt 9.2) wurden ausschließlich dokumentiert, nicht korrigiert — gemäß Sprintvorgabe „Nicht korrigieren".
- Die nächste inhaltliche Aktualisierung dieses Portfolios sollte erfolgen, sobald (a) der Herausgeber eine OD-008-Entscheidung trifft, (b) ein Version-1.1-Programm formal eröffnet wird, oder (c) ein neuer Content-Analysis-Zyklus des Knowledge Atlas neue Structure-×-Evidence-Befunde liefert (`KNOWLEDGE_ATLAS_GOVERNANCE.md`, Abschnitt 2).
- Format- und Strukturänderungen an diesem Dokument (Abschnittsreihenfolge, Statusvokabular, Scoring-Gewichte) sind, analog zu anderen Governance-Dokumenten des Research Program, nur durch Felix vorzunehmen.

---

*Dieses Dokument ist eine Steuerungs- und Priorisierungsebene, kein Wissensobjekt und keine Framework-Datei. Es trifft keine inhaltliche Bewertung einzelner Wissensobjekte über das hinaus, was bereits in den referenzierten Dateien dokumentiert ist. Vollständiger Methodenbericht: `00_project/RESEARCH_PORTFOLIO_INITIALIZATION_REPORT.md`.*
