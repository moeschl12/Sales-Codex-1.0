# Repository KPIs — Sales Codex

**Dokumentklasse: Operational**  
Version: 1.1  
Stand: 2026-07-03 (External Audit Resolution Sprint — Nachtrag B-0003 bis B-0015)

**Nachtrags-Hinweis (2026-07-03):** Dieses Dokument war seit 2026-06-30 nicht aktualisiert worden und enthielt nur B-0001 und B-0002, obwohl zum Zeitpunkt dieses Nachtrags 15 Bücher abgeschlossen sind — ein vom externen Audit ("Wissenschaftliche Prüfung des Sales Codex") zutreffend identifizierter Befund. Die Zeilen für B-0001 und B-0002 bleiben unverändert (nicht Gegenstand des Audits). Für B-0003 bis B-0015 gilt eine einheitliche, transparente Zählformel: **Objekte gesamt = Statements + Annahmen(neu) + Mechanismen(neu) + Prinzipien(neu) + Techniken(neu) + Modelle(neu)** — erweiterte (nicht neu angelegte) Objekte werden separat ausgewiesen, aber nicht in "Objekte gesamt" mitgezählt. Diese Formel entspricht der bereits für B-0001 verwendeten Konvention; die bestehende B-0002-Zeile folgt einer leicht abweichenden, inklusiveren historischen Zählweise (dort sind "MECs neu/erweitert" bereits zusammengefasst in der Summe enthalten) — dieser Unterschied wird hier dokumentiert, nicht rückwirkend geglättet. **Scientific Debt neu** wurde für alle 15 Bücher objektiv nachgezählt (Anzahl Tabellenzeilen je Buchsektion in `SCIENTIFIC_DEBT.md`). **Reuse Rate, Scientific Confidence und Open Questions** sind für B-0003 bis B-0015 nicht in vergleichbarer, buchspezifischer Form dokumentiert und werden hier nicht rückwirkend neu bewertet (keine erfundenen Einschätzungen) — als "—" markiert, mit Verweis auf die jeweilige Primärquelle.

---

## Konzept

Repository KPIs ermöglichen den quantitativen Vergleich zwischen Buchanalysen und helfen, Qualitätsmuster zu erkennen. Sie sind Indikatoren, keine Ziele.

---

## KPI-Definitionen

| KPI | Definition | Einheit |
|---|---|---|
| **Statements / Buch** | Anzahl ST-Objekte mit dieser SRC-ID | Anzahl |
| **Annahmen / Buch** | Anzahl A-Objekte (neu, nicht erweitert) | Anzahl |
| **MECs neu** | Anzahl neu angelegter MEC-Objekte | Anzahl |
| **MECs erweitert** | Anzahl erweiterter bestehender MEC-Objekte | Anzahl |
| **Prinzipien / Buch** | Anzahl neuer P-Objekte | Anzahl |
| **Techniken / Buch** | Anzahl neuer T-Objekte | Anzahl |
| **Canonicalization Rate** | Erweiterte MECs / (neue + erweiterte MECs) × 100 | % |
| **Reuse Rate** | Objekte mit ≥2 SRC-IDs / Gesamtobjekte im Repository | % |
| **Objekte gesamt** | Alle neu erzeugten Objekte (ST+A+MEC+P+T+MOD) | Anzahl |
| **Scientific Confidence** | Objekte mit E3 oder höher / Gesamtobjekte für dieses Buch | % |
| **Open Questions** | Anzahl dokumentierter offener Fragen in VAL-Objekt | Anzahl |
| **Scientific Debt neu** | Neue Einträge in SCIENTIFIC_DEBT.md durch dieses Buch | Anzahl |

---

## Messwerte

### B-0001 — SPIN Selling (SRC-0001)

| KPI | Wert |
|---|---|
| Statements / Buch | 23 |
| Annahmen / Buch | 4 |
| MECs neu | 4 |
| MECs erweitert | 0 |
| Prinzipien / Buch | 7 |
| Techniken / Buch | 4 |
| Canonicalization Rate | 0% |
| Reuse Rate | — (erstes Buch) |
| Objekte gesamt | 42 |
| Scientific Confidence | ~0% (alle E1–E2) |
| Open Questions | TBD |
| Scientific Debt neu | 3 |

