# Knowledge Atlas Content Analysis — Sprint 1

**Dokumentklasse:** Archived (einmaliger Sprint-Report nach Abschluss — nicht Teil des laufenden Operational-Sets)
**Rolle bei Erstellung:** Editor (Claude), read-only, diagnostisch — kein Forscher, kein Framework-Architekt, keine Herausgeberentscheidung
**Datum:** 2026-07-05
**Task-Type-Einordnung:** Kein exakter Treffer in `TASK_TYPES.md`. Am nächsten: **T6 — Audit** (repositoryweit, rein lesend, Auditbericht mit explizitem Methodikabschnitt), erweitert um eine explizite Graph-Metrik-Ebene, die T6 selbst nicht vorsieht und die auch über den in `08_knowledge_atlas/ATLAS_MANIFEST.md` Abschnitt 3 definierten Scope von Atlas v0.1.3 hinausgeht (dort ausdrücklich ausgeschlossen: Zentralitätsmetriken, Cluster-/Community-Erkennung). Diese Erweiterung ist durch den vorliegenden Herausgeberauftrag selbst explizit angefordert (Analysefragen 1–9) und wird hier als einmalige, ad-hoc-Diagnoseleistung außerhalb des versionierten Atlas-Compilers durchgeführt — **keine Änderung an `ATLAS_MANIFEST.md`, `compile_atlas.py` oder den offiziellen Atlas-Outputs.**
**Scope:** Ausschließlich lesend. Keine neuen Wissensobjekte, keine neue Forschung, keine inhaltlichen Änderungen an bestehenden Objekten, keine Framework-Änderungen, keine neuen Editor Decisions, keine geschlossenen Open Decisions, keine ergänzten Kanten, keine Cluster-Reorganisation.

---

## 1. Executive Summary

Der Sales Codex wurde erstmals nicht nur inhaltlich gelesen, sondern als Graph analysiert: 514 Wissensobjekte, 2071 explizite Referenzen, 18 Reference Orphans — Zahlen, die exakt der zuletzt bekannten Referenz entsprechen (keine Abweichung, siehe Abschnitt 2). Zusätzlich zur reinen Compiler-Baseline wurde für diesen Sprint eine ad-hoc-Metrikebene (Degree, Betweenness, PageRank, Konnektivitätskomponenten, Greedy-Modularity-Communities) über drei Graphansichten berechnet (Vollgraph, konzeptueller Graph ohne Statements, MEC-P-T-Fokusgraph), um Aussagen zu treffen, die durch reines Lesen einzelner Objekte nicht sichtbar würden.

Die wichtigsten Befunde in Kürze:

Der Codex hat einen klar identifizierbaren, robusten strukturellen Kern: MEC-0002 (Verlustaversion/Status-quo-Kosten) und MEC-0003 (Reaktanz) sind über alle drei Graphansichten und alle drei Zentralitätsmaße hinweg konsistent die beiden stärksten Mechanismus-Hubs — und beide sind evidenzstark (E4, breite Quellenbasis über 3–6 Bücher). Ihre strukturelle Zentralität ist damit keine reine Modellierungsartefakt, sondern spiegelt eine echte, mehrfach unabhängig bestätigte Synthesefunktion.

Gleichzeitig zeigt der Graph ein zentrales Risiko, das durch reines Lesen einzelner Objekte kaum auffällt, weil jedes einzelne Objekt für sich genommen bereits transparent dokumentiert ist: MEC-0018 (Pre-Suasion) ist strukturell der drittzentralste Mechanismus im Vollgraphen, verliert aber in den beiden konzeptuellen Graphansichten (ohne Statement-Volumen) mehrere Rangplätze — ein Hinweis, dass ein Teil seiner Vollgraph-Zentralität aus Zitierhäufigkeit, nicht aus konzeptueller Einbettung stammt — und stützt sich auf eine Quellenbasis (Cialdini Pre-Suasion, Ariely), die selbst einen dokumentierten, hochprioren Replikationskrisen-Befund trägt (`SCIENTIFIC_DEBT.md`, B-0010, Priorität Hoch). Struktur und Evidenzrisiko koexistieren hier real, nicht nur behauptet.

Auf der anderen Seite liegen mehrere evidenzstarke, aber strukturell kaum genutzte Mechanismen brach — am deutlichsten MEC-0020 (Perspektivübernahme-Asymmetrie durch Macht, Galinsky, E4, peer-reviewed) mit null Prinzip-Anbindungen im gesamten Codex, sowie MEC-0021 (Anchoring, E5 — eines der am besten replizierten Phänomene der Psychologie überhaupt), das trotz Spitzenevidenz nur unterdurchschnittlich in Prinzipien und Techniken verarbeitet ist.

Die Cluster-Analyse zeigt, dass der Codex neben einem großen, diffusen, gut vernetzten Kern (drei durch Greedy-Modularity getrennte, aber inhaltlich fließend ineinander übergehende Großcluster) auch mehrere kleine, dichte, thematisch homogene Satelliten-Cluster besitzt, die fast ausschließlich aus einem einzigen Buch/einer einzigen Quelle gespeist werden (Sludge/Choice-Architecture-Cluster aus SRC-0013, Zero-Preis-Cluster aus SRC-0012). Eine dieser Inseln ist vollständig vom Rest des Graphen getrennt: die vier Statements zum gescheiterten Ariely-Ehrlichkeitsexperiment (ST-0241–ST-0244) — und diese Isolation ist, wie der Abgleich mit `SCIENTIFIC_DEBT.md` (B-0012) zeigt, keine strukturelle Lücke, sondern das sichtbare graphische Echo einer bereits getroffenen redaktionellen Entscheidung, diese Befunde bewusst nicht zu P/MEC-Objekten zu erheben.

Alle 18 Reference Orphans wurden einzeln geprüft (Abschnitt 8). Kein einziger ist ein "vergessenes" Objekt im Sinne eines Fehlers — die Klassifikation reicht von legitimer Meta-/Kontextaussage (historische Einordnung, Forschungsmethodik) über bewusst verworfene Kandidaten (ST-0212, dokumentiert in `analysis.md`) bis zu zwei Fällen mit echtem, wenn auch niedrigprioritärem Synthesepotenzial (ST-0068/ST-0084, zwei unabhängig orphane Voss-Statements zu Verhandlungstempo/Deadlines, die keine Rückbindung an ein P/T-Objekt haben, obwohl sie inhaltlich handlungsrelevant sind).

**Antwort auf die Abschlussfrage:** Der Knowledge Atlas macht sichtbar, dass die editorisch bereits bekannte Vorsicht bei einzelnen Quellen (Ariely, CEB, Tethr) sich strukturell als beobachtbare Graph-Isolation oder als messbare Zentralitäts-/Evidenz-Diskrepanz niederschlägt — nicht nur als Fußnote im Fließtext. Das reine Lesen einzelner Objekte zeigt Vorsicht pro Objekt; der Graph zeigt, wie diese Vorsicht sich strukturell auf die gesamte Wissensbasis auswirkt (z. B. dass evidenzstarke Mechanismen wie MEC-0020/MEC-0021 trotz hoher Qualität strukturell brachliegen, während ein Mechanismus mit dokumentiertem Replikationsrisiko wie MEC-0018 strukturell überproportional zentral ist). Diese Kombination — hohe Struktur bei bekanntem Risiko, niedrige Struktur bei hoher Qualität — ist ohne graphbasierte Betrachtung nicht systematisch erkennbar.

**Empfohlene primäre nächste Hauptaktion** (siehe Abschnitt 13 für die vollständige Begründung): **Editorial Review Priority — MEC-0018 (Pre-Suasion) und seine drei abhängigen P-Objekte (P-0035, P-0036, P-0041) auf einen sichtbaren, im Objekt selbst plazierten Struktur-Risiko-Hinweis prüfen**, analog zum bereits für andere Objekte etablierten Muster "⚠ Hinweis: Publication Bias" — keine neue Recherche, keine E-Level-Änderung, nur eine editorische Sichtbarkeitsentscheidung, die dem Herausgeber vorzulegen ist.

---

## 2. Methodik und Grenzen

### 2.1 Datengrundlage

