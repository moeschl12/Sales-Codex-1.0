# Codex Merge Readiness Overview

**Dokumentklasse:** Governance / Entscheidungsgrundlage (Übersicht, keine Umsetzung)
**Task-Type:** am ehesten T6_AUDIT (repositoryweite, rein lesende Bewertung mit Scope-Grenze) mit T11_SCIDEBT-Bezug (Scientific-Debt-Konsolidierung) — kein exakter Treffer in `TASK_TYPES.md`, daher hier explizit benannt statt stillschweigend zugeordnet.
**Auftrag:** "Codex-Zusammenführungsübersicht als Entscheidungsgrundlage für den Aufbau eines schlanken, nutzbaren Sales-Codex-Leitfadens" (Felix, 2026-07-14)
**Charakter:** Reine Übersicht/Bestandsaufnahme. Keine neuen Wissensobjekte angelegt, keine bestehenden Objekte geändert, keine neuen Quellen recherchiert, kein Commit/Push.
**Grundlage:** `00_project/ACADEMIC_RECOVERY_CONSOLIDATION_REPORT.md`, `00_project/ACADEMIC_RECOVERY_PLAN.md` (Kopf-/Abschnittsebene), `00_project/SCIENTIFIC_DEBT.md` (vollständig), `05_research/LITERATURE_INDEX.md` (Sektionsebene), `00_project/review_queue.md`, `00_project/OPEN_DECISIONS.md` (OD-007, OD-010 punktuell), `01_framework/02_evidence_system/evidence_system.md`, sowie alle 57 Prinzipien-, 30 Mechanismen-, 47 Techniken- und 12 Modell-Objekte in `03_knowledge_base/`.
**Datum:** 2026-07-14

---

## 1. Executive Summary

Der Academic-Recovery-Block AR-001 bis AR-014 ist abgeschlossen, die ED-AR-1 bis ED-AR-10-Entscheidungen sind getroffen. Der Codex-Bestand (57 Prinzipien, 30 Mechanismen, 47 Techniken, 12 Modelle, plus 60 Annahmen und 331 Statements als Unterbau) ist damit in einem konsolidierten, aber nicht gleichmäßig reifen Zustand. Für einen schlanken Praxisleitfaden ist die zentrale Erkenntnis dieser Übersicht: **Reife ist nicht gleich über den Codex verteilt, sondern folgt klaren Bruchlinien.**

Drei wiederkehrende Muster prägen die Evidenzlage:

Erstens sind die Kernmechanismen aus etablierter Kognitions- und Sozialpsychologie (Verlustaversion, Anchoring, Reziprozität, soziale Bewährtheit, Autorität, Reaktanz, Kontrast, Fairness/Ultimatum-Spiel, Konkretheits-Encoding) durchweg gut belegt (E4–E5) — die vertriebsspezifische *Anwendung* dieser Mechanismen ist jedoch fast überall nur E2–E3, weil sie meist auf genau einer Praktiker-Hauptquelle beruht. Diese Lücke ist nicht auflösbar durch weiteres Lesen bestehender Bücher, sondern nur durch neue B2B-spezifische Primärforschung — das ist eine strukturelle Eigenschaft des Codex, keine Nachlässigkeit.

Zweitens tragen drei proprietäre, kommerzielle Großstudien (SPIN/Huthwaite N=35.000; Challenger/CEB N=6.000; JOLT/Tethr-ML) einen erheblichen Teil der konkreten, "griffigen" Zahlen im Codex (53%/38%/9%-Loyalitätssplit, 44%/56%-Indecision-Split) — bei allen dreien fehlt unabhängige Replikation und öffentliche Rohdatenprüfung (SD-SYS-001, SD-SYS-004, Kategorie 3: "plausibel, aber nicht sales-spezifisch nachgewiesen"). Diese Zahlen sind für einen Leitfaden riskant, wenn sie als belastbare Fakten statt als Anbieterbefunde mit Vorbehalt dargestellt werden.

Drittens ist ein ganzer Theoriecluster (Buying-Center-/Principal-Agent-Dynamik: Johnston & Lewin 1996, Eisenhardt 1989, Webster & Wind 1972, March & Simon 1958) zu drei Vierteln durch fehlenden Primärtextzugriff blockiert (ED-AR-7: dauerhaft blockiert bis neue Zugriffslage, keine automatischen Wiederholungsversuche). Nur Sheth (1973) wurde vollständig verarbeitet. Dieser Cluster trägt aktuell vor allem Konsens-/Champion-Praxisregeln, deren theoretische Tiefenbegründung nicht primärtextgeprüft ist.

Auf der positiven Seite gibt es einen harten Kern mit niedrigem Scientific-Debt-Risiko und hoher Praxisreife: Verhandlungsgrundprinzipien (Getting to Yes), Anchoring, die Fairness-Schwelle (nach AR-012 kulturell präzisiert und von Hoch auf Mittel herabgestuft), Vertrauen als B2B-Erfolgstreiber (durch Ohiomah et al. 2020 aktuell gestärkt) und Konkretheit/Klarheit in der Kommunikation. Diese Blöcke eignen sich am ehesten, um zuerst geschrieben zu werden.

**Methodischer Hinweis zur Reichweite dieser Übersicht:** Ausgewertet wurden alle P-/MEC-/T-/MOD-Objekte vollständig (Titel, Evidenzfeld, Status, ggf. Grenzen) sowie `SCIENTIFIC_DEBT.md` vollständig (472 Zeilen) und der Konsolidierungsbericht vollständig. Die 331 Statement- und 60 Annahme-Objekte wurden **nicht** einzeln gelesen, sondern nur über ihre Verknüpfung in P-/MEC-Objekten und über die buchweise organisierten `SCIENTIFIC_DEBT.md`-Einträge erschlossen — für eine Zusammenführungsübersicht auf Leitfaden-Kapitelebene ist das die tragende Objektebene; eine Einzelprüfung aller 391 ST/A-Objekte wäre ein eigener, deutlich größerer Auftrag (vgl. Suchgrenze `PROJECT_BOOTSTRAP.md`). `ACADEMIC_RECOVERY_PLAN.md` wurde nur auf Kopf-/Abschnittsebene geprüft, da der Konsolidierungsbericht ihn explizit als Grundlage nennt und inhaltlich referenziert.

---

## 2. Leitfadenreife-Matrix

Legende Leitfadenreife: **A** = direkt leitfadenreif · **B** = leitfadenreif mit Vorsicht/Boundary Conditions · **C** = nur Hintergrund/keine starke Praxisregel · **D** = blockiert/nicht verwenden.
Legende Claim-Stärke: starke Praxisregel · kontextabhängige Praxisregel · plausible Arbeitshypothese · Hintergrundwissen · nicht verwenden.

