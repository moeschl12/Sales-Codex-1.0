# Research Agenda — SPR-0001

## Zweck

Priorisierte Forschungsagenda für Sprint 2. Grundlage: Alle offenen Fragen, Scientific Debt, ausstehende Validierungen und Widersprüche aus Sprint 1. Die Reihenfolge ist nicht alphabetisch oder nach Entstehungszeitpunkt — sie ist nach wissenschaftlichem Risiko und praktischer Relevanz für die Qualität des Sales Codex geordnet.

## Priorisierungs-Framework

**Tier 1 — Kritisch:** Muss vor Sprint 2-Buch-Eingabe gelöst oder eingeordnet werden; betrifft das Fundament des Wissensmodells  
**Tier 2 — Hoch:** Signifikante Lücke; sollte im nächsten Sprint adressiert werden  
**Tier 3 — Mittel:** Verbesserung der Wissensbasis; kann nach Büchern adressiert werden  
**Tier 4 — Niedrig:** Nice-to-have; verschiebbar

---

## TIER 1 — KRITISCHE FORSCHUNGSFRAGEN

### F-001 — W-001: Teach First vs. Diagnose First

**Quelle:** W-001 (contradiction_matrix.md)  
**Betroffene Objekte:** A-0020, P-0021, P-0025, MEC-0013, T-0019, T-0023

**Frage:** Unter welchen Bedingungen liefert Discovery-First (Gap Selling) vs. Insight-First (Challenger Sale) bessere Verkaufsergebnisse?

**Warum Tier 1:** Dies ist der einzige ungelöste methodologische Widerspruch des Sprints. Solange er offen ist, kann kein kohärentes Verkaufsmodell (MOD-S1) erstellt werden. Verkäufer, die den Sales Codex anwenden, erhalten widersprüchliche Handlungsanweisungen.

**Mögliche Forschungswege:**

1. **Meta-Analyse:** Gibt es publizierte Studien zu "Insight-First Selling" vs. "Needs-Based Selling"? Suchbegriffe: "consultative selling vs. insight selling", "SPIN vs. Challenger", "discovery-led sales", Rackham + Dixon Vergleich.

2. **Dritte-Quelle-Prüfung:** Gibt es ein drittes Buch, das dieselbe Frage adressiert? Kandidaten: "The JOLT Effect" (Matthew Dixon, 2022 — Status Quo Bias als Gegenpol zu Challenger?), "Fanatical Prospecting" (Blount), "Sell the Way You Buy" (Priemer).

3. **Situationsmodell:** Entwickle ein Hypothesen-Situationsmodell:
   - Käufer kennt Problem, sucht Lösung → Diagnose First effizienter?
   - Käufer erkennt Problem noch nicht → Insight First effizienter?
   - Dokumentiere als H-001 in der Wissensbasis, wenn keine Primärquelle gefunden.

**Deliverable:** Entweder: F-001 geschlossen durch Primärquelle. Oder: H-001 als explizite, nicht gesicherte Hypothese angelegt.

---

### F-002 — Externe Validierung MEC-0010 und MEC-0011 (Voss-Neurowissenschaft)

**Quelle:** Scientific Debt B-0003 (SCIENTIFIC_DEBT.md); canonicalization_report.md Abschnitt 2.3  
**Betroffene Objekte:** MEC-0010, MEC-0011

**Frage:**
- MEC-0010: Gibt es neurowissenschaftliche Belege für Amygdala-Regulation durch Labeling, die über Voss' Behauptungen hinausgehen?
- MEC-0011: Spiegelneuronen-Hypothese — ist sie nach aktuellem Stand der Neurowissenschaft haltbar?

**Warum Tier 1:** MEC-0011 wurde in canonicalization_report.md als "zu unsicher für eigenständiges MEC-Objekt" eingestuft. Wenn die Spiegelneuronen-Hypothese widerlegt ist, muss MEC-0011 aufgelöst oder zurückgestuft werden. MEC-0010 ist die Grundlage mehrerer Voss-Techniken (P-0016, T-0013, T-0014) — wenn MEC-0010 schwach ist, verlieren diese Techniken ihre mechanistische Begründung.

**Mögliche Forschungswege:**

1. **Gemini-Review MEC-0010:** Prompt-Vorschlag: "Gibt es neurowissenschaftliche Peer-Review-Evidenz (z.B. Lieberman et al., affect labeling Studien) für die Behauptung, dass Verbalisierung von Emotionen die Amygdala-Aktivierung reduziert? Wenn ja: Qualität der Evidenz? Wenn nein: Was ist bekannt?"

