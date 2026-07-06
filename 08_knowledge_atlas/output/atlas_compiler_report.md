# Atlas Compiler Report — v0.1.3 (Hardening Sprint)

**Dokumentklasse:** Reference (Generierter Analyse-Output)
**Erzeugt von:** `08_knowledge_atlas/scripts/compile_atlas.py`
**Erzeugt am:** 2026-07-06
**Grundlage:** `08_knowledge_atlas/ATLAS_MANIFEST.md`, Abschnitt 2 (Knoten-Basis, Kanten-Basis, Analyse-Fokus)
**Hinweis:** Rein lesend erzeugt. Keine Wissensobjekte in `03_knowledge_base/` wurden verändert. Dieser Report wird nur erzeugt, wenn keine Duplicate-IDs vorliegen (H-01) — siehe Abschnitt 5.

---

## 1. Nodes je Typ

| ID-Präfix | Objekttyp | Anzahl |
|---|---|---|
| `ST` | Statement | 309 |
| `A` | Annahme | 60 |
| `MEC` | Mechanismus | 30 |
| `P` | Prinzip | 57 |
| `T` | Technik | 47 |
| `MOD` | Modell | 12 |
| **Gesamt** | | **515** |
| davon Sonder-ID-Format (z. B. `P-S1-XXX`) | | 4 |

## 2. Edges

Anzahl gerichteter, deduplizierter expliziter Referenzen: **2111**

Eine Kante `(source_id -> target_id)` bedeutet: Die Datei von `source_id` enthält im Volltext (außerhalb von Code-Blöcken, Inline-Code und HTML-Kommentaren) eine explizite Nennung von `target_id`. Keine semantische Typisierung, keine Gewichtung (Manifest Abschnitt 2.2). Seit v0.1.2 enthält jede Kante zusätzlich die Zeilennummer der (ersten) Fundstelle (`edges.csv`, Spalte `line_number`). Seit v0.1.3 kann `target_id` auch das Ergebnis einer konservativen Genitiv-Normalisierung sein (H-02, siehe Abschnitt 6.3).

## 3. Reference Orphans

Anzahl Reference Orphans (Knoten ohne jede eingehende oder ausgehende explizite Referenz): **18** von 515 Knoten

| ID-Präfix | Objekttyp | Orphans | Nodes gesamt | Anteil |
|---|---|---|---|---|
| `ST` | Statement | 18 | 309 | 5.8% |
| `A` | Annahme | 0 | 60 | 0.0% |
| `MEC` | Mechanismus | 0 | 30 | 0.0% |
| `P` | Prinzip | 0 | 57 | 0.0% |
| `T` | Technik | 0 | 47 | 0.0% |
| `MOD` | Modell | 0 | 12 | 0.0% |

Vollständige Liste: `reference_orphans.csv`. Ein Reference-Orphan-Befund ist keine Qualitätsaussage (Manifest Abschnitt 4).

## 4. Unaufgelöste Referenzen

Anzahl textlicher ID-Muster, die auf keine existierende Node-ID im Knoten-Inventar verweisen: **2**
Anzahl unterschiedlicher betroffener Ziel-IDs: **1**

| Referenzierte (nicht existierende) ID | Genannt in |
|---|---|
| `T-0048` | P-S1-003, ST-0307 |

## 5. Duplikat-IDs

Seit v0.1.3 (H-01) bricht der Compiler bei erkannten Duplikat-IDs vor der Referenzextraktion und vor jeder Output-Erzeugung mit Exit Code != 0 ab (siehe `abort_on_duplicate_ids()`). Dieser Report wird also nur erzeugt, wenn zum Zeitpunkt des Laufs **keine** Duplikat-IDs vorlagen.

Keine Duplikat-IDs gefunden (jede ID wird in genau einer Datei beansprucht).

## 6. Korrekturhistorie

### 6.1 Erster Lauf → Sonder-ID-Korrektur (2026-07-04, v0.1.1)