### 2.1 Problem / Need / Gap / Cost of Inaction

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0001, MEC-0002, MEC-0004; P-0001, P-0002, P-0004, P-0005, P-0006, P-0025, P-0026; P-S1-001 (Cost of Inaction), P-S1-003 (Problemzentrierung); T-0001–T-0004, T-0022–T-0024; MOD-0001, MOD-0005 |
| Quellenbasis | SRC-0001 (SPIN Selling), SRC-0005 (Gap Selling), SRC-0029–0031 (Kahneman/Tversky Primärquellen, AR-007) |
| Evidenzlage (einfach) | Der psychologische Kernmechanismus (Verlustaversion/Problemgewicht) ist einer der bestbelegten Befunde der Verhaltensökonomik (E4/E5 allgemein). Die Vertriebsanwendung selbst hängt aber fast vollständig an einer einzigen Praktikerquelle (SPIN) bzw. bei P-0002 exakt an dieser einen Quelle — AR-007 fand keine unabhängige zweite Evidenzbasis. Gap Selling (B-0005) ist zusätzlich nur aus einer unvollständigen Quelle extrahiert. |
| Scientific-Debt-Status | B-0001: Externe Validierung ausstehend (Mittel). SD-SYS-002: Gap-Selling-Quellenunvollständigkeit (Hoch, impliziter Vollständigkeitsvorbehalt für alle B-0005-Objekte). ED-AR-1 entschieden: P-0002 von "E4-Kandidat" auf E3 präzisiert. |
| Leitfadenreife | **A** für den SPIN-Kern (P-0001, P-0004, P-0005, T-0001–T-0004) — in sich konsistent, jahrzehntelang praktisch erprobt. **B** für P-0002 (Solution-Value) — Einzelquellenabhängigkeit explizit benennen. **C** für Gap-Selling-spezifische Objekte (P-0025/P-0026, MOD-0005) wegen Quellenlücke. |
| Empfohlene Claim-Stärke | SPIN-Fragesequenz (Situation→Problem→Implication→Need-Payoff) = kontextabhängige Praxisregel. "Lösungswert folgt Problemgewicht" (P-0002) = plausible Arbeitshypothese, nicht als starke Regel. Gap-Diagnose-Tiefe = Hintergrundwissen bis Quellenlücke geschlossen. |
| Grenzen/Warnhinweise | Nicht bei Impulskäufen/geringem Involvement. Ethisches Risiko Mittel bis Hoch bei übertriebener Problemvergrößerung ("Angstverkauf"). |
| Offene Anschlussfragen | Gap-Selling-Vollquelle beschaffen (SD-SYS-002, seit Sprint 1 unverändert offen). Unabhängige zweite Evidenzbasis für P-0002 weiterhin nicht gefunden. |

### 2.2 Insight / Reframing / Challenger / Teach-Tailor-Take-Control

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0013 (Insight-Disruption), MEC-0014 (Konsens als Kaufsicherheit, geteilt); MOD-0004 (TTC-Modell); P-0021–P-0024; T-0019–T-0021; A-0019 |
| Quellenbasis | SRC-0004 (Challenger Sale, proprietäre CEB-Studie N=6.000), Rapp et al. 2014 (SRC-0021, Modellkritik), Sheth 1973 (SRC-0025) |
| Evidenzlage (einfach) | Die zentrale Zahl (53%/38%/9%-Loyalitätssplit, A-0019) beruht auf einer nicht replizierten, proprietären Studie ohne öffentliche Rohdaten. Zusätzlich existiert unabhängige akademische Modellkritik am Gesamtmodell (Rapp et al. 2014, Konstruktvalidität der fünf Profile in Frage gestellt) — betrifft das Modell als Ganzes, nicht isoliert die Kennzahl. Nach ED-AR-4 ist MEC-0014 in drei Ebenen getrennt: beobachteter CEB-Befund (E3), spezifische Kausalkette über persönliches Risiko (E2), Generalisierung (E2). |
| Scientific-Debt-Status | A-0019/SD-SYS-001: Replikationsrisiko, Hoch, unverändert. SD-SYS-004: Publication-Bias-Kategorie 3 ("plausibel, nicht sales-spezifisch nachgewiesen"), Hoch. ED-AR-4/ED-AR-5 entschieden (Kalibrierung durchgeführt, kein neues MEC "Principal-Agent-Risiko" ohne Primärtextzugriff). W-001/OQ-2 bleibt auch nach W-008 empirisch ungeklärt. |
| Leitfadenreife | **B** — die qualitative Kernlogik (Teach vor Lösung, Reframing, interne Befähigung des Champions) ist praktisch brauchbar; die konkreten Prozentzahlen dürfen **nicht** unkommentiert als Fakt stehen. |
| Empfohlene Claim-Stärke | "Insight/Reframing vor Lösungspräsentation" = kontextabhängige Praxisregel. Konkrete CEB-Prozentzahlen = nicht verwenden als belastbare Statistik, allenfalls als explizit gekennzeichneter Anbieterbefund. |
| Grenzen/Warnhinweise | Proprietäre, nicht peer-reviewte Datenbasis; strukturelles Publication-Bias-Risiko plausibel, aber nicht sales-spezifisch nachgewiesen; W-001-Editor-Decision: kein universeller Gegensatz zu Diagnose-First (Gap Selling/SPIN), sondern kontextabhängige Koexistenz. |
| Offene Anschlussfragen | OQ-2 (Omission-Kipppunkt im Buying Center) nur durch dediziertes Primärexperiment klärbar. Agency-Theory-Pfad bleibt unvalidierte Transferhypothese. |

### 2.3 Buying Center / Konsens / Champion / Stakeholder-Tailoring

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0014, A-0022, ST-0126; P-0022, P-0023; T-0020; Cross-Links aus W-004 |
| Quellenbasis | SRC-0004 (CEB), SRC-0025 (Sheth 1973, vollständig verarbeitet), SRC-0026 (Webster & Wind 1972, **blockiert**), SRC-0027 (Eisenhardt 1989, **blockiert**), SRC-0017 (Johnston & Lewin 1996, **blockiert**), SRC-0039 (March & Simon 1958, **blockiert**) |
| Evidenzlage (einfach) | Der theoretische Kerncluster (Principal-Agent-/Buying-Center-Theorie) ist zu drei Vierteln blockiert — nur Sheth (1973) wurde vollständig gelesen und liefert konzeptionelle Stütze für Rollendifferenzierung/Konfliktmodi. Kein eigenständiges MEC "Principal-Agent-Risiko" existiert; der bestehende Agency-Pfad in MEC-0014 (seit W-004) ist ausdrücklich als unvalidierte Transferhypothese gekennzeichnet, nicht als tragende Objektstütze. |
| Scientific-Debt-Status | AR-003/AR-005/AR-014 dauerhaft blockiert bis neue Zugriffslage (ED-AR-7, keine automatischen Wiederholungsversuche). Fusion-Kandidat MEC-0006/MEC-0014 weiterhin offen (`review_queue.md`, Herausgeberentscheidung ausstehend). Meta-Prinzip-Kandidat "Asymmetrische Risikoverteilung im Buying Center" nicht formal angelegt (NSTD). |
| Leitfadenreife | **B** für die Praxisempfehlung selbst (Champion braucht interne Verbündete/Konsens, Stakeholder-spezifisch ansprechen — P-0022/P-0023/T-0020). **C** für die theoretische Tiefenbegründung (Buying-Center-Konsensmechanismus als solcher, wegen der Blockadequote). |
| Empfohlene Claim-Stärke | "Champion braucht organisationsweite Unterstützung" = kontextabhängige Praxisregel. "Konsens reduziert persönliches Karriererisiko des Champions" (Agency-Pfad) = plausible Arbeitshypothese, nicht stärker formulieren. |
| Grenzen/Warnhinweise | Keine belastbare quantitative Aussage darüber, wie viel/welche Art von Konsens nötig ist. CTX/OD-007 (Kontext-Modifikator-Ebene für Objekte wie diese) ist entscheidungsreif, aber noch nicht von Felix entschieden. |
| Offene Anschlussfragen | OD-007-Entscheidung aussteht (entscheidungsreif seit 2026-07-01). Fusion-Kandidat MEC-0006/MEC-0014 aussteht. Blockierte Primärquellen nur bei neuem Zugriff erneut prüfen. |

