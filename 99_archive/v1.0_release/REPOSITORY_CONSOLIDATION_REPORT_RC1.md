# Repository Consolidation Report — RC-1

**Dokumentklasse:** Audit / Reference
**Sprint:** Repository Consolidation Sprint 1 (rein strukturell, read-only)
**Auditor:** KI-Redaktion Sales Codex, Rolle: Lead-Architekt / Repository-Auditor
**Stichtag:** 2026-07-02
**Methodik:** Ausschließlich lesende, strukturelle Analyse des gesamten Repository (718 Dateien exkl. `.git`, davon 683 Markdown-Dateien). Keine Datei wurde verändert, verschoben, umbenannt, archiviert oder gelöscht. Es wurden keine neuen Wissensobjekte, keine neue Literatur, keine Frameworkänderungen, keine Open Decisions und keine Governance-Regeln erzeugt.
**Explizite Nicht-Ziele:** Inhaltliche/wissenschaftliche Bewertung einzelner Wissensobjekte (siehe stattdessen `CODEX_AUDIT_2026-07.md`, `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`). Dieser Bericht bewertet ausschließlich Struktur, Ablage, Benennung, Governance-Architektur und Skalierbarkeit.
**Grundregel:** Keine eigene Erinnerung als Autorität. Jede Aussage in diesem Bericht stützt sich auf tatsächlich gelesene Repository-Dateien (Pfade werden durchgängig zitiert). Wo Unsicherheit besteht, wird sie markiert, nicht geglättet.

---

# 1. Executive Summary

## Gesamtzustand

Der Sales Codex ist inhaltlich ungewöhnlich weit entwickelt (683 Markdown-Dateien, 15 vollständige Buchanalysen, 514 Wissensobjekte in `03_knowledge_base/` — 309 Statements, 60 Annahmen, 29 Mechanismen, 57 Prinzipien, 47 Techniken, 12 Modelle), aber strukturell hat die Ablage mit diesem Wachstum nicht vollständig Schritt gehalten. Es handelt sich nicht um ein unordentliches Repository — im Gegenteil: Die Kernstruktur (`00_project` bis `99_archive`) ist sauber konzipiert und in weiten Teilen konsequent umgesetzt. Das eigentliche Risiko liegt an den Rändern: in einer numerischen Ordnerkollision auf oberster Ebene, in einer Governance-Ebene, die auf neun teils parallele, teils verwaiste Steuerungsdokumente angewachsen ist, in einem zentralen Steuerungsdokument (`book_catalog.md`), das seit dem zweiten Buch nicht mehr mit der Realität übereinstimmt, und in einer Forschungsprogramm-Struktur, die zu 88 % aus unbefüllten Platzhalterdateien besteht.

Bemerkenswert ist, dass ein erheblicher Teil dieser Befunde bereits **repository-intern selbst dokumentiert** ist — in `CODEX_AUDIT_2026-07.md`, `POST_MORTEM_B0002.md`, `CURRENT_STATE.md` und `review_queue.md` finden sich frühere Hinweise auf denselben leeren Duplikat-Ordner, dieselbe Wissensmodell-Doppelung und dieselbe Fehlplatzierung von VAL-0002, die dieser Bericht unabhängig bestätigt. Das ist einerseits ein Beleg für eine gesunde Selbstprüfungskultur — andererseits ein Beleg dafür, dass erkannte strukturelle Probleme bislang nicht in tatsächliche Konsolidierung überführt wurden, weil sie mangels Herausgeber-Entscheidung "vorgemerkt, nicht behoben" blieben.

## Architektur-Reifegrad

Auf einer informellen Skala von "Prototyp" bis "produktionsreif für 5 Jahre Wachstum" liegt die Architektur bei **solide, aber nicht freeze-reif**. Das Nummernschema (`00_` bis `07_`, `99_`), die Trennung von Rohquellen, Wissensbasis, Buchanalyse, Synthese und Publikation sowie das durchgängige ID-System (SRC/ST/A/MEC/P/T/MOD/VAL) sind gute, skalierbare Grundentscheidungen. Das System ist jedoch an mehreren Stellen bereits unter der aktuellen Last (15 Bücher, 514 Wissensobjekte) an Grenzen gestoßen, die bei einer Verdopjung (siehe Kapitel 9) ohne Korrektur zu echten Betriebsproblemen würden.

## Wartbarkeit

Die Wartbarkeit der **Wissensebene** (`03_knowledge_base/`) ist hoch — jedes Objekt ist ID-adressierbar, Source-ID-Feld-Konvention seit v1.0 verbindlich, Canonicalisierungslogik dokumentiert. Die Wartbarkeit der **Governance-Ebene** (`00_project/`) ist demgegenüber gefährdet: 36 Dateien liegen flach in einem einzigen Verzeichnis, ohne Unterordnung nach Typ (aktive Steuerung vs. einmalige Sprintberichte vs. historische Artefakte), und mindestens vier dieser Dateien (`decision_log.md`, `roadmap.md`, `REPOSITORY_KPIS.md`, Teile von `backlog.md`) sind faktisch verwaist, aber nicht als solche gekennzeichnet oder archiviert.

## Größte strukturelle Risiken

Erstens die Nummernkollision auf oberster Ebene (`04_book_analysis` **und** `04_synthesis`; `05_publications` **und** `05_research`) — ein Namensschema, das nicht mehr eindeutig ist, ist bei weiterem Wachstum ein Skalierungsrisiko. Zweitens `02_sources/book_catalog.md`, das laut `task_rules.md` die maßgebliche Steuerungsquelle für die automatische Task-Generierung ist, dessen Buch-IDs und Statuswerte aber seit B-0002 nicht mehr der Realität entsprechen. Drittens die weitgehend leere Gerüststruktur von `06_research_program/` (14 von 16 Dateien mit 1–3 Zeilen Inhalt), die im Auftrag als abgeschlossene Entwicklungsphase ("Research Program") vorausgesetzt wird, strukturell aber überwiegend unbefüllt ist.

## Wichtigste Stärken

Die durchgängige ID-Architektur und das Canonical-Knowledge-Model mit expliziter Neu-/Erweitern-/Zusammenführen-/Verwerfen-Logik sind ein seltenes Maß an struktureller Disziplin für ein Ein-Personen-Wissensprojekt. Die Selbstprüfungskultur ist außergewöhnlich: Governance-Dokumente widersprechen sich nicht heimlich, sondern dokumentieren Widersprüche aktiv (`OPEN_DECISIONS.md`, `SCIENTIFIC_DEBT.md`). Die Trennung "Infrastruktur Englisch / Inhalt Deutsch" (`LANGUAGE_POLICY.md`) wird über praktisch das gesamte Repository konsequent eingehalten.

---

# 2. Repository Structure Review

## Gesamtstruktur

```
00_project/            Projektsteuerung, Governance, Sprint-/Audit-Berichte (36 Dateien + peer_review/decisions/)
01_framework/           Methodik, Standards, Wissensmodell, Agentenprotokolle, Templates (8 Unterordner)
02_sources/             Quellen: Bücher (Rohdateien + SRC-Objekte), 5 leere Kategorieordner
03_knowledge_base/      6 aktiv genutzte + 3 leere Wissensobjekt-Kategorien
04_book_analysis/       15 befüllte + 1 leerer Buchordner
04_synthesis/           3 Sprint-Synthesen (Nummernkollision mit 04_book_analysis)
05_publications/        4 leere Unterordner (noch nicht begonnen)
05_research/            1 Datei (Nummernkollision mit 05_publications)
06_media/               3 leere Unterordner
06_research_program/    aktives Forschungsprogramm, überwiegend Platzhalter
07_scripts/             1 README, keine Skripte
99_archive/             1 README, keine archivierten Inhalte
+ 10 Root-Dateien (README, VISION, CURRENT_STATE, CONTRIBUTING, LANGUAGE_POLICY, INDEX,
  PROJECT_BOOTSTRAP, CLAUDE_BOOTSTRAP, SETUP, SCRP-0001_Sales_Core.md)
```

## Bewertung: logische Trennung, Verantwortlichkeiten, Hierarchie

Die Grundidee — Quellen trennen von Wissensbasis, trennen von Buchanalyse, trennen von Synthese, trennen von Publikation — ist architektonisch richtig und in `README.md` sauber begründet ("Nicht zuerst das Buch schreiben. Zuerst das Wissenssystem bauen."). Die Verantwortlichkeiten der einzelnen Top-Level-Ordner sind grundsätzlich überschneidungsfrei definiert. Die Hierarchietiefe ist angemessen: Die tiefste reguläre Verschachtelung liegt bei vier Ebenen (`06_research_program/active/W001/<Datei>`), was für ein Wissenssystem dieser Größe nicht übermäßig ist.

## Konkrete Befunde

### Befund 2.1 — Nummernkollision `04_*` und `05_*`

**Problem:** Zwei Ordnerpaare tragen dieselbe Ordnungsziffer: `04_book_analysis/` und `04_synthesis/`; `05_publications/` und `05_research/`. Ein Präfix-Nummernschema soll eine eindeutige, sortierbare Lesereihenfolge herstellen — bei doppelter Vergabe verliert es diese Funktion.

**Begründung/Ursache:** `05_research/` wurde nachträglich im Academic Recovery Sprint Phase 2 angelegt (`CURRENT_STATE.md`, Abschnitt "Academic Recovery Sprint … Phase 2": *"Neuer Repository-Bereich `05_research/` mit `LITERATURE_INDEX.md` angelegt"*), ohne dass zu diesem Zeitpunkt eine Kollisionsprüfung gegen bestehende Top-Level-Nummern erfolgte. `04_synthesis/` wurde vermutlich analog als eigenständige Ergänzung zu `04_book_analysis/` angelegt, ohne Rücksicht auf die fortlaufende Zählung.

**Nutzen einer Korrektur:** Wiederherstellung einer eindeutigen, sortierbaren Ordnerhierarchie; verhindert, dass zukünftige Automatisierung (`07_scripts/`) oder neue Mitarbeitende (menschlich oder KI) die Nummer als Suchschlüssel fehlinterpretieren.

**Aufwand:** Mittel (Umbenennung von zwei Ordnern plus Anpassung aller referenzierenden Pfadangaben — siehe Kapitel 8, Cross-Reference-Audit, für das Ausmaß der Referenzierung).

**Priorität:** HOCH (siehe Kapitel 12, Kategorie A).

### Befund 2.2 — `05_research/` als Ein-Datei-Ordner mit inhaltlicher Nähe zu `06_research_program/`

