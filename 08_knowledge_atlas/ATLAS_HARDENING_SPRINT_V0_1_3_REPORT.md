# Atlas Hardening Sprint v0.1.3 — Report

**Dokumentklasse:** Reference (Sprint-Abschlussbericht)
**Rolle bei Erstellung:** Lead Software Engineer / Repository Architect / Release Engineer für den Knowledge Atlas, im Auftrag des Herausgebers
**Datum:** 2026-07-05
**Grundlage:** `08_knowledge_atlas/SECOND_AUDIT_REMAINING_FINDINGS_TRIAGE.md` (Befunde T-01, T-02, T-03), `08_knowledge_atlas/ATLAS_MANIFEST.md`, Auftrag „Sales Codex – Knowledge Atlas Hardening Sprint v0.1.3 + Release Verification Run"
**Zweck:** Dokumentiert die Umsetzung der drei freigegebenen Härtungsmaßnahmen H-01, H-02, H-03 in `compile_atlas.py` (v0.1.2 → v0.1.3). Für die tatsächliche Ausführungsverifikation siehe das separate Dokument `ATLAS_RELEASE_VERIFICATION_V0_1_3.md` — dieser Bericht beschreibt ausschließlich die Implementierung, nicht deren Laufzeitverifikation.

---

## 1. Executive Summary

Dieser Sprint setzt genau die drei in der technischen Triage (`SECOND_AUDIT_REMAINING_FINDINGS_TRIAGE.md`) als handlungsrelevant eingestuften Robustheitslücken um: H-01 (Duplicate-ID Hard Fail, Grundlage T-02), H-02 (konservative Genitiv-Normalisierung, Grundlage T-01) und H-03 (defensive Fence-Balance-Prüfung, Grundlage T-03). T-04, T-05, T-06 und T-07 wurden — wie im Auftrag ausdrücklich vorgegeben — bewusst nicht bearbeitet.

Alle drei Maßnahmen wurden ausschließlich in `08_knowledge_atlas/scripts/compile_atlas.py` umgesetzt. Keine Wissensobjekte wurden verändert, keine Manifest-Änderung war zwingend erforderlich. Die Compiler-Version wurde im Dateikopf, in der DOT-Export-Kopfzeile und im generierten Report auf `v0.1.3` angehoben.

**Wichtige Einschränkung dieses Berichts:** Dieser Bericht deckt ausschließlich **Phase 1 (Implementierung)** ab. Die in Phase 2 geforderte tatsächliche Ausführungsverifikation (RV-01 bis RV-07) ist Gegenstand von `ATLAS_RELEASE_VERIFICATION_V0_1_3.md`. Der dortige Status ist entscheidend dafür, ob die hier beschriebene Implementierung tatsächlich als funktionsfähig gelten kann — dieser Bericht allein stellt **keine** Freigabe dar.

---

## 2. Ausgangslage

Die technische Triage vom 2026-07-05 hatte für die sieben verbleibenden Befunde des zweiten Audits folgende Einordnung ergeben (der zuvor separat geprüfte und zurückgewiesene Crash-Befund ist nicht Teil dieser Triage):

| Befund | Klassifikation | Priorität | In diesem Sprint bearbeitet? |
|---|---|---|---|
| T-01 (Genitiv-Suffix) | CONFIRMED ROBUSTNESS GAP | P2 | Ja (H-02) |
| T-02 (Duplicate-ID) | CONFIRMED ROBUSTNESS GAP | P1 | Ja (H-01) |
| T-03 (ungeschlossene Fenced Code Blocks) | CONFIRMED ROBUSTNESS GAP (Audit-Wirkung korrigiert) | P3 | Ja (H-03) |
| T-04 (ungepaarte Inline-Backticks) | CONFIRMED ROBUSTNESS GAP (Audit-Wirkung korrigiert) | P3 | Nein (laut Auftrag ausgeschlossen) |
| T-05 (T-0048) | DATA FINDING | — | Nein (Redaktionsentscheidung) |
| T-06 (Bereichsauflösung) | INTENTIONAL SCOPE DECISION | P4 | Nein (bereits entschieden) |
| T-07 (alphabetisches Sonderformat) | HYPOTHETICAL LIMITATION | P4 | Nein (kein aktueller Bedarf) |

Der Auftrag für diesen Sprint übernimmt diese Einordnung unverändert und grenzt den Umsetzungsscope explizit auf H-01, H-02 und H-03 ein.

---

## 3. Implementierter Scope

Einzige geänderte Codedatei: `08_knowledge_atlas/scripts/compile_atlas.py`.