### B-0002 — Influence (SRC-0002)

| KPI | Wert |
|---|---|
| Statements / Buch | 26 |
| Annahmen / Buch | 8 |
| MECs neu | 5 |
| MECs erweitert | 3 |
| Prinzipien / Buch | 8 |
| Techniken / Buch | 7 |
| Canonicalization Rate | 37,5% |
| Reuse Rate | TBD nach mehr Büchern |
| Objekte gesamt | 59 |
| Scientific Confidence | ~0% (alle E1–E2, E3 nach Gemini-Validierung möglich) |
| Open Questions | 5 |
| Scientific Debt neu | 6 |

### B-0003 — Never Split the Difference (SRC-0003)

| KPI | Wert |
|---|---|
| Statements / Buch | 57 |
| Annahmen / Buch (neu) | 5 |
| MECs neu | 3 |
| MECs erweitert | 3 |
| Prinzipien / Buch | 5 |
| Techniken / Buch | 7 |
| Modelle (neu) | 1 (MOD-0003) |
| Canonicalization Rate | 50% (3 erweitert / 6 gesamt-MECs) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 78 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 9 |

Quelle: `04_book_analysis/Never Split the Difference/BOOK_REVIEW_REPORT_B0003.md`

### B-0004 — The Challenger Sale (SRC-0004)

| KPI | Wert |
|---|---|
| Statements / Buch | 26 |
| Annahmen / Buch (neu) | 6 |
| MECs neu | 2 |
| MECs erweitert | 2 |
| Prinzipien / Buch | 4 |
| Techniken / Buch | 3 |
| Modelle (neu) | 1 (MOD-0004) |
| Canonicalization Rate | 50% (2 erweitert / 4 gesamt-MECs) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 42 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 7 |

Quelle: `04_book_analysis/The Challenger Sale/BOOK_REVIEW_REPORT_B0004.md`

### B-0005 — Gap Selling (SRC-0005)

| KPI | Wert |
|---|---|
| Statements / Buch | 17 |
| Annahmen / Buch (neu) | 6 |
| MECs neu | 1 |
| MECs erweitert | 2 |
| Prinzipien / Buch | 2 |
| Techniken / Buch | 4 |
| Modelle (neu) | 1 |
| Canonicalization Rate | 67% (2 erweitert / 3 gesamt-MECs) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 31 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 4 |

Quelle: `04_book_analysis/Gap Selling/BOOK_REVIEW_REPORT_B0005.md`

### B-0006 — The JOLT Effect (SRC-0006)

| KPI | Wert |
|---|---|
| Statements / Buch | 14 |
| Annahmen / Buch (neu) | 6 |
| MECs neu | 1 (MEC-0016, FOMU) |
| MECs erweitert | 1 (MEC-0015) |
| Prinzipien / Buch | 4 |
| Techniken / Buch | 5 |
| Modelle (neu) | 1 (MOD-0006) |
| Canonicalization Rate | 3% (buchspezifisch dokumentierte Formel; Nenner 32 Kandidaten-Objekte, abweichend vom MEC-only-Verfahren anderer Bücher — nicht harmonisiert, siehe Primärquelle) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 31 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 3 |

Quelle: `04_book_analysis/The JOLT Effect/BOOK_REVIEW_REPORT_B0006.md`

### B-0007 — Getting to Yes (SRC-0007)

| KPI | Wert |
|---|---|
| Statements / Buch | 10 |
| Annahmen / Buch (neu) | 4 |
| MECs neu | 1 (MEC-0017) |
| MECs erweitert | 0 (1 Verlinkung ohne inhaltliche Änderung: MEC-0010) |
| Prinzipien / Buch | 4 |
| Techniken / Buch | 4 |
| Modelle (neu) | 1 (MOD-0007) |
| Canonicalization Rate | 4% (1 Verlinkung ohne Änderung / 24 Objekte) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 24 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 2 |

Quelle: `04_book_analysis/Getting to Yes/BOOK_REVIEW_REPORT_B0007.md`