Grundlage sind ausschließlich die realen Exporte eines tatsächlich durchgeführten Compiler-Laufs (`08_knowledge_atlas/scripts/compile_atlas.py`, Version v0.1.3, ausgeführt am 2026-07-05 im Rahmen dieses Sprints): `nodes.csv` (514 Knoten), `edges.csv` (2071 gerichtete, deduplizierte Referenzen), `reference_orphans.csv` (18 Orphans). Der Compiler-Lauf erzeugte byte-identische Outputs zum bereits im Repository vorliegenden Stand (`git diff --stat -- 08_knowledge_atlas/` liefert keine Änderung) — die Baseline ist damit doppelt bestätigt: einmal durch den eigenen Lauf, einmal durch Übereinstimmung mit dem zuvor committeten Stand.

### 2.2 Baseline-Verifikation

| Kennzahl | Zuletzt bekannte Referenz | Realer Lauf (dieser Sprint, 2026-07-05) | Abweichung |
|---|---|---|---|
| Nodes | 514 | 514 | keine |
| Edges | 2071 | 2071 | keine |
| Reference Orphans | 18 | 18 | keine |
| Duplicate IDs | 0 | 0 | keine |
| Unaufgelöste Referenzen | — | 2 (Zielstring `T-0048`, genannt in P-S1-003 und ST-0307) | siehe unten |

Keine Abweichung von der Referenz-Baseline. Die zwei unaufgelösten Referenzen sind kein neuer Befund dieses Sprints, sondern bereits im Compiler-Report dokumentiert (`atlas_compiler_report.md`, Abschnitt 4) und wurden hier lediglich gegen ihren inhaltlichen Kontext geprüft: `T-0048` ist eine im Fließtext vorweggenommene, aber nie formal angelegte Technik ("Prospecting: Problem-zentrierter Outreach", vgl. P-S1-003 Zeile 41, sowie ST-0307 "Grundlage für T-0048 (falls als Technik formuliert)"). Dies ist ein dokumentierter, bewusster Zustand (Compiler-Triage-Punkt T-05, siehe `atlas_compiler_report.md`), kein neuer Fehlerbefund — wird in Abschnitt 11 als Research/Synthesis-Kandidat aufgeführt, nicht in diesem Sprint umgesetzt.

Node- und Edge-Typ-Verteilung (real, aus `nodes.csv`/`edges.csv`):

| Typ | Anzahl |
|---|---|
| ST | 309 |
| A | 60 |
| P | 57 |
| T | 47 |
| MEC | 29 |
| MOD | 12 |
| **Gesamt** | **514** |

Edge-Typ-Paare (ungerichtet gezählt, Top-Kategorien): MEC–ST (286), P–ST (219), A–ST (195), ST–ST (185), MEC–P (137), P–T (116), MEC–T (102), A–P (90), ST–T (85), P–P (79), MOD–P (75), MOD–ST (70), MEC–MEC (67), MEC–MOD (67), A–MEC (62), A–MOD (58), T–T (50), MOD–T (44), MOD–MOD (36), A–T (24), A–A (24).

### 2.3 Methodische Erweiterung gegenüber dem Atlas-Compiler

`ATLAS_MANIFEST.md` (Abschnitt 3) schließt Zentralitätsmetriken und Cluster-/Community-Erkennung für Atlas v0.1 explizit aus. Der vorliegende Sprintauftrag verlangt jedoch ausdrücklich Degree, Betweenness, PageRank-artige Maße und Cluster-Analyse (Analysefragen 1, 5). Diese Metriken wurden **außerhalb** des versionierten Compilers, ausschließlich für diesen Report, ad hoc berechnet — auf Basis der bereits exportierten `nodes.csv`/`edges.csv`, ohne den Compiler-Code oder das Manifest zu verändern. Da die Sandbox-Umgebung keinen Internetzugriff hat und `networkx` nicht installierbar war, wurden Degree, Konnektivitätskomponenten, Betweenness (Brandes-Algorithmus, ungewichtet) und PageRank (Power-Iteration, Damping 0,85) sowie eine Greedy-Modularity-Community-Erkennung (Clauset-Newman-Moore-artig) in reinem Python neu implementiert und gegen die exportierten Kantenlisten gerechnet. Dies ist eine Einmalauswertung für diesen Diagnose-Sprint, keine neue Atlas-Version — sollte eine spätere, dauerhafte Metrik-Ebene gewünscht sein, wäre dies gemäß Manifest Abschnitt 3 ein separat freizugebendes Atlas-Release (z. B. "v0.2"), nicht Gegenstand dieses Sprints.

### 2.4 Drei Graphansichten

Wie im Auftrag gefordert, wurden mindestens drei Ansichten berechnet, um Metrik-Artefakte einer einzelnen Sichtweise zu erkennen:

- **Full Knowledge Graph:** alle 514 Knoten, 2071 Kanten.
- **Conceptual Graph (ohne ST):** nur A, MEC, P, T, MOD — 205 Knoten, 1031 gerichtete Kanten, **ein einziges Konnektivitäts-Cluster** (keine Isolate) — das bestätigt, dass alle 18 Orphans reine ST-Objekte sind (siehe Abschnitt 8) und die konzeptuelle Objektebene selbst vollständig verbunden ist.
- **MEC-P-T-Fokusgraph:** nur MEC, P, T — 133 Knoten, 551 gerichtete Kanten, überwiegend eine Komponente (130 Knoten) plus eine isolierte Zweiergruppe (T-0038/P-0039) und ein Einzelknoten (P-0040, siehe Abschnitt 4/10).

### 2.5 Bias Checks (vor der Interpretation durchgeführt)

- **Centrality Bias durch Objekttypen:** Der mittlere Undirected-Degree unterscheidet sich massiv nach Typ (MOD ø 28,0; MEC ø 22,6; P ø 11,9; T ø 8,5; A ø 7,0; ST ø 3,5). Das ist strukturell erwartbar (MOD/MEC sitzen pipeline-bedingt oben, ST unten — Statements werden zitiert, sie zitieren selten selbst), keine Qualitätsaussage. Jeder Zentralitätsvergleich in diesem Report erfolgt **innerhalb** eines Objekttyps (MEC gegen MEC, P gegen P), nie typübergreifend.
- **Statement Volume Bias:** Da ST 60% aller Knoten stellt und an über der Hälfte aller Kanten beteiligt ist (MEC–ST, P–ST, A–ST, ST–ST zusammen 885 von 2071 Kanten-Nennungen), wird ein Objekt allein durch viele Beleg-Zitate strukturell "zentraler", ohne konzeptuell stärker vernetzt zu sein. Deshalb wurde der konzeptuelle Graph ohne ST als Gegenprobe berechnet (Abschnitt 3 zeigt konkret, wo sich Rangplätze dadurch verschieben — v. a. MEC-0018).
- **Edge-Type Bias:** Der Compiler kennt keine Kantentypisierung (Manifest Abschnitt 2.2) — eine "unterstützt"-Kante zählt strukturell gleich wie eine "widerspricht"-Kante oder eine reine Zitat-Kante. Betweenness/PageRank können daher Objekte aufwerten, die viel zitiert werden, ohne dass die Zitat-Richtung (Zustimmung, Kritik, Abgrenzung) geprüft wurde. Dies wird qualitativ durch Abgleich mit `SCIENTIFIC_DEBT.md` korrigiert, nicht durch den Graphen selbst.
- **Source Concentration:** Für MEC und MOD wurde die Anzahl distinkter zitierter `SRC-XXXX` je Objekt gezählt (Abschnitte 3, 6). Bei MOD-0002 zeigt sich, dass zwei von drei zitierten Quellen (SRC-0002, SRC-0008) vom selben Autor (Cialdini) stammen — scheinbare Quellenvielfalt ohne echte Autoren-/Methodenvielfalt.
- **Unterschiede der Evidenzfelder zwischen Objekttypen:** MEC/MOD/T nutzen "Evidenzlevel", P nutzt "Evidenzklassifikation", A nutzt "Evidenzstatus", ST nutzt "Evidenzklasse" (harmonisiert im Final Pre-Release Sprint, siehe `CURRENT_STATE.md`). Für dieses Sprint wurden die jeweils typspezifischen Feldnamen verwendet, keine Vereinheitlichung vorgenommen.
- **Echte Isolation versus fehlende Graphrelation:** Bei jedem Orphan- und Cluster-Befund wurde geprüft, ob das Objekt selbst inhaltlich Querverweise nennt, die der Compiler nicht als ID-Referenz erkennt (z. B. ST-0171 nennt im Fließtext einen "Cross-Book-Bezug" zu Gap Selling und JOLT, ist aber laut Graph ein Orphan — die inhaltliche Verbindung existiert, nur nicht als deklarierte Objekt-ID).