Neue/geänderte Funktionen:
- `abort_on_duplicate_ids(result)` — neu (H-01)
- `try_genitive_normalization(token, nodes)` — neu (H-02)
- `check_fence_balance(rel_path, raw_text)` — neu (H-03)
- `extract_references()` — erweitert um Aufruf der Fence-Balance-Prüfung und der Genitiv-Normalisierung; Selbstreferenz-Prüfung erfolgt jetzt nach der Normalisierung
- `main()` — ruft `abort_on_duplicate_ids()` unmittelbar nach `build_node_inventory()` und vor `extract_references()` auf
- `write_report()` — neue Abschnitte/Hinweise zu H-01 (Abschnitt 5), H-02/H-03-Kennzahlen (Abschnitt 6.3), aktualisierte Grenzen (Abschnitt 7)
- `CompilerResult` — zwei neue Felder: `fence_warnings: list[str]`, `genitive_normalizations: int`
- Kopfkommentar, `COMPILER_VERSION`-Konstante, DOT-Export-Kopfzeile: `v0.1.2` → `v0.1.3`

Nicht verändert: `split_prefix()`, `GENERIC_ID_PATTERN`, `mask_non_reference_regions()`, `build_node_inventory()` (Knoten-Identifikation selbst), `find_reference_orphans()`, CSV-/DOT-Schema (Spalten unverändert), alle Wissensobjekte in `03_knowledge_base/`.

---

## 4. H-01 — Duplicate-ID Hard Fail

**Zielverhalten laut Auftrag:** Bei erkannter Duplicate-ID müssen alle kollidierenden Dateipfade ausgegeben, der Compiler mit Exit Code != 0 beendet, die Referenzextraktion nicht auf mehrdeutiger Basis fortgesetzt und keine Outputs erzeugt/überschrieben werden.

**Umsetzung:** `build_node_inventory()` bleibt unverändert — sie erkennt Duplikate weiterhin vollständig (`result.duplicate_ids`, jede beanspruchende Datei erfasst). Neu ist `abort_on_duplicate_ids(result)`, die unmittelbar danach in `main()` aufgerufen wird:

```python
result = CompilerResult()
id_claims = build_node_inventory(result)

abort_on_duplicate_ids(result)   # H-01: Hard Fail hier, vor allem Weiteren

extract_references(result)
orphans = find_reference_orphans(result)
... (Output-Erzeugung folgt erst danach)
```

`abort_on_duplicate_ids()` gibt bei mindestens einer Duplicate-ID auf `stderr` aus: die Gesamtzahl betroffener IDs, für jede ID alle beanspruchenden Dateipfade, und eine explizite Bestätigung, dass keine Outputs erzeugt/überschrieben wurden — und beendet den Prozess mit `sys.exit(1)`. Da dieser Aufruf vor `extract_references()` und vor allen `write_*`-Funktionen erfolgt, ist ausgeschlossen, dass bei einer Duplicate-ID jemals eine Referenzextraktion auf mehrdeutiger Node-Basis läuft oder ein Output-Artefakt (auch nur teilweise) neu geschrieben wird.

**Architekturprinzip umgesetzt:** Kein automatisches Merge, kein „first file wins" auf Output-Ebene (die interne Datenstruktur `result.nodes` registriert weiterhin technisch nur die erste Datei — das ist notwendig, um den Duplikatstatus überhaupt korrekt zu erkennen und auszugeben —, aber diese Datenlage wird nie in einen Output überführt, da der Prozess vorher abbricht). Keine heuristische Auswahl der „richtigen" Datei.

---

## 5. H-02 — Genitiv-Normalisierung

**Zielverhalten laut Auftrag:** Normalisierung eines Tokens wie „MEC-0011s" auf „MEC-0011" nur, wenn (1) das volle Token nicht existiert, (2) es exakt auf ein kleines „s" endet, (3) die Basis-ID (Token ohne „s") existiert und (4) diese Basis-ID dem Standard-ID-Format entspricht.

**Umsetzung:** Neue Funktion `try_genitive_normalization(token, nodes)`:

```python
def try_genitive_normalization(token, nodes):
    if len(token) < 2 or token[-1] != "s":
        return None
    candidate = token[:-1]
    candidate_node = nodes.get(candidate)
    if candidate_node is None:
        return None
    if not candidate_node.is_standard:
        return None
    return candidate
```

Aufruf in `extract_references()`, ausschließlich im bereits bestehenden Zweig „Token existiert nicht im Knoten-Inventar" (Bedingung 1 ist damit strukturell durch den Aufrufkontext erzwungen — die Funktion wird gar nicht erst aufgerufen, wenn das volle Token bereits existiert):