**Problem:** `05_research/` enthält ausschließlich `LITERATURE_INDEX.md` (eine Datei). Gleichzeitig existiert `06_research_program/` als vollständige, mehrstufige Struktur für "Research" im engeren Sinn (Hypothesen, Reviews, Decision Briefs). Zwei Top-Level-Ordner mit dem Wortstamm "research" für unterschiedliche, aber verwandte Zwecke sind für neue Bearbeitende nicht auf den ersten Blick unterscheidbar.

**Begründung:** `OPEN_DECISIONS.md`, OD-011, benennt dieses Problem bereits selbst ("Literature-Governance") und fragt, ob `LITERATURE_INDEX.md` "als dauerhafter Framework-Bestandteil formal verankert werden" soll und wie es sich von `SCIENTIFIC_DEBT.md`/`review_queue.md` abgrenzt — ohne bislang eine Antwort zu haben.

**Nutzen:** Eine Konsolidierung würde gleichzeitig die Nummernkollision aus Befund 2.1 auflösen und die in OD-011 bereits gestellte Frage strukturell beantworten.

**Aufwand:** Gering (eine Datei verschieben).

**Priorität:** HOCH — siehe Kapitel 4, Klassifikation, für den konkreten MERGE-Vorschlag.

### Befund 2.3 — Fünf leere Kategorieordner unter `02_sources/`

**Problem:** `02_sources/articles/`, `interviews/`, `other/`, `podcasts/`, `studies/` sind vollständig leer, obwohl `README.md` sie explizit als Bestandteil der Struktur nennt ("Bücher, Studien, Artikel, Interviews, Podcasts und sonstige Quellen"). Alle 15 bislang verarbeiteten Quellen sind Bücher.

**Begründung:** Dies ist kein Fehler, sondern der erwartbare Zustand eines Projekts, das bislang ausschließlich im "Book Mode" gearbeitet hat. Die Ordner sind vorbereitete Kategorien für eine Quellenvielfalt, die noch nicht eingetreten ist.

**Nutzen/Einordnung:** Kein Handlungsbedarf. Diese leeren Ordner sind **keine Altlast**, sondern vorbereitete Erweiterbarkeit — im Unterschied zu Befund 2.4.

**Priorität:** Keine (nur zur Vollständigkeit dokumentiert).

### Befund 2.4 — Leerer Duplikat-Ordner `04_book_analysis/Never_Split_The_Difference/`

**Problem:** Neben dem befüllten Ordner `04_book_analysis/Never Split the Difference/` (mit Leerzeichen, 3 Dateien) existiert ein zweiter, vollständig leerer Ordner `04_book_analysis/Never_Split_The_Difference/` (mit Unterstrichen).

**Begründung:** Dieser Befund ist **bereits im Repository selbst dokumentiert und zur Entfernung vorgemerkt**: `CURRENT_STATE.md` (Abschnitt "Codex Audit 2026-07 …") vermerkt wörtlich *"Leerer Ordner `04_book_analysis/Never_Split_The_Difference/` zur Entfernung vorgemerkt (nicht gelöscht)"*. Der Ordner ist seit mindestens dem Consistency Correction Sprint (2026-07) als Duplikat bekannt, aber laut Read-Only-Regel dieses Sprints und mangels Herausgeber-Freigabe weiterhin vorhanden.

**Nutzen einer Korrektur:** Beseitigt eine irreführende Verzeichnisstruktur, die bei automatisierter Verarbeitung (State Inspector, Task-Generierung) zu Fehlinterpretationen führen könnte.

**Aufwand:** Minimal (Ordner löschen — kein Dateiinhalt betroffen).

**Priorität:** HOCH, aber bereits als Entscheidung beim Herausgeber anhängig — kein neuer Befund, sondern Bestätigung eines bekannten offenen Punktes.

### Befund 2.5 — Inkonsistente Benennung der Buchordner unter `04_book_analysis/`

**Problem:** 14 von 15 befüllten Buchordnern verwenden Leerzeichen im Ordnernamen (`Never Split the Difference`, `The Challenger Sale`, `Thinking, Fast and Slow` — Letzterer sogar mit Komma). Ein Ordner (`SPIN_Selling`) verwendet Unterstriche. `LANGUAGE_POLICY.md` schreibt für Ordnernamen ausdrücklich "Englisch" und technische Robustheit vor, trifft aber keine explizite Aussage zu Leerzeichen vs. Unterstrichen — dennoch ist jedes andere ID-basierte Namensschema im Repository (Dateien, nicht Ordner) konsequent unterstrich-/snake_case-basiert.

**Begründung:** `SPIN_Selling` ist der älteste Buchordner (Pilot 001, angelegt vor der Konvention der übrigen 14 Bücher) und hat vermutlich die ursprüngliche, spätere nicht weiterverfolgte Namenskonvention behalten.

**Nutzen:** Konsistente Ordnernamen erleichtern Skripting/Automatisierung (`07_scripts/`) und vermeiden Sonderfallbehandlung bei Pfaden mit Leerzeichen und Kommas (Letzteres ist in Shell-Kontexten besonders fehleranfällig).

**Aufwand:** Mittel (15 Ordner umbenennen + alle referenzierenden Pfade in Governance-/Buchdateien anpassen).

**Priorität:** MITTEL (funktionsfähig, aber technische Schuld — siehe Kapitel 10).

### Befund 2.6 — `05_publications/` vollständig leer

**Problem:** Alle vier Unterordner (`sales_codex_book/`, `talks/`, `trainings/`, `workbook/`) sind leer.

**Begründung:** Konsistent mit dem in `VISION.md` und `roadmap.md` beschriebenen Phasenmodell ("Phase 4 — Veröffentlichung" liegt nach den aktuell laufenden Phasen). Kein struktureller Mangel, sondern erwartungsgemäßer Zustand vor Erreichen dieser Phase.

**Priorität:** Keine.

### Befund 2.7 — Root-Level-Datei `SCRP-0001_Sales_Core.md` außerhalb jeder Ordnerstruktur

**Problem:** Mit 73.540 Byte die mit Abstand größte Einzeldatei im Repository (außerhalb `02_sources/books/`) liegt direkt im Repository-Root, gleichrangig neben `README.md`, `VISION.md` usw. — obwohl sie inhaltlich ein generiertes Exportdokument ist ("Externes Peer-Review-Paket", laut Eigenbeschreibung Zeile 3–4 der Datei), kein Grundlagendokument des Projekts.

**Begründung:** Root-Dateien sind laut `README.md`-Konvention für projektweite Einstiegsdokumente reserviert (Vision, Setup, Sprachregeln, Index). Ein für externe Gutachter erstelltes, in sich geschlossenes Exportdokument eines einzelnen Sprints (Sales Sprint 1) gehört nach dieser Logik nicht auf die Root-Ebene.

**Nutzen einer Korrektur:** Root-Ebene bleibt auf die zehn tatsächlichen Einstiegsdokumente begrenzt und dadurch überblickbar; das Exportdokument wird an einem Ort auffindbar, der seiner Funktion entspricht (Peer-Review-Governance).

**Aufwand:** Gering (eine Datei verschieben).

**Priorität:** MITTEL — siehe Kapitel 4 für Klassifikation.

## Skalierbarkeit und Konsistenz — Zusammenfassung

Die Struktur ist für den aktuellen Umfang funktionsfähig, zeigt aber an mehreren Stellen, dass organisches Wachstum (neue Ordner nach Bedarf, ohne Rückprüfung gegen das Nummernschema) die ursprüngliche Konsistenz bereits zweimal durchbrochen hat. Eine Verdopplung des Inhalts ohne vorherige Korrektur dieser Befunde würde die Unklarheiten vervielfachen, nicht nur linear fortschreiben (siehe Kapitel 9).

---

# 3. File Responsibility Review

Diese Analyse deckt alle 718 Dateien (exkl. `.git`) ab. Da eine Einzelbewertung aller 683 Markdown-Dateien den Rahmen sprengen würde und die Wissensobjekt-Ebene (`03_knowledge_base/`, 514 Objekte) ein durchgehend einheitliches, bereits im Framework definiertes Muster verwendet (ein Objekt = eine Datei = eine ID, keine strukturellen Auffälligkeiten festgestellt), erfolgt die Bewertung auf zwei Ebenen: (a) eine vollständige Kategorienübersicht mit Dateizahlen und struktureller Einordnung, (b) eine Einzelbewertung aller Dateien, die von ihrer jeweiligen Kategorie-Norm abweichen ("auffällige Dateien" — vollständig in Kapitel 4 klassifiziert).

## 3.1 Kategorienübersicht

| Bereich | Dateien | Zweck | Struktureller Zustand |
|---|---|---|---|
| Root (10 Dateien) | 10 | Einstiegspunkte, Grundregeln | 4 konkurrierende Onboarding-Dokumente (siehe 3.3); 1 Fehlplatzierung (SCRP-0001) |
| `00_project/` (36 Dateien + 3 in `peer_review/decisions/`) | 39 | Governance, Sprint-/Audit-Berichte | Flache Struktur ohne Typ-Unterordnung; mehrere verwaiste Dokumente (siehe 3.2) |
| `01_framework/` | 27 | Methodik, Standards, Templates, Agentenprotokolle | Strukturell sauber; 1 Dublette (Wissensmodell, siehe 3.4) |
| `02_sources/` | 51 (17 SRC/Katalog-MD + 34 Rohdateien) | Primärquellen | 1 Fehlplatzierung (SRC-0010); Rohdateien-Sammlung teils unklar zugeordnet (siehe 3.5) |
| `03_knowledge_base/` | 514 | Wissensobjekte (ST/A/MEC/P/T/MOD) | Aktiv genutzte Kategorien einheitlich; 3 von 9 Kategorien vollständig ungenutzt (competencies, meta_models, observations) |
| `04_book_analysis/` | 45 (+ 1 Leerordner) | Buchspezifische Analysen | Uneinheitliches Datei-Set pro Buch (1–5 Dateien), historisch bedingt (siehe 3.6) |
| `04_synthesis/` | 8 | Sprintübergreifende Synthese | Strukturell sauber, aber Nummernkollision (Kap. 2) |
| `05_publications/` | 0 | Spätere Veröffentlichungsformen | Noch nicht begonnen (kein Mangel) |
| `05_research/` | 1 | Literaturverzeichnis | Isolierter Ein-Datei-Ordner (Kap. 2) |
| `06_media/` | 0 | Bilder, Diagramme, Mindmaps | Noch nicht begonnen (kein Mangel) |
| `06_research_program/` | 16 | Forschungsprogramm (Hypothesen bis Editor Decision) | 14 von 16 Dateien sind 1–3-zeilige Platzhalter (siehe 3.7) |
| `07_scripts/` | 1 | Automatisierung | Nur README, keine Skripte (kein Mangel, vorbereitete Struktur) |
| `99_archive/` | 1 | Archiv | Nur README, keine archivierten Inhalte (siehe Kap. 6/10) |

