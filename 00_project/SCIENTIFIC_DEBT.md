# Scientific Debt — Sales Codex

**Dokumentklasse: Operational**  
Version: 1.0  
Stand: 2026-06-30  
Analogie: Technische Schulden in der Softwareentwicklung

---

## Konzept

Scientific Debt bezeichnet Wissensobjekte oder Behauptungen im Sales Codex, bei denen die Evidenzbasis bekanntermaßen unvollständig ist — und die für eine spätere Validierung vorgemerkt sind.

Ein Objekt mit Scientific Debt ist nicht falsch. Es ist unvollständig gesichert. Es wird im Repository behalten und genutzt, aber seine Einschränkungen sind explizit dokumentiert.

---

## Kategorien

| Kategorie | Definition |
|---|---|
| **Replikationsrisiko** | Studie existiert, aber Replikationsstatus unklar oder negativ |
| **Externe Validierung ausstehend** | Gemini- oder Perplexity-Prüfung noch nicht durchgeführt |
| **Unbelegte Annahme** | A-Objekt ohne direkte Primärquelle; aus Schlussfolgerungen abgeleitet |
| **Widersprüchliche Evidenz** | Zwei Quellen widersprechen sich; kein Urteil möglich |
| **Offene Forschungsfrage** | Bekannte Lücke; kein Beleg vorhanden |
| **Kulturelle Generalisierung** | Befund aus einer Population; Übertragbarkeit ungesichert |
| **Publication Bias (kommerzielle Studien)** | Studie stammt von einem Anbieter/Consulting-Haus mit kommerziellem Interesse an einem positiven Ergebnis; selektive Publikation nicht auszuschließen (neu: ARS-0001, Peer Review Sprint 2) |

---

## Tracking

### B-0001 — SPIN Selling (SRC-0001)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| P-0001–P-0007 | Externe Validierung ausstehend | Gemini-Validierung der SPIN-Mechanismen gegen aktuelle Forschung | Mittel |
| MEC-0001–MEC-0004 | Externe Validierung ausstehend | Replikationsstatus der zugrundeliegenden Studien ungeprüft | Mittel |
| MOD-0001 | Offene Forschungsfrage | SPIN vs. Challenger Sale: Methodik-Vergleich ausstehend | Niedrig |

### B-0002 — Influence (SRC-0002)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MEC-0005–MEC-0009 | Externe Validierung ausstehend | Gemini-Validierung gegen aktuelle Sozialpsychologie | Hoch |
| ST-0033 (Langer-Xerox) | Replikationsrisiko | Replikationsstatus der Xerox-Studie in Replikationskrise unklar | Hoch |
| ST-0035 (Regan-Studie) | Replikationsrisiko | Replikationsstatus des Reziprozitätsexperiments ungeprüft | Mittel |
| A-0007 | Unbelegte Annahme | Evolutionäre Verankerung der Compliance-Prinzipien — keine direkte Primärquelle | Niedrig |
| P-0009, P-0012 | Offene Forschungsfrage | B2B-spezifische Reziprozitäts- und Rapport-Belege fehlen | Mittel |
| MEC-0009 vs. MEC-0002 | Widersprüchliche Evidenz | Abgrenzung Perzeptueller Kontrast vs. Verlustaversion in Grenzfällen unklar | Niedrig |

---

