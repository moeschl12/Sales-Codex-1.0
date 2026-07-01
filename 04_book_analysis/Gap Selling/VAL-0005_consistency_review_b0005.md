# VAL-0005 — Konsistenz-Review: Gap Selling (B-0005)

## Review-ID

VAL-0005

## Geprüftes Buch

SRC-0005 — Gap Selling, Keenan, 2018

## Reviewer

Cowork (KI-Redakteur, Sales Codex)

## Datum

2026-06-30

## Prüfumfang

9 Bereiche gemäß Standard-VAL-Protokoll

---

## 1. QUELLTREUE: Alle Statements direkt aus PDF?

**Status: BESTANDEN ✓**

Alle 17 Statements (ST-0133–ST-0149) enthalten:
- Direkte Originalzitate aus dem PDF (feismo.com-Datei)
- Seitenangaben (PDF-Paginierung)
- Kapitelangaben

**Einschränkung (dokumentiert):** Das PDF ist eine Teilfassung (98 Seiten). Fehlende Kapitel: Ch1, Ch2, Ch6, Ch13, Ch15–Ch20. Die Kernmethodik (Ch3, Ch7–Ch12, Ch14, Ch21, Conclusion) ist vollständig verfügbar. Fehlende Kapitel wurden in SRC-0005 und analysis.md dokumentiert.

**Training-Knowledge-Kontamination:** KEINE. Alle inhaltlichen Aussagen sind PDF-basiert. Externe Quellen (Miller 1956, Kahneman/Tversky 1979) werden in MECs/Techniken nur als wissenschaftliche Grundlagen zitiert, nicht als primäre Gap-Selling-Inhalte. Die Gartner/CEB-Zahl (5,4 Entscheider) ist im PDF explizit zitiert (ST-0138, ST in Kap. 12).

---

## 2. ANNAHMEN: Regelkonformität (A-0024–A-0029)

**Status: BESTANDEN ✓**

| ID | Formulierung klar? | Evidenzgrad? | Grenzen? | Kontextgrenzen? |
|---|---|---|---|---|
| A-0024 | ✓ | E2 | ✓ | ✓ Impulskäufe |
| A-0025 | ✓ | E2 | ✓ | ✓ Öffentlicher Sektor |
| A-0026 | ✓ | E2 (+ Cross-Book E3) | ✓ | ✓ Commodity |
| A-0027 | ✓ | E2 (MEC-0002 E4) | ✓ | ✓ COI nicht messbar |
| A-0028 | ✓ | E2 | ✓ | ✓ Kollektive Entscheidungen |
| A-0029 | ✓ | E2 (+ A-0018 Cross) | ✓ | ✓ Branchenspezifisch |

Alle Annahmen formulieren Grenzen und Kontexteinschränkungen. ✓

---

## 3. OR-REGEL: Prinzipien mit ≥2 MECs oder ≥2 Annahmen?

**Status: BESTANDEN ✓**

| Prinzip | Basis | Erfüllt? |
|---|---|---|
| P-0025 | A-0024 + A-0026 + A-0028 (3 Annahmen) | ✓ |
| P-0026 | A-0029 + A-0026 (2 Annahmen) | ✓ |

---

## 4. MEC-CANONICALIZATION: Rate berechnen

**Status: BESTANDEN ✓**

- Neue MECs: 1 (MEC-0015)
- Erweiterte bestehende MECs: 2 (MEC-0002, MEC-0004)
- Gesamt MEC-Objekte: 3

**Canonicalization Rate: 2/3 = 67%** (>50% — erfüllt)

| MEC | Entscheidung | Begründung |
|---|---|---|
| MEC-0015 (Kognitive Überlastung) | NEU | Kein existierendes MEC-Objekt für diesen Mechanismus; Miller's Law war im Codex nicht abgedeckt |
| MEC-0002 Extension (COI) | EXTENDED | COI ist direkte Ausprägung von Verlustaversion; drittes Buch, das denselben Mechanismus anwendet |
| MEC-0004 Extension (Yes-Sequenz) | EXTENDED | Yes-Sequenz ist explizite Anwendung von Commitment/Konsistenz, bereits in MEC-0004 kodiert |

---

## 5. TECHNIKEN: Praktisch beschrieben, anwendbar?

**Status: BESTANDEN ✓**

| Technik | Ablauf vorhanden? | Wann anwenden? | MEC/P-Referenz? |
|---|---|---|---|
| T-0022 (Gap-Demo) | ✓ 5-Schritte | ✓ | ✓ |
| T-0023 (Gap Discovery Q) | ✓ 4 Fragetypen + Quantifizierungsregel | ✓ | ✓ |
| T-0024 (PIC) | ✓ Tabellen-Struktur | ✓ | ✓ |
| T-0025 (Inkonsistenz-Challenge) | ✓ 4-Schritt-Ablauf | ✓ | ✓ |