## 3.2 `00_project/` — Aktiv vs. historisches Artefakt vs. verwaist

Von den 36 Dateien in `00_project/` sind nach Lektüre folgende Klassen unterscheidbar:

**Aktiv/Operational (kontinuierlich gepflegt, in jeder Session gelesen):** `NEXT_ACTION.md`, `CURRENT_STATE.md` (Root), `OPEN_DECISIONS.md`, `SESSION_LOG.md`, `changelog.md`, `task_rules.md`, `SCIENTIFIC_DEBT.md`, `REPOSITORY_KPIS.md` — laut eigener Klassifikationstabelle in `PROJECT_BOOTSTRAP.md`.

**Steuerungsdokumente mit unklarem Aktualisierungsstatus:** `book_catalog.md` (in `02_sources/`, nicht `00_project/`, aber funktional hierher gehörig) ist als "zentrale Steuerungsliste" deklariert, aber seit B-0002 nicht mehr synchron mit der Realität (siehe 3.2.1 unten — kritischster Einzelbefund dieses Berichts). `backlog.md` hat drei durchgängig leere Tabellen (READY/IN_PROGRESS/REVIEW) und eine nur teilweise gepflegte DONE-Tabelle (vollständige Tasklisten für B-0002, nur Kurzeinträge für B-0006–B-0010, keine Einträge für B-0003–B-0005 und B-0011–B-0015). `roadmap.md` verharrt bei "Phase 0 — läuft", obwohl das Projekt laut `SALES_CODEX_1_0_PROGRAM.md` längst ein eigenes, aktuelleres 5-Phasen-Modell verwendet. `decision_log.md` enthält ausschließlich drei Einträge vom Gründungstag (2026-06-27) und wurde seither nicht mehr fortgeführt — seine Funktion wurde faktisch von `OPEN_DECISIONS.md` übernommen.

**Einmalige Sprint-/Audit-Berichte (historisch, aber korrekt abgelegt):** `ACADEMIC_RECOVERY_PLAN.md`, `ACADEMIC_RECOVERY_REPORT.md`, `ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`, `BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md`, `CODEX_AUDIT_2026-07.md`, `CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md`, `OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`, `SPRINT_2_ABSCHLUSSBERICHT.md`, `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`, `WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md`, `VALIDIERUNGSSPRINT_MEC0010-0012.md` — diese sind funktional korrekt als abgeschlossene Artefakte in `00_project/` verortet, aber nicht von den aktiven Steuerungsdokumenten unterscheidbar, da keine Unterordnung existiert (siehe Kapitel 5).

**Fehlplatzierte, buchspezifische Dokumente:** `VAL-0001_consistency_review_pilot001.md`, `VAL-0002_consistency_review_influence.md`, `PILOT_001_ABSCHLUSSBERICHT.md` liegen in `00_project/`, obwohl das für alle Folgebücher (B-0003 bis B-0015) etablierte Muster VAL-Dateien und Abschlussberichte im jeweiligen `04_book_analysis/<Buch>/`-Ordner ablegt. Dies ist **kein neuer Befund** — `POST_MORTEM_B0002.md` (Zeile 220) hält bereits am 2026-06-30 fest: *"VAL-0002 liegt in `00_project/` statt in einer quellenspezifischen Struktur … Konsistenter wäre `04_book_analysis/Influence/VAL-0002.md`."* Die Empfehlung wurde dokumentiert, aber nie umgesetzt.

**Einmalige Prozessartefakte ohne dauerhaften Wert:** `task_proposal_B-0002_influence.md` ist ein Vorschlagsdokument für einen seit langem abgeschlossenen Task; `task_rules.md` selbst sieht vor, dass "nur ein aktiver Vorschlag gleichzeitig existieren" darf — das Dokument hat also keine aktive Funktion mehr.

### 3.2.1 Kritischster Einzelbefund: `book_catalog.md` vs. Repository-Realität

`02_sources/book_catalog.md` definiert sich selbst (Zeile 5–11) als die Datei, aus der Cowork "deterministisch konkrete Arbeitsaufträge ableitet" und ist laut `task_rules.md` Abschnitt 2 eine der fünf Pflicht-Eingaben des Task-Generierungssystems. Der tatsächliche Katalogzustand:

- **Statuswerte veraltet:** B-0001 (SPIN Selling) trägt Status `REVIEW`, obwohl `CURRENT_STATE.md` das Buch als abgeschlossen führt. B-0002 (Influence) trägt `IN_PROGRESS`, obwohl abgeschlossen. B-0003 bis B-0040 tragen ausnahmslos `WAITING`, obwohl 13 weitere Bücher (B-0003 bis B-0015) nachweislich vollständig verarbeitet wurden.
- **Buch-IDs divergieren fundamental von den tatsächlich vergebenen IDs:** Ab B-0006 stimmen Katalog-ID und real vergebene Buch-ID nicht mehr überein. Katalog-B-0006 = "How to Win Friends and Influence People" (Carnegie) — tatsächlich vergebenes B-0006 = "The JOLT Effect". Katalog-B-0007 = "To Sell Is Human" — tatsächlich B-0007 = "Getting to Yes". Katalog-B-0015 = "Thinking, Fast and Slow" — tatsächlich B-0010. Katalog-B-0016 = "Predictably Irrational" — tatsächlich B-0012. Katalog-B-0017 = "Pre-Suasion" — tatsächlich B-0008. Katalog-B-0028 = "Getting to Yes" (nochmals, mit anderer ID) — tatsächlich B-0007.

**Einordnung:** Dies ist keine kosmetische Unstimmigkeit. Die Datei, die laut eigenem Zweck und laut `task_rules.md` die maßgebliche Eingabequelle für automatisierte Arbeitsableitung ist, würde bei tatsächlicher Nutzung durch das beschriebene System (Abschnitt 4.2 in `task_rules.md`: "Cowork aktiviert sich auf genau einem Buch: dem ersten Eintrag im Catalog mit Status READY") aktuell **kein einziges** der 13 bereits abgeschlossenen Bücher erkennen und stattdessen fälschlich B-0002 (Influence) als "in Bearbeitung" fortsetzen wollen. Das Steuerungsinstrument ist strukturell vorhanden, aber faktisch seit 15 von 15 verarbeiteten Büchern nicht mehr die tatsächliche Steuerungsquelle — diese Rolle hat informell `CURRENT_STATE.md`/`NEXT_ACTION.md` übernommen, ohne dass `book_catalog.md` diese Ablösung dokumentiert oder `task_rules.md` entsprechend angepasst wurde.

## 3.3 Root-Ebene — vier konkurrierende Onboarding-Dokumente

Vier Root-Dateien definieren jeweils eine eigene, nicht deckungsgleiche "Pflichtlektüre"-Reihenfolge für neue Sessions:

| Dokument | Vorgeschriebene Lesereihenfolge |
|---|---|
| `INDEX.md` | README → VISION → CURRENT_STATE → CONTRIBUTING → LANGUAGE_POLICY → master_agent_protocol |
| `PROJECT_BOOTSTRAP.md` | PROJECT_BOOTSTRAP → CURRENT_STATE → NEXT_ACTION → betroffene Arbeitsdateien |
| `CLAUDE_BOOTSTRAP.md` | README → VISION → CURRENT_STATE → CONTRIBUTING → LANGUAGE_POLICY → INDEX → master_agent_protocol → claude_editor_protocol |
| `SETUP.md` | README → VISION → CURRENT_STATE → CONTRIBUTING → LANGUAGE_POLICY → INDEX → kompletter Ordner `01_framework/` |

`CURRENT_STATE.md` selbst (letzte Zeile) nennt wiederum eine fünfte Variante: *"Pflichtlektüre beim Session-Start: `PROJECT_BOOTSTRAP.md` + dieses Dokument + `00_project/NEXT_ACTION.md` + `00_project/SALES_CODEX_1_0_PROGRAM.md`"*. Auch dies ist kein neuer Befund — `review_queue.md`, Abschnitt "Claude Onboarding Review", vermerkt bereits seit einer früheren Session den offenen Prüfpunkt *"Inkonsistenz INDEX.md / CONTRIBUTING.md prüfen"*, ohne dass eine Auflösung dokumentiert ist.

## 3.4 `01_framework/05_knowledge_model/` — dokumentierte Dublette

Der Ordner enthält zwei Dateien für denselben Zweck: `canonical_knowledge_model.md` (334 Zeilen, versioniert, mit vollständiger Entscheidungslogik) und `codex_knowledge_model.md` (69 Zeilen, älter, ohne Versionsangabe). Die zweite Datei trägt bereits einen eigenen Warnhinweis (eingefügt im Consistency Correction Sprint 2026-07): *"Dieses Dokument wird als wahrscheinlich veraltet eingestuft … `canonical_knowledge_model.md` ist die maßgebliche, aktuell gültige Quelle."* Die Datei wurde bewusst nicht gelöscht, weil "Repository-Struktur wird nicht eigenständig verändert" — die Herausgeber-Entscheidung steht noch aus (siehe `SALES_CODEX_1_0_PROGRAM.md`, "Phase 1 … Repository-Hygiene (Duplikat-Ordner, `codex_knowledge_model.md`)").

## 3.5 `02_sources/books/` — Rohquellen ohne Verarbeitungsstatus-Kennzeichnung

Der Ordner enthält 34 Binärdateien (PDF/EPUB) und 16 SRC-Markdown-Dateien (davon eine fehlplatziert, siehe unten) in einem einzigen flachen Verzeichnis. Von den 34 Rohdateien entsprechen 15 einem verarbeiteten SRC-Objekt (z. B. `SPIN® -Selling - Neil Rackham.pdf` ↔ `SRC-0001_SPIN_Selling.md`). Die übrigen 17 Rohdateien (u. a. *12 Rules for Life*, *Atomic Habits*, *Against Empathy*, *Crucial Conversations*, *Drive*, *Buyology*, *The 48 Laws of Power*, *The Art of War*, *Think and Grow Rich*, *The Trusted Advisor*, *Moonwalking with Einstein*, *Harry Lorayne — The Memory Book*, *Meditations*, *Welcome to Your Brain*, *Quiet* und *Quiet Kids*, *Strategy and Tactics of Pricing*) haben **kein** zugehöriges SRC-Objekt und tragen größtenteils unbereinigte, herkunftsbedingte Dateinamen von Downloadquellen (`_OceanofPDF.com_…`, `pdfcoffee.com_…`, `dokumen.pub_…`, `vdoc.pub_…`, `feismo.com-…`, `…_Worldfreebooks.com_…`). Dies ist inhaltlich Rohmaterial-Backlog, kein Fehler — aber strukturell nicht von den aktiv referenzierten Primärquellen unterscheidbar, ohne jede Datei einzeln zu öffnen.