### B-0003 — Never Split the Difference (SRC-0003)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MEC-0010 | Externe Validierung ausstehend | Lieberman (2007): Transfer Lab→Gespräch unbelegt; Fremd-Labeling nicht direkt getestet (RQ-0010-1, RQ-0010-2) | **Hoch** |
| MEC-0011 | Externe Validierung ausstehend | Stephens/Hasson (2010): Transfer passives Zuhören→aktives Mirroring unbelegt; Spiegelneuronen-Claim umstritten (RQ-0011-3, RQ-0011-4) | **Hoch** |
| MEC-0011 | Replikationsrisiko | Spiegelneuronen-Verbindung zu menschlicher sozialer Kognition ist wissenschaftlich kontrovers | **Hoch** |
| MEC-0012 | Externe Validierung ausstehend | What/How vs. Why Framing-Effekt auf Verarbeitungstiefe nicht direkt belegt; MacLean-Triune-Brain überholt | Mittel |
| A-0016 | Unbelegte Annahme | "≥3 Black Swans in jeder Verhandlung" — Voss-Daumenregel ohne empirische Basis; E1 | Niedrig |
| ST-0088 | Kulturelle Generalisierung | "Why ist immer eine Anklage" — universell behauptet, keine kulturvergleichende Evidenz | Niedrig |
| ST-0094 | Widersprüchliche Evidenz | Mehrabian 7-38-55: Originalstudie betrifft inkonsistente Kommunikation/Einstellungen, nicht allgemeine Gesprächsgewichtung | Mittel |

**Sprint-Dokument:** `00_project/VALIDIERUNGSSPRINT_MEC0010-0012.md`

---

### B-0004 — The Challenger Sale (SRC-0004)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| A-0023 | Unbelegte Annahme | TTC-Trainierbarkeit: keine Längsschnittdaten zu Trainingseffekten auf Challenger-Profil-Attributen publiziert; E2 | Mittel |
| MEC-0013 | Externe Validierung ausstehend | Insight-Disruption: kognitive Dissonanz (E4) gut belegt, aber spezifische Challenger-Anwendung im Verkaufsgespräch nicht RCT-getestet | Mittel |
| MEC-0014 | Offene Forschungsfrage | Konsens als Kaufsicherheit: B2B-spezifische Mechanismus-Forschung fehlt; aus Gruppenentscheidungspsychologie hergeleitet, aber nicht direkt belegt | Mittel |
| A-0019 | Replikationsrisiko | 53%/38%/9%-Split: CEB-Methodik nicht publiziert; keine externe Replikation der Loyalitäts-Attribut-Verteilung bekannt | Hoch |
| MOD-0004 | Externe Validierung ausstehend | TTC-Modell als integriertes System: Challenger-Profil-Befund belegt das Gesamt-Profil, nicht die sequentielle Wirkung von Teach→Tailor→Take Control als eigenständige Elemente | Mittel |
| MOD-0004 | Kulturelle Generalisierung | CEB-Studie primär US/westlicher Enterprise-B2B-Kontext; Übertragbarkeit auf andere Kulturen und SMB-Märkte ungeprüft | Niedrig |
| MOD-0001 vs. MOD-0004 | Widersprüchliche Evidenz | SPIN Diagnose-Primat (MEC-0001, MEC-0004) vs. Challenger Insight-Primat (MEC-0013): kein direkter Vergleichsstudie; beide proprietäre Methoden | Mittel |

---

### B-0005 — Gap Selling (SRC-0005)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MOD-0005, P-0025, P-0026 | Offene Forschungsfrage | Gap-Selling-Methodik als Ganzes: kein RCT oder Wirksamkeitsstudie; Keenan-Behauptungen anekdotisch und proprietär | Mittel |
| A-0020 vs. P-0025 | Widersprüchliche Evidenz | Challenger "Teach First" vs. Gap Selling "Diagnose First": kein Direktvergleich; fundamentaler Methodologiekonflikt ungelöst | **Hoch** |
| A-0029 | Offene Forschungsfrage | Credibility-Entstehung: Wie genau wird Expertise durch den Käufer attribuiert? Wann reicht Diagnose-Tiefe, wann braucht man proaktive Insights? | Mittel |
| T-0022, MEC-0015 | Offene Forschungsfrage | 6-Feature-Demo-Regel: Miller's Law ist gut belegt (E5), aber der optimale Feature-Count für Sales Demos ist empirisch nicht gemessen | Niedrig |

---