Der erste Compiler-Lauf erkannte Node-IDs nur im Standardformat `PRÄFIX-####`. Vier reale Prinzip-Objekte mit Sonderformat (`P-S1-001` bis `P-S1-004`) fehlten dadurch im Knoten-Inventar. Nach Korrektur der Knoten-Identifikation (dateinamenbasiert statt festes Zahlenformat) waren alle vier Objekte und ihre Referenzen erfasst, jedoch über ein zusätzliches, statisch codiertes Literal-Verzeichnis im Referenz-Scan (asymmetrische Parser-Logik).

| Kennzahl | v0.1 (Standardformat-Bug) | v0.1.1 (Literal-Fix) |
|---|---|---|
| Nodes gesamt | 510 | 514 |
| Edges | 2031 | 2076 |
| Reference Orphans | 18 | 18 |
| Unaufgelöste Referenzen | 1 | 2 |

### 6.2 Architecture Review Implementation (2026-07-04, v0.1.2)

Externes Architecture Review identifizierte die in 6.1 beschriebene Literal-Lösung als architektonischen Mangel (Befund F-01, MAJOR): Tippfehler in Sonder-ID-Referenzen wurden dadurch stillschweigend ignoriert statt als unaufgelöste Referenz gemeldet. Zusätzlich fehlte eine Vorfilterung von Code-Blöcken/Kommentaren (F-02) und eine Zeilennummer in der Kanten-Herkunft (F-04). Details: `08_knowledge_atlas/ATLAS_ARCHITECTURE_REVIEW_IMPLEMENTATION_REPORT.md`.

| Kennzahl | v0.1.1 (vor Review-Sprint) | v0.1.2 |
|---|---|---|
| Nodes gesamt | 514 | 514 |
| Edges | 2076 | 2071 |
| Reference Orphans | 18 | 18 |
| Unaufgelöste Referenzen | 2 | 7 |
| Duplikat-IDs | 0 | 0 |

### 6.3 Atlas Hardening Sprint v0.1.3 (2026-07-05)

Ein zweites, unabhängiges Architecture Audit (`SECOND_INDEPENDENT_ARCHITECTURE_AUDIT.md`) sowie die anschließende technische Triage (`SECOND_AUDIT_REMAINING_FINDINGS_TRIAGE.md`) identifizierten drei umzusetzende Robustheitslücken: H-01 (Duplicate-ID-Verhalten, T-02), H-02 (Genitiv-Suffix-Erkennung, T-01) und H-03 (fehlende Fence-Balance-Prüfung, T-03). Alle drei wurden in diesem Sprint umgesetzt (siehe `ATLAS_HARDENING_SPRINT_V0_1_3_REPORT.md` für Details). Der zuvor im zweiten Audit behauptete deterministische Laufzeitabsturz wurde bereits separat als nicht reproduzierbar zurückgewiesen (`SECOND_AUDIT_CRASH_FINDING_VERIFICATION.md`) und ist von diesem Sprint nicht betroffen.

| Kennzahl | v0.1.2 (vor Hardening) | v0.1.3 (aktueller Lauf) |
|---|---|---|
| Nodes gesamt | 514 | 515 |
| Edges | 2071 | 2111 |
| Reference Orphans | 18 | 18 |
| Unaufgelöste Referenzen | 7 | 2 |
| Duplikat-IDs | 0 | 0 |
| Genitiv-Normalisierungen (H-02, Diagnosezähler) | — | 5 |
| Fence-Balance-Warnungen (H-03) | — | 0 |

**Fence-Balance-Warnungen (H-03):** Keine — alle geprüften Dateien mit Fenced-Code-Blöcken sind balanciert.

## 7. Grenzen des Compilers v0.1.3