2. **Gemini-Review MEC-0011:** Prompt-Vorschlag: "Wie ist der aktuelle wissenschaftliche Konsens zu Spiegelneuronen beim Menschen? Ist die ursprüngliche Behauptung (MN erklären Empathie/Mimikry) repliziert? Gibt es eine Rizzolatti-kritische Literatur?"

3. **Entscheidungsmatrix nach Review:**
   - MEC-0010 bestätigt → behalten, E-Level update
   - MEC-0010 nicht bestätigt → als E1-Hypothese rückstufen, Techniken-Objekte anpassen
   - MEC-0011 bestätigt → behalten
   - MEC-0011 widerlegt → MEC-0011 in MEC-0010 integrieren oder als "(veraltet)" markieren

**Deliverable:** MEC-0010 und MEC-0011 mit aktualisiertem E-Level und Primärquellen-Referenz.

---

## TIER 2 — HOHE PRIORITÄT

### F-003 — Externe Validierung Cialdini-MECs (Verkaufskontext)

**Quelle:** Scientific Debt B-0002 (SCIENTIFIC_DEBT.md); evidence_upgrade_report.md Abschnitt 5  
**Betroffene Objekte:** MEC-0005–MEC-0009

**Frage:** Sind die sechs Cialdini-Mechanismen im B2B-Komplex-Verkaufskontext mit vergleichbarer Stärke repliziert worden?

**Warum Tier 2:** Die fünf MECs haben E4 (gut repliziert im Labor), aber fast alle Studien wurden in Konsumgüter-Compliance-Kontexten durchgeführt. B2B-Komplex-Verkauf mit 5,4 Entscheidern, Due-Diligence-Prozessen und langen Zyklen ist grundlegend verschieden. Der Transfer ist plausibel aber nicht bestätigt.

**Mögliche Forschungswege:**

1. **Gemini-Review MEC-0005 (Reziprozität) in B2B:** "Gibt es Feldstudien zu Reziprozitäts-Effekten im B2B-Vertrieb oder Procurement?"
2. **Gemini-Review MEC-0006 (Social Proof) in B2B:** "Wie wirkt Social Proof in langen B2B-Entscheidungsprozessen mit mehreren Entscheidern?"
3. **Sonderfall MEC-0007 (Liking):** W-002 ist noch teilaufgelöst. MEC-0007 ist gleichzeitig der Cialdini-MEC mit der stärksten Kontraindikation aus anderen Sprint-1-Büchern (A-0018). Priorität: höchste unter den Cialdini-MECs.

**Deliverable:** Für jeden MEC: "Bestätigt für B2B", "Nicht repliziert", oder "Kontextgebunden ab X" mit Quelle.

---

### F-004 — Fusions-Kandidaten: MEC-0006/MEC-0014 und MEC-0010/MEC-0012

**Quelle:** canonicalization_report.md Abschnitt 2.3  
**Betroffene Objekte:** MEC-0006, MEC-0014, MEC-0010, MEC-0012

**Frage:**
- MEC-0006 (Social Proof) + MEC-0014 (Konsens als Kaufsicherheit): Sind das zwei Mechanismen oder ein Mechanismus in zwei Kontexten?
- MEC-0010 (Amygdala-Regulation) + MEC-0012 (Dual Process): Überlappen sie genug für eine Zusammenführung?

**Warum Tier 2:** Fragmentierung der MECs erhöht die Pflegekosten des Codex und schwächt die Eindeutigkeit von Verweisen aus P- und T-Objekten.

**Mögliche Forschungswege:**

1. Vergleiche beide MEC-Paare auf Mechanismusebene: Wenn der psychologische Wirkpfad identisch ist, fusionieren. Wenn verschieden, behalten.
2. Kriterium: Hätte man in einem anderen Kontext (nicht Verkauf) auch zwei verschiedene Mechanismen beschrieben?

**Deliverable:** Entscheidung "Fusion" oder "Beibehaltung" mit schriftlicher Begründung pro Paar. Wenn Fusion: Überarbeitete MEC-Datei.

---

### F-005 — W-002: Liking-Schwelle in B2B (Hygienefaktor-Hypothese)

**Quelle:** W-002 (contradiction_matrix.md)  
**Betroffene Objekte:** MEC-0007, A-0018, A-0029

**Frage:** Gibt es eine messbare Komplexitätsschwelle, ab der MEC-0007 (Liking) von Expertise als Kauftreiber abgelöst wird? Oder gilt: Liking als Basis-Hygienefaktor, Expertise als Differenzierer?

