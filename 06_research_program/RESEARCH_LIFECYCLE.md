# Research Lifecycle

Version: RC-1
Stand: 2026-07-03
Geltungsbereich: Alle Forschungsprojekte (`W-XXX`) ab RC-1
Grundlage: `RESEARCH_PROGRAM_REVIEW_RC1.md`, Kapitel 3 (Referenzmodell: Research Question → Theory Assessment → Research → Peer Review → Editor Decision → Repository Integration → Health Check) und Kapitel 8, Empfehlungen 1, 3, 4

---

## 1. Zweck dieses Dokuments

Dieses Dokument beschreibt den vollständigen Forschungsprozess von der ersten offenen Frage bis zur geprüften Integration in den Sales Codex — analog zum Operating Manual für Buchanalysen, aber für Forschungsprojekte.

Es löst zwei konkrete Befunde der Architekturprüfung (`RESEARCH_PROGRAM_REVIEW_RC1.md`) auf:

**Erstens** fehlte eine benannte "Research Question"-Stufe vollständig (Kapitel 3, Zeile "Research Question"). Ab RC-1 ist sie Stufe 1 jedes neuen Forschungsprojekts.

**Zweitens** war die Reihenfolge zwischen "Theory Assessment" und "Research" unklar (Kapitel 3, Zeile "Theory Assessment"; Kapitel 8, Blocker 8). Diese Unklarheit wird hier explizit aufgelöst: Das im Sprintauftrag vorgegebene Referenzmodell (`RESEARCH_PROGRAM_REVIEW_RC1.md`, Kapitel 3, erster Absatz) definiert die Reihenfolge *Research Question → Theory Assessment → Research → Peer Review*. Für W-001 lag die Theory-Landscape-Stufe jedoch faktisch **nach** den beiden Reviews (siehe `active/W001/README.md` für die Begründung, warum dies bei W-001 nicht rückwirkend geändert wird). Für **alle künftigen Projekte** gilt ab RC-1 verbindlich die neun Stufen dieses Dokuments, in dieser Reihenfolge — mit der Theory Landscape als konsolidierende Stufe **nach** Master Review und Peer Review (Begründung: Abschnitt 3, Stufe 5). Dies ist eine bewusste Governance-Entscheidung dieses Sprints, keine unkommentierte Fortschreibung des W-001-Musters — beide Lesarten wurden geprüft (Abschnitt 3, Stufe 5, "Abgrenzung").

## 2. Stufenübersicht

| # | Stufe | Datei (Konvention) | Verantwortliche Rolle |
|---|---|---|---|
| 1 | Research Question | `00_RESEARCH_QUESTION.md` | Research Lead |
| 2 | Initial Hypothesis | `01_INITIAL_HYPOTHESIS.md` | Research Lead |
| 3 | Master Review (Research) | `02_..._MASTER_REVIEW.md` | Scientific Reviewer |
| 4 | Peer Review | `03_..._RED_TEAM_REVIEW.md` | Peer / Red Team Reviewer |
| 5 | Theory Landscape | `04_THEORY_LANDSCAPE.md` | Scientific Reviewer oder Research Lead |
| 6 | Decision Brief | `05_DECISION_BRIEF.md` | Research Lead |
| 7 | Editor Decision | `06_EDITOR_DECISION.md` | Herausgeber (Felix) |
| 8 | Repository Integration | `REPOSITORY_INTEGRATION_LOG.md` | Research Lead |
| 9 | Health Check | `HEALTH_CHECK.md` | Research Lead |

Rollendefinitionen: `RESEARCH_GOVERNANCE.md`, Abschnitt 4. Templates für jede Stufe: `templates/`.

---

## 3. Stufe 1 — Research Question

**Ziel:** Die zu klärende Frage explizit, präzise und unabhängig von einer bereits feststehenden Antwort formulieren — bevor irgendeine Hypothese aufgestellt wird.

**Eingaben:** Der Anlass (z. B. ein dokumentierter Widerspruch aus `contradiction_matrix.md`, `OPEN_DECISIONS.md` oder `00_project/SCIENTIFIC_DEBT.md`); relevante bestehende Wissensobjekte (P-/MEC-/A-IDs), die die Frage berühren.

