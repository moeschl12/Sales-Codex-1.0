# Research Governance

Version: RC-1
Stand: 2026-07-03
Geltungsbereich: Alle Forschungsprojekte (`W-XXX`) in `06_research_program/`
Grundlage: `RESEARCH_PROGRAM_REVIEW_RC1.md` (Architekturprüfung, 2026-07-02), Empfehlungen 1–6
Autorität: Dieses Dokument gilt ab RC-1. Änderungen nur durch Felix.

---

## 1. Zweck des Research Programs

Der Sales Codex trifft laufend Aussagen, die sich nicht allein durch die Standard-Buchanalyse (`00_project/SALES_CODEX_OPERATING_MANUAL.md`) klären lassen — insbesondere dann, wenn mehrere bereits verarbeitete Quellen einander widersprechen (Beispiel: der seit Sprint 1 ungelöste Widerspruch *Teach First* vs. *Diagnose First*, dokumentiert in `contradiction_matrix.md` und `OPEN_DECISIONS.md`).

Das Research Program ist der dafür vorgesehene, vom regulären Buchanalyse-Workflow **getrennte** Prozess: eine begrenzte Anzahl offener, benannter Forschungsfragen wird hier systematisch bearbeitet — durch Hypothesenbildung, wissenschaftliche Prüfung, kritisches Gegengutachten und eine bewusste Herausgeber-Entscheidung — bevor (und nur wenn) ein Ergebnis in den Sales Codex überführt wird.

Das Research Program ersetzt nicht das Evidenzsystem (`01_framework/02_evidence_system/evidence_system.md`) oder das Canonical Knowledge Model (`01_framework/05_knowledge_model/canonical_knowledge_model.md`). Es ist ein vorgelagerter Klärungsprozess für Fälle, die diese beiden Instrumente allein nicht auflösen — sein Ergebnis muss am Ende trotzdem durch dieselben Identitäts- und Evidenzregeln, wie jedes andere Wissensobjekt auch.

## 2. Geltungsbereich

Dieses Dokument und alle übrigen programmweiten Dateien in `06_research_program/` (`README.md`, `DECISION_POLICY.md`, `RESEARCH_STATUS.md`, `RESEARCH_LIFECYCLE.md`, `REPOSITORY_INTEGRATION.md`, `templates/`) gelten für **jedes** Forschungsprojekt, unabhängig von Thema oder beteiligtem KI-System — aktuell `active/W001/`, sowie jedes künftige `W-XXX`.

Sie gelten **nicht** für:

- Buchanalysen (`04_book_analysis/`) — dafür gilt das Operating Manual.
- Synthese-Sprints (`04_synthesis/`) — eigener, bereits etablierter Prozess.
- Einzelne Validierungsaufträge außerhalb eines benannten Forschungsprojekts (z. B. Ad-hoc-Gemini-Prüfungen einzelner MEC-Objekte) — dafür gilt Kapitel 6 des Operating Manual (Review-Prozess).

Grenzfälle (z. B. eine Recherche, die sich im Verlauf zu einem vollwertigen Forschungsprojekt auswächst) werden durch den Herausgeber entschieden, nicht durch Cowork eigenständig eingestuft.

## 3. Verhältnis zum Sales Codex

Forschung ist strikt vom offiziellen Sales Codex getrennt (siehe `README.md`). Kein Inhalt aus einem laufenden Forschungsprojekt gilt als Bestandteil des Codex, solange keine positive Editor Decision (`DECISION_POLICY.md`) vorliegt und die Repository Integration (`REPOSITORY_INTEGRATION.md`) nicht abgeschlossen ist.

Dies gilt unabhängig vom Umfang oder der wissenschaftlichen Qualität eines Zwischendokuments — auch ein 330-zeiliges, gut referenziertes Gutachten (z. B. `active/W001/02_SCIENTIFIC_MASTER_REVIEW.md`) ist bis zur Editor Decision ausschließlich Forschungsmaterial, kein Codex-Wissen.

## 4. Rollen

Das Research Program übernimmt das im Operating Manual (Kapitel 2) etablierte Rollenmodell und passt es an die spezifischen Stufen des Forschungsprozesses an. Rollen sind funktional definiert, nicht werkzeuggebunden — jede Rolle kann von unterschiedlichen KI-Systemen wahrgenommen werden, solange die Unabhängigkeitsanforderung in Abschnitt 4.3 eingehalten wird.

### 4.1 Herausgeber (Felix)

Letztentscheidungsinstanz. Zuständig für:

