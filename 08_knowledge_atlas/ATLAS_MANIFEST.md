# Atlas Manifest — Knowledge Atlas v0.1

**Dokumentklasse:** Reference (Subsystem-Definition)
**Rolle bei Erstellung:** Editor (Claude) im Auftrag des Herausgebers — Initialisierung eines neuen Entwicklungsbausteins für Sales Codex v1.1
**Datum:** 2026-07-04
**Status:** Scope-Entwurf v0.1 — noch keine Implementierung, kein Code, keine Analyse durchgeführt
**Zweck:** Definiert den minimalen, freigegebenen Erstumfang des Knowledge Atlas als Analyse-Subsystem über dem bestehenden Sales-Codex-Repository.

---

## 1. Einordnung

Der Knowledge Atlas ist ein potenzieller neuer Entwicklungsbaustein für Sales Codex v1.1. Er ist kein eigenständiges Wissensobjekt (kein ST/P/A/T/MEC/MOD) und kein Framework-Dokument im Sinne von `01_framework/`, sondern ein Analyse-Subsystem, das bestehende Wissensobjekte und ihre expliziten Verknüpfungen strukturell auswertet.

Ablageort: `08_knowledge_atlas/` (Top-Level, nächste freie Ordnernummer — siehe Abschnitt 6).

Leitprinzip für diesen und alle folgenden Atlas-Schritte: **Große Vision, kleine Arbeitsaufträge. Das Repository ist die Source of Truth.** Dieses Manifest beschreibt ausschließlich v0.1. Spätere Versionen (Layer, Rich Edges, Metriken, Query Engine, Code-Parser) werden erst nach separater Freigabe als eigene Manifest-Versionen ergänzt, nicht rückwirkend in dieses Dokument eingearbeitet.

## 2. Scope v0.1

### 2.1 Knoten-Basis

Knoten sind ausschließlich Wissensobjekte mit expliziter ID aus der Knowledge Base, entsprechend den in `01_framework/05_knowledge_model/canonical_knowledge_model.md` definierten Objekttypen:

| ID-Präfix | Objekttyp | Fundort |
|---|---|---|
| `ST` | Statement | `03_knowledge_base/statements/` |
| `A` | Annahme | `03_knowledge_base/assumptions/` |
| `MEC` | Mechanismus | `03_knowledge_base/mechanisms/` |
| `P` | Prinzip | `03_knowledge_base/principles/` |
| `T` | Technik | `03_knowledge_base/techniques/` |
| `MOD` | Modell | `03_knowledge_base/models/` |

Kein anderer Objekttyp (SRC, VAL, SPR, Kompetenzen, Meta-Modelle, Beobachtungen etc.) ist in v0.1 Teil der Knoten-Basis.

### 2.2 Kanten-Basis

Kanten sind ausschließlich explizite Referenzen zwischen den unter 2.1 definierten Knoten.

Eine explizite Referenz ist jede bewusst deklarierte Objekt-ID (`ST-XXXX`, `A-XXXX`, `MEC-XXXX`, `P-XXXX`, `T-XXXX`, `MOD-XXXX`) innerhalb der dafür vorgesehenen Repository-Struktur einer Objektdatei — insbesondere benannte Referenzabschnitte, Listen oder Tabellen (z. B. "Verknüpfte Prinzipien", "Mögliche Annahmen", "Enthaltene Prinzipien", "Genutzter Mechanismus" und vergleichbare, in den Templates unter `01_framework/08_templates/` vorgesehene Felder). Der Atlas geht dabei von keiner bestimmten Markdown-Syntax aus — maßgeblich ist die bewusste Deklaration der Objekt-ID im dafür vorgesehenen Referenzformat, nicht ihre technische Notation.

Der Atlas interpretiert keine Bedeutung der Referenz. Er stellt ausschließlich fest, dass eine explizite Referenz zwischen zwei Objekten existiert — unabhängig davon, in welchem benannten Abschnitt sie steht, in welche Richtung sie zeigt oder was sie inhaltlich ausdrückt (z. B. "unterstützt", "widerspricht", "leitet ab"). Keine implizite Ableitung, keine Gewichtung, keine Typisierung der Kante — jede Kante ist in v0.1 ungerichtet-neutral im Sinne von "es existiert eine explizite Referenz zwischen Knoten X und Knoten Y".

### 2.3 Analyse-Fokus

Einziger Analyse-Zweck in v0.1: **Reference-Orphan-Identifikation.**

Ein Knoten gilt als Reference Orphan, wenn er innerhalb der unter 2.1 definierten Knoten-Basis weder eingehende noch ausgehende expliziten Referenzen (2.2) zu einem anderen Knoten dieser Basis besitzt.

