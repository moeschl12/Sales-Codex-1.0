# MOD-0003 — BCSM + Voss Verhandlungssystem

## Model ID

MOD-0003

## Source ID

SRC-0003

## Name

Behavioral Change Stairway Model (BCSM) und Voss' Verhandlungssystem

## Ursprung / Quelle

- BCSM: FBI Crisis Negotiation Unit (CNU), entwickelt intern auf Basis von Carl Rogers' Person-Centered Therapy (1940er–1950er). Rogers: "Unconditional Positive Regard" als Basis echter Verhaltensänderung.
- Voss' Verhandlungssystem: "Never Split the Difference" (2016) — Erweiterung des FBI-BCSM um konkrete Verhandlungstechniken und psychologische Mechanismen aus FBI-Praxis und neuerer Verhandlungsforschung.
- Primärquelle: ST-0082 (BCSM-Beschreibung), Kap. 5, PDF S. 131–132.

## Zweck

Das BCSM beschreibt, wie Verhandlungsführung Verhaltensänderung ermöglicht — nicht durch Überzeugung, sondern durch einen sequenziellen Prozess, der beim Aufbau echter Empathie beginnt. Voss' Verhandlungssystem integriert das BCSM als konzeptionelles Fundament und ergänzt es durch neurobiologisch begründete Techniken und taktische Frameworks (Ackerman, Kalibrierte Fragen, Black Swan).

**Kernthese des Modells:**
Verhaltensänderung setzt emotionale Akzeptanz voraus — nicht Überzeugung. Wer den Schritt von "Empathie" zu "Rapport" überspringt, kann keine echte Beeinflussung erreichen. "That's right" (ST-0080) ist der messbare Indikator für Stufe 4-5.

## Die fünf BCSM-Stufen

| Stufe | Name | Verhandlungs-Operative | Sales-Kontext |
|---|---|---|---|
| 1 | Aktives Zuhören | Mirroring (T-0012), strategisches Schweigen | Bedarfsanalyse, kein Reden über Lösung |
| 2 | Empathie | Labeling (T-0013), Akkusationsaudit (T-0014) | Einwand-Deeskalation, Verständnis signalisieren |
| 3 | Rapport | "That's right"-Ansteuerung, Summary (→ ST-0080) | Vertrauensaufbau, Gegenüber fühlt sich verstanden |
| 4 | Einfluss | Kalibrierte Fragen (T-0015), Ackerman (T-0017), Loss Framing (P-0018) | Preisverhandlung, Lösungsdesign |
| 5 | Verhaltensänderung | Rule of Three (T-0016), Implementierungsfragen | Commitment-Sicherung, Umsetzung |

**Kritischer Punkt:** Stufe 4 (Einfluss) ist erst nach Stufe 3 (Rapport) möglich. Jeder Versuch, Einfluss vor Rapport auszuüben, scheitert an System-1-Barrieren (→ MEC-0012) oder Reaktanz (→ MEC-0003).

## Annahmen

| A-ID | Name |
|---|---|
| A-0013 | Emotionen sind das primäre Verhandlungsmedium |
| A-0015 | Sicherheit und Kontrolle als primäre Verhandlungsbedürfnisse |
| A-0017 | Verbale Zustimmung und Commitment divergieren systematisch |
| A-0016 | In jeder Verhandlung existieren spielverändernde unbekannte Informationen |

## Enthaltene Prinzipien

| P-ID | Name | BCSM-Stufe |
|---|---|---|
| P-0016 | Tactical Empathy | 1–3 |
| P-0017 | Autonomie-Illusion durch Fragen | 3–4 |
| P-0018 | Loss Framing vor Gain Framing | 4 |
| P-0019 | Commitment-Verifikation | 5 |
| P-0020 | Black-Swan-Orientierung | 1–4 (durchgehend) |

## Enthaltene Techniken

| T-ID | Name | BCSM-Stufe |
|---|---|---|
| T-0012 | Mirroring | 1 |
| T-0013 | Labeling | 2 |
| T-0014 | Akkusationsaudit | 2 (präventiv) |
| T-0015 | Kalibrierte Fragen | 3–4 |
| T-0016 | Rule of Three | 5 |
| T-0017 | Ackerman-Modell | 4 |
| T-0018 | Negotiation One Sheet | Pre-Contact |

## Mechanismen