- Freigabe jedes Forschungsprojekts bei Aufnahme (neues `W-XXX` anlegen)
- Die Editor Decision (Stufe 7, `06_EDITOR_DECISION.md`) — einzige Instanz mit Integrationsvollmacht (siehe `DECISION_POLICY.md`)
- Eskalationsentscheidungen bei Abbruchbedingungen (Abschnitt 7)
- Entscheidungen über Statusübergänge, die laut `RESEARCH_LIFECYCLE.md` dem Herausgeber vorbehalten sind (z. B. `active` → `archived` bei Ablehnung)
- Klärung von Zusammenführungs- oder Abgrenzungsfragen zwischen Forschungsprojekten

Der Herausgeber ist nicht der Produzent der Forschungsinhalte. Er ist der Entscheider — analog zur Rollentrennung im Operating Manual Kapitel 2.

### 4.2 Research Lead (Claude / Cowork)

Zuständig für:

- Formulierung der Research Question und der Initial Hypothesis (Stufen 1–2)
- Projektkoordination: Anlage des `W-XXX`-Ordners nach Template, Pflege von `README.md`, `OPEN_QUESTIONS.md`, `REFERENCES.md`, `RESEARCH_LOG.md`
- Fortlaufende Aktualisierung des Projekteintrags in `RESEARCH_STATUS.md`
- Erstellung des Decision Brief (Stufe 6) auf Basis von Master Review und Peer Review
- Durchführung der Repository Integration nach positiver Editor Decision (Stufe 8), gemäß `REPOSITORY_INTEGRATION.md`
- Durchführung des Health Check (Stufe 9)

Der Research Lead arbeitet ausschließlich auf Basis des Repositories. Eigene Erinnerung ist keine Quelle der Wahrheit (Grundregel des Projekts).

### 4.3 Scientific Reviewer

Erstellt den Master Review (Stufe 3, `02_..._MASTER_REVIEW.md`): systematische Bewertung konkurrierender Hypothesen, ggf. Synthese zu einer neuen Theorie. Entspricht funktional der Rolle "ChatGPT — Scientific & Systems Editor" aus dem Operating Manual Kapitel 2, ist aber nicht auf ein bestimmtes System festgelegt.

### 4.4 Peer / Red Team Reviewer

Erstellt die kritische Gegenprüfung (Stufe 4, `03_..._RED_TEAM_REVIEW.md`). **Unabhängigkeitsanforderung:** Der Red Team Reviewer darf nicht dieselbe Instanz/Session sein, die den Master Review (Stufe 3) erstellt hat. Dies ist die einzige harte Prozessregel zur Rollentrennung im Research Program — sie sichert das in der Review (`RESEARCH_PROGRAM_REVIEW_RC1.md`, Executive Summary) als "methodisch wertvoll" hervorgehobene Kontrollprinzip: kein unwidersprochenes Gutachten mündet direkt in eine Entscheidung.

Für W-001 wurde diese Rolle durch Gemini wahrgenommen (siehe Dateiname `03_GEMINI_RED_TEAM_REVIEW.md`); künftige Projekte benennen die Rolle im Dateinamen nach dem tatsächlich eingesetzten System oder generisch als `03_RED_TEAM_REVIEW.md`, wenn das System wechselt oder unerheblich ist.

### 4.5 Wissenschaftliche Validierung (optional, projektabhängig)

Bei Aufnahme eines Ergebnisses mit Anspruch auf Evidenzklasse E3 oder höher (siehe `01_framework/02_evidence_system/evidence_system.md`) kann zusätzlich die im Operating Manual Kapitel 2 definierte Rolle "Gemini — Wissenschaftliche Validierung" herangezogen werden. Diese Prüfung ist nicht je Forschungsprojekt verpflichtend, wird aber empfohlen, wenn die Editor Decision eine Integration mit hoher Evidenzklasse vorsieht (siehe `DECISION_POLICY.md`, Abschnitt 3).

### 4.6 Verantwortlichkeits-Übersicht

| Stufe | Dokument | Verantwortliche Rolle |
|---|---|---|
| 1 — Research Question | `00_RESEARCH_QUESTION.md` | Research Lead |
| 2 — Initial Hypothesis | `01_INITIAL_HYPOTHESIS.md` | Research Lead |
| 3 — Master Review (Research) | `02_..._MASTER_REVIEW.md` | Scientific Reviewer |
| 4 — Peer Review | `03_..._RED_TEAM_REVIEW.md` | Peer / Red Team Reviewer (unabhängig von Stufe 3) |
| 5 — Theory Landscape | `04_THEORY_LANDSCAPE.md` | Scientific Reviewer oder Research Lead (siehe `RESEARCH_LIFECYCLE.md`, Stufe 5) |
| 6 — Decision Brief | `05_DECISION_BRIEF.md` | Research Lead |
| 7 — Editor Decision | `06_EDITOR_DECISION.md` | Herausgeber (Felix) |
| 8 — Repository Integration | `REPOSITORY_INTEGRATION_LOG.md` | Research Lead, nach Freigabe |
| 9 — Health Check | `HEALTH_CHECK.md` | Research Lead |