Zusätzlich zu den Standardansichten wurde die Kanten-Zusammensetzung einzelner Top-Hubs nach Nachbartyp aufgeschlüsselt (siehe Abschnitt 3), um Degree nicht pauschal als ein einziges Signal zu behandeln.

### 2.6 Grenzen dieser Analyse

Diese Analyse ist ausschließlich strukturell (Graph) und dokumentarisch (Abgleich mit `SCIENTIFIC_DEBT.md`, Evidenzfeldern der Objekte). Sie ersetzt keine inhaltliche Forschung, keine neue externe Validierung und keine Herausgeberentscheidung. Community Detection wurde als Analyseinstrument eingesetzt, nicht als endgültige Taxonomie (Cluster-Grenzen sind ein Ergebnis eines Optimierungsalgorithmus, nicht redaktionell kuratiert). Nicht jedes der 514 Objekte wurde einzeln inhaltlich neu gelesen — Stichproben wurden dort vertieft, wo der Graph einen auffälligen Befund lieferte (hohe Zentralität, Isolation, geringe Anbindung trotz hoher Evidenz).

---

## 3. Mechanism Hub Analysis

### 3.1 Robuste Hubs (konsistent über alle drei Ansichten und alle drei Metriken)

| MEC | Full-Graph (Degree / Betweenness / PageRank-Rang) | Conceptual (ohne ST) Rang | MEC-P-T-Fokus Rang | Evidenzlevel | Quellenvielfalt (SRC) |
|---|---|---|---|---|---|
| MEC-0002 — Verlustaversion/Status-quo-Kosten | 1 / 1 / 1 | 1 | 1 | E4 (allgemeiner Mechanismus, gut repliziert) | 6 (SRC-0001,-0003,-0004,-0005,-0010,-0013) |
| MEC-0003 — Reaktanz durch Kontrollverlust | 2 / 2 / 4 | 2 | 2 | "Vorläufig E4" | 3 (SRC-0001,-0002,-0003) |

MEC-0002 und MEC-0003 sind über alle neun Kombinationen (3 Ansichten × 3 Metriken, soweit anwendbar) hinweg an Rang 1/2 — das ist keine Metrik-spezifische Zufälligkeit, sondern ein robuster Befund. Beide sind zusätzlich evidenzstark und ziehen ihre Zentralität aus mehreren unabhängigen Büchern (MEC-0002 aus sechs, MEC-0003 aus dreien). Dies bestätigt die bereits in `04_synthesis/SPR-0001_Sales_Core_Synthesis/synthesis.md` getroffene Einschätzung ("MEC-0002 ist das Gravitationszentrum des Sales Codex") jetzt mit echter Graphmetrik statt nur qualitativer Beobachtung — und zeigt zusätzlich, dass diese Zentralität auch nach Herausrechnen der reinen ST-Zitierhäufigkeit bestehen bleibt (Conceptual-Graph-Rang unverändert 1/2).

### 3.2 Struktureller Hub mit Evidenzrisiko — der zentrale Einzelbefund dieses Sprints

**MEC-0018 (Pre-Suasion: Attentionale Vorbereitung vor der Botschaft):** Rang 3 im Vollgraphen nach Degree/Betweenness/PageRank (37 Grad, Betweenness 7571, PageRank 0,014), fällt aber in beiden konzeptuellen Ansichten (ohne ST) auf Rang 6 zurück. Das bedeutet: Ein spürbarer Teil seiner Vollgraph-Zentralität stammt aus Statement-Zitierhäufigkeit (16 von 37 direkten Nachbarn sind ST-Objekte), nicht aus konzeptueller MEC/P/T/MOD-Vernetzung.

Gleichzeitig ist MEC-0018 laut `SCIENTIFIC_DEBT.md` (B-0010, Priorität **Hoch**) mit einem dokumentierten Replikationsrisiko behaftet: Ein Teil der zugrundeliegenden Priming-Forschung (Bargh/Dijksterhuis-Stil, wie von Kahneman in *Thinking, Fast and Slow* referenziert) gilt als in der Replikationskrise nicht bestätigt — Kahneman selbst erkannte dies 2012 öffentlich an. Das Objekt selbst dokumentiert dies bereits transparent und differenziert (Evidenzlevel-Abschnitt: E4 nur für die basale Spreading-Activation, E2 für die sozial-/verhaltensbezogene Priming-Ebene, Gesamteinstufung E2–E3 für die Sales-Anwendung). Die Quellenbasis ist zudem mit nur zwei zitierten Büchern (SRC-0008 Pre-Suasion, SRC-0012 Predictably Irrational) schmaler als bei MEC-0002/MEC-0003.

**Das ist keine neue Kritik an MEC-0018 selbst — das Objekt ist bereits korrekt und differenziert dokumentiert (Korrektur vom Final Pre-Release Sprint, 2026-07-03).** Der neue Befund dieses Sprints ist ausschließlich strukturell: MEC-0018 trägt in drei nachgelagerten Prinzipien (siehe unten) eine strukturelle Zentralität, die höher ist, als seine eigene, bereits als vorsichtig eingestufte Evidenzlage vermuten lässt — und diese Diskrepanz war vor dieser Graphanalyse nicht als Gesamtbild sichtbar, weil sie sich erst aus dem Vergleich von Zentralitätsrang und Evidenzlevel ergibt, nicht aus dem Lesen des Objekts allein.

Direkt von MEC-0018 abhängige Prinzipien (P-Nachbarn im Graph): P-0035 (Rahmen zuerst), P-0036 (Aufmerksamkeit strategisch lenken), P-0041 (System-1-kompatible Darstellung) — alle drei erben die Evidenzunsicherheit strukturell, ohne dass dies in den P-Objekten selbst notwendigerweise ebenso differenziert sichtbar gemacht ist wie im MEC-Objekt (nicht im Rahmen dieses Sprints inhaltlich geprüft — Empfehlung siehe Abschnitt 11/13).

### 3.3 Evidenzstarke, aber strukturell unauffällige Mechanismen (Vorgriff auf Abschnitt 10)

MEC-0020 (Galinsky-Machtperspektive, E4) und MEC-0021 (Anchoring, E5 — höchste Evidenzklasse) liegen beide weit unten in der Zentralitäts-Rangliste (MEC-0020: Gesamtgrad 12, letzter Platz unter allen 29 MEC nach P-Anbindung; MEC-0021: Gesamtgrad 28, aber nur 4 P- und 2 T-Verbindungen trotz Spitzenevidenz). Vollständige Einordnung in Abschnitt 10.

### 3.4 Vollständige MEC-Übersicht (Degree, sortiert, Vollgraph)

| MEC | Grad gesamt | Betweenness | PageRank | Evidenzlevel (Kurzfassung) |
|---|---|---|---|---|
| MEC-0002 | 83 | 25776,3 | 0,0336 | E4 |
| MEC-0003 | 56 | 16141,5 | 0,0157 | Vorläufig E4 |
| MEC-0018 | 37 | 7571,2 | 0,0140 | E2–E3 (differenziert, s.o.) |
| MEC-0007 | 33 | 9192,1 | 0,0087 | E4 |
| MEC-0012 | 31 | 10229,8 | 0,0072 | E4 |
| MEC-0001 | 31 | 3446,6 | 0,0223 | Vorläufig E4 |
| MEC-0009 | 29 | 2559,4 | 0,0098 | E4 |
| MEC-0004 | 29 | 2336,1 | 0,0158 | Vorläufig E4 |
| MEC-0021 | 28 | 4945,5 | 0,0097 | **E5** |
| MEC-0013 | 28 | 4453,7 | 0,0068 | E3 |
| MEC-0008 | 27 | 4385,6 | 0,0088 | E4 |
| MEC-0010 | 25 | 4682,3 | 0,0068 | E2 (herabgestuft) |
| MEC-0015 | 21 | 2536,0 | 0,0038 | E5 |
| MEC-0005 | 21 | 1999,0 | 0,0096 | E4 |
| MEC-0016 | 19 | 2820,9 | 0,0033 | E4 |
| MEC-0006 | 17 | 2093,1 | 0,0052 | E4 |
| MEC-0025 | 14 | 1400,1 | 0,0022 | E4 (Kernphänomen), E3 (neuronale Fundierung) |
| MEC-0011 | 14 | 1907,5 | 0,0029 | E2 (herabgestuft) |
| MEC-0029 | 13 | 2727,2 | 0,0029 | E3 |
| MEC-0028 | 13 | 2635,0 | 0,0054 | E4 (Basiseffekt) / E2–E3 (Anwendungsfall) |
| MEC-0020 | 12 | 1534,9 | 0,0030 | E4 |
| MEC-0026 | 11 | 1857,2 | 0,0024 | E3 |
| MEC-0022 | 11 | 226,98 | 0,0027 | E3 |
| MEC-0017 | 11 | 721,58 | 0,0020 | E4/E3 |
| MEC-0027 | 10 | 656,58 | 0,0022 | E3 |
| MEC-0024 | 8 | 583,67 | 0,0048 | E2 |
| MEC-0023 | 8 | 1128,1 | 0,0020 | E3 |
| MEC-0014 | 8 | 889,14 | 0,0015 | E3 |
| MEC-0019 | 7 | 276,42 | 0,0015 | E4 |

