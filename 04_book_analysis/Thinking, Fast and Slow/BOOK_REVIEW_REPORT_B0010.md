# BOOK REVIEW REPORT — B-0010: Thinking, Fast and Slow

## Report-Metadaten

| Feld | Wert |
|---|---|
| Report-ID | BOOK_REVIEW_REPORT_B0010 |
| Buch-ID | B-0010 |
| Titel | Thinking, Fast and Slow |
| Autor | Daniel Kahneman |
| Jahr | 2011 |
| Quellenklasse | A+ |
| Sprint | Sprint 2 |
| Erstellt | 2026-07-01 |
| Status | Abgeschlossen |

---

## Zusammenfassung der erstellten Knowledge Objects

### Statements (8)

| ID | Titel | Evidenz | QK |
|---|---|---|---|
| ST-0194 | System 1 dominiert Urteils- und Kaufentscheidungen; S2 rationalisiert post-hoc | E5 | QK-5 |
| ST-0195 | Anchoring-Effekt: Bezugszahlen verankern Schätzungen systematisch (zwei Mechanismen) | E5 | QK-5 |
| ST-0196 | WYSIATI: System 1 baut kohärente Urteile ohne Berücksichtigung fehlender Evidenz | E5 | QK-5 |
| ST-0197 | Cognitive Ease: einfache Darstellung erhöht Glaubwürdigkeit und Sympathie | E4 | QK-4 |
| ST-0198 | Prospect Theory: Verluste wiegen ~2× so schwer wie Gewinne; S-Kurve der Wertfunktion | E5 | QK-5 |
| ST-0199 | Framing-Effekt: logisch äquivalente Optionen werden bei unterschiedlicher Formulierung unterschiedlich bewertet | E5 | QK-5 |
| ST-0200 | Expert Intuition valide nur in regulären Umgebungen mit Feedback (Kahneman/Klein) | E4 | QK-4 |
| ST-0201 | Planning Fallacy: systematische Unterschätzung von Kosten und Überschätzung von Benefits | E4 | QK-4 |

### Assumptions (2)

| ID | Titel | Status |
|---|---|---|
| A-0047 | Kaufentscheidungen sind primär System-1-Prozesse; Logik allein überzeugt nicht | Annahme — gut gestützt im Consumer-Kontext; B2B-Transfer E2 |
| A-0048 | Anker im Gespräch sollten proaktiv gesetzt werden — passives Warten überlässt Frame dem Käufer | Annahme — strategische Schlussfolgerung aus ST-0195 |

### Mechanismen (1 NEU + 2 EXTEND + 1 NSTD aufgelöst)

| ID | Titel | Status |
|---|---|---|
| MEC-0021 | Anchoring-Mechanismus (zwei Pfade: S1-Priming + S2-Adjustment) | NEU — E5 |
| MEC-0002 | Loss Aversion — SRC-0010 als Primärquelle; Prospect Theory vollständig | EXTEND |
| MEC-0012 | Dual-Process — SRC-0010 als kanonische Primärquelle; Cognitive Ease + WYSIATI integriert | EXTEND |
| MEC-0009 | NSTD-Marker "Anchoring-Quervergleich ausstehend" aufgelöst → Abgrenzung zu MEC-0021 dokumentiert | NSTD aufgelöst |

### Prinzipien (3)

| ID | Titel | Evidenz |
|---|---|---|
| P-0041 | System-1-kompatible Darstellung: emotional ansprechend bevor rational überzeugend | E4 |
| P-0042 | Ankerkontrolle: ersten numerischen Anker im Gespräch setzen | E4 |
| P-0043 | Outside View: Referenzklassenprognose statt Inside-View-Planung | E4 |

### Techniken (2)

| ID | Titel | Evidenz |
|---|---|---|
| T-0040 | Wert-Anker-Technik: ROI-Referenzpunkt vor Preisgespräch setzen | E4 |
| T-0041 | Cognitive-Ease-Gestaltung: Präsentation vereinfachen für S1-Resonanz | E4 |

### Modelle (1)

| ID | Titel | Status |
|---|---|---|
| MOD-0010 | Kognitive Bias-Landkarte für Kaufentscheidungen (Kahneman) | NEU — E5/E3 |

