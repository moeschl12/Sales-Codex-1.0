# SCRP-0001 — Sales Codex Review Package: Sales Core Sprint 1

**Dokumenttyp:** Externes Peer-Review-Paket  
**Erstellt:** 2026-07-01  
**Reviewer-Zielgruppe:** Externe wissenschaftliche Gutachter ohne Zugang zum Repository  
**Sprint:** Sales Sprint 1 (S1)  
**Quellen:** 5 Bücher, verarbeitet 2026-06-27 bis 2026-07-01  
**Gesamtobjekte:** 254 Wissensobjekte

---

## Hinweis für Reviewer

Dieses Dokument ist vollständig eigenständig. Es setzt keinerlei Kenntnis des Sales Codex Repository voraus. Alle Wissensobjekte, Evidenzbewertungen, Widersprüche und offenen Fragen sind vollständig in diesem Dokument enthalten. Querverweise auf Repository-Dateien sind als kontextuelle Hinweise markiert; ihr Inhalt ist vollständig in dieses Dokument übernommen.

Geprüft werden soll:
1. Die Evidenzklassifikation einzelner Mechanismen und Prinzipien
2. Die Robustheit der Widerspruchsanalyse
3. Die Vollständigkeit und Korrektheit der Scientific Debt-Dokumentation
4. Die Qualität der Forschungsagenda

---

## Inhaltsverzeichnis

1. Executive Summary
2. Repository-Kontext
3. Wissensmodell
4. Sprint Overview
5. Meta-Prinzipien (S1-SYNTHESIS)
6. Mechanismen (MEC-0001 bis MEC-0015)
7. Prinzipien (P-0001 bis P-0026)
8. Modelle (MOD-0001 bis MOD-0005)
9. Contradiction Matrix
10. Canonicalization Report
11. Emerging Principles
12. Scientific Debt
13. Research Agenda
14. Offene wissenschaftliche Fragen
15. Anhang: Statistik des Sales Codex

---

## 1. Executive Summary

Der Sales Codex ist ein evidenzbasiertes Wissenssystem über Vertrieb, Verkauf, Verhandlung und Käuferpsychologie. Ziel ist nicht die Sammlung von Verkaufstipps, sondern die Destillation wissenschaftlich überprüfbarer Mechanismen, die Kaufentscheidungen erklären.

Sprint 1 (S1) hat fünf einflussreiche Werke aus dem Zeitraum 1984–2018 verarbeitet: SPIN Selling (Rackham, 1988), Influence (Cialdini, 1984), Never Split the Difference (Voss/Raz, 2016), The Challenger Sale (Dixon/Adamson, 2011) und Gap Selling (Keenan, 2018). Aus diesen fünf Büchern wurden 254 Wissensobjekte extrahiert, klassifiziert und in ein kohärentes Wissensmodell integriert.

**Stärkste Befunde des Sprints:**

Verlustaversion (MEC-0002) ist der am breitesten gestützte Mechanismus des Sales Codex. Vier von fünf Büchern — aus verschiedenen Jahrzehnten, von unabhängigen Autoren, mit unterschiedlichen methodischen Zugängen — konvergieren auf dieselbe Kernlogik: Die stärkste Kaufmotivation entsteht aus den Kosten des Nicht-Handelns, nicht aus dem Versprechen der Lösung. Dieses Ergebnis ist durch Laborforschung (Kahneman/Tversky 1979, E4) und drei unabhängige Feldmethodologien gestützt.

**Kritischer ungelöster Widerspruch:**

Widerspruch W-001 (Teach First vs. Diagnose First) ist der einzige ungelöste methodologische Kernwiderspruch. The Challenger Sale (Dixon/Adamson) empfiehlt, Käufer proaktiv durch externe Insights zu reframen, bevor die Discovery vollständig ist. Gap Selling (Keenan) verbietet jede Lösungspräsentation vor vollständiger Diagnose. Beide beanspruchen Universalgültigkeit für B2B-Komplex. Kein direkter Vergleich existiert. Dieser Widerspruch verhindert die Formulierung eines integrierten Verkaufsmodells.

**Vier Sprint-übergreifende Meta-Prinzipien** wurden als neue Wissensobjekte angelegt (P-S1-001 bis P-S1-004), weil sie erst durch die Kombination aller Bücher sichtbar werden — kein Einzelbuch formuliert sie als übergreifendes Prinzip.

**Grenzen des Sprints:**

