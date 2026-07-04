# Research Program Review — RC-1

**Dokumentklasse:** Audit / Reference
**Sprint:** Research Program Finalization Sprint, Phase 1 — Architecture Review
**Auditor:** KI-Redaktion Sales Codex, Rolle: Architektur- und Governance-Prüfer
**Stichtag:** 2026-07-02
**Methodik:** Ausschließlich lesende, strukturelle Analyse des vollständigen Ordners `06_research_program/` (16 Dateien) sowie seiner Anbindung an das übrige Repository. Keine Datei wurde verändert. Es wurden keine neuen Theorien, keine neuen Wissensobjekte, keine Literaturrecherche und keine Frameworkänderungen vorgenommen.
**Explizites Nicht-Ziel:** Wissenschaftliche Bewertung der Inhalte von W-001 (Socio-Cognitive Sensegiving Model, konkurrierende Hypothesen, Red-Team-Kritik). Dieser Bericht bewertet ausschließlich die Architektur, Dokumentenstruktur, Prozesslogik und Governance des Research Programs — nicht, ob das SCSM wissenschaftlich korrekt ist oder ob die Red-Team-Kritik daran zutrifft. Wo Inhalte von W-001 erwähnt werden, dient dies ausschließlich der strukturellen Einordnung (z. B. "erreichen zwei Dokumente einen gegensätzlichen Befund, ohne dass eine nachgelagerte Stufe dies verarbeitet" ist eine Prozessbeobachtung, keine Inhaltsbewertung).

---

## Bestandsaufnahme (Grundlage aller folgenden Kapitel)

`06_research_program/` umfasst 19 Markdown-Dateien in vier Bereichen: vier programmweite Governance-Dokumente (`README.md`, `RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md`, `RESEARCH_STATUS.md`), fünf Templates (`templates/`), das einzige aktive Forschungsprojekt `active/W001/` (10 Dateien) sowie zwei leere Lifecycle-Ordner (`archived/`, `completed/`).

**Zentraler struktureller Befund, der praktisch jedes folgende Kapitel prägt:** Von den 19 Dateien enthalten **17 (89,5 %) ausschließlich eine ein- bis dreizeilige Titelzeile ohne inhaltliche Substanz** — darunter alle vier Governance-Dokumente und alle fünf Templates. Nur zwei Dateien sind tatsächlich ausgearbeitet: `active/W001/02_SCIENTIFIC_MASTER_REVIEW.md` (330 Zeilen) und `active/W001/03_GEMINI_RED_TEAM_REVIEW.md` (290 Zeilen). Diese extreme Schieflage zwischen Governance-Anspruch und Governance-Substanz ist die Wurzel der meisten in diesem Bericht dokumentierten Befunde.

---

# 1. Gesamtarchitektur

## Vollständigkeit

Unvollständig. Die vier Governance-Dokumente definieren zusammen nur einen einzigen Satz Prozessschritte (`RESEARCH_GOVERNANCE.md`: *"Hypothesen -> Reviews -> Theory Landscape -> Decision Brief -> Editor Decision"*) und eine einzige Entscheidungsregel (`DECISION_POLICY.md`: *"Nur Editor Decisions erlauben eine Übernahme in den Codex."*). Es fehlen: Rollendefinitionen, Abbruchbedingungen, Qualitätskriterien für jede Stufe, ein Eskalationspfad, eine Definition von "abgeschlossen" je Stufe, sowie jede Beschreibung, wie ein Forschungsprojekt physisch von `active/` nach `completed/` oder `archived/` wandert (Kriterium? Wer entscheidet? Vergleichbar mit der sehr expliziten Statuslogik in `02_sources/book_catalog.md`/`task_rules.md` für Buchanalysen — dort existiert eine vollständige Zustandsmaschine, hier keine).

## Konsistenz

Die vorhandenen vier Sätze sind untereinander widerspruchsfrei: `RESEARCH_STATUS.md` (*"W-001: ACTIVE (Theory Landscape)"*) passt zur in `RESEARCH_GOVERNANCE.md` definierten Reihenfolge (Hypothese ✓, zwei Reviews ✓, aktuell also folgerichtig "Theory Landscape"). Insofern besteht keine interne Widersprüchlichkeit — aber auch keine Tiefe, gegen die Konsistenz sinnvoll geprüft werden könnte.

## Verantwortlichkeiten

Nicht definiert. Kein Dokument in `06_research_program/` benennt, wer eine Hypothese aufstellt, wer ein Review durchführt, wer die Theory Landscape erstellt oder wer die Editor Decision trifft. Zum Vergleich: Das übrige Repository regelt Rollen an mehreren Stellen explizit und redundant (`CONTRIBUTING.md`, `SALES_CODEX_OPERATING_MANUAL.md` Kapitel 2, `01_framework/07_agent_protocols/`). Für das Research Program existiert kein analoges Rollendokument. `DECISION_POLICY.md`s "Editor Decisions" impliziert einen Herausgeber (vermutlich Felix, konsistent mit dem repositoryweiten Rollenmodell), aber dies wird nirgends im Ordner selbst festgehalten.