- **Kein Query Interface, keine Layer, keine Rich Edges, keine Metriken** — dies ist ein reiner Struktur-Export gemäß Manifest Abschnitt 3, keine Analyseplattform.
- **Volltext-Scan ohne Abschnittserkennung (reduziert, nicht behoben).** Seit v0.1.2 werden Code-Blöcke, Inline-Code und HTML-Kommentare vor dem Scan ausgeschlossen. Der Compiler unterscheidet aber weiterhin nicht, ob eine verbleibende ID-Nennung in einem benannten Referenzabschnitt, in normalem Fließtext oder in einer Tabelle steht — jede dieser Nennungen zählt gleichermaßen als explizite Referenz.
- **Sonderformat-Erkennung erfordert mindestens eine Ziffer im ersten Suffix-Segment.** Diese Heuristik unterscheidet echte Sonder-IDs (z. B. "S1" in `P-S1-001`) von den im Repository sehr häufigen generischen Begriffen wie "T-Objekt", "P-Kandidat" oder "MEC-ID". Ein rein alphabetisches Sonderformat ohne jede Ziffer (z. B. hypothetisch "P-ALPHA-001") würde dadurch nicht erkannt — im aktuellen Repository-Bestand kommt ein solches Format nicht vor und ist auch durch keine Governance-Regel vorgesehen (Triage T-07, bewusst nicht in v0.1.3 adressiert).
- **Genitiv-Normalisierung (H-02) ist bewusst eng gefasst.** Nur ein Token, das (a) nicht selbst existiert, (b) auf ein kleines "s" endet und (c) dessen Basis-ID im Standardformat (PRÄFIX-####) existiert, wird normalisiert. Andere Suffixe (z. B. "MEC-0011er", Genitiv mit Apostroph, oder ein Genitiv-"s" an einer Sonderformat-ID) werden weiterhin nicht aufgelöst und bleiben unaufgelöste Referenzen. Dies ist eine bewusste Konservativität, kein technisches Versehen.
- **Kompakte Bereichsangaben werden nicht aufgelöst (bewusst, siehe F-03).** Notationen wie "MEC-0005 bis MEC-0009" werden nur an den textlich vollständig genannten IDs erkannt. Diese Erweiterung wurde im Architecture Review vorgeschlagen, vom Herausgeber aber ausdrücklich nicht freigegeben und daher nicht implementiert.
- **Fence-Balance-Prüfung (H-03) ist eine reine Zählung, keine Strukturprüfung.** Sie erkennt eine ungerade Gesamtzahl von ``` je Datei, kann aber eine geradzahlige, jedoch falsch gepaarte Konstellation (z. B. ``` als unbeabsichtigter Trenner) nicht erkennen. Kein Markdown-AST, keine zeilenweise State-Machine — bewusst minimal gehalten (Triage T-03: aktuell kein realer Vorkommensfall im Bestand).
- **Inline-Backtick-Hardening (T-04) wurde bewusst nicht umgesetzt.** Der theoretische Schadensradius ist durch die Musterkonstruktion (`` `[^`\n]+` ``) strukturell auf eine einzelne Zeile begrenzt; im aktuellen Bestand existiert kein Fall eines ungepaarten Backticks (empirisch verifiziert, siehe Triage T-04).
- **Keine Gewichtung von Mehrfachnennungen.** Wird dieselbe Ziel-ID mehrfach in derselben Quelldatei genannt, entsteht dennoch nur eine Kante; die gespeicherte Zeilennummer bezieht sich auf die erste Fundstelle, nicht auf alle Fundstellen.
- **Keine Validierung der inhaltlichen Richtigkeit** einer Referenz — der Compiler prüft nur, ob die referenzierte ID im Knoten-Inventar existiert (siehe Abschnitt 4), nicht ob die Referenz fachlich sinnvoll ist.
- **Keine Erkennung von IDs außerhalb der sechs definierten Typen** (z. B. SRC-, VAL-, SPR-, B-, W-IDs) — diese sind laut Manifest Abschnitt 2.1 nicht Teil der Knoten-Basis und werden vom Compiler grundsätzlich ignoriert, auch wenn sie im Fließtext vorkommen.
- **Dateinamenbasierte ID-Zuordnung.** Die ID eines Knotens wird ausschließlich aus dem Dateinamen abgeleitet (Segment vor dem ersten Unterstrich). Abweichungen zwischen Dateiname und internem ID-Feld werden nicht geprüft.
- **Kein inkrementeller Modus.** Jeder Lauf verarbeitet das gesamte Knoten-Inventar neu; es gibt keinen automatisierten Abgleich gegen einen vorherigen Lauf (die Vergleiche in Abschnitt 6 sind manuell dokumentierte Einzelfälle, kein laufender Mechanismus).

---

*Dieser Report ist ein generierter Analyse-Output, kein Wissensobjekt. Er ersetzt keine Herausgeberentscheidung und trifft keine inhaltliche Bewertung.*