### 2.4 Trust / Beziehung / Rapport

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0030 (ABI-Modell), MEC-0007 (Sympathieübertragung); P-0012 (Rapport); MOD-0003 |
| Quellenbasis | Mayer, Davis & Schoorman 1995 (ABI, meta-analytisch bestätigt durch Colquitt et al. 2007), Palmatier et al. 2006, Ohiomah, Benyoucef & Andreev 2020 (SRC-0022) |
| Evidenzlage (einfach) | Der allgemeine ABI-Trust-Mechanismus ist meta-analytisch sehr gut belegt (E4). Die B2B-Sales-Relevanz wurde durch AR-009 zusätzlich gestärkt: Kundenvertrauen ist laut Ohiomah et al. (2020, 139 Studien) die stärkste einzelne B2B-Erfolgsdeterminante (r=0,48). Die interne Trennung Cognitive/Affective Trust bleibt uneinheitlich belegt (W-003, OQ-1). High-Ticket-B2C-Transfer (z. B. Immobilien/Hausbau) ist ausdrücklich **nicht** belegt — keine Fertighaus-spezifischen Regeln ableiten (Editor Decision W-003). |
| Scientific-Debt-Status | W-003 OQ-1 bis OQ-9 offen, aber überwiegend Niedrig/Mittel priorisiert, kein Folgeprojekt vorgesehen. MEC-0030-Evidenzlevel-Anhebung wegen Ohiomah-Befund geprüft, aber nicht dringlich entschieden (AR-009). |
| Leitfadenreife | **A** für "Vertrauen ist einer der stärksten B2B-Erfolgstreiber" (breit und aktuell konvergent bestätigt). **B** für spezifische Trust-Aufbau-Taktiken, die auf der Cognitive/Affective-Trennung beruhen. |
| Empfohlene Claim-Stärke | "Vertrauen korreliert stark mit Vertriebserfolg" = starke Praxisregel (Meta-Analyse-Basis). Getrennte Cognitive-/Affective-Trust-Taktiken = plausible Arbeitshypothese. |
| Grenzen/Warnhinweise | Kein High-Ticket-B2C-Transfer (explizit ausgeschlossen). Trust-Repair (Vertrauensreparatur nach Bruch) liegt außerhalb des MEC-0030-Scopes. |
| Offene Anschlussfragen | W-003 OQ-1–OQ-9 (Detailfragen zu Trust-Repair, Sequenzierung, SET-Konkurrenzmodell) bleiben dokumentiert offen. |

### 2.5 Indecision / JOLT / Choice Overload / Risikoabbau

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0015 (kognitive Überlastung, inkl. AR-013-Erweiterung ED-AR-2), MEC-0016 (FOMU); MOD-0006 (JOLT-Modell); T-0026–T-0030; ST-0151; P-S1-004 (Informationssparsamkeit) |
| Quellenbasis | SRC-0006 (JOLT/Tethr, proprietär), SRC-0016 (Tversky & Shafir 1992, vollständig verarbeitet, AR-013), Miller's Law (E5, kanonisch) |
| Evidenzlage (einfach) | Die Kernzahl (44%/56%-Split) beruht auf nicht offengelegter, proprietärer ML-Klassifizierung ohne externe Replikation. Tversky & Shafir (1992) liefert unabhängige akademische Stütze **nur** für das allgemeine Phänomen "Aufschub/Rückkehr zur Default-Option bei Optionskonflikt" — **nicht** für FOMU/MEC-0016 selbst (AR-013: expliziter Negativbefund, anderer kausaler Mechanismus) und nicht für die spezifischen Tethr-Zahlen. MEC-0015 wurde entsprechend um einen vierten, akademisch gestützten Auslösepfad erweitert (ED-AR-2). |
| Scientific-Debt-Status | B-0006 mehrere offene Punkte (Mittel: 44%/56%-Split weiterhin unrepliziert; MEC-0016/A-0031 externe Validierung nach AR-013-Prüfung weiterhin ausstehend). |
| Leitfadenreife | **A** für Miller's-Law-basierte Informationsreduktion (P-S1-004, T-0022, sehr robust belegt). **B** für die JOLT-Grundlogik "Unentschlossenheit als eigene Kategorie neben Nein" (jetzt teilweise akademisch gestützt). **C** für die 44%/56%-Zahl und die vier JOLT-Techniken als getestetes Gesamtsystem. |
| Empfohlene Claim-Stärke | "Weniger Optionen/Information reduziert Entscheidungslähmung" = starke Praxisregel (robust). "44% aller verlorenen Deals sind Unentschlossenheit" = nicht verwenden als Fakt, höchstens als gekennzeichneter Anbieterbefund. "FOMU als Haupttreiber der Unentschlossenheit" = plausible Arbeitshypothese. |
| Grenzen/Warnhinweise | JOLT-Datenbasis ist US-COVID-Zeitraum (2020–2021) — Übertragbarkeit auf Präsenzverkauf/Post-COVID/Nicht-US-Märkte ungetestet. |
| Offene Anschlussfragen | Externe Replikation der Tethr-Klassifizierung fehlt weiterhin und ist nicht in Aussicht. |

### 2.6 Verhandlung / BATNA / Interessen / objektive Kriterien

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MOD-0007 (Principled Negotiation), MEC-0017 (Fixed-Pie Fallacy); P-0031–P-0034; T-0031–T-0034 |
| Quellenbasis | SRC-0007 (Getting to Yes), Thompson 1990 |
| Evidenzlage (einfach) | Institutionell sehr gut etabliert (Harvard, jahrzehntelange Rechts-/Mediationspraxis), aber kein RCT-Vergleich gegen positionelles Feilschen. Fixed-Pie-Fallacy-Mechanismus selbst ist gut belegt (E4); die konkrete B2B-Preisverhandlungsanwendung ist nicht direkt gemessen. |
| Scientific-Debt-Status | B-0007: niedrigste Priorität im gesamten Codex (Niedrig, Externe Validierung ausstehend / Offene Forschungsfrage). |
| Leitfadenreife | **A** — Kernprinzipien sind praxisreif und tragen die niedrigste Scientific-Debt-Priorität im gesamten Repository. |
| Empfohlene Claim-Stärke | "Interessen statt Positionen fokussieren", "objektive Kriterien nutzen", "BATNA kennen und entwickeln" = starke Praxisregel für die Grundprinzipien; kontextabhängige Praxisregel für die konkrete B2B-Preisanwendung. |
| Grenzen/Warnhinweise | Kein direkter Wirksamkeitsvergleich zu alternativen Verhandlungsstilen; funktioniert schwächer in rein distributiven Verhandlungen ohne Interessenvielfalt. |
| Offene Anschlussfragen | Keine dringlichen. |