## Skalierbarkeit

Das Grundmuster (`active/`, `archived/`, `completed/`, projektspezifische `W`-Ordner) ist strukturell für beliebig viele parallele Forschungsprojekte ausgelegt und in diesem Punkt solide — vergleichbar mit dem grundsätzlich guten Lifecycle-Konzept von `book_catalog.md`. Das eigentliche Skalierungsrisiko liegt nicht im Ordnerschema, sondern darin, dass bei mehreren gleichzeitig laufenden Projekten dieselben unbefüllten Governance-Dokumente und Templates mehrfach unzureichend blieben — Skalierung würde die aktuelle Unschärfe vervielfachen, nicht auflösen.

## Verständlichkeit

Gering, gerade für Außenstehende (menschlich oder KI), die nur `06_research_program/` lesen. `active/W001/README.md` lautet vollständig: *"# W-001 / Forschungsprojekt."* — der Ordner selbst erklärt nicht, welche Frage W-001 untersucht. Diese Information existiert nur außerhalb des Ordners: eine repositoryweite Suche findet **50 andere Dateien, die "W-001" erwähnen** (u. a. `CURRENT_STATE.md`, `OPEN_DECISIONS.md`, mehrere Synthese- und Buchanalyse-Dokumente), wo W-001 durchgängig als *"Teach First vs. Diagnose First"*-Widerspruch beschrieben wird — aber **keine dieser Erläuterungen ist im Research-Program-Ordner selbst verlinkt oder wiederholt**. Ein Bearbeiter, der ausschließlich `06_research_program/` öffnet, kann nicht rekonstruieren, worum es in W-001 geht, ohne gezielt im übrigen Repository zu suchen.

---

# 2. Dokumentenstruktur