## 3.6 `04_book_analysis/` — uneinheitliches Datei-Set je Buch

| Buch | Dateien | Enthält |
|---|---|---|
| SPIN Selling | 1 | nur `analysis.md` |
| Influence | 2 | `analysis.md`, `BOOK_REVIEW_REPORT` (VAL fehlt hier — liegt in `00_project/`) |
| Never Split the Difference, Gap Selling, Getting to Yes, Pre-Suasion, The Challenger Sale, The JOLT Effect, Thinking Fast and Slow, To Sell Is Human | je 3 | `analysis.md`, `BOOK_REVIEW_REPORT`, `VAL-…` |
| Emotional Intelligence, Made to Stick, Nudge, Predictably Irrational, Priceless | je 4 (Emotional Intelligence: 5, inkl. `test_probe.md`) | zusätzlich `CANONICALIZATION_REPORT` |

**Einordnung:** Diese Staffelung ist **methodisch erklärbar und in `CURRENT_STATE.md` dokumentiert** — der `CANONICALIZATION_REPORT` wurde erst mit dem Behavioral Science Expansion Sprint (B-0011 bis B-0015) eingeführt. Es handelt sich um dokumentierte Prozessevolution, nicht um eine strukturelle Inkonsistenz im negativen Sinn. Die einzige echte Auffälligkeit ist die zusätzliche Datei `test_probe.md` in "Emotional Intelligence" (siehe Kapitel 7).

## 3.7 `06_research_program/` — überwiegend Platzhalterinhalt

Von 16 Markdown-Dateien enthalten 14 lediglich 1–3 Zeilen Text (u. a. `README.md`: 3 Zeilen, `RESEARCH_GOVERNANCE.md`: 3 Zeilen, `DECISION_POLICY.md`: 3 Zeilen, `RESEARCH_STATUS.md`: 3 Zeilen, alle 5 Dateien in `templates/`: je 20–28 Byte). Nur zwei Dateien enthalten substanziellen Inhalt: `active/W001/02_SCIENTIFIC_MASTER_REVIEW.md` (330 Zeilen) und `active/W001/03_GEMINI_RED_TEAM_REVIEW.md` (290 Zeilen). Details und Einordnung siehe Kapitel 6.

## 3.8 Root-Datei `SCRP-0001_Sales_Core.md`

Bereits in Kapitel 2 (Befund 2.7) strukturell eingeordnet. Inhaltlich ein vollständiges, in sich geschlossenes externes Review-Paket für Sales Sprint 1 (254 Wissensobjekte) — funktional ein Exportartefakt, keine Grundlagendatei.

---

# 4. File Classification

Diese Tabelle klassifiziert jede in Kapitel 2–3 als auffällig identifizierte Datei bzw. jeden auffälligen Ordner. Alle übrigen ca. 700 Dateien (insbesondere die vollständige `03_knowledge_base/`-Ebene sowie 01_framework-Kerndokumente) folgen einheitlich ihrer jeweiligen Kategorienorm und werden hier nicht einzeln aufgeführt (implizit: KEEP).

| # | Datei/Ordner | Klassifikation | Begründung | Ziel (bei MERGE/MOVE) / Neuer Name (bei RENAME) |
|---|---|---|---|---|
| 1 | `04_book_analysis/Never_Split_The_Difference/` (leer) | **DELETE** | Leerer Duplikat-Ordner zum befüllten `Never Split the Difference/`; bereits repository-intern zur Entfernung vorgemerkt (`CURRENT_STATE.md`) | — |
| 2 | `04_book_analysis/Emotional Intelligence/test_probe.md` (0 Byte) | **DELETE** | Leere Debug-Datei eines Subagenten; bereits in `SESSION_LOG.md`/`changelog.md` als zu entfernendes Housekeeping-Item dokumentiert | — |
| 3 | `01_framework/05_knowledge_model/codex_knowledge_model.md` | **ARCHIVE** | Selbst als "wahrscheinlich veraltet" gekennzeichnet, durch `canonical_knowledge_model.md` ersetzt; Inhalt historisch wertvoll (zeigt Modellevolution), daher nicht DELETE | `99_archive/` |
| 4 | `02_sources/SRC-0010_thinking_fast_and_slow.md` | **MOVE** | Einzige SRC-Datei außerhalb von `02_sources/books/`; alle 15 übrigen SRC-Dateien liegen dort | `02_sources/books/` |
| 5 | `00_project/VAL-0001_consistency_review_pilot001.md` | **MOVE** | Buchspezifische Validierung, gehört analog zu allen Folgebüchern in den Buchordner | `04_book_analysis/SPIN_Selling/` |
| 6 | `00_project/VAL-0002_consistency_review_influence.md` | **MOVE** | Identisch — zusätzlich bereits in `POST_MORTEM_B0002.md` als Korrekturempfehlung dokumentiert, nie umgesetzt | `04_book_analysis/Influence/` |
| 7 | `00_project/PILOT_001_ABSCHLUSSBERICHT.md` | **MOVE** | Funktionales Äquivalent zu `BOOK_REVIEW_REPORT_B00XX.md`, das bei allen Folgebüchern im Buchordner liegt | `04_book_analysis/SPIN_Selling/` |
| 8 | `SCRP-0001_Sales_Core.md` (Root) | **MOVE** | Generiertes externes Peer-Review-Exportpaket; gehört funktional zur Peer-Review-Governance, nicht auf Root-Ebene neben Projektgrundlagendokumenten | `00_project/peer_review/decisions/` |
| 9 | `05_research/LITERATURE_INDEX.md` | **MERGE** | Löst Nummernkollision mit `05_publications/` auf; inhaltlich Teil der Forschungsgovernance, für die `06_research_program/` bereits existiert; deckt sich mit der in OD-011 selbst gestellten Frage | `06_research_program/LITERATURE_INDEX.md` (danach `05_research/` entfernen) |
| 10 | `00_project/decision_log.md` | **ARCHIVE** | Nur 3 Einträge vom Gründungstag (2026-06-27), seither nicht fortgeführt; Funktion vollständig von `OPEN_DECISIONS.md` übernommen | `99_archive/` |
| 11 | `00_project/roadmap.md` | **ARCHIVE** | Verharrt bei "Phase 0 — läuft"; funktional durch `SALES_CODEX_1_0_PROGRAM.md` (5-Phasen-Modell) abgelöst, aber nie als obsolet markiert | `99_archive/` |
| 12 | `00_project/task_proposal_B-0002_influence.md` | **ARCHIVE** | Einmaliges Vorschlagsdokument für einen seit 2026-06-30 abgeschlossenen Task; `task_rules.md` sieht ohnehin nur einen gleichzeitig aktiven Vorschlag vor | `99_archive/` |
| 13 | `CLAUDE_BOOTSTRAP.md` (Root) | **ARCHIVE** | In `PROJECT_BOOTSTRAP.md`s eigener Dokumentklassifizierungstabelle bereits als "Archived" geführt, liegt aber weiterhin auf Root-Ebene neben aktiven Dokumenten | `99_archive/` |
| 14 | `SETUP.md` (Root) | **ARCHIVE** | Einmalige Erstinbetriebnahme-Anleitung (Git-Init, VS-Code-Setup); letzte Zeile ("Ab jetzt keine Strukturarbeit mehr") ist seit vielen Sprints faktisch überholt | `99_archive/` |
| 15 | `02_sources/book_catalog.md` | **KEEP** (mit dringender inhaltlicher Überarbeitungsempfehlung) | Strukturell notwendig als von `task_rules.md` referenzierte Pflichteingabe; Datei bleibt, Inhalt ist jedoch der gravierendste Einzelbefund dieses Berichts (siehe 3.2.1) — Korrektur ist eine redaktionelle, keine strukturelle Maßnahme und daher außerhalb des Scopes dieses Read-Only-Sprints | — |
| 16 | `00_project/backlog.md` | **KEEP** | Strukturell weiterhin valides Kanban-Format gemäß `task_rules.md`; Lückenhaftigkeit der DONE-Tabelle ist ein Pflegehinweis, keine strukturelle Fehlplatzierung | — |
| 17 | `00_project/REPOSITORY_KPIS.md` | **KEEP** | Struktur (KPI-Definitionen + Messwerttabellen) ist sound; nur für B-0001/B-0002 befüllt — Pflegehinweis, keine Strukturfrage | — |
| 18 | `INDEX.md` (Root) | **KEEP** | Rolle als Einstiegsindex strukturell sinnvoll; Inhalt veraltet (verweist noch auf `codex_knowledge_model.md`, listet nur Pilot-Objekte) — Korrektur ist redaktionell | — |
| 19 | `PROJECT_BOOTSTRAP.md` (Root) | **KEEP** | Enthält in der Tabelle "Relevante Framework-Dateien" durchgehend falsche Ordnernamen (siehe Kapitel 8); Korrektur ist eine Inhaltskorrektur einer im Übrigen strukturell richtig platzierten Datei | — |

**Zusammenfassung der Klassifikation:** 2× DELETE, 4× MOVE, 1× MERGE, 5× ARCHIVE, 5× KEEP (mit Pflegehinweis), zusätzlich 1 großer, nicht in diese Tabelle gefasster Strukturvorschlag (Nummernkollision `04_synthesis`/`05_publications`, siehe Kapitel 2 und 10 — dies ist eine Umbenennung auf Architekturebene, keine Einzeldatei-Klassifikation).

---

# 5. Governance Review

Diese Bewertung betrachtet ausschließlich die **Struktur** der Governance-Dokumente — nicht die inhaltliche Richtigkeit einzelner Einträge oder Entscheidungen.

## Bestandsaufnahme der Governance-Instrumente