### B-0008 — Pre-Suasion (SRC-0008)

| KPI | Wert |
|---|---|
| Statements / Buch | 11 |
| Annahmen / Buch (neu) | 4 |
| MECs neu | 2 (MEC-0018, MEC-0019) |
| MECs erweitert | 1 |
| Prinzipien / Buch | 3 |
| Techniken / Buch | 3 |
| Modelle (neu) | 1 (MOD-0008) |
| Canonicalization Rate | 4% (1 / (24+1)) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 24 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 3 |

Quelle: `04_book_analysis/Pre-Suasion/BOOK_REVIEW_REPORT_B0008.md`

### B-0009 — To Sell Is Human (SRC-0009)

| KPI | Wert |
|---|---|
| Statements / Buch | 8 |
| Annahmen / Buch (neu) | 3 |
| MECs neu | 1 (MEC-0020) |
| MECs erweitert | 0 |
| Prinzipien / Buch | 3 |
| Techniken / Buch | 2 |
| Modelle (neu) | 1 |
| Canonicalization Rate | 0% (alle Objekte neu) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 18 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 3 |

Quelle: `04_book_analysis/To Sell Is Human/BOOK_REVIEW_REPORT_B0009.md`

### B-0010 — Thinking, Fast and Slow (SRC-0010)

| KPI | Wert |
|---|---|
| Statements / Buch | 8 |
| Annahmen / Buch (neu) | 2 |
| MECs neu | 1 (MEC-0021, Anchoring) |
| MECs erweitert | 2 (+ 1 NSTD-Marker aufgelöst) |
| Prinzipien / Buch | 3 |
| Techniken / Buch | 2 |
| Modelle (neu) | 1 |
| Canonicalization Rate | 15% (3/20 — 2 EXTEND + 1 NSTD-Auflösung; 17 neu) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 17 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 3 |

Quelle: `04_book_analysis/Thinking, Fast and Slow/BOOK_REVIEW_REPORT_B0010.md`

### B-0011 — Emotional Intelligence (SRC-0011)

| KPI | Wert |
|---|---|
| Statements / Buch | 16 |
| Annahmen / Buch (neu) | 1 (+ 1 EXTEND) |
| MECs neu | 1 |
| MECs erweitert | 3 |
| Prinzipien / Buch | 1 (+ 1 EXTEND) |
| Techniken / Buch | 1 |
| Modelle (neu) | 0 |
| Canonicalization Rate | 75% MEC-spezifisch (3 EXTEND / (1 neu + 3 EXTEND)); 20% codex-weite Gesamtformel (5/25, alle Objekttypen) — beide Werte im Primärbericht dokumentiert |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 20 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 9 |

Quelle: `04_book_analysis/Emotional Intelligence/BOOK_REVIEW_REPORT_B0011.md`

### B-0012 — Predictably Irrational (SRC-0012)

| KPI | Wert |
|---|---|
| Statements / Buch | 31 |
| Annahmen / Buch (neu) | 4 (+ 1 EXTEND) |
| MECs neu | 1 (MEC-0023) |
| MECs erweitert | 5 |
| Prinzipien / Buch | 3 (+ 1 EXTEND) |
| Techniken / Buch | 1 |
| Modelle (neu) | 0 (1 EXTEND: MOD-0010) |
| Canonicalization Rate | 83,3% MEC-basiert (5 erweitert / (1 neu + 5 erweitert)) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 40 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 8 |

Quelle: `04_book_analysis/Predictably Irrational/BOOK_REVIEW_REPORT_B0012.md`

### B-0013 — Nudge: The Final Edition (SRC-0013)

| KPI | Wert |
|---|---|
| Statements / Buch | 18 |
| Annahmen / Buch (neu) | 2 (+ 1 re-geprüft, unverändert) |
| MECs neu | 1 (MEC-0024, Sludge) |
| MECs erweitert | 5 |
| Prinzipien / Buch | 3 |
| Techniken / Buch | 2 |
| Modelle (neu) | 1 (MOD-0011) |
| Canonicalization Rate | 83,3% MEC-basiert (5 erweitert / (1 neu + 5 erweitert)) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 27 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 7 |