**Warum Tier 2:** Betrifft die Handlungsrelevanz der A-0018-Kontextgrenzen und das Design von T-Objekten (Credibility-Techniken vs. Rapport-Techniken).

**Mögliche Forschungswege:**

1. Suchbegriff: "buyer loyalty complexity threshold" + "sales effectiveness"
2. Cialdini-Primärliteratur: Gibt es Studien, die Liking-Effekte nach Komplexität differenzieren?
3. CEB-Daten: Gibt es in der originalen Challenger Sale Forschung eine Kontrollvariable "Liking des Verkäufers"?

**Deliverable:** W-002 entweder von "Teilaufgelöst" auf "Kontextgebunden" upgraden (mit Quelle) oder auf "Ungelöst" rückstufen.

---

## TIER 3 — MITTLERE PRIORITÄT

### F-006 — Langer-Xerox Replikationsstatus (MEC-0001)

**Quelle:** Scientific Debt B-0001 (SCIENTIFIC_DEBT.md)  
**Betroffene Objekte:** MEC-0001 (Selbstverbalisierung)

**Frage:** Ist das klassische Langer-Xerox-Experiment (1978) — "May I use the Xerox machine because I need to make copies?" — repliziert worden? Gilt "because" als inhaltsleer noch?

**Mögliche Forschungswege:** Suche nach Replikationsstudien zu Langer 1978. Stichwörter: "mindless compliance", "Langer Xerox replication", "because heuristic".

**Deliverable:** E-Level-Update für MEC-0001 oder Bestätigung des aktuellen Status.

---

### F-007 — Rackham SPIN-Primärstudie — Designdetails

**Quelle:** Scientific Debt B-0001 (SCIENTIFIC_DEBT.md)  
**Betroffene Objekte:** MEC-0001, T-0001–T-0004, P-0002

**Frage:** Waren die 35.000 SPIN-Verkaufsgespräche verblindete Beobachtungen, oder war der Rater über die Verkäuferleistung informiert? Gibt es eine Beschreibung der Erfolgskriterien?

**Mögliche Forschungswege:** Rackham's "Making Major Sales" (1987) als Primärquelle; akademische Methodenkritik.

**Deliverable:** Ergänzung der Methodengrenzen in SRC-0001; E-Level-Kommentar für MEC-0001.

---

### F-008 — Rapport als Hygienefaktor — Hypothesen-Formalisierung

**Quelle:** emerging_principles.md (Kandidat X, negativer Befund)  
**Betroffene Objekte:** MEC-0007, A-0018, A-0029

**Frage:** Ist es modellierbar, dass Rapport/Sympathie notwendige, aber nicht hinreichende Bedingung für B2B-Käufe ist? Falls ja: Unter welchen Bedingungen verschiebt sich das Verhältnis?

**Mögliche Forschungswege:** Primärliteratur zu "dual-process buying" + "trust in B2B". Alternativ: Kann aus Cialdini + Challenger + Gap Selling ein Hypothesen-Statement (H-001) formuliert werden, das für Sprint 2-Bücher testbar ist?

**Deliverable:** Wenn Primärquelle gefunden: A-Objekt; wenn nicht: H-001 als explizit spekulatives Statement mit Prüfanforderung.

---

### F-009 — 6-Feature-Regel: Empirische Basis jenseits von Miller's Law

**Quelle:** Scientific Debt B-0005 (SCIENTIFIC_DEBT.md)  
**Betroffene Objekte:** T-0022 (Gap-Demo-Methode), MEC-0015

**Frage:** Ist die "max. 6 Features" Regel im Demo-Kontext empirisch belegt, oder ist das eine Extrapolation aus Miller's Law (1956) auf B2B-Demo-Situationen?

**Mögliche Forschungswege:** Suchbegriff: "cognitive load sales demo", "feature overload B2B". Miller's Law 1956 nochmals auf ursprüngliche Claim-Präzision prüfen (7±2 vs. 4±1 neuere Updates).

**Deliverable:** MEC-0015 E-Level-Kommentar aktualisieren; T-0022 Kontextgrenzen-Abschnitt ergänzen.

---

## TIER 4 — NIEDRIGE PRIORITÄT / VERSCHIEBBAR

### F-010 — Sprint 1 Meta-Analyse: Verkaufsforschung 2019–2025

**Frage:** Was ist seit den Sprint-1-Büchern (neuestes: Gap Selling 2018) an empirischer Verkaufsforschung erschienen?

**Mögliche Forschungswege:** Google Scholar: "B2B sales", "consultative selling", "sales effectiveness" 2019–2025. Insbesondere: Replikationen von CEB-Daten (Dixon), Rackham-Updates.