**Ergebnisse:** `00_RESEARCH_QUESTION.md`, ausgefüllt nach `01_framework/08_templates/research_question_template.md` (bestehendes Framework-Template — siehe Abschnitt 7, "Verhältnis zum Hauptframework"). Enthält mindestens: die Frage selbst, warum sie relevant ist, betroffene Prinzipien/Modelle, benötigte Quellen, eine vorläufige (noch nicht ausgearbeitete) Hypothese.

**Qualitätskriterien:** Die Frage ist so formuliert, dass sie durch Forschung tatsächlich beantwortbar ist (nicht rhetorisch, nicht bereits durch bestehende Codex-Prinzipien beantwortet). Der Anlass ist mit einer konkreten Repository-Referenz belegt, nicht nur behauptet.

**Übergabekriterien (an Stufe 2):** Die Frage ist so präzise, dass eine erste, noch ungeprüfte Hypothese formulierbar ist. Der Herausgeber hat die Aufnahme eines neuen `W-XXX`-Projekts bestätigt (`RESEARCH_GOVERNANCE.md`, Abschnitt 4.1).

**Verantwortliche Rolle:** Research Lead.

---

## 4. Stufe 2 — Initial Hypothesis

**Ziel:** Eine erste, konkrete, prüfbare Ausgangshypothese formulieren, die auf die Research Question antwortet.

**Eingaben:** `00_RESEARCH_QUESTION.md`.

**Ergebnisse:** `01_INITIAL_HYPOTHESIS.md`, ausgefüllt nach `templates/INITIAL_HYPOTHESIS_TEMPLATE.md`.

**Qualitätskriterien:** Die Hypothese ist falsifizierbar (Falsifizierungsbedingung explizit benannt, analog zur Anforderung an Annahmen im `canonical_knowledge_model.md`, Abschnitt 3.2). Sie ist von der Research Question klar unterscheidbar (Frage ≠ vorweggenommene Antwort).

**Übergabekriterien (an Stufe 3):** Die Hypothese ist konkret genug, dass ein Scientific Reviewer sie systematisch gegen Alternativhypothesen prüfen kann.

**Verantwortliche Rolle:** Research Lead.

---

## 5. Stufe 3 — Master Review (Research)

**Ziel:** Die eigentliche Forschungsleistung: systematische Bewertung der Ausgangshypothese und konkurrierender Alternativhypothesen anhand wissenschaftlicher Gütekriterien (Erklärungskraft, Parsimonie, Plausibilität, Falsifizierbarkeit, Anschlussfähigkeit an Standardtheorien).

**Eingaben:** `01_INITIAL_HYPOTHESIS.md`; vorhandene Literatur und Quellen (dokumentiert am Ende des Reviews, konsolidiert später in `REFERENCES.md`).

**Ergebnisse:** `02_..._MASTER_REVIEW.md`, ausgefüllt nach `templates/MASTER_REVIEW_TEMPLATE.md`. Enthält mindestens: Executive Summary, systematische Bewertung jeder geprüften Hypothese, Vergleichstabelle, Beantwortung der ursprünglichen Research Question, nummerierte Quellenverweise mit Referenzliste.

**Qualitätskriterien:** Jede geprüfte Hypothese wird anhand derselben Kriterien bewertet (Vergleichbarkeit). Stärken und Schwächen werden für jede Hypothese benannt, nicht nur für die am Ende favorisierte. Für jede zentrale Behauptung ist gekennzeichnet, ob belastbare Evidenz existiert oder nicht (analog zur im Repository etablierten Praxis, siehe `active/W001/02_SCIENTIFIC_MASTER_REVIEW.md`, wiederkehrende Formulierung "keine belastbare Evidenz bekannt").

**Übergabekriterien (an Stufe 4):** Der Master Review liegt vollständig vor und beansprucht kein Ergebnis als bereits entschieden — die Bewertung bleibt einer unabhängigen Gegenprüfung zugänglich (keine Formulierung, die eine Peer Review vorwegnimmt oder für überflüssig erklärt).