### 2.7 Social Proof / Authority / Reciprocity / Scarcity / Unity

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0005–MEC-0009, MEC-0019; MOD-0002; P-0008–P-0015; T-0005–T-0011 |
| Quellenbasis | SRC-0002 (Influence, Cialdini), Milgram 1963/1974, Regan 1971, Freedman & Fraser 1966, Langer/Xerox |
| Evidenzlage (einfach) | Allgemeine sozialpsychologische Mechanismen sind gut belegt (E4), B2B-spezifische Anwendung überwiegend E3 (Feldbelege, keine Meta-Analyse). Xerox-Studie (Langer) hat unklaren Replikationsstatus (Hoch), Regan-Reziprozitätsexperiment ungeprüften Replikationsstatus (Mittel). Research Pack 3 bestätigt unabhängig "keine robuste B2B-spezifische Meta-Analyse" für Reciprocity, Social Proof, Authority, Liking (SD-SYS-006, Konvergenzbestätigung — löst die Lücke nicht auf, bestätigt nur die vorsichtige Kalibrierung). |
| Scientific-Debt-Status | B-0002: mehrere Einträge Hoch (externe Validierung, Replikationsrisiko). **Wichtige Präzisierung (OD-010, 2026-07-13):** Der wörtliche Platzhaltersatz "Gemini-Validierung ausstehend" wurde in 9 betroffenen Objekten (u. a. MOD-0002, P-0009, P-0012, P-0013, P-0015) redaktionell auf "externe Validierung ausstehend, Instrument gemäß OD-010 nicht mehr aktuell" umformuliert — die inhaltliche Evidenzlücke selbst ist dadurch **nicht** geschlossen, nur die Terminologie korrigiert. Nahe Varianten (z. B. MEC-0005–MEC-0008: "Gemini-Validierung für [Aspekt] ausstehend") waren laut Editor Decision OD-009–012 explizit **nicht** Teil dieser Bereinigung und sollten bei Bedarf gesondert geprüft werden. |
| Leitfadenreife | **A** für die sechs Cialdini-Grundprinzipien als Erklärungsraster (breit repliziert, E4 allgemein). **B** für die konkreten Vertriebstechniken (T-0005–T-0011), da B2B-Feldbelege dünner sind als Laborbelege. |
| Empfohlene Claim-Stärke | Grundprinzipien als Erklärungsmodell = starke Praxisregel. Einzelne Techniken (Vorab-Leistung, Verknappungssignale) = kontextabhängige Praxisregel. |
| Grenzen/Warnhinweise | Kulturelle Variation (individualistisch/kollektivistisch); professionelle B2B-Einkäufer teils resistenter gegen automatische Compliance-Trigger. |
| Offene Anschlussfragen | Terminologie-Bereinigung gemäß OD-010 in den nicht explizit genannten Objekten (MEC-0005–MEC-0008 u. a.) noch nicht durchgeführt — als redaktioneller Nacharbeitspunkt dokumentiert, nicht Teil dieses Auftrags. |

### 2.8 Pricing / Framing / Anchoring / Fairness

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0009 (Kontrast), MEC-0021 (Anchoring), MEC-0023 (Zero-Preis), MEC-0025 (Altruistische Bestrafung/Fairness); MOD-0010, MOD-0011; P-0014, P-0042, P-0045–P-0051; T-0008, T-0040, T-0043, T-0046 |
| Quellenbasis | SRC-0010 (Kahneman), SRC-0012 (Predictably Irrational/Ariely), SRC-0013 (Nudge), SRC-0014 (Priceless), SRC-0029–0031 (Kahneman/Tversky-Primärquellen, AR-007), SRC-0037/0038 (Henrich 2001, Oosterbeek et al. 2004 — AR-012) |
| Evidenzlage (einfach) | Anchoring (MEC-0021) ist E5 und eines der am robustesten replizierten Phänomene der Kognitionspsychologie — sogar nach Publication-Bias-Korrektur bestätigt (Schley & Weingarten 2023). Das Fairness-/Ultimatum-Spiel-Grundphänomen ist E4 (37-Studien-Metaanalyse); AR-012 hat die kulturelle Generalisierungsgrenze präzisiert und von Hoch auf Mittel herabgestuft (Kernmechanismus über 25 marktintegrierte Länder robust, Regionalvariation nicht durch Hofstede erklärbar, Randrisiko nur bei extremer Marktferne — kein realistisches B2B-Szenario). **Wichtiger Vorbehalt:** Die für den Codex genutzten Kernmechanismen (Decoy, Anchoring, Zero-Preis, Endowment) sind bibliografisch über unabhängige Gründungsquellen von Arielys dokumentiertem Autoren-Integritätsrisiko entkoppelt ("partially mitigated") — betroffen bleibt spezifisch das Ehrlichkeits-/Dishonesty-Kapitel (bewusst nicht in P/MEC überführt). Choice Architecture/Default-Effekt (MOD-0011, MEC-0002-Erweiterung) steht unter einer aktiven, ungelösten Publikationsbias-Kontroverse (SD-SYS-005) und wurde deshalb bewusst **nicht** auf ein höheres Evidenzlevel gehoben trotz neuer B-0013-Stützbelege. |
| Scientific-Debt-Status | SD-SYS-005 (Mittel, aktive wissenschaftliche Kontroverse, nicht aufgelöst). B-0012 Autoren-Integritätsrisiko "partially mitigated" (Hoch als generelle Kategorie). AR-012 kulturelle Generalisierung teilweise geschlossen (Mittel, herabgestuft von Hoch). |
| Leitfadenreife | **A** für Anchoring-Grundtechnik (sehr robust) und Fairness-Schwelle (kulturell präzisiert). **B** für Default-Effekt/Choice Architecture (aktive Kontroverse — nicht pauschal aufwerten). **C** für Decoy-/Zero-Preis-Techniken (stärker B2C- als B2B-getestet). |
| Empfohlene Claim-Stärke | "Erster Anker bestimmt Verhandlungsspielraum" = starke Praxisregel. "Fairness-Schwelle beachten" = starke Praxisregel mit eng gefasster kultureller Randbedingung. "Defaults lenken Entscheidungen" = kontextabhängige Praxisregel (nicht als Universalhebel darstellen). |
| Grenzen/Warnhinweise | WEIRD-Bias durchgängig (US-Studierende in den meisten Experimenten); kein direkter B2B-Transfer in den meisten Einzelexperimenten; Ariely-Ehrlichkeitskapitel nicht verwendbar. |
| Offene Anschlussfragen | Isolierte, defaultspezifische (statt pauschale Choice-Architecture-)Meta-Analyse noch nicht identifiziert. |