```python
if target_id not in result.nodes:
    normalized = try_genitive_normalization(target_id, result.nodes)
    if normalized is not None:
        target_id = normalized
        result.genitive_normalizations += 1

if target_id == node.id:
    continue  # Selbstreferenz ignorieren (auch nach Normalisierung)

if target_id not in result.nodes:
    result.unresolved_references.append(...)
    continue
...
```

**Wichtige Reihenfolge-Entscheidung:** Die Selbstreferenz-Prüfung (`target_id == node.id`) wurde bewusst **hinter** die Normalisierung verschoben. In v0.1.2 verglich sie das rohe, noch nicht normalisierte Token — dadurch wurden echte Selbstreferenzen in Genitivform (z. B. „MEC-0011s" in der Datei von MEC-0011 selbst) nicht erkannt und fälschlich als unaufgelöste Referenz gemeldet. Mit der neuen Reihenfolge greift der Selbstreferenz-Ausschluss korrekt auch nach Normalisierung (siehe RV-03, Fall D).

**Bedingung 4 (Standardformat-Pflicht der Basis-ID):** Verhindert, dass eine hypothetische, real existierende Sonderformat-ID, die zufällig auf „s" endet, ungewollt gekürzt wird. Dies ist die konservativste der im Triage-Dokument bewerteten Optionen (Option 2, mit zusätzlicher Einschränkung auf Standardformat-Basis-IDs).

**Dedup-Verhalten:** Da die Normalisierung vor der Kantenbildung erfolgt, dedupliziert `seen_edges` korrekt gegen bereits über die reguläre (nicht-genitivische) Schreibweise erfasste Kanten — eine bereits bestehende Kante wird durch eine zusätzliche Genitivform-Nennung nicht verdoppelt.

**Nicht umgesetzt (laut Auftrag ausdrücklich untersagt):** keine pauschale Entfernung jedes abschließenden „s", keine Aufweichung von `GENERIC_ID_PATTERN` selbst, keine Korrektur „erratener" unbekannter Tokens, keine Normalisierung, wenn das volle Token bereits existiert, keine Änderung an echten Sonderformat-IDs.

---

## 6. H-03 — Fence-Balance-Prüfung

**Zielverhalten laut Auftrag:** Minimale defensive Prüfung, ob die Anzahl der Fenced-Code-Marker (```) pro Datei plausibel balanciert ist; bei Abweichung eine klare Warnung mit Datei- und Problembenennung, deterministisches Verhalten, keine große Architektur.

**Umsetzung:** Neue Funktion `check_fence_balance(rel_path, raw_text)`, aufgerufen in `extract_references()` auf dem unmaskierten `raw_text` (vor `mask_non_reference_regions()`, da die Marker danach bereits durch Leerzeichen ersetzt wären):

```python
def check_fence_balance(rel_path, raw_text):
    count = raw_text.count("```")
    if count % 2 != 0:
        return f"Unbalancierte Fenced-Code-Bloecke in `{rel_path}`: {count} ..."
    return None
```

Warnungen werden in `result.fence_warnings` gesammelt, am Ende des Laufs auf `stdout` ausgegeben und im generierten Report (Abschnitt 6.3) mit Dateibezug dokumentiert. Es handelt sich um eine reine Zählung der literalen Zeichenfolge ` ``` ` — keine Markdown-AST, keine zeilenweise State-Machine, kein Hard Fail. Bei einer Abweichung läuft der Compiler unverändert weiter; die Warnung ist rein informativ (entsprechend der ausdrücklichen Auftragsvorgabe, dies „klein zu halten").

**Bewusst nicht umgesetzt:** Erkennung, welcher konkrete Block unbalanciert ist (nur die Gesamtzahl je Datei wird geprüft); keine Unterscheidung zwischen „ein Block fehlt am Ende" und „ein ``` wird zweckentfremdet als Trenner verwendet" — beides würde eine State-Machine erfordern, die laut Auftrag explizit nicht gefordert ist, solange eine kleine, robuste Prüfung genügt.

---

## 7. Nicht umgesetzte Punkte

Wie im Auftrag ausdrücklich vorgegeben, wurden folgende Punkte **nicht** bearbeitet:

- **T-04 (Inline-Backtick-Hardening):** keine zusätzliche Logik. Begründung (aus der Triage übernommen): Schadensradius strukturell auf eine Zeile begrenzt, aktueller Bestand frei von Fällen.
- **T-05 (T-0048):** keine Technik angelegt, keine Wissensobjekte geändert, keine Referenzen korrigiert. Bleibt redaktioneller Datenbefund.
- **T-06 (Bereichsauflösung):** keine automatische Auflösung von Bereichsnotationen implementiert. Bereits bewusst zurückgestellte Scope-Entscheidung, unverändert gültig.
- **T-07 (alphabetische Sonderformate):** keine Parser-Erweiterung für hypothetische Formate wie „P-ALPHA-001". Kein aktueller Anwendungsfall, keine Governance-Regel.

Zusätzlich wurden — wie in den „Allgemeinen Implementierungsregeln" des Auftrags gefordert — keine semantischen Relationstypen, Gewichte, Scores, Zentralitätsmetriken, Embeddings, KI-Auswertungen, Datenbanken, Query Engines, Layer oder automatische Bereichsauflösung eingeführt.

---

## 8. Geänderte Dateien

- `08_knowledge_atlas/scripts/compile_atlas.py` — einzige inhaltliche Codeänderung (v0.1.2 → v0.1.3).
- `08_knowledge_atlas/output/*` — werden bei erfolgreichem Compilerlauf automatisch regeneriert (nicht manuell bearbeitet); Status siehe `ATLAS_RELEASE_VERIFICATION_V0_1_3.md`.
- `08_knowledge_atlas/ATLAS_HARDENING_SPRINT_V0_1_3_REPORT.md` — dieses Dokument (neu).
- `08_knowledge_atlas/ATLAS_RELEASE_VERIFICATION_V0_1_3.md` — Release Verification Report (neu, separates Dokument).

Nicht verändert: `08_knowledge_atlas/ATLAS_MANIFEST.md`, alle Wissensobjekte in `03_knowledge_base/`, `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`.

---

## 9. Technische Auswirkungen

- **Datenintegrität:** H-01 schließt den einzigen in der Triage identifizierten Mechanismus für stillen, schwer entdeckbaren Kantenverlust (künftige Duplicate-IDs). Ein Duplikat blockiert jetzt den gesamten Lauf, statt unauffällig unvollständige Kanten zu erzeugen.
- **Report-Qualität:** H-02 reduziert die Anzahl falscher „unaufgelöster Referenzen" im aktuellen Bestand um die fünf empirisch nachgewiesenen Genitiv-Fälle (`MEC-0011s` × 4 Nennungen, `MEC-0018s` × 1 Nennung — siehe Triage T-01), ohne die Kantenstruktur selbst zu verändern (keine der betroffenen Nennungen erzeugt eine neue, vorher fehlende Kante — siehe Triage-Nachweis, dass die einzige nicht-selbstreferenzielle Nennung bereits anderweitig als Kante erfasst war).
- **Frühwarnung:** H-03 macht künftige unbalancierte Fenced-Code-Blöcke sichtbar, statt sie unbemerkt zu lassen — ohne das aktuelle (bereits balancierte) Verhalten zu verändern.
- **Keine Änderung der Kern-Nodeanzahl, Kantenlogik für Nicht-Genitiv-Fälle oder Orphan-Definition.**

---

## 10. Bekannte verbleibende Einschränkungen

- H-02 normalisiert ausschließlich Genitiv-„s" an Standardformat-Basis-IDs — andere Suffixformen (z. B. „-er", Apostroph-Genitiv, Genitiv-„s" an einer Sonderformat-ID) bleiben unaufgelöst.
- H-03 prüft nur die Gesamtzahl der Fence-Marker je Datei, nicht die korrekte paarweise Zuordnung einzelner Blöcke.
- T-04, T-05, T-06, T-07 bleiben wie vereinbart unbearbeitet.
- Die vorbestehende Formulierungsspannung im Manifest (Abschnitt 2.2 spricht von „ungerichtet-neutral", während der Compiler seit einer früheren, vom Herausgeber freigegebenen Korrektur gerichtete Kanten mit `source_id`/`target_id` erfasst) besteht unverändert fort. Sie wurde nicht durch diesen Sprint verursacht und ist nicht Teil des freigegebenen Scopes von H-01/H-02/H-03 — wird hier nur der Vollständigkeit halber erneut dokumentiert, nicht neu bewertet oder behoben.

---

## 11. Übergabe an Release Verification

Die hier beschriebene Implementierung ist nach bestem Wissen manifest-konform, konservativ und auf den freigegebenen Scope beschränkt. Ob sie tatsächlich fehlerfrei läuft und die erwarteten Effekte erzielt, kann jedoch **ausschließlich durch tatsächliche Ausführung** bestätigt werden — nicht durch diese Implementierungsbeschreibung allein. Die entsprechende Prüfung (RV-01 bis RV-07) sowie das abschließende Release Gate sind in `08_knowledge_atlas/ATLAS_RELEASE_VERIFICATION_V0_1_3.md` dokumentiert.

---

*Dieser Bericht beschreibt eine Implementierung, keine Verifikation. Er ersetzt keine Herausgeberentscheidung und ist kein Wissensobjekt.*