| Datei | Zweck (laut Inhalt/Namen) | Verantwortlichkeit | Abhängigkeiten | Redundanz/Auffälligkeit |
|---|---|---|---|---|
| `README.md` | Grundregel: Trennung Forschung/Codex | Programmweit | Keine erkennbar | Ein Satz, keine Redundanz, aber keine Substanz |
| `RESEARCH_GOVERNANCE.md` | Prozessreihenfolge | Programmweit | Keine erkennbar | Ein Satz; überschneidet sich thematisch mit `DECISION_POLICY.md` (beide sind "Governance"), ohne dass die Abgrenzung zwischen beiden Dateien erklärt wird |
| `DECISION_POLICY.md` | Integrationsregel in den Codex | Programmweit | Bezug zu `active/W001/06_EDITOR_DECISION.md` (implizit) | Ein Satz; keine Kriterien, wann eine Editor Decision positiv/negativ ausfällt |
| `RESEARCH_STATUS.md` | Statusanzeige laufender Projekte | Programmweit | `active/W001/` | Einzeiliges Freitextformat ohne Tabellenstruktur — skaliert nicht auf mehrere Projekte (vgl. Befund unter Kapitel 1, Skalierbarkeit) |
| `templates/DECISION_BRIEF_TEMPLATE.md` | Vorlage für Entscheidungsvorlagen | Templateebene | Für `05_DECISION_BRIEF.md`-Dateien | Nur Titelzeile, keine Feldstruktur |
| `templates/EDITOR_DECISION_TEMPLATE.md` | Vorlage für Editor Decisions | Templateebene | Für `06_EDITOR_DECISION.md`-Dateien | Nur Titelzeile, keine Feldstruktur |
| `templates/RED_TEAM_TEMPLATE.md` | Vorlage für Red-Team-Reviews | Templateebene | Für `03_*_RED_TEAM_REVIEW.md`-Dateien | Nur Titelzeile, keine Feldstruktur |
| `templates/RESEARCH_PROJECT_TEMPLATE.md` | Vermutlich: Vorlage für neue `W`-Projektordner | Templateebene | Unklar — Verhältnis zu `active/W001/README.md` nicht erkennbar | Nur Titelzeile; **Zweck gegenüber `README.md` je Projekt nicht abgegrenzt** — mögliche Doppelverantwortung zweier Dokumenttypen für dieselbe Funktion (Projektbeschreibung), aber mangels Inhalt nicht abschließend feststellbar |
| `templates/THEORY_LANDSCAPE_TEMPLATE.md` | Vorlage für Theorielandschaften | Templateebene | Für `04_THEORY_LANDSCAPE.md`-Dateien | Nur Titelzeile, keine Feldstruktur |
| `active/W001/README.md` | Projekteinstieg W-001 | Projektebene | — | Enthält keine inhaltliche Einordnung der Forschungsfrage (siehe Kapitel 1) |
| `active/W001/01_INITIAL_HYPOTHESIS.md` | Ausgangshypothese | Projektebene | Kein zugehöriges Template vorhanden | Nur Titelzeile — für die erste inhaltliche Stufe des Prozesses existiert keinerlei Anleitung, was hier dokumentiert werden soll |
| `active/W001/02_SCIENTIFIC_MASTER_REVIEW.md` | Wissenschaftliches Obergutachten, vier konkurrierende Hypothesen + Synthese-Theorie (SCSM) | Projektebene | Kein zugehöriges Template vorhanden (einzige umfangreiche Dokumentart ohne Template) | Vollständig ausgearbeitet (330 Zeilen, durchnummerierte Quellenverweise, Referenzliste); **verwendet keine Markdown-Überschriften (`##`)** — reiner Fließtext mit thematischen Absätzen, abweichend vom sonstigen Repository-Standard (z. B. Buchanalysen, Sprintberichte), die durchgängig strukturierte Überschriften nutzen |
| `active/W001/03_GEMINI_RED_TEAM_REVIEW.md` | Kritisches Gegengutachten zum SCSM | Projektebene | `templates/RED_TEAM_TEMPLATE.md` (Template selbst leer) | Vollständig ausgearbeitet (290 Zeilen, 13 Prüfkriterien, Referenzliste); gleiches Formatierungsmuster wie 02 (keine `##`-Überschriften) |
| `active/W001/04_THEORY_LANDSCAPE.md` | Systematische Theorieprüfung | Projektebene | `templates/THEORY_LANDSCAPE_TEMPLATE.md` (Template selbst leer) | Nur Titelzeile — **obwohl laut `RESEARCH_STATUS.md` dies die aktuell aktive Stufe ist**, existiert noch kein Inhalt |
| `active/W001/05_DECISION_BRIEF.md` | Entscheidungsvorlage | Projektebene | `templates/DECISION_BRIEF_TEMPLATE.md` (leer) | Nur Titelzeile |
| `active/W001/06_EDITOR_DECISION.md` | Finale Entscheidung | Projektebene | `templates/EDITOR_DECISION_TEMPLATE.md` (leer) | Nur Titelzeile |
| `active/W001/OPEN_QUESTIONS.md` | Offene Fragen des Projekts | Projektebene | Kein zugehöriges Template | Nur Titelzeile, kein Eintrag — obwohl beide ausgearbeiteten Reviews inhaltlich zahlreiche offene/widersprüchliche Punkte referenzieren (z. B. die vom Red Team angeführte fehlende empirische Messbarkeit), wurde keiner davon hier verzeichnet |
| `active/W001/REFERENCES.md` | Konsolidiertes Literaturverzeichnis des Projekts | Projektebene | Kein zugehöriges Template | Nur Titelzeile, keine Einträge — **obwohl** `02_SCIENTIFIC_MASTER_REVIEW.md` (59 nummerierte Quellen) und `03_GEMINI_RED_TEAM_REVIEW.md` (69 nummerierte Quellen) jeweils eigene, vollständige Referenzlisten am Dateiende führen. Die projektweite `REFERENCES.md` dupliziert diese Funktion nicht, sondern bleibt schlicht ungenutzt — Verantwortlichkeit für Literaturverwaltung liegt faktisch bei den Einzeldokumenten, nicht bei der dafür vorgesehenen Datei |
| `active/W001/RESEARCH_LOG.md` | Chronologisches Arbeitsprotokoll | Projektebene | Kein zugehöriges Template | Nur Titelzeile, kein Eintrag — im Unterschied zu `00_project/SESSION_LOG.md` (Vorbild-Muster im übrigen Repository) wurde dieses Muster hier nicht übernommen |

## Identifizierte Redundanzen, Lücken und Fehlplatzierungen

**Doppelte Inhalte:** Keine gefunden — bei einem Füllstand von 12,5 % ist inhaltliche Dopplung strukturell kaum möglich. Die einzige funktionale Doppelverantwortung betrifft die Literaturverwaltung (`REFERENCES.md` vs. die in `02`/`03` eingebetteten Referenzlisten, siehe Tabelle oben) — hier liegt allerdings eher eine ungenutzte als eine doppelt genutzte Datei vor.

**Fehlende Dokumente:** Für drei zentrale Dateitypen existiert kein Template, obwohl sie im aktiven Projekt bereits verwendet werden: eine Vorlage für die Ausgangshypothese (`01_INITIAL_HYPOTHESIS`), eine Vorlage für die umfangreichste Dokumentart des gesamten Prozesses (`02_SCIENTIFIC_MASTER_REVIEW`/"Research"-Stufe) sowie Vorlagen für `OPEN_QUESTIONS`, `REFERENCES` und `RESEARCH_LOG`. Es fehlt zudem ein programmweites Rollen-/Protokolldokument analog zu `01_framework/07_agent_protocols/`.