### 2.9 Kommunikation / Mirroring / Labeling / Fragen / Kritik

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0010 (Labeling), MEC-0011 (Mirroring), MEC-0012 (Dual-Process-Framing); P-0016–P-0020, P-0044; T-0012–T-0018, T-0042; MOD-0003 |
| Quellenbasis | SRC-0003 (Never Split the Difference/Voss), Lieberman et al. 2007, Stephens & Hasson 2010, SRC-0011 (Emotional Intelligence/Gottman) |
| Evidenzlage (einfach) | MEC-0010/MEC-0011 wurden 2026-07-01 per Peer Review von E3 auf E2 herabgestuft (Laborstudien ohne direkten B2B-Verhandlungsbeweis; die Spiegelneuronen-Verbindung selbst ist wissenschaftlich umstritten, E1). Zusätzlich besteht ein **aktiver, ungelöster Widerspruch**: Ireland & Henderson (2014) zeigen, dass anhaltendes/spätes verbales Mirroring über eine gesamte Verhandlung mit höherem Sackgassenrisiko korreliert, während Voss es ohne zeitliche Einschränkung als durchgehende Technik empfiehlt. Kalibrierte Fragen (T-0015) haben etwas bessere Stützung (Williams 1983 Lawyer Study, E3), aber keine direkten kontrollierten Verhandlungsexperimente. P-0044 (Verhaltenskritik statt Charakterangriff) ist eine Konvergenz zweier unabhängiger, außerhalb des Vertriebs entstandener Forschungslinien (Gottman, Levinson), daher E3. |
| Scientific-Debt-Status | B-0003: mehrfach Hoch (externe Validierung ausstehend für MEC-0010/MEC-0011, Replikationsrisiko der Spiegelneuronen-Verbindung). Widerspruch Ireland & Henderson vs. Voss dokumentiert, nicht aufgelöst (Mittel). |
| Leitfadenreife | **B** für Labeling und kalibrierte Fragen (praktisch brauchbar, aber mit E2/E3-Vorsicht formulieren). **C** für Mirroring speziell über die gesamte Gesprächsdauer (aktiver Widerspruch — hier nicht als pauschale Dauerregel formulieren). **B** für P-0044 (Kritikformulierung). |
| Empfohlene Claim-Stärke | "Emotionen benennen (Labeling) deeskaliert" = kontextabhängige Praxisregel. "Fragen statt Aussagen senken Reaktanz" = kontextabhängige Praxisregel. "Mirroring durchgehend anwenden" = nicht verwenden als Dauerregel — wenn überhaupt, nur früh im Gespräch mit explizitem Warnhinweis. |
| Grenzen/Warnhinweise | Spiegelneuronen-Erklärung nicht mehr als Begründung verwenden (E1, umstritten). Zeitliche Grenze bei Mirroring beachten (Ireland & Henderson). |
| Offene Anschlussfragen | Widerspruch Ireland & Henderson vs. Voss bleibt ungelöst. Keine direkten B2B-Verhandlungsexperimente zu kalibrierten Fragen. |

### 2.10 Sticky Ideas / Klarheit / Konkretheit / Curse of Knowledge

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0026 (Curse of Knowledge), MEC-0027 (Gap-Theorie der Neugier), MEC-0028 (Konkretheits-Encoding), MEC-0029 (Narrative Transportation); MOD-0012 (SUCCESS); P-0036, P-0053; T-0047 |
| Quellenbasis | SRC-0015 (Made to Stick), Camerer/Loewenstein/Weber 1989, Rubin 1995, Loewenstein 1994 |
| Evidenzlage (einfach) | Curse of Knowledge ist E3 (konvergente Studiendesigns, aber keine Meta-Analyse identifiziert). Konkretheits-Encoding ist E4 (breit repliziert für Gedächtnisleistung generell) — **aber** der spezifische Anwendungsfall "Identifiable Victim Effect" (Rokia-Spendenexperiment) hat eine gescheiterte, präregistrierte 2023-Replikation (⚠⚠, bewusst nicht als eigener Mechanismus verwendet). Das SUCCESS-Gesamtmodell (MOD-0012) selbst ist als Kombinationswirkung nicht getestet. Durchgängiges Survivorship-Bias-Risiko im gesamten Quellbuch (unkontrollierte Fallstudien, Hoch). |
| Scientific-Debt-Status | B-0015: mehrere Hoch-Einträge (Survivorship-Bias, Identifiable-Victim-Replikationsversagen). Verifikationslücken bei Newton 1990/Bechky 1999 (unveröffentlichte Dissertationen). |
| Leitfadenreife | **A** für Konkretheit/Klarheit als Kommunikationsprinzip (P-0053, gut konvergent, geringes Risiko). **C** für "eine emotionale Einzelfallgeschichte schlägt Statistik" (Identifiable Victim Effect — Replikation gescheitert). **C** für SUCCESS als Gesamt-Framework (nur als Checkliste, nicht als getestetes System). |
| Empfohlene Claim-Stärke | "Konkret statt abstrakt kommunizieren" = starke Praxisregel. "Eine emotionale Einzelperson wirkt stärker als eine Statistik" = nicht verwenden als pauschale starke Regel — nur als Hintergrundwissen mit explizitem Replikationsvorbehalt. |
| Grenzen/Warnhinweise | Anekdoten-/Survivorship-Bias im Quellmaterial selbst (Buch benennt dies teils selbst als Zielkonflikt Simplizität vs. Genauigkeit). |
| Offene Anschlussfragen | Keine Meta-Analyse zu Curse of Knowledge oder Gap-Theorie der Neugier identifiziert. |

### 2.11 Sonstige Themen: Emotionale Intelligenz / Selbstregulation

| Feld | Inhalt |
|---|---|
| Tragende Objekte | MEC-0020 (Perspektivübernahme-Macht), MEC-0022 (Emotional Contagion); P-0039–P-0041, P-0044; T-0038, T-0039 |
| Quellenbasis | SRC-0011 (Emotional Intelligence/Goleman), Grant-Studien, Seligman/MetLife |
| Evidenzlage (einfach) | Die Konstruktvalidität von "Emotional Intelligence" selbst ist akademisch seit Jahrzehnten umstritten (Überlappung mit Big-Five-Persönlichkeitsdimensionen, Hoch) — **wichtiger Vorbehalt:** die drei dazu zitierten Standardreferenzen (Harms & Credé, Landy, Locke) stammen aus einem externen Gutachten und wurden nicht eigenständig websuchverifiziert. Der Marshmallow-Test zeigt bei Kontrolle für sozioökonomischen Status einen deutlich abgeschwächten Effekt (Watts, Duncan & Quan 2018, Hoch). Die Seligman/MetLife-Optimismus-Studie hat einen Autoren-Interessenkonflikt (Autor war Mitentwickler des Trainingsprogramms) — bewusst nicht zu einem eigenen P-Objekt erhoben. Emotional Contagion (MEC-0022) selbst ist unabhängig davon E3, gut konvergent belegt, mit reiner B2B-Transferlücke. |
| Scientific-Debt-Status | SRC-0011: mehrere Hoch-Einträge (Konstruktvalidität, Marshmallow-Replikationsabschwächung, Seligman-Interessenkonflikt). |
| Leitfadenreife | **C** für das EQ-Cluster insgesamt (Konstruktvaliditätsdebatte). **B** für Emotional Contagion speziell (eigenständig über Hatfield/Cacioppo/Rapson gestützt, unabhängig vom Goleman-EQ-Konstrukt). |
| Empfohlene Claim-Stärke | "Der emotionale Zustand des Verkäufers überträgt sich auf den Käufer" = plausible Arbeitshypothese. Generelle "EQ sagt Verkaufserfolg voraus"-Aussagen = nicht verwenden ohne Warnhinweis. |
| Grenzen/Warnhinweise | Konstruktvalidität von EQ umstritten; Seligman-Studie mit Interessenkonflikt. |
| Offene Anschlussfragen | Harms & Credé/Landy/Locke-Zitate noch nicht eigenständig verifiziert. |