| Instrument | Datei | Rolle laut Selbstbeschreibung | Aktualisierungsstatus (strukturell beobachtet) |
|---|---|---|---|
| CURRENT_STATE | `CURRENT_STATE.md` | Zustandsbericht, Pflichtlektüre jeder Session | Aktiv, sehr ausführlich, wächst linear (315 Zeilen, chronologisch angehängt) |
| NEXT_ACTION | `00_project/NEXT_ACTION.md` | "Genau eine nächste Aktion" | Aktiv, aber enthält de facto ein vollständiges chronologisches Sprintprotokoll (152 Zeilen) statt einer einzelnen Aktion — Formatzweck und tatsächliche Nutzung sind auseinandergelaufen |
| SESSION_LOG | `00_project/SESSION_LOG.md` | Chronologisches Kurzprotokoll | Aktiv |
| changelog | `00_project/changelog.md` | Änderungsprotokoll | Aktiv, inhaltlich stark überlappend mit SESSION_LOG (beide protokollieren dieselben Sprints mit vergleichbarem Detailgrad) |
| OPEN_DECISIONS | `00_project/OPEN_DECISIONS.md` | Herausgeber-Entscheidungen | Aktiv, strukturell das reifste Governance-Dokument (klare OD-IDs, Status, Auflösungshistorie) |
| review_queue | `00_project/review_queue.md` | ursprünglich: Validierungs-Rückstand von Pilot 001 | Aktiv, aber im Lauf der Zeit zu einem Sammelbecken für mindestens vier verschiedene Dinge geworden: Validierungsrückstände, Fusionskandidaten, Meta-Prinzip-Kandidaten, Literaturkandidaten, "Später prüfen"-Notizen |
| decision_log | `00_project/decision_log.md` | frühe Entscheidungsprotokollierung | **Verwaist** seit 2026-06-27 (siehe Kapitel 3/4) |
| backlog | `00_project/backlog.md` | Kanban-Tasktracking | **Teilweise verwaist** — Tabellenstruktur aktiv designed, aber inkonsistent befüllt |
| roadmap | `00_project/roadmap.md` | Phasenplanung | **Verwaist**, funktional durch `SALES_CODEX_1_0_PROGRAM.md` abgelöst |
| REPOSITORY_KPIS | `00_project/REPOSITORY_KPIS.md` | Quantitativer Buchvergleich | **Teilweise verwaist** — Konzept aktiv, Datenpflege nach 2 von 15 Büchern eingestellt |
| SCIENTIFIC_DEBT | `00_project/SCIENTIFIC_DEBT.md` | Evidenzlücken-Matrix | Aktiv, laut mehreren Audits "vorbildlich" geführt |
| task_rules | `00_project/task_rules.md` | Task-Ableitungslogik | Aktiv, aber abhängig von `book_catalog.md`, das strukturell entkoppelt ist (siehe 3.2.1) |
| SALES_CODEX_1_0_PROGRAM | `00_project/SALES_CODEX_1_0_PROGRAM.md` | übergeordnetes Steuerungsdokument seit 2026-07-02 | Neu, aktiv, deklariert sich selbst als das, was `roadmap.md` einmal war |

## Überschneidungen und Redundanzen

Es lassen sich drei überlappende Cluster identifizieren:

**Cluster 1 — Prozessprotokollierung:** `SESSION_LOG.md`, `changelog.md` und `NEXT_ACTION.md` protokollieren jeweils denselben Satz an Sprintereignissen mit unterschiedlichem, aber überlappendem Detailgrad. Ein Ereignis wie der Behavioral Science Review Sprint erscheint vollständig (mit teils identischem Wortlaut) in allen drei Dateien plus zusätzlich in `CURRENT_STATE.md`. Dies ist keine Dopplung im Sinne identischer Dateien (Kapitel 6 bestätigt keine Hash-Duplikate), aber eine funktionale Redundanz, die vier separate Pflegeorte für dieselbe Information erzeugt.

**Cluster 2 — Offene-Fragen-Dokumente:** `SCIENTIFIC_DEBT.md`, `review_queue.md` und `05_research/LITERATURE_INDEX.md` verwalten je eigene, sich teils überschneidende Listen offener/unsicherer Punkte. Dieses Problem ist — bemerkenswert — bereits vom Repository selbst als OD-011 erkannt und als offene Entscheidung dokumentiert; dieser Bericht bestätigt aus rein struktureller Sicht dieselbe Beobachtung unabhängig.

**Cluster 3 — Planungsdokumente:** `roadmap.md`, `backlog.md`, `REPOSITORY_KPIS.md` und `decision_log.md` sind vier Planungs-/Tracking-Instrumente aus der Gründungsphase, von denen mindestens zwei (`roadmap.md`, `decision_log.md`) faktisch durch neuere Dokumente (`SALES_CODEX_1_0_PROGRAM.md`, `OPEN_DECISIONS.md`) abgelöst wurden, ohne dass diese Ablösung strukturell nachvollzogen (Archivierung) wurde.

## Verantwortlichkeiten

Die Rollenverteilung Mensch/KI ist über mehrere Dokumente konsistent beschrieben (`CONTRIBUTING.md`, `PROJECT_BOOTSTRAP.md`, `SALES_CODEX_OPERATING_MANUAL.md`) und widerspruchsfrei. Auffällig ist lediglich die Dokumentklassifizierungstabelle in `PROJECT_BOOTSTRAP.md` selbst: Sie stuft `review_queue.md` als "Archived" ein, obwohl die Datei nachweislich aktiv gepflegt wird (letzter belegter Eintrag: Academic Recovery Sprint Phase 2, 2026-07-01) — ein interner Widerspruch zwischen der Klassifikationsregel und ihrer eigenen Anwendung.

## Langfristige Wartbarkeit

Mit aktuell neun teils überlappenden, teils verwaisten Steuerungsdokumenten allein in `00_project/` (ohne Sprintberichte) ist die Governance-Ebene an einem Punkt, an dem jede neue Sprintart tendenziell ein weiteres Trackingdokument statt einer Erweiterung bestehender Strukturen erzeugt (`SALES_CODEX_1_0_PROGRAM.md` ist das jüngste Beispiel dieses Musters). Ohne Konsolidierung vor Version 1.0 wird diese Zahl weiter wachsen (siehe Kapitel 9).

---

# 6. Research Program Integration

Bewertet wird ausschließlich die **Repository-Integration** von `06_research_program/`, nicht die wissenschaftliche Methodik der Forschungsarbeit selbst (Inhalt von `02_SCIENTIFIC_MASTER_REVIEW.md`/`03_GEMINI_RED_TEAM_REVIEW.md` wird hier nicht bewertet).

## Speicherort und Ordnerstruktur

Der Speicherort (`06_research_program/`, getrennt von `03_knowledge_base/` und `04_book_analysis/`) ist strukturell korrekt gewählt: `06_research_program/README.md` stellt explizit fest, "Forschung ist strikt vom offiziellen Sales Codex getrennt" — die physische Trennung in einen eigenen Top-Level-Ordner setzt diese Grundregel konsequent um und verhindert, dass ungeprüfte Forschungshypothesen versehentlich mit kanonischen Wissensobjekten vermischt werden.

Die interne Gliederung (`active/`, `archived/`, `completed/`, `templates/`, mit projektspezifischen Unterordnern wie `W001/`) folgt demselben Lifecycle-Muster wie `book_catalog.md` (WAITING/IN_PROGRESS/DONE) und ist als Konzept skalierbar: Ein `W002`, `W003` usw. ließe sich ohne strukturelle Änderung ergänzen.

## Auffälligkeit: Skelettstatus der Struktur

Von 16 Dateien in `06_research_program/` enthalten 14 lediglich 1–3 Zeilen Inhalt — darunter sämtliche fünf Dateien im `templates/`-Ordner (`DECISION_BRIEF_TEMPLATE.md`, `EDITOR_DECISION_TEMPLATE.md`, `RED_TEAM_TEMPLATE.md`, `RESEARCH_PROJECT_TEMPLATE.md`, `THEORY_LANDSCAPE_TEMPLATE.md`, je 20–28 Byte) sowie vier der acht Dateien im aktiven Projekt `W001/` (`README.md`, `01_INITIAL_HYPOTHESIS.md`, `04_THEORY_LANDSCAPE.md`, `05_DECISION_BRIEF.md`, `06_EDITOR_DECISION.md`, `OPEN_QUESTIONS.md`, `REFERENCES.md`, `RESEARCH_LOG.md` — davon sind `04_THEORY_LANDSCAPE.md`, `05_DECISION_BRIEF.md`, `06_EDITOR_DECISION.md` durchgehend 3-zeilige Platzhalter). Nur zwei Dateien (`02_SCIENTIFIC_MASTER_REVIEW.md`, 330 Zeilen; `03_GEMINI_RED_TEAM_REVIEW.md`, 290 Zeilen) enthalten tatsächlich ausgearbeiteten Inhalt.

**Wichtiger Hinweis zur Unsicherheit:** Der Auftrag für diesen Sprint nennt "Theory Assessment Framework (TAF)" als eine der bereits abgeschlossenen Entwicklungsphasen des Repository. Eine gezielte repositoryweite Suche (auch nach der Abkürzung "TAF") ergab **keinen einzigen Treffer** — weder als Dateiname noch als Textstelle in irgendeiner der 683 Markdown-Dateien. Der inhaltlich naheliegendste Baustein im Repository ist die "Theory Landscape" innerhalb des `06_research_program`-Workflows (`RESEARCH_GOVERNANCE.md`: *"Hypothesen -> Reviews -> Theory Landscape -> Decision Brief -> Editor Decision"*; Datei `templates/THEORY_LANDSCAPE_TEMPLATE.md` sowie `active/W001/04_THEORY_LANDSCAPE.md`). Ob "TAF" ein außerhalb dieses Repositorys geführtes Konzept ist, eine geplante, aber noch nicht angelegte Datei, oder eine andere Bezeichnung für die "Theory Landscape"-Stufe — lässt sich aus dem Repository-Zustand nicht auflösen. Dies wird hier als Unsicherheit dokumentiert, nicht als Annahme aufgelöst.

## Skalierbarkeit

Als Ordnerkonzept ist `06_research_program/` gut auf mehrere gleichzeitig laufende Forschungsprojekte vorbereitet (`active/`, `archived/`, `completed/` mit `W`-präfigierten Einzelordnern). Der praktische Engpass liegt nicht in der Struktur, sondern im Füllstand: Mit nur einem Projekt (`W001`) und einer noch nicht in Breite erprobten Governance-Kette (`DECISION_POLICY.md`: *"Nur Editor Decisions erlauben eine Übernahme in den Codex"* — ein Satz ohne begleitendes Verfahren) lässt sich noch nicht beurteilen, ob die vorgesehene Fünf-Stufen-Kette (Hypothese → Reviews → Theory Landscape → Decision Brief → Editor Decision) in der Praxis trägt, sobald mehrere `W`-Projekte parallel laufen.

## Langfristige Wartbarkeit — Empfehlung (nur dokumentiert, nicht umgesetzt)