**Unnötige Dokumente:** Keine identifiziert. Jede vorhandene Datei hat eine erkennbare, sinnvolle intendierte Funktion — das Problem ist Unterfüllung, nicht Überfluss.

**Falsche Speicherorte:** Keine gefunden. Alle 16 Dateien liegen an einem für ihre erkennbare Funktion plausiblen Ort innerhalb der bestehenden Ordnerlogik (`active/archived/completed/templates`).

---

# 3. Prozessarchitektur

**Vorgabe-Referenzmodell:** Research Question → Theory Assessment → Research → Peer Review → Editor Decision → Repository Integration → Health Check (7 Stufen).

**Tatsächlich im Repository beschriebenes Modell** (`RESEARCH_GOVERNANCE.md`): Hypothese → Reviews → Theory Landscape → Decision Brief → Editor Decision (5 benannte Stufen, umgesetzt in 6 nummerierten Dateien, da "Reviews" im aktiven Projekt in zwei Dokumente — Master Review und Red Team Review — aufgeteilt wurde).

## Abgleich Stufe für Stufe

| Referenzstufe | Entsprechung im Repository | Befund |
|---|---|---|
| Research Question | Keine explizite Entsprechung | `01_INITIAL_HYPOTHESIS.md` beginnt bereits bei der Hypothese, nicht bei der zugrunde liegenden Forschungsfrage. Die eigentliche Frage hinter W-001 ("Teach First vs. Diagnose First") wird im Ordner selbst nirgends formuliert (siehe Kapitel 1, Verständlichkeit) — sie ist nur über externe Dokumente rekonstruierbar. Eine dedizierte, benannte "Research Question"-Stufe fehlt strukturell. |
| Theory Assessment | Teilweise: `04_THEORY_LANDSCAPE.md` | Im Referenzmodell würde man eine Theoriebewertung *vor* der eigentlichen Forschung erwarten (Scoping: welche Theorien existieren bereits, bevor man forscht). Im tatsächlichen Ablauf liegt die "Theory Landscape"-Stufe jedoch *nach* den beiden Reviews (02, 03) — die eigentliche Theoriearbeit (Bewertung von vier konkurrierenden Hypothesen inkl. Synthese zu einer neuen Theorie) hat in `02_SCIENTIFIC_MASTER_REVIEW.md` bereits stattgefunden, bevor die dafür vorgesehene "Theory Landscape"-Stufe überhaupt beginnt. Die Reihenfolge des tatsächlichen Prozesses weicht damit von der im Referenzmodell nahegelegten Logik ab; ob dies beabsichtigt ist (Theory Landscape als *nachgelagerte, konsolidierende* Stufe statt als *vorgelagerte* Scoping-Stufe), lässt sich mangels jeder Erläuterung in `RESEARCH_GOVERNANCE.md` nicht feststellen. |
| Research | Faktisch in `02_SCIENTIFIC_MASTER_REVIEW.md` enthalten | Keine eigenständige, benannte "Research"-Stufe mit eigenem Template existiert. Die primäre Forschungsarbeit (Literatursynthese, Theoriebildung) ist inhaltlich untrennbar mit der ersten "Review"-Stufe verschmolzen. Für künftige Projekte bleibt unklar, ob eine separate Recherchephase vor dem Master Review vorgesehen ist. |
| Peer Review | `03_GEMINI_RED_TEAM_REVIEW.md` | Vorhanden und strukturell nachvollziehbar als kritisches Gegengutachten zur ersten Stufe. Es existiert jedoch nur **eine** Review-Instanz — kein Mechanismus für mehrere/iterative Review-Runden, kein Kriterium, wann ein Peer Review als "bestanden" oder "nicht bestanden" gilt. |
| Editor Decision | `06_EDITOR_DECISION.md` (leer) | Stufe strukturell vorgesehen und mit `DECISION_POLICY.md` verknüpft ("nur Editor Decisions erlauben Übernahme"). Für W-001 noch nicht erreicht/befüllt — dies ist im aktuellen Projektstand plausibel (Theory Landscape und Decision Brief stehen noch aus), aber die Datei selbst enthält keinerlei Entscheidungskriterien, die eine künftige Befüllung anleiten würden. |
| Repository Integration | **Keine Entsprechung gefunden** | Es existiert keine Datei, kein Template und kein Abschnitt in einem Governance-Dokument, der beschreibt, *wie* eine positive Editor Decision tatsächlich zu neuen oder veränderten Objekten in `03_knowledge_base/` führt. Offen bleiben: Welchem Objekttyp (ST/A/MEC/P/T/MOD) würde ein akzeptiertes Forschungsergebnis zugeordnet? Gilt der Book-Mode-Pipeline-Standard (SRC→ST→A→MEC→P→T→MOD, `PROJECT_BOOTSTRAP.md`) auch für Research-Program-Ergebnisse, oder ein eigener Mechanismus? Keines der 16 Dokumente beantwortet dies. Diese fehlende Schnittstelle ist der gravierendste Einzelbefund dieses Kapitels. |
| Health Check | **Keine Entsprechung gefunden** | Weder ein Dateiname noch eine Textstelle innerhalb von `06_research_program/` erwähnt eine Health-Check-Stufe. Bemerkenswert: Der Begriff "Health Check" ist im *übrigen* Repository durchaus etabliert (u. a. `OPEN_DECISIONS.md`, `CURRENT_STATE.md`, `SALES_CODEX_1_0_PROGRAM.md`) — dort allerdings selbst als unerledigter Punkt geführt: `POST_MORTEM_B0002.md` (Phase 11) hält fest, dass ein "Repository Health Check" nie formalisiert wurde, und dies wurde im Rahmen des Open-Decisions-Resolution-Sprints bei OD-003 als dokumentierte, bewusst nicht geschlossene Restlücke festgehalten. Das Fehlen einer Health-Check-Stufe im Research Program ist damit kein isoliertes Versäumnis dieses Teilbereichs, sondern spiegelt eine bereits repositoryweit bekannte, unbehobene Lücke. |

