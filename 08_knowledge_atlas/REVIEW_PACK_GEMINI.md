# Atlas Review Pack — für Gemini Research (Validierung Compiler v0.1.1)

**Dokumentklasse:** Reference (Review-Handoff)
**Rolle bei Erstellung:** Editor (Claude) im Auftrag des Herausgebers — reine Zusammenstellung, keine neuen Analysen, keine Code-Änderungen
**Datum:** 2026-07-04
**Adressat:** Gemini, gemäß `01_framework/07_agent_protocols/gemini_validation_protocol.md` (Validierungs- und Gegenprüfungsassistent)
**Zweck:** Kompakter Prüfstand, mit dem Gemini jede Datei in `08_knowledge_atlas/` effizient gegen `ATLAS_MANIFEST.md` (v0.1-Scope) prüfen kann, ohne das gesamte Repository laden zu müssen.

---

## 1. Prüfauftrag

Bitte prüfen: Bildet jede Datei in `08_knowledge_atlas/` exakt den in `ATLAS_MANIFEST.md` Abschnitt 2 definierten Scope ab (Knoten-Basis 2.1, Kanten-Basis 2.2, Analyse-Fokus 2.3) — ohne eine der in Abschnitt 3 weiterhin ausgeschlossenen Erweiterungen (Layer, Rich Edges, Metriken, Query Engine)? Referenzdatei für den Soll-Zustand ist ausschließlich `ATLAS_MANIFEST.md`; dieses Review Pack ist ein Snapshot, keine eigene Autorität.

## 2. Vollständige Dateiliste mit Zweck

| Pfad | Zweck |
|---|---|
| `08_knowledge_atlas/ATLAS_MANIFEST.md` | Soll-Zustand: Scope-Definition v0.1 (Knoten-Basis, Kanten-Basis, Analyse-Fokus, explizite Ausschlüsse, Klarstellung zur Compiler-Implementierung als v0.1.1-Inkrement). Maßgebliches Prüfdokument. |
| `08_knowledge_atlas/REVIEW_PACK_GEMINI.md` | Dieses Dokument — Prüfstand-Zusammenstellung für Gemini, keine eigene Wissens- oder Scope-Quelle. |
| `08_knowledge_atlas/scripts/compile_atlas.py` | Ist-Zustand: Compiler-Implementierung v0.1.1. Scannt `03_knowledge_base/`, baut Knoten-/Kanten-Inventar, erkennt Reference Orphans, exportiert alle Output-Dateien. Reiner Python-Standardbibliothek-Code, keine externen Abhängigkeiten. |
| `08_knowledge_atlas/output/nodes.csv` | Vollständiges Knoten-Inventar (id, type, filename, path, title). 514 Zeilen (+ Header). |
| `08_knowledge_atlas/output/edges.csv` | Vollständige, deduplizierte, gerichtete Kantenliste (source_id, source_type, target_id, target_type, declared_in). 2076 Zeilen (+ Header). |
| `08_knowledge_atlas/output/reference_orphans.csv` | Teilmenge von `nodes.csv`: Knoten ohne jede eingehende oder ausgehende explizite Referenz. 18 Zeilen (+ Header). |
| `08_knowledge_atlas/output/atlas_network.dot` | Graphviz-Export (gerichteter Graph) derselben Knoten/Kanten, nur Knotentyp als Shape codiert — keine Kantentypisierung, keine Metriken. |
| `08_knowledge_atlas/output/atlas_compiler_report.md` | Menschenlesbarer Lauf-Report: Zahlen je Abschnitt, unaufgelöste Referenzen, Duplikat-IDs, Korrekturhistorie, Grenzen. Vollständige Langfassung der Zahlen unten in Abschnitt 4/5. |

Keine weiteren Dateien existieren aktuell in `08_knowledge_atlas/`.

## 3. Compiler-Stand

- **Version:** v0.1.1 ("Compiler Pilot") — laut `ATLAS_MANIFEST.md` Abschnitt 3 (Klarstellung vom 2026-07-04) ein separates, ausdrücklich freigegebenes Inkrement zum Scope-Manifest v0.1, keine rückwirkende Scope-Änderung.
- **Letzter Lauf:** 2026-07-04, deterministisch, rein lesend (keine Datei in `03_knowledge_base/` verändert).
- **Funktionsweise:** Volltext-Regex-Scan jeder Objektdatei in den sechs definierten `03_knowledge_base/`-Unterordnern auf ID-Muster der sechs Knotentypen. Selbstreferenzen werden verworfen, Mehrfachnennungen derselben Ziel-ID dedupliziert. Kanten werden gerichtet erfasst (`source_id -> target_id`, Provenienz über `declared_in`).