Vor einer Skalierung auf mehrere parallele Forschungsprojekte sollte geklärt werden, ob die noch leeren Governance-Dateien (`README.md`, `RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md`, `RESEARCH_STATUS.md`) bewusst minimalistisch gehalten sind oder unvollständige Platzhalter, die vor einer Verdopplung der Forschungsprojekte ausformuliert werden müssten. Diese Frage kann dieser Bericht nicht beantworten — sie ist eine Herausgeber-Entscheidung, keine strukturelle Feststellung.

---

# 7. Repository Hygiene

| Datei/Ordner | Befund | Klassifikation | Begründung |
|---|---|---|---|
| `04_book_analysis/Emotional Intelligence/test_probe.md` | 0 Byte, leere Debug-Datei | **DELETE** | Vom B-0011-Subagenten versehentlich hinterlassen; bereits in `SESSION_LOG.md` und `changelog.md` als bekanntes Housekeeping-Item vermerkt, konnte laut dortiger Notiz bislang nicht automatisiert entfernt werden |
| `04_book_analysis/Never_Split_The_Difference/` | leerer Duplikat-Ordner | **DELETE** | Siehe Kapitel 2/4 |
| `02_sources/articles/`, `interviews/`, `other/`, `podcasts/`, `studies/` | leer | **KEEP** | Vorbereitete, noch nicht genutzte Quellkategorien — kein Hygieneproblem |
| `03_knowledge_base/competencies/`, `meta_models/`, `observations/` | leer | **KEEP** | Im Framework definierte, aber bislang nicht befüllte Objektkategorien — Wissensmodell sieht sie explizit vor (`README.md` Zeile 23) |
| `05_publications/sales_codex_book/`, `talks/`, `trainings/`, `workbook/` | leer | **KEEP** | Vorbereitete Struktur für spätere Phase (siehe `roadmap.md` Phase 4) |
| `06_media/diagrams/`, `images/`, `mindmaps/` | leer | **KEEP** | Vorbereitete Struktur, kein Inhalt bislang erwartet |
| `06_research_program/archived/`, `completed/` | leer | **KEEP** | Erwartungsgemäß leer — es wurde noch kein Forschungsprojekt abgeschlossen oder archiviert |
| `07_scripts/` | nur README, keine Skripte | **KEEP** | Explizit als Platzhalter für "spätere Automatisierungen" beschrieben |
| `99_archive/` | nur README, keine archivierten Inhalte | **KEEP** | Struktur vorbereitet; die in diesem Bericht unter Kapitel 4 vorgeschlagenen ARCHIVE-Ziele wären die ersten tatsächlichen Belegungen |
| `02_sources/books/` — 17 unverarbeitete Rohquellen mit Downloadquellen-Dateinamen | inkonsistente Benennung, kein Verarbeitungsstatus erkennbar | **KEEP** | Legitimes Rohmaterial-Backlog, kein Fehler — aber siehe Kapitel 10 für eine Strukturempfehlung (Sub-Kategorisierung "verarbeitet" vs. "Backlog") |
| Keine gefundenen exakten Datei-Duplikate | MD5-Prüfung aller 683 Markdown-Dateien ergab **keine** zwei inhaltsgleichen Dateien | — | Positivbefund — keine Handlungsnotwendigkeit |
| Keine `.gitkeep`-Dateien in leeren Ordnern | 18 leere Ordner sind nicht durch Platzhalterdateien versioniert | **Hinweis, kein Klassifikationsfall** | Da Git leere Verzeichnisse nicht nativ verfolgt, hängt der Fortbestand dieser vorbereiteten Struktur vom lokalen Dateisystem ab, nicht vom Git-Verlauf — bei einem Klon des Repositorys über Git würden alle 18 leeren Ordner nicht mit übertragen. Rein strukturelle Beobachtung, keine Handlungsempfehlung im Rahmen dieses Sprints. |

**Zusammenfassung:** Zwei tatsächliche Hygiene-Fälle (beide bereits vom Repository selbst erkannt), keine verwaisten Binärdateien, keine doppelten Markdown-Inhalte, keine "vergessenen" Testdateien außer der einen bekannten. Das Repository ist in der Fläche bemerkenswert sauber — die Befunde konzentrieren sich auf wenige, bereits identifizierte Punkte.

---

# 8. Cross Reference Audit

## Methodik

Da im gesamten Repository **keine einzige** Markdown-Hyperlink-Syntax (`[Text](Pfad.md)`) verwendet wird — alle internen Verweise erfolgen als reiner Text in Backticks, z. B. `` `00_project/CURRENT_STATE.md` `` — wurden alle 165 auf diese Weise referenzierten `.md`-Pfade extrahiert und gegen das tatsächliche Dateisystem geprüft.

**Strukturelle Grundfeststellung:** Da keines dieser Verweise ein klickbarer Link ist, kann kein Tooling und kein Leseprogramm eine tote Referenz automatisch anzeigen — jede Inkonsistenz bleibt unsichtbar, bis sie zufällig beim Lesen auffällt. Dies ist selbst ein struktureller Befund (siehe Kapitel 10, Refactoring-Empfehlung zu automatisierter Link-Prüfung über `07_scripts/`).

## Befunde: fehlerhafte/tote Referenzen

| Referenzierender Pfad | Referenzierter (nicht existierender) Pfad | Einordnung |
|---|---|---|
| `00_project/POST_MORTEM_B0002.md`, Zeile 220 | `04_book_analysis/Influence/VAL-0002.md` | **Keine tote Referenz im klassischen Sinn** — die Datei wird als *Ziel einer Korrekturempfehlung* genannt ("Konsistenter wäre …"), nicht als bestehender Verweis. Bestätigt aber unabhängig den in Kapitel 3/4 dokumentierten Fehlplatzierungsbefund von VAL-0002. |
| `00_project/task_proposal_B-0002_influence.md`, Zeile 328 | `00_project/ABSCHLUSSBERICHT_B-0002_influence.md` | Im Vorschlag genannter, geplanter Ausgabepfad; tatsächlich realisiert wurde stattdessen `04_book_analysis/Influence/BOOK_REVIEW_REPORT_B0002.md`. Historisches Artefakt einer nicht weiterverfolgten Namenskonvention — keine aktive tote Referenz, da das Quelldokument selbst archivierungswürdig ist (siehe Kapitel 4). |
| `04_book_analysis/Nudge/CANONICALIZATION_REPORT_B0013.md`, Zeile 137 | `peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md` (ohne `00_project/`-Präfix) | Unvollständiger Pfad — die Datei existiert tatsächlich unter `00_project/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`. Der fehlende Präfix macht die Referenz bei wörtlicher Pfadauflösung ungültig. |

## Befund: Verweis auf nicht existierenden internen Anker

`04_book_analysis/Nudge/CANONICALIZATION_REPORT_B0013.md` (Zeile 137) verweist zusätzlich auf einen Abschnitt **"SD-SYS-004"** in `SCIENTIFIC_DEBT.md`. Eine gezielte Prüfung von `00_project/SCIENTIFIC_DEBT.md` ergab: Eine Überschrift `SD-SYS-004` existiert in dieser Datei **nicht** (0 Treffer bei direkter Suche), obwohl mindestens fünf weitere Dateien (`ACADEMIC_RECOVERY_PLAN.md`, `CODEX_AUDIT_2026-07.md`, `SALES_CODEX_1_0_PROGRAM.md`, `SESSION_LOG.md`, `peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`) auf diese Kennung verweisen. Der `CANONICALIZATION_REPORT_B0013.md`-Autor hat diese Lücke bereits selbst entdeckt und explizit dokumentiert ("… jedoch ohne einen eigenen `#### SD-SYS-004`-Überschriftenabschnitt in `SCIENTIFIC_DEBT.md` selbst … hiermit zur Kenntnis dokumentiert und an eine höhere Sprint-Ebene zur Bereinigung weitergegeben, nicht eigenständig repariert"). Dieser Bericht bestätigt den Befund unabhängig und markiert ihn hiermit erneut als weiterhin offen.

## Befund: Isolierte falsche Pfadangaben in `PROJECT_BOOTSTRAP.md`

Die Tabelle "Relevante Framework-Dateien" in `PROJECT_BOOTSTRAP.md` (Zeilen 137–143) referenziert sechs Ordnerpfade, die mit der tatsächlichen `01_framework/`-Struktur nicht übereinstimmen:

| Referenziert in PROJECT_BOOTSTRAP.md | Tatsächlicher Ordnername |
|---|---|
| `01_framework/01_project_charter/` | `01_framework/00_charter/` |
| `01_framework/02_methodology/` | `01_framework/01_methodology/` |
| `01_framework/03_evidence_system/` | `01_framework/02_evidence_system/` |
| `01_framework/04_source_standards/` | `01_framework/03_source_standard/` |
| `01_framework/05_extraction_standards/` | `01_framework/04_principle_extraction/` |
| `01_framework/06_knowledge_model/` | `01_framework/05_knowledge_model/` |

Alle sechs Zeilen sind sowohl in der Nummerierung als auch teilweise im Namen falsch. Diese Tabelle scheint aus einer früheren, nie umgesetzten oder seither umbenannten Ordnerplanung übernommen und nicht aktualisiert worden zu sein. Diese Diskrepanz ist isoliert auf `PROJECT_BOOTSTRAP.md` beschränkt — keine andere Datei im Repository übernimmt diese falschen Pfade (bestätigt durch repositoryweite Suche).

## Befund: veralteter Verweis in `INDEX.md`

`INDEX.md` (Zeile 21) verweist auf `01_framework/05_knowledge_model/codex_knowledge_model.md` als das zu lesende Wissensmodell-Dokument. Der Pfad selbst ist gültig (die Datei existiert), aber inhaltlich veraltet: Seit dem Consistency Correction Sprint 2026-07 ist `canonical_knowledge_model.md` die maßgebliche Quelle (siehe Kapitel 3.4). `INDEX.md` wurde seit der Ersteinrichtung des Projekts (2026-06-27, laut Inhalt "Erste Wissensobjekte" mit ausschließlich Pilot-001-Referenzen) nicht mit dem seitherigen Wachstum synchronisiert.

## Konsistenz der Benennungen

Über alle geprüften Querverweise hinweg ist die ID-Nomenklatur (SRC-/ST-/A-/MEC-/P-/T-/MOD-/VAL-/B-/OD-/SD-/W-) durchgängig konsistent verwendet — keine Falschschreibungen oder Kollisionen bei Objekt-IDs wurden festgestellt. Die Inkonsistenzen betreffen ausschließlich Datei-/Ordnerpfade, nicht das ID-System selbst.

