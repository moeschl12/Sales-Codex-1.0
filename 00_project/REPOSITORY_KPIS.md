# Repository KPIs — Sales Codex

**Dokumentklasse: Operational**  
Version: 1.0  
Stand: 2026-06-30

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

---

## Interpretation

**Canonicalization Rate:**
- 0% → Alle Mechanismen sind neu. Mögliches Signal für fehlende Querprüfung.
- >30% → Gute Wiederverwendung bestehender Strukturen. Wissensintegration funktioniert.

**Scientific Confidence:**
- <10% → Alle Erkenntnisse sind Quellenprinzipien (E1–E2). Externe Validierung erforderlich, bevor Techniken empfohlen werden.

**Scientific Debt wächst** mit jedem Buch bis zur Validierungsphase. Das ist kein Problem — es ist der ehrliche Zustand einer aufbauenden Wissensbasis.

---

*Stand: 2026-06-30. Wird nach jeder Buchanalyse aktualisiert.*