**Deliverable:** Kurznotiz für SESSION_LOG.md; ggf. neue Bücher für Sprint 3.

---

### F-011 — Cialdini: Pre-Suasion (2016) als Ergänzungsquelle

**Frage:** Liefert "Pre-Suasion" (Cialdini, 2016) relevante Zusatzevidenz für MEC-0005–0009, insbesondere im Kontext B2B-Aufmerksamkeitssteuerung?

**Relevanz für bestehende Objekte:** MEC-0005 (Reziprozität), P-0008 (Trigger-Design-Primat), ST-0148 (Gap Prospecting)

**Empfehlung:** Kandidat für Sprint 3 (Vertiefungs-Sprint), nicht Sprint 2.

---

### F-012 — Challenger Sale CEB-Daten: Vollständige Rohdaten verfügbar?

**Frage:** Sind die CEB-Befragungsdaten (N=6.000, A-0018, A-0022) öffentlich zugänglich oder in akademischen Zeitschriften publiziert?

**Mögliche Forschungswege:** Gartner/CEB Website; Dixon + Adamson Google Scholar-Profil; Harvard Business Review Artikel.

**Deliverable:** Quellenangabe für A-0018 verbessern; Replikation für A-0022 suchen.

---

## BUCHEMPFEHLUNGEN FÜR SPRINT 2

Kriterien: (1) Direkte Relevanz für W-001; (2) Empirische Stärke; (3) Neue Perspektiven, die Sprint-1-Konvergenz herausfordern könnten

| Rang | Titel | Autor | Jahr | Relevanz |
|---|---|---|---|---|
| 1 | The JOLT Effect | Matthew Dixon | 2022 | Status Quo Bias vs. COI; direkte Adressierung von W-001 (Dixon ist Challenger-Koautor — würde er jetzt Diagnose First empfehlen?) |
| 2 | Fanatical Prospecting | Jeb Blount | 2015 | Problem-zentrierung in Outreach; Test von P-S1-003; Gap-Prospecting-Parallelität |
| 3 | The Psychology of Selling | Brian Tracy | 2004 | Practitioner-Klassiker; Test ob MEC-0002/MEC-0004 als universal bestätigt werden |
| 4 | Sell the Way You Buy | David Priemer | 2020 | Käuferperspektive + Neurowissenschaft; Test von MEC-0010 aus nicht-Voss-Quelle |
| 5 | Predictable Revenue | Aaron Ross | 2011 | Outbound-Spezifika; Ergänzung zu ST-0148 (Gap Prospecting) |

**Priorisierungs-Begründung:** The JOLT Effect hat höchste Priorität, weil Dixon als Challenger-Koautor eine Position zu W-001 haben könnte, die entweder die Synthese auflöst oder den Widerspruch vertieft. Beide Szenarien sind für den Codex wertvoll.

---

## AGENTA ZUSAMMENFASSUNG

| ID | Titel | Tier | Typ |
|---|---|---|---|
| F-001 | W-001 Teach vs. Diagnose First | 1 | Widerspruch |
| F-002 | MEC-0010/MEC-0011 Validierung | 1 | Scientific Debt |
| F-003 | Cialdini-MECs im B2B-Kontext | 2 | Scientific Debt |
| F-004 | MEC-Fusions-Kandidaten | 2 | Canonicalization |
| F-005 | W-002 Liking-Schwelle | 2 | Widerspruch |
| F-006 | Langer-Xerox Replikationsstatus | 3 | Scientific Debt |
| F-007 | Rackham SPIN Methodendetails | 3 | Scientific Debt |
| F-008 | Rapport als Hygienefaktor | 3 | Offene Frage |
| F-009 | 6-Feature-Regel Empirie | 3 | Scientific Debt |
| F-010 | Verkaufsforschung 2019–2025 | 4 | Meta-Analyse |
| F-011 | Pre-Suasion als Ergänzung | 4 | Buchkandidat |
| F-012 | CEB-Rohdaten Verfügbarkeit | 4 | Quellenprüfung |

**Sprint 2 empfohlener Startpunkt:** F-002 (Gemini-Review MEC-0010/MEC-0011) und F-003 (Gemini-Review Cialdini-MECs in B2B), weil beide schnell mit externen KI-Reviews abgearbeitet werden können und das Fundament für Buchauswahl klären.

Dann: Nächstes Buch beginnen (Empfehlung: The JOLT Effect), während F-001 durch den Buchinhalt beantwortet werden könnte.

## Status

Abgeschlossen — 2026-07-01