### B-0006 — The JOLT Effect (SRC-0006)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| ST-0151, MOD-0006 | Offene Forschungsfrage | 44%/56%-Split (Status quo vs. Indecision): Klassifizierungsmethodik der Tethr-ML-Analyse nicht offengelegt; keine externe Replikation | Mittel |
| MEC-0016, A-0031 | Externe Validierung ausstehend | FOMU als primärer Indecision-Treiber: konzeptuell fundiert (antizipatorische Reue), aber kausaler Nachweis im B2B-Kaufkontext fehlt | Mittel |
| T-0026–T-0030, MOD-0006 | Kulturelle Generalisierung | Alle JOLT-Techniken basieren auf US-COVID-Daten (2020–2021); Übertragbarkeit auf Präsenz-Verkauf, Post-COVID, Nicht-US-Märkte ungetestet | Niedrig |

---

### B-0008 — Pre-Suasion (SRC-0008)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MEC-0018, MOD-0008 | Externe Validierung ausstehend | B2B-Übertragbarkeit der Pre-Suasion-Laborbefunde nicht direkt gemessen; Privileged-Moment-Dauer in realen Verkaufsgesprächen unbekannt | Mittel |
| MEC-0019, ST-0181 | Externe Validierung ausstehend | Unity-Kapitel am wenigsten extern repliziert; Cialdinis theoretische Synthese aus Social Identity Theory, Aron IOS und Synchronie-Forschung — Sales-spezifische Anwendung E2 | Niedrig |

---

### B-0007 — Getting to Yes (SRC-0007)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| A-0039, MOD-0007 | Externe Validierung ausstehend | Principled Negotiation vs. positionelles Feilschen: Kein RCT-Vergleich; institutionell gut belegt aber empirische Überlegenheit nicht direkt gemessen | Niedrig |
| MEC-0017 | Offene Forschungsfrage | Fixed-Pie Fallacy in B2B-Sales-spezifischem Kontext (Preisverhandlung nach Pitch): nicht direkt gemessen; Thompson (1990) ist allgemeine Verhandlungsforschung | Niedrig |

---

### B-0010 — Thinking, Fast and Slow (SRC-0010)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MEC-0018, ST-0179 | Replikationsrisiko | Priming-Forschung aus Kahneman Kap. 4: mehrere Priming-Studien (Bargh etc.) sind in der Replikationskrise nicht standgehalten. Kahneman hat dies 2012 öffentlich anerkannt. MEC-0018 (Pre-Suasion/Priming) und ST-0179 (Assoziativität) sind tangiert | **Hoch** |
| ST-0195, MEC-0021, T-0040 | Transferlücke | B2B-Sales-Transfer: Anchoring, Cognitive Ease und Framing in Lab und Consumer-Kontext E5; in professionellen B2B-Einkaufsprozessen mit erfahrenen Entscheidern schwächer belegt | Mittel |
| ST-0200 | Offene Forschungsfrage | Expert Intuition in Enterprise Sales: Kahneman/Klein-Framework für traditionelle Expertise-Domänen entwickelt; Gültigkeitsbedingungen in langen B2B-Zyklen (6–18 Monate, multikausale Entscheide) nicht direkt gemessen | Niedrig |

---

### B-0009 — To Sell Is Human (SRC-0009)

| Objekt-ID | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| ST-0193, T-0039, A-0046 | Offene Forschungsfrage | Improv-Transfer auf Sales (A-0046): kein RCT; Wirksamkeit von Yes-And-Training auf Verkaufsleistung empirisch nicht gemessen | Niedrig |
| ST-0189, MEC-0020 | Replikationsrisiko | Ambivert-Vorteil (Grant): Einzelstudie im Call-Center-Kontext; Replikation in komplexen B2B-Verkaufssituationen fehlt | Mittel |
| A-0045, ST-0192 | Offene Forschungsfrage | Prosoziale Motivation vs. Eigennutz langfristig: Grant-Studie zeigt kurzfristige Aktivierungseffekte; dauerhafte Überlegenheit prosozialer Motivation gegenüber Eigennutzmotivation nicht longitudinal belegt | Mittel |

