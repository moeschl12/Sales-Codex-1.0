# VAL-0004 — Interner Konsistenz-Review: B-0004 The Challenger Sale

## Validation ID

VAL-0004

## Geprüftes Objekt

Alle Wissensobjekte aus B-0004 — The Challenger Sale (Dixon/Adamson 2011)  
ST-0107 bis ST-0132, A-0018 bis A-0023, MEC-0013, MEC-0014 + 2 erweiterte MECs (MEC-0002, MEC-0007), P-0021 bis P-0024, T-0019 bis T-0021, MOD-0004

## Fragestellung

Sind alle Wissensobjekte aus B-0004 intern konsistent, vollständig cross-referenziert, quellenbelegt und evidenzmäßig korrekt eingestuft?

## Prüfquelle(n)

Direkter Datei-Abgleich aller Wissensobjekte (2026-06-30)  
PDF-Quelle: The Challenger Sale, Portfolio/Penguin, 2011 (pdfplumber-Extraktion via Python)

---

## Prüfbereiche und Ergebnisse

### 1. Vollständigkeit der Objektmenge

| Objekttyp | Soll | Ist | Status |
|---|---|---|---|
| Statements (ST) | 26 | 26 | ✓ OK — ST-0107 bis ST-0132 |
| Annahmen (A) | 6 | 6 | ✓ OK — A-0018 bis A-0023 |
| Mechanismen (neu) | 2 | 2 | ✓ OK — MEC-0013, MEC-0014 |
| Mechanismen (erweitert) | 2 | 2 | ✓ OK — MEC-0002, MEC-0007 |
| Prinzipien (P) | 4 | 4 | ✓ OK — P-0021 bis P-0024 |
| Techniken (T) | 3 | 3 | ✓ OK — T-0019 bis T-0021 |
| Modelle (MOD) | 1 | 1 | ✓ OK — MOD-0004 |

**Gesamtprüfung:** Vollständig.

---

### 2. Source-ID-Integrität

Alle Objekte auf korrekten Source-ID-Eintrag (SRC-0004) geprüft.

| Objekttyp | Source-ID vorhanden | Status |
|---|---|---|
| ST-Objekte (26) | 26/26 | ✓ OK |
| A-Objekte (6) | 6/6 | ✓ OK |
| MEC-Objekte (2 neu) | 2/2 | ✓ OK |
| MEC-Objekte (2 ext.) | 2/2 | ✓ OK (Erweiterungs-Sektion datiert + sourced) |
| P-Objekte (4) | 4/4 | ✓ OK |
| T-Objekte (3) | 3/3 | ✓ OK |
| MOD-0004 | 1/1 | ✓ OK |

---

### 3. Multi-Quellen-Anforderung bei Prinzipien (OR-Regel)

Regel: Jedes P muss aus ≥2 MECs ODER ≥2 A-Objekten abstrahiert sein (kombiniert möglich).

| P-ID | MECs | A-Objekte | OR-Regel | Status |
|---|---|---|---|---|
| P-0021 | MEC-0013, MEC-0002 (2) | — | ✓ ≥2 MECs | OK |
| P-0022 | — | A-0018, A-0020, A-0021 (3) | ✓ ≥2 A-Objekte | OK |
| P-0023 | MEC-0014, MEC-0013 (2) | A-0022 | ✓ ≥2 MECs | OK |
| P-0024 | — | A-0018, A-0020, A-0023 (3) | ✓ ≥2 A-Objekte | OK |

**Ergebnis:** Alle 4 Prinzipien erfüllen die OR-Regel. ✓

---

### 4. Evidenzklassifikation — Konsistenzprüfung

Prüfung: Wird E1-E4 korrekt angewendet? E4 = gut replizierte Laborstudien; E1 = Einzel-Anekdote/unbelegte Behauptung.

