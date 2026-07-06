# Research Portfolio Initialization Report

**Dokumentklasse:** Archived (einmaliger Sprint-Report nach Abschluss — nicht Teil des laufenden Operational-Sets)
**Rolle bei Erstellung:** Research Portfolio Architect (Claude), im Auftrag des Herausgebers — Konsolidierung, Architektur, Priorisierungsvorschlag. Kein Forscher, kein Framework-Architekt, keine Herausgeberentscheidung.
**Datum:** 2026-07-05
**Auslöser:** Herausgeberauftrag „Research Portfolio Initialization Sprint"
**Ergebnisdatei:** `06_research_program/RESEARCH_PORTFOLIO.md`

---

## 1. Scope

Aufgabe dieses Sprints war ausschließlich Architektur, Konsolidierung und Priorisierung — keine neue Forschung, keine Websuche, keine Literaturverifikation, keine neue wissenschaftliche Synthese, keine neuen Wissensobjekte (MEC/P/T/MOD/ST/A), keine Änderung bestehender Wissensobjekte, keine Framework-Änderung. Der Sprint überführt bereits dokumentierte Forschungsbedarfe in eine neue, zusätzliche Steuerungsebene (`06_research_program/RESEARCH_PORTFOLIO.md`) oberhalb des bestehenden Research Program, ohne bestehende Systeme zu duplizieren oder zu verändern.

Explizit ausgeschlossen und in diesem Sprint auch nicht vorgenommen: Änderungen an Wissensobjekten, Framework-Dateien, Buchanalysen, dem Knowledge Atlas, `SCIENTIFIC_DEBT.md`, `OPEN_DECISIONS.md`, `LITERATURE_INDEX.md`, `research_agenda.md` oder an Version 1.0.

---

## 2. Sources Reviewed

**Vollständig gelesen:**