---

## 4. Principle Dependency Analysis

Von 57 Prinzipien (inkl. 4 Meta-Prinzipien P-S1-001–004) haben:

| # MEC-Verbindungen | Anzahl P |
|---|---|
| 0 | 8 |
| 1 | 14 |
| 2 | 19 |
| 3 | 8 |
| 4 | 5 |
| 5 | 3 |

Kein Prinzip hat gleichzeitig ≥5 Technik-Anbindungen UND ≤1 Mechanismus-Anbindung — die im Auftrag befürchtete Konstellation ("P mit vielen nachgelagerten Techniken trotz schmaler mechanistischer Basis") kommt im aktuellen Bestand **nicht vor**. Das ist ein sauberer Negativbefund.

### 4.1 Prinzipien mit 0 MEC-Verbindungen (8)

| P | Titel | T-Links | Einordnung |
|---|---|---|---|
| P-0019 | Commitment-Verifikation als eigenständige Verhandlungsphase | 2 | Voss-Praktikerprinzip (Verhandlungsphase); stützt sich im Objekt vermutlich auf MEC-0001/MEC-0010 über den Praxistext, aber keine explizite ID-Referenz — mögliche Graphmodellierungslücke, keine erkennbare inhaltliche Leere |
| P-0020 | Black-Swan-Orientierung: Verhandlung als Entdeckungsprozess | 3 | Voss-Kernkonzept, epistemisch-methodisch formuliert (Haltung, nicht Mechanismus) — legitime Spezialisierung, kein MEC in der aktuellen Taxonomie modelliert diese Haltung direkt |
| P-0022 | TTC-Dreiklang: Teach, Tailor, Take Control als notwendige Kombination | 3 | Challenger-Meta-Prinzip, das mehrere MECs (MEC-0013 u. a.) kombiniert, aber als Kombinationsaussage selbst nicht an ein einzelnes MEC gebunden — legitime Synthesefunktion auf P-Ebene |
| P-0024 | Vertriebstransformation als organisationale Systemfähigkeit | 0 | Organisations-/Change-Management-Ebene, nicht individualpsychologisch — liegt bewusst außerhalb der MEC-Taxonomie (die primär kognitiv/sozialpsychologisch modelliert) |
| P-0033 | BATNA kennen und entwickeln: Einzige legitime Machtbasis in Verhandlungen | 2 | Harvard-Verhandlungsprinzip, strukturell-strategisch statt mechanistisch-psychologisch — legitime Spezialisierung |
| P-0039 | Buoyancy: Erklärungsstil bestimmt Resilienz im Selling | 1 | **E4-Evidenz (Seligman/MetLife), aber 0 MEC- und nur 1 T-Verbindung** — siehe Abschnitt 10, Underused-Strength-Kandidat |
| P-0040 | Purposeful Serving: Prosozialer Rahmen als Leistungsverstärker | 0 | **E4-Evidenz (Grant-Studien), 0 MEC- und 0 T-Verbindungen** — im MEC-P-T-Fokusgraph vollständig isoliert (Abschnitt 10) |
| P-S1-003 | Problem-Zentrierung als universelles Differenzierungsprinzip | 4 | Sprint-1-Meta-Prinzip (Synthese über mehrere Bücher hinweg formuliert); referenziert im Vollgraph 13 andere Objekte, wird selbst aber von keinem referenziert (In-Degree 0) — klassisches "Sink"-Muster eines nachträglich synthetisierten Meta-Objekts, keine strukturelle Schwäche im Sinne einer Wissenslücke |

### 4.2 Prinzipien mit genau 1 MEC-Verbindung (14)

P-0005, P-0009, P-0011, P-0012, P-0013, P-0015, P-0029, P-0031, P-0034, P-0035, P-0043, P-0046, P-0047, P-0050 — durchgängig Prinzipien, die aus genau einem Buch/einer Buch-Linie stammen und einen einzelnen, spezifischen Mechanismus direkt operationalisieren (z. B. P-0015 Knappheit/Zeitdruck ↔ MEC-0003 Reaktanz; P-0046 Kostenlos ↔ MEC-0023 Zero-Preis-Effekt). Dies ist überwiegend **legitime Spezialisierung** (ein Prinzip pro Mechanismus ist laut `canonical_knowledge_model.md`-Logik zulässig, solange das Prinzip selbst aus ≥2 Quellen abstrahiert — was hier nicht separat geprüft wurde und für eine künftige T7-Konsistenzprüfung empfohlen wird, siehe Abschnitt 11). P-0035 gehört zur MEC-0018-Abhängigkeitskette (Abschnitt 3.2) und ist damit der einzige Fall in dieser Gruppe mit einem zusätzlichen Evidenzrisiko-Bezug.

---

## 5. Technique Integration Analysis

Von 47 Techniken haben nur 2 keine P-Verbindung — beide bleiben aber über MEC und/oder MOD angebunden, sodass **keine Technik im gesamten Codex vollständig unangebunden** ist (0 P UND 0 MEC gleichzeitig kommt nicht vor).

| T | Titel | P-Links | MEC-Links | MOD-Links | Evidenzlevel | Einordnung |
|---|---|---|---|---|---|---|
| T-0036 | Commitment-Lock: Verhaltenshandlung nach Pre-Suasion-Opener sichern | 0 | 2 | 1 | E4 (Konsistenzforschung, peer-reviewed) | Legitime Graphmodellierungslücke — evidenzstark, über MEC/MOD ausreichend eingebettet, fehlende P-Kante ist wahrscheinlich ein Modellierungsartefakt, kein Qualitätsproblem |
| T-0039 | Yes-And-Technik: Einwände als Angebote behandeln | 0 | 1 | 1 | E2 (Practitioner-Evidenz, Improv-Praxis; Verbindung zur Reaktanzforschung nicht direkt gemessen) | **Praktische Technik mit schwacher Fundierung UND schwacher Integration** — deckt sich mit `SCIENTIFIC_DEBT.md` B-0009 (Improv-Transfer, "kein RCT", Priorität Niedrig). Beide Schwächen (Evidenz, Integration) treten hier gemeinsam auf — der einzige Fall im gesamten T-Bestand mit dieser Kombination |

Verteilung P-Verbindungen über alle 47 T: 0×2, 1×19, 2×13, 3×6, 4×4, 5×2, 6×1 — die Mehrheit (19 von 47) hat genau eine P-Anbindung, was für ein Technik-Prinzip-Verhältnis in einem praxisorientierten Codex plausibel und nicht auffällig ist.

---

## 6. Cross-Domain Model Analysis

Alle 12 Modelle wurden auf Quellenvielfalt (distinkte `SRC-XXXX`-Zitate im Objekt) und In-/Out-Degree-Asymmetrie geprüft:

| MOD | Titel | Zitierte SRC | Echte Autoren-/Buchvielfalt | In-Grad | Out-Grad | Einordnung |
|---|---|---|---|---|---|---|
| MOD-0012 | SUCCESS-Framework (Made to Stick) | 6 (SRC-0008,-0011,-0012,-0013,-0014,-0015) | Ja — 6 verschiedene Autoren/Werke | 3 | 21 | **Einzig genuin breite Cross-Domain-Synthese** im Codex-Bestand |
| MOD-0010 | Kahnemans Bias-Landkarte | 3 (SRC-0010,-0012,-0014) | Ja — 3 verschiedene Autoren (Kahneman, Ariely, Poundstone) | 5 | 38 | Breite Quellenbasis, aber starke In-/Out-Asymmetrie (s.u.) |
| MOD-0002 | Cialdinis 6-Prinzipien-Modell | 3 (SRC-0001,-0002,-0008) | **Nein — 2 von 3 Quellen (SRC-0002, SRC-0008) sind vom selben Autor (Cialdini)** | 25 | 36 | Scheinbare Breite; echte externe Diversität nur SRC-0001 |
| MOD-0001 | SPIN Selling | 1 (SRC-0001) | — (Einzelquelle) | 19 | 21 | Legitimes Einzelbuch-Modell |
| MOD-0003 | BCSM + Voss | 1 (SRC-0003) | — | 7 | 26 | Legitimes Einzelbuch-Modell |
| MOD-0004 | Challenger TTC | 1 (SRC-0004) | — | 8 | 28 | Legitimes Einzelbuch-Modell |
| MOD-0005 | Gap Selling Modell | 1 (SRC-0005) | — | 1 | 38 | Legitimes Einzelbuch-Modell, aber extreme Senke (s.u.) |
| MOD-0006 | JOLT-Modell | 1 (SRC-0006) | — | 2 | 16 | Legitimes Einzelbuch-Modell |
| MOD-0007 | Principled Negotiation | 1 (SRC-0007) | — | 2 | 15 | Legitimes Einzelbuch-Modell |
| MOD-0008 | Pre-Suasion-Modell | 1 (SRC-0008) | — | 5 | 10 | Legitimes Einzelbuch-Modell, teilt Evidenzrisiko mit MEC-0018 |
| MOD-0009 | Pinks ABCs of Selling | 1 (SRC-0009) | — | 18 | 15 | Legitimes Einzelbuch-Modell, gut bidirektional eingebunden |
| MOD-0011 | Choice Architecture | 1 (SRC-0013) | — | 10 | 17 | Legitimes Einzelbuch-Modell |

**Zentraler Befund:** Nur 2 von 12 Modellen (MOD-0010, MOD-0012) sind durch echte Autoren-/Werkvielfalt cross-domain im engeren Sinne; MOD-0002 hat drei Quellenzitate, aber nur einen davon außerhalb der eigenen Autorenfamilie — die scheinbare Breite ist zu zwei Dritteln eine Ein-Autoren-Perspektive (Cialdini selbst zitiert und interpretiert sich in Pre-Suasion teils selbst). Dies ist keine Qualitätskritik an MOD-0002 (Cialdinis Modell ist strukturell und evidenzseitig eines der stärksten im Codex), sondern eine Präzisierung: "Cross-Domain" sollte im Codex zwischen **struktureller** Brückenfunktion (viele verschiedene MEC/P/T verbindend — das leistet MOD-0002 sehr wohl) und **quellenseitiger** Breite (mehrere unabhängige Autoren) unterschieden werden.

**In-/Out-Asymmetrie ("Senken"):** MOD-0005 (Gap Selling) hat Out-Grad 38 gegen In-Grad 1 — das Modell zitiert/verweist auf sehr viele andere Objekte, wird aber selbst kaum referenziert. Dieselbe Asymmetrie, etwas schwächer, bei MOD-0010 (In 5 / Out 38). Dies deckt sich mit der bereits dokumentierten Quellenunvollständigkeit von B-0005 (`SCIENTIFIC_DEBT.md`, SD-SYS-002, Priorität Hoch: Gap Selling wurde aus einer Teilfassung des Buches analysiert) — ein Modell, das viel zitiert, aber wenig zitiert wird, ist strukturell ein Kandidat für "noch nicht in den Rest des Codex zurücksynthetisiert", nicht zwangsläufig ein Qualitätsmangel.

---

## 7. Cluster Analysis

Greedy-Modularity-Clustering (496 Knoten mit Grad > 0, 1780 eindeutige ungerichtete Kanten) ergab **11 Communities**, finale Modularität Q ≈ 0,591 (Q > 0,3 gilt gemeinhin als Hinweis auf echte Clusterstruktur, nicht Zufallsrauschen).

| Community | Größe | Interne Dichte | Externe Kanten | Charakter |
|---|---|---|---|---|
| 0 | 130 | 0,048 | 123 | Großer, diffuser Kernbereich, alle Typen gemischt |
| 1 | 120 | 0,060 | 189 | Großer, diffuser Kernbereich, alle Typen gemischt |
| 2 | 104 | 0,057 | 165 | Großer, diffuser Kernbereich, alle Typen gemischt |
| 3 | 35 | 0,141 | 47 | Pre-Suasion (Cialdini) + Curiosity-Gap (Made to Stick) — thematische Brücke Aufmerksamkeitssteuerung |
| 4 | 32 | 0,151 | 49 | Made-to-Stick-SUCCESS-Cluster (Curse of Knowledge, Concreteness, Narrative Transportation) + Autorität (Cialdini) |
| 5 | 28 | 0,146 | 48 | JOLT/Indecision-Cluster (weitgehend SRC-0006-homogen) |
| 6 | 22 | 0,152 | 30 | **Sludge/Choice-Architecture-Cluster — nahezu vollständig aus SRC-0013 (Nudge) gespeist** |
| 7 | 12 | 0,348 | 40 | Unity/We-Identity (Cialdini) verbunden mit Challenger-Profil-Statements — echte thematische Brücke "Beziehung vs. Credibility" zwischen zwei Büchern |
| 8 | 6 | 0,867 | 6 | **Zero-Preis-Effekt — fast vollständig aus SRC-0012 (Ariely) gespeist, sehr dicht, kaum externe Anbindung** |
| 9 | 4 | 0,500 | **0** | **Vollständig isoliert:** ST-0241–ST-0244, das gescheiterte Ariely-Ehrlichkeitsexperiment (siehe Abschnitt 8/9) |
| 10 | 3 | — | — | Door-Game/Optionsverlust-Angst (Ariely), ebenfalls SRC-0012-homogen, kaum externe Anbindung |

**Drei Großcluster (0/1/2) vs. kleine Satelliten (3–10):** Die drei großen Communities zusammen enthalten 354 der 496 verbundenen Knoten (71%), sind aber mit einer internen Dichte von 0,05–0,06 sehr locker vernetzt — die Modularitäts-Optimierung trennt hier eher graduelle Übergänge in einem großen, gut integrierten Kern als drei inhaltlich trennscharfe "Silos". Die kleinen Cluster (Größe 4–35) sind dagegen deutlich dichter (0,14–0,87) und lassen sich fast durchgängig einer einzigen Quelle oder einem engen Themenfeld zuordnen.

**Buch-/quellendominierte Cluster:** Community 6 (Sludge/Choice Architecture, SRC-0013), Community 8 (Zero-Preis, SRC-0012) und Community 10 (Door Game, SRC-0012) sind strukturell dichte, aber quellenkonzentrierte Satelliten — wissenschaftlich nicht per se schwach (Choice-Architecture-Grundeffekte sind gut belegt, siehe MOD-0011), aber mit geringer externer Anbindung ("starke, aber tendenziell isolierte Wissensbereiche" im Sinne der Auftragsfrage). Community 9 ist der einzige Fall vollständiger Isolation (0 externe Kanten) — siehe Abschnitt 8/9 für die Einordnung als bewusste redaktionelle Entscheidung, nicht als Fehler.

**Synthesechance:** Community 7 (Unity/Credibility-Brücke zwischen Cialdini und Challenger Sale) zeigt, dass der Codex bereits mindestens eine echte, graphisch sichtbare Cross-Book-Synthese zwischen zwei sehr unterschiedlichen Denkschulen (Compliance-Psychologie vs. B2B-Vertriebsforschung) leistet — ein Muster, das sich möglicherweise auch für andere, bisher nicht verbundene Satelliten (z. B. Community 5, JOLT) lohnen könnte, ohne dass dies hier bereits inhaltlich geprüft wurde.

---

## 8. Vollständige Orphan Analysis

Alle 18 Reference Orphans (ausnahmslos ST-Objekte) wurden einzeln gegen ihren vollständigen Objektinhalt und gegen `SCIENTIFIC_DEBT.md` geprüft.