| MEC-ID | Name | BCSM-Stufe |
|---|---|---|
| MEC-0010 | Amygdala-Regulation durch Labeling | 2 |
| MEC-0011 | Neural Coupling durch Isopraxismus | 1–3 |
| MEC-0012 | Dual-Process System 1 → System 2 | 2–4 |
| MEC-0002 | Verlustaversion | 4 |
| MEC-0003 | Reaktanz | 3–4 (Deaktivierung) |
| MEC-0007 | Sympathieübertragung (Similarity) | 3 |

## Kausallogische Struktur

```
PRE-CONTACT
  Negotiation One Sheet (T-0018) → Hypothesenrahmen + Empathie-Vorbereitung
  
STUFE 1: AKTIVES ZUHÖREN
  Mirroring (T-0012) + Strategisches Schweigen
  → Neural Coupling (MEC-0011) entsteht
  → System-1-Reaktivität sinkt (MEC-0012)
  
STUFE 2: EMPATHIE
  Labeling (T-0013) + Akkusationsaudit (T-0014)
  → Amygdala-Regulation (MEC-0010)
  → System 2 wird zugänglich (MEC-0012)
  
STUFE 3: RAPPORT
  Summary → "That's right" (ST-0080)
  → Similarity-Sympathie (MEC-0007 ext.)
  → Reaktanz deaktiviert (MEC-0003)
  
STUFE 4: EINFLUSS
  Kalibrierte Fragen (T-0015) + Loss Framing (P-0018) + Ackerman (T-0017)
  → Loss Aversion aktiviert (MEC-0002)
  → Autonomie-Illusion (MEC-0003 positiv genutzt)
  
STUFE 5: VERHALTENSÄNDERUNG
  Rule of Three (T-0016) + Implementierungsfragen
  → Commitment-Verifikation (P-0019)
  → Echter Behavioral Change
  
DURCHGEHEND (alle Stufen):
  Black-Swan-Orientierung (P-0020): kalibrierte Exploration
```

## Bester Kontext

- Hochkomplexe Verhandlungen mit emotionaler Aufladung (Krisennegotiationen, schwierige Stakeholder, Preisverhandlungen mit persönlichem Einsatz)
- Multi-Session-Verhandlungen: BCSM-Stufen können sich über mehrere Gespräche erstrecken
- Verhandlungen mit unbekanntem oder misstrauischem Gegenüber
- Komplexer B2B-Vertrieb (Major Sales, wo Relationship-Aufbau Voraussetzung ist)

## Grenzen

- **Routine-Transaktionen:** In standardisierten, niedrig-emotionalen Verhandlungen ist das volle BCSM überdimensioniert — einzelne Techniken genügen
- **Extreme Zeitbeschränkung:** Stufen 1–3 brauchen Zeit; unter Zeitdruck können spätere Stufen direkt eingeleitet werden (mit Risiko)
- **Machtextrem-Situationen:** Wenn eine Seite absolute Macht hat und das Gegenüber keine Alternative, vereinfacht sich die Dynamik — BCSM-Ansatz nicht immer notwendig oder möglich
- ⚠ BCSM ist primär ein Sequenz-Modell: Wenn eine Stufe übersprungen oder halbherzig durchlaufen wird, können spätere Stufen kollabieren

## Konkurrierende Modelle

| Modell | Kernunterschied | Sales Codex Einordnung |
|---|---|---|
| Harvard-Schule (Fisher/Ury 1981) | BATNA/ZOPA-fokussiert, rational, "separate people from problem" | Ergänzend bei rationalen Verhandlungen; schwächer bei emotionaler Aufladung |
| SPIN Selling (Rackham, MOD-0001) | Kognitive Bedarfsentwicklung, keine explizite Emotions-Management-Sequenz | Komplementär: SPIN = Problembewusstsein erzeugen; BCSM = emotionale Bereitschaft erzeugen |
| Cialdini-Modell (MOD-0002) | Compliance durch Trigger-Aktivierung | Komplementär: Cialdini = Influence-Layer auf Stufe 4 des BCSM anwendbar |

## Canonicalisierungsentscheidung

Wurde geprüft, ob ein bestehendes MOD-Objekt dieses Modell bereits abdeckt?

| Geprüftes Objekt | Ergebnis | Begründung |
|---|---|---|
| MOD-0001 (SPIN) | Kein Overlap | SPIN = kognitive Bedarfsentwicklung; BCSM = emotionale Sequenz |
| MOD-0002 (Cialdini) | Kein Overlap | Cialdini = Trigger-basierte Compliance; BCSM = Rapport-erste Sequenz |

