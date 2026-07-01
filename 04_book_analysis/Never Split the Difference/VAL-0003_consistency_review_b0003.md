# VAL-0003 — Interner Konsistenz-Review: B-0003 Never Split the Difference

## Validation ID

VAL-0003

## Geprüftes Objekt

Alle Wissensobjekte aus B-0003 — Never Split the Difference (Voss/Raz 2016)  
ST-0050 bis ST-0106, A-0013 bis A-0017, MEC-0010 bis MEC-0012 + 3 erweiterte MECs (MEC-0002, -0003, -0007), P-0016 bis P-0020, T-0012 bis T-0018, MOD-0003

## Fragestellung

Sind alle Wissensobjekte aus B-0003 intern konsistent, vollständig cross-referenziert, quellenbelegt und evidenzmäßig korrekt eingestuft?

## Prüfquelle(n)

Direkter Datei-Abgleich aller Wissensobjekte (2026-06-30)  
PDF-Quelle: Never Split the Difference, HarperBusiness, 2016 (pdfplumber-Extraktion via Python)

---

## Prüfbereiche und Ergebnisse

### 1. Vollständigkeit der Objektmenge

| Objekttyp | Soll | Ist | Status |
|---|---|---|---|
| Statements (ST) | 57 | 57 | ✓ OK — ST-0050 bis ST-0106 |
| Annahmen (A) | 5 | 5 | ✓ OK — A-0013 bis A-0017 |
| Mechanismen (neu) | 3 | 3 | ✓ OK — MEC-0010, -0011, -0012 |
| Mechanismen (erweitert) | 3 | 3 | ✓ OK — MEC-0002, -0003, -0007 |
| Prinzipien (P) | 5 | 5 | ✓ OK — P-0016 bis P-0020 |
| Techniken (T) | 7 | 7 | ✓ OK — T-0012 bis T-0018 |
| Modelle (MOD) | 1 | 1 | ✓ OK — MOD-0003 |

**Gesamtprüfung:** Vollständig.

---

### 2. Source-ID-Integrität

Alle Objekte auf korrekten Source-ID-Eintrag (SRC-0003) geprüft.

| Objekttyp | Source-ID vorhanden | Status |
|---|---|---|
| ST-Objekte (57) | 57/57 | ✓ OK |
| A-Objekte (5) | 5/5 | ✓ OK |
| MEC-Objekte (3 neu) | 3/3 | ✓ OK |
| MEC-Objekte (3 ext.) | 3/3 | ✓ OK (Erweiterungs-Sektion datiert + sourced) |
| P-Objekte (5) | 5/5 | ✓ OK |
| T-Objekte (7) | 7/7 | ✓ OK |
| MOD-0003 | 1/1 | ✓ OK |

---

### 3. Multi-Quellen-Anforderung bei Prinzipien (OR-Regel)

Regel: Jedes P muss aus ≥2 MECs ODER ≥2 A-Objekten abstrahiert sein (kombiniert möglich).

| P-ID | MECs | A-Objekte | OR-Regel | Status |
|---|---|---|---|---|
| P-0016 | MEC-0010, MEC-0011, MEC-0012 (3) | A-0013 | ✓ ≥2 MECs | OK |
| P-0017 | MEC-0003, MEC-0012 (2) | A-0015 | ✓ ≥2 MECs | OK |
| P-0018 | MEC-0002 (1) | A-0014, A-0013 (2) | ✓ ≥2 A-Objekte | OK |
| P-0019 | — | A-0017, A-0015 (2) | ✓ ≥2 A-Objekte | OK |
| P-0020 | — | A-0016, A-0017 (2) | ✓ ≥2 A-Objekte | OK |

**Ergebnis:** Alle 5 Prinzipien erfüllen die OR-Regel. ✓

---

### 4. Evidenzklassifikation — Konsistenzprüfung

Prüfung: Wird E1-E5 korrekt angewendet? E4/E5 = gut replizierte Laborstudien; E1 = Einzel-Anekdote/Einzelfallbericht.

