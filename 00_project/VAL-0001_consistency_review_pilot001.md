# VAL-0001 — Interner Konsistenz-Review: Pilot 001 SPIN Selling

## Validation ID

VAL-0001

## Geprüftes Objekt

Alle Wissensobjekte aus Pilot 001 — SPIN Selling  
(ST-0001 bis ST-0023, A-0001 bis A-0004, P-0001 bis P-0007, MEC-0001 bis MEC-0004, T-0001 bis T-0004, MOD-0001)

## Fragestellung

Sind alle Wissensobjekte intern konsistent, vollständig cross-referenziert und evidenzmäßig korrekt eingestuft?

## Prüfquelle(n)

Direkter Datei-Abgleich aller Wissensobjekte (2026-06-27)

---

## Prüfbereiche und Ergebnisse

### 1. Vollständigkeit der Objektmenge

| Objekttyp | Soll | Ist | Status |
|---|---|---|---|
| Statements (ST) | 23 | 23 | ✓ OK |
| Annahmen (A) | 4 | 4 | ✓ OK |
| Prinzipien (P) | 7 | 7 | ✓ OK |
| Mechanismen (MEC) | 4 | 4 | ✓ OK |
| Techniken (T) | 4 | 4 | ✓ OK |
| Modelle (MOD) | 1 | 1 | ✓ OK |

### 2. ID-Referenz-Integrität in MOD-0001

**Geprüft:** Alle in MOD-0001 referenzierten IDs gegen tatsächlich existierende Dateien.

**Ergebnis:** ✓ Alle 19 referenzierten IDs (A-0001 bis A-0004, P-0001 bis P-0007, MEC-0001 bis MEC-0004, T-0001 bis T-0004) sind als Dateien vorhanden.

### 3. Mechanismus-Referenz-Integrität in Prinzipien

**Befund 1 (behoben):** P-0001 und P-0002 hatten Mechanismusnamen als Freitext, keine MEC-IDs. Da MEC-Objekte beim Anlegen von P-0001 und P-0002 noch nicht existierten, war dies initial unvermeidbar.

**Maßnahme:** P-0001 und P-0002 wurden aktualisiert — Mechanismen jetzt mit MEC-IDs referenziert.

**Befund 2 (offen, kein Blocker):** P-0002 nennt "Kontrasteffekt" als dritten Mechanismus. Kein eigenes MEC-Objekt vorhanden. Der Kontrasteffekt (Anchoring/Contrast Effect) ist ein realer psychologischer Mechanismus, aber noch nicht als MEC-Objekt formalisiert. In P-0002 als Kandidat für MEC-0005 markiert. Keine Sofortmaßnahme erforderlich.

### 4. Evidenzklassen-Konsistenz

| Prinzip | Evidenz | Einschätzung |
|---|---|---|
| P-0001 | E3 | ✓ Korrekt — gute Stützung durch SPIN-Forschung + Psychologie |
| P-0002 | E4-Kandidat | ⚠ Grenzwertig — allg. Verlustaversionsforschung ist E4, aber spezifische Anwendung auf Major Sales eher E3. Formulierung "Kandidat" signalisiert Vorbehalt. Akzeptabel. |
| P-0003 | E2 | ✓ Korrekt — primär eine Ableitung, noch wenig direkte Verkaufsforschung |
| P-0004 | E3 | ✓ Korrekt |
| P-0005 | E3 | ✓ Korrekt |
| P-0006 | E2 | ✓ Korrekt — Kausalaussage stärker als Datenbasis |
| P-0007 | E2 | ✓ Korrekt |

**Anmerkung zu P-0002:** Bei der nächsten Revision sollte geprüft werden, ob "E4-Kandidat" auf "E3 (Mechanismus E4, Anwendung E3)" präzisiert wird.

### 5. Technik-zu-Prinzip-zu-Mechanismus-Ketten

| Technik | Prinzip | Mechanismus | Vollständig? |
|---|---|---|---|
| T-0001 | P-0004 | (kein direkter) | ✓ Korrekt — T-0001 erzeugt primär Wissen, keinen Mechanism beim Käufer |
| T-0002 | P-0001, P-0004 | MEC-0001 | ✓ OK |
| T-0003 | P-0002, P-0004, P-0006 | MEC-0001, MEC-0002 | ✓ OK |
| T-0004 | P-0001, P-0004, P-0005 | MEC-0001, MEC-0004 | ✓ OK |

### 6. Falsch-positive Befunde (ausgeräumt)

T-0004 enthielt im Text "(ST-0015, ST-0016)" als Referenz auf Statement-Objekte. Die automatische ID-Extraktion hat diese fälschlicherweise als "T-0015/T-0016" geparst. Inhaltlich korrekt — es handelt sich um ST-Referenzen, nicht T-Referenzen. Kein Fehler.

### 7. Kapitelzuordnungs-Unsicherheiten

Zwei Statement-Objekte haben unsichere Kapitelzuordnungen:
- ST-0004 (Vier Gesprächsergebnisse): Könnte Kapitel 1 oder 2 sein. Markiert.
- ST-0021 (Vier Gesprächsphasen): Kapitelzuordnung tentativ. Markiert.

**Empfehlung:** Bei Primärtext-Verifikation als erstes klären.

### 8. Statement-Zählfehler (behoben)

analysis.md hatte "19 gesamt" für Statements angegeben. Tatsächliche Anzahl: 23. Korrigiert.

### 9. Sprachpolitik-Konformität

Stichprobe: Dateinamen auf Englisch ✓, Inhalte auf Deutsch ✓. Keine Abweichungen festgestellt.

### 10. Ethische Risiko-Markierungen

Alle Objekte mit mittlerem oder hohem ethischen Risiko wurden markiert:
- ST-0013 — Implication Questions: mittel bis hoch ✓
- P-0002 — mittel bis hoch ✓
- P-0004 — mittel ✓
- P-0006 — niedrig ✓
- MEC-0002 — mittel bis hoch bei Übertreibung ✓

---

## Einschätzung

Die Wissensbasis ist intern konsistent. Die zwei behobenen Befunde (MEC-ID-Referenzen in P-0001/P-0002, Zählfehler) waren redaktioneller Natur. Der offene Befund (Kontrasteffekt ohne MEC-Objekt) ist kein Blocker, sondern ein Entwicklungskandidat.

## Änderungsempfehlung

1. **Sofort (durchgeführt):** P-0001 und P-0002 MEC-Referenzen ergänzt. Zählfehler korrigiert.
2. **Nächste Revision:** P-0002 Evidenzklasse präzisieren ("E4-Kandidat" → "E3 (Mechanism: E4, Anwendung: E3)").
3. **Folgearbeit:** MEC-0005 (Kontrasteffekt) anlegen, wenn weiteres Quellmaterial dies stützt.
4. **Externe Validierung:** Primärtext-Verifikation aller ST-Objekte, Gemini-Validierung der Mechanismen, Perplexity-Recherche zu Replikationsstudien.

## Status

Abgeschlossen — 2026-06-27