## Gesamtbefund Prozessarchitektur

Von den sieben referenzierten Stufen sind zwei (Peer Review, Editor Decision) klar und mit passender Datei vorhanden, zwei (Theory Assessment, Research) sind vorhanden, aber unklar abgegrenzt bzw. in der Reihenfolge zum Referenzmodell inkonsistent, und drei (Research Question, Repository Integration, Health Check) fehlen vollständig ohne jede strukturelle Entsprechung. Der beschriebene Prozess ist damit **weder vollständig noch vollumfänglich konsistent** mit dem in diesem Sprint vorgegebenen Referenzmodell.

---

# 4. Governance

## Rollen

Nicht definiert (siehe Kapitel 1). Kein Dokument benennt, wer "Researcher", "Reviewer" oder "Editor" im Kontext des Research Programs ist, welche Qualifikation oder welchen Prozess diese Rollen durchlaufen, oder ob KI-Systeme (analog zu `01_framework/07_agent_protocols/` für den Hauptcodex) unterschiedliche Rollen einnehmen dürfen.

## Verantwortlichkeiten

Einzig klar zugewiesen ist die Integrationsschwelle: *"Nur Editor Decisions erlauben eine Übernahme in den Codex"* (`DECISION_POLICY.md`) — dies ist inhaltlich sinnvoll und konsistent mit dem repositoryweiten Prinzip, dass Felix als Herausgeber die letzte Entscheidungsinstanz ist. Alle vorgelagerten Verantwortlichkeiten (wer erstellt eine Hypothese, wer beauftragt ein Review, wer entscheidet über den Übergang zwischen Stufen) sind nicht zugewiesen.

## Entscheidungslogik

Rudimentär. Es existiert eine Freigabeschwelle (Editor Decision erforderlich für Integration), aber keine Kriterien, *wann* eine Editor Decision positiv ausfallen sollte — kein Bewertungsraster, keine Mindestanforderungen an Evidenzqualität, keine Verbindung zum bereits im Hauptcodex etablierten Evidenzsystem (E1–E5, `01_framework/02_evidence_system/`). Das ist bemerkenswert, da gerade das Evidenzsystem eines der am weitesten ausgearbeiteten und am konsequentesten angewendeten Governance-Instrumente des übrigen Repositorys ist (siehe `REPOSITORY_CONSOLIDATION_REPORT_RC1.md` Kapitel 1, "wichtigste Stärken") — ein Verweis darauf wäre naheliegend gewesen, fehlt aber vollständig.

## Nachvollziehbarkeit

Gemischt. Auf Dokumentenebene ist die Nachvollziehbarkeit innerhalb der beiden ausgearbeiteten Reviews hoch — beide verwenden durchgehend nummerierte Inline-Verweise mit zugehöriger Referenzliste am Dateiende, ein im übrigen Repository ebenfalls übliches Zitierprinzip. Auf Prozessebene ist die Nachvollziehbarkeit jedoch gering: Es gibt kein Datum, keinen Autor/Bearbeiter-Vermerk und keinen Statuszeitstempel in den beiden Kernreviews selbst (anders als etwa Sprintberichte in `00_project/`, die durchgehend Metadaten-Kopfzeilen mit Datum, Sprint, Auftrag führen). `RESEARCH_LOG.md`, das genau diese Lücke schließen würde, ist leer.