Alle fünf Bücher sind proprietäre Methoden-Werke ohne unabhängige RCT-Validierung. Die Evidenzbasis reicht von E5 (Miller's Law für MEC-0015) bis E1 (Spiegelneuronenhypothese für MEC-0011). Diese Spannbreite ist explizit dokumentiert und bildet die Grundlage der Scientific Debt-Dokumentation.

---

## 2. Repository-Kontext

### 2.1 Was ist der Sales Codex?

Der Sales Codex ist ein strukturiertes Wissenssystem, das Erkenntnisse über Verkauf, Verhandlung und Käuferpsychologie in einem formalen Wissensmodell erfasst. Das Ziel ist kein Ratgeber und keine Methodenempfehlung — das Ziel ist eine evidenzbasierte Wissensbasis, die Mechanismen hinter Kaufentscheidungen systematisch dokumentiert, klassifiziert und auf Widersprüche prüft.

### 2.2 Prinzipien der Wissenserstellung

Das Repository operiert nach folgenden unveränderlichen Grundregeln:

- **Keine Erfindung von Quellen oder Fakten.** Alle Wissensobjekte müssen auf existierende Quellen zurückführbar sein.
- **Unsicherheit wird dokumentiert, nicht geglättet.** Evidenzlücken und Widersprüche werden explizit markiert.
- **Widersprüche werden dokumentiert, nicht aufgelöst.** Ein dokumentierter Widerspruch ist wertvoller als eine spekulativ aufgelöste Inkonsistenz.
- **Synthese hat Vorrang vor Wachstum.** Neue Objekte werden nur angelegt, wenn kein bestehendes Objekt den neuen Sachverhalt abdeckt.
- **Keine Struktur- oder Framework-Änderungen ohne explizite Freigabe.**

### 2.3 Wissens-Pipeline

Wissen fließt durch folgende Stufen:

```
Primärquelle (SRC) → Statements (ST) → Annahmen (A) → Mechanismen (MEC)
→ Prinzipien (P) → Techniken (T) → Modelle (MOD) → Validierung (VAL)
```

Jeder Schritt erfordert einen Quellennachweis. Jedes Objekt hat eine ID, eine Evidenzklassifikation und — wenn relevant — eine Quellenkonfidenzbewertung.

### 2.4 Was dieser Sprint ist und was nicht

Sprint 1 hat fünf Bücher systematisch analysiert. Das Ergebnis ist kein Vergleich der Methoden (welche ist besser?) und keine Metaanalyse (welche Techniken funktionieren empirisch?). Es ist eine strukturierte Wissensbasis: Was behaupten diese Werke? Welche Mechanismen beschreiben sie? Wo konvergieren sie? Wo widersprechen sie sich?

---

## 3. Wissensmodell

### 3.1 Objekttypen

Der Sales Codex verwendet sechs primäre Objekttypen:

**SRC (Quelle):** Die Primärquelle (Buch, Studie, Artikel). Enthält Metadaten: Autor, Jahr, Quellenklasse (A = akademische Primärforschung, B = Practitioner-Buch, C = Sekundärquelle), Evidenzklasse des Buches insgesamt.

**ST (Statement):** Einzelne, belegbare Aussagen direkt aus der Quelle. Jedes ST ist einer Seite oder einem Kapitel zugeordnet. STs sind die atomare Einheit der Wissensextraktion.

**A (Annahme):** Implizite oder explizite Grundannahmen einer Quelle. Annahmen sind notwendige Bedingungen für die Gültigkeit der darauf aufbauenden Argumente. Sie werden explizit gemacht, um Kontextgrenzen sichtbar zu halten.

**MEC (Mechanismus):** Der psychologische, neurowissenschaftliche oder sozialpsychologische Wirkmechanismus hinter beobachtbaren Verhaltensänderungen. MECs sind buchübergreifend — sie können durch mehrere unabhängige Bücher gestützt werden (Extension) oder neu angelegt werden. MECs sind die wichtigste Kanonisierungsebene des Codex.

**P (Prinzip):** Eine handlungsrelevante Ableitung aus mindestens einem Mechanismus (MEC) oder mindestens zwei Annahmen (A). Prinzipien beschreiben, was ein Verkäufer tun oder lassen soll — begründet durch den Mechanismus, nicht durch Intuition.

**T (Technik):** Konkrete, operationalisierbare Handlung, die ein Prinzip umsetzt. Techniken sind die praktischste Schicht.

**MOD (Modell):** Ein buchspezifisches integriertes Rahmenwerk, das mehrere Mechanismen, Prinzipien und Techniken in einer kohärenten Logik verbindet.

### 3.2 Evidenzklassifikation (E-Level)

| Stufe | Bezeichnung | Beschreibung |
|---|---|---|
| E5 | Kanonische Wissenschaft | Gut replizierte, breite Konsensforschung (z.B. Miller's Law 1956) |
| E4 | Laborgesichert | Replizierte Labor-/Feldexperimente mit breitem Konsens (z.B. Prospect Theory, Kahneman/Tversky 1979) |
| E3 | Feldstudie | Gut begründete Primärstudie oder Feldbefragung mit klarer Methodik (z.B. CEB-Studie N=6.000, Rackham Huthwaite-Studie) |
| E2 | Practitioner-Evidenz | Practitioner-Modell mit logischer Stützung, anekdotisch oder plausibel abgeleitet |
| E1 | Spekulativ | Ungeprüfte Hypothese oder spekulative Annahme |

### 3.3 Quellen-Konfidenz (QK)

Quellen-Konfidenz beschreibt, wie viele unabhängige Quellen ein Wissensobjekt stützen — unabhängig vom Evidenzlevel.

| QK | Quellen |
|---|---|
| QK-1 | 1 Quelle |
| QK-2 | 2 unabhängige Quellen |
| QK-3 | 3 unabhängige Quellen |
| QK-4 | 4 unabhängige Quellen |
| QK-5 | 5 unabhängige Quellen (Sprint-Maximum) |

Ein Objekt kann QK-3/E2 sein: Drei Bücher stützen es, aber keines hat eine Primärstudie. Ein anderes Objekt kann QK-1/E4 sein: Eine Quelle, aber gut laborgesichert.

### 3.4 Canonicalization

Canonicalization bezeichnet die Entscheidung, ob ein neues Buch einen neuen Mechanismus beschreibt (neue MEC-Anlage) oder denselben Mechanismus in einem neuen Kontext anwendet (Extension eines bestehenden MEC). Nur MECs werden kanonisiert; Prinzipien, Annahmen und Techniken werden immer neu angelegt, weil ihre Formulierungen buchspezifisch sind.

**Canonicalization Rate:** Extensions / (Neue Objekte + Extensions) × 100. Je höher die Rate, desto stärker konvergiert das Wissenssystem statt zu fragmentieren.

**Sprint-1-Rate:** 31,8% (7 Extensions / 22 MEC-Ereignisse)

---

## 4. Sprint Overview

### 4.1 Analysierte Quellen

| ID | Buch | Autor | Jahr | Quellenklasse | Gesamt-E-Level |
|---|---|---|---|---|---|
| SRC-0001 | SPIN Selling | Neil Rackham | 1988 | B (Practitioner, intern-empirisch) | E3 |
| SRC-0002 | Influence: The Psychology of Persuasion | Robert B. Cialdini | 1984/2007 | B (Sozialpsychologie-Populärwerk) | E3/E4 |
| SRC-0003 | Never Split the Difference | Chris Voss / Tahl Raz | 2016 | B (Practitioner + Neurowiss.) | E2/E3 |
| SRC-0004 | The Challenger Sale | Matthew Dixon / Brent Adamson (CEB) | 2011 | B (Befragungsstudie CEB) | E3 |
| SRC-0005 | Gap Selling | Keenan | 2018 | B (Practitioner) | E2 |

### 4.2 Wissensobjekte gesamt

| Typ | B-0001 | B-0002 | B-0003 | B-0004 | B-0005 | Gesamt |
|---|---|---|---|---|---|---|
| Statements (ST) | 23 | 26 | 57 | 26 | 17 | **149** |
| Annahmen (A) | 4 | 8 | 5 | 6 | 6 | **29** |
| Mechanismen (MEC) — neu | 4 | 5 | 3 | 2 | 1 | **15** |
| Mechanismen (MEC) — ext. | — | — | 3 | 2 | 2 | **7** |
| Prinzipien (P) | 7 | 8 | 5 | 4 | 2 | **26** |
| Techniken (T) | 4 | 7 | 7 | 3 | 4 | **25** |
| Modelle (MOD) | 1 | 1 | 1 | 1 | 1 | **5** |
| **Gesamt** | **43** | **55** | **81** | **44** | **31** | **254** |

### 4.3 Thematischer Bogen

Die fünf Bücher decken verschiedene Dimensionen des Verkaufs- und Überzeugungsprozesses ab:

| Buch | Primäre Dimension | Erkenntnisebene |
|---|---|---|
| SPIN Selling | Fragetechnik / Bedarfsentwicklung | Operativ |
| Influence | Compliance-Psychologie / Hebelmechanismen | Mechanistisch |
| Never Split | Verhandlung / Emotionsregulation | Taktisch-psychologisch |
| Challenger Sale | Verkäuferprofil / Differenzierung | Strategisch-organisational |
| Gap Selling | Kaufdiagnose / Problem-Zentrierung | Methodologisch |

### 4.4 Sprint-Ergebnis auf einem Blick

| Befund | Detail |
|---|---|
| Stärkster Mechanismus | MEC-0002 (Verlustaversion / COI) — QK-5, alle 5 Bücher |
| Robustestes Prinzip | P-0002 (Lösungswert folgt Problemgewicht) — QK-4 |
| Kritischer Widerspruch | W-001: Teach First (Challenger) vs. Diagnose First (Gap Selling) — UNGELÖST |
| Neue Meta-Prinzipien | P-S1-001 bis P-S1-004 |
| Sprint-Canonicalization Rate | 31,8% |
| Abgelehntes Objekt | MOD-S1 (integriertes Modell) — wegen W-001 nicht möglich |

---

## 5. Meta-Prinzipien (S1-SYNTHESIS)

Die folgenden vier Prinzipien sind Sprint-übergreifende Synthese-Ergebnisse. Sie sind nicht in einzelnen Büchern enthalten — sie werden erst durch die Kombination aller Sprint-Bücher sichtbar. Jedes erfordert mindestens zwei unabhängige Quellenbestätigungen.

### P-S1-001 — Cost of Inaction als universeller Kaufmotivator

**Evidenzklasse:** E4 (allg.) + E3 (3 Verkaufsmethodologien)  
**Quellen-Konfidenz:** QK-5 (alle 5 Bücher)  
**Status:** Aktiv

**Formulierung:**  
Die stärkste Kaufmotivation entsteht aus den Kosten des Nicht-Handelns (Cost of Inaction, COI), nicht aus dem Versprechen der Lösung. Dieses Prinzip gilt in jeder Phase des Verkaufs- und Verhandlungsprozesses — von der ersten Discovery bis zur finalen Preisverhandlung. Es ist nicht das Werkzeug einer einzelnen Methode, sondern das psychologische Grundgesetz, dem alle untersuchten Methodologien folgen.

**Buchstützung:**

| Buch | Formulierung | Objekt |
|---|---|---|
| SPIN Selling (B-0001, 1988) | Implication Questions machen Kosten des Status Quo bewusst | T-0003, P-0002 |
| Influence (B-0002, 1984) | Prospect Theory: Verluste > Gewinne (Kahneman/Tversky 1979) | MEC-0002 |
| Never Split (B-0003, 2016) | Negative Leverage: Kosten des Scheiterns als Verhandlungshebel | T-0015, P-0018 |
| Challenger Sale (B-0004, 2011) | Rational Drowning: quantifizierter Business Impact | MEC-0002 ext. |
| Gap Selling (B-0005, 2018) | COI explizit als Budget-Freischaltungs-Mechanismus | A-0027 |

**Warum erst durch Sprint sichtbar:** Kein Buch formuliert COI als sprint-übergreifendes Gesetz. SPIN nennt es als Fragetechnik. Cialdini als psychologischen Mechanismus. Voss als Verhandlungshebel. Challenger als Pitch-Schritt. Gap Selling als Qualifikationslogik. Erst die Kombination zeigt: COI ist nicht ein Werkzeug — es ist die verbindende Logik aller untersuchten Methoden.

**Verknüpfte Objekte:** MEC-0002 (primärer Mechanismus); P-0002, P-0018, A-0027

**Kontextgrenzen:**  
Stärkste Wirkung bei Kaufentscheidungen, die Statusquo-Änderung erfordern. Schwächer bei Impulskäufen ohne wahrgenommenen Statusquo-Schutz.

---

### P-S1-002 — Mikro-Commitment-Sequenz als Kaufstruktur

**Evidenzklasse:** E4 (allg., Festinger 1957) + E3 (3 Methodologien)  
**Quellen-Konfidenz:** QK-4 (B-0001, B-0002, B-0004, B-0005)  
**Status:** Aktiv

**Formulierung:**  
Jede Kaufentscheidung — insbesondere im B2B-Komplex — ist keine einzelne Entscheidung am Ende eines Prozesses, sondern das Ergebnis einer akkumulierten Sequenz kleiner Zustimmungen (Mikro-Commitments). Jedes "Ja" erhöht die Wahrscheinlichkeit des nächsten. Der finale Kauf ist der logische Endpunkt einer langen Sequenz — kein isoliertes Ereignis.

**Buchstützung:**

| Buch | Formulierung | Objekt |
|---|---|---|
| SPIN Selling (B-0001) | Need-Payoff Questions → Explicit Need → Käufer hat selbst committet | MEC-0004, T-0004 |
| Influence (B-0002) | Commitment & Consistency; Lowballing: Commitment hält bei Angebotsänderung | MEC-0004 ext. |
| Gap Selling (B-0005) | "A sale is made up of hundreds of little sales" — Yes-Sequenz | MEC-0004 ext. |
| Challenger Sale (B-0004) | Champion Building: schrittweise interne Commitments aufbauen | P-0023 |

**Verknüpfte Objekte:** MEC-0004 (primärer Mechanismus); P-0007, P-0010, ST-0145

---

### P-S1-003 — Problem-Zentrierung als universelles Differenzierungsprinzip

**Evidenzklasse:** E3 (CEB-Studie A-0019) + E2 (methodologische Konvergenz)  
**Quellen-Konfidenz:** QK-4 (B-0001, B-0003, B-0004, B-0005)  
**Status:** Aktiv; ⚠ Aktiver Widerspruch W-001 dokumentiert

**Formulierung:**  
Der nachhaltigste Wettbewerbsvorteil im Verkauf entsteht nicht durch Produktvorteile, Preisgestaltung oder persönliche Sympathie, sondern durch die Qualität des Problemverständnisses. Wer das Problem des Käufers tiefer, präziser und früher versteht als jeder Wettbewerber, hat einen strukturell nicht kopierbaren Vorteil.

**Buchstützung:**

| Buch | Formulierung | Objekt |
|---|---|---|
| SPIN Selling (B-0001) | Need Development: Bedarfsentwicklung vor Lösung | P-0004 |
| Challenger Sale (B-0004) | 53% Loyalität durch Sales Experience; Teach als Insight-Lieferung | A-0019, P-0021 |
| Gap Selling (B-0005) | Problemdiagnose (PIC, Root Cause) als Credibility-Signal | P-0026, A-0029 |
| Never Split (B-0003) | Black Swans = verborgene Motivationen; Insight als Verhandlungsvorteil | A-0016, T-0017 |

**⚠ Widerspruch W-001:** Dieses Prinzip impliziert, dass tiefes Problemverständnis vor Insight-Lieferung kommen sollte (Diagnose First). Dies steht im Widerspruch zu A-0020 (Challenger: Kunden wollen gelehrt werden) und P-0021 (Commercial Teaching als Teach-First-Prinzip). P-S1-003 beschreibt, *was* differenziert (Problemkenntnis), nicht *wann* sie eingesetzt wird — W-001 betrifft die Sequenz.

---

### P-S1-004 — Informationssparsamkeit als Wirkungsverstärker

**Evidenzklasse:** E5 (Miller's Law 1956) + E2 (methodologische Konvergenz)  
**Quellen-Konfidenz:** QK-4 (B-0001, B-0002, B-0004, B-0005)  
**Status:** Aktiv

**Formulierung:**  
Weniger Information zur richtigen Zeit wirkt stärker als mehr Information zur falschen Zeit. Jede effektive Verkaufsmethodik des Sprints begrenzt aktiv die Informationsmenge pro Interaktion, um kognitive Überlastung zu vermeiden und Relevanz zu maximieren. Kognitive Beschränkung ist kein Hygieneanspruch — sie ist ein Wirkungsprinzip.

**Buchstützung:**

| Buch | Regel | Objekt |
|---|---|---|
| SPIN Selling (B-0001) | Benefit erst nach explizitem Need — nie als Feature-Liste | P-0005 |
| Influence (B-0002) | Compliance-Trigger wirken durch Fokus auf einen Hebel, nicht viele | P-0008 |
| Challenger Sale (B-0004) | 6-Step Commercial Teaching Pitch als informationsstrukturierte Sequenz | T-0019 |
| Gap Selling (B-0005) | Max. 6 Features in der Demo (Miller's Law explizit) | T-0022, MEC-0015 |

**Mechanistische Grundlage:**  
MEC-0015 (Kognitive Überlastung durch Feature-Overload): Wenn Informationsmenge kognitive Kapazität überschreitet (Miller 1956: 7±2 Chunks; Cowan 2001: 4±1), sinkt Verarbeitungstiefe und Kaufbereitschaft.

**Evidenzlücke:** Die "max. 6 Features"-Regel (Keenan) ist eine Extrapolation von Miller's Law auf Demo-Kontexte — kein Verkaufsexperiment repliziert diese Zahl direkt.

---

## 6. Sämtliche Mechanismen (MEC-0001 bis MEC-0015)

Mechanismen sind die Kernschicht des Wissensmodells. Sie beschreiben psychologische oder neurowissenschaftliche Wirkpfade — nicht Techniken. Jeder Mechanismus enthält: Erstquelle, E-Level, QK-Level, Extension-Dokumentation.

---

### MEC-0001 — Selbstüberzeugung durch Verbalisierung

**E-Level:** E4 (allgemein) / E3 (Verkaufskontext)  
**QK:** QK-1 (B-0001 primär)  
**Erstquelle:** SRC-0001 (SPIN Selling, Rackham 1988)  
**Primärevidenz:** Bem (1972) Selbstwahrnehmungstheorie; Petty/Cacioppo Elaboration Likelihood Model; Cialdini-Beobachtungen (SRC-0002)

**Beschreibung:**  
Was ein Mensch laut ausspricht, überzeugt ihn mehr als was ein anderer sagt. Selbstverbalisierung verändert Einstellungen stärker als Fremdinformation, weil das Gehirn das Gesprochene als eigene Position verbucht.

**Verkaufsanwendung:**  
Need-Payoff Questions (T-0004) in SPIN Selling: Der Verkäufer bringt den Käufer dazu, die Lösung und ihren Wert selbst zu formulieren. Diese Selbstformulierung ist überzeugender als jede Verkäufer-Präsentation.

**Widerspruch:**  
MEC-0001 vs. MEC-0013 (Insight-Disruption): SPIN setzt auf Käufer-Selbstverbalisierung; Challenger Sale setzt auf externe Verkäufer-Perspektive. Kein echter Widerspruch, aber in der Discovery-Phase konkurrieren beide (→ W-003).

**Wissenschaftliche Grenzen:**  
Gut im Labor gesichert. Transfer auf komplexe B2B-Verkaufsgespräche nicht direkt repliziert. Langer-Xerox-Studie (1978) — ein Klassiker der Compliance-Forschung, der diesen Mechanismus mitbegründet — hat in der Replikationskrise unklaren Status (→ Scientific Debt F-006).

---

### MEC-0002 — Verlustaversion und Kosten des Status Quo (COI)

**E-Level:** E4 (Labor, Kahneman/Tversky 1979) + E3 (3 Verkaufsmethodologien)  
**QK:** QK-5 (alle 5 Bücher)  
**Erstquelle:** SRC-0002 (Influence, Cialdini), primäre Evidenzbasis: Kahneman/Tversky 1979  
**Extensions:** SRC-0003 (Negative Leverage), SRC-0004 (Rational Drowning), SRC-0005 (COI-Explizitmachung)

**Beschreibung:**  
Menschen gewichten Verluste ca. 2–2,5× stärker als äquivalente Gewinne (Prospect Theory, Kahneman/Tversky 1979). Im Kaufkontext: Die Kosten des Nicht-Handelns (Cost of Inaction = COI) motivieren stärker als der Nutzen der Lösung.

**Dies ist der am breitesten gestützte Mechanismus des Sales Codex.**

**Extension-Details:**

| Buch | Extension | Kontext |
|---|---|---|
| SPIN Selling (SRC-0001) | Implication Questions — Kosten des Status Quo bewusst machen | Discovery |
| Influence (SRC-0002) | Prospect Theory als Labor-Grundlage | Theoretisch |
| Never Split (SRC-0003) | Negative Leverage — Kosten des Scheiterns als Verhandlungshebel | Verhandlung |
| Challenger Sale (SRC-0004) | Rational Drowning — quantifizierter Business Impact in Pitch-Schritt 3 | Pitch |
| Gap Selling (SRC-0005) | COI-Explizitmachung — wenn COI > Investitionskosten, Budget erschlossen | Qualifikation |

**Wissenschaftliche Einschätzung:**  
Der Labornaturbefund (Kahneman/Tversky E4) ist robust. Die Verkaufsanwendung über drei unabhängige Methodologien (SPIN 1988, Challenger 2011, Gap 2018) stärkt die praktische Konfidenz erheblich. Direkte RCT-Studie zu COI-Aktivierung als Verkaufsintervention fehlt.

---

### MEC-0003 — Reaktanz durch Kontrollverlust

**E-Level:** E4 (Labor, Brehm 1966)  
**QK:** QK-2 (B-0001 als Problem, B-0003 als Lösung)  
**Erstquelle:** SRC-0001; Primärevidenz: Jack Brehm (1966) Reaktanztheorie  
**Extensions:** SRC-0002 (Knappheit), SRC-0003 (Calibrated Questions als Lösung)

**Beschreibung:**  
Wenn Menschen wahrnehmen, dass ihre Entscheidungsfreiheit eingeschränkt wird, reagieren sie mit psychologischem Widerstand (Reaktanz): Sie wollen die bedrohte Option noch stärker oder verweigern die Zustimmung vollständig. In Verkaufssituationen: Zu viel Druck erzeugt Gegendruck.

**Doppelte Anwendung:**  
Rackham beschreibt Reaktanz als Risiko zu aggressiver Abschlusstechniken. Voss beschreibt mit "Calibrated Questions" die Lösung: Fragen, die dem Gegenüber Kontrolle zurückgeben (Autonomieillusion), deaktivieren Reaktanz.

**Kontextgrenze:**  
Gilt besonders bei druckbasierten Verkaufsansätzen. Verkäufer, die keine Drucksituation erzeugen, aktivieren MEC-0003 seltener.

---

### MEC-0004 — Kognitive Konsistenz durch explizite Bedarfsartikulierung

**E-Level:** E4 (Labor, Festinger 1957)  
**QK:** QK-3 (B-0001, B-0002, B-0005)  
**Erstquelle:** SRC-0001; Primärevidenz: Festinger (1957) Kognitive Dissonanztheorie  
**Extensions:** SRC-0002 (Lowballing, Post-Entscheidungs-Rationalisierung), SRC-0005 (Yes-Sequenz)

**Beschreibung:**  
Menschen streben nach Konsistenz zwischen ihren Aussagen und ihrem Verhalten. Wenn jemand explizit formuliert, ein Problem zu haben und eine Lösung zu wollen (expliziter Bedarf), erzeugt Nicht-Kaufen kognitive Dissonanz. Der Commitment-Sequenzeffekt: frühe Zustimmungen erhöhen die Wahrscheinlichkeit späterern Zustimmungen.

**Extension-Details:**

| Buch | Extension | Spezifik |
|---|---|---|
| Influence (SRC-0002) | Lowballing: Commitment hält, wenn Bedingungen sich nach dem Ja verschlechtern | Commitment-Persistenz |
| Gap Selling (SRC-0005) | Yes-Sequenz: "A sale is made up of hundreds of little sales" | Sequenzielle Akkumulation |

---

### MEC-0005 — Reziprozitätspflicht

**E-Level:** E4 (Labor, Gouldner 1960; Regan 1971) / E3 (Feldbeobachtungen, Cialdini)  
**QK:** QK-1 (B-0002)  
**Erstquelle:** SRC-0002 (Influence)

**Beschreibung:**  
Menschen fühlen sich verpflichtet, Gefälligkeiten zu erwidern — auch wenn sie die Gegenleistung nicht verlangt haben, nicht wollten und die ursprüngliche Leistung den eigenen Bedürfnissen nicht entspricht. Die Verpflichtung ist kulturell universal und schwer zu unterdrücken.

**Verkaufsanwendung:**  
Vorab-Leistung (T-0005) als Verkaufstechnik: Kleine Gefälligkeit oder kostenlose Information vor dem Gespräch erhöht Compliance-Bereitschaft des Gegenübers.

**Scientific Debt:**  
Regan-Studie (1971) — Replikationsstatus in post-Replikationskrise unklar. B2B-spezifische Belege fehlen.

---

### MEC-0006 — Soziale Bewährtheit als Korrektheitssignal

**E-Level:** E4 (Labor) / E3 (Feldbeobachtungen, Cialdini)  
**QK:** QK-1 (B-0002)  
**Erstquelle:** SRC-0002 (Influence)  
**Primärevidenz:** Latané/Darley (1970) Bystander-Effekt; Phillips (1974) Imitations-Suizid

**Beschreibung:**  
Unter Unsicherheit orientieren Menschen ihr Verhalten an dem anderer. Je ähnlicher die Referenzgruppe, desto stärker der Effekt. Im Verkauf: Referenzkunden aus ähnlichen Branchen oder Situationen erzeugen stärkeres Kaufsignal als abstrakte Statistiken.

**Mögliche Verwandtschaft mit MEC-0014** (Konsens als Kaufsicherheit in Gruppen): Werden zukünftig auf Fusions-Kandidatur geprüft (→ F-004, Research Agenda).

---

### MEC-0007 — Sympathieübertragung auf Produkturteil

**E-Level:** E4 (Labor) / E3 (Feldbeobachtungen, Cialdini)  
**QK:** QK-1 (B-0002) + Kontext-Grenzfall B-0004, B-0005  
**Erstquelle:** SRC-0002  
**Primärevidenz:** Frenzen/Davis Tupperware-Studie (1990); Davis (1973) Halo-Effekt

**Beschreibung:**  
Sympathie gegenüber einer Person überträgt sich auf das Urteil über deren Produkte und Empfehlungen. Ähnlichkeit, Komplimente, vertraute Umgebung und physische Attraktivität sind die häufigsten Auslöser.

**⚠ Wichtige Kontextgrenze:**  
The Challenger Sale (SRC-0004) zeigt: Relationship Builder (= sympathiefokussierter Verkäufer) sind das schwächste B2B-Verkäuferprofil (7% der Stars). Gap Selling (SRC-0005) bestätigt: "Be an expert, not a friend." MEC-0007 gilt unbestritten für einfache Kaufentscheidungen — die Übertragung auf komplexes B2B-Kaufverhalten mit mehreren Entscheidern und langen Zyklen ist nicht repliziert und durch Gegenbefunde infrage gestellt (→ W-002).

---

### MEC-0008 — Autorität als automatischer Compliance-Auslöser

**E-Level:** E4 (Labor) / E3 (Feldbeobachtungen, Cialdini)  
**QK:** QK-1 (B-0002) + Kontext B-0005  
**Erstquelle:** SRC-0002  
**Primärevidenz:** Milgram (1963, 1974) Gehorsamsexperiment

**Beschreibung:**  
Statussymbole (Titel, Kleidung, Trappings) erzeugen automatische Compliance-Reaktionen — auch wenn die Autorität inhaltlich nicht verifiziert ist. Cialdini: Menschen reagieren auf Autorität als Signal, nicht auf tatsächliche Expertise.

**Verkaufsanwendung (Gap Selling-Kontext):**  
A-0029 (Expertise-Credibility als Discovery-Gate) beschreibt, wie Verkäufer durch Problemverständnis (nicht Statussymbole) Autorität signalisieren. Diese Ergänzung vertieft MEC-0008: Autorität ist aktivierbar durch echte Expertise, nicht nur durch äußere Signale.

---

### MEC-0009 — Perzeptueller Kontrast

**E-Level:** E4 (Labor) / E3 (Feldbeobachtungen, Cialdini)  
**QK:** QK-1 (B-0002)  
**Erstquelle:** SRC-0002  
**Primärevidenz:** Weber's Law; Brunswick-Billardstudie

**Beschreibung:**  
Die Wahrnehmung eines Reizes wird durch den vorangegangenen Reiz relativ verändert. Zwei Gegenstände werden nicht absolut, sondern im Vergleich zueinander beurteilt. Im Verkauf: Ein teures Produkt zuerst zeigen lässt das günstigere attraktiver erscheinen (Sell-Down-Sequenz).

**Abgrenzung zu MEC-0002:**  
Perzeptueller Kontrast ist eine relationale Wahrnehmungsverzerrung (Reihenfolgeeffekt). Verlustaversion ist eine motivationale Gewichtungsasymmetrie (Verluste vs. Gewinne). Beide wirken in Preissituationen, aber auf verschiedenen Pfaden.

---

### MEC-0010 — Amygdala-Regulation durch affektives Labeling

**E-Level:** E2-Kandidat (Transfer unbelegt)  
**QK:** QK-1 (B-0003)  
**Erstquelle:** SRC-0003 (Never Split the Difference)  
**Primärevidenz:** Lieberman et al. (2007), fMRT-Studie, Journal of Psychological Science

**Beschreibung:**  
Voss behauptet (gestützt auf Lieberman 2007): Das Benennen einer Emotion (Labeling) reduziert die Amygdala-Aktivierung und ermöglicht System-2-Denken. Labeling wäre damit neurobiologisch erklärbar.

**⚠ Kritische Einschränkung:**  
Lieberman (2007) zeigte Amygdala-Dämpfung beim Benennen von Emotionen aus Gesichtsfotos — nicht durch Fremd-Labeling in einem Gespräch. Der Transfer vom Labor (passives Emotionsbenennen bei Bildmaterial) auf aktives Labeling in Gesprächssituationen ist nicht direkt belegt. Externe Validierung ausstehend (→ F-002, Research Agenda). E-Level: E2-Kandidat, kein E3.

---

### MEC-0011 — Neural Coupling durch Isopraxismus (Spiegelneuronen-Hypothese)

**E-Level:** E1 (Spiegelneuronen-Transfer umstritten)  
**QK:** QK-1 (B-0003)  
**Erstquelle:** SRC-0003  
**Primärevidenz:** Stephens, Silbert & Hasson (2010), PNAS — Neuronale Synchronisation bei Kommunikation

**Beschreibung:**  
Voss behauptet: Mirroring (Wiederholen der letzten 1–3 Worte des Gesprächspartners) erzeugt neuronale Synchronisation (Neural Coupling), die Rapport und Kooperationsbereitschaft fördert.

**⚠ Kritische Einschränkung:**  
Dies ist der wissenschaftlich unsicherste Mechanismus des Sprints. Stephens et al. (2010) zeigten neuronale Synchronisation bei normalem Zuhören — nicht spezifisch bei Mirroring als Intervention. Die Spiegelneuronen-Verbindung zu menschlicher sozialer Kognition ist wissenschaftlich kontrovers: Die direkte Übertragung von Makaken-Spiegelneuronen-Befunden (Rizzolatti et al.) auf menschliche soziale Kognition und Empathie ist nicht repliziert. Externe Validierung ausstehend (→ F-002). MEC-0011 bleibt im Codex, aber explizit als E1-Kandidat markiert.

---

### MEC-0012 — Dual-Process-Steuerung System 1 → System 2

**E-Level:** E4 (allg., Kahneman 2011) / E1 (MacLean-Triune-Brain-Erweiterung, Voss)  
**QK:** QK-1 (B-0003)  
**Erstquelle:** SRC-0003  
**Primärevidenz:** Kahneman (2011) "Thinking, Fast and Slow"; Tversky/Kahneman (1974, 1979)

**Beschreibung:**  
Menschen verarbeiten Informationen in zwei Modi: System 1 (schnell, automatisch, assoziativ, emotional) und System 2 (langsam, deliberat, kognitiv aufwendig). Unter Stress oder emotionaler Belastung dominiert System 1 — was rationale Verhandlungen erschwert. Voss nutzt Techniken (Labeling, Mirroring), um von System 1 zu System 2 zu führen.

**Einschränkung (Voss-Erweiterung):**  
Voss integriert MacLean's Triune Brain-Modell (Reptiliengehirn / limbisches System / Neokortex), das in der modernen Neurowissenschaft als überholt gilt. Der E4-Kern (Kahneman's System 1/2) bleibt valide; die Triune-Brain-Erweiterung ist E1.

---

### MEC-0013 — Insight-Disruption durch Reframing

**E-Level:** E4 (Festinger's Kognitive Dissonanztheorie) + E3 (Dixon/Adamson CEB-Studie)  
**QK:** QK-1 (B-0004)  
**Erstquelle:** SRC-0004 (The Challenger Sale)  
**Primärevidenz:** Festinger (1957) Kognitive Dissonanz; Kahneman (1979, 2011); Dixon/Adamson (2011)

**Beschreibung:**  
Eine externe Perspektive, die eine bestehende Überzeugung eines Käufers erschüttert (Reframe), erzeugt kognitive Dissonanz und erhöht Aufmerksamkeit und Kaufbereitschaft. Der Verkäufer liefert dem Käufer eine Einsicht, die er ohne den Verkäufer nicht gehabt hätte — und die seinen Status Quo in ein neues Licht rückt.

**Verkaufsanwendung:**  
Commercial Teaching Pitch (T-0019): Der Verkäufer beginnt mit einer branchenspezifischen Einsicht (Warmer → Reframe), bevor er das Kundenproblem anspricht. Die Einsicht schafft Credibility und emotionale Öffnung für die weitere Konversation.

**Abgrenzung zu MEC-0001:**  
MEC-0001 (Selbstverbalisierung) wirkt durch Käufer-Selbstformulierung. MEC-0013 (Insight-Disruption) wirkt durch Verkäufer-externale Perspektive. Beide sind psychologisch gut begründet; ihre situativen Vorzüge sind empirisch ungeklärt (→ W-003).

---

### MEC-0014 — Konsens als Kaufsicherheit in Gruppen

**E-Level:** E3-Kandidat (CEB-Befragungsstudie, Gartner; Janis 1972 Groupthink)  
**QK:** QK-1 (B-0004) + Quell-Konvergenz B-0005 (CEB-Datenpunkt)  
**Erstquelle:** SRC-0004

**Beschreibung:**  
In konsensbasierten B2B-Kaufprozessen brauchen Entscheider internen Rückhalt als persönliche Risikoabsicherung ("widespread support from across their organization" als Top-1-Loyalitätstreiber, CEB). Ohne Konsens ist der Deal gefährdet — nicht wegen des Produkts, sondern wegen persönlicher Risikowahrnehmung der Entscheider.

**Fusions-Kandidat:**  
MEC-0014 ist konzeptuell verwandt mit MEC-0006 (Social Proof). Mögliche Unterscheidung: MEC-0006 = externe soziale Bestätigung (Referenzkunden); MEC-0014 = interne soziale Bestätigung (Buying Center). Fusion wird für Sprint 2 geprüft (→ F-004).

---

### MEC-0015 — Kognitive Überlastung durch Feature-Overload

**E-Level:** E5 (Miller's Law 1956) + E4 (Paradox of Choice, Schwartz 2004) + E2 (Demo-Anwendung, Keenan)  
**QK:** QK-1 (B-0005) + implizit B-0001, B-0004  
**Erstquelle:** SRC-0005 (Gap Selling)

**Beschreibung:**  
Wenn die präsentierte Informationsmenge die kognitive Kapazität des Käufers überschreitet (Miller 1956: 7±2 Chunks; Cowan 2001: 4±1), sinkt Verarbeitungstiefe — Käufer sortieren nicht, sie brechen ab oder verschieben die Entscheidung (Status-quo-Präferenz, MEC-0002).

**Verkaufsanwendung (Gap Selling):**  
Keenan's Regel: max. 6 Features in einer Demo. Keenan zitiert Miller's Law explizit als Begründung. Dies ist eine praktische Extrapolation — kein Demo-spezifisches Experiment bestätigt "6" als optimale Zahl.

**Evidenzlücke:**  
Miller's Law gilt für Working Memory allgemein (E5). Cowan (2001) revidierte die Zahl auf 4±1 Chunks. Die Anwendung auf Verkaufs-Demos ist E2.

---

## 7. Sämtliche Prinzipien (P-0001 bis P-0026)

### Prinzipien aus SPIN Selling (SRC-0001, B-0001)

---

**P-0001 — Selbstformulierte Erkenntnis als stärkste Überzeugungsform**  
*E3 | QK-1 (B-0001)*  
Käufer, die Probleme und Lösungsbedarfe selbst formulieren, sind stärker überzeugt als Käufer, denen die Lösung präsentiert wird. Need-Payoff Questions (T-0004) sind das operative Werkzeug. Basis: MEC-0001 (Selbstverbalisierung).

---

**P-0002 — Lösungswert folgt Problemgewicht**  
*E4-Kandidat | QK-4 (B-0001, B-0003, B-0004, B-0005)*  
Der wahrgenommene Wert einer Lösung ist direkte Funktion des wahrgenommenen Problemgewichts. Je schwerwiegender das Problem (Kosten, Konsequenzen, emotionale Last), desto wertvoller die Lösung — unabhängig von objektiven Produktmerkmalen. Basis: MEC-0002.

---

**P-0003 — Kontextgebundenheit von Verkaufstechniken**  
*E2 | QK-1 (B-0001)*  
Techniken, die in einfachen (Minor) Verkäufen wirksam sind, können in komplexen (Major) Verkäufen schaden. Insbesondere: Abschlusstechniken und geschlossene Fragen, die in Transaktionsverkäufen funktionieren, erzeugen in Major Sales Reaktanz (MEC-0003).

---

**P-0004 — Need Development als Kaufvoraussetzung**  
*E3 | QK-2 (B-0001, B-0005)*  
Kein Käufer ohne entwickelten expliziten Bedarf kauft. Discovery-Gespräche müssen latente implizite Bedarfe in explizite, selbstformulierte Kaufwünsche transformieren, bevor eine Lösungspräsentation wirksam ist.

---

**P-0005 — Benefit-Need-Linkage**  
*E3 | QK-1 (B-0001)*  
Ein Benefit (Nutzenvorteil) erzeugt Kaufbereitschaft nur, wenn er direkt an einen explizit formulierten Bedarf des Käufers geknüpft ist. Unverknüpfte Benefits erscheinen irrelevant oder erzeugen Einwände.

---

**P-0006 — Einwandprävention durch Bedarf-zuerst-Logik**  
*E2 | QK-1 (B-0001)*  
Die meisten Kaufeinwände entstehen, wenn Lösungen präsentiert werden, bevor der Bedarf vollständig entwickelt ist. Einwände sind oft Symptome schlechter Discovery, nicht echter Ablehnung.

---

**P-0007 — Verpflichtungssicherung statt Abschlusstechnik**  
*E2 | QK-1 (B-0001)*  
Klassische Abschlusstechniken (Trial Close, Assumptive Close) sind kontraproduktiv in Major Sales. Stattdessen: strukturierter "Advance" — eine klare nächste Aktion, die den Kaufprozess vorwärtsbewegt ohne Druck.

---

### Prinzipien aus Influence (SRC-0002, B-0002)

---

**P-0008 — Trigger-Design-Primat (Meta-Prinzip)**  
*E3 | QK-1 (B-0002)*  
Unter kognitiver Begrenzung (Zeitdruck, Unsicherheit, Komplexität) aktivieren Menschen automatische Compliance-Reaktionen auf Einzelmerkmale (Trigger). Trigger-Design ist Argumentationsarchitektur überlegen, wenn kognitive Kapazität des Käufers begrenzt ist. Meta-Prinzip über MEC-0005 bis MEC-0009.

---

**P-0009 — Vorab-Leistung als Compliance-Instrument**  
*E3 | QK-1 (B-0002)*  
Eine unverlangte Vorleistung (Information, Ressource, Geste) aktiviert MEC-0005 (Reziprozitätspflicht) und erhöht die Wahrscheinlichkeit, dass der Empfänger einer späteren Bitte entspricht.

---

**P-0010 — Commitment-Sequenzierung**  
*E3 | QK-1 (B-0002)*  
Kleine, frühe Commitments erhöhen die Wahrscheinlichkeit größerer späterer Commitments. Das Selbstbild des Käufers passt sich an seine öffentlich geäußerten Positionen an (MEC-0004). Strategisch: Mit kleinem, ungefährlichem "Ja" beginnen.

---

**P-0011 — Soziale Beweise: Unsicherheit + Referenzgruppen-Ähnlichkeit**  
*E3 | QK-1 (B-0002)*  
Social Proof wirkt stärker unter Unsicherheit und wenn die Referenzgruppe dem Käufer ähnlich ist. Allgemeine Kundenzahlen ("1.000 Kunden") wirken schwächer als spezifische, ähnliche Referenzen ("7 Unternehmen in Ihrer Branche mit Ihrem Umsatzvolumen").

---

**P-0012 — Rapport als kaufentscheidender Faktor (mit Kontextgrenze)**  
*E3 | QK-1 (B-0002)*  
Sympathie erhöht Kaufbereitschaft. Dieser Effekt ist im Labor gut belegt (MEC-0007). Wichtige Kontextgrenze (→ W-002): In komplexen B2B-Kaufprozessen ist Rapport kein hinreichender Differenzierer (→ A-0018, A-0029).

---

**P-0013 — Autorität durch Positionierung vor dem Gespräch**  
*E3 | QK-1 (B-0002)*  
Autoritätssignale (Titel, Credential, Referenz auf Expertise) wirken stärker, wenn sie vor dem Gespräch gesetzt werden — nicht im Gespräch selbst. Positionierung durch Dritte ist stärker als Eigenpositionierung.

---

**P-0014 — Referenzrahmen-Kontrolle ist Wert-Kontrolle**  
*E3 | QK-1 (B-0002)*  
Wer den Vergleichsrahmen kontrolliert, kontrolliert die Wertwahrnehmung. Preise, Leistungen und Risiken werden relativ wahrgenommen (MEC-0009). Der Anker (erste genannte Zahl oder Referenz) dominiert alle späteren Urteile.

---

**P-0015 — Knappheit: Zwei unabhängige Kanäle**  
*E3 | QK-1 (B-0002)*  
Knappheit wirkt über zwei Mechanismen: (1) erhöhter wahrgenommener Wert durch Seltenheit, (2) Reaktanz durch drohende Freiheitseinschränkung (MEC-0003). Beide wirken zusammen, können aber getrennt aktiviert werden. Nur legitime Knappheit ist ethisch und langfristig wirksam.

---

### Prinzipien aus Never Split the Difference (SRC-0003, B-0003)

---

**P-0016 — Tactical Empathy vor rationaler Verhandlung**  
*E3 | QK-1 (B-0003)*  
Emotionale Anerkennung (nicht Sympathie) ist Voraussetzung für rationale Kooperation. Solange das Gegenüber sich nicht verstanden fühlt, ist System 2 nicht zugänglich (MEC-0012). Tactical Empathy (Labeling + aktives Zuhören) schafft die emotionale Bereitschaft für sachliche Einigung.

---

**P-0017 — Autonomie-Illusion durch Fragen**  
*E3 | QK-1 (B-0003)*  
Offene, kalibrierte Fragen ("What makes this a challenge?") geben dem Gegenüber das Gefühl, die Situation zu kontrollieren — während sie tatsächlich die Richtung des Gesprächs lenken. Dies deaktiviert MEC-0003 (Reaktanz) und erhöht Kooperationsbereitschaft.

---

**P-0018 — Loss Framing vor Gain Framing**  
*E2 | QK-1 (B-0003)*  
In Verhandlungen ist es wirksamer, das Verlustrisiko bei Nicht-Einigung zu betonen (was verliert das Gegenüber?) als den Gewinn bei Einigung. Basis: MEC-0002 (Verlustaversion). Voss nennt dies "Negative Leverage".

---

**P-0019 — Commitment-Verifikation**  
*E2 | QK-1 (B-0003)*  
Verbale Zustimmung (Ja, sounds good) und echtes Commitment divergieren systematisch (A-0017). Rule of Three (T-0016) und Implementierungsfragen verifizieren echtes Commitment jenseits verbaler Bestätigung.

---

**P-0020 — Black-Swan-Orientierung**  
*E2 | QK-1 (B-0003)*  
In jeder Verhandlung existieren spielverändernde Informationen, die dem Verhandlungsführer nicht bekannt sind (A-0016). Jede Gesprächsphase ist potenziell eine Black-Swan-Recherche-Phase. Wer Black Swans findet, gewinnt strukturelle Verhandlungsvorteile.

---

### Prinzipien aus The Challenger Sale (SRC-0004, B-0004)

---

**P-0021 — Commercial Teaching Pitch als Wirkungssequenz**  
*E3 | QK-1 (B-0004)*  
Der sechsstufige Commercial Teaching Pitch (Warmer → Reframe → Rational Drowning → Emotional Impact → A New Way → Your Solution) ist die operationalisierte Form von Insight-Selling. Reihenfolge ist nicht verhandelbar: Reframe muss vor Lösungspräsentation kommen.

---

**P-0022 — TTC-Dreiklang als notwendige Bedingung**  
*E3 | QK-1 (B-0004)*  
Teach allein, Tailor allein oder Take Control allein sind unzureichend. Der Challenger Sale-Verkäufer ist nur dann überdurchschnittlich wirksam, wenn alle drei Komponenten kombiniert werden. Fehlende Komponenten sabotieren die anderen.

---

**P-0023 — Champion als internen Mobilizer befähigen**  
*E3 | QK-1 (B-0004)*  
In konsensbasierten B2B-Kaufprozessen reicht die Überzeugung des Champions nicht aus. Der Verkäufer muss den Champion befähigen, das interne Stakeholder-Netzwerk selbst zu überzeugen. "Don't just sell to your champion. Sell through your champion."

---

**P-0024 — Vertriebstransformation als organisationale Systemfähigkeit**  
*E3 | QK-1 (B-0004)*  
Challenger-Transformation scheitert ohne systemische Unterstützung. Reps, die TTC-Training erhalten, revertieren ohne Manager-Coaching, Marketing-Content und Incentive-Systeme innerhalb von 90 Tagen zum alten Verhalten.

---

### Prinzipien aus Gap Selling (SRC-0005, B-0005)

---

**P-0025 — Vollständige Gap-Diagnose vor Lösungspräsentation**  
*E2 | QK-2 (B-0001 implizit, B-0005 explizit)*  
Keine Lösung darf präsentiert werden, bevor Current State, Future State, Root Causes, Business Impact und intrinsische Motivation ("The Why") vollständig erschlossen und quantifiziert sind. Jede vorzeitige Lösungspräsentation adressiert einen unvollständig verstandenen Kunden.

**⚠ Methodologischer Widerspruch W-001:** P-0025 (Diagnose First) und P-0021 (Teach First) sind methodologisch nicht vollständig kompatibel. Widerspruch dokumentiert, unaufgelöst.

---

**P-0026 — Problem-Zentrierung als Differenzierungsprinzip (Gap Selling)**  
*E2 | QK-1 (B-0005)*  
Verkäufer differenzieren sich nicht durch Produkte oder Persönlichkeit, sondern durch Qualität der Problemdiagnose. Wer Root Causes benennt, die dem Käufer nicht bekannt waren, erzeugt Credibility durch Expertise-Wahrnehmung (A-0029, MEC-0008).

---

## 8. Sämtliche Modelle (MOD-0001 bis MOD-0005)

Modelle integrieren mehrere Mechanismen, Prinzipien und Techniken eines Buches in einer kohärenten Kausallogik. Jedes Modell ist buchspezifisch.

---

### MOD-0001 — SPIN Selling (Rackham, 1988)

**Kernthese:**  
In Major Sales entsteht Erfolg primär durch qualitativ hochwertige Fragen, die den Käufer dazu bringen, eigene Probleme zu erkennen, deren Bedeutung zu durchdringen und den Wunsch nach Lösung selbst zu formulieren — nicht durch Lösungspräsentation oder Abschlusstechniken.

**Vier Gesprächsphasen:**  
1. Preliminaries — geringe Erfolgswirkung
2. Investigating — Kernphase; SPIN-Fragen
3. Demonstrating Capability — nur Benefits, nach expliziten Bedarfen
4. Obtaining Commitment — strukturierter Advance, kein Closing

**SPIN-Fragetypen:**

| Kürzel | Funktion | Technik |
|---|---|---|
| S (Situation) | Kontext erfassen | T-0001 |
| P (Problem) | Implizite Bedarfe identifizieren | T-0002 |
| I (Implication) | Problemgewicht entwickeln | T-0003 |
| N (Need-Payoff) | Explizite Bedarfe formulieren lassen | T-0004 |

**Kausalstruktur:**
```
Situationsverständnis → Problemidentifikation → Impliziter Bedarf
→ Problemgewicht (Implication) → Lösungsdringlichkeit
→ Expliziter Bedarf (Need-Payoff) → Kaufbereitschaft
→ Benefit an Bedarf knüpfen → Angemessenen Advance sichern
```

**Grenzen:**  
Nicht ausreichend für Multi-Stakeholder-Komplexität. Forschung nicht peer-reviewed; entstammt Rackham's eigenem Unternehmen Huthwaite. Kulturelle Übertragbarkeit nicht systematisch geprüft.

---

### MOD-0002 — Cialdini's Sechs-Prinzipien-Modell der Compliance

**Kernthese:**  
Menschen verfügen über ein begrenztes kognitives Verarbeitungsbudget. Unter Zeitdruck, Unsicherheit und Informationsüberflutung aktivieren sie automatische Reaktionsprogramme auf spezifische Einzelmerkmale (Trigger). Sechs universell verankerte Prinzipien beschreiben die häufigsten solcher Trigger.

**Die sechs Prinzipien:**

| Nr. | Prinzip | Kern-MEC | Prinzip-Objekt |
|---|---|---|---|
| 1 | Reziprozität | MEC-0005 | P-0009 |
| 2 | Commitment & Konsistenz | MEC-0004 | P-0010 |
| 3 | Soziale Bewährtheit | MEC-0006 | P-0011 |
| 4 | Sympathie | MEC-0007 | P-0012 |
| 5 | Autorität | MEC-0008 | P-0013 |
| 6 | Knappheit | MEC-0003 | P-0015 |

*Hinweis: Das Modell mit 7 Prinzipien (inkl. Unity) gilt für Ausgabe 2021. SRC-0002 ist die Ausgabe 2007 mit 6 Prinzipien.*

**Rahmenkonzept:**
```
Kognitive Last / Zeitdruck / Unsicherheit
→ Heuristik-Aktivierung (Einzelmerkmal als Entscheidungsgrundlage)
→ Trigger wird gesetzt → Automatische Compliance-Reaktion
→ Entscheidung ohne vollständige Informationsverarbeitung
```

**Grenzen:**  
Feldbeobachtungen aus 1970er–1980er Jahren (USA). Kulturelle Generalisierbarkeit variiert. Replikationskrise betrifft einzelne zitierte Studien. Direkte B2B-Replikation fehlt.

---

### MOD-0003 — BCSM + Voss Verhandlungssystem (Never Split)

**Kernthese:**  
Verhaltensänderung setzt emotionale Akzeptanz voraus — nicht Überzeugung. Das Behavioral Change Stairway Model (BCSM, FBI) beschreibt einen sequenziellen Prozess, der beim Aufbau echter Empathie beginnt. Einfluss ist erst nach Rapport möglich.

**Die fünf BCSM-Stufen:**

| Stufe | Name | Kerntechnik | MEC |
|---|---|---|---|
| 1 | Aktives Zuhören | Mirroring (T-0012) | MEC-0011 |
| 2 | Empathie | Labeling (T-0013), Akkusationsaudit (T-0014) | MEC-0010 |
| 3 | Rapport | "That's right"-Ansteuerung | MEC-0007 |
| 4 | Einfluss | Kalibrierte Fragen (T-0015), Loss Framing (P-0018) | MEC-0002, MEC-0003 |
| 5 | Verhaltensänderung | Rule of Three (T-0016) | MEC-0004 |

**Kritischer Punkt:** Stufe 4 (Einfluss) ist erst nach Stufe 3 (Rapport) möglich. Jeder Versuch, Einfluss vor Rapport auszuüben, scheitert an System-1-Barrieren.

**Evidenzlevel gesamt:** E3 (BCSM ist intern entwickeltes FBI-Modell, nicht peer-reviewed publiziert; Einzelkomponenten variieren von E4 bis E1).

---

### MOD-0004 — Challenger Sale TTC-Modell (Dixon/Adamson, CEB)

**Kernthese:**  
Spitzenverkäufer differenzieren sich nicht durch starke Beziehungen oder breites Produktwissen, sondern durch drei kombinierte Verhaltensweisen: Teach (proaktiver Insight), Tailor (stakeholderspezifische Anpassung), Take Control (assertive Prozessführung).

**Empirische Basis:**  
N=6.000 Vertriebsmitarbeiter, 90 Unternehmen, CEB 2009 (Faktoranalyse, 44 Attribute, 5 Profile).

**Fünf Vertriebsprofile:**

| Profil | Anteil (%) | Stars (%) |
|---|---|---|
| Challenger | 27 | 40 |
| Lone Wolf | 18 | 25 |
| Hard Worker | 21 | 17 |
| Reactive Problem Solver | 14 | 12 |
| Relationship Builder | 21 | **7** |

**TTC-Komponenten:**

*Teach:* Commercial Teaching Pitch (T-0019): Warmer → Reframe (MEC-0013) → Rational Drowning (MEC-0002) → Emotional Impact → A New Way → Your Solution. Logik: "Lead to, not lead with your solution."

*Tailor:* Stakeholder-spezifische Botschaftsanpassung (T-0020). Champion-Enablement: Champion als interner Proxy-Verkäufer (P-0023).

*Take Control:* Assertive Prozessführung ohne Aggressivität. Früherkennung und Ausstieg aus strukturell verlorenen Prozessen (T-0021).

**Grenzen:**  
Proprietäre Daten (CEB). Keine externe Replikation. Kein RCT für TTC-Wirksamkeit. US-/westliche Enterprise-B2B Ausgangslage.

---

### MOD-0005 — Gap Selling Modell (Keenan, 2018)

**Kernthese:**  
Kaufentscheidungen entstehen ausschließlich aus einem quantifizierbaren Gap zwischen Current State und Future State. Die Aufgabe des Verkäufers ist Diagnostiker, nicht Überredungskünstler.

**Kern-Formel:** Future State – Current State = The Gap → je größer der Gap, desto stärker die Kaufmotivation.

**Kausalstruktur:**
```
[Vor-Gespräch] PIC erstellen → Hypothesen über Probleme / Root Causes
→ [Phase 1] Credibility aufbauen (MEC-0008)
→ [Phase 2] Current State erschließen (T-0023, 5 Elemente, Quantifizierungsregel)
→ [Phase 3] Future State + The Why erschließen (MEC-0002 aktiviert)
→ [Phase 4] Gap qualifizieren (COI > Investitionskosten? → A-0025)
→ [Phase 5] Entscheidungskriterien + Kaufprozess (MEC-0014)
→ [Phase 6] Demo / Lösung (T-0022, max. 6 Features, MEC-0015)
[Gesamter Prozess] Yes-Sequenz (MEC-0004)
```

**Konflikt mit MOD-0004:**  
Gap Selling (Diagnose First, P-0025) und Challenger Sale (Teach First, P-0021) sind methodologisch nicht vollständig kompatibel. Widerspruch W-001 ungelöst.

**⚠ Einschränkung:**  
Partielle PDF (fehlende Kapitel 1, 2, 6, 13, 15–20). Kernmethodik vollständig verfügbar, aber möglicherweise fehlende Konzepte.

---

## 9. Contradiction Matrix

Diese Matrix dokumentiert alle identifizierten Widersprüche zwischen den Büchern des Sprints. Widersprüche werden nicht geglättet.

---

### W-001 — Teach First vs. Diagnose First

**Typ:** Methodologisch  
**Status:** UNGELÖST — höchste Priorität für Sprint 2  
**Betroffene Bücher:** B-0004 (Challenger), B-0005 (Gap Selling)  
**Betroffene Objekte:** A-0020, P-0021, P-0025, MEC-0013, T-0019, T-0023

**Kern des Widerspruchs:**

The Challenger Sale: Der Verkäufer beginnt mit einer proaktiven Einsicht (Teach-Phase), die den Käufer reframt, bevor die vollständige Discovery abgeschlossen ist. Käufer kennen ihre Probleme bereits; was ihnen fehlt, ist eine neue Perspektive.

Gap Selling: Kein Pitch, keine Lehre, bevor nicht Current State, Future State und The Why vollständig erschlossen sind. Jede vorzeitige Lösungspräsentation adressiert einen unvollständig verstandenen Kunden.

**Soll der Verkäufer zuerst zum Kunden reden (Teach), oder soll er den Kunden zuerst reden lassen (Diagnose)?**

**Drei Erklärungsansätze (alle spekulativ, nicht bestätigt):**

*Erklärung 1 — Situationstyp:* Challenger für Käufer, die ihr Problem kennen; Gap Selling für Käufer, die ihr Problem noch nicht kennen. Problem: Beide Bücher beanspruchen Universalgültigkeit.

*Erklärung 2 — Verkäuferkompetenz:* Challenger setzt tiefe Branchenkenntnis für proaktive Insights voraus; Gap Selling setzt Hypothesenbildung (PIC) voraus. Problem: Beschreibt Kompetenzanforderung, keine Situationsstrategie.

*Erklärung 3 — Phasenmodell:* Challenger-Teach als Outreach-Türöffner; Gap-Discovery als Vertiefung im Gespräch. Problem: Gap Selling beschreibt auch Gap Prospecting als Problem-zentriert, nicht Insight-first.

**Forschungsstand:** Kein direkter empirischer Vergleich Challenger-Methodik vs. Gap-Selling-Methodik bekannt.

---

### W-002 — Liking als Differenzierer in B2B

**Typ:** Kontextuell  
**Status:** Teilaufgelöst (Kontextgrenze plausibel, aber nicht empirisch belegt)  
**Betroffene Objekte:** MEC-0007, A-0018, A-0029

**Widerspruch:** Cialdini (B-0002): Sympathie überträgt sich auf Produktbeurteilung (E4, Labor). Challenger + Gap Selling: Relationship Builder performen am schwächsten in B2B (A-0018 E3; A-0029 E2).

**Teilauflösung:** Kontextgrenze durch Transaktionskomplexität: MEC-0007 gilt stärker bei einfachen, schnellen Entscheidungen. In komplexem B2B mit 5,4 Entscheidern und langen Zyklen überlagern rationale Due-Diligence-Prozesse Liking-Signale. Diese Auflösung ist plausibel aber spekulativ — keine Studie misst den Komplexitätsschwellenwert.

---

### W-003 — Selbstverbalisierung vs. externe Perspektive

**Typ:** Methodologisch  
**Status:** Scheinkonflikt (phasengebunden), auf Discovery-Ebene offen

**Widerspruch:** SPIN (B-0001) MEC-0001: Käufer-Selbstformulierung überzeugt stärker als Verkäufer-Aussagen. Challenger (B-0004) MEC-0013: Externe Insight-Disruption durch Verkäufer erzeugt Credibility und Kaufmotivation.

**Phasenbezogene Auflösung:** MEC-0013 (Insight) → Öffnungsphase; MEC-0001 (Selbstverbalisierung) → Need-Formulierungsphase. In einem integrierten Modell: Teach (MEC-0013) → Tailor/Discovery (MEC-0001). Problem: Gilt nur, wenn Challenger-Sequenz korrekt ist — was W-001 voraussetzt.

---

### W-004 — Konstruktive Spannung vs. Spannungsabbau

**Typ:** Methodologisch  
**Status:** Kontextgebunden (aufgelöst)

**Widerspruch:** Challenger (B-0004): Konstruktive Spannung über Status Quo ist produktiv und darf nicht sofort aufgelöst werden. Voss (B-0003): Tactical Empathy reduziert emotionale Spannung als Voraussetzung für rationale Kooperation.

**Auflösung:** Verschiedene Spannungstypen: Challenger-Spannung = kognitive Dissonanz über das Problem (motiviert Kauf). Voss-Spannung = emotionale Abwehrhaltung in Verhandlung (blockiert Einigung). Beide Methoden haben recht für ihren jeweiligen Spannungstyp.

---

### W-005 — Qualitative vs. quantitative Discovery

**Typ:** Konzeptuell  
**Status:** Scheinkonflikt (komplementäre Zugänge)

**Voss:** Discovery durch emotionale Annäherung, Labeling, offene Fragen. Black Swans sind oft qualitativ. **Gap Selling:** Quantifizierungsregel: Keine offene Antwort ohne Zahlen akzeptieren.

**Auflösung:** Komplementär. Voss erschließt die emotionale Hinterbühne (Why). Gap Selling erschließt die quantifizierbare Vorderbühne (What + How much). Kombination möglich.

---

### Widerspruchs-Zusammenfassung

| ID | Typ | Status | Priorität |
|---|---|---|---|
| W-001 | Methodologisch | UNGELÖST | ⭐ Kritisch |
| W-002 | Kontextuell | Teilaufgelöst | Mittel |
| W-003 | Methodologisch | Scheinkonflikt (phasenbezogen) | Mittel |
| W-004 | Methodologisch | Kontextgebunden | Niedrig |
| W-005 | Konzeptuell | Scheinkonflikt | Niedrig |

---

## 10. Canonicalization Report

### 10.1 Definition

Canonicalization bezeichnet die Entscheidung, ob ein neues Buch einen bestehenden Mechanismus in neuem Kontext beschreibt (Extension) oder einen grundlegend neuen Mechanismus einführt (neue MEC-Anlage).

**Sprint-1-Canonicalization-Rate:** 7/22 = **31,8%**

### 10.2 Rate per Buch

| Buch | Neue MECs | Extended MECs | Rate |
|---|---|---|---|
| B-0001 SPIN | 4 | 0 | 0% (Baseline, keine Vorgänger) |
| B-0002 Influence | 5 | 0 | 0% |
| B-0003 Never Split | 3 | 3 | 50% |
| B-0004 Challenger | 2 | 2 | 50% |
| B-0005 Gap Selling | 1 | 2 | 67% |
| **Gesamt** | **15** | **7** | **31,8%** |

Die ansteigende Rate (0% → 0% → 50% → 50% → 67%) entspricht der Erwartung: Je mehr MECs existieren, desto häufiger können neue Bücher Extensions statt Neuanlagen liefern.

### 10.3 Wichtigste Canonicalization-Entscheidungen

**Beste Entscheidung:** MEC-0002-Extension (×3 über B-0003, B-0004, B-0005). Verlustaversion wurde dreimal angereichert statt dreimal neu angelegt. Dies ist der wichtigste Canonicalization-Erfolg des Sprints.

**Wichtigste Neuanlage:** MEC-0013 (Insight-Disruption). Hätte als Extension von MEC-0001 angelegt werden können, wäre aber konzeptuell falsch gewesen: Insight-Disruption (Verkäufer spricht) ist das Gegenteil von Selbstverbalisierung (Käufer spricht).

**Retrospektive Kritik:** MEC-0011 (Spiegelneuronen) wurde als eigenständiges Objekt angelegt, obwohl der wissenschaftliche Status E1 ist. Zukünftig: E1-Kandidaten als "hypothetisch" markieren und nicht als vollständige MECs anlegen.

### 10.4 Fusions-Kandidaten für Sprint 2

- MEC-0006 (Social Proof) + MEC-0014 (Konsens als Kaufsicherheit): Möglicherweise ein Mechanismus in zwei Kontexten (extern/intern).
- MEC-0010 (Amygdala-Regulation) + MEC-0012 (Dual Process): Überlappende Phänomene; Grenzziehung zu überprüfen.
- MEC-0011: Rückstufung oder Integration in MEC-0010 erwogen.

### 10.5 Canonicalization-Regeln für Sprint 2

1. MEC-Extension-Schwelle: Gleicher psychologischer Wirkpfad in neuem Kontext → Extension.
2. MEC-Neuanlage-Schwelle: Grundlegend anderer neuraler/kognitiver Prozess → Neue Anlage.
3. E1-Kandidaten: Als "(hypothetisch)" markieren, getrennt von E3+-MECs.
4. Angestrebte Sprint-2-Rate: ≥60%.

---

## 11. Emerging Principles

Emerging Principles sind Prinzipien, die erst durch die Kombination mehrerer unabhängiger Bücher sichtbar werden. Anforderungen: ≥2 unabhängige Quellen, nicht in bestehenden P-Objekten vollständig abgedeckt, praktische Handlungsrelevanz.

### Vier bestätigte Emerging Principles

Die formalen Objekte sind in Abschnitt 5 vollständig dokumentiert. Hier: die Begründung, warum diese Prinzipien erst durch den Sprint sichtbar wurden.

**P-S1-001 (COI als universeller Kaufmotivator):** QK-5. Jedes Buch hat eine Version — Implication Questions (SPIN), Prospect Theory (Cialdini), Negative Leverage (Voss), Rational Drowning (Challenger), COI-Explizitmachung (Gap). Erst die Kombination zeigt: Es ist kein Werkzeug — es ist das Grundgesetz der Kaufmotivation.

**P-S1-002 (Mikro-Commitment-Sequenz):** QK-4. SPIN beschreibt es für Need Development. Cialdini für Compliance. Gap Selling nennt es explizit "Yes-Sequenz". Erst zusammen wird sichtbar: Der Kauf ist keine einzelne Entscheidung, sondern eine akkumulierte Sequenz.

**P-S1-003 (Problem-Zentrierung als Differenzierung):** QK-4. SPIN sagt: Diagnosefragen wirken besser als Präsentationen. Challenger sagt: Insight differenziert (53% Loyalitätsstudie). Gap Selling sagt: Root-Cause-Kenntnis erzeugt Credibility. Voss sagt: Black Swans entscheiden. Erst zusammen: Problemkenntnis ist der strukturelle Wettbewerbsvorteil.

**P-S1-004 (Informationssparsamkeit):** QK-4. SPIN: Benefit nur nach Need. Cialdini: Fokus auf einen Trigger. Challenger: 6-Step-Pitch. Gap: max. 6 Demo-Features. Erst zusammen: Kognitive Beschränkung ist Wirkungsprinzip, nicht Hygiene.

### Drei abgelehnte Kandidaten

**Kandidat X (Rapport als Hygienefaktor):** Plausible Hypothese, aber kein Buch formuliert "Hygienefaktor" explizit. Kein neues P-Objekt — stattdessen als Forschungsfrage dokumentiert (F-008).

**Kandidat Y (Kaufentscheidungen sind emotional):** Zu unspezifisch. Verschiedene Bücher meinen verschiedene emotionale Dimensionen (MEC-0002, MEC-0010, A-0028). Nicht operational formulierbar.

**Kandidat Z (Vertrauen als Kaufvoraussetzung):** Triviale Allgemeingültigkeit ohne Sprint-spezifischen Mehrwert. Wird durch buchspezifische Objekte (MEC-0008, A-0029, MEC-0010) abgedeckt.

### Abgelehntes Meta-Modell MOD-S1

Ein Sprint-übergreifendes Verkaufsmodell (MOD-S1) wurde geprüft und explizit abgelehnt. Grund: W-001 (Teach First vs. Diagnose First) ist ungelöst. Ein MOD-S1 würde diesen Widerspruch glätten und eine methodologische Entscheidung implizieren, die empirisch nicht getroffen werden kann. MOD-S1 ist Sprint-2-Kandidat nach W-001-Auflösung.

---

## 12. Scientific Debt

Scientific Debt bezeichnet Wissensobjekte, bei denen die Evidenzbasis bekanntermaßen unvollständig ist und spätere Validierung vorgesehen ist. Ein Objekt mit Scientific Debt ist nicht falsch — es ist unvollständig gesichert.

**Kategorien:**

| Kategorie | Definition |
|---|---|
| Replikationsrisiko | Studie existiert, Replikationsstatus unklar oder negativ |
| Externe Validierung ausstehend | Prüfung durch externe KI oder Literaturrecherche noch nicht durchgeführt |
| Unbelegte Annahme | A-Objekt ohne direkte Primärquelle |
| Widersprüchliche Evidenz | Zwei Quellen widersprechen sich; kein Urteil möglich |
| Offene Forschungsfrage | Bekannte Lücke; kein Beleg vorhanden |
| Kulturelle Generalisierung | Befund aus einer Population; Übertragbarkeit ungesichert |

### Scientific Debt aus B-0001 (SPIN Selling)

| Objekt | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| P-0001–P-0007 | Externe Validierung ausstehend | Validierung der SPIN-Mechanismen gegen aktuelle Forschung | Mittel |
| MEC-0001–MEC-0004 | Externe Validierung ausstehend | Replikationsstatus zugrundeliegender Studien ungeprüft | Mittel |
| ST-Langer-Xerox | Replikationsrisiko | Langer (1978) "because"-Studie: Replikationsstatus in Replikationskrise unklar | Mittel |
| MOD-0001 | Offene Forschungsfrage | SPIN vs. Challenger Sale: empirischer Methodikvergleich fehlt | Niedrig |

### Scientific Debt aus B-0002 (Influence)

| Objekt | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MEC-0005–MEC-0009 | Externe Validierung ausstehend | Validierung gegen aktuelle Sozialpsychologie und B2B-Kontext | **Hoch** |
| ST-0033 (Langer-Xerox) | Replikationsrisiko | Replikationsstatus unklar | **Hoch** |
| ST-0035 (Regan 1971) | Replikationsrisiko | Reziprozitätsexperiment: Replikationsstatus ungeprüft | Mittel |
| A-0007 | Unbelegte Annahme | Evolutionäre Verankerung der Compliance-Prinzipien — keine direkte Primärquelle | Niedrig |
| P-0009, P-0012 | Offene Forschungsfrage | B2B-spezifische Reziprozitäts- und Rapport-Belege fehlen | Mittel |
| MEC-0009 vs. MEC-0002 | Widersprüchliche Evidenz | Abgrenzung Perzeptueller Kontrast vs. Verlustaversion in Grenzfällen | Niedrig |

### Scientific Debt aus B-0003 (Never Split)

| Objekt | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| MEC-0010 | Externe Validierung ausstehend | Lieberman (2007): Transfer Lab→Gespräch unbelegt; Fremd-Labeling nicht direkt getestet | **Hoch** |
| MEC-0011 | Replikationsrisiko | Spiegelneuronen-Verbindung zu menschlicher Kognition wissenschaftlich kontrovers | **Hoch** |
| MEC-0011 | Externe Validierung ausstehend | Stephens/Hasson (2010): Transfer auf aktives Mirroring unbelegt | **Hoch** |
| MEC-0012 (Triune Brain) | Unbelegte Annahme | MacLean's Triune Brain-Modell gilt als überholt | Mittel |
| T-0013 (Labeling-Technik) | Externe Validierung ausstehend | Praktische Wirksamkeit von Labeling in Verkaufsgesprächen vs. Verhandlung unbelegt | Mittel |

### Scientific Debt aus B-0004 (Challenger Sale)

| Objekt | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| A-0019 (53% Loyalität) | Externe Validierung ausstehend | CEB-Daten: unabhängige Replikation fehlt; proprietäre Methodik | **Hoch** |
| A-0020 (Kunden wollen gelehrt werden) | Widersprüchliche Evidenz | W-001 ungelöst — Gegenbefund durch P-0025 | **Hoch** |
| MEC-0013 | Externe Validierung ausstehend | Insight-Disruption: Wirksamkeit gegenüber Selbstverbalisierung ungeklärt | Mittel |
| MEC-0014 | Externe Validierung ausstehend | Konsens als Kaufsicherheit: keine B2B-spezifische Primärstudie | Mittel |
| P-0023, P-0024 | Offene Forschungsfrage | Champion-Enablement-Dynamik: empirisch nicht isoliert gemessen | Niedrig |

### Scientific Debt aus B-0005 (Gap Selling)

| Objekt | Kategorie | Beschreibung | Priorität |
|---|---|---|---|
| P-0025, P-0026, MOD-0005 | Offene Forschungsfrage | Keine Primärforschung zu Gap-Selling-Methodik; rein practitioner-basiert | Mittel |
| MEC-0015 (6-Feature-Regel) | Offene Forschungsfrage | Miller's Law auf Demo-Kontext extrapoliert, nicht direkt repliziert | Mittel |
| A-0024–A-0029 | Unbelegte Annahme | Alle Gap-Selling-Annahmen ohne Primärforschung | Mittel |
| ⚠ Partielle Quelle | Quellengrenze | Fehlende Kapitel 1, 2, 6, 13, 15–20 im PDF | Hoch |

---

## 13. Research Agenda

Priorisierte Forschungsagenda für Sprint 2. Grundlage: Scientific Debt, Widersprüche und offene Fragen aus Sprint 1.

**Tier 1 — Kritisch** (muss vor Sprint-2-Bucheingabe eingeordnet sein):

### F-001 — W-001: Teach First vs. Diagnose First

**Frage:** Unter welchen Bedingungen liefert Discovery-First vs. Insight-First bessere B2B-Verkaufsergebnisse?

**Forschungswege:**
1. Meta-Analyse: Publizierte Studien zu "Insight-First Selling" vs. "Needs-Based Selling"
2. Dritte-Quelle-Prüfung: The JOLT Effect (Dixon 2022) als wahrscheinlichste Auflösungsquelle
3. Hypothesenformalisierung: H-001 als explizit spekulatives Statement, wenn keine Primärquelle gefunden

**Deliverable:** Entweder F-001 durch Primärquelle geschlossen — oder H-001 als nicht gesichertes Statement angelegt.

---

### F-002 — MEC-0010 und MEC-0011: Neurowissenschaftliche Validierung

**Frage (MEC-0010):** Gibt es Peer-Review-Evidenz für Amygdala-Regulation durch Labeling in Gesprächssituationen?

**Frage (MEC-0011):** Wie ist der aktuelle wissenschaftliche Konsens zu Spiegelneuronen beim Menschen?

**Entscheidungsmatrix nach Review:**
- Bestätigt → E-Level updaten
- Nicht bestätigt → E1-Hypothese; abhängige Techniken-Objekte anpassen
- MEC-0011 widerlegt → in MEC-0010 integrieren oder als "(veraltet)" markieren

---

**Tier 2 — Hoch:**

### F-003 — Cialdini-MECs im B2B-Kontext

**Frage:** Sind MEC-0005 bis MEC-0009 im B2B-Komplex-Verkauf mit vergleichbarer Stärke wie im Labor repliziert?

Besonderer Fokus: MEC-0007 (Liking) wegen stärkster Kontraindikation durch andere Sprint-Bücher.

### F-004 — Fusions-Kandidaten MEC-0006/MEC-0014 und MEC-0010/MEC-0012

**Frage:** Sind diese Paare ein Mechanismus in zwei Kontexten (Fusion) oder zwei verschiedene Mechanismen?

Kriterium: Gleicher psychologischer Wirkpfad → Fusion; verschiedene Wirkpfade → Beibehaltung.

### F-005 — W-002: Liking-Schwelle in B2B

**Frage:** Ab welcher Transaktionskomplexität verliert MEC-0007 seine Wirkung als Differenzierer?

---

**Tier 3 — Mittel:**

| ID | Frage | Betroffene Objekte |
|---|---|---|
| F-006 | Langer-Xerox 1978: Replikationsstatus? | MEC-0001 |
| F-007 | Rackham SPIN-Studien-Designdetails: verblindete Beobachtungen? | SRC-0001, MEC-0001 |
| F-008 | Rapport als Hygienefaktor: formalisierbar? | MEC-0007, A-0018, A-0029 |
| F-009 | 6-Feature-Regel: Primärevidenz jenseits Miller's Law? | MEC-0015, T-0022 |

---

**Tier 4 — Niedrig / Verschiebbar:**

| ID | Frage |
|---|---|
| F-010 | Verkaufsforschung 2019–2025: Was ist seit den Sprint-Büchern erschienen? |
| F-011 | Pre-Suasion (Cialdini 2016) als Ergänzungsquelle für MEC-0005–0009? |
| F-012 | CEB-Rohdaten (N=6.000): Öffentlich zugänglich oder publiziert? |

---

**Buchempfehlungen Sprint 2:**

| Rang | Titel | Autor | Jahr | Relevanz |
|---|---|---|---|---|
| 1 | The JOLT Effect | Matthew Dixon | 2022 | Direkte Adressierung W-001; Dixon als Challenger-Koautor |
| 2 | Fanatical Prospecting | Jeb Blount | 2015 | Test P-S1-003 in Outreach; Gap Prospecting-Parallelität |
| 3 | The Psychology of Selling | Brian Tracy | 2004 | Klassiker; Test MEC-0002/MEC-0004 als universal |
| 4 | Sell the Way You Buy | David Priemer | 2020 | Käuferperspektive + Neurowiss.; Test MEC-0010 aus Nicht-Voss-Quelle |
| 5 | Predictable Revenue | Aaron Ross | 2011 | Outbound-Spezifika; Ergänzung ST-0148 |

---

## 14. Offene wissenschaftliche Fragen

Dieser Abschnitt fasst die zentralen wissenschaftlichen Fragen zusammen, die der Sales Codex nach Sprint 1 offen hält. Diese Fragen sind nicht rhetorisch — sie markieren echte Lücken im Wissensstand.

### 14.1 Methodologische Kernfrage

**Die wichtigste offene Frage des Sprints:**

Unter welchen Bedingungen ist Insight-First-Selling (Challenger: proaktiver Reframe vor Discovery) dem Diagnose-First-Selling (Gap Selling: vollständige Discovery vor jeder Lösungspräsentation) überlegen — und umgekehrt?

Diese Frage ist nicht beantwortbar aus dem vorliegenden Quellmaterial. Beide Ansätze beanspruchen Universalgültigkeit für B2B-Komplex. Beide haben praktische Evidenz. Ein direkter Vergleich fehlt vollständig (W-001).

### 14.2 Mechanismus-Übertragungsfragen

**Frage 1:** Sind Cialdini's Compliance-Mechanismen (MEC-0005–MEC-0009), die unter Laborbedingungen mit Einzelentscheidern in Konsumgüterkontexten repliziert wurden, in gleichem Maß wirksam in B2B-Kaufentscheidungen mit 5,4 Entscheidern, Due-Diligence-Prozessen und 6-monatigen Entscheidungszyklen?

**Frage 2:** Gibt es eine messbare Schwelle der Transaktionskomplexität, ab der MEC-0007 (Liking als Kauftreiber) von Expertise/Insight als Hauptdifferenzierer abgelöst wird?

**Frage 3:** Ist MEC-0010 (Amygdala-Regulation durch Labeling) im Gespräch wirksam? Lieberman (2007) maß Amygdala-Reaktion beim passiven Betrachten von Emotionsfotos — nicht beim Empfang von Labeling-Aussagen in einem Gespräch.

### 14.3 Neurowissenschaftliche Validierungsfragen

**Frage 4:** Welchen Status hat die Spiegelneuronen-Hypothese (MEC-0011) in der aktuellen Neurowissenschaft? Die ursprünglichen Rizzolatti-Befunde (Makaken) wurden für die menschliche soziale Kognition und Empathie extrapoliert — ist diese Extrapolation belegt oder widerlegt?

**Frage 5:** Ist MacLean's Triune Brain-Modell (Reptiliengehirn/limbisches System/Neokortex), das Voss zur Erklärung von MEC-0012 nutzt, in der aktuellen Neurowissenschaft noch vertretbar?

### 14.4 Methodik-Fragen der Sprint-Quellen

**Frage 6:** Waren Rackhams 35.000 SPIN-Beobachtungen verblindete Ratings (Beobachter wussten nicht, welche Gespräche zu Erfolgen führten) oder war der Rater informiert? Diese Frage beeinflusst das Evidenzlevel von SRC-0001.

**Frage 7:** Sind die CEB-Daten (N=6.000, A-0018, A-0022) öffentlich zugänglich oder unabhängig repliziert? Der wichtigste Einzelbefund des Challenger Sale (53% Loyalitätssplit) basiert auf proprietären Daten.

**Frage 8:** Sind die Cialdini-Kernstudien (Regan 1971 Reziprozitätsstudie, Langer 1978 Xerox-Studie) in der post-Replikationskrise Sozialpsychologie repliziert worden?

### 14.5 Strukturelle Modellfragen

**Frage 9:** Können die fünf Sprint-Methoden (SPIN, Cialdini, Voss/BCSM, Challenger TTC, Gap Selling) in einem kohärenten integrierten Verkaufsmodell kombiniert werden — und wenn ja, welche Sequenz der Phasen wäre wissenschaftlich begründbar?

**Frage 10:** Ist das Relationship-Builder-Profil (7% Stars in CEB-Studie) universell schwach — oder nur in den Enterprise-B2B-Märkten, die CEB 2009 untersuchte? Gilt das Ergebnis für SMB, Transaktionsgeschäft oder andere Kulturräume?

---

## 15. Anhang: Statistik des Sales Codex

### 15.1 Gesamtstatistik Sprint 1

| Kennzahl | Wert |
|---|---|
| Verarbeitete Bücher | 5 |
| Zeitraum der Quellen | 1984–2018 |
| Gesamtobjekte | 254 |
| Statements (ST) | 149 |
| Annahmen (A) | 29 |
| Mechanismen gesamt | 22 (15 neu + 7 Extensions) |
| Prinzipien (P) | 26 (buchspezifisch) + 4 Meta-Prinzipien (P-S1) |
| Techniken (T) | 25 |
| Modelle (MOD) | 5 |
| Widersprüche (W) | 5 (1 ungelöst, 1 teilaufgelöst, 3 aufgelöst/Scheinkonflikt) |
| Meta-Prinzipien (Sprint) | 4 (P-S1-001 bis P-S1-004) |
| Abgelehnte Meta-Prinzip-Kandidaten | 3 (Kandidaten X, Y, Z) |
| Abgelehnte Objekte | MOD-S1 (integriertes Modell) |
| Sprint-Canonicalization Rate | 31,8% |
| Research-Agenda-Fragen | 12 (F-001 bis F-012) |

### 15.2 Evidenzverteilung der Mechanismen

| E-Level | Mechanismen | IDs |
|---|---|---|
| E5 | 1 (anteilig: MEC-0015 hat E5-Grundlage) | MEC-0015 (Miller's Law) |
| E4 | 10 | MEC-0001, MEC-0002, MEC-0003, MEC-0004, MEC-0005, MEC-0006, MEC-0007, MEC-0008, MEC-0009, MEC-0012 (Kahneman-Teil) |
| E3 | 3 | MEC-0010 (E2-Kandidat), MEC-0013, MEC-0014 |
| E2 | 1 | MEC-0010 (Transfer-Ebene) |
| E1 | 1 | MEC-0011 (Spiegelneuronen) |

### 15.3 Quellen-Konfidenz der Mechanismen

| QK-Level | Mechanismen | Anteil |
|---|---|---|
| QK-5 | MEC-0002 | 1 (7%) |
| QK-3 | MEC-0004 | 1 (7%) |
| QK-2 | MEC-0001 (mit Cialdini), MEC-0003, MEC-0007 | 3 (20%) |
| QK-1 | MEC-0005, MEC-0006, MEC-0008, MEC-0009, MEC-0010, MEC-0011, MEC-0012, MEC-0013, MEC-0014, MEC-0015 | 10 (66%) |

### 15.4 Evidenzverteilung der Meta-Prinzipien

| ID | E-Level | QK |
|---|---|---|
| P-S1-001 | E4 (allg.) + E3 (3 Methoden) | QK-5 |
| P-S1-002 | E4 (Festinger) + E3 (3 Methoden) | QK-4 |
| P-S1-003 | E3 (CEB A-0019) + E2 (methodol. Konvergenz) | QK-4 |
| P-S1-004 | E5 (Miller's Law) + E2 (Konvergenz) | QK-4 |

### 15.5 Evidenz-Rangliste (Top 8)

| Rang | Objekt | E-Level | QK | Begründung |
|---|---|---|---|---|
| 1 | MEC-0002 | E4 (Lab) + E3 (3 Methoden) | QK-5 | Kahneman/Tversky + 4 Bücher |
| 2 | P-0002 / P-S1-001 | E4-Kandidat | QK-4–5 | 4–5 Bücher, konsistent über 40 Jahre |
| 3 | MEC-0004 | E4 (Lab) + E3 (3 Methoden) | QK-3 | Festinger + 3 Bücher |
| 4 | MEC-0005–0009 | E4 (Lab) | QK-1 | Hoch im Labor; B2B-Transfer ungesichert |
| 5 | A-0018 | E3 | QK-2 | CEB (N=6.000) + Gap Selling |
| 6 | MEC-0001 | E3–E4 (Lab) | QK-1 | Bem + SPIN; keine Folgebestätigung |
| 7 | MEC-0013 | E4 (Dissonanz) + E3 (CEB) | QK-1 | Sehr plausibel; nur Challenger |
| 8 | MEC-0015 | E5 (Miller) + E2 (Demo) | QK-1 | Starke Grundlage; Demo-Transfer E2 |

### 15.6 Nächste freie IDs

| Typ | Nächste ID |
|---|---|
| ST | ST-0150 |
| A | A-0030 |
| MEC | MEC-0016 |
| P | P-0027 |
| T | T-0026 |
| MOD | MOD-0006 |
| VAL | VAL-0006 |
| SRC | SRC-0006 |

---

## Dokumentabschluss

**Erstellt:** 2026-07-01  
**Grundlage:** Alle Quell-Dateien des Sales Codex Repository, Sprint S1-SYNTHESIS  
**Enthaltene Repository-Dokumente:** synthesis.md, contradiction_matrix.md, canonicalization_report.md, evidence_upgrade_report.md, emerging_principles.md, research_agenda.md, SCIENTIFIC_DEBT.md, MEC-0001 bis MEC-0015, P-0001 bis P-0026, P-S1-001 bis P-S1-004, MOD-0001 bis MOD-0005, CURRENT_STATE.md  
**Modifiziert nach Erstellung:** Keine Repository-Dateien werden nach Erstellung dieses Dokuments verändert.

---

*Sales Codex — Evidenzbasiertes Wissen über Vertrieb, Verkauf, Verhandlung und Käuferpsychologie*  
*Peer-Review-Paket SCRP-0001 | Sprint S1*