---

### Peer Review Sprint 1 — Systemische Scientific Debt (neu 2026-07-01)

**Hinweis:** Die folgenden Einträge entstammen dem Peer Review von SCRP-0001 (2026-07-01). Sie ergänzen die buchspezifischen Einträge oben um systemische Querschnittsrisiken.

#### SD-SYS-001 — Proprietäre Studien ohne unabhängige Peer-Review-Replikation

| Betroffene Objekte | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| ST-0001 bis ST-0023 (SPIN/Huthwaite-Basis) | Replikationsrisiko | Huthwaites Feldbeobachtungen (N=35.000 Verkaufsgespräche) sind proprietär. Rohdaten, Faktorladungen und Signifikanztests nicht öffentlich einsehbar. Kein akademisches Peer-Review-Verfahren nachgewiesen. Betrifft alle Objekte, die exklusiv auf Huthwaite-Daten ohne unabhängige Stützquelle zurückgreifen. | **Hoch** |
| ST-0107 bis ST-0132 (CEB/Challenger-Basis) | Replikationsrisiko | CEB-Befragungsstudie (N=6.000) für Challenger Sale: proprietär, keine öffentlichen Rohdaten. Das 53%-Loyalitätsergebnis (A-0019), die 5-Profile-Verteilung (ST-0108 ff.) und die Krisenverkäufer-Befunde sind nicht peer-reviewed repliziert. Betrifft alle Objekte, die exklusiv auf diesen Daten beruhen. | **Hoch** |
| A-0019, P-S1-003 | Offene Forschungsfrage | Verbeke, Dietz & Verwaal (2010/2011): Akademische Meta-Analyse zu Vertriebsleistungstreibern (JAMS 39(3), 407–428) — **geprüft in ARS-0001/Research Pack 1 (2026-07-01), siehe unten**. Ergebnis: Meta-Analyse bestätigt NICHT die CEB-53%-Loyalitätsbehauptung (A-0019) — unterschiedliche Analyseebene (Individual-Determinanten-Regression vs. Organisations-Loyalitätsumfrage). A-0019 bleibt ungestützt durch unabhängige Replikation. | Mittel |

**Maßnahme Sprint 2:** Individuelle Prüfung jedes betroffenen Objekts, ob zusätzliche unabhängige Stützquellen vorhanden sind, die E3 rechtfertigen. Falls nicht: E-Level-Herabstufung auf E2.

#### SD-SYS-002 — B-0005 Gap Selling Quellenunvollständigkeit

| Betroffene Objekte | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MOD-0005, alle B-0005-Objekte | Offene Forschungsfrage | B-0005 (Gap Selling) wurde auf Basis einer partiellen Quelle analysiert. Fehlende Kapitel können Aussagen enthalten, die bestehende Objekte modifizieren oder widersprechen. Der aktuelle Status ist: Extraktion unter Quellenvorbehalt. | **Hoch** |

**Maßnahme:** Vollständige Quelle beschaffen. Bis dahin gilt für alle B-0005-Objekte ein impliziter Vollständigkeitsvorbehalt.

#### SD-SYS-003 — Zirkelschlussrisiko bei QK-Ratings durch Meme-Replikation

| Betroffene Objekte | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| P-S1-001 bis P-S1-004 (QK-4/5) | Widersprüchliche Evidenz | Der Reviewer identifiziert ein methodologisches Risiko: Wenn Practitioner-Bücher gegenseitig aufeinander verweisen oder auf denselben US-Corporate-Training-Zeitgeist reagieren, suggeriert QK-Konvergenz fälschlicherweise wissenschaftliche Validität. Kein Korrektiv-Mechanismus im aktuellen Wissensmodell vorhanden. | Mittel |