---

# 5. Templates

## Vorhandene Templates (5)

`DECISION_BRIEF_TEMPLATE.md`, `EDITOR_DECISION_TEMPLATE.md`, `RED_TEAM_TEMPLATE.md`, `RESEARCH_PROJECT_TEMPLATE.md`, `THEORY_LANDSCAPE_TEMPLATE.md` — alle fünf bestehen ausschließlich aus einer Titelzeile ohne Feldstruktur, Pflichtabschnitte oder Ausfüllhinweise. Zum Vergleich: Die 13 Templates in `01_framework/08_templates/` (für den Hauptcodex) definieren durchgängig konkrete Pflichtfelder (siehe z. B. `principle_template.md`, `technique_template.md`). Die Research-Program-Templates erreichen dieses Strukturierungsniveau in keinem der fünf Fälle.

## Fehlende Templates

- **Initial-Hypothesis-Template** — für die erste inhaltliche Stufe jedes Forschungsprojekts existiert keine Vorlage.
- **Research-/Master-Review-Template** — für die umfangreichste und wissenschaftlich anspruchsvollste Dokumentart (vgl. `02_SCIENTIFIC_MASTER_REVIEW.md`, 330 Zeilen) existiert keine Vorlage, obwohl dies inhaltlich die zentrale Forschungsleistung jedes Projekts sein dürfte.
- **Open-Questions-Template**, **References-Template**, **Research-Log-Template** — für alle drei projektbegleitenden Dokumente fehlt eine Vorlage; alle drei sind im einzigen bestehenden Projekt unbefüllt geblieben (siehe Kapitel 2).
- **Rollenprotokoll** (kein Template, sondern ein fehlendes Governance-Dokument analog zu `01_framework/07_agent_protocols/`).

## Doppelte Templates

Keine gefunden — alle fünf vorhandenen Templates haben unterscheidbare, nicht überlappende Namen. Die einzige Unklarheit betrifft nicht eine Dopplung, sondern eine unklare Abgrenzung: **`RESEARCH_PROJECT_TEMPLATE.md`** könnte sowohl als übergeordnete Vorlage für einen neuen `W`-Projektordner insgesamt gedacht sein als auch spezifisch als Vorlage für die `README.md` jedes Projekts — beide Lesarten sind mit dem vorhandenen (nicht vorhandenen) Inhalt vereinbar, eine Klärung ist mangels Substanz nicht möglich.

---

# 6. Übergang zum Repository

Der Übergang zwischen Research Program und dem übrigen Repository ist an mehreren Stellen strukturell nicht abgesichert.

**Fehlende Schnittstelle 1 — Framework-Ebene:** Eine gezielte Suche nach "research_program", "Research Program" und "W-001" in den drei zentralen Methodikdokumenten des Repositorys (`01_framework/05_knowledge_model/canonical_knowledge_model.md`, `00_project/SALES_CODEX_OPERATING_MANUAL.md`, `00_project/task_rules.md`) ergab **keinen einzigen Treffer**. Das bedeutet: Kein einziges der Dokumente, die den offiziellen Wissenspipeline-Standard des Sales Codex definieren, erwähnt das Research Program oder beschreibt, wie dessen Ergebnisse in diesen Standard einfließen. Das Research Program existiert damit strukturell parallel zum Framework, ohne dass das Framework von seiner Existenz "weiß".

**Fehlende Schnittstelle 2 — Repository Integration (siehe auch Kapitel 3):** Keine Datei beschreibt den technischen/redaktionellen Ablauf von einer akzeptierten Editor Decision zu einem neuen oder veränderten Wissensobjekt.

**Fehlende Schnittstelle 3 — Interne Verlinkung:** Innerhalb von `06_research_program/` selbst enthält keine der 16 Dateien einen Backtick-Pfadverweis auf eine andere Datei desselben Ordners (repositoryweite Prüfung ergab null Treffer für dieses Muster innerhalb des Ordners). Selbst die durchnummerierte Abfolge 01–06 wird nirgends explizit referenziert oder erklärt (z. B. verweist `06_EDITOR_DECISION.md` nicht auf `05_DECISION_BRIEF.md`) — die Reihenfolge ergibt sich ausschließlich implizit aus der Dateinamens-Nummerierung.