- `PROJECT_BOOTSTRAP.md`
- `CURRENT_STATE.md` (vollständig, zwei Leseabschnitte wegen Dateilänge)
- `00_project/NEXT_ACTION.md`
- `00_project/OPEN_DECISIONS.md` (vollständig, OD-001 bis OD-012)
- `00_project/SCIENTIFIC_DEBT.md` (vollständig, zwei Leseabschnitte wegen Dateilänge — B-0001 bis B-0015 sowie die systemischen SD-SYS- und ARS-0001-Sektionen)
- `00_project/SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md` (vollständig)
- `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md` (vollständig, zwei Leseabschnitte wegen Dateilänge)
- `00_project/KNOWLEDGE_ATLAS_GOVERNANCE.md` (vollständig)
- `05_research/LITERATURE_INDEX.md` (Abschnitte A, B, C vollständig gelesen — größter Teil der Datei; Abschnitte D ff., falls vorhanden, wurden aufgrund der bereits erreichten inhaltlichen Sättigung für die Fragestellung dieses Sprints nicht zusätzlich gelesen, siehe Abschnitt 3 „Konsolidierungsmethode")
- `04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md` (vollständig)
- `00_project/review_queue.md` (vollständig)
- `06_research_program/RESEARCH_GOVERNANCE.md`, `RESEARCH_STATUS.md`, `README.md` (vollständig)
- `06_research_program/completed/W001/06_EDITOR_DECISION.md`, `OPEN_QUESTIONS.md` (vollständig)
- `06_research_program/templates/RESEARCH_PROJECT_TEMPLATE.md` (zur Stilreferenz)
- `TASK_TYPES.md` (zur Selbsteinordnung dieses Sprints, siehe unten)
- `LANGUAGE_POLICY.md` (Sprachregeln)
- Direkte Objekteinsicht: `03_knowledge_base/mechanisms/MEC-0020_perspektivuebernahme_asymmetrie_macht.md`, `MEC-0021_anchoring_mechanismus.md`, `MEC-0025_fairness_verzicht_ultimatum.md` (Pflichtprüfung gemäß Aufgabe 6 des Sprintauftrags)

**Nicht direkt gelesen (bewusst, gemäß Sprintvorgabe):** Der Gemini-Report selbst (`Sales Codex Forschungsstrategie Review.md`) wurde nicht erneut direkt eingesehen — die Sprintvorgabe verlangt ausdrücklich, den Gemini-Report nur indirekt über den bereits vorliegenden Peer-Review-Bericht zu nutzen, außer zur Nachprüfung eines konkreten Einzelpunkts. Ein solcher Nachprüfungsbedarf ergab sich nicht, da der Peer-Review-Bericht die relevanten Gemini-Aussagen (insbesondere die Objektzuordnungen zu MEC-0020/0021/0025 und die Literaturempfehlungen) bereits wörtlich zitiert und einzeln bewertet.

**Task-Type-Einordnung dieses Sprints:** Kein exakter Treffer in `TASK_TYPES.md`. Am ehesten eine Mischung aus T4 (Architekturarbeit — Struktur-/Priorisierungsvorschlag, keine Ausführung einer Forschungsentscheidung) und T8 (Governance — Konsolidierung bestehender Entscheidungsgrundlagen), jedoch ohne exakte Passung zu einem der zwölf definierten Typen. Diese Erweiterung ist durch den vorliegenden, expliziten Herausgeberauftrag selbst angefordert.

---

## 3. Consolidation Method

**Schritt 1 — Longlist (intern, nicht als eigenes Artefakt gespeichert):** Aus allen unter Abschnitt 2 genannten Quellen wurden alle expliziten Forschungsbedarfe extrahiert: Open Decisions mit Forschungsbezug (OD-005, OD-008, OD-010, OD-011), alle Scientific-Debt-Kategorien „Externe Validierung ausstehend"/„Offene Forschungsfrage"/„Replikationsrisiko" mit Priorität Hoch oder Mittel, alle noch nicht bearbeiteten research_agenda-Punkte (F-002 bis F-012, F-001 bereits durch W-001 erledigt), alle Atlas-Sprint-1-Befunde aus Abschnitt 10/11 (Underused Strengths, Synthesis Priority Map), alle in `review_queue.md` dokumentierten Literatur- und Meta-Prinzip-Kandidaten, sowie die durch den Peer-Review-Bericht als „übernehmen" oder „später prüfen" eingestuften Gemini-Empfehlungen.

**Schritt 2 — Dubletten zusammenführen:** ELM erschien identisch in OD-008, `LITERATURE_INDEX.md`, `review_queue.md` und im Peer-Review-Bericht — als ein Theme (RP-001) geführt, nicht viermal. Trust Formation erschien identisch in OD-008, `review_queue.md` und im Peer-Review-Bericht — ein Theme (RP-002). Cognitive Load erschien in research_agenda F-009, `SCIENTIFIC_DEBT.md` B-0005 und im Peer-Review-Bericht (GAP-03) — ein Theme (RP-003).

**Schritt 3 — Erledigte Themen entfernt:** F-001 (W-001, Teach First vs. Diagnose First) wurde nicht erneut als Theme geführt — durch Editor Decision vom 2026-07-03 bereits vollständig durch den Research-Program-Lifecycle gelaufen und integriert. Die „Choice Architecture/Default Effects"-Lücke aus `review_queue.md` (Stand 2026-07-01) wurde als durch B-0013 (2026-07-02) bereits geschlossen identifiziert und nicht als Theme aufgenommen (siehe Abschnitt 4).

**Schritt 4 — Rein redaktionelle Aufgaben entfernt:** Die MEC-0006/MEC-0014-Fusionsfrage (`review_queue.md`) wurde nicht als Research Theme geführt — es handelt sich um eine Canonicalisierungs-/Governance-Frage (bereits zweimal vom Herausgeber gegen sofortige Fusion entschieden), keine wissenschaftliche Lücke im Sinne von Leitprinzip 1 des Sprintauftrags.

**Schritt 5 — Quellenkandidaten übergeordneten Themes zugeordnet:** Einzelne Literaturtitel (Petty & Cacioppo 1986, Mayer/Davis/Schoorman 1995, Palmatier et al. 2006, Sweller et al. 2011, Eisenhardt 1989, Gigerenzer et al. 1999, Miller & Rollnick 2012, Adams 1965, Thibaut & Walker 1975) wurden nicht als eigene Portfolioeinheiten geführt, sondern als „Known Source Candidates" innerhalb der jeweiligen Theme Card (gemäß Leitprinzip 1: „Research Themes statt Bücher").

**Schritt 6 — Verdichtung auf 6–10 Themes:** Ergebnis: acht Themes (RP-001 bis RP-008), siehe Abschnitt 5.

---

## 4. Duplicate and Redundancy Findings