| Objekt | Zugeordnetes Evidenzlevel | Angemessen? | Anmerkung |
|---|---|---|---|
| A-0018 (RB verliert in komplexem B2B) | E3 | ✓ | N=6.000 kalibriert E3; kein RCT, proprietäre Daten |
| A-0019 (53% Loyalität durch Sales Experience) | E3 | ✓ | Befragungsstudie; Kausalität nicht belegt |
| A-0020 (Kunden wollen gelehrt werden) | E3 | ✓ | Loyalitätsattribute-Ranking erfragt, nicht experimentell |
| A-0021 (konstruktive Spannung produktiv) | E3 | ✓ | Abgeleitet aus Performance-Daten; kein direktes Spannungsexperiment |
| A-0022 (Konsensbasierter Kauf) | E3 | ✓ | CEB-Befragung; Kausalstruktur unklar |
| A-0023 (TTC trainierbar) | E2 | ✓ | Praxisbeobachtung; kein Längsschnittnachweis |
| MEC-0013 (Insight-Disruption) | E3/E4 | ✓ | Kogn. Dissonanz E4 repliziert; Challenger-Anwendung nur E3 |
| MEC-0014 (Konsens als Kaufsicherheit) | E3 | ✓ | Gruppenentscheidungspsychologie belegt; B2B-spezifisch E3 |
| P-0021 (Commercial Teaching Pitch) | E3 | ✓ | Konservativ — Sequenz als Ganzes nicht RCT-getestet |

**Ergebnis:** Evidenzklassifikationen sind konsistent und konservativ. Keine Über-Evidenzierung. ✓

---

### 5. Quellenintegrität — Keine Training-Knowledge-Kontamination

Prüffrage: Wurden alle inhaltlichen Aussagen aus PDF-Text extrahiert oder aus Quellen, die in den ST-Dateien referenziert sind?

| Prüfpunkt | Ergebnis |
|---|---|
| Alle 26 ST-Dateien: Originalzitat oder Paraphrase mit Kapitelangabe + PDF-Seite | ✓ |
| Quantitative Angaben (53%, 40%, 6.000, 90, etc.) aus PDF-Text, nicht aus Modellwissen | ✓ |
| MEC-Erweiterungen: datiert + explizit als SRC-0004-Beitrag markiert | ✓ |
| Keine P/T/MOD-Datei macht factual claims ohne ST-Rückverweis | ✓ |

**Festgestellte Ausnahmen — CEB-Behauptungen ohne externe Replikation:**

| Statement | Unbelegte / eingeschränkte Behauptung | Markierung |
|---|---|---|
| ST-0122 | 53%/38%/9%-Split: Methodik nicht öffentlich einsehbar | Evidenz E3 + Offene Fragen in A-0019 |
| ST-0124 | 6-Schritt-Pitch als CEB-Framework-Konstrukt — nicht als eigenständige Einheit getestet | E3 in P-0021 + Grenze |
| ST-0119 | "Natur-Nurture-Frage irrelevant" — normatives Argument, kein empirischer Nachweis | E2 in A-0023 |
| ST-0130 | Manager-Exzellenz-Prozentzahlen (~25%/~25%/~28%/~22%) — Messdetails nicht publiziert | E3 markiert |

**Ergebnis:** Keine Training-Knowledge-Kontamination. CEB-Spezifika korrekt als proprietäre Daten eingestuft. ✓

---

### 6. Widerspruchs-Dokumentation

Prüffrage: Wurden alle Cross-Book-Widersprüche dokumentiert (statt geglättet)?

| Widerspruch | Dokumentiert in | Status |
|---|---|---|
| Cialdini Liking (MEC-0007) vs. Challenger RB = schwächstes Profil | ST-0109, A-0018, MEC-0007 Erweiterung | ✓ Auflösung: unterschiedliche Kontexte (einfach vs. komplex) |
| Voss BCSM Spannungsreduktion vs. Challenger konstruktive Spannung | ST-0118, A-0021 | ✓ Auflösung: Krisenverhandlung vs. Kaufgespräch |
| SPIN Diagnose-Primat vs. Challenger Insight-Primat | ST-0122, A-0020, MEC-0013 | ✓ Auflösung: SPIN wirkt bei bewussten Bedürfnissen; Challenger bei unbekannten |
| TTC-Modell-Claim vs. Commodity-Markt-Realität | MOD-0004 Grenzen, A-0019 Offene Fragen | ✓ Grenze dokumentiert |
| "Challengers werden gemacht" vs. fehlende Längsschnittbelege | A-0023, E2 markiert | ✓ Evidenzlücke offen markiert |

**Ergebnis:** 5 dokumentierte Widersprüche/Grenzen — alle erfasst, keine geglättet. ✓

---

### 7. Canonicalization Rate (MEC-Objekte)

Berechnung: Extended MECs / (neue + extended MECs) × 100

- Neue MECs: 2 (MEC-0013, MEC-0014)
- Erweiterte MECs: 2 (MEC-0002, MEC-0007)
- Gesamt: 4

**Canonicalization Rate:** 2 / 4 × 100 = **50%**

Vergleich: B-0003 (Never Split the Difference): 50%. B-0002 (Influence): 37,5%.