**Vorhandene, funktionierende Verbindung:** In die andere Richtung — vom übrigen Repository zum Research Program — besteht durchaus eine intensive inhaltliche Bezugnahme: 45 Dateien außerhalb von `06_research_program/` erwähnen "W-001", meist im Kontext des ungelösten methodischen Kernwiderspruchs des gesamten Sales Codex (u. a. `CURRENT_STATE.md`, `OPEN_DECISIONS.md`, mehrere Synthese- und Buchanalyse-Dokumente). Das Research Program ist im übrigen Repository also als Konzept präsent und relevant — die Schnittstelle ist somit **einseitig**: Das Hauptrepository verweist auf das Research Program, aber nicht umgekehrt, und es existiert kein dokumentierter Mechanismus für den Rückfluss der Ergebnisse.

---

# 7. Wartbarkeit

**Über mehrere Jahre mit zahlreichen künftigen Forschungsprojekten voraussichtlich nicht ohne vorherige Nacharbeit wartbar.** Begründung:

Das Ordnerschema selbst (`active/archived/completed/W`-Projektordner) skaliert strukturell unbegrenzt und ist insofern langfristig tragfähig. Die eigentliche Wartbarkeitsgefahr liegt in der fehlenden inhaltlichen Tiefe der Governance-Schicht: Jedes künftige Forschungsprojekt müsste mangels ausgefüllter Templates und Rollenregeln entweder (a) das Muster von W-001 informell nachahmen, ohne dass dieses Muster irgendwo als verbindlich dokumentiert ist, oder (b) jeweils neu improvisieren, was zu unterschiedlichen, nicht vergleichbaren Projektstrukturen über die Zeit führen würde — ein Risiko, das im Hauptcodex durch die sehr expliziten Templates und das Task-Regelwerk (`task_rules.md`) aktiv verhindert wird, im Research Program aber ungebremst besteht.

`RESEARCH_STATUS.md`s einzeiliges Freitextformat (*"W-001: ACTIVE (Theory Landscape)"*) wird bei zwei oder mehr gleichzeitig laufenden Projekten unpraktikabel, da keine Tabellenstruktur vorgesehen ist. Ohne eine solche Struktur ist absehbar, dass der Status mehrerer Projekte entweder inkonsistent gepflegt oder die Datei stillschweigend zu einer Liste umgebaut wird, ohne dass dies irgendwo als Konvention festgelegt wäre.

Die vollständige Isolation von der Framework-Ebene (Kapitel 6) bedeutet zusätzlich, dass jede künftige Überarbeitung des Hauptframeworks (Evidenzsystem, Canonical Knowledge Model) das Research Program nicht automatisch mitzieht — die beiden Bereiche können langfristig auseinanderdriften, ohne dass ein Mechanismus dies verhindert oder auch nur bemerkbar macht.

---

# 8. Release Readiness

**Bewertung: Nicht geeignet, als Version RC-1 eingefroren zu werden.**

Ein Freeze würde bedeuten, den aktuellen Zustand — 17 von 19 Dateien ohne inhaltliche Substanz, fünf Templates ohne Feldstruktur, keine Rollen- oder Entscheidungskriterien, keine Integrationsschnittstelle zum Hauptrepository, keine Health-Check-Stufe — als stabile Grundlage für alle künftigen Forschungsprojekte zu kanonisieren. Das widerspräche dem erkennbaren Anspruch des Programms selbst (ein mehrstufiger, governance-gesicherter Prozess, analog zur Sorgfalt des Book Mode).

## Ausschließlich strukturelle Blocker

1. **Templates ohne Feldstruktur.** Alle fünf vorhandenen Templates enthalten nur eine Titelzeile. Ein Freeze würde diesen Leerzustand als finale Version festschreiben.
2. **Fehlende Templates für zentrale Stufen** (Initial Hypothesis, Research/Master Review, Open Questions, References, Research Log — siehe Kapitel 5).
3. **Fehlendes Rollen- und Entscheidungsregelwerk** (siehe Kapitel 4) — kein Pendant zu `01_framework/07_agent_protocols/` oder den Abbruchbedingungen des Book Mode.
4. **Fehlende Repository-Integrationsschnittstelle** (siehe Kapitel 3 und 6) — es ist strukturell nicht definiert, wie ein akzeptiertes Forschungsergebnis zu einem Wissensobjekt wird.
5. **Fehlende Health-Check-Stufe** (siehe Kapitel 3) — deckt sich mit einer bereits repositoryweit bekannten, unter OD-003 dokumentierten Lücke.
6. **Vollständige Entkopplung von der Framework-Ebene** (siehe Kapitel 6) — Canonical Knowledge Model, Operating Manual und Task Rules erwähnen das Research Program nicht.
7. **Fehlende interne Verlinkung** innerhalb von `06_research_program/` selbst (siehe Kapitel 6).
8. **Prozessreihenfolge-Unklarheit** zwischen "Theory Assessment" und "Research" (siehe Kapitel 3) — nicht falsch, aber nicht erklärt, was bei mehreren künftigen Projekten zu unterschiedlichen Interpretationen führen kann.