### 2.12 Meta-Prinzipien (Cross-Book-Konvergenz, Sprint-1-Synthese)

| Feld | Inhalt |
|---|---|
| Tragende Objekte | P-S1-001 (Cost of Inaction), P-S1-002 (Mikro-Commitment-Sequenz), P-S1-003 (Problemzentrierung), P-S1-004 (Informationssparsamkeit) |
| Quellenbasis | Konvergenz aus B-0001, B-0002, B-0003, B-0004, B-0005 (jeweils 4–5 Bücher pro Meta-Prinzip) |
| Evidenzlage (einfach) | Jedes Meta-Prinzip kombiniert einen soliden Einzelmechanismus (meist E4/E5) mit einer zusätzlichen "methodologischen Konvergenz"-Komponente (E2) — die Konvergenz selbst erhöht die Plausibilität, ersetzt aber keine unabhängige Studie. |
| Scientific-Debt-Status | SD-SYS-003: Zirkelschlussrisiko — wenn Practitioner-Bücher sich gegenseitig zitieren oder auf denselben US-Corporate-Trainings-Zeitgeist reagieren, kann Konvergenz fälschlich wissenschaftliche Validität suggerieren. Kein Korrektiv-Mechanismus im aktuellen Wissensmodell vorhanden (Herausgeber-Entscheidung ausstehend, `OPEN_DECISIONS.md`). |
| Leitfadenreife | **B** — nützlich als Cross-Book-Muster für ein Einleitungskapitel, aber mit explizitem Hinweis auf das Zirkelschlussrisiko. |
| Empfohlene Claim-Stärke | "Mehrere unabhängige Vertriebsmethoden konvergieren auf X" = kontextabhängige Praxisregel, nicht "wissenschaftlich bewiesen". |
| Grenzen/Warnhinweise | Konvergenz ≠ unabhängige Replikation, solange das Zirkelschlussrisiko (SD-SYS-003) ungeklärt ist. |
| Offene Anschlussfragen | Mögliches Meme-Filter-Feld für QK-Objekte (Herausgeberentscheidung ausstehend). |

---

## 3. Leitfaden-ready First

Fünf bis acht Themenblöcke, die sich am besten eignen, um zuerst zu Leitfaden-Kapiteln ausgebaut zu werden — priorisiert nach Kombination aus hoher Evidenzreife, niedrigem/geklärtem Scientific-Debt-Risiko und geringer aktiver Kontroverse.

**1. Verhandlungsgrundprinzipien (Getting to Yes / Cluster 2.6)**
Warum zuerst: niedrigste Scientific-Debt-Priorität im gesamten Codex, institutionell seit Jahrzehnten erprobt, keine offene Kontroverse.
Tragende Objekte: MOD-0007, MEC-0017, P-0031–P-0034, T-0031–T-0034.
Erlaubte Claims: "Interessen statt Positionen fokussieren", "objektive Kriterien nutzen", "BATNA kennen und entwickeln" als starke Praxisregeln.
Zu vermeidende Claims: eine quantifizierte Überlegenheit gegenüber positionellem Feilschen (kein RCT vorhanden).

**2. Anchoring und Preisrahmung (Cluster 2.8, Kernteil)**
Warum zuerst: E5, eines der am robustesten replizierten Phänomene, sogar nach Publication-Bias-Korrektur bestätigt.
Tragende Objekte: MEC-0021, T-0040, T-0046, P-0042.
Erlaubte Claims: "Der erste genannte Wert prägt den weiteren Verhandlungsspielraum" als starke Praxisregel.
Zu vermeidende Claims: Verallgemeinerungen auf alle Anker-Subtypen ohne Differenzierung (bewusster/relevanter Anker vs. inzidenteller/dimensionsfremder Anker).

**3. Fairness-Schwelle (Cluster 2.8, Fairness-Teil)**
Warum zuerst: E4, durch AR-012 gerade erst kulturell präzisiert und von Hoch auf Mittel herabgestuft — aktuell so gut abgesichert wie selten im Codex.
Tragende Objekte: MEC-0025, P-0051.
Erlaubte Claims: "Ein Angebot unterhalb der Fairness-Schwelle riskiert Ablehnung trotz objektivem Vorteil" als starke Praxisregel.
Zu vermeidende Claims: pauschale Übertragbarkeit auf jede Kultur ohne den engeren, jetzt präzisierten Vorbehalt (extreme Marktferne, unerklärte Regionalvariation).

**4. Need Development / SPIN-Kern (Cluster 2.1, Kernteil)**
Warum zuerst: in sich konsistent, jahrzehntelang praktisch erprobt, Kernmechanismus (Verlustaversion) gut belegt.
Tragende Objekte: P-0001, P-0004, P-0005, T-0001–T-0004.
Erlaubte Claims: "Implizite Bedarfe müssen zu explizit artikulierten Bedarfen entwickelt werden" als kontextabhängige Praxisregel.
Zu vermeidende Claims: P-0002 ("Lösungswert folgt Problemgewicht") nicht als eigenständig starke Regel neben dem SPIN-Kern führen — Einzelquellenabhängigkeit benennen.

**5. Vertrauen als B2B-Erfolgstreiber (Cluster 2.4, Kernteil)**
Warum zuerst: durch aktuelle Meta-Analyse (Ohiomah et al. 2020) frisch gestärkt, breite Konvergenz.
Tragende Objekte: MEC-0030, MEC-0007, P-0012.
Erlaubte Claims: "Vertrauen ist einer der stärksten Einzelprädiktoren für B2B-Verkaufserfolg" als starke Praxisregel.
Zu vermeidende Claims: spezifische Cognitive-vs-Affective-Trust-Taktiken als getrennte, belastbare Techniken (Evidenz uneinheitlich); kein High-Ticket-B2C-Transfer.

**6. Cialdini-Grundprinzipien als Erklärungsraster (Cluster 2.7, Kernteil)**
Warum zuerst: die allgemeinen Mechanismen sind mit die bestbelegten im gesamten Codex (E4), auch wenn die B2B-Anwendung dünner belegt ist.
Tragende Objekte: MEC-0005–MEC-0009, MEC-0019, MOD-0002.
Erlaubte Claims: die sechs Prinzipien als Erklärungsmodell für Käuferverhalten, als starke Praxisregel.
Zu vermeidende Claims: einzelne B2B-Vertriebstechniken (T-0005–T-0011) nicht mit derselben Sicherheit formulieren wie den Erklärungsrahmen selbst; Hinweis auf ausstehende externe Validierung (OD-010-Terminologie beachten, siehe 2.7).