| Befund | Betroffene Dateien | Einordnung |
|---|---|---|
| ELM als Literaturkandidat wird in vier unabhängigen Dokumenten identisch geführt (OD-008, `LITERATURE_INDEX.md`, `review_queue.md`, Peer-Review-Bericht) | s. o. | Keine Inkonsistenz — vierfache Konvergenz stärkt die Priorisierung von RP-001, statt ein Redundanzproblem darzustellen. Als ein Theme geführt. |
| Trust Formation analog dreifach konvergent (OD-008, `review_queue.md`, Peer-Review-Bericht) | s. o. | Wie oben — als ein Theme (RP-002) geführt. |
| „Choice Architecture / Default Effects"-Kandidat in `review_queue.md` ist **veraltet** — die dort beschriebene Lücke wurde durch die vollständige Verarbeitung von B-0013 (Nudge: The Final Edition, 2026-07-02, MOD-0011) bereits geschlossen. `review_queue.md` wurde an dieser Stelle nach B-0013 nicht aktualisiert. | `00_project/review_queue.md`, Abschnitt „Neue Literaturkandidaten aus Research Pack 2, 3, 4" | **Inkonsistenz identifiziert, gemäß Sprintvorgabe nur dokumentiert, nicht korrigiert.** Im Portfolio als Excluded/Redundant (Abschnitt 9.2 des Portfolios) vermerkt, `review_queue.md` selbst bleibt unverändert. |
| MEC-0020/MEC-0021/MEC-0025 werden vom Gemini-Report als gemeinsames „Underused Science"-Thema mit inhaltlich falschen Objektzuordnungen behauptet. | `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md`, Abschnitt 5; direkte Objekteinsicht in diesem Sprint | **Falschbehauptung bestätigt** (dritte, unabhängige Bestätigung nach Peer-Review-Bericht selbst). Kein gemeinsames Theme angelegt — siehe Abschnitt 6 dieses Berichts und Abschnitt 9.3 des Portfolios. |
| research_agenda.md, F-001 wird in mehreren Folgedokumenten (SESSION_LOG, Scientific Debt) als erledigt referenziert, steht aber in `research_agenda.md` selbst noch als offener Tier-1-Punkt. | `04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md` vs. `CURRENT_STATE.md`, `06_research_program/completed/W001/` | Keine Korrektur in `research_agenda.md` vorgenommen (außerhalb des Scopes — Datei ist in der Sperrliste dieses Sprints). Im Portfolio korrekt als „bereits erledigt" behandelt (F-001 taucht in keinem Theme als offener Bedarf auf), aber die Diskrepanz selbst wird hier dokumentiert, da sie eine Repository-Inkonsistenz ist. |

---

## 5. Themes Created

Acht Themes, `RP-001` bis `RP-008`:

| ID | Titel | Einordnung im Portfolio |
|---|---|---|
| RP-001 | Persuasion Architecture (Elaboration Likelihood Model) | Top Priority |
| RP-002 | Trust Formation & Relationship Marketing | Top Priority |
| RP-003 | Cognitive Load & Decision Complexity | Secondary Priority |
| RP-004 | Buying Center Social Dynamics & Organisationale Risikoverteilung | Top Priority |
| RP-005 | Negotiation Science Calibration | Secondary Priority |
| RP-006 | Principal-Agent Theory & Organisationale Mikropolitik | Secondary Priority |
| RP-007 | Ecological Rationality (Heuristiken als adaptive Werkzeuge) | Watchlist |
| RP-008 | Change Motivation / Motivational Interviewing | Watchlist |

Von den zehn in der Aufgabenstellung als mögliche Kandidaten genannten Themen wurden acht in modifizierter Form übernommen; zwei wurden bewusst nicht als eigenständige Themes angelegt:

- **„Underused Scientific Capital"** wurde nach Prüfung nicht als eigenständiges Theme geführt (siehe Abschnitt 6 dieses Berichts) — stattdessen als Randanschluss in RP-004 (MEC-0020) und RP-005 (MEC-0021, MEC-0025) dokumentiert.
- **„Implementation Intentions / Intent-Behavior Gap"** wurde mangels jeglichen Repository-Belegs nicht als Theme angelegt (siehe Portfolio, Abschnitt 9.4).

---

## 6. Gemini / Peer Review Handling

Gemäß Sprintvorgabe wurde der Gemini-Report ausschließlich indirekt über `SCIENTIFIC_PEER_REVIEW_GEMINI_RESEARCH_STRATEGY.md` verwertet. Der Peer-Review-Bericht hatte in jedem Punkt Vorrang vor unverifizierten Gemini-Behauptungen.