Keiner dieser acht Punkte ist ein inhaltlicher/wissenschaftlicher Blocker (die Frage, ob SCSM wissenschaftlich haltbar ist, ist ausdrücklich nicht Gegenstand dieser Bewertung) — alle acht sind strukturelle Governance- und Dokumentationslücken.

---

# Executive Summary

## Größte Stärken

Die physische Trennung von Forschung und offiziellem Codex (`README.md`: *"Forschung ist strikt vom offiziellen Sales Codex getrennt"*) ist ein methodisch richtiger und im übrigen Repository konsequent respektierter Grundsatz — keine ungeprüften Forschungsergebnisse sind in `03_knowledge_base/` eingesickert. Die einzige vollständig durchgeführte Recherche- und Reviewarbeit (W-001, Stufen 1–3) zeigt, dass der Prozess bei tatsächlicher Nutzung substanzielle, gut referenzierte Ergebnisse produzieren kann (330 plus 290 Zeilen, durchgehend mit nummerierten Quellenverweisen). Besonders hervorzuheben ist die bewusste Anlage eines kritischen Gegengutachtens (Red Team Review) unmittelbar nach der ersten Synthese — ein methodisch wertvolles, in sich schlüssiges Kontrollprinzip, das strukturell verhindert, dass ein einzelnes, unwidersprochenes Gutachten unmittelbar in eine Entscheidung münden könnte.

## Wichtigste Schwächen

Der eklatante Substanzunterschied zwischen den vier Governance-Dokumenten/fünf Templates (89,5 % aller Dateien im Ordner sind reine Titelzeilen) und den beiden inhaltlich ausgearbeiteten Reviewdokumenten ist die dominante Schwäche: Das Research Program hat bislang keine eigene, verbindliche Prozessarchitektur hervorgebracht, sondern lediglich eine Ordnerstruktur mit Absichtserklärungen. Zwei damit verbundene Einzelbefunde verdienen besondere Aufmerksamkeit: Erstens fehlt eine definierte Schnittstelle zur Repository-Integration vollständig — selbst wenn W-001 heute eine Editor Decision erhielte, ist nirgends beschrieben, wie das Ergebnis in `03_knowledge_base/` ankäme. Zweitens haben die beiden bereits abgeschlossenen Reviewstufen von W-001 zwei entgegengesetzte fachliche Schlussfolgerungen erreicht (Empfehlung vs. Ablehnung des geprüften Modells), doch die für genau diese Situation vorgesehene nächste Stufe (Theory Landscape) ist vollständig leer — der Prozess bietet an der Stelle, an der er am dringendsten gebraucht würde, keinerlei Struktur.

## Priorisierte Empfehlungen (zur Herausgeber-Entscheidung, nicht umgesetzt)

1. Templates für alle fünf Stufen mit tatsächlicher Feldstruktur ausarbeiten, zusätzlich fehlende Templates für Initial Hypothesis, Research/Master Review, Open Questions, References und Research Log ergänzen.
2. Ein Rollen- und Entscheidungsregelwerk für das Research Program definieren (Rollen, Abbruchbedingungen, Bewertungskriterien für Editor Decisions — ggf. mit Bezug zum bestehenden Evidenzsystem E1–E5).
3. Eine explizite Repository-Integrationsschnittstelle beschreiben (welcher Objekttyp, welcher Pipeline-Schritt, welches Template greift bei Annahme eines Forschungsergebnisses).
4. Eine Health-Check-Stufe für das Research Program definieren — idealerweise im Zusammenhang mit der bereits repositoryweit offenen Health-Check-Frage (OD-003) gelöst, nicht isoliert.
5. `active/W001/README.md` um eine knappe Einordnung der Forschungsfrage ergänzen, damit der Ordner ohne externen Kontext verständlich ist.
6. Klärung, ob `RESEARCH_PROJECT_TEMPLATE.md` und projektbezogene `README.md`-Dateien redundant oder unterschiedlich sind.

## Gesamtreifegrad

**MAJOR REVISION REQUIRED.**

Begründung in einem Satz: Ein Ordner, in dem 17 von 19 Dateien und alle fünf Templates ausschließlich aus einer Titelzeile bestehen, in dem keine Rollen, keine Integrationsschnittstelle und keine Health-Check-Stufe definiert sind und der von den zentralen Framework-Dokumenten des Repositorys nicht referenziert wird, kann nicht als "Ready" oder "Ready after Minor Revision" gelten — die substanzielle Lücke liegt nicht in Details, sondern in der Governance-Architektur selbst.

---

*Dieser Bericht wurde ausschließlich lesend erstellt. Keine Datei in `06_research_program/` oder anderswo im Repository wurde verändert. Alle genannten Empfehlungen sind zur Herausgeber-Entscheidung dokumentie