| ST | Titel (gekürzt) | Buch | Klassifikation | Begründung |
|---|---|---|---|---|
| ST-0023 | SPIN-Kompetenz: gezieltes Üben | SRC-0001 | Unkritisch | Trainings-/Kompetenzaufbau-Empfehlung, keine inhaltliche Mechanismus-Aussage — legitime Meta-Ebene |
| ST-0025 | Forschungsmethodik Cialdini (3-Jahres-Feldstudie) | SRC-0002 | Unkritisch | Reine Quellenkontext-/Methodikangabe, keine Sachaussage, die verlinkt werden müsste |
| ST-0068 | Verlangsamen als Verhandlungsinstrument | SRC-0003 | **Möglicher Missing Link** | Substanzielle, handlungsrelevante Aussage (Tempo als Verhandlungshebel), aber an kein P/T gebunden — potenzielle Anbindung an P-0033 (BATNA/Machtbasis) oder ein eigenes Tempo-Prinzip wäre inhaltlich denkbar, hier nicht geprüft |
| ST-0084 | Deadlines sind meist flexibel (+ Don-Moore-Forschung) | SRC-0003 | **Möglicher Missing Link** | Substanzielle Aussage mit doppelter Quellenbasis (Voss + Moore-Forschung), keine P/T-Anbindung trotz Praxisrelevanz für Verhandlungstaktik |
| ST-0107 | Vier Durchbrüche in der Vertriebsgeschichte | SRC-0004 | Unkritisch | Historisch-narrative Einordnung (Rackham-Vorwort), keine eigenständige Mechanismus-/Prinzipaussage |
| ST-0108 | Fünf Profile statistisch abgeleitet | SRC-0004 | Unkritisch | Methodologische Validierung der CEB-Faktoranalyse — Kontext für A-0019, nicht selbst mechanistisch |
| ST-0110 | Ausgangslage Krisenverkäuferstudie 2009 | SRC-0004 | Unkritisch | Reine narrative Rahmensetzung für die CEB-Studie |
| ST-0112 | Solution Selling dominiert B2B | SRC-0004 | Unkritisch | Marktkontext-Aussage, Hintergrundrahmen für das Buch, kein Mechanismus |
| ST-0114 | Performance-Gap 4× größer in Solution Selling | SRC-0004 | Redaktionell interessant | Quantitativer Befund mit Implikationscharakter (Key-Person-Abhängigkeit steigt mit Komplexität) — evtl. relevant für eine künftige Diskussion der TTC-Modell-Grenzen (MOD-0004), hier nicht weiterverfolgt |
| ST-0115 | Fünf Profile: Definitionen | SRC-0004 | Unkritisch | Definitorische Auflistung, deren Einzelinhalte bereits über andere, verlinkte Statements (z. B. ST-0109, ST-0117) im Graph vertreten sind |
| ST-0152 | Drei Quellen der Kundenunentschlossenheit | SRC-0006 | **Möglicher Missing Link** | Zentrale Taxonomie für die J-Komponente von JOLT — erwartbar wäre eine explizite Rückbindung an P-0027 (Entscheidungsfähigkeits-Qualifikation); nicht vorhanden |
| ST-0153 | JOLT-Akronym (Judge/Offer/Limit/Take Risk Off) | SRC-0006 | Unkritisch | Definitorischer Überblick, dessen vier Elemente einzeln über P/T-Objekte abgedeckt sind |
| ST-0171 | Optionen erfinden vor Entscheiden (Brainstorming) | SRC-0007 | **Möglicher Missing Link** | Das Objekt selbst dokumentiert einen "Cross-Book-Bezug" zu Gap Selling (B-0005) und JOLT (B-0006) im Fließtext — die inhaltliche Verbindung ist bekannt und benannt, aber nicht als deklarierte Objekt-ID-Referenz erfasst. Bestes Beispiel im gesamten Orphan-Set für "fehlende Graphrelation trotz dokumentierter inhaltlicher Verbindung" |
| ST-0212 | Group IQ: soziale Harmonie (Sternberg/Williams, Bell Labs) | SRC-0011 | **Legitimer, bewusst dokumentierter Spezialfall** | Das Objekt selbst dokumentiert explizit: als P-Kandidat geprüft und verworfen (Team-/Organisationskontext statt Käufer-Verkäufer-Dyade), siehe `analysis.md`, Abschnitt "Verworfene Kandidaten" — ein Musterbeispiel für einen redaktionell bereits korrekt verarbeiteten Orphan |
| ST-0218 | Behavioral-Economics-Definition (Ariely) | SRC-0012 | Unkritisch | Buchdefinierende Einleitungsaussage, Rahmenkonzept für das gesamte Kapitel, keine Einzelmechanismus-Aussage |
| ST-0227 | Hot-Cold-Empathy-Gap (Berkeley-Arousal-Experiment) | SRC-0012 | Wissenschaftlich interessant, aber bewusst niedrigprior | Bereits in `SCIENTIFIC_DEBT.md` (B-0012) dokumentiert: WEIRD-Bias, N=25, nur männliche Probanden. Objekt selbst markiert "geringere direkte Kaufpsychologie-Relevanz ... Codex-eigene Extrapolation" — Isolation ist konsistent mit der im Objekt selbst konstatierten Randlage |
| ST-0228 | Deadline-Experiment (Prokrastination/Selbstkontrolle) | SRC-0012 | **Synthesechance** | Substanzieller Befund (diktierte > selbstgewählte > keine Deadlines) mit klarer Vertriebsprozess-Relevanz (gestaffelte Meilensteine); zusammen mit dem ebenfalls orphanen ST-0084 (Voss, Deadlines) ergäbe sich ein buchübergreifendes Deadline-Thema, das aktuell an keiner Stelle des Graphen explizit zusammengeführt ist |
| ST-0245 | Bierbestell-Sequenz (Uniqueness/Konformität, USA/Hongkong) | SRC-0012 | Wissenschaftlich interessant, bewusst niedrigprior | In `SCIENTIFIC_DEBT.md` (B-0012, "Durchgängig") bereits als einziges interkulturell repliziertes Experiment des Buches gewürdigt; Inhalt (Konsumentenkonformität) liegt konzeptuell am Rand des B2B-Vertriebsfokus, Isolation ist plausibel |

**Zusammenfassung:** 8 unkritisch (reine Kontext-/Definitions-/Methodikaussagen), 1 legitimer, bereits dokumentierter Spezialfall (ST-0212), 2 wissenschaftlich interessant, aber bewusst niedrigpriorisiert (ST-0227, ST-0245), 1 redaktionell interessant (ST-0114), 4 mögliche Missing Links (ST-0068, ST-0084, ST-0152, ST-0171) und 1 explizite Synthesechance mit Bezug zu einem zweiten Orphan (ST-0228, in Kombination mit ST-0084). Kein einziger Orphan wurde als "struktureller Qualitätsfehler" eingestuft — der Reference-Orphan-Status korreliert im gesamten Bestand mit keinem einzigen Fall von Datenverlust oder übersehenem Inhalt, sondern durchgängig mit Meta-Ebene, bewusster redaktioneller Entscheidung oder — in vier Fällen — einer plausiblen, aber nicht umgesetzten Verlinkungsmöglichkeit.

---

## 9. Structure × Evidence Risk Analysis

| Struktur | Evidenz | Interpretation | Konkrete Beispiele |
|---|---|---|---|
| Hoch | Hoch | Robuster Kern | MEC-0002 (E4, 6 Quellen, Rang 1 in allen 3 Ansichten), MEC-0003 (E4, Rang 2 in allen 3 Ansichten), MEC-0021 (E5, aber s.u. auch als "niedrig/hoch" relevant je nach Betrachtungsebene) |
| Hoch | Schwach/unsicher | **Strategisches Evidenzrisiko** | **MEC-0018** (Rang 3 im Vollgraphen, E2–E3, dokumentiertes Replikationsrisiko B-0010 Priorität Hoch, schmale Quellenbasis) und nachgelagert MOD-0008, P-0035, P-0036, P-0041; sekundär MEC-0010/MEC-0011 (beide 2026-07-01 per Peer-Review-Entscheidung auf E2 herabgestuft, weiterhin mit Betweenness > 1900 strukturell relevant) |
| Niedrig | Hoch | Mögliche Integrations-/Synthesechance | **MEC-0020** (E4, peer-reviewed, aber 0 P-Verbindungen — der klarste Einzelfall im gesamten Bestand), **MEC-0021** (E5 — höchste Evidenzklasse überhaupt — aber nur 4 P-/2 T-Verbindungen, unterdurchschnittlich für seine Evidenzstärke), P-0039 und P-0040 (beide E4, aber 0 MEC-Verbindungen) |
| Niedrig | Niedrig | Randbereich/geringe Priorität | Community 9 (ST-0241–ST-0244, Ariely-Dishonesty-Cluster, Priorität Hoch in `SCIENTIFIC_DEBT.md` B-0012 — bewusst nicht zu P/MEC erhoben, vollständig isoliert, 0 externe Kanten), T-0039 (E2, 0 P-Links) |