**Übernommen (gemäß Peer-Review-Empfehlung „übernehmen"):**
- Palmatier, Dant, Grewal & Evans (2006) als ergänzender Literaturkandidat zu RP-002 (Trust Formation) — **nicht** websuchverifiziert in diesem Sprint (außerhalb des Scopes: keine Websuche), als „noch nicht verifiziert" gekennzeichnet.
- Petty & Cacioppo (1986) / ELM als Bestätigung der bereits bestehenden OD-008-Priorität, ausdrücklich **nicht** dem Gemini-Report zugeschrieben, sondern als externe Zweitbestätigung einer bereits vor dem Gemini-Report bestehenden internen Priorität behandelt.
- Cognitive Load (GAP-03) als reale Lücke übernommen (RP-003) — jedoch mit einer **neu formulierten** Begründung, da die im Gemini-Report gegebene Herleitung über eine falsche MEC-0020-Zuordnung erfolgte (siehe unten).
- Buying Center Social Dynamics (GAP-01) als reale, wenn auch leicht überzeichnete Lücke übernommen (RP-004).
- Gigerenzer et al. (1999) als Watchlist-Kandidat (RP-007) übernommen, mit reduzierter Priorität gegenüber den vier Kern-Themes.
- Motivational Interviewing als reiner Beobachtungskandidat (RP-008) übernommen, exakt wie in der Sprintvorgabe („ggf. … als Beobachtungskandidat") formuliert — nicht als validierte Lücke.

**Nicht übernommen (gemäß expliziter Sprintvorgabe und/oder Peer-Review-Befund):**
- Die falsche MEC-0020-Zuordnung („Cognitive Load & Information Overload") — durch direkte Objekteinsicht in diesem Sprint ein drittes Mal bestätigt als falsch. MEC-0020 behandelt Perspektivübernahme-Asymmetrie durch Macht, nicht Cognitive Load.
- Die falsche MEC-0021-Zuordnung („Affective Forecasting & Anticipated Regret") — durch direkte Objekteinsicht bestätigt als falsch. MEC-0021 behandelt Anchoring.
- Die falsche MEC-0025-Zuordnung („Psychological Reactance & Autonomy-Supportive Communication") — durch direkte Objekteinsicht bestätigt als falsch. MEC-0025 behandelt Altruistische Bestrafung/Ultimatum-Spiel-Fairness; Reaktanz ist bereits eigenständig als MEC-0003 im Codex vorhanden.
- Die vollständige Referenzliste des Gemini-Reports (sechs thematisch unpassende Fußnoten) — gemäß Peer-Review-Befund 2 vollständig verworfen, keine Aufnahme in das Portfolio.
- Unbestätigte bibliografische Angaben („Autonomy in the Workplace", Deci & Ryan 2008; „Relational Capital Theory"-Etikettierung von Palmatier) — nicht als eigenständige Themes, nur als Randvermerk (Portfolio, Abschnitt 9.7).
- Themen, die bereits nachweislich ausreichend abgedeckt sind (Choice Architecture/Default Effects, s. Abschnitt 4) — nicht übernommen.
- Pauschale Abwertungen bestehender Frameworks (Gemini-Executive-Summary „fast ausschließlich … Ratgeberliteratur") — nicht übernommen; der Peer-Review-Bericht selbst widerlegt dies bereits anhand von `LITERATURE_INDEX.md` (Abschnitt 4, Overstatement 1).

---

## 7. Prioritization Result

Scoring-Methodik: fünf Dimensionen (Scientific Gap 30 %, Strategic Relevance 25 %, Practical Leverage 20 %, Integration Leverage 15 %, Research Cost 10 % invers), Skala 1–5 je Dimension, siehe `RESEARCH_PORTFOLIO.md` Abschnitt 5 für die vollständige Formel.

| ID | Score | Einordnung |
|---|---|---|
| RP-001 | 4,40 | Top Priority |
| RP-003 | 4,05 | Secondary Priority (trotz zweithöchstem Score — Begründung unten) |
| RP-004 | 4,05 | Top Priority |
| RP-002 | 3,95 | Top Priority (trotz niedrigerem Score als RP-003/004 — Begründung unten) |
| RP-005 | 3,35 | Secondary Priority |
| RP-006 | 3,00 | Secondary Priority |
| RP-007 | 2,35 | Watchlist |
| RP-008 | 2,20 | Watchlist |

**Warum die Top-3-Auswahl nicht rein den höchsten drei Rohwerten folgt:** Die vier Spitzenwerte liegen mit 3,95 bis 4,40 in einem engen Band, das keine belastbare mechanische Rangfolge erlaubt. Zusätzlich zum Score wurde berücksichtigt, dass RP-001 und RP-002 beide bereits **vor diesem Sprint** durch eine bestehende, entscheidungsreife Herausgeber-Governance-Struktur (OD-008, Rang 1 und Rang 2) explizit priorisiert sind — ein stärkeres, bereits formal etabliertes Signal als der in diesem Sprint neu berechnete Score. RP-004 wurde trotz eines nominal identischen Scores zu RP-003 als Top Priority statt RP-003 gewählt, da RP-004 (a) mehr bereits vorhandene Repository-Infrastruktur nutzt (Meta-Prinzip-Kandidat in `review_queue.md`, Atlas-Community-7-Befund, SD-SYS-001/A-0019), und (b) die im Reifegradbericht dokumentierte schwächste Einzeldimension des Codex (B2B-Generalisierbarkeit, C+) direkt adressiert. Diese Abwägung ist transparent im Portfolio (Abschnitt 6, „Hinweis zur Rangfolge") dokumentiert, nicht verdeckt.

---

## 8. First Investment Recommendation

**RP-001 — Persuasion Architecture (Elaboration Likelihood Model).**

Vollständige Begründung (erwarteter Grenznutzen, Anschlussfähigkeit, Aufwand, zuständige Governance-Stelle): `RESEARCH_PORTFOLIO.md`, Abschnitt 10. Kurzfassung: höchster Score bei niedrigstem Aufwand unter den Top-Kandidaten, dreifach unabhängig konvergent bestätigt (OD-008, `review_queue.md`, Peer-Review-Bericht), unmittelbar an eine bereits bestehende, entscheidungsreife Open Decision (OD-008) andockbar — kein neues Governance-Instrument erforderlich.

**Ausdrücklicher Vorbehalt (wiederholt aus dem Portfolio):** Dies ist eine Empfehlung an den Herausgeber. Kein Research Sprint wird durch dieses Dokument automatisch ausgelöst.

---

## 9. Files Changed

Zwei neue Dateien angelegt, keine bestehende Datei verändert:

1. `06_research_program/RESEARCH_PORTFOLIO.md` (neu)
2. `00_project/RESEARCH_PORTFOLIO_INITIALIZATION_REPORT.md` (neu, dieses Dokument)

---

## 10. Explicitly Not Changed

Gemäß Sprintvorgabe wurden folgende Dateien und Bereiche ausschließlich gelesen, nicht verändert — auch nicht dort, wo dieser Bericht Inkonsistenzen dokumentiert (Abschnitt 4):

- Bestehende Wissensobjekte (`03_knowledge_base/` — inkl. MEC-0020, MEC-0021, MEC-0025, die für Aufgabe 6 direkt eingesehen, aber nicht editiert wurden)
- Framework-Dateien (`01_framework/`)
- Buchanalysen (`04_book_analysis/`)
- Der Knowledge Atlas (`08_knowledge_atlas/`) und seine Governance (`KNOWLEDGE_ATLAS_GOVERNANCE.md`)
- `00_project/SCIENTIFIC_DEBT.md`
- `00_project/OPEN_DECISIONS.md` (insbesondere OD-008, OD-010 — beide bleiben unverändert offen)
- `05_research/LITERATURE_INDEX.md`
- `04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md`
- `00_project/review_queue.md` (trotz der in Abschnitt 4 dokumentierten Veralterung an einer Stelle)
- `06_research_program/RESEARCH_GOVERNANCE.md`, `RESEARCH_STATUS.md`, `DECISION_POLICY.md`, `RESEARCH_LIFECYCLE.md`, `REPOSITORY_INTEGRATION.md`, `templates/`
- `06_research_program/completed/W001/` (vollständig, einschließlich aller neun Lifecycle-Dokumente)
- Version 1.0 im Gesamten (`99_archive/v1.0_release/`)
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md` — dieser Sprint ist kein regulärer Entwicklungssprint für Version 1.1 und aktualisiert daher nicht den Session-Abschluss-Dreiklang aus `PROJECT_BOOTSTRAP.md`, Abschnitt „Pflichtabschluss jeder Session". Sollte der Herausgeber wünschen, dass dieser Sprint dort vermerkt wird, ist dies ein separater, expliziter Folgeauftrag.

---

*Dieser Bericht ist ein generierter Sprintabschluss-Output, kein Wissensobjekt und keine Framework-Datei. Er ersetzt keine Herausgeberentscheidung.*