Details zu Zielen, Eingaben, Ergebnissen, Qualitäts- und Übergabekriterien jeder Stufe: `RESEARCH_LIFECYCLE.md`.

## 5. Statusdefinitionen

Jedes Forschungsprojekt trägt in `RESEARCH_STATUS.md` genau einen der folgenden Status:

| Status | Bedeutung |
|---|---|
| `ACTIVE (Stufe N)` | Projekt in Bearbeitung, aktuelle Stufe gemäß Abschnitt 4.6 in Klammern angegeben |
| `ON_HOLD` | Projekt pausiert (z. B. wartet auf externe Ressource oder Herausgeber-Priorisierung); Grund wird in `RESEARCH_LOG.md` dokumentiert |
| `AWAITING_EDITOR_DECISION` | Decision Brief liegt vor, Projekt wartet auf Stufe 7 |
| `INTEGRATING` | Editor Decision positiv, Repository Integration (Stufe 8) läuft |
| `HEALTH_CHECK` | Integration abgeschlossen, Health Check (Stufe 9) läuft |
| `COMPLETED` | Health Check bestanden, Projekt nach `completed/` verschoben |
| `ARCHIVED` | Projekt eingestellt oder abgelehnt, nach `archived/` verschoben |

Diese Statuswerte sind die einzigen gültigen Werte für das Feld "Status" in `RESEARCH_STATUS.md` und in jedem `README.md` eines `W-XXX`-Projekts.

## 6. Lifecycle und Ordnerübergänge

### 6.1 Kurzüberblick

Der vollständige Prozess (9 Stufen, Research Question bis Health Check) ist in `RESEARCH_LIFECYCLE.md` beschrieben. Dieses Kapitel regelt ausschließlich die **Ordnerübergänge** zwischen `active/`, `completed/` und `archived/`.

### 6.2 `active/` → `completed/`

**Bedingung:** Editor Decision positiv (vollständig oder teilweise angenommen) **und** Repository Integration abgeschlossen **und** Health Check bestanden (siehe `RESEARCH_LIFECYCLE.md`, Stufe 9).

**Vorgehen:** Der gesamte Projektordner (`W-XXX/`) wird unverändert von `active/` nach `completed/` verschoben. Kein Dateiinhalt wird bei der Verschiebung verändert. `RESEARCH_STATUS.md` wird auf `COMPLETED` gesetzt, mit Datum und Verweis auf den Health-Check-Bericht.

**Entscheidungsinstanz:** Research Lead vollzieht die Verschiebung; sie ist kein eigenständiger Ermessensspielraum, sondern die mechanische Folge einer bereits getroffenen Editor Decision plus bestandenem Health Check.

### 6.3 `active/` → `archived/`

**Bedingung:** Editor Decision negativ (vollständige Ablehnung) **oder** Herausgeber stellt das Projekt aus anderen Gründen ein (z. B. Überholung durch ein neueres Projekt, dauerhafte Nichtverfügbarkeit einer benötigten Ressource).

**Vorgehen:** Der Projektordner wird unverändert verschoben. `RESEARCH_STATUS.md` wird auf `ARCHIVED` gesetzt, mit Begründung und Datum. Die Editor Decision (oder eine kurze Einstellungsbegründung des Herausgebers, falls keine Editor Decision vorliegt) bleibt im Ordner erhalten — nichts wird gelöscht.

**Entscheidungsinstanz:** Ausschließlich Herausgeber.

### 6.4 `completed/` → `archived/`

**Bedingung:** Ein bereits integriertes Forschungsergebnis wird später durch ein neueres Forschungsprojekt widerlegt oder überholt (z. B. eine spätere Editor Decision revidiert eine frühere).

**Vorgehen:** Der überholte Projektordner wird nach `archived/` verschoben, mit einem ergänzenden Vermerk (neue Datei `SUPERSEDED_BY.md` im Projektordner oder Eintrag in `RESEARCH_LOG.md`), der auf das überholende Projekt verweist. Bereits integrierte Wissensobjekte werden **nicht** automatisch zurückgenommen — das ist eine separate Herausgeber-Entscheidung gemäß `canonical_knowledge_model.md` (Abstieg der Evidenzklasse, Dokumentation des Widerspruchs, kein Löschen).

