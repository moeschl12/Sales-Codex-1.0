# VAL-0002 — Interner Konsistenz-Review: B-0002 Influence

## Validation ID

VAL-0002

## Geprüftes Objekt

Alle Wissensobjekte aus B-0002 — Influence (Cialdini 2007)  
(ST-0024 bis ST-0049, A-0005 bis A-0012, MEC-0005 bis MEC-0009 + 3 erweiterte MECs, P-0008 bis P-0015, T-0005 bis T-0011, MOD-0002)

## Fragestellung

Sind alle Wissensobjekte intern konsistent, vollständig cross-referenziert, quellenbelegt und evidenzmäßig korrekt eingestuft?

## Prüfquelle(n)

Direkter Datei-Abgleich aller Wissensobjekte (2026-06-30)

---

## Prüfbereiche und Ergebnisse

### 1. Vollständigkeit der Objektmenge

| Objekttyp | Soll | Ist | Status |
|---|---|---|---|
| Statements (ST) | 26 | 26 | ✓ OK |
| Annahmen (A) | 8 | 8 | ✓ OK |
| Mechanismen (neu) | 5 | 5 | ✓ OK |
| Mechanismen (erweitert) | 3 | 3 | ✓ OK |
| Prinzipien (P) | 8 | 8 | ✓ OK |
| Techniken (T) | 7 | 7 | ✓ OK |
| Modelle (MOD) | 1 | 1 | ✓ OK |

**Gesamtprüfung:** Alle 26 ST-Objekte (ST-0024–ST-0049) vorhanden (Dateicount verifiziert: 30 Einträge im Ordner, davon 4 aus anderen Quellen — Differenz OK).

---

### 2. Source-ID-Integrität

**Geprüft:** Alle ST-, A-, MEC-, P-, T-, MOD-Objekte aus Influence auf korrekte Source-ID-Vergabe.

| Objekttyp | Source-ID vorhanden | Status |
|---|---|---|
| ST-Objekte (26) | 26/26 | ✓ OK |
| A-Objekte (8) | 8/8 | ✓ OK |
| MEC-Objekte (5 neu) | 5/5 | ✓ OK |
| P-Objekte (8) | 8/8 | ✓ OK |
| T-Objekte (7) | 7/7 | ✓ OK |
| MOD-0002 | 1/1 | ✓ OK |

---

### 3. Multi-Quellen-Anforderung bei Prinzipien (Pflichtprüfung TASK-0006)

Regel: Kein P-Objekt darf lediglich Reformulierung eines Einzelmechanismus sein. Jedes P muss aus ≥2 Mechanismen oder Annahmen abstrahiert sein.

| P-ID | MECs | A-Objekte | Abgrenzungsbegründung | Status |
|---|---|---|---|---|
| P-0008 | 5 (MEC-0005 bis MEC-0009) | 3 (A-0005, A-0006, A-0011) | Meta-Prinzip: kein Einzel-MEC | ✓ OK |
| P-0009 | 1 (MEC-0005) | 2 (A-0007, A-0011) | Dokumentiert: 3 Dimensionen über MEC-0005 hinaus | ✓ OK |
| P-0010 | 2 (MEC-0001 ext., MEC-0004 ext.) | 1 (A-0009) | Dokumentiert: Synthese beider MECs zur Sequenz-Architektur | ✓ OK |
| P-0011 | 1 (MEC-0006) | 2 (A-0005, A-0010) | Dokumentiert: Moderator-Analyse + Referenzgruppen-Implikation | ✓ OK |
| P-0012 | 1 (MEC-0007) | 2 (A-0010, A-0006) | Dokumentiert: Normative Neubewertung + Quantifizierung | ✓ OK |
| P-0013 | 1 (MEC-0008) | 2 (A-0010, A-0006) | Dokumentiert: Temporale Implikation + Signal vs. Substanz | ✓ OK |
| P-0014 | 2 (MEC-0009, MEC-0005) | 1 (A-0008) | Dokumentiert: Strategische Kontrolle + Dual-Mechanismus | ✓ OK |
| P-0015 | 1 (MEC-0003 ext.) | 2 (A-0012, A-0008) | Dokumentiert: Dual-Kanal-Synthese + Legitimitätsbedingung | ✓ OK |