> Ein Reference Orphan ist ein Knoten ohne eingehende oder ausgehende explizite Referenzen innerhalb des für den Atlas definierten Scopes. Der Begriff beschreibt ausschließlich den strukturellen Zustand des Graphen und trifft keine Aussage über die fachliche Qualität oder Vollständigkeit des Wissensobjekts.

Kein Scoring, keine Zentralitätsmetrik, keine Cluster- oder Community-Erkennung — ausschließlich die binäre Feststellung "referenziert" vs. "Orphan".

## 3. Explizit ausgeschlossen in v0.1

- Zusätzliche Layer (z. B. thematische, chronologische oder Buch-Layer)
- Rich Edges (typisierte, gewichtete oder gerichtete Kantenbedeutung)
- Metriken (Zentralität, Cluster-Koeffizient, Pfadlängen o. ä.)
- Query Engine oder interaktive Abfrageschnittstelle
- Code-Parser oder automatisierte Extraktion — v0.1 definiert nur den Scope, keine Implementierung

Diese Punkte sind nicht verworfen, sondern bewusst auf spätere, separat freizugebende Atlas-Versionen verschoben.

**Klarstellung zur Compiler-Implementierung (ergänzt 2026-07-04):** Der Ausschluss von Code-Parsern in diesem Abschnitt bezieht sich auf den durch dieses Manifest definierten Scope selbst — Atlas v0.1 legt ausschließlich Knoten-Basis, Kanten-Basis und Analyse-Fokus fest (Abschnitt 2), ohne Implementierung. Eine spätere Implementierung eines Compilers, der exakt diesen bereits freigegebenen Scope mechanisch abbildet, ist als separates, ausdrücklich freizugebendes Inkrement zulässig ("Atlas v0.1.1 / Compiler Pilot") und stellt keine rückwirkende Änderung dieses Manifests dar. Eine solche Implementierung darf den in Abschnitt 2 definierten Scope nicht erweitern — insbesondere keine der hier weiterhin ausgeschlossenen Punkte (Layer, Rich Edges, Metriken, Query Engine) einführen.

## 4. Nicht-Ziele

- Der Knowledge Atlas verändert keine bestehenden Wissensobjekte.
- Der Knowledge Atlas trifft keine Canonicalisierungs- oder Qualitätsurteile über den Inhalt der Knoten — er bildet ausschließlich die Verlinkungsstruktur ab.
- Ein "Reference Orphan" ist keine automatische Qualitätsaussage (z. B. "fehlerhaft" oder "zu entfernen"). Die Bewertung, ob ein Orphan-Befund handlungsrelevant ist, bleibt Herausgeberentscheidung.

## 5. Offene Punkte (nicht Teil von v0.1, zur späteren Klärung)

- Genauer Ausführungsmodus der Analyse (manuell durch Agenten-Durchsicht vs. Skript) — in v0.1 bewusst offen, da Abschnitt 3 jeden Code-Parser ausschließt.
- Ausgabeformat eines künftigen Orphan-Reports (Tabelle, separate Reportdatei, Ablageort) — wird erst mit dem ersten tatsächlichen Analyse-Auftrag festgelegt.
- Umgang mit Knoten, die nur einseitig referenzieren (z. B. Datei A referenziert B, B enthält aber keine Rückreferenz) — Definition in 2.3 behandelt dies bereits als "nicht Orphan" (ausgehende Referenz genügt), sollte aber bei der ersten Analyse explizit bestätigt werden.

## 6. Begründung der Ablageentscheidung

Freigegeben durch den Herausgeber am 2026-07-04. Ermittelte Top-Level-Belegung zum Zeitpunkt der Anlage:

`00_project`, `01_framework`, `02_sources`, `03_knowledge_base`, `04_book_analysis` + `04_synthesis` (dokumentierte Nummernkollision, siehe `00_project/REPOSITORY_CONSOLIDATION_REPORT_RC1.md`, Kapitel 12), `05_publications` + `05_research` (dieselbe Kollision), `06_media` + `06_research_program` (dieselbe Kollision), `07_scripts`, `99_archive`.

`08` war zum Zeitpunkt der Prüfung die einzige unbelegte einstellige Top-Level-Nummer. `08_knowledge_atlas/` wurde als eigenständiger Top-Level-Ordner gewählt (statt als Unterordner von `07_scripts/` oder `03_knowledge_base/`), da der Atlas ein eigenständiges Subsystem mit eigener Roadmap ist (vgl. Abschnitt 3) und nicht als reines Tooling oder als Teil der Wissensobjekt-Ablage selbst missverstanden werden soll. Keine bestehende Datei oder Ordnernummerierung wurde verändert.

---

*Dieses Manifest definiert ausschließlich v0.1. Jede Erweiterung des Scopes (Abschnitt 3) erfordert ein neues, separat freizugebendes Manifest bzw. eine explizite Versionsanhebung dieses Dokuments.*