**Verantwortliche Rolle:** Scientific Reviewer.

---

## 6. Stufe 4 — Peer Review (Red Team Review)

**Ziel:** Kritische, unabhängige Gegenprüfung des Master Review — insbesondere der favorisierten Hypothese/Synthese — anhand derselben oder strengerer wissenschaftlicher Gütekriterien.

**Eingaben:** `02_..._MASTER_REVIEW.md`.

**Ergebnisse:** `03_..._RED_TEAM_REVIEW.md`, ausgefüllt nach `templates/RED_TEAM_TEMPLATE.md`. Enthält mindestens: eine benannte Anzahl von Prüfkriterien (siehe Template), je Kriterium eine explizite Einordnung (erfüllt / teilweise erfüllt / nicht erfüllt), ein wissenschaftliches Endurteil, eine klare Empfehlung (Annehmen / Ablehnen / Überarbeiten).

**Qualitätskriterien:** Der Peer Reviewer ist nicht identisch mit dem Scientific Reviewer aus Stufe 3 (`RESEARCH_GOVERNANCE.md`, Abschnitt 4.4 — einzige harte Rollentrennungsregel des Programms). Jedes Prüfkriterium wird einzeln begründet, nicht pauschal. Ein negatives Gesamturteil darf nicht vermieden werden, nur weil Stufe 3 bereits viel Arbeit investiert hat — die Review-Stufe ist die dafür vorgesehene Kontrollinstanz (siehe `RESEARCH_PROGRAM_REVIEW_RC1.md`, Executive Summary, "Größte Stärken").

**Übergabekriterien (an Stufe 5):** Ein explizites Endurteil liegt vor, unabhängig davon, ob es dem Master Review widerspricht. Ein Widerspruch zwischen Stufe 3 und Stufe 4 ist **kein** Abbruchgrund (siehe `RESEARCH_GOVERNANCE.md`, Abschnitt 7) — er wird unverändert an Stufe 5 weitergereicht.

**Verantwortliche Rolle:** Peer / Red Team Reviewer.

---

## 7. Stufe 5 — Theory Landscape

**Ziel:** Die Ergebnisse aus Master Review (Stufe 3) und Peer Review (Stufe 4) — insbesondere wenn sie widersprechen — gegen die breitere Landschaft bestehender Theorien und Modelle einordnen und konsolidieren. Diese Stufe beantwortet nicht "wer hat recht", sondern "wo stehen beide Befunde im Verhältnis zu etablierten Theoriefeldern, und was folgt daraus für eine Entscheidung".

**Abgrenzung (Reihenfolge-Entscheidung):** Diese Stufe könnte alternativ *vor* Stufe 3 als reine Scoping-Übung stehen (so das im Sprintauftrag zitierte allgemeine Referenzmodell). Für das Research Program wird sie stattdessen bewusst **nach** den beiden Reviews positioniert, aus zwei Gründen: Erstens leistet der Master Review (Stufe 3) bereits selbst einen wesentlichen Teil der Scoping-Arbeit (systematischer Vergleich konkurrierender Hypothesen inklusive ihrer Anschlussfähigkeit an Standardtheorien — siehe `active/W001/02_SCIENTIFIC_MASTER_REVIEW.md`, Abschnitt "Anschlussfähigkeit an wissenschaftliche Disziplinen"). Eine vorgelagerte, separate Scoping-Stufe würde diese Arbeit doppeln. Zweitens entsteht der eigentliche Bedarf für eine Theorielandschaft-Einordnung erst dann, wenn ein Widerspruch zwischen zwei Reviews vorliegt, der eingeordnet werden muss (wie bei W-001) — vorher ist unklar, wogegen überhaupt eingeordnet werden müsste. Diese Entscheidung gilt ab RC-1 für alle neuen Projekte; W-001 selbst wird nicht rückwirkend umstrukturiert (siehe `active/W001/README.md`).

**Eingaben:** `02_..._MASTER_REVIEW.md`, `03_..._RED_TEAM_REVIEW.md`.