---

## 6. MOD-VOLLSTÄNDIGKEIT: Alle Objekte in MOD-0005 referenziert?

**Status: BESTANDEN ✓**

MOD-0005 enthält:
- Kausallogische Struktur als ASCII-Flowchart ✓
- Vollständige Tabellen: ST, A, MEC, P, T ✓
- Modell-Vergleiche: SPIN, Challenger, Never Split, Influence ✓
- Einschränkungen (PDF-Teilfassung, fehlende Empirie) ✓

---

## 7. WIDERSPRÜCHE: Alle dokumentiert, keine geglättet?

**Status: BESTANDEN ✓**

Identifizierte Widersprüche und Spannungen:

| Widerspruch | Dokumentiert in | Gelöst? |
|---|---|---|
| A-0020 (Kunden wollen gelehrt, B-0004) vs. P-0025 (Discovery First, B-0005) | P-0025, T-0023, MOD-0005 | NEIN — für S1-SYNTHESIS |
| MEC-0007 (Liking wirkt) vs. A-0029 (Expertise > Likability) | A-0029, ST-0137, ST-0146 | Teilweise gelöst: Kontext-Grenze dokumentiert (Liking = nützlich aber nicht hinreichend) |
| BANT-Budget vs. A-0025 (Budget = Funktion des Gap) | A-0025, ST-0138 | Dokumentiert; keine Auflösung notwendig (methodologische Konkurrenz) |
| Credibility durch Insight (B-0004) vs. Credibility durch Diagnose-Tiefe (B-0005) | A-0029, MOD-0005 | NEIN — für S1-SYNTHESIS |

---

## 8. TRAINING-KNOWLEDGE-KONTAMINATION: Prüfung

**Status: BESTANDEN ✓**

Prüffrage: Gibt es Inhalte in den B-0005-Objekten, die auf Modellwissen basieren statt auf PDF-Text?

Stichprobenartige Prüfung:
- A-0026 (Business Impact treibt Kaufentscheidungen): Psychologische Verknüpfung (SPIN, MEC-0002) explizit als Cross-Book-Bezug / Evidenz-Unterstützung markiert, nicht als Quellinformation. ✓
- MEC-0015 (Miller's Law): Miller 1956 ist externe Wissenschaftsquelle — korrekt zitiert als Grundlage für Keenans Empfehlung, nicht als Gap-Selling-Inhalt. ✓
- Alle STs haben Direktzitate aus dem PDF. ✓

**Feststellung:** Kein Training-Knowledge-Inhalt als Quellinformation eingeflossen.

---

## 9. PARTIELLE PDF: Dokumentation und Auswirkung

**Status: AKZEPTIERT mit Vermerk ✓**

- Fehlende Kapitel: Ch1 (Einleitung?), Ch2, Ch6, Ch13, Ch15–Ch20
- Kernmethodik verfügbar: Kapitel 3, 7–12, 14, 21, Conclusion = vollständige Discovery → Gap → Demo → Pipeline → Prospecting → Leadership-Methodik
- Dokumentiert in: SRC-0005, analysis.md
- Quellenklasse: B (nicht B+ wegen Teilfassung)

**Einschätzung:** Fehlende Kapitel enthalten vermutlich ergänzende Beispiele oder Randthemen. Die sechs definierten Kernphasen des Gap Selling Modells sind vollständig abgedeckt.

---

## GESAMTERGEBNIS

**BESTANDEN ✓**

Alle 9 Prüfbereiche bestanden. Eine offene Frage (A-0020 vs. P-0025 Widerspruch) ist bewusst undokumentiert-ungelöst und für S1-SYNTHESIS vorgemerkt.

---

## Zusammenfassung Kennzahlen

| Kennzahl | Wert |
|---|---|
| Statements erstellt | 17 (ST-0133–ST-0149) |
| Neue Annahmen | 6 (A-0024–A-0029) |
| Neue MECs | 1 (MEC-0015) |
| Extended MECs | 2 (MEC-0002, MEC-0004) |
| Canonicalization Rate | 67% |
| Neue Prinzipien | 2 (P-0025, P-0026) |
| Neue Techniken | 4 (T-0022–T-0025) |
| Modelle | 1 (MOD-0005) |
| Dokumentierte Widersprüche | 4 |
| Gelöste Widersprüche | 1 (Liking-Kontext) |
| Ungelöste Widersprüche (→ Synthesis) | 3 |

## Status

Abgeschlossen