**Zentraler Befund (Kern der Auftragsfrage):** Strukturell wichtige Teile des Codex hängen tatsächlich an einer wissenschaftlich vorsichtig einzustufenden Grundlage — konkret die MEC-0018-Familie (Pre-Suasion). Dies ist kein neues Risiko (das Objekt selbst dokumentiert es bereits vorbildlich transparent), aber der Grad der strukturellen Zentralität dieses konkreten Risikos war vor dieser Analyse nicht in einem einzigen Blick sichtbar — er ergibt sich erst aus dem Vergleich von Graphrang und Evidenzlevel über mehrere Objekte hinweg. Auf der Gegenseite zeigt sich, dass der Codex evidenzseitig stärkere Bausteine besitzt (MEC-0020, MEC-0021), die strukturell nicht annähernd so viel Gewicht tragen, wie ihre Wissenschaftlichkeit es erlauben würde.

---

## 10. Underused Strengths and Synthesis Opportunities

| Objekt | Evidenzlevel | Strukturbefund | Mögliche Frage (keine Umsetzung) |
|---|---|---|---|
| MEC-0020 (Perspektivübernahme-Asymmetrie durch Macht, Galinsky) | E4, peer-reviewed, repliziert | 0 P-Verbindungen (einziger MEC im gesamten Bestand mit diesem Wert), nur 1 T-Verbindung, Gesamtgrad 12 (drittniedrigster aller 29 MEC) | Gäbe es ein Prinzip, das explizit auf machtbasierter Perspektivübernahme-Asymmetrie aufbaut (z. B. im Buying-Center- oder Verhandlungskontext)? Aktuell nicht modelliert |
| MEC-0021 (Anchoring) | **E5** — höchste Evidenzklasse, "eines der am häufigsten replizierten Phänomene der Kognitionspsychologie" laut eigenem Objekt | Nur 4 P- und 2 T-Verbindungen — deutlich unterdurchschnittlich im Verhältnis zu MEC-0002/MEC-0003 (12–13 P-Verbindungen bei vergleichbarer oder niedrigerer Evidenzklasse) | Ist die praktische Ausschöpfung des am besten belegten Effekts im gesamten Codex bereits vollständig, oder gibt es unentdeckte Anwendungsfelder jenseits der bisherigen Anker-/Verhandlungstechniken? |
| P-0039 (Buoyancy/Erklärungsstil) und P-0040 (Purposeful Serving) | Beide E4 (Seligman/MetLife bzw. Grant-Studien) | Beide ohne MEC-Anbindung; P-0040 im MEC-P-T-Fokusgraph vollständig isoliert (Community-Analyse: eigenständiges Zweier-/Einzelknoten-Fragment) | Zwei evidenzstarke Prinzipien aus "To Sell Is Human" (Pink) sitzen strukturell am Rand des Mechanismus-Netzwerks — liegt das an einer echten konzeptuellen Eigenständigkeit (Resilienz/Motivation als eigene Kategorie neben Kognition/Sozialpsychologie) oder an einer noch fehlenden MEC-Modellierung? |
| MEC-0025 (Altruistische Bestrafung) | E4 (Kernphänomen, Metaanalyse über 37 Studien) | Nur 1 P-Verbindung trotz breiter Replikationsbasis | Analog zu MEC-0020/0021 — starke Grundlagenforschung, schmale Prinzipien-Ableitung |
| MEC-0026–MEC-0029 (Made-to-Stick-Familie: Curse of Knowledge, Curiosity Gap, Concreteness, Narrative Transportation) | Durchgängig E3–E4 | Durchgängig nur 2 P-Verbindungen, überwiegend 0 T-Verbindungen | **Wahrscheinlich ein Recency-Effekt, kein Qualitätsproblem:** B-0015 (Made to Stick) war das zuletzt verarbeitete Buch im Behavioral Science Expansion Sprint (2026-07-02) — der Codex hatte strukturell am wenigsten Zeit, nachgelagerte P/T-Objekte für diese vier Mechanismen zu bilden. Dies ist explizit als Bias-Hinweis zu lesen, nicht als Bewertung der MEC-Qualität |

**Wichtiger methodischer Hinweis zu dieser Sektion:** Alle Einträge sind als Fragen formuliert, nicht als Handlungsaufträge. Es wurde keine automatische Erweiterung, kein neues Objekt und keine neue Kante vorgenommen.

---

## 11. Research and Synthesis Priority Map

| # | Befund | Graphbefund | Evidenzbefund | Strategische Bedeutung | Unsicherheit | Empfohlener Arbeitstyp | Priorität |
|---|---|---|---|---|---|---|---|
| 1 | MEC-0018-Familie: Struktur/Evidenz-Diskrepanz sichtbar machen | Rang 3 (Vollgraph), fällt in konzeptuellen Ansichten auf Rang 6 | E2–E3, dokumentiertes Replikationsrisiko (B-0010, Priorität Hoch) | Hoch — größter Einzelbefund dieses Sprints | Niedrig (Befund ist durch Graph + Scientific Debt doppelt bestätigt) | **Editorial Review Priority** (Sichtbarkeits-Hinweis in P-0035/P-0036/P-0041 prüfen, analog zum bestehenden ⚠-Publication-Bias-Muster) | **Hoch** |
| 2 | MEC-0020/MEC-0021: evidenzstarke, strukturell unterausgeschöpfte Mechanismen | Niedrige P-/T-Anbindung trotz Spitzenrang bei Grad (MEC-0021) bzw. niedrigem Gesamtgrad (MEC-0020) | E4/E5 — beide oberes Ende der Evidenzskala | Mittel — mögliche ungenutzte Substanz, aber keine Dringlichkeit | Mittel (ob eine Erweiterung sinnvoll ist, ist eine inhaltliche Frage, kein reiner Graphbefund) | **Synthesis Priority** (prüfen, ob ein neues P aus MEC-0020 bzw. eine Erweiterung der MEC-0021-Anwendung sachlich gerechtfertigt ist — kein automatisches Anlegen) | Mittel |
| 3 | ST-0068/ST-0084/ST-0228: Deadline-/Tempo-Thema buchübergreifend unverbunden | 3 Orphans über 2 Bücher (Voss, Ariely) ohne gegenseitige oder P/T-Anbindung | E2–E3 (praxisnah, teils mit Feldexperiment-Stützung) | Niedrig-mittel — thematisch kohärent, aber kein zentraler Codex-Bereich | Mittel | **Synthesis Priority** (mögliches gemeinsames Prinzip zu Deadlines/Verhandlungstempo prüfen) | Niedrig |
| 4 | ST-0171: dokumentierter Cross-Book-Bezug ohne Graph-Kante | Orphan trotz explizitem Fließtext-Verweis auf B-0005/B-0006 | E3 | Niedrig — Einzelfall | Niedrig | **Graph Modeling Review** (prüfen, ob eine explizite ID-Referenz nachträglich ergänzt werden sollte — Entscheidung liegt beim Herausgeber, nicht automatisch umzusetzen) | Niedrig |
| 5 | MOD-0002: scheinbare vs. echte Quellenvielfalt | 3 SRC zitiert, 2 davon derselbe Autor | E3 (Modell-Ebene) | Niedrig — beeinflusst nicht die Kernaussage des Modells, aber die "Cross-Domain"-Einordnung sollte präzise bleiben | Niedrig | **Editorial Review Priority** (Formulierung "cross-domain" vs. "cross-book (gleicher Autor)" ggf. in künftigen Sprint-Reports präzisieren) | Niedrig |
| 6 | MOD-0005/MOD-0010: strukturelle "Senken" (hoher Out-, niedriger In-Grad) | Extreme Asymmetrie (MOD-0005: 1 vs. 38) | MOD-0005 deckt sich mit bereits bekannter Quellenunvollständigkeit (SD-SYS-002, Priorität Hoch) | Mittel — bereits bekanntes Risiko, hier graphisch neu bestätigt | Niedrig (Ursache bereits dokumentiert) | **No Action** (Risiko ist bereits in `SCIENTIFIC_DEBT.md` mit eigener Priorität geführt — dieser Sprint bestätigt es nur graphisch, keine neue Handlung nötig) | — |
| 7 | T-0048: referenzierte, aber nie angelegte Technik | 2 unaufgelöste Referenzen im Compiler-Report | — (existiert nicht als Objekt) | Niedrig | Niedrig (bereits als Compiler-Triage-Punkt T-05 dokumentiert) | **Research Priority** (nur falls ein künftiger Prospecting-Themenblock bearbeitet wird — kein eigenständiger Sprintauslöser) | Niedrig |
| 8 | Community 9 (Ariely-Dishonesty-Cluster): vollständige Isolation | 0 externe Kanten, einzige vollständig isolierte Mehrknoten-Komponente im Vollgraphen | Bereits als "bewusst nicht verwertet" dokumentiert (B-0012, Priorität Hoch) | Niedrig für Handlung, hoch für Dokumentationswert | Niedrig | **No Action** (Isolation ist die korrekte, gewollte graphische Konsequenz einer bereits getroffenen Entscheidung) | — |
| 9 | MEC-0026–0029 (Made to Stick): niedrige Integration | Durchgängig niedrige P-/T-Anbindung | E3–E4, keine Qualitätsauffälligkeit | Niedrig — wahrscheinlich Recency-Effekt | Mittel (nicht abschließend von echter thematischer Randständigkeit unterscheidbar ohne inhaltliche Prüfung) | **Graph Modeling Review** / Beobachtung für den nächsten Atlas-Lauf (erneut prüfen, ob sich die Anbindung mit der Zeit organisch verbessert) | Niedrig |