---

# 9. Architecture Review

**Leitfrage:** Ist die aktuelle Architektur geeignet, doppelt so viele Bücher (30 statt 15), doppelt so viele Wissensobjekte (~1.030 statt 514) und doppelt so viele Research-Projekte (2 statt 1, absehbar mehr) ohne strukturelle Probleme aufzunehmen?

**Antwort: Nein, nicht ohne vorherige Korrektur der in diesem Bericht dokumentierten Befunde.** Die Architektur selbst (Nummernschema, ID-System, Objekthierarchie) ist im Grundsatz tragfähig für diese Größenordnung — das eigentliche Risiko liegt nicht in der Konzeption, sondern darin, dass mehrere bereits bei 15 Büchern sichtbar gewordene Symptome sich bei Verdopplung nicht linear, sondern strukturell verschärfen würden.

## Konkrete Architekturprobleme bei Verdopplung

**1. `00_project/` als flaches Verzeichnis.** Aktuell 36 Dateien plus ein Unterordner. Bei einer Verdopplung der Sprintaktivität (jeder bisherige Sprinttyp — Book Mode, Academic Recovery, Peer Review, Consistency Correction, Governance — hat mindestens einen eigenen Bericht erzeugt) ist mit 60–70 Dateien in diesem einen Verzeichnis zu rechnen, weiterhin ohne Unterordnung nach Typ. Ein Verzeichnis dieser Größe ohne Substruktur ist für Menschen nicht mehr auf einen Blick erfassbar und für KI-Sessions bei "nur die direkt betroffenen Arbeitsdateien lesen" (`PROJECT_BOOTSTRAP.md`, Arbeitsprinzip 1) zunehmend schwerer gezielt navigierbar.

**2. Flache Objektordner in `03_knowledge_base/`.** `statements/` enthält bereits 309 Dateien in einem einzigen Verzeichnis ohne Unterindex nach Buch, Thema oder Zeitraum — Navigation erfolgt ausschließlich sequenziell über die ID. Bei einer Verdopplung auf ca. 600+ Statements (und entsprechend auf `principles/`, `assumptions/`, `techniques/`) wird dieses Verzeichnis für keine Form der manuellen Sichtung mehr praktikabel; die einzige Erschließung bleibt eine gezielte ID- oder Volltextsuche. Dies ist im aktuellen Umfang bereits grenzwertig und bei doppeltem Umfang ein echtes Navigationsproblem, das die Architektur in ihrer jetzigen Form nicht adressiert (kein Index, kein Tagging, kein Unterordner-Schema nach Quelle).

**3. `book_catalog.md` als Wachstumsbremse.** Der Katalog ist für 40 vorgemerkte Bücher angelegt, aber bereits bei 15 verarbeiteten Büchern (37,5 % des vorgesehenen Umfangs) vollständig von der Realität entkoppelt (siehe 3.2.1). Eine Verdopplung auf 30 Bücher unter unveränderten Bedingungen würde bedeuten, dass die für automatisierte Steuerung vorgesehene Infrastruktur (`task_rules.md`) durchgehend auf Basis veralteter Daten arbeiten müsste oder — wie tatsächlich geschehen — schlicht umgangen und durch manuelle Steuerung über `CURRENT_STATE.md`/`NEXT_ACTION.md` ersetzt wird. Bei 30 Büchern wird der Koordinationsaufwand für rein manuelle, unstrukturierte Steuerung (wie aktuell praktiziert) ohne belastbaren Katalog spürbar höher.

**4. Nummernschema mit bereits zwei Kollisionen.** Ein einstufiges, zweistelliges Präfixschema (`00`–`07`, `99`) hat aktuell noch ungenutzte Nummern (`08`–`98`) für neue Top-Level-Kategorien übrig — das Schema selbst ist also nicht erschöpft. Das eigentliche Problem ist die bereits zweimal beobachtete Governance-Lücke: Neue Ordner wurden ohne Prüfung gegen bestehende Nummern angelegt. Ohne eine einfache Regel ("vor Anlage eines neuen Top-Level-Ordners: Nummernkollision prüfen") wird sich dieses Muster bei doppelter Aktivität mit höherer Wahrscheinlichkeit wiederholen, nicht seltener auftreten.

**5. Research-Programm-Skalierung ungetestet.** Mit aktuell einem einzigen Forschungsprojekt (`W001`) ist unklar, ob die Governance-Kette (Hypothese → Reviews → Theory Landscape → Decision Brief → Editor Decision) bei mehreren parallelen `W`-Projekten mit unterschiedlichem Reifegrad tragfähig ist — insbesondere, da `RESEARCH_STATUS.md` aktuell nur ein einzelnes Statusfeld für ein Projekt vorsieht ("W-001: ACTIVE"), nicht erkennbar eine Tabellenstruktur für mehrere gleichzeitige Projekte.

**6. Buchordner-Namenskonvention nicht automatisierungsfreundlich.** Ordnernamen mit Leerzeichen und einem Komma (`Thinking, Fast and Slow/`) funktionieren in interaktiver Nutzung, sind aber in Skript-/Automatisierungskontexten (vorgesehen für `07_scripts/`) eine wiederkehrende Fehlerquelle. Bei 30 statt 15 Büchern vervielfacht sich die Zahl der Sonderfälle, die jedes künftige Skript individuell behandeln müsste.

## Was an der Architektur bereits gut auf Skalierung vorbereitet ist

Das ID-System (SRC-/ST-/A-/MEC-/P-/T-/MOD-Nummern) ist inhärent unbegrenzt skalierbar und hat bei 514 Objekten keine einzige Kollision oder Lücke gezeigt. Der Ordner-je-Buch-Ansatz in `04_book_analysis/` skaliert strukturell beliebig (ein neuer Ordner pro Buch). Die Trennung Rohquelle/Wissensobjekt/Buchanalyse/Synthese bleibt bei doppeltem Umfang konzeptionell unverändert tragfähig.

---

# 10. Repository Refactoring Opportunities

| # | Beschreibung | Nutzen | Risiko | Aufwand | Priorität |
|---|---|---|---|---|---|
| 1 | Nummernkollision auflösen: `04_synthesis/` → `05_synthesis/`, `05_research/`-Inhalt in `06_research_program/` mergen, danach `06_media/` → `07_media/`, `06_research_program/` → `08_research_program/`, `07_scripts/` → `09_scripts/` (oder alternative Minimallösung: nur die zwei kollidierenden Paare umbenennen, ohne Kaskade) | Eindeutiges, wieder sortierbares Nummernschema; Grundlage für jede künftige Automatisierung | Hoher Umstellungsaufwand bei Kaskadenvariante; viele Pfadverweise müssten angepasst werden (siehe Kapitel 8) | Hoch (Kaskade) / Mittel (Minimallösung) | HOCH |
| 2 | `book_catalog.md` inhaltlich mit tatsächlichem Buchbestand synchronisieren oder explizit als "nicht aktuell gepflegt, siehe CURRENT_STATE.md" kennzeichnen | Verhindert Fehlsteuerung bei künftiger (teil-)automatisierter Task-Generierung gemäß `task_rules.md` | Gering — reine Redaktionsarbeit | Mittel | HOCH |
| 3 | `00_project/` in Unterordner gliedern (z. B. `governance/`, `sprints/`, `reports/`) analog zum bereits bestehenden `peer_review/decisions/`-Muster | Erhält Übersichtlichkeit bei weiterem linearem Wachstum der Sprintberichte | Alle referenzierenden Pfadangaben (siehe Kapitel 8-Methodik) müssten mitgeführt werden | Mittel | MITTEL |
| 4 | Vier Onboarding-Dokumente (`INDEX.md`, `PROJECT_BOOTSTRAP.md`, `CLAUDE_BOOTSTRAP.md`, `SETUP.md`) auf ein einziges, maßgebliches Dokument konsolidieren; übrige archivieren oder als Spezialfall kennzeichnen | Beseitigt eine bereits selbst im Repository (`review_queue.md`) erkannte Inkonsistenz; reduziert Einstiegsreibung für neue Sessions/Menschen | Gering, sofern eine Fassung klar als maßgeblich benannt wird | Gering–Mittel | HOCH |
| 5 | `codex_knowledge_model.md` nach `99_archive/` verschieben (Editor-Entscheidung bereits in `SALES_CODEX_1_0_PROGRAM.md` als offen benannt) | Beseitigt aktive Dublette im Kernframework-Ordner | Sehr gering | Gering | HOCH |
| 6 | Erste tatsächliche Nutzung von `99_archive/` (aktuell 0 Inhalte trotz vorbereiteter Struktur) — mit den in Kapitel 4 vorgeschlagenen ARCHIVE-Kandidaten befüllen | Archiv erfüllt erstmals seinen deklarierten Zweck; entlastet aktive Verzeichnisse | Sehr gering | Gering | MITTEL |
| 7 | Sub-Indexierung von `03_knowledge_base/statements/` (309 Dateien) — z. B. eine generierte Übersichtsdatei pro Quelle/Kategorie, ohne die flache ID-Ablage selbst zu verändern | Adressiert das in Kapitel 9 identifizierte größte Skalierungsrisiko der Wissensebene, bevor es bei 600+ Dateien akut wird | Gering, sofern rein additiv (Indexdatei statt Restrukturierung) | Mittel | MITTEL |
| 8 | Buchordner-Benennung vereinheitlichen (`SPIN_Selling` → `SPIN Selling`, oder umgekehrt alle 14 auf Unterstrich-Konvention) | Konsistenz, Automatisierungsfreundlichkeit für `07_scripts/` | Betrifft viele Querverweise (Kapitel 8) | Mittel | NIEDRIG |
| 9 | `02_sources/books/` in verarbeitete Quellen vs. Rohmaterial-Backlog trennen (z. B. Statusspalte in `book_catalog.md` statt neuer Ordner, um Strukturwachstum zu vermeiden) | Schafft Transparenz über 17 aktuell unklar zugeordnete Rohdateien | Gering | Mittel | NIEDRIG |
| 10 | Automatisierte Cross-Reference-Prüfung als erstes Skript in `07_scripts/` (prüft Backtick-Pfadverweise gegen tatsächliche Dateiexistenz) | Verhindert künftige tote Referenzen wie in Kapitel 8 dokumentiert, ohne manuelle Audits wie diesen zu benötigen | Keines (additives Tooling) | Mittel | MITTEL |
| 11 | Governance-Cluster konsolidieren: `decision_log.md` und `roadmap.md` archivieren (bereits funktional abgelöst), `SESSION_LOG.md`/`changelog.md`-Überlappung klären (ggf. eine Datei als Kurzform, andere als Volltext definieren) | Reduziert Pflegeorte für dieselbe Information von vier auf effektiv zwei | Gering | Mittel | MITTEL |
| 12 | `06_research_program/`-Platzhalterdateien entweder ausformulieren oder explizit als bewusst minimal kennzeichnen (Herausgeber-Entscheidung) | Klärt, ob die Struktur für ein zweites Forschungsprojekt (`W002`) bereit ist oder erst noch ausgearbeitet werden muss | Keines (reine Klärung) | Gering | MITTEL |