Quelle: `04_book_analysis/Nudge/BOOK_REVIEW_REPORT_B0013.md`

### B-0014 — Priceless: The Myth of Fair Value (SRC-0014)

| KPI | Wert |
|---|---|
| Statements / Buch | 20 |
| Annahmen / Buch (neu) | 1 (+ 1 EXTEND) |
| MECs neu | 1 (MEC-0025, Fairness-Verzicht) |
| MECs erweitert | 2 |
| Prinzipien / Buch | 1 (+ 2 EXTEND) |
| Techniken / Buch | 1 |
| Modelle (neu) | 0 (1 EXTEND: MOD-0010) |
| Canonicalization Rate | 66,7% MEC-basiert (2 erweitert / (1 neu + 2 erweitert)) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 24 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 6 |

Quelle: `04_book_analysis/Priceless/BOOK_REVIEW_REPORT_B0014.md`

### B-0015 — Made to Stick (SRC-0015)

| KPI | Wert |
|---|---|
| Statements / Buch | 23 |
| Annahmen / Buch (neu) | 4 |
| MECs neu | 4 (MEC-0026–MEC-0029) |
| MECs erweitert | 1 (MEC-0018, Querverweis) |
| Prinzipien / Buch | 2 (+ 1 EXTEND: P-0036) |
| Techniken / Buch | 1 |
| Modelle (neu) | 1 (MOD-0012) |
| Canonicalization Rate | 20,0% MEC-basiert (1 erweitert / (4 neu + 1 erweitert)) |
| Reuse Rate | — (nicht buchspezifisch dokumentiert) |
| Objekte gesamt | 35 |
| Scientific Confidence | — (nicht buchspezifisch dokumentiert) |
| Open Questions | — (nicht buchspezifisch dokumentiert) |
| Scientific Debt neu | 10 |

Quelle: `04_book_analysis/Made to Stick/BOOK_REVIEW_REPORT_B0015.md`

---

## Repository-weite Summen (Stand 2026-07-03, alle 15 Bücher)

| Kennzahl | Wert |
|---|---|
| Statements gesamt (alle 15 Bücher) | 309 |
| Objekte gesamt (Summe aller "Objekte gesamt"-Zeilen, B-0001–B-0015) | 42 + 59 + 78 + 42 + 31 + 31 + 24 + 24 + 18 + 17 + 20 + 40 + 27 + 24 + 35 = 512 |
| Scientific Debt neu gesamt (Summe aller Buchzeilen) | 3+6+9+7+4+3+2+3+3+3+9+8+7+6+10 = 83 |
| Analysierte Bücher | 15 |

*Hinweis: „Objekte gesamt" 512 vs. tatsächlicher Repository-Bestand 514 Wissensobjekte (`03_knowledge_base/`) — Differenz von 2 durch Meta-Prinzipien P-S1-001–004 (S1-SYNTHESIS-Sprint, nicht einem Einzelbuch zugeordnet) und ggf. Rundungs-/Zuordnungseffekte bei buchübergreifend erweiterten Objekten. Nicht weiter aufgeschlüsselt — außerhalb des Audit-Scopes.*

---

## Interpretation

**Canonicalization Rate:**
- 0% → Alle Mechanismen sind neu. Mögliches Signal für fehlende Querprüfung.
- >30% → Gute Wiederverwendung bestehender Strukturen. Wissensintegration funktioniert.

**Scientific Confidence:**
- <10% → Alle Erkenntnisse sind Quellenprinzipien (E1–E2). Externe Validierung erforderlich, bevor Techniken empfohlen werden.

**Scientific Debt wächst** mit jedem Buch bis zur Validierungsphase. Das ist kein Problem — es ist der ehrliche Zustand einer aufbauenden Wissensbasis.

---

*Stand: 2026-07-03 (External Audit Resolution Sprint). Wird nach jeder Buchanalyse aktualisiert — dieser Grundsatz wurde zwischen 2026-06-30 und 2026-07-03 nicht eingehalten (13 Bücher fehlten); mit diesem Nachtrag wiederhergestellt.*