**7. Konkretheit und Klarheit in der Kommunikation (Cluster 2.10, Kernteil)**
Warum zuerst: E3/E4, geringes Kontroversrisiko, unmittelbar praktisch umsetzbar.
Tragende Objekte: MEC-0026, P-0053.
Erlaubte Claims: "Konkrete, sinnlich vorstellbare Sprache wird besser verstanden und erinnert als abstrakte" als starke Praxisregel.
Zu vermeidende Claims: den Identifiable-Victim-Effekt (Einzelfallgeschichte schlägt Statistik) nicht im selben Kapitel als gleichwertig sichere Regel führen (Replikation gescheitert).

**8. Informationssparsamkeit / kognitive Entlastung (Cluster 2.1 und 2.5, Querschnitt)**
Warum zuerst: auf Miller's Law gestützt, E5, eines der am wenigsten strittigen Prinzipien im Codex.
Tragende Objekte: P-S1-004, T-0022, MEC-0015 (Kernteil).
Erlaubte Claims: "Weniger, aber relevantere Information zur richtigen Zeit wirkt stärker als mehr Information" als starke Praxisregel.
Zu vermeidende Claims: die spezifische "6-Feature-Regel" nicht als empirisch optimierte Zahl darstellen (nur Miller's-Law-Herleitung, kein direkter Test des optimalen Feature-Counts in Sales-Demos).

---

## 4. Vorerst Nicht Übernehmen

Themen, die im Codex vorkommen, aber vorerst nicht in den ersten Leitfaden gehören.

**Challenger/CEB-Kennzahlen (53%/38%/9%-Split) als belastbare Fakten** — zu schwache Evidenz: proprietäre, nicht replizierte Studie, Publication-Bias-Kategorie 3. Die qualitative Grundlogik (Insight vor Lösung) ist unter 3.2 bereits als "später, mit Vorsicht" vorgesehen; die Zahlen selbst gehören nicht in einen ersten Leitfaden.

**JOLT/Tethr-Kennzahlen (44%/56%-Split) und die vier JOLT-Techniken als Gesamtsystem** — zu schwache Evidenz, identische Begründung (proprietäre ML-Klassifizierung, keine externe Replikation).

**Buying-Center-/Principal-Agent-Theoriecluster als eigenständiges Kapitel** — zu hoher Kontextabstand/noch blockierte Primärquelle: drei von vier zentralen Theoriequellen (Johnston & Lewin, Eisenhardt, Webster & Wind) sind blockiert; nur Sheth (1973) verarbeitet. Champion-/Konsens-Praxisregeln selbst können in andere Kapitel (z. B. Cluster 2.2/2.3 kurz) einfließen, aber kein eigenständiges, theoretisch fundiertes Kapitel vor Zugriffsklärung.

**Mirroring als durchgehende Dauertechnik** — aktiver, ungelöster wissenschaftlicher Widerspruch (Ireland & Henderson 2014 vs. Voss); zu früh für eine unqualifizierte Praxisregel.

**Emotionale Intelligenz (Goleman-Konstrukt) als eigenes Kapitel** — eher Hintergrund als Praxisregel: Konstruktvaliditätsdebatte seit Jahrzehnten ungeklärt, zitierte Standardreferenzen nicht eigenständig verifiziert.

**Identifiable-Victim-Effect / anekdotenlastige "Made to Stick"-Fallstudien als starke Regel** — zu schwache Evidenz: gescheiterte präregistrierte Replikation (2023), durchgängiges Survivorship-Bias-Risiko im Quellmaterial.

**Choice Architecture/Default-Effekt als pauschal starke Regel** — zu komplex/zu früh: aktive, ungelöste Publikationsbias-Kontroverse (SD-SYS-005); der Codex selbst hebt das Evidenzlevel bewusst nicht an, ein Leitfaden sollte hier nicht vorpreschen.

**Value-Based Selling** — explizit außerhalb Scope (ED-AR-8, 2026-07-14): primär B2B-Preisstrategie-Forschungsagenda ohne eigene Empirie, kein etabliertes Set käuferpsychologischer Mechanismen. Kein Codex-Objekt vorhanden, das aufgenommen werden könnte.

---

## 5. Blockierte Quellen und Nicht-Entscheidungen

### 5.1 Kanonische, aktive Wissensobjekte
Alle 57 Prinzipien, 30 Mechanismen, 47 Techniken und 12 Modelle in `03_knowledge_base/` sind aktiver, kanonischer Bestand (Status überwiegend "Entwurf" — kein Objekt trägt einen anderen Status als "Entwurf" oder leer; kein einziges Objekt ist im gesamten Bestand als "Validiert" markiert, was für T12-Publikationsarbeit relevant ist, siehe Abschnitt 7).

### 5.2 Scientific Debt (aktiv, dokumentiert, aber nicht blockierend)
Vollständig in `00_project/SCIENTIFIC_DEBT.md` geführt (B-0001 bis B-0015, SD-SYS-001 bis SD-SYS-006, W-001 bis W-004-Einträge). Die höchste-Priorität-Einträge sind: A-0019/SD-SYS-001 (CEB-Split, Hoch), B-0006 44%/56%-Split (Mittel-Hoch), MEC-0010/MEC-0011 Replikationsrisiko (Hoch), B-0012 Autoren-Integritätsrisiko Ariely (Hoch, "partially mitigated"), B-0015 Survivorship-Bias und Identifiable-Victim-Replikationsversagen (Hoch), SRC-0011 EQ-Konstruktvalidität (Hoch).

### 5.3 Blockierte Primärquellen (dauerhaft blockiert bis neue Zugriffslage, ED-AR-7)
- **Johnston & Lewin (1996)** — "Organizational buying behavior" (AR-003, SRC-0017). Kein legitimer Volltextzugriff gefunden.
- **Eisenhardt (1989)** — Agency Theory (AR-005, SRC-0027). Kein legitimer Volltextzugriff gefunden.
- **Webster & Wind (1972)** — Buying-Center-Theorie (Teil von AR-004, SRC-0026). Kein legitimer Volltextzugriff gefunden.
- **March & Simon (1958)**, *Organizations* — theoretisches Fundament Buying-Center-Cluster (AR-014, SRC-0039). Nur Controlled-Digital-Lending-Ausleihe ohne Download verfügbar.

Für alle vier gilt: mehrere legitime Zugriffswege geprüft, keine automatischen Wiederholungsversuche in künftigen Sprints; erneute Prüfung nur bei institutionellem Zugriff, Bibliotheks-/Archive.org-Zugang, Herausgeber-Bereitstellung oder neuem legitimen Open-Access-Fund.

### 5.4 Historische/archivierte Research-Artefakte
`06_research_program/completed/` (W001, W002, W003, W004, W008) — abgeschlossene Forschungsprojekte mit Editor Decisions, nicht rückwirkend editiert. Ihre offenen Anschlussfragen (OQ-x) sind zentral in `SCIENTIFIC_DEBT.md` weitergeführt. `99_archive/` — historisch, nicht aktiv geladen. `04_synthesis/SPR-0001_Sales_Core_Synthesis/contradiction_matrix.md` — Sprint-1-Artefakt, abgeschlossen, wird nicht rückwirkend editiert; neue Widersprüche werden in künftigen Synthese-Dokumenten geführt.

### 5.5 NSTD-Kandidaten (noch nicht formalisiert)
Aus `00_project/review_queue.md`:
- **Fusion-Kandidat MEC-0006/MEC-0014** — Herausgeberentscheidung ausstehend seit Sprint 1 (2026-07-01), zuletzt 2026-07-01 bestätigt weiterhin offen.
- **Meta-Prinzip-Kandidat "Asymmetrische Risikoverteilung im Buying Center"** — Kandidat, nicht angelegt, vollständiger Quervergleich mit A-0019/MEC-0014 aussteht.
- **MEC-Kandidat "Adaptive Selling Behavior"** (Franke & Park 2006) — nur Abstract-Ebene, kein Primärtextzugriff.
- **MEC-Kandidat "Elaboration Likelihood Model"** (Petty & Cacioppo 1986) — höchste Priorität unter den Literaturkandidaten, kein Primärtextzugriff.
- **MEC-Kandidat "Persuasion Knowledge Model"** (Friestad & Wright 1994) — kein Primärtext, keine neue Statement-Basis über MEC-0003 hinaus erkennbar.
- **MEC-Kandidat "Fairness/Equity Theory"** (Adams 1965, Thibaut & Walker 1975) — kein Primärtext; nicht zu verwechseln mit dem bereits bestehenden MEC-0025 (anderer theoretischer Ursprung, Sanfey/Ultimatum-Spiel statt Equity Theory).
- Hinweis: "Trust Formation" (Mayer, Davis & Schoorman 1995) war ursprünglich ebenfalls NSTD-Kandidat, ist aber durch W-003 inzwischen als MEC-0030 formal angelegt — dieser Punkt der review_queue ist damit überholt (nicht mehr NSTD).

### 5.6 Objekte, die nach ED-AR-Entscheidungen bewusst NICHT angelegt wurden
- Kein eigenständiges MEC "Principal-Agent-Risiko" (ED-AR-4, ED-AR-7) — mangels Primärtextzugriff auf Eisenhardt (1989).
- Keine neue P-Anlage aus den Sheth-Statements (ED-AR-5) — "Champion als interner Mobilizer" existiert bereits als P-0023, Stakeholder-Tailoring als T-0020.
- Kein neues SD-SYS-Querschnittsprojekt zu kultureller Generalisierung (ED-AR-9) — wird objektbezogen weitergeführt.
- Value-Based Selling bleibt außerhalb Scope (ED-AR-8) — derzeit, nicht dauerhaft; Wiedervorlage nur bei neuer Primärforschung oder expliziter Scope-Erweiterung.

---

## 6. Offene, aber nicht blockierende Fragen

- **OD-007** (Kontext-/Domänen-Modifikator-Ebene, CTX) — entscheidungsreif seit 2026-07-01, wartet auf Herausgeberwahl zwischen drei Optionen. Relevant für mehrere Cluster (insb. 2.2, 2.3), da eine CTX-Ebene beeinflussen würde, wie Boundary Conditions im Leitfaden strukturiert werden.
- **Fusion-Kandidat MEC-0006/MEC-0014** — offen, betrifft Cluster 2.3 und 2.7 (Social Proof extern vs. Konsens intern).
- **Meta-Prinzip "Asymmetrische Risikoverteilung im Buying Center"** — Kandidat, nicht formalisiert, betrifft Cluster 2.2/2.3.
- **W-001/OQ-2 bis OQ-5** — empirisch ungeklärte Restfragen aus dem Research Program, betreffen primär Cluster 2.2.
- **W-003/OQ-1 bis OQ-9** — Trust-Detailfragen, betreffen Cluster 2.4.
- **SD-SYS-003** (Zirkelschlussrisiko Meta-Prinzipien) — Herausgeberentscheidung zu einem möglichen Meme-Filter-Feld aussteht, betrifft Cluster 2.12.
- **OD-010-Terminologiebereinigung unvollständig** — nahe Varianten des "Gemini-Validierung ausstehend"-Platzhalters (u. a. MEC-0005–MEC-0008, A-0005, A-0006, A-0008, P-0003) wurden bei der OD-010-Bereinigung bewusst ausgeklammert; betrifft Cluster 2.7.
- **Programmweites additives Synthesemuster (R-1)** — laut `NEXT_ACTION.md` viertes bestätigtes Vorkommen (W-002/W-003/W-004/W-008), Editor-Autorisierung für eine programmweite Methoden-Review steht aus. Nicht direkt objektbezogen, aber relevant für die Art, wie künftige Leitfaden-Kapitel Kontroversen auflösen (Tendenz zu additiven Mittelpositionen wurde mehrfach beobachtet).

---

## 7. Empfehlung für nächsten Redaktionsschritt

Diese Übersicht ist eine Bestandsaufnahme, keine Umsetzung. Als nächster Schritt bieten sich aus Sicht der Redaktion an — ausdrücklich als Vorschlag, keine Herausgeberentscheidung vorwegnehmend:

Erstens könnte Felix aus der Liste "Leitfaden-ready First" (Abschnitt 3) die ein bis zwei Blöcke auswählen, mit denen der schlanke Leitfaden tatsächlich eröffnet werden soll — die acht genannten Blöcke sind nicht als gleichrangige Startpunkte gedacht, sondern als geordneter Vorschlag (Verhandlungsgrundprinzipien und Anchoring stehen an erster Stelle, weil sie die geringste Scientific-Debt-Last tragen).

Zweitens wäre eine kurze redaktionelle Konvention sinnvoll, bevor die erste Leitfaden-Kapitel geschrieben werden: eine einheitliche Regel, wie proprietäre Anbieter-Kennzahlen (53%/38%/9%, 44%/56%) im Leitfaden – falls überhaupt – gekennzeichnet werden, damit nicht jedes Kapitel diese Frage einzeln neu entscheidet. Das ist eine Framework-nahe Frage (Templates/Methodik) und liegt damit außerhalb des Scopes dieser Übersicht — sie wird hier nur als Beobachtung markiert, nicht entschieden.

Drittens: Kein im Codex-Bestand vorhandenes Objekt trägt aktuell den Status "Validiert" (alle 146 P-/MEC-/T-/MOD-Objekte stehen auf "Entwurf" oder haben ein leeres Statusfeld). T12 (Publikationsarbeit) verlangt laut `TASK_TYPES.md` ausdrücklich nur Objekte mit Status "Validiert" als Grundlage. Sollte der Leitfaden als T12-Publikationsarbeit im engeren Sinn behandelt werden, wäre vor Kapitelarbeit eine gesonderte Herausgeberentscheidung nötig, ob (a) der bestehende "Entwurf"-Status für Leitfadenzwecke ausreicht, oder (b) zunächst ein Validierungsschritt (VAL-Reports, T5) für die in Abschnitt 3 genannten Kernobjekte nachgeholt werden soll. Dies ist ausdrücklich eine Reserved Decision, keine Aufgabe für diese Session.

Viertens bleiben die in Abschnitt 6 gelisteten offenen, aber nicht blockierenden Fragen unabhängig vom Leitfadenprojekt bearbeitbar — sie müssen den Start der Leitfadenarbeit nicht verzögern, sollten aber nicht in Vergessenheit geraten.

---

*Erstellt: 2026-07-14 | Redaktionelle Bestandsaufnahme, keine Umsetzung | KI-Redaktion Sales Codex (Claude/Cowork) | Kein Commit, kein Push.*