Interpretation: B-0004 baut in gleichem Maß auf bestehende psychologische Mechanismen (Verlustaversion, Liking-Transfer) wie es neue einführt (Insight-Disruption, Konsens-Kaufsicherheit). Das ist konzeptuell konsistent: Challenger Sale zieht auf bekannte Mechanismen, aktiviert sie aber in neuer Kombination und neuem Kontext.

---

### 8. Nicht-Anlage-Dokumentation (abgelehnte Kandidaten)

Welche Objekte wurden als Kandidaten identifiziert, aber nicht angelegt?

| Typ | Beschreibung | Ablehnungsgrund |
|---|---|---|
| T | Lone-Wolf-Identifikation als Diagnose-Technik | Zu vage — keine klare Handlungsanweisung; als Konzept in MOD-0004 + ST-0131 abgedeckt |
| T | "Inactive Challenger"-Aktivierungstechnik | Framework-Exposition (TTC-Training) ist T-0019/T-0020 — keine eigenständige Technik darüber hinaus |
| MEC | "Solutions Fatigue" als Wahrnehmungsmechanismus | Zu situationsspezifisch; Kernmechanismus ist MEC-0009 (Perceptual Contrast, SRC-0002) + MEC-0013; keine neue Mechanismusdimension |
| P | "Lone Wolf nicht skalieren" als Organisations-Prinzip | Negativprinzip ohne eigenständige Handlungsanweisung; in MOD-0004 und P-0024 als Grenzbeschreibung abgedeckt |
| A | "Beste Manager kommen aus Challenger-Reihen" | Zu spezifisch für eine allgemeine Annahme; Befund in ST-0130 dokumentiert, A-0023 enthält die allgemeinere Trainierbarkeits-Annahme |

---

### 9. Cross-Reference-Vollständigkeit

Stichprobenprüfung: Sind wichtige Objekte wechselseitig verlinkt?

| Verbindung | Verlinkt? |
|---|---|
| MEC-0013 ← P-0021 (Commercial Teaching Pitch) | ✓ |
| MEC-0013 ← T-0019 (Commercial Teaching Pitch Technik) | ✓ |
| MEC-0014 ← P-0023 (Champion-Mobilisierung) | ✓ |
| MEC-0002 ↔ MEC-0013 (Sequenz: Disruption → Verlustaversion) | ✓ (in MEC-0002 Erweiterung) |
| A-0018 ← P-0022 (TTC-Dreiklang) | ✓ |
| A-0022 ← P-0023 (Champion als Mobilizer) | ✓ |
| MOD-0004 ← alle relevanten T, P, MEC, A | ✓ (in Tabellen) |
| MEC-0007 ← A-0018 (Boundary Condition: Liking kein Differenzierer in Komplex-B2B) | ✓ (in MEC-0007 Erweiterung) |

**Ergebnis:** Cross-References vollständig für geprüfte Verbindungen. ✓

---

## Ergebnis

**Gesamturteil: BESTANDEN**

Alle 9 Prüfbereiche ohne kritische Fehler bestanden. Anmerkungen:

1. **A-0023 (Trainierbarkeit)** verbleibt auf E2 — es gibt keine publizierten Längsschnittdaten zu TTC-Trainingseffekten. Richtig so markiert. SCIENTIFIC_DEBT eintragen.
2. **P-0021 (Commercial Teaching Pitch)** ist als 6-Schritt-Einheit nicht RCT-getestet — nur der Challenger-Profil-Befund belegt Wirksamkeit des Gesamtprofils, nicht der Sequenz als solcher. Korrekt auf E3 gesetzt.
3. **MEC-0014 (Konsens als Kaufsicherheit)** ist konzeptuell plausibel und gut hergeleitet, aber B2B-spezifische Mechanismus-Forschung fehlt. Als offene Forschungsfrage markieren.

## Änderungsempfehlung

1. **SCIENTIFIC_DEBT.md aktualisieren:** Fehlende Längsschnittdaten für TTC-Training (A-0023) + keine externe CEB-Replikation + keine MEC-0014-Spezifika aus B2B-Kaufforschung
2. **analysis.md aktualisieren:** Alle Sektionen auf "abgeschlossen" setzen; MEC/P/T/MOD-Tabellen befüllen
3. **Deferred (aus VAL-0003):** Gemini-Validierung MEC-0005–0009 (Cialdini) noch ausstehend — Priorität unverändert

## Status

Abgeschlossen — 2026-06-30