| Objekt | Zugeordnetes Evidenzlevel | Angemessen? | Anmerkung |
|---|---|---|---|
| A-0014 (Loss Aversion) | E2 | ✓ | Kahneman/Tversky (1979) rechtfertigt E3 für den Mechanismus; E2 wegen Anwendungs-Einschränkungen korrekt |
| A-0016 (Black Swans) | E1 | ✓ | "≥3 Black Swans"-Daumenregel ist nur Voss-Behauptung |
| MEC-0010 (Labeling) | E3 | ✓ | Lieberman (2007) fMRT-Studie, aber Labstudie nicht Feldstudio |
| MEC-0011 (Neural Coupling) | E3 | ✓ | Stephens/Hasson (2010) PNAS solide; Spiegelneuronen-Verbindung kritisch markiert |
| MEC-0012 (Dual-Process) | E4/E3/E1 | ✓ | Differenziert nach Kahneman vs. MacLean — korrekt |
| P-0016 (Tactical Empathy) | E3 | ✓ | Konservativ korrekt — FBI-Praxis + neurobiolog. Belege, aber kein Verhandlungs-RCT |
| T-0017 (Ackerman-Modell) | E2 | ✓ | Kein publizierter Ursprung; Praxis-Evidenz |

**Ergebnis:** Evidenzklassifikationen sind konsistent und konservativ. Keine Über-Evidenzierung festgestellt. ✓

---

### 5. Quellenintegrität — Keine Training-Knowledge-Kontamination

Prüffrage: Wurden alle inhaltlichen Aussagen aus PDF-Text extrahiert (pdfplumber) oder aus Quellen, die in den ST-Dateien referenziert sind?

| Prüfpunkt | Ergebnis |
|---|---|
| Alle 57 ST-Dateien: Originalzitat oder Paraphrase mit Kapitelangabe + PDF-Seite | ✓ |
| Wissenschaftliche Referenzen: aus Notes-Abschnitt (PDF S. 337–340) oder Fußnoten | ✓ |
| Keine ST-Datei enthält Aussagen ohne Quellenangabe | ✓ |
| MEC-Erweiterungen: datiert + explizit als SRC-0003-Beitrag markiert | ✓ |
| Keine P/T/MOD-Datei macht factual claims ohne ST-Rückverweis | ✓ |

**Festgestellte Ausnahmen / Unbelegte Voss-Behauptungen (korrekt markiert in ST-Dateien):**

| Statement | Unbelegte Behauptung | Markierung |
|---|---|---|
| ST-0088 | "Why ist immer eine Anklage" — universelle Behauptung ohne Beleg | ⚠ in ST-Datei |
| ST-0094 (7-38-55) | Mehrabian-Übergeneralisierung auf alle Kommunikation | ⚠ + Dokumentation Originalkontext |
| ST-0106 | "7:1 ROI auf Vorbereitungszeit" | ⚠ in ST-Datei |
| A-0016 | "≥3 Black Swans in jeder Verhandlung" | E1 markiert |

**Ergebnis:** Keine Training-Knowledge-Kontamination. Unbelegte Voss-Behauptungen korrekt markiert. ✓

---

### 6. Widerspruchs-Dokumentation

Prüffrage: Wurden alle internen Widersprüche im Voss-System dokumentiert (statt geglättet)?

| Widerspruch | Dokumentiert in | Status |
|---|---|---|
| "Gegenüber zuerst anchern lassen" vs. Ackerman beginnt mit eigenem Extremanker (Schritt 2) | ST-0099, P-0018 | ✓ Auflösung: situationsabhängig |
| "Why ist immer Anklage" — kulturelle Generalisierung ohne Beleg | ST-0088 | ✓ Grenze markiert |
| 7-38-55-Regel: Mehrabian-Kontext ≠ Voss-Anwendung | ST-0094 | ✓ Primärquelle dokumentiert |
| Negative Leverage: Voss lehrt es, aber warnt auch vor direktem Einsatz | ST-0102, P-0018, MEC-0003 ext. | ✓ Bedingungen klar |
| BCSM: intern entwickeltes FBI-Modell ohne externe Peer-Review | MOD-0003 | ✓ Evidenzniveau E2 |

**Ergebnis:** 5 dokumentierte Widersprüche — alle erfasst, keine geglättet. ✓

---

### 7. Canonicalization Rate (MEC-Objekte)