**Entscheidungsinstanz:** Ausschließlich Herausgeber.

### 6.5 Was niemals passiert

Kein Forschungsprojekt-Ordner wird gelöscht. Kein Dateiinhalt eines abgeschlossenen oder archivierten Projekts wird nachträglich verändert, außer durch die in Abschnitt 6.4 beschriebene ergänzende Verweisdatei. Dies entspricht dem repositoryweiten Grundsatz "Dokumentiere Widersprüche, statt sie zu glätten" (`CONTRIBUTING.md`, Grundregel 8).

## 7. Abbruchbedingungen

Folgende Zustände führen zu einem Arbeitsstopp und Eskalation an den Herausgeber — analog zu Operating Manual Kapitel 7, angepasst an den Forschungskontext:

| Bedingung | Maßnahme |
|---|---|
| Master Review und Peer Review erreichen entgegengesetzte fachliche Schlussfolgerungen | Kein automatisches Auflösen. Beide Befunde werden vollständig in die Theory Landscape (Stufe 5) übernommen; die Entscheidung, welcher Seite gefolgt wird (oder keiner), liegt ausschließlich beim Decision Brief / der Editor Decision — nicht bei einer der beiden Review-Stufen selbst. |
| Primärquelle/Studie nicht zugänglich | Arbeit an der betroffenen Teilfrage stoppen; in `OPEN_QUESTIONS.md` dokumentieren; nicht durch Trainingswissen ersetzen, außer mit expliziter Herausgeber-Freigabe und vollständiger Unsicherheitsmarkierung. |
| Ethischer Grenzfall | Sofortige Eskalation an den Herausgeber. Keine eigenständige Entscheidung. |
| Unauflösbarer Canonicalisierungskonflikt bei der Repository Integration | Integration stoppen, Kandidaten in `review_queue.md` eintragen (siehe `canonical_knowledge_model.md`, Abschnitt 4.3), Editor Decision um diesen Punkt ergänzen. |
| Health Check findet ungelöste Pflichtprüfung | Projekt bleibt in `active/`, auch wenn eine Editor Decision bereits vorliegt. Kein Übergang nach `completed/`, bis behoben oder als bewusst akzeptierte Restlücke dokumentiert (siehe `RESEARCH_LIFECYCLE.md`, Stufe 9). |

## 8. Abschlusskriterien (programmweit)

Ein Forschungsprojekt gilt als **abgeschlossen** (unabhängig vom Ausgang), wenn genau eine der folgenden Bedingungen erfüllt ist:

1. **Angenommen:** Editor Decision positiv oder teilweise positiv → Repository Integration abgeschlossen → Health Check bestanden → Status `COMPLETED`.
2. **Abgelehnt:** Editor Decision negativ → Status `ARCHIVED`, keine Repository Integration, kein Health Check erforderlich (es gibt nichts zu prüfen, was in den Codex eingeflossen wäre).

Ein Projekt ohne Editor Decision ist niemals abgeschlossen, unabhängig davon, wie umfangreich Master Review und Peer Review bereits ausgearbeitet sind.

## 9. Verhältnis zu anderen Governance-Dokumenten

Bei Widersprüchen zwischen Research-Program-Dokumenten und dem übrigen Repository gilt folgende Rangfolge:

1. `00_project/SALES_CODEX_OPERATING_MANUAL.md` und `01_framework/05_knowledge_model/canonical_knowledge_model.md` — für alles, was die Identität und Integration von Wissensobjekten betrifft (auch wenn sie aus dem Research Program stammen).
2. `01_framework/02_evidence_system/evidence_system.md` — für Evidenzklassen.
3. Dieses Dokument (`RESEARCH_GOVERNANCE.md`) und `RESEARCH_LIFECYCLE.md` — für den Forschungsprozess selbst.
4. `DECISION_POLICY.md` — für die Entscheidungskriterien der Editor Decision.

Das Research Program führt keine eigene, abweichende Identitätslogik für Wissensobjekte ein. Es entscheidet nur, *ob* und *unter welcher Ausgangslage* ein Ergebnis der bestehenden Logik zugeführt wird.

---

*Dieses Dokument gilt ab RC-1 (2026-07-03). Änderungen nur durch Felix. Vorgängerversion (ein Satz ohne Substanz) siehe Git-Historie.*