**Ergebnisse:** `04_THEORY_LANDSCAPE.md`, ausgefüllt nach `templates/THEORY_LANDSCAPE_TEMPLATE.md`. Enthält mindestens: eine Gegenüberstellung der zentralen Streitpunkte zwischen Stufe 3 und Stufe 4, eine Einordnung in bestehende Theoriefelder außerhalb der bereits geprüften Hypothesen, eine Einschätzung, welche offenen Fragen durch weitere Forschung (statt durch Herausgeber-Ermessen) klärbar wären.

**Qualitätskriterien:** Kein Streitpunkt aus Stufe 3/4 wird stillschweigend fallengelassen. Jede Einordnung benennt, ob sie auf zusätzlicher externer Theorie beruht oder eine reine Neugewichtung der bereits vorliegenden Argumente ist.

**Übergabekriterien (an Stufe 6):** Alle Streitpunkte zwischen Master Review und Peer Review sind entweder eingeordnet oder explizit als "durch Theory Landscape nicht auflösbar, gehört in die Editor Decision" markiert.

**Verantwortliche Rolle:** Scientific Reviewer (bevorzugt, wegen fachlicher Kontinuität zu Stufe 3) oder Research Lead, falls der Scientific Reviewer nicht verfügbar ist.

---

## 8. Stufe 6 — Decision Brief

**Ziel:** Die Stufen 1–5 für den Herausgeber zu einer knappen, handlungsfähigen Entscheidungsgrundlage verdichten.

**Eingaben:** Alle bisherigen Projektdokumente (`00`–`04`).

**Ergebnisse:** `05_DECISION_BRIEF.md`, ausgefüllt nach `templates/DECISION_BRIEF_TEMPLATE.md`. Enthält mindestens: Zusammenfassung der Research Question und des Ergebnisses, die zentralen Streitpunkte aus Stufe 5, eine begründete Empfehlung (nicht bindend — die Entscheidung bleibt beim Herausgeber), eine Tabelle möglicher Integrationsoptionen mit voraussichtlichem Objekttyp.

**Qualitätskriterien:** Der Decision Brief fügt keine neuen inhaltlichen Argumente hinzu, die nicht bereits in Stufe 3–5 belegt sind (reine Verdichtung, keine neue Forschung). Die Empfehlung ist als Empfehlung gekennzeichnet, nicht als Vorwegnahme der Entscheidung.

**Übergabekriterien (an Stufe 7):** Der Brief ist so verfasst, dass der Herausgeber ausschließlich auf seiner Basis (ohne Rückgriff auf die Volltexte der Stufen 3–5) eine informierte Entscheidung treffen kann.

**Verantwortliche Rolle:** Research Lead.

---

## 9. Stufe 7 — Editor Decision

**Ziel:** Verbindliche Herausgeberentscheidung über Annahme, teilweise Annahme, Zurückstellung oder Ablehnung.

**Eingaben:** `05_DECISION_BRIEF.md` (und bei Bedarf die Volltexte der Stufen 3–5).

**Ergebnisse:** `06_EDITOR_DECISION.md`, ausgefüllt nach `templates/EDITOR_DECISION_TEMPLATE.md`. Kriterien für die Entscheidung selbst: `DECISION_POLICY.md`.

**Qualitätskriterien:** Siehe `DECISION_POLICY.md`, Abschnitt 3.

**Übergabekriterien (an Stufe 8):** Bei "Annehmen"/"Teilweise annehmen" liegt die in `DECISION_POLICY.md`, Abschnitt 5 geforderte Tabelle "Geplante Integration" vor. Bei "Ablehnen" endet der Prozess hier (→ `RESEARCH_GOVERNANCE.md`, Abschnitt 6.3, Archivierung). Bei "Zurückstellen" kehrt das Projekt zur benannten Stufe zurück.

**Verantwortliche Rolle:** Herausgeber (Felix).

---

## 10. Stufe 8 — Repository Integration

**Ziel:** Das angenommene Ergebnis tatsächlich als Wissensobjekt(e) im Sales Codex anlegen.