**Entscheidung:** Neu anlegen (MOD-0003)

## Quervergleich mit bestehenden MOD-Objekten

| MOD-ID | Vergleich | Abgrenzung |
|---|---|---|
| MOD-0001 | SPIN arbeitet mit kognitiven Fragen (SPIN = System 2); BCSM beginnt mit Emotion (System 1) | BCSM schafft die emotionale Bereitschaft, die SPIN-Fragen wirksam macht |
| MOD-0002 | Cialdini's Trigger wirken auf Stufe 4 (Einfluss) des BCSM | BCSM strukturiert den Prozess; Cialdini liefert Einfluss-Instrumente für eine spezifische Stufe |

## Evidenzlevel

E3 — BCSM ist intern entwickeltes FBI-Modell, nicht peer-reviewed publiziert. Einzelne Komponenten sind gut belegt: Aktives Zuhören (Rogers, E4), Labeling/Amygdala (Lieberman 2007, E3), Neural Coupling (Stephens 2010, E3), Loss Aversion (Kahneman/Tversky, E4). Integration zu Gesamtmodell: E2 (Voss-Praxis, qualitative Fallberichte).

## Codex-Interpretation

Das BCSM ergänzt MOD-0001 (SPIN) und MOD-0002 (Cialdini) um eine **Sequenz-Logik auf emotionaler Ebene**. Während SPIN erklärt, wie man das richtige Bedürfnis entwickelt, und Cialdini erklärt, welche Trigger Compliance auslösen, erklärt BCSM, wann und in welcher Reihenfolge Einfluss überhaupt möglich wird.

Die drei Modelle zusammen:
- **SPIN:** Was ist das Problem und wie groß ist es? (Kognition)
- **BCSM:** In welchem emotionalen Zustand ist das Gegenüber und wie wird er kooperativ? (Emotion)
- **Cialdini:** Welche automatischen Compliance-Trigger kann ich auf Stufe 4 nutzen? (Automatische Reaktion)

## Erweiterung: Präzisierung von „Vertrauen" in Stufe 3 (Rapport) — Research Program W-003

**[Ergänzt 2026-07-05 aus W-003 — Trust Formation & Relationship Marketing Research Project. Editor Decision 2026-07-05: Teilweise annehmen, siehe `06_research_program/completed/W003/06_EDITOR_DECISION.md`]**

Der Begriff „Vertrauensaufbau" in Stufe 3 des BCSM (siehe Kausallogische Struktur oben: „STUFE 3: RAPPORT ... → Similarity-Sympathie (MEC-0007 ext.) ... → Reaktanz deaktiviert (MEC-0003)") wurde bislang ohne mechanistische Fundierung verwendet. W-003 präzisiert: Diese Stufe entspricht überwiegend einer **affektiven** Trust-Bildung (im Sinne der bei MEC-0030 dokumentierten internen Differenzierung Cognitive/Affective Trust nach McAllister 1995) — aufgebaut über Mirroring, aktives Zuhören und Labeling, also über wiederholte, positiv erlebte Interaktion, nicht primär über explizite Kompetenz- oder Integritätsprüfung. Die in Stufe 4 (Einfluss) einsetzende Kalibrierte-Fragen-/Ackerman-Technik setzt demgegenüber bereits implizit eine gewisse **kognitive** Ability-Wahrnehmung voraus (der Verhandler wird als kompetent genug wahrgenommen, um komplexere Einflussversuche zu akzeptieren).

**Cross-Link:** MEC-0030 (Vertrauensbildung aus wahrgenommener Vertrauenswürdigkeit) liefert die mechanistische Grundlage, auf die sich „Vertrauen" in diesem Modell künftig präziser beziehen kann — insbesondere die dortige Ability/Benevolence/Integrity-Struktur. Dies ist eine begriffliche Präzisierung, keine inhaltliche Änderung der BCSM-Stufenlogik selbst.

**Kein E-Level-Wechsel** (bleibt E3/E2 gemäß bestehender Einstufung).

Vollständige Herleitung: `06_research_program/completed/W003/02_SCIENTIFIC_MASTER_REVIEW.md`, `04_THEORY_LANDSCAPE.md`, Repository Impact Analysis.

## Status

Entwurf — erstellt 2026-06-30 (SRC-0003); ergänzt 2026-07-05 (W-003 — Präzisierung „Vertrauen" in Stufe 3, Cross-Link zu MEC-0030)