**Befund:** Vier P-Objekte (P-0009, P-0011, P-0012, P-0013, P-0015) referenzieren nur einen Hauptmechanismus, aber je zwei A-Objekte. Die Multi-Quellen-Anforderung ("aus mehreren Mechanismen oder Annahmen") ist in allen Fällen erfüllt. Abgrenzungsbegründungen sind in den Objekten explizit dokumentiert. ✓

---

### 4. Canonicalisierungs-Dokumentation (MEC-Objekte)

**Geprüft:** Haben MEC-0001, MEC-0003, MEC-0004 (erweiterte MECs) eine Canonicalisierungs-Entscheidung dokumentiert?

| MEC | Entscheidung | Abschnitt vorhanden | Status |
|---|---|---|---|
| MEC-0001 | Erweitert: Bem's Self-Perception | ✓ | ✓ OK |
| MEC-0003 | Erweitert: Knappheit als Reaktanz | ✓ | ✓ OK |
| MEC-0004 | Erweitert: Lowballing + Post-Entscheidung | ✓ | ✓ OK |

---

### 5. ID-Referenz-Integrität in MOD-0002

**Geprüft:** Alle in MOD-0002 referenzierten IDs gegen tatsächlich existierende Dateien.

| Referenz-Typ | Referenzierte IDs | Dateien vorhanden | Status |
|---|---|---|---|
| Annahmen | A-0005 bis A-0012 | 8/8 | ✓ OK |
| Mechanismen | MEC-0005 bis MEC-0009 | 5/5 | ✓ OK |
| Prinzipien | P-0008 bis P-0015 | 8/8 | ✓ OK |
| Techniken | T-0005 bis T-0011 | 7/7 | ✓ OK |

---

### 6. Evidenzklassen-Konsistenz

| Objektgruppe | Einschätzung | Status |
|---|---|---|
| ST-Objekte | Alle mit Primärtext-Zitat oder direkter Quellenangabe | ✓ OK |
| A-Objekte | Keine eigene Evidenzklasse (abgeleitet aus STs) | ✓ OK |
| MEC-Objekte (neu) | E4 (allgem. Mechanismus) + E3 (Verkaufsanwendung) — korrekt differenziert | ✓ OK |
| P-Objekte | Alle vorläufig E3 — korrekt für Cialdini-Quelllage (Felddaten, begrenzte B2B-Replikation) | ✓ OK |
| T-Objekte | E3 (Techniken aus Felddaten, Labor) — korrekt | ✓ OK |
| MOD-0002 | M2 (Reifegrad) — korrekt für erste Extraktion ohne externe Validierung | ✓ OK |

---

### 7. Ethische Risiko-Markierungen

**Geprüft:** Haben alle Objekte mit hohem oder mittlerem ethischen Risiko eine Markierung?

| Objekt | Risiko | Markierung | Status |
|---|---|---|---|
| MEC-0005 (Reziprozität) | Mittel | "Uninvitierte Gaben" markiert | ✓ OK |
| MEC-0006 (Sozialbeweis) | Mittel | "Konstruierter Sozialbeweis" markiert | ✓ OK |
| MEC-0007 (Sympathie) | Mittel | "Sympathie-Engineering" markiert | ✓ OK |
| MEC-0008 (Autorität) | Hoch | ⚠ "Credential-Faking" markiert | ✓ OK |
| P-0008 (Meta-Prinzip) | Hoch | "Trigger bei inadäquatem Angebot" markiert | ✓ OK |
| P-0009 (Vorab-Leistung) | Mittel | Distinktion echte Leistung vs. Gift-Giving | ✓ OK |
| P-0013 (Autorität) | Hoch | "Authentisch vs. Fake" markiert | ✓ OK |
| P-0015 (Knappheit) | Hoch | "Legitime vs. konstruierte Knappheit" markiert | ✓ OK |
| T-0006 (Rejection-then-Retreat) | Mittel | "Erstforderung muss ernst sein" markiert | ✓ OK |
| T-0009 (Referenz) | Niedrig/Hoch | "Authentisch vs. konstruiert" markiert | ✓ OK |
| T-0010 (Credential) | Hoch | "Authentisch vs. Fake" markiert | ✓ OK |
| T-0011 (Knappheit) | Hoch | "Legitim vs. Fake-Scarcity" markiert | ✓ OK |