---

# 11. Release Candidate Assessment

**Frage:** Ist die Repository-Struktur geeignet, als Release Candidate RC-1 eingefroren zu werden?

**Bewertung: Noch nicht — es bestehen konkrete strukturelle Blocker.** Ein "Freeze" impliziert, dass die Ordnerhierarchie, das Nummernschema und die Governance-Ablage ab diesem Punkt als stabile Grundlage gelten, auf der weiteres Wachstum aufsetzt. Mehrere der in diesem Bericht dokumentierten Befunde sind genau diejenigen Eigenschaften, die ein Freeze *nicht* einfrieren sollte, weil sie bereits als fehlerhaft/unvollständig bekannt sind.

## Strukturelle Blocker (keine Forschungsblocker)

1. **Nummernkollision `04_*`/`05_*` (Kapitel 2, 10).** Ein RC-Status sollte kein Nummernschema einfrieren, das bereits zwei Kollisionen enthält — jede künftige Erweiterung würde auf einer bekannt inkonsistenten Basis aufsetzen.

2. **`book_catalog.md` strukturell entkoppelt von der Realität (Kapitel 3.2.1).** Ein RC-Freeze der Governance-Architektur ist nicht sinnvoll, solange das laut eigener Dokumentation zentrale Steuerungsinstrument der Task-Generierung seit 13 von 15 Büchern nicht mehr benutzbar ist, ohne dass diese Ablösung irgendwo festgehalten wurde.

3. **Vier widersprüchliche Onboarding-Dokumente (Kapitel 3.3).** Ein RC sollte eine einzige, eindeutige Prozedur für den Sitzungseinstieg definieren. Aktuell existieren vier voneinander abweichende Vorgaben plus eine fünfte, wiederum abweichende Kurzform in `CURRENT_STATE.md` selbst.

4. **Bereits selbst erkannte, aber nicht behobene Hygienepunkte (leerer Duplikat-Ordner, `test_probe.md`, `codex_knowledge_model.md`, VAL-0001/VAL-0002-Fehlplatzierung).** Ein Freeze sollte nicht bekannte, dokumentierte Defekte in die eingefrorene Baseline übernehmen, wenn deren Behebung nachweislich risikoarm ist (Kapitel 4, 7).

5. **Unklare Abschlussreife von `06_research_program/` (Kapitel 6).** Da unklar ist, ob die 14 Platzhalterdateien bewusst minimal oder unvollständig sind, kann eine Struktur-Einfrierung an dieser Stelle versehentlich einen unfertigen Zustand kanonisieren.

6. **Fehlende automatisierte Cross-Reference-Prüfung (Kapitel 8).** Ohne ein Mindestmaß an Verweisprüfung (und sei es nur ein einfaches Skript) wird jede künftige Umbenennung — inklusive der für RC-1 selbst nötigen Korrekturen — neue tote Referenzen erzeugen können, ohne dass dies auffällt.

## Was einem Freeze nicht entgegensteht

Das Kernschema (00–07, 99), das ID-System der Wissensobjekte, die Trennung der Verarbeitungsstufen und die Objekt-Templates in `01_framework/08_templates/` sind strukturell reif und müssen für RC-1 nicht verändert werden. Die inhaltliche/wissenschaftliche Reife (Reifegrad B+, W-001 ungelöst usw.) ist explizit **kein** Gegenstand dieser Bewertung — das ist Aufgabe von `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` und liegt außerhalb des Scopes dieses rein strukturellen Sprints.

---

# 12. Consolidation Roadmap

## Kategorie A — Vor RC-1 zwingend

1. Nummernkollision `04_book_analysis`/`04_synthesis` und `05_publications`/`05_research` auflösen (mindestens Minimallösung: `05_research/LITERATURE_INDEX.md` nach `06_research_program/` verschieben, `04_synthesis/` umbenennen oder `04_book_analysis/` und `04_synthesis/` unter einem gemeinsamen `04_`-Elternordner zusammenführen — Entscheidung liegt beim Herausgeber).
2. `book_catalog.md` mit dem tatsächlichen Buchbestand (B-0001 bis B-0015, korrekte Titel, korrekte Status) synchronisieren oder explizit als nicht-autoritativ kennzeichnen, mit Verweis auf `CURRENT_STATE.md` als tatsächliche Quelle der Wahrheit.
3. Leeren Duplikat-Ordner `04_book_analysis/Never_Split_The_Difference/` entfernen (bereits herausgeberseitig zur Entscheidung anhängig).
4. `test_probe.md` entfernen (bereits herausgeberseitig zur Entscheidung anhängig).
5. Vier Onboarding-Dokumente auf eine widerspruchsfreie, einheitlich referenzierte Reihenfolge konsolidieren.
6. `PROJECT_BOOTSTRAP.md`s fehlerhafte Framework-Pfadtabelle korrigieren (Kapitel 8).
7. `codex_knowledge_model.md`-Verbleib entscheiden (Archiv vs. Löschung vs. bewusster Verbleib) — bereits als offener Punkt in `SALES_CODEX_1_0_PROGRAM.md` benannt.

## Kategorie B — Vor Version 1.0 sinnvoll

1. `00_project/` in Typ-Unterordner gliedern (Governance/aktiv, Sprintberichte/historisch, analog zum bereits bestehenden `peer_review/decisions/`-Muster).
2. VAL-0001 und VAL-0002 sowie `PILOT_001_ABSCHLUSSBERICHT.md` in die jeweiligen Buchordner verschieben.
3. `SCRP-0001_Sales_Core.md` von der Root-Ebene in eine Peer-Review-Governance-Struktur verschieben.
4. `decision_log.md`, `roadmap.md`, `task_proposal_B-0002_influence.md`, `CLAUDE_BOOTSTRAP.md`, `SETUP.md` archivieren (`99_archive/` damit erstmals tatsächlich genutzt).
5. Governance-Cluster konsolidieren (`SESSION_LOG.md`/`changelog.md`-Überlappung klären; Verhältnis `SCIENTIFIC_DEBT.md`/`review_queue.md`/`LITERATURE_INDEX.md` gemäß der bereits offenen OD-011 klären).
6. Buchordner-Benennung vereinheitlichen (Leerzeichen vs. Unterstrich, Kommabehandlung).
7. `06_research_program/`-Platzhalterdateien ausformulieren oder bewusst als minimal kennzeichnen.
8. SD-SYS-004-Referenz in `SCIENTIFIC_DEBT.md` auflösen (Abschnitt anlegen oder alle fünf verweisenden Stellen korrigieren).

## Kategorie C — Nach Version 1.0

1. Sub-Indexierung von `03_knowledge_base/statements/` und anderen umfangreichen flachen Objektordnern.
2. Erstes Automatisierungsskript in `07_scripts/`: Cross-Reference-Prüfung (Backtick-Pfade gegen Dateiexistenz).
3. `02_sources/books/` inhaltlich nach verarbeitet/Backlog kennzeichnen (ohne notwendigerweise neue Ordner anzulegen).
4. Klärung, ob `06_research_program/` bei mehreren parallelen `W`-Projekten eine tabellarische Statusübersicht (statt Einzeiler in `RESEARCH_STATUS.md`) benötigt.
5. Evaluierung eines Tag-/Themen-basierten Navigationsmechanismus für die Wissensbasis bei fortgesetztem Wachstum über 1.000 Objekte hinaus.

---

# Abschluss

## Gesamtbewertung der Repository-Architektur

Solide, gut konzipierte Grundarchitektur mit gepflegter, disziplinierter Wissensobjekt-Ebene — aber mit einer Governance- und Nummernschicht, die dem inhaltlichen Wachstum nicht durchgehend gefolgt ist. Die Selbstprüfungskultur des Projekts ist eine echte Stärke: Ein bemerkenswerter Anteil der hier dokumentierten Befunde war bereits vom Repository selbst erkannt, aber mangels Konsolidierungssprint nie in tatsächliche Struktur-Korrektur überführt worden. Dieser Bericht bündelt diese verstreuten Selbstbeobachtungen erstmals an einem Ort und ergänzt sie um eigenständig geprüfte Befunde (insbesondere die vollständige Divergenz von `book_catalog.md`, die vier widersprüchlichen Onboarding-Dokumente und die tote Referenz auf SD-SYS-004).

## Klassifikationsstatistik (Kapitel 4)

| Kategorie | Anzahl |
|---|---|
| KEEP (mit Pflegehinweis) | 5 |
| MERGE | 1 |
| MOVE | 4 |
| RENAME | 0 (Umbenennungen betreffen ausschließlich Ordner-Ebene, siehe Kapitel 2/10 — keine Einzeldatei-RENAME identifiziert) |
| ARCHIVE | 5 |
| DELETE | 2 |

## Die fünf wichtigsten strukturellen Maßnahmen vor RC-1

1. Nummernkollision auf oberster Ebene auflösen (`04_book_analysis`/`04_synthesis`, `05_publications`/`05_research`).
2. `book_catalog.md` mit der Repository-Realität synchronisieren oder explizit als nicht-autoritativ kennzeichnen — der gravierendste Einzelbefund dieses Berichts.
3. Die vier widersprüchlichen Onboarding-Dokumente auf eine eindeutige Sitzungseinstiegsprozedur konsolidieren.
4. Die bereits selbst erkannten, aber unerledigten Hygienepunkte abschließen (Duplikat-Ordner, `test_probe.md`, `codex_knowledge_model.md`, VAL-0001/VAL-0002-Platzierung).
5. `PROJECT_BOOTSTRAP.md`s fehlerhafte Framework-Pfadtabelle korrigieren, um die Root-Ebene als verlässlichen Einstiegspunkt zu bestätigen.

---

*Dieser Bericht wurde ausschließlich lesend erstellt. Keine Repository-Datei wurde verändert, verschoben, umbenannt, archiviert oder gelöscht. Alle in Kapitel 4, 7, 10 und 12 genannten Maßnahmen sind Empfehlungen zur Herausgeber-Entscheidung, keine durchgeführte