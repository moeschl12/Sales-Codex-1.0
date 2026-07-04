# Canonicalization Report — B-0011 (Emotional Intelligence, Goleman 1995)

## Zweck

Detaillierte Dokumentation aller Canonicalization-Entscheidungen der B-0011-Buchanalyse, gemäß Editor-Auftrag "Behavioral Science Expansion" — Priorität 1 (Kanonisierung vor Neuanlage). Ergänzt VAL-0011 und BOOK_REVIEW_REPORT_B0011.md um die geforderten strukturierten Einzelabschnitte.

**Formel (übernommen aus SPR-0001/canonicalization_report.md):** Canonicalization Rate = Extensions / (Neue Objekte + Extensions) × 100, bezogen auf Mechanismen (MECs) — die Objektkategorie, die im CKM primär kanonisierbar ist.

---

## 1. Neue Statements

**Anzahl:** 16
**ID-Bereich:** ST-0202 bis ST-0217

Alle 16 Statements sind buchspezifische Einzelaussagen (per CKM-Definition nicht kanonisierbar/erweiterbar — Statements werden immer neu angelegt, auch wenn ihr Inhalt zur Fundierung bestehender A/MEC/P-Objekte verwendet wird). 5 der 16 Statements dienten als Belegquelle für Erweiterungen bestehender Objekte (ST-0202/ST-0216 → MEC-0010; ST-0206/ST-0215 → MEC-0020; ST-0208/ST-0209 → MEC-0022/A-0049; ST-0210/ST-0211 → P-0016/P-0044).

---

## 2. Neue Assumptions

**Anzahl:** 1
**ID:** A-0049

A-0049 ("Emotionale Zustände übertragen sich unwillkürlich zwischen Interaktionspartnern") wurde als neue Annahme angelegt statt als Unterfall von A-0013 dokumentiert, weil beide Annahmen unterschiedliche Falsifizierungsbedingungen haben: A-0013 könnte falsch sein, während A-0049 richtig bleibt (Emotionen übertragen sich zwar unwillkürlich, steuern aber Entscheidungen nicht primär) und umgekehrt (Emotionen könnten Entscheidungen dominieren, ohne dass ein unwillkürlicher zwischenmenschlicher Übertragungskanal existiert). Gemäß CKM §3.2 ("Eine Annahme impliziert die andere logisch → als Unterfall dokumentieren") war dies hier NICHT der Fall — daher eigenständige Neuanlage gerechtfertigt.

Zusätzlich wurde A-0013 erweitert (siehe Abschnitt 4).

---

## 3. Neue Mechanismen

**Anzahl:** 1
**ID:** MEC-0022 — "Emotional Contagion durch unbewusste Facial-/Motor-Mimikry"

### Canonicalization-Rejection-Begründung (vollständig)

Geprüfter Kandidat für Erweiterung: **MEC-0011 (Neural Coupling durch Isopraxismus)**

| Kriterium | MEC-0011 (bestehend) | MEC-0022 (neu) |
|---|---|---|
| Stimulus (X) | Bewusst eingesetzte Mirroring-Technik (Verhandler spiegelt gezielt Wortwahl/Tonfall) | Unwillkürliche Wahrnehmung von Mimik/Motorik des Gegenübers, unabhängig von Technikeinsatz |
| Prozess (Y) | Hypothetisches "Neural Coupling" (Stephens/Hasson 2010, fMRT-Hirnsynchronisation bei Sprecher-Hörer-Dyaden) — E2/E1, wissenschaftlich umstritten | Facial-Feedback-Mechanismus (Motor-Mimikry → propriozeptives Feedback → Emotionsauslösung) — E3–E4, breit repliziert (Hatfield/Cacioppo/Rapson) |
| Reaktion (Z) | Rapport/Vertrautheitsgefühl durch bewusst wahrgenommene Synchronität | Tatsächliche Emotionsübernahme, auch ohne bewusste Wahrnehmung der Mimikry |
| Steuerbarkeit | Intentional, technikbasiert, trainierbar | Unwillkürlich, nicht direkt steuerbar (nur indirekt über eigene Emotionsregulation) |
| Kernevidenz | Stephens, Silbert & Hasson (2010), PNAS — Einzelstudie, E2 | Hatfield, Cacioppo & Rapson (1993, 1994) — theoretisch und empirisch breiter fundiert, E3–E4 |

**Prüfung der vier Bedingungen für MEC-Neuanlage (gemäß Editor-Auftrag):**

1. **Keine sinnvolle Kanonisierung möglich:** Erfüllt — MEC-0011 selbst dokumentiert bereits vor dieser Erweiterung, dass "Chartrand & Bargh (1999) und Lakin & Chartrand (2003) allgemeine unbewusste Verhaltensnachahmung solide belegen (E4) — das ist nicht dasselbe wie MEC-0011s spezifischer Gegenstand [bewusstes, gezieltes Mirroring]". Diese Lücke wird durch MEC-0022 nun explizit geschlossen, statt MEC-0011 inhaltlich zu verwässern.
2. **Unabhängiger Kausalmechanismus X→Y→Z, verschieden von allen bestehenden:** Erfüllt — siehe Vergleichstabelle oben; unwillkürliche Facial-Feedback-Kette ist mechanistisch verschieden von bewusster Technikanwendung (MEC-0011) und von Amygdala-Labeling (MEC-0010, das über explizite sprachliche Benennung wirkt, nicht über Mimikry).
3. **Unabhängige wissenschaftliche Evidenz:** Erfüllt — Hatfield/Cacioppo/Rapson-Forschungslinie ist eigenständig von der Stephens/Hasson-Neural-Coupling-Forschung und von der Lieberman-Labeling-Forschung.
4. **Keine bloße Umbenennung:** Erfüllt — MEC-0022 beschreibt eine andere Wirkrichtung (passiv, bidirektional zwischen beiden Gesprächspartnern) als MEC-0011 (aktiv, vom Verhandler ausgehend).

**Ergebnis:** Alle vier Bedingungen erfüllt → Neuanlage gerechtfertigt. Zusätzlich wurde MEC-0011 um einen expliziten Abgrenzungsvermerk zu MEC-0022 ergänzt (siehe Abschnitt 4), um zukünftige Verwechslung zu vermeiden.

**Keine weiteren neuen Mechanismen wurden angelegt.** Alle übrigen buchspezifischen Befunde mit Mechanismus-Charakter (präfrontale Regulation, Attunement, Bewegungssynchronie, PONS-Dekodierung, Hoffman-Empathiestufen) konnten bestehenden MECs (MEC-0010, MEC-0020) als vertiefende Fundierung zugeordnet werden — siehe Abschnitt 4.

---

## 4. Erweiterte Objekte

**Anzahl:** 5 (3 MEC, 1 P, 1 A)

| Objekt | Art der Erweiterung |
|---|---|
| MEC-0010 (Amygdala-Regulation durch Labeling) | Neue wissenschaftliche Grundlage: LeDoux' Zwei-Pfad-Modell (low road/high road) als neurobiologischer Rahmen, erstmals mit vollständiger Primärquelle (LeDoux 1996, 2000). Neue Grenzen-Dimension: Kagan-Temperamentsforschung (individuelle Amygdala-Basiserregbarkeit, partielle Neuroplastizität). Kein E-Level-Wechsel. |
| MEC-0011 (Neural Coupling durch Isopraxismus) | Neuer Abgrenzungsvermerk zu MEC-0022, um Verwechslung von bewusstem Mirroring und unwillkürlicher Mimikry zu vermeiden. Keine inhaltliche Erweiterung der Kausalkette selbst. Kein E-Level-Wechsel. |
| MEC-0020 (Perspektivübernahme-Asymmetrie unter Macht) | Neue entwicklungspsychologische Fundierung: Hoffmans 4-Stufen-Modell der Empathieentwicklung bestätigt die Unterscheidung zwischen motorischer Mimikry (MEC-0022) und kognitiver Perspektivübernahme (MEC-0020). Vollständige PONS-Test-Primärquelle mit Reliabilitätsdaten ergänzt. Kein E-Level-Wechsel. |
| P-0016 (Tactical Empathy) | Neuer Mechanismus-Verweis (MEC-0022) ergänzt. Konvergenzbestätigung aus zwei unabhängigen Forschungsfeldern (Gottman Ehe-Forschung, Levinson Arbeitsplatz-Feedback-Forschung) für die Kernthese "Empathie vor Inhalt". Neue Grenzen-Anmerkung zur methodischen Kritik an Gottmans 94%-Prädiktionsgenauigkeit. Kein E-Level-Wechsel. |
| A-0013 (Emotionen sind das primäre Verhandlungsmedium) | Erweiterung des Anwendungskontexts von "primär Hochstress-/Krisenverhandlung" auf "generelle Entscheidungsfindung" durch Damasios somatische Marker-Hypothese (Fallstudie "Elliot") und LeDoux' strukturelle Zwei-Pfad-Argumentation. Kein E-Level-Wechsel. |

---

## 5. Canonicalization Rate

**Berechnungsbasis (MEC-spezifisch, wie in SPR-0001 definiert):**

- Neue MECs: 1 (MEC-0022)
- Erweiterte MECs: 3 (MEC-0010, MEC-0011, MEC-0020)
- **Canonicalization Rate B-0011 = 3 / (1 + 3) × 100 = 75%**

**Einordnung im Vergleich zu Sprint 1 (SPR-0001):** Die Sprint-1-Zielrate war ≥60% (siehe canonicalization_report.md, Abschnitt 3, Regel 5). B-0011 übertrifft diese Zielmarke deutlich (75%) und liegt signifikant über dem Sprint-1-Höchstwert (B-0005: 67%). Dies ist ein direkter, quantitativer Beleg für die erfolgreiche Umsetzung der Editor-Priorität "wissenschaftliche Vertiefung statt Wachstum" in diesem Sprint.

**Codex-weite Rate (alle Objekttypen, informativ, nicht die primäre Kennzahl):** 5 Extensions / (20 Neue + 5 Extensions) × 100 = 20%. Diese niedrigere Zahl ist methodisch erwartbar, da Statements (16 von 20 Neuanlagen) per Definition immer neu angelegt werden.

---

## 6. Neue Scientific Debt Einträge

Vollständig eingetragen in `00_project/SCIENTIFIC_DEBT.md`, neue Sektion "B-0011 — Emotional Intelligence (SRC-0011)" (8 Einträge). Zusammenfassung:

| Objekt-ID | Kategorie | Priorität |
|---|---|---|
| ST-0213 (Marshmallow-Test) | Replikationsrisiko | Hoch |
| ST-0214 (Ekman-Universalität) | Widersprüchliche Evidenz | Mittel |
| ST-0217 (Seligman-Optimismus) | Publication Bias | Hoch |
| MEC-0022, A-0049 (Emotional Contagion) | Transferlücke | Mittel |
| P-0016-Erweiterung (Gottman-Prädiktion) | Externe Validierung ausstehend | Mittel |
| MEC-0010-Erweiterung, P-0016 (Kagan-Moderation) | Offene Forschungsfrage | Niedrig |
| ST-0205, A-0013-Erweiterung (Damasio) | Offene Forschungsfrage | Niedrig |
| SRC-0011 (SRC-0010-Dateianomalie) | Unbelegte Annahme (Repository-Hinweis) | Mittel |

---

## 7. Neue Literaturquellen

Vollständig eingetragen in `05_research/LITERATURE_INDEX.md`, Abschnitt B (Sozialpsychologie, Persuasion & Interpersonal Influence). Zusammenfassung:

| APA-Zitation | Verifikationsstatus | Unterstützt |
|---|---|---|
| LeDoux, J. (1996). *The Emotional Brain*. Simon & Schuster. | Verifiziert (2026-07-02) | MEC-0010, A-0013 |
| LeDoux, J. (2000). Emotion Circuits in the Brain. *Annual Review of Neuroscience*, 23, 155–184. | Verifiziert (2026-07-02) | MEC-0010 |
| Hatfield, E., Cacioppo, J.T. & Rapson, R.L. (1993). Emotional Contagion. *Current Directions in Psychological Science*, 2(3), 96–100. | Verifiziert (2026-07-02) | MEC-0022 |
| Hatfield, E., Cacioppo, J.T. & Rapson, R.L. (1994). *Emotional Contagion*. Cambridge University Press. | Verifiziert (2026-07-02) | MEC-0022, A-0049 |
| Rosenthal, R., Hall, J.A., DiMatteo, M.R., Rogers, P.L. & Archer, D. (1979). *Sensitivity to Nonverbal Communication: The PONS Test*. Johns Hopkins University Press. | Verifiziert (2026-07-02) inkl. Reliabilitätsdaten | MEC-0020 |

**Nicht bibliografisch vollständig verifizierbar (offene Frage, nicht erfunden):** Dimberg (Uppsala, Facial-EMG-Forschung zu Emotional Contagion) — im Buch erwähnt, aber vollständige Zitation (Jahr, Journal) über WebSearch nicht mit ausreichender Sicherheit auffindbar. In ST-0208 als offene Frage markiert statt spekulativ zitiert.

---

## 8. Publikationsbias-Risiken

Identifiziert und dokumentiert (siehe auch SCIENTIFIC_DEBT.md):

1. **Seligman/Met-Life-Studie (ST-0217):** Höchstes Risiko — Autor war zugleich Mitentwickler des evaluierten Trainingsprogramms. Klassisches Muster kommerziell motivierter Forschung. Deshalb bewusst nicht zu einem Prinzip erhoben.
2. **Marshmallow-Test (ST-0213):** Kein direktes kommerzielles Interesse, aber Publikations-/Rezeptionsbias: der ursprüngliche dramatische Befund wurde weit stärker rezipiert als die abschwächende Replikation (Watts et al. 2018) — ein Muster, das in der Verhaltenswissenschaft häufig auftritt (auffällige Erstbefunde erhalten mehr mediale Aufmerksamkeit als nüchterne Replikationen).
3. **Gottman 94%-Zahl:** Kein klassischer Publikationsbias, aber ein methodischer Präsentationsbias (In-Sample-Retrodiktion als "Vorhersage" vermarktet) — von Statistikern (Gelman) öffentlich kritisiert.

---

## 9. Neue Tier-1-Kandidaten (nur Dokumentation, keine Eintragung)

Gemäß Auftrag: Diese Quellen werden hier nur als mögliche Kandidaten für `00_project/ACADEMIC_RECOVERY_PLAN.md` dokumentiert — eine tatsächliche Eintragung dort ist außerhalb des Scopes dieser Buchanalyse.

- **Hatfield, Cacioppo & Rapson (1993, 1994) — Emotional Contagion:** Starker Kandidat für Tier-1. Breit rezipierte, mehrfach replizierte Theorie mit klarer, prüfbarer Kausalstruktur; würde MEC-0022 von E3–E4 auf potenziell E4–E5 heben, falls eine aktuelle Meta-Analyse zur Effektstärke gefunden werden kann (in diesem Sprint nicht durchgeführt).
- **Rosenthal et al. (1979) PONS-Test:** Mittlerer Kandidat — etabliertes, standardisiertes Messinstrument mit guter Reliabilität, aber die Frage der Validität für Verhandlungs-/Vertriebskontexte (nicht nur allgemeine nonverbale Sensitivität) bliebe zu klären.
- **LeDoux (1996, 2000):** Mittlerer Kandidat — sehr einflussreiche neurowissenschaftliche Grundlagenarbeit, aber bereits primär als Grundlagenrahmen (nicht als direkt anwendungsbezogene Interventionsstudie) genutzt; Tier-1-Einstufung müsste klären, ob Grundlagenforschung ohne direkten Interventionsbezug die Tier-1-Kriterien erfüllt.

---

## Status

Abgeschlossen — 2026-07-02
