# MOD-0006 — JOLT-Modell: Vier-Elemente-System zur Überwindung von Kundenunentschlossenheit

## Model ID

MOD-0006

## Name

JOLT-Modell

## Beschreibung

Das JOLT-Modell ist ein vier-elementiges System zur Diagnose und Überwindung von Kundenunentschlossenheit in der Post-Status-quo-Phase des Kaufprozesses. Es ergänzt bestehende Verkaufsmethodologien (SPIN, Challenger, Gap Selling) um eine bisher unzureichend adressierte Phase: die Zeit nach der Überwindung des Status-quo-Bias, wenn der Käufer intellektuell kaufbereit ist, aber emotional blockiert.

## Modell-Typ

Prozessmodell / Interventions-Framework

## Kernstruktur

```
VORAUSSETZUNG: Status quo ist überwunden (durch SPIN, Challenger oder Gap Selling)
↓
PHASE: Kundenunentschlossenheit (56% aller No-Decision-Verluste)
↓
JOLT-INTERVENTION:

J — Judge the Indecision
    ├── Quelle: Bewertungsproblem? → O
    ├── Quelle: Informationsbedürfnis? → L  
    └── Quelle: Ergebnisunsicherheit? → T

O — Offer Your Recommendation
    └── Spezifische Empfehlung statt Optionsliste
        Mechanismus: MEC-0015 Choice Overload auflösen

L — Limit the Exploration
    └── Informationsfluss kontrollieren / Experten-Positionierung
        Mechanismus: MEC-0008 Autorität

T — Take Risk Off the Table
    └── Risiko konkret reduzieren / Believable Impact
        Mechanismus: MEC-0016 FOMU adressieren
```

## Forschungsbasis

ML-Analyse von Millionen virtueller Verkaufsgespräche via Tethr-Plattform (Dixon & McKenna, 2022). 8.300+ Verhaltensmerkmale analysiert. Kernbefund: 44% der No-Decision-Verluste aus Status-quo-Präferenz; 56% aus Kundenunentschlossenheit.

## Verhältnis zu bestehenden Modellen

| Modell | Phase | Problem | JOLT-Verhältnis |
|---|---|---|---|
| MOD-0001 SPIN | Discovery | Bedarf aufbauen | Vorgelagert zu JOLT |
| MOD-0004 Challenger TTC | Teach → Tailor → Take Control | Status quo überwinden | Vorgelagert zu JOLT |
| MOD-0005 Gap Selling | Current State → Future State | Gap quantifizieren, Status quo überwinden | Vorgelagert zu JOLT |
| **MOD-0006 JOLT** | **Post-Status-quo** | **Unentschlossenheit überwinden** | **Nachgelagert zu allen obigen** |

JOLT ist kein Ersatz für die anderen Modelle — es schließt eine Lücke, die alle anderen offen lassen.

## W-001-Implikation

W-001 (Teach First vs. Diagnose First) adressiert die Status-quo-Phase. JOLT adressiert die Post-Status-quo-Phase. Die W-001-Debatte und JOLT sind orthogonal — JOLT löst W-001 nicht, schärft aber die Frage: Welches Modell für Status-quo-Phase kombiniert sich am besten mit JOLT?

**Indirekte Evidenz für Challenger-Affinität:**
- JOLT-O (Empfehlung geben) und JOLT-L (Informationsfluss kontrollieren) entsprechen dem "Take Control"-Element von Challenger (MOD-0004)
- JOLT-J (Diagnose) entspricht SPIN's Discovery-Ansatz
- Die Kombination SPIN-Discovery + JOLT-JOLT ist konzeptuell konsistent; ebenso Challenger-Teaching + JOLT

## Evidenzlevel

E2 (Proprietäre ML-Datenbasis, nicht peer-reviewed; gut replizierbare Einzelmechanismen mit E4-Grundlage)

## Grenzen

- JOLT setzt voraus, dass die Status-quo-Phase erfolgreich abgeschlossen wurde; bei gemischter Status-quo/Indecision-Situation muss sequenziell vorgegangen werden
- JOLT-Elemente werden situationsabhängig, nicht sequenziell eingesetzt — J ist immer zuerst, O/L/T nach Diagnoseergebnis
- Keine Daten zur JOLT-Effektivität in Nicht-COVID-Umgebungen oder Nicht-US-Märkten
- Proprietäre Datenbasis limitiert externe Validierungsmöglichkeiten

## Verknüpfte Objekte

- Prinzipien: P-0027, P-0028, P-0029, P-0030
- Techniken: T-0026, T-0027, T-0028, T-0029, T-0030
- Mechanismen: MEC-0015 (erweitert), MEC-0016 (neu)
- Statements: ST-0150–ST-0164

## ⚠ Hinweis: Publication Bias (Kommerzielle Quelle)

Dieses Objekt beruht (mit) auf der proprietaeren Tethr-ML-Klassifizierung (44%/56%-Split), durchgefuehrt von einem kommerziellen Analytics-Anbieter. Die Klassifizierungsmethodik ist nicht offengelegt; keine unabhaengige Replikation bekannt. Siehe `SCIENTIFIC_DEBT.md`, SD-SYS-004 (Publication Bias kommerzieller Studien) fuer die vollstaendige Einordnung. **[Ergaenzt 2026-07-03, External Audit Resolution Sprint]**

## AR-013-Ergänzung: Akademische Grundlage für das allgemeine Post-Status-quo-Phänomen, nicht für das JOLT-Modell selbst

**[Ergänzt 2026-07-13, Academic Recovery Sprint, AR-013]**

Tversky & Shafir (1992, "Choice under Conflict: The Dynamics of Deferred Decision", *Psychological Science* 3(6), 358–361; SRC-0016, ST-0310/ST-0311, volltextgeprüft) demonstrieren peer-reviewt und unabhängig von Tethr/JOLT, dass Entscheider auch bei einem objektiv mindestens ebenso guten Angebot aufschieben oder zur Default-Option zurückkehren können, wenn zwischen den verfügbaren Optionen ein schwer auflösbarer Trade-off besteht. Dies liefert eine unabhängige akademische Stütze für die allgemeine Plausibilität einer "Post-Status-quo-Unentschlossenheit" als eigenständiges Phänomen (die Grundprämisse, auf der MOD-0006 aufbaut).

**Was dadurch NICHT gestützt wird:** Die Studie testet keines der vier JOLT-Elemente (J/O/L/T), keine B2B-Kaufsituation und keinen der spezifischen kausalen Pfade (Diagnoseproblem, Informationsbedürfnis, Ergebnisunsicherheit), die MOD-0006 postuliert. Der zugrunde liegende Mechanismus in Tversky & Shafir (Attribut-Trade-off-Konflikt zwischen bekannten Optionen) deckt sich zudem nicht mit MEC-0016 (FOMU/antizipierte Reue über eine eigene Fehlentscheidung), auf dem das T-Element von JOLT primär aufbaut — siehe MEC-0016, Abschnitt "AR-013-Prüfung", für die vollständige Abgrenzung. Kein E-Level-Wechsel für MOD-0006 (bleibt E2) — die proprietäre Datengrundlage und die fehlende externe Validierung der spezifischen JOLT-Struktur bestehen unverändert fort.

## Status

Entwurf — erstellt 2026-07-01 (SRC-0006); AR-013-Ergänzung 2026-07-13 (Tversky & Shafir 1992, keine Änderung der Evidenzklasse)