---

### 8. Sprachpolitik-Konformität

Stichprobe: Dateinamen auf Englisch (snake_case) ✓, Inhalte auf Deutsch ✓. Keine Abweichungen.

---

### 9. Widersprüche / offene Fragen (nicht behoben, dokumentiert)

| Nr. | Widerspruch / offene Frage | Wo dokumentiert |
|---|---|---|
| 1 | Gemini-Validierung für Replikationsstatus einzelner Studien (Milgram-Replikation, Langer-Xerox, Regan, Phillips-Werther) ausstehend | MEC-0005, MEC-0006, MEC-0007, MEC-0008 |
| 2 | Kahneman-Quervergleich (System 1/2 vs. Cialdini-Heuristiken) ausstehend | MOD-0002 |
| 3 | Anchoring (Tversky & Kahneman) vs. Kontrastprinzip (MEC-0009): operationell identisch? | MEC-0009, P-0014 |
| 4 | B2B-spezifische Evidenz für Reziprozitätsmechanismus in formalen Procurement-Prozessen fehlt | MEC-0005, P-0009 |
| 5 | P-0002 aus Pilot-001 referenziert "Kontrasteffekt" ohne MEC-Objekt — jetzt durch MEC-0009 gedeckt; P-0002 sollte in Folgerevision auf MEC-0009 aktualisiert werden | P-0002 (SRC-0001) |

**Empfehlung zu Nr. 5:** P-0002 aus SPIN Selling enthält Hinweis auf MEC-0005 als Kandidat (VAL-0001-Befund). Dieser Kandidat ist jetzt MEC-0009 (Perzeptueller Kontrast). P-0002 sollte in einer nachgelagerten Revisionsrunde aktualisiert werden. Kein Blocker für Influence-Abschluss.

---

### 10. Querverweise zwischen SRC-0001 und SRC-0002

Die Mechanismen MEC-0001 bis MEC-0004 wurden im Zuge von Influence erweitert. Beide Erweiterungsabschnitte und Canonicalisierungsentscheidungen sind in den jeweiligen MEC-Dateien dokumentiert. Cross-Source-Integrität: ✓

---

## Einschätzung

Die Wissensbasis für Influence ist intern konsistent. Alle Pflichtprüfungen (Source-ID, Multi-Quellen-Anforderung für Prinzipien, Canonicalisierungs-Dokumentation, ID-Referenz-Integrität, ethische Risiko-Markierungen) ergeben keine Blocker-Befunde.

Fünf offene Fragen sind dokumentiert und als Nicht-Blocker klassifiziert. Gemini-Validierung und Kahneman-Quervergleich sind als zukünftige Arbeiten markiert.

## Änderungsempfehlungen

1. **Nächste Revision:** P-0002 (SRC-0001) auf MEC-0009 aktualisieren (VAL-0001-Befund Nr. 3 aus Pilot-001 ist jetzt lösbar).
2. **Folgearbeit:** Gemini-Validierung für Replikationsstatus kritischer Studien (Befund Nr. 1).
3. **Folgearbeit:** Kahneman-Quervergleich durchführen — Kandidat für eigenes Modell oder MOD-0002-Ergänzung (Befund Nr. 2).
4. **Folgearbeit:** B2B-Spezifik der Reziprozitätswirkung recherchieren (Befund Nr. 4).

## Status

Abgeschlossen — 2026-06-30
