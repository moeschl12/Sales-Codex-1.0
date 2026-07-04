# Decision Brief

Projekt-ID: W-001
Stufe: 6 (`RESEARCH_LIFECYCLE.md`, Abschnitt 8)
Stand: 2026-07-03
Adressat: Herausgeber (Felix)
Bearbeitet im Rahmen: "Research Project W-001 Completion Sprint"

**Hinweis zur Neutralität:** Dieses Dokument enthält gemäß Sprintauftrag ("Neutraler Decision Brief... Keine Empfehlung. Nur Entscheidungsgrundlagen.") **keine Empfehlung**, welche Option gewählt werden soll. Es verdichtet ausschließlich, was in `04_THEORY_LANDSCAPE.md` bereits belegt ist, und macht die Konsequenzen jeder Option explizit.

---

## 1. Zusammenfassung der Research Question

Sollte ein B2B-Vertriebsansatz primär diagnostisch oder primär belehrend vorgehen, und lässt sich dieser Widerspruch theoretisch auflösen? (Vollständige Formulierung: `README.md`)

## 2. Zusammenfassung des Ergebnisses

Vier konkurrierende Basishypothesen (CEAM, MDM, CQM, SMM) wurden im Master Review systematisch bewertet; keine wurde vollständig widerlegt, alle vier weisen dieselbe strukturelle Lücke auf (unzureichende Erklärung der Multi-Akteur-Komplexität eines Buying Centers). Der Master Review entwickelte daraus eine mathematisch formalisierte Synthese-Theorie (SCSM). Der Red Team Review prüfte diese Synthese anhand von 13 wissenschaftlichen Gütekriterien und bewertete 11 von 13 als "nicht erfüllt", 2 als "teilweise erfüllt" — keines als vollständig erfüllt. Die Theory Landscape (Stufe 5) hat diesen Befund bestätigt und präzisiert: Der Widerspruch zwischen den beiden Reviews betrifft ausschließlich die mathematische Formalisierung (SCSM), nicht die zugrunde liegende phänomenologische Beobachtung (Sensemaking-Ansatz empirisch überlegen), die von beiden Reviews unwidersprochen bleibt.

## 3. Zentrale Streitpunkte (aus Theory Landscape übernommen)

| Streitpunkt | Master Review | Red Team Review | Auflösung durch Theory Landscape |
|---|---|---|---|
| Ist das SCSM als mathematisches Modell wissenschaftlich tragfähig? | Ja — Typ-IV/V-Theorie, quantifizierbare Vorhersagen | Nein — 11/13 Kriterien nicht erfüllt, "Mathiness" | Nicht auflösbar auf Ebene der Theory Landscape — beide Positionen bleiben mit ihren jeweiligen Argumenten bestehen; siehe `04_THEORY_LANDSCAPE.md` Abschnitt 3.5 für die vollständige 13-Kriterien-Tabelle |
| Ist die phänomenologische Sensemaking-Kernbeobachtung (Gartner-Studie) belastbar? | Ja | Ja (nicht bestritten) | Kein Streitpunkt — beide Reviews stimmen überein |
| Sind CEAM, MDM, CQM als Einzelhypothesen brauchbar? | Ja, mit benannten Schwächen | Nicht einzeln geprüft (nur im SCSM-Verbund kritisiert) | Kein direkter Streitpunkt, aber ungleiche Prüftiefe |

## 4. Evidenzlage im Überblick

| Element | Evidenzqualität | Quelle |
|---|---|---|
| Sensemaking-Verkäufer erzielen höhere Glaubwürdigkeit/Abschlussraten | Eine großzahlige externe Studie (Gartner, >1.100 Befragte), von beiden Reviews unwidersprochen zitiert | `REFERENCES.md` #3, #37, #57 |
| SCSM-spezifische mathematische Vorhersagen (z. B. "Information-Quantity-Penalty") | Keine empirische Prüfung vorliegend — Vorhersagen sind laut Master Review selbst erst noch zu testendes zukünftiges Forschungsprogramm | `02_SCIENTIFIC_MASTER_REVIEW.md`, Abschnitt "Offene Forschungsfragen" |
| ADAPTS-Skala (Grundlage von CEAM) | Seit 1990 dokumentierte, mehrfach replizierte psychometrische Schwäche | `REFERENCES.md` #86, #87 |
| Trend zu verkäuferfreiem B2B-Kauf (Geltungsbereichseinschränkung für alle vier Hypothesen) | Eine zitierte Studie (bis 75 % Präferenz für verkäuferfreien Kauf) | `03_GEMINI_RED_TEAM_REVIEW.md`, Abschnitt 2.10 |