### Bekannte Korrektur (bereits durchgeführt, dokumentiert in `atlas_compiler_report.md` Abschnitt 6)

Der erste Compiler-Lauf erkannte Knoten-IDs nur im Standardformat `PRÄFIX-####` (vier Ziffern) und übersah dadurch vier real existierende Prinzip-Objekte mit abweichendem ID-Schema: **`P-S1-001` bis `P-S1-004`** (Sprint-1-Synthese-Prinzipien, Ordner `principles/`, YAML-Frontmatter `typ: Prinzip`). Nach Korrektur der ID-Erkennung (Knoten-ID wird aus dem Dateinamen abgeleitet statt aus einem festen Zahlenformat) sind alle vier Objekte sowie ihre Referenzen von/zu `MEC-0015`, `P-0028`, `ST-0150`, `ST-0156`, `ST-0164` korrekt erfasst. Kein neuer ID-Typ wurde dabei in den Scope aufgenommen — es handelte sich um einen Compiler-Bug, keine Scope-Erweiterung.

## 4. Aktuelle Node-/Edge-/Orphan-Zahlen (Stand des letzten Laufs)

| Kennzahl | Wert |
|---|---|
| Nodes gesamt | **514** |
| — ST (Statement) | 309 |
| — A (Annahme) | 60 |
| — MEC (Mechanismus) | 29 |
| — P (Prinzip) | 57 (davon 4 im Sonderformat `P-S1-XXX`) |
| — T (Technik) | 47 |
| — MOD (Modell) | 12 |
| Edges (gerichtet, dedupliziert) | **2076** |
| Reference Orphans gesamt | **18** (alle Typ `ST`, 5,8 % aller Statements; 0 % bei A/MEC/P/T/MOD) |
| Unaufgelöste Referenzen | **2** Nennungen, 1 betroffene Ziel-ID: `T-0048` (referenziert von `P-S1-003` und `ST-0307`, existiert nicht in `techniques/`) |
| Duplikat-IDs | **0** |

Vollständige Rohdaten: `output/nodes.csv`, `output/edges.csv`, `output/reference_orphans.csv`.

## 5. Bekannte Limitationen (v0.1.1)

- Reiner Struktur-Export — kein Query Interface, keine Layer, keine Rich Edges, keine Metriken (Manifest Abschnitt 3).
- Volltext-Scan ohne Abschnittserkennung: ID-Nennungen in Fließtext, Tabellen, Codeblöcken/ASCII-Diagrammen zählen gleichermaßen als explizite Referenz wie Nennungen in benannten Referenzabschnitten.
- Kompakte Bereichsangaben (z. B. „MEC-0005 bis MEC-0009", „MEC-0005–0009") werden nur an den textlich vollständig genannten IDs erkannt; implizite Zwischenwerte werden nicht rekonstruiert.
- Keine Gewichtung von Mehrfachnennungen derselben Referenz in einer Datei (dedupliziert zu einer Kante).
- Keine inhaltliche Validierung von Referenzen — nur Existenzprüfung gegen das Knoten-Inventar.
- IDs außerhalb der sechs definierten Typen (SRC-, VAL-, SPR-, B-, W-IDs) werden grundsätzlich ignoriert, auch im Fließtext.
- Sonder-ID-Formate (wie `P-S1-XXX`) werden nur als bekannte, real vorhandene Literale erkannt, nicht generisch — ein Tippfehler in einem Sonderformat würde nicht als unaufgelöste Referenz auffallen (nur beim Standardformat `PRÄFIX-####` zuverlässig).
- Kein inkrementeller Modus: jeder Lauf verarbeitet das gesamte Inventar neu, kein Diff gegen einen vorherigen Lauf außer der einmalig dokumentierten Korrektur in Abschnitt 6 des Compiler-Reports.

Vollständiger Wortlaut aller Limitationen: `output/atlas_compiler_report.md`, Abschnitt 7.

## 6. Hinweise für die Prüfung

- Dieses Pack enthält **keine neuen Änderungen** an Code oder Daten — reine Zusammenstellung des bestehenden Zustands zum 2026-07-04.
- Bei Abweichungen zwischen diesem Pack und dem tatsächlichen Repository-Zustand gilt das Repository (bzw. die Originaldateien in `08_knowledge_atlas/`) als Quelle der Wahrheit, nicht dieses Dokument.
- Etwaige Befunde bitte wie im Codex üblich einordnen: Manifest korrekt / Manifest unvollständig / Repository weicht vom Manifest ab / unklar — Herausgeberentscheidung erforderlich.

---

*Dieses Review Pack ist ein Snapshot-Dokument, kein Wissensobjekt und kein Ersatz für die Originaldateien. Es trifft keine eigene Bewertung und ersetzt keine Herausgeberentscheidung.*