---

## Kanonisierungs-Statistik

| Kategorie | Gesamt | NEU | EXTEND | NSTD aufgelöst |
|---|---|---|---|---|
| Statements | 8 | 8 | 0 | 0 |
| Assumptions | 2 | 2 | 0 | 0 |
| Mechanisms | 4 | 1 | 2 | 1 |
| Principles | 3 | 3 | 0 | 0 |
| Techniques | 2 | 2 | 0 | 0 |
| Models | 1 | 1 | 0 | 0 |
| **Gesamt** | **20** | **17** | **2** | **1** |

**Canonicalization Rate B-0010:** 3/20 = 15% (2 EXTEND + 1 NSTD-Auflösung; 17 NEU)

Begründung: Kahneman liefert primäre wissenschaftliche Grundlage für mehrere bereits im Codex vorhandene Mechanismen — zwei MECs wurden daher mit SRC-0010 als Primärquelle ergänzt (EXTEND). Die konkreten Bias-Befunde (Anchoring, WYSIATI, Cognitive Ease, Framing) waren noch nicht als eigenständige Objekte im Codex.

---

## Scientific Debt (neu identifiziert)

| ID | Typ | Beschreibung | Priorität |
|---|---|---|---|
| SD-B010-001 | Replikationsrisiko | Priming-Forschung aus Kap. 4: mehrere Studien haben in der Replikationskrise nicht standgehalten. Kahneman hat dies 2012 öffentlich anerkannt. Betrifft MEC-0018 (Pre-Suasion Priming) als Querverbindung | Hoch |
| SD-B010-002 | Transferlücke | B2B-Sales-Transfer: Anchoring, Framing und Cognitive Ease sind im Lab und Consumer-Kontext gut belegt; B2B-spezifische Evidenz in professionellen Einkaufsprozessen schwächer | Mittel |
| SD-B010-003 | Offene Forschungsfrage | Expert Intuition in Enterprise Sales: Feedback-Loop-Qualität in langen B2B-Zyklen (6–18 Monate, multikausale Entscheide) nicht empirisch gemessen | Niedrig |

---

## W-001-Status nach B-0010

**Unverändert — OFFEN**

B-0010 ist Käufer-Psychologie, nicht Verkäufer-Methodik. MOD-0010 ist neutral. Kein Beitrag zur W-001-Auflösung.

---

## Retroaktiver Quellen-Upgrade durch B-0010

SRC-0010 ist ab jetzt die kanonische Primärquelle für:
- System 1/2 Dual-Process-Modell (MEC-0012)
- Prospect Theory und Loss Aversion (MEC-0002)
- Anchoring (MEC-0021 — neu angelegt)

Diese Präzisierung verbessert die Evidenzbasis des gesamten Codex: Bisherige Referenzierungen waren auf Sekundärquellen (Voss/Cialdini) aufgebaut; Kahneman als Primärforscher gibt diesen Mechanismen eine stärkere wissenschaftliche Grundlage.

---

## VAL-Status

VAL-0010: BESTANDEN (alle 7 Prüfpunkte, keine Blocker)

---

## Gesamt-Bewertung B-0010

**Wichtigste Beiträge für den Sales Codex:**

1. **Primärquellen-Upgrade** (MEC-0002, MEC-0012): Kahneman als Primärforscher stärkt die wissenschaftliche Basis für Loss Aversion und System 1/2 rückwirkend
2. **MEC-0021 (Anchoring)**: Löst einen seit B-0002 offenen NSTD-Marker; wichtiger Mechanismus für Preis- und Verhandlungsgestaltung
3. **ST-0196 (WYSIATI) + ST-0197 (Cognitive Ease)**: Neue konzeptuelle Werkzeuge für Präsentationsgestaltung mit E5/E4-Basis
4. **ST-0200 (Expert Intuition) + ST-0201 (Planning Fallacy)**: Einzige Quelle im Sprint, die Verkäufer-Biases thematisiert; wichtig für Prognosekalibrierung
5. **SD-B010-001 (Priming-Replikation)**: Aufdeckung einer Evidenzlücke, die auch MEC-0018 (Pre-Suasion) berührt

## Status

Abgeschlossen — Sprint 2 — 2026-07-01