**Eingaben:** `06_EDITOR_DECISION.md` mit positiver Entscheidung und ausgefüllter Integrationstabelle.

**Ergebnisse:** Neue oder erweiterte Wissensobjekte in `03_knowledge_base/` gemäß bestehendem Objekttyp (ST/A/MEC/P/T/MOD); `REPOSITORY_INTEGRATION_LOG.md` im Projektordner, das jede vorgenommene Integrationsaktion mit ID, Objekttyp, Aktion (NEU/ERWEITERT) und Dateipfad protokolliert.

**Qualitätskriterien und Ablauf:** Vollständig beschrieben in `REPOSITORY_INTEGRATION.md`. Kurzfassung: Es gilt exakt dieselbe Identitäts- und Entscheidungslogik wie bei jeder Buchanalyse (`canonical_knowledge_model.md`, Abschnitt 4) — keine Sonderregeln für Research-Program-Ergebnisse.

**Übergabekriterien (an Stufe 9):** Alle in der Editor Decision zugesagten Integrationsschritte sind entweder durchgeführt oder mit Begründung als nicht durchführbar dokumentiert (z. B. Zusammenführungskandidat, der laut `canonical_knowledge_model.md` Abschnitt 4.3 eine gesonderte Herausgeber-Entscheidung erfordert und noch aussteht).

**Verantwortliche Rolle:** Research Lead.

---

## 11. Stufe 9 — Health Check

**Ziel, Umfang, Prüfkriterien, Abschlussbedingungen:** Vollständig beschrieben in Abschnitt 12 dieses Dokuments (eigener Abschnitt wegen des Umfangs, siehe Sprintauftrag Phase 5).

**Verantwortliche Rolle:** Research Lead.

---

## 12. Health Check — Details

### 12.1 Zweck

Sicherstellen, dass ein abgeschlossenes Forschungsprojekt — unabhängig vom Ausgang (angenommen oder abgelehnt) — keine strukturellen Schäden im Repository hinterlassen hat, dass alle Governance-Anforderungen dieses Dokuments und von `RESEARCH_GOVERNANCE.md` tatsächlich erfüllt wurden, und dass der Übergang nach `completed/` bzw. `archived/` auf einer geprüften, nicht nur behaupteten Grundlage steht.

Der Health Check ist **projektspezifisch** (eine Prüfung pro `W-XXX`-Projekt) und damit klar abgegrenzt von der in `00_project/OPEN_DECISIONS.md`, OD-003 dokumentierten, weiterhin offenen Frage eines *repositoryweiten* Health-Check-Protokolls (Prüfung des gesamten Repositorys, nicht eines einzelnen Forschungsprojekts). Dieses Dokument löst OD-003 nicht — beide Ebenen bleiben unabhängig voneinander bestehen. Ein künftiger repositoryweiter Health Check (falls per OD-003 eingeführt) und der hier definierte projektspezifische Health Check schließen sich nicht aus; letzterer kann als Baustein des ersteren dienen, ist aber eigenständig nutzbar.

### 12.2 Umfang

Der Health Check prüft ausschließlich:

1. Die Vollständigkeit der Projektdokumentation selbst (Stufen 1–8 des jeweiligen Projekts).
2. Bei angenommenen Ergebnissen: die technische und inhaltliche Konsistenz der in Stufe 8 integrierten Wissensobjekte.
3. Die Konsistenz der programmweiten Statusdokumente (`RESEARCH_STATUS.md`) mit dem tatsächlichen Projektzustand.

Er prüft **nicht** den Zustand des übrigen Repositorys außerhalb der durch dieses Projekt berührten Dateien (das wäre Gegenstand eines repositoryweiten Health Checks, s. o.).

### 12.3 Prüfkriterien