**Maßnahme (Herausgeber-Entscheidung ausstehend):** Mögliche Einführung eines Meme-Filter-Feldes für QK-Objekte — dokumentiert in OPEN_DECISIONS.md.

---

### Academic Recovery Sprint (ARS-0001) — Research Pack 1 (2026-07-01)

**Hinweis:** Die folgenden Einträge entstehen aus der Verarbeitung von "Research Pack 1" im Rahmen von ARS-0001 (Academic Recovery Sprint). Alle Quellen wurden vor Integration per Websuche verifiziert (Autoren, Jahr, Journal, DOI/Fundstelle). Details, Einzelbewertung pro Quelle und vollständige Zitationen: `00_project/ACADEMIC_RECOVERY_REPORT.md`.

**Wichtiger methodischer Hinweis:** Keine der folgenden Quellen wurde in einen neuen MEC/P/T-Objekt-Vollprozess (Schritt 1–9 Operating Manual) überführt. Für alle Quellen liegt nur Abstract-/Sekundärebene vor (Websuche), kein Volltext-Zugriff. Eine formale Objekterstellung (neues MEC „Adaptive Selling" o.ä.) erfordert Primärtext-Extraktion nach Standardprozess — das ist ausdrücklich **nicht** in diesem Schritt erfolgt, um den Nachvollziehbarkeits-Standard (Abschnitt 4 Operating Manual) nicht zu verletzen. Die Quellen werden daher als **ergänzende, dokumentierte Literaturreferenzen** an bestehenden Objekten geführt — nicht als neue Wissensobjekte.

| Betroffene Objekte | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MEC-0014, W-001/Problemreife-Hypothese | Offene Forschungsfrage → teilweise adressiert | Franke & Park (2006), *Salesperson Adaptive Selling Behavior and Customer Orientation: A Meta-Analysis*, JMR 43(4), 693–702 (155 Samples, N>31.000): Adaptive Selling Behavior (ASB) erhöht objektive und Fremdrating-Verkaufsleistung. Dies ist **indirekte, strukturelle Stützung** für die Logik hinter der Problemreife-Hypothese (Anpassung der Vorgehensweise an Käufersignale wirkt) — **kein direkter Test** der spezifischen Dreistufung (Unbekannt/Falsch eingeschätzt/Richtig-aber-unartikuliert). Siehe ACADEMIC_RECOVERY_REPORT.md für vollständige Einordnung. | Mittel |
| A-0019, P-S1-003, SD-SYS-001 | Offene Forschungsfrage → geprüft, nicht aufgelöst | Verbeke, Dietz & Verwaal (2010/2011) jetzt inhaltlich geprüft (nicht nur referenziert): fünf signifikante Leistungstreiber (Selling-related Knowledge β=.28, Adaptiveness β=.27, Role Ambiguity β=−.25, Cognitive Aptitude β=.23, Work Engagement β=.23). Bestätigt NICHT die CEB-Challenger-Taxonomie oder den 53%-Split (A-0019) — andere Analyseebene. SD-SYS-001 bleibt für A-0019 offen. | Mittel |
| SD-SYS-001, Generalisierbarkeit (Reifegradbericht 1.5) | Offene Forschungsfrage | Ohiomah, Benyoucef & Andreev (2020), *A multidimensional perspective of B2B sales success: A meta-analytic review*, Industrial Marketing Management 90, 435–452 (139 Studien, 1980–2019). B2B-spezifische Meta-Analyse — direkt relevant für die Generalisierbarkeits-Schwäche (C+) des Codex. Granulare Einzelbefunde nicht extrahiert (kein Volltextzugriff) — als Literaturkandidat für SPR-0003/Buchanalyse-artige Vertiefung vorgemerkt, nicht inhaltlich verwertet. | Niedrig |
| CTX-Frage (OPEN_DECISIONS, OD-007) | Offene Forschungsfrage | Marcos-Cuevas et al., *Reclaiming the contingent nature of the determinants of salesperson performance: an extended meta-analysis*, Journal of Personal Selling & Sales Management 44(4), 2023 (150 Studien, 936 Effekte). Etabliert akademisch eine Drei-Klassen-Taxonomie (universal / kontextspezifisch / notwendig-aber-nicht-hinreichend) für Erfolgstreiber — liefert akademische Fachsprache für die Bewertung der CTX-Layer-Frage aus dem Peer Review. Kein MEC-Bezug. | Mittel |
| MEC-0014 | Unbelegte Annahme → teilweise ergänzt | Webster & Wind (1972, JM 36(2), 12–19), Sheth (1973, JM 37(4), 50–56 — **Korrektur:** Research Pack 1 nannte "1987", verifiziertes Publikationsjahr ist 1973), Eisenhardt (1989, AMR 14(1), 57–74, Agency Theory) als theoretische Standardwerke zu Buying Center und Principal-Agent-Dynamik ergänzt. Keine E-Level-Änderung — reine Theorie-Referenzen ohne Primärtext-Extraktion. Siehe MEC-0014-Objekt, Abschnitt "Ergänzende Theorie-Referenzen (ARS-0001)". | Mittel |
| Gesamtcodex, "Advancing Value-Based Selling Research" (2023, IMM 111) | Offene Forschungsfrage | Kein direkter MEC-Bezug im aktuellen Codex (keine Value-Based-Selling-Objekte vorhanden). Als Literaturkandidat für Academic Recovery Plan (Behavioral-Economics-B2B-Integrationslücke) vorgemerkt. | Niedrig |

**Zitationskorrektur (Transparenzpflicht):** Research Pack 1 zitierte Sheth mit Jahr "1987". Websuchverifikation ergibt: Sheth, J.N. (1973), "A Model of Industrial Buyer Behavior", Journal of Marketing 37(4), 50–56. Es wurde keine Sheth-Publikation von 1987 zu diesem Thema gefunden. Die Korrektur wird hier dokumentiert statt stillschweigend übernommen (Repository-Regel: „Erfinde niemals Quellen oder Fakten", „Kennzeichne Unsicherheit").

---

### Peer Review Sprint 2 — Systemische Scientific Debt (neu 2026-07-01)

**Hinweis:** Die folgenden Einträge entstammen dem wissenschaftlichen Gutachten nach Sprint 2 (`00_project/WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md`) und dessen Bewertung in ARS-0001 (`00_project/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`).

#### SD-SYS-004 — Publication Bias kommerzieller B2B-Studien (CEB/Challenger, JOLT/Tethr)

| Betroffene Objekte | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| A-0019, ST-0107–ST-0132 (Challenger/CEB) | Publication Bias (kommerzielle Studien) | CEB (heute Gartner) hat ein kommerzielles Interesse an einem positiven Ergebnis für die von ihr vertriebene Challenger-Methodik; die Studie wurde ursprünglich als Kundenreport veröffentlicht, nicht peer-reviewed. Selektive Veröffentlichung korrelierender (statt widersprechender) Befunde ist nicht auszuschließen, aber auch nicht direkt nachgewiesen. Allgemeine Literatur zu Industry-Sponsorship-Bias (z.B. medizinische Forschung) zeigt strukturelles Risiko dieser Konstellation, ohne dass eine sales-spezifische Studie dazu vorliegt. | Hoch |
| ST-0151, MOD-0006 (JOLT/Tethr) | Publication Bias (kommerzielle Studien) | Die Tethr-ML-Klassifizierung (44%/56%-Split) wurde von einem kommerziellen Analytics-Anbieter durchgeführt und nicht unabhängig repliziert (vgl. bestehender Eintrag SD-B006-001). | Mittel |

**Einordnung:** Diese Kategorie ergänzt, ersetzt aber nicht SD-SYS-001 (Replikationsrisiko). Der Unterschied: SD-SYS-001 fragt "gibt es unabhängige Wiederholung?", SD-SYS-004 fragt "gibt es einen strukturellen Anreiz zur selektiven Berichterstattung?". Beide Fragen sind unabhängig relevant und werden getrennt geführt.

#### Dokumentierte, nicht angelegte Kandidaten aus dem Peer Review Sprint 2

Diese Punkte sind bewusst **nicht** als neue Wissensobjekte angelegt (Begründung siehe `PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`), aber als Rechercheaufträge dokumentiert:

- **Meta-Prinzip-Kandidat "Asymmetrische Risikoverteilung im Buying Center":** Reviewer-Vorschlag, dass das persönliche Karriererisiko des internen Champions strukturell schwerer wiegt als der rationale Unternehmensnutzen (konvergent aus SPIN, Challenger, JOLT). Kandidat dokumentiert in `review_queue.md`. Nicht formal angelegt — vollständiger Quervergleich mit bestehenden P-/A-Objekten (A-0019, MEC-0014) nach Operating-Manual-Schritt-5-Prozess steht aus.
- **Kontradiktions-Kandidat "Kognitive Leichtigkeit vs. Rational Drowning":** Spannung zwischen Kahnemans Cognitive-Ease-Präferenz (MEC-0012) und der bewussten kognitiven Belastungsmaximierung der Challenger-Methodik (MEC-0013). Nicht identisch mit dem bereits in SPR-0002 aufgelösten Spannungsfeld 3 (emotionale Amygdala-Regulation vs. Dissonanz) — hier geht es um kognitive statt emotionale Last. Dokumentiert für SPR-0003/nächste Widerspruchsmatrix-Revision (contradiction_matrix.md ist als Sprint-1-Artefakt abgeschlossen und wird nicht rückwirkend editiert; neue Widersprüche werden in künftigen Synthese-Dokumenten geführt).

---

### Academic Recovery Sprint Phase 2 — Research Pack 2, 3, 4 (2026-07-01)

**Hinweis:** Die folgenden Einträge entstammen der Verarbeitung von "Research Pack 2" (Entscheidungspsychologie/Behavioral Economics), "Research Pack 3" (Sozialpsychologie/Persuasion) und "Research Pack 4" (Verhandlungsforschung). Details: `00_project/ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`, Literaturbelege: `05_research/LITERATURE_INDEX.md`.

#### SD-SYS-005 — Publication-Bias-Kontroverse bei Nudging/Choice-Architecture-Meta-Analysen

| Betroffene Objekte | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| Kein bestehendes MEC (Literaturkandidat "Choice Architecture", review_queue.md) | Widersprüchliche Evidenz | Mertens et al. (2021, PNAS) berichten einen Choice-Architecture-Gesamteffekt von d=0.43. Zwei publizierte PNAS-Erwiderungen (Maier et al. 2022, "No evidence for nudging after adjusting for publication bias"; sowie ein Gelman-Kommentar) bestreiten diese Effektgröße nach Publication-Bias-Korrektur. Zusätzlich existiert eine Korrektur zum Originalpaper (Kodierfehler, ein Datensatz aus einer zurückgezogenen Studie). Research Pack 2 selbst nennt Mertens et al. unkritisch als "zentral", ohne diese Kontroverse zu erwähnen — vom Editor bei der Prüfung ergänzt. | Mittel |

**Einordnung:** Relevant, sobald der Codex Choice Architecture/Default Effects als eigenständiges MEC formalisiert (aktuell nicht der Fall) — die Evidenzlage selbst ist ein Grund, damit nicht vorschnell zu sein.

#### SD-SYS-006 — Konvergenzbestätigungen bestehender Scientific-Debt-Einträge (B-0003, B-0002)

| Betroffene Objekte | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MEC-0010, MEC-0011, A-0016, ST-0077, ST-0087, ST-0088 (B-0003, Voss-Practitioner-Begriffe) | Externe Validierung ausstehend — jetzt teilweise konvergent bestätigt | Research Pack 4 stuft unabhängig **Tactical Empathy, Calibrated Questions, No-Oriented Questions und Black Swan Theory explizit als "keine robuste akademische Evidenz gefunden"** ein — deckungsgleich mit den bestehenden E1/E2-Einstufungen dieser Objekte. Diese unabhängige externe Konvergenz erhöht das Vertrauen, dass die bestehende Skepsis korrekt kalibriert ist. **Löst die zugrunde liegenden offenen Fragen nicht auf** (kein Ersatz für Gemini-Validierung oder Primärtext-Vertiefung) — reduziert aber das Risiko, dass die Codex-eigene Einschätzung systematisch zu vorsichtig oder zu großzügig war. | Niedrig (Bestätigung, keine neue Unsicherheit) |
| MEC-0005–MEC-0009 (B-0002, Cialdini-Prinzipien) | Externe Validierung ausstehend — teilweise konvergent bestätigt | Research Pack 3 nennt für Reciprocity, Social Proof, Authority, Liking exakt dieselben oder ergänzende Standardreferenzen wie die bestehenden Codex-Objekte und bestätigt unabhängig: "keine robuste B2B-spezifische Meta-Analyse" für alle vier. Dies ist keine Auflösung der bestehenden Gemini-Validierungs-Anforderung (OD-005), aber eine zusätzliche, unabhängige Bestätigung der Zitationsgenauigkeit und der offenen B2B-Lücke. | Niedrig |

#### Neue dokumentierte Literaturkandidaten (nicht angelegt) aus Research Pack 2–4

- **Elaboration Likelihood Model** (Petty & Cacioppo 1986) — höchste Priorität, siehe `ACADEMIC_RECOVERY_REPORT_PACK_2_4.md` Abschnitt 5.1 und `review_queue.md`.
- **Trust Formation** (Mayer, Davis & Schoorman 1995) — konvergent in Pack 3 und Pack 4 identifiziert, siehe Abschnitt 5.2.
- **Persuasion Knowledge Model** (Friestad & Wright 1994) — siehe Abschnitt 5.3.
- **Fairness/Equity Theory** (Adams 1965; Thibaut & Walker 1975) — siehe Abschnitt 5.4.
- **Choice Architecture/Default Effects** (Thaler & Sunstein 2008; Mertens et al. 2021, mit SD-SYS-005-Kontroverse) — siehe Abschnitt 5.5.

---

## Schuldenabbau-Prioritäten

1. **Hoch (sofort):** Validierungssprint MEC-0010/0011 — Fremd-Labeling (RQ-0010-2) + Behavioral Mirroring (RQ-0011-4) + Spiegelneuronen-Status (RQ-0011-3)
2. **Hoch (sofort):** B-0005 Quellenunvollständigkeit klären (SD-SYS-002)
3. **Hoch (parallel):** Gemini-Validierung MEC-0005–MEC-0009 + Langer-Xerox-Replikationsstatus
4. **Hoch (Sprint 2):** Individuelle E-Level-Prüfung aller Huthwaite/CEB-exklusiven Objekte (SD-SYS-001)
5. **Mittel:** MEC-0012 What/How-Framing + Mehrabian 7-38-55 Originalkontext + Gemini SPIN-Mechanismen
6. **Niedrig:** SPIN vs. Challenger Sale Vergleich + Kontrast/Verlustaversion Abgrenzung + B2B-Belege Reziprozität/Rapport

---

## Schuldenabbau-Protokoll

Wenn ein Scientific-Debt-Eintrag durch externe Validierung aufgelöst wird:

1. Eintrag aus dieser Tabelle entfernen (oder als "aufgelöst" markieren).
2. Betroffenes Objekt aktualisieren (Evidenzklasse, Notiz).
3. SESSION_LOG.md Eintrag ergänzen.

---

*Stand: 2026-06-30. Wird nach jeder Buchanalyse aktualisiert.*