**Wichtiger Hinweis zur Quellenqualität:** Keine der 119 in `REFERENCES.md` konsolidierten Quellen ist eine im Sales Codex nach `01_framework/08_templates/source_template.md` erfasste Quelle mit zugewiesener Quellenklasse (A–F). Es handelt sich durchgängig um Web-Recherche-Ergebnisse der beiden Reviews selbst (Blog-Zusammenfassungen, Scribd-Dokumente, Wikipedia, einzelne Fachartikel) — eine formale Quellenklassifizierung nach Sales-Codex-Standard hat für keine dieser 119 Quellen stattgefunden und wäre bei einer Repository Integration nachzuholen (siehe `05_DECISION_BRIEF.md` Abschnitt 6, unten, sowie den Repository-Integrationsplan im Completion Report).

## 5. Offene Fragen (unverändert aus `OPEN_QUESTIONS.md`)

- OQ-2, OQ-3, OQ-4: Weiterführende empirische Forschungsfragen, unabhängig vom Ausgang dieser Entscheidung.
- OQ-5: Geltungsbereich-Überdehnung durch den Trend zu verkäuferfreiem B2B-Kauf — betrifft potenziell jede Option.

## 6. Konsequenzen jeder Entscheidungsoption

Diese Optionen entsprechen `DECISION_POLICY.md`, Abschnitt 2. Für jede Option werden ausschließlich die Konsequenzen beschrieben — keine Präferenz.

### Option "Annehmen" (SCSM vollständig, inkl. mathematischer Formalisierung)

**Konsequenz:** Würde dem Befund des Red Team Review in 11 von 13 Kriterien widersprechen. Voraussetzung für eine Evidenzklasse E3+ (`DECISION_POLICY.md`, Abschnitt 3) wäre eine zusätzliche wissenschaftliche Validierung (`RESEARCH_GOVERNANCE.md`, Abschnitt 4.5) — auf Basis der vorliegenden Reviews allein wäre dieser Nachweis nicht erbracht. Würde ein neues Modell-Objekt (MOD) mit vollständiger mathematischer Formalisierung im Sales Codex etablieren — ein Novum, da bislang kein MOD-Objekt im Codex auf Differentialgleichungen beruht (Abgleich außerhalb des Scopes dieses Sprints, nicht durchgeführt).

### Option "Teilweise annehmen" (phänomenologischer Kern ohne mathematische Formalisierung)

**Konsequenz:** Würde nur die in `04_THEORY_LANDSCAPE.md` Abschnitt 4 als "nicht verworfen" markierten Elemente integrieren (empirische Kernbeobachtung, phasen-/kontextabhängiges Verhältnis von Diagnose und Belehrung als unformalisierte Heuristik). Erfordert eine explizite Festlegung, welcher Objekttyp (vermutlich Prinzip, ggf. mit Bezug zu bestehenden P-Objekten zu SPIN/Challenger) und welche Evidenzklasse (voraussichtlich E2, da einzelne Studie/Forschungsstrang ohne dritte unabhängige Bestätigung — `canonical_knowledge_model.md`, Abschnitt 7) angemessen wäre. Würde die 13-Kriterien-Kritik des Red Team Review zu weiten Teilen umgehen, da die kritisierten Elemente (Ω, Σ, κ, ξ, Differentialgleichung) gerade nicht übernommen würden.

### Option "Zurückstellen"

**Konsequenz:** Erfordert laut `DECISION_POLICY.md`, Abschnitt 2 eine konkrete, prüfbare Bedingung für die erneute Vorlage. Mögliche konkrete Bedingungen, die sich aus der Theory Landscape ableiten ließen (rein deskriptiv aufgeführt, nicht empfohlen): eine zusätzliche externe wissenschaftliche Validierung des SCSM (Kriterium 7, empirische Operationalisierbarkeit); eine überarbeitete, nicht-mathematisch-formalisierte Fassung des SCSM zur erneuten Prüfung; eine Klärung der OQ-5-Randbedingung (Geltungsbereich) vor einer Entscheidung über alle vier Basishypothesen.

### Option "Ablehnen"

**Konsequenz:** Keine Repository Integration. W-001 würde nach `archived/` verschoben (`RESEARCH_GOVERNANCE.md`, Abschnitt 6.3). Der zugrunde liegende, seit SPR-0001 dokumentierte Widerspruch ("Teach First vs. Diagnose First") bliebe im Sales Codex weiterhin ungelöst und müsste ggf. erneut als eigenständiges Forschungsprojekt oder über `00_project/OPEN_DECISIONS.md` adressiert werden — diese Konsequenz betrifft alle vier Basishypothesen gemeinsam, nicht nur das SCSM, da eine vollständige Ablehnung auch die "nicht verworfenen" Teilelemente aus Abschnitt 4 der Theory Landscape nicht integrieren würde.

## 7. Was dieser Brief nicht enthält

Keine Empfehlung, welche Option zu wählen ist. Keine Bewertung, ob der Herausgeber der Einschätzung des Master Review oder des Red Team Review folgen sollte. Diese Bewertung ist ausdrücklich der Editor Decision (Stufe 7) vorbehalten (`RESEARCH_GOVERNANCE.md`, Abschnitt 4.1).

## 8. Status

Vollständig — vorgelegt zur Editor Decision (Stufe 7). Siehe `06_EDITOR_DECISION.md` (Entwurf).