---

## 12. Editorial Assessment

Der Sales Codex zeigt in dieser ersten graphbasierten Betrachtung ein insgesamt konsistentes Bild: Die strukturell zentralsten Objekte sind überwiegend auch die evidenzstärksten (MEC-0002, MEC-0003), was dafür spricht, dass die bisherige redaktionelle Intuition über "wichtige" Mechanismen bereits weitgehend mit der tatsächlichen Netzwerkstruktur übereinstimmt. Der Codex ist zudem, abgesehen von den 18 (ausschließlich ST-typischen) Orphans, im konzeptuellen Kern (A/MEC/P/T/MOD) vollständig verbunden — es gibt keine zweite, verborgene "Parallelwissensbasis".

Der wichtigste redaktionell relevante Einzelbefund ist die MEC-0018-Konstellation: nicht weil das Objekt selbst mangelhaft dokumentiert wäre (es ist im Gegenteil ein Beispiel für vorbildliche Evidenzdifferenzierung), sondern weil seine strukturelle Downstream-Wirkung (drei abhängige Prinzipien) einen Risikograd trägt, der auf P-Ebene möglicherweise nicht in gleicher Klarheit sichtbar ist wie auf MEC-Ebene. Dies ist eine Sichtbarkeits-, keine Sachfrage.

Die Cluster-Analyse bestätigt, dass Buch-/Autorenkonzentration ein wiederkehrendes, aber überwiegend unproblematisches Strukturmuster ist (Einzelbuch-Modelle sind laut Methodik legitim) — mit der Ausnahme, dass "Cross-Domain"-Zuschreibungen (MOD-0002) präziser zwischen struktureller und quellenseitiger Breite unterscheiden sollten.

Die Existenz mehrerer evidenzstarker, aber strukturell unterintegrierter Mechanismen (MEC-0020, MEC-0021, MEC-0025) deutet darauf hin, dass der Codex mancherorts konservativer in der Prinzipien-Ableitung war, als die zugrundeliegende Wissenschaft es erlauben würde — dies ist eher ein Zeichen von Sorgfalt (keine überstürzte P-Bildung) als von Nachlässigkeit, sollte aber als bewusste redaktionelle Beobachtung festgehalten werden.

---

## 13. Recommended Next Action

**Primäre nächste Hauptaktion (genau eine):**

**Editorial Review Priority — Sichtbarkeits-Prüfung der MEC-0018-Abhängigkeitskette.** Der Herausgeber prüft, ob P-0035 (Rahmen zuerst), P-0036 (Aufmerksamkeit strategisch lenken) und P-0041 (System-1-kompatible Darstellung) sowie MOD-0008 (Pre-Suasion-Modell) einen sichtbaren, kurzen Struktur-Risiko-Hinweis erhalten sollten — analog zum bereits etablierten Muster "⚠ Hinweis: Publication Bias" bei den 29 Challenger/JOLT-Objekten (External Audit Resolution Sprint, 2026-07-03). Es handelt sich um eine reine Sichtbarkeits- und Konsistenzentscheidung: Die zugrundeliegende Evidenzbewertung selbst (E2–E3, differenziert in MEC-0018) ist bereits korrekt und wird durch diese Aktion nicht verändert — keine neue Recherche, keine E-Level-Änderung, keine neue Herausgeberentscheidung wird durch diesen Report selbst getroffen. Diese Aktion wurde gewählt, weil sie (a) den mit Abstand robustesten und am höchsten priorisierten Einzelbefund dieses Sprints direkt adressiert, (b) mit dem Verbotsrahmen dieses Sprints vollständig vereinbar ist (keine neuen Objekte, keine Framework-Änderung, keine geschlossene Open Decision), und (c) einen bereits im Repository etablierten Präzedenzmechanismus nutzt statt einen neuen zu erfinden.

Alle übrigen in Abschnitt 11 gelisteten Punkte (Underused Strengths, Orphan-Missing-Links, MOD-0002-Präzisierung, T-0048) sind dokumentiert, aber ausdrücklich nicht als primäre nächste Aktion vorgeschlagen — sie sind niedriger priorisiert oder bereits anderweitig erfasst.

---

## Anhang: Verifikation vor Abschluss

1. **Compiler erneut ausgeführt** (zweiter Lauf am Ende des Sprints, vor Fertigstellung dieses Reports): Nodes 514, Edges 2071, Orphans 18, Duplicate IDs 0 — identisch zum ersten Lauf und zur Referenz-Baseline.
2. **Zahlenkonsistenz geprüft:** Node-Typ-Summe (309+60+57+47+29+12 = 514) und Edge-Typ-Paar-Summe (286+219+195+185+137+116+102+90+85+79+75+70+67+67+62+58+50+44+36+24+24 = 2071) stimmen exakt mit den Compiler-Ausgaben überein.
3. **Rankings stichprobenartig gegen Rohdaten validiert:** MEC-0002/MEC-0003-Rangfolge in allen drei Graphansichten manuell gegen `metrics_full.csv`, `metrics_conceptual_no_ST.csv` und `metrics_MEC_P_T_focus.csv` geprüft; P-0039/P-0040/P-S1-003-Isolation im MEC-P-T-Fokusgraph gegen die Connected-Components-Ausgabe verifiziert; Community-9-Isolation (Ariely-Dishonesty) gegen zwei unabhängige Verfahren (Connected Components UND Greedy-Modularity-Clustering) gegengeprüft — beide liefern dasselbe Vier-Knoten-Fragment.
4. **Alle 18 real gefundenen Orphans abgedeckt** — vollständige Liste in Abschnitt 8, kein Orphan aus `reference_orphans.csv` ausgelassen.
5. **Keine Wissensobjekte, Quellen oder Framework-Dateien verändert.** Einzige Repository-Änderung durch diesen Sprint ist diese Reportdatei selbst (`00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`). `08_knowledge_atlas/output/*` wurde durch den erneuten Compiler-Lauf neu geschrieben, aber inhaltlich unverändert (`git diff --stat -- 08_knowledge_atlas/` liefert keine Differenz). Vorbestehende, nicht von diesem Sprint stammende unstaged Änderungen im Repository (u. a. `00_project/NEXT_ACTION.md`, mehrere archivierte Release-Dokumente — erkennbar an `git status` zu Sprintbeginn) wurden nicht berührt und sind nicht Gegenstand dieses Sprints.

---

*Dieser Report ist ein generierter Analyse-Output eines diagnostischen Sprints, kein Wissensobjekt und keine Framework-Datei. Er ersetzt keine Herausgeberentscheidung und trifft keine inhaltliche Bewertung einzelner Wissensobjekte über das hinaus, was bereits in den Objekten selbst oder in `SCIENTIFIC_DEBT.md` dokumentiert ist.*