| # | Prüfpunkt | Bedingung für "erfüllt" |
|---|---|---|
| 1 | Vollständigkeit der Stufendokumente | Alle Dateien der Stufen 1–7 existieren und enthalten mehr als eine Titelzeile (kein Stub). |
| 2 | Konsistenz Editor Decision ↔ Integration | Jede in der Editor-Decision-Tabelle "Geplante Integration" zugesagte Aktion ist im `REPOSITORY_INTEGRATION_LOG.md` mit Ergebnis (durchgeführt / begründet nicht durchgeführt) wiederzufinden. |
| 3 | Objekt-Referenzintegrität (nur bei Integration) | Jedes neu angelegte oder erweiterte Wissensobjekt ist unter einer gültigen, bislang nicht vergebenen ID (bzw. korrekt erweiterten bestehenden ID) auffindbar; keine doppelten IDs entstanden. |
| 4 | Evidenzklassen begründet (nur bei Integration) | Jedes integrierte Objekt trägt eine Evidenzklasse mit nachvollziehbarer Begründung gemäß `evidence_system.md`. |
| 5 | Herkunftsverweis vorhanden (nur bei Integration) | Jedes integrierte Objekt referenziert im Feld "Source ID" (bzw. gleichwertigem Herkunftsfeld) die Projekt-ID (`W-XXX`) gemäß `REPOSITORY_INTEGRATION.md`, Abschnitt 3. |
| 6 | Keine neuen toten Pfadverweise | Repositoryweite Stichprobe auf Backtick-Pfadverweise, die durch dieses Projekt neu entstanden sind, zeigt keine ungültigen Pfade. |
| 7 | `RESEARCH_STATUS.md` aktuell | Der Statuseintrag des Projekts entspricht dem tatsächlichen Stufenstand zum Prüfzeitpunkt. |
| 8 | `RESEARCH_LOG.md` lückenlos | Jeder Stufenübergang des Projekts ist im Log chronologisch nachvollziehbar, ohne Sprünge ohne Erklärung. |
| 9 | `OPEN_QUESTIONS.md` abgearbeitet oder übergeben | Jede dort verzeichnete offene Frage ist entweder beantwortet (mit Verweis) oder explizit an ein Nachfolgeprojekt bzw. `00_project/SCIENTIFIC_DEBT.md` übergeben. |

### 12.4 Abschlussbedingungen

Der Health Check gilt als **bestanden**, wenn jeder Prüfpunkt aus Abschnitt 12.3 entweder mit "erfüllt" oder — soweit auf das Projekt nicht anwendbar (z. B. Prüfpunkte 3–5 bei einem abgelehnten Projekt ohne Integration) — mit "nicht anwendbar" bewertet ist.

Jeder Prüfpunkt, der weder "erfüllt" noch "nicht anwendbar" ist, muss vor dem Übergang nach `completed/` bzw. `archived/` entweder behoben oder als bewusst akzeptierte Restlücke dokumentiert werden — mit Begründung, im `HEALTH_CHECK.md` des Projekts UND als Eintrag in `RESEARCH_LOG.md`. Eine unbehobene, unbegründete Lücke blockiert den Ordnerübergang (siehe `RESEARCH_GOVERNANCE.md`, Abschnitt 7, letzte Zeile).

Der ausgefüllte Health-Check-Bericht wird nach `templates/HEALTH_CHECK_TEMPLATE.md` erstellt und verbleibt dauerhaft im Projektordner (auch nach Verschiebung nach `completed/`/`archived/`).

---

## 13. Verhältnis zum Hauptframework

Die Stufe 1 (Research Question) verwendet bewusst das bereits bestehende `01_framework/08_templates/research_question_template.md` statt eines neuen, Research-Program-spezifischen Templates — es adressiert exakt dieselbe Frage (Research Question mit ID, Frage, Relevanz, betroffene Prinzipien, benötigte Quellen, vorläufige Hypothese, Status) und wird bereits an anderer Stelle im Repository verwendet (`04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md`). Eine Neuerfindung dieses Templates innerhalb von `06_research_program/templates/` würde eine unnötige Dopplung schaffen. Alle übrigen acht Stufen verwenden Research-Program-spezifische Templates, da für sie im Hauptframework keine Entsprechung existiert.

---

*Dieses Dokument gilt ab RC-1 (2026-07-03). Änderungen nur durch Felix.*