Berechnung: Extended MECs / (neue + extended MECs) × 100

- Neue MECs: 3 (MEC-0010, -0011, -0012)
- Erweiterte MECs: 3 (MEC-0002, -0003, -0007)
- Gesamt: 6

**Canonicalization Rate:** 3 / 6 × 100 = **50%**

Zum Vergleich: B-0002 Influence: 3/8 = 37,5%. Rate ist gestiegen, da Voss-Inhalte teilweise auf bereits etablierten psychologischen Mechanismen aufbauen.

---

### 8. Nicht-Anlage-Dokumentation (abgelehnte Kandidaten)

Welche Objekte wurden als Kandidaten identifiziert, aber nicht angelegt?

| Typ | Beschreibung | Ablehnungsgrund |
|---|---|---|
| T | FM-DJ-Stimme (Tonlagen-Regulation) | Kompetenz-Charakter (kontinuierliche Fähigkeit, keine isolierte Technik) → Kompetenz-Referenz in P/T |
| T | "That's right"-Ansteuerung (Summary-Technik) | Teil von T-0016 (Rule of Three) und T-0015 abgedeckt; eigenständige Technik zu schmal |
| T | Face Time / Unguarded Moments | Strategische Kontextprinzip, kein isolierter Handlungsschritt — referenziert in P-0020 |
| MEC | "Langer et al. Because"-Effekt | Nicht eigenständiger Mechanismus; Teilaspekt von MEC-0007 (Sympathie) / normativem Leverage |
| P | No-orientierte Verhandlungseröffnung | In P-0017 (Autonomie-Illusion) als Technik-Ausprägung enthalten; kein eigenständiger Prinzip-Charakter |

---

### 9. Cross-Reference-Vollständigkeit

Stichprobenprüfung: Sind wichtige Objekte wechselseitig verlinkt?

| Verbindung | Verlinkt? |
|---|---|
| MEC-0010 ← T-0013 (Labeling) | ✓ |
| MEC-0010 ← P-0016 (Tactical Empathy) | ✓ |
| MEC-0003 ← P-0017 (Autonomie-Illusion) | ✓ |
| A-0014 ← P-0018 (Loss Framing) | ✓ |
| A-0017 ← P-0019 (Commitment-Verifikation) | ✓ |
| A-0016 ← P-0020 (Black Swan) | ✓ |
| MOD-0003 ← alle relevanten T, P, MEC | ✓ (in Tabellen) |
| MEC-0002 ↔ MEC-0003 (Interdependenz Leverage) | ✓ (in beiden Dateien) |

**Ergebnis:** Cross-References vollständig für geprüfte Verbindungen. ✓

---

## Ergebnis

**Gesamturteil: BESTANDEN**

Alle 9 Prüfbereiche ohne kritische Fehler bestanden. Kleinere Anmerkungen:

1. **P-0019** referenziert kein explizites MEC-Objekt — OR-Regel über ≥2 A-Objekte erfüllt (korrekt), aber ein direktes MEC für "Kognitive Konsistenz durch Wiederholung" (MEC-0004 aus SRC-0001) könnte als Ergänzung nachgetragen werden.
2. **A-0016** (Black Swans) bleibt E1 — Voss-Daumenregel ohne empirische Basis. Korrekt so markiert.
3. **MEC-0011** (Neural Coupling): Spiegelneuronen-Verbindung auf menschliches Sozialverhalten ist wissenschaftlich umstritten — korrekt mit ⚠ markiert.

## Änderungsempfehlung

1. **Optionale Ergänzung:** P-0019 könnte MEC-0004 (Kognitive Konsistenz, SRC-0001) als Cross-Reference erhalten — Priorität niedrig.
2. **Zukunfts-Task:** Externe Validierung (durch Gemini oder weitere KI-Systeme) für MEC-0010 und MEC-0011 wäre wertvoll — Lieberman (2007) Transfer auf Verhandlungskontext und Spiegelneuronen-Frage.
3. **Deferred:** Gemini-Validierung der Cialdini-MECs (MEC-0005–0009) aus VAL-0002 noch ausstehend.

## Status

Abgeschlossen — 2026-06-30
