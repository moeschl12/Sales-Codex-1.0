# Cowork Performance Audit — Claude-Arbeitsweise im Sales Codex

**Dokumentklasse:** Analyse / Reference
**Rolle bei Erstellung:** Principal AI Systems Engineer (Claude Cowork) — nicht Editor, Autor, Research Assistant oder Knowledge Engineer. Gegenstand ist die eigene Arbeitsweise, nicht der fachliche Inhalt des Sales Codex.
**Datum:** 2026-07-05
**Status:** Vorschlag zur Herausgeber-Prüfung — keine Repository-Änderungen, keine Framework-Änderungen, kein Eingriff in laufende Governance (Version 1.0 gilt als veröffentlicht und unveränderlich, siehe `CURRENT_STATE.md`)
**Verhältnis zu bestehenden Dokumenten:** Überschneidet sich thematisch mit `99_archive/00_project_history/PROCESS_PATTERN_ANALYSIS_2026-07.md`, hat aber einen anderen Fokus. Jenes Dokument sucht wiederkehrende Arbeitsmuster als Kandidaten für Skills. Dieses Dokument analysiert ausschließlich Tokenverbrauch, Dateiladestrategie und Prompting — keine Skill-Vorschläge, keine inhaltliche Prozessbewertung.

---

## Analysebasis und Grenzen (verbindlich zu lesen)

Diese Analyse stützt sich ausschließlich auf tatsächlich zugängliche Daten:

- Vollständige Verzeichnisstruktur und Dateigrößen des Repositorys (`sales-codex-workspace-v1.0`, Stand 2026-07-05), erhoben per Shell (`find`, `du`, `wc`).
- Volltext von: `PROJECT_BOOTSTRAP.md`, `CLAUDE_BOOTSTRAP.md`, `README.md`, `INDEX.md`, `CURRENT_STATE.md` (Auszug), `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md` (Kopf/Fuß), `00_project/task_rules.md` (Auszug), `00_project/REPOSITORY_KPIS.md` (Auszug), `00_project/COWORK_EXECUTION_PROTOCOL.md` (Auszug), `01_framework/07_agent_protocols/master_agent_protocol.md`, `01_framework/07_agent_protocols/claude_editor_protocol.md`, `08_knowledge_atlas/ATLAS_MANIFEST.md`, drei Beispiel-Statement-Dateien, `99_archive/00_project_history/PROCESS_PATTERN_ANALYSIS_2026-07.md` (Auszug).
- Git-Historie (`git log`): **4 Commits insgesamt** über die gesamte sichtbare Projektlaufzeit.
- Stichprobenhafter Zugriff auf zwei von 16 lokal verfügbaren Cowork-Sessions über das Session-Tool — jeweils nur die letzten 4–6 Nachrichten (Ende der Session, assistentenseitig). **Kein Zugriff auf die ursprünglichen Nutzer-Prompts dieser Sessions, keine vollständigen Transkripte gelesen.** Aussagen zu Felix' tatsächlichem Promptstil sind daher explizit als Inferenz aus den im Repository dokumentierten Protokollen (Bootstrap-Dateien, Execution Protocol) gekennzeichnet, nicht als beobachtete Chatanalyse.
- Alle Tokenschätzungen sind grobe Näherungen (≈ 4 Zeichen/Token für deutschsprachigen Markdown-Text). Sie dienen der Größenordnung, nicht als exakte Zahl.

Nicht analysiert: die 14 weiteren lokal sichtbaren Sessions (nur Titel bekannt), Inhalte außerhalb dieses Repositorys, jegliche Cowork-interne Kontextfenster-Telemetrie (nicht zugänglich).

---

## 1. Executive Summary

Der Sales Codex hat in fünf Tagen (27.06.–04.07.2026) ein methodisch striktes, gut atomisiertes Wissenssystem aufgebaut: 514 Wissensobjekte in `03_knowledge_base/` (309 ST, 60 A, 29 MEC, 57 P, 47 T, 12 MOD), im Schnitt ~50–70 Zeilen pro Datei, templatekonform, einzeln referenzierbar. Diese Ebene ist token-effizient und sollte unverändert bleiben.

Das eigentliche Tokenproblem liegt nicht in der Wissensbasis, sondern in der **Prozess- und Governance-Ebene**: `00_project/` enthält 43 Dateien mit zusammen 1,10 MB Text (≈ 275.000 Tokens) — kein einziges Wissensobjekt darunter, ausschließlich Sprintberichte, Audits, Freeze-Erklärungen, Release-Dokumente und Statusdateien. Das sind bereits 63 % der Größe der gesamten Wissensbasis (`03_knowledge_base/`, 1,74 MB), obwohl die Wissensbasis der eigentliche Projektzweck ist und die Prozessebene nur Mittel zum Zweck sein sollte.

Zusätzlich existieren vier verschiedene, teils widersprüchliche Dokumente, die definieren, was eine Session zuerst lesen soll (`CLAUDE_BOOTSTRAP.md`, `PROJECT_BOOTSTRAP.md`, `INDEX.md`, `COWORK_EXECUTION_PROTOCOL.md`). Der aktuell gültige Leitfaden (`PROJECT_BOOTSTRAP.md`, v1.1) fordert im selben Atemzug „nicht unnötig das ganze Repository lesen" und definiert eine „Operational"-Dateiklasse von acht Dateien, die angeblich „in jeder Session" gelesen werden müssen — zusammen ≈ 283 KB / ≈ 71.000 Tokens. Das ist ein interner Widerspruch, kein Prompting-Problem.

`NEXT_ACTION.md` verstößt gegen seine eigene Titelzeile („Genau eine nächste Aktion. Kein Backlog. Kein Mehrfach-Eintrag.") — die Datei ist 25 KB groß und enthält mehrere gestapelte „Vorheriger Sprint"-Abschnitte, die inhaltlich fast identisch in `CURRENT_STATE.md` und `SESSION_LOG.md` erneut stehen. Ein und derselbe Sprint wird damit an mindestens drei bis vier Stellen in voller Prosalänge beschrieben.

Positiver Befund aus der Stichprobe zweier realer Sessions: Die Chat-Antworten selbst sind bereits knapp (kurze Zusammenfassung + Dateiliste, keine langen Zwischenberichte im Chat). Das Tokenproblem liegt nicht in der Chat-Verbosität, sondern in der Dateischicht, die jede Session zwingt zu laden bzw. neu zu erzeugen.

Größtes ungenutztes Sparpotenzial: der bereits vorhandene, aber kaum genutzte `08_knowledge_atlas` (Graph über Objekt-IDs, Orphan-Erkennung, bereits einmal kompiliert) — ein Werkzeug, das genau die Art von Konsistenzprüfung ersetzen könnte, die sonst brute-force über bis zu 514 Dateien läuft.

---

## 2. Top-10 Tokenfresser

| # | Datei / Verhalten | Ursache | Geschätzter Tokenverbrauch | Einsparpotenzial | Risiko bei Reduktion |
|---|---|---|---|---|---|
| 1 | „Operational"-Pflichtlektüre laut `PROJECT_BOOTSTRAP.md` (`backlog.md`, `CURRENT_STATE.md`, `NEXT_ACTION.md`, `SESSION_LOG.md`, `OPEN_DECISIONS.md`, `task_rules.md`, `SCIENTIFIC_DEBT.md`, `REPOSITORY_KPIS.md`) | Dateiklassen-Tabelle deklariert 8 Dateien als „liest KI in jeder Session", ohne Aufgabenbezug | ≈ 71.000 Token, wenn wörtlich befolgt | Sehr hoch (~85 %) — nur 2 von 8 sind wirklich sessionsunabhängig nötig | Gering, wenn Klassifizierung präzisiert statt gestrichen wird |
| 2 | `SESSION_LOG.md` (83 KB, 838 Zeilen, 32 Einträge) | Unbegrenztes Append-only-Log ohne Archivierungsschwelle | ≈ 20.800 Token pro Volllesung | Hoch (~90 %) durch Rotation/Archivierung | Gering — Historie bleibt in Archivdatei erhalten |
| 3 | `CURRENT_STATE.md` (51 KB, 467 Zeilen) | Enthält vollständige Phase-1-bis-5-Prosa jedes Sprints statt einer kompakten Zustandszusammenfassung | ≈ 12.800 Token | Hoch (~80 %) durch Kürzung auf reinen Zustand + Verweise | Mittel — Detailverlust muss durch Verweis auf Sprintbericht kompensiert werden |
| 4 | `SCIENTIFIC_DEBT.md` (58 KB) | Als „Operational" klassifiziert, aber nur bei inhaltlicher Qualitätsarbeit relevant, nicht bei Release-/Struktur-Sprints | ≈ 14.600 Token | Hoch (~90 %) — nur bei Buch-/Evidenzarbeit laden | Gering |
| 5 | `NEXT_ACTION.md` (25 KB) — verstößt gegen eigene Ein-Aktion-Regel | Sprint-Abschlüsse werden angehängt statt ersetzt, dupliziert `CURRENT_STATE.md`/`SESSION_LOG.md` | ≈ 6.300 Token | Sehr hoch (~90 %) durch strikte Ein-Aktion-Disziplin | Gering — Historie steht bereits in `SESSION_LOG.md` |
| 6 | `00_project/` als Ganzes (43 Dateien, 1,10 MB) für „Repository-Überblick"-Aufgaben | ~25 einmalige Sprint-/Freeze-/Audit-Berichte (Version 1.0, 30.06.–04.07.) liegen unarchiviert flach neben aktiven Dateien; `99_archive/` enthält nur 5 alte Dateien | ≈ 275.000 Token bei naiver Volllesung des Ordners | Sehr hoch (~70 %) durch Archivierung abgeschlossener Version-1.0-Berichte | Gering — Version 1.0 ist laut `CURRENT_STATE.md` ohnehin eingefroren, Berichte werden nicht mehr verändert |
| 7 | Vier konkurrierende Bootstrap-Dokumente (`CLAUDE_BOOTSTRAP.md`, `PROJECT_BOOTSTRAP.md`, `INDEX.md`, `COWORK_EXECUTION_PROTOCOL.md §2.1`) | Kein einheitlicher Einstiegspunkt; ältere Dokumente wurden nie entfernt oder klar als obsolet markiert | ≈ 2.500–3.000 Token zusätzlich, wenn mehr als ein Bootstrap-Dokument gelesen wird | Hoch (~75 %) durch einen einzigen kanonischen Einstieg | Gering |
| 8 | `OPEN_DECISIONS.md` (31 KB) unabhängig vom Aufgabentyp geladen | Als „Operational" klassifiziert, aber nur für Governance-/Entscheidungsarbeit relevant | ≈ 7.800 Token | Hoch (~85 %) — nur bei Entscheidungs-/Freigabe-Aufgaben | Gering |
| 9 | Redundante Sprint-Beschreibung über 3–4 Dateien gleichzeitig (`CURRENT_STATE.md` + `NEXT_ACTION.md` + `SESSION_LOG.md` + Einzelbericht, z. B. `VERSION_1_0_CLOSING_REPORT.md`) | Kein einziges „Source of Truth"-Prinzip für Sprintstatus — derselbe Sachverhalt wird mehrfach in voller Prosa reproduziert | ≈ 5.000–8.000 Token Redundanz pro Sprintabschluss | Hoch (~60 %) durch Verweis statt Wiederholung | Mittel — Redundanz wurde teils bewusst für Unabhängigkeit der Dokumente gewählt |
| 10 | Fehlende Nutzung von `08_knowledge_atlas` für Konsistenz-/Referenzprüfungen | Atlas existiert nur als Scope-Manifest (v0.1) und einmaliger Compiler-Lauf, kein etabliertes Abfragemuster in Prompts | Indirekt: jede manuelle Referenzprüfung kostet ~Dutzende Dateizugriffe statt einer `edges.csv`/`nodes.csv`-Abfrage | Mittel bis hoch, abhängig von Aufgabenhäufigkeit | Gering — Atlas ist bereits freigegeben, nur ungenutzt |

Nicht in der Liste, weil in der Stichprobe **nicht** als Tokenfresser bestätigt: Chat-seitige Zusammenfassungen am Sessionende. Beide gesampelten Sessions endeten mit kurzen, dateibezogenen Zusammenfassungen ohne lange Zwischenberichte — im Einklang mit `PROJECT_BOOTSTRAP.md`, Abschnitt „Kommunikation im Chat".

---

## 3. Dateiladestrategie

### Immer laden

Nur, was für praktisch jede Aufgabe unverzichtbar ist:

- `PROJECT_BOOTSTRAP.md` — einziger kanonischer Einstiegspunkt (siehe Abschnitt 4).
- `CURRENT_STATE.md` — **aber nur, wenn auf eine kompakte Kopf-Fassung gekürzt** (siehe Abschnitt 8). In der jetzigen Form (467 Zeilen Volltext-Sprintprosa) ist auch dies bereits zu groß für „immer".
- `00_project/NEXT_ACTION.md` — sofern auf tatsächlich eine Aktion begrenzt (siehe Abschnitt 8).

Begründung: Diese drei Dateien beantworten die einzige Frage, die vor jeder Aufgabe zwingend geklärt sein muss — „was ist der Stand, was ist als Nächstes zu tun". Alles andere hängt vom konkreten Auftrag ab.

### Nur bei Bedarf laden

- `01_framework/*` (Methodik, Evidenzsystem, Canonical Knowledge Model, Templates) — nur bei Aufgaben, die neue Wissensobjekte anlegen oder Framework-Fragen berühren.
- `00_project/task_rules.md` — nur bei Buchanalyse-/Task-Generierungsaufgaben.
- `00_project/OPEN_DECISIONS.md` — nur bei Governance-/Entscheidungsaufgaben.
- `00_project/SCIENTIFIC_DEBT.md`, `REPOSITORY_KPIS.md` — nur bei Qualitäts-/Evidenzarbeit oder Release-Reporting.
- Einzelne `03_knowledge_base/*`-Objekte — nur die tatsächlich betroffenen IDs, nie der ganze Ordner.
- `08_knowledge_atlas/output/*.csv` — bei Referenz-/Konsistenzprüfungen anstelle manueller Mehrfach-Dateizugriffe.
- Einzelne, namentlich benannte Sprint-/Audit-Berichte aus `00_project/` — nur wenn eine Aufgabe explizit auf einen davon verweist.
- Agentenprotokolle (`01_framework/07_agent_protocols/*`) — nur bei Rollenfragen oder Multi-Agent-Koordination, nicht routinemäßig.

Begründung: Diese Dateien sind fachlich notwendig, aber aufgabenspezifisch. Sie routinemäßig zu laden verletzt genau das Prinzip, das `PROJECT_BOOTSTRAP.md` selbst fordert („nur laden, was der aktuelle Job erfordert").

### Nicht standardmäßig laden

- `00_project/SESSION_LOG.md` — reine Historie, nur bei expliziter Nachfrage nach vergangenen Sessions.
- Alle „Operational"-als-solche-markierten, aber sprintgebundenen Einmal-Berichte (`*_REPORT.md`, `*_CLOSING_REPORT.md`, `POST_MORTEM_*.md`, `RC1_FREEZE_*.md`, `ACADEMIC_RECOVERY_*.md`) — historisch, nicht aktiv wirksam nach Abschluss des jeweiligen Sprints.
- `CLAUDE_BOOTSTRAP.md` — laut `PROJECT_BOOTSTRAP.md` selbst als „Archived" klassifiziert; sollte nicht mehr gelesen werden (siehe Abschnitt 4).
- `99_archive/*` — per Definition Archiv.
- `changelog.md` — nur bei Versionsfragen, nicht bei inhaltlicher Arbeit.

Begründung: Diese Dateien beschreiben, was war, nicht was zu tun ist. Sie sind für Audits und Nachvollziehbarkeit wertvoll, aber für den Normalbetrieb einer Session reine Kontextlast.

---

## 4. Bootstrap-Analyse

Vier Dokumente definieren aktuell, was eine Session zu Beginn lesen soll — mit unterschiedlichem Inhalt:

| Dokument | Stand | Liste | Status |
|---|---|---|---|
| `CLAUDE_BOOTSTRAP.md` | unbekannt (keine Versionsangabe), 1,2 KB | 8 Dateien: README, VISION, CURRENT_STATE, CONTRIBUTING, LANGUAGE_POLICY, INDEX, master_agent_protocol, claude_editor_protocol | Von `PROJECT_BOOTSTRAP.md` selbst als **„Archived"** klassifiziert (Zeile 129), verweist als „Erste Aufgabe" noch auf die längst abgeschlossene SPIN-Selling-Pilotanalyse |
| `INDEX.md` | 2,0 KB, 02.07. aktualisiert | 6 Dateien: README, VISION, CURRENT_STATE, CONTRIBUTING, LANGUAGE_POLICY, master_agent_protocol | Nicht als obsolet markiert, aber inhaltlich mit `PROJECT_BOOTSTRAP.md` inkonsistent (kein `NEXT_ACTION.md`) |
| `PROJECT_BOOTSTRAP.md` | v1.1, 6,1 KB, freigegeben 30.06. | 3 Punkte: PROJECT_BOOTSTRAP, CURRENT_STATE, NEXT_ACTION, dann nur betroffene Arbeitsdateien | Aktuell gültig, schlankester Ansatz |
| `COWORK_EXECUTION_PROTOCOL.md §2.1` | v1.0, 27.06. | Deckt sich inhaltlich mit `PROJECT_BOOTSTRAP.md`, ergänzt „Aufgabenliste anlegen (TaskCreate)" | Als „Reference" klassifiziert, wird also nicht automatisch gelesen — obwohl es den Sessionstart regelt |

**Befund:** Es gibt keinen einzigen, unmissverständlichen Einstiegspunkt. Ein Claude-Agent, der sich am Dateinamen orientiert, würde plausibel zuerst `CLAUDE_BOOTSTRAP.md` öffnen (Namensübereinstimmung mit dem eigenen Modell) — genau die Datei, die das aktuelle Governance-System selbst als veraltet einstuft und die auf eine seit Wochen abgeschlossene Pilotaufgabe verweist.

Konkrete Antworten auf die Prüffragen:

- **Zu groß:** Keine der vier Bootstrap-Dateien selbst ist groß. Das Problem ist nicht Dateigröße, sondern Vervielfachung von Einstiegspunkten.
- **Redundant:** `CLAUDE_BOOTSTRAP.md` und `INDEX.md` sind gegenüber `PROJECT_BOOTSTRAP.md` vollständig redundant und teilweise widersprüchlich (unterschiedliche Dateilisten, kein Verweis auf `NEXT_ACTION.md`).
- **Sollte gekürzt werden:** Keine Kürzung nötig — Entfernung bzw. explizite Archivierung der überholten Varianten ist der richtige Hebel, nicht Kürzung.
- **Sollte in Kurz-/Langversion aufgeteilt werden:** `CURRENT_STATE.md` (siehe Abschnitt 8) — nicht die Bootstrap-Dateien selbst.
- **Sollte nur noch Archiv sein:** `CLAUDE_BOOTSTRAP.md` — die eigene Governance-Tabelle in `PROJECT_BOOTSTRAP.md` verlangt das bereits; es fehlt nur die tatsächliche Verschiebung nach `99_archive/`.

---

## 5. Prompting-Analyse

**Wichtige Einschränkung:** Die folgenden Aussagen stützen sich auf die im Repository dokumentierten Protokolle (`PROJECT_BOOTSTRAP.md`, `COWORK_EXECUTION_PROTOCOL.md`) sowie auf zwei kurze, assistentenseitige Transkript-Ausschnitte — nicht auf eine systematische Analyse von Felix' tatsächlichen Prompts über alle 16 sichtbaren Sessions. Für belastbarere Aussagen über den tatsächlichen Promptstil müsste Felix entweder gezielt Beispielprompts bereitstellen oder eine vollständige Transkriptanalyse separat freigeben.

Aus den beobachtbaren Daten lassen sich dennoch drei belastbare Muster ableiten:

1. **Rollenbindung funktioniert.** In beiden gesampelten Sessions endete die Arbeit mit knappen, dateibezogenen Zusammenfassungen — genau wie in `PROJECT_BOOTSTRAP.md` gefordert („Was wurde erledigt, welche Dateien geändert, was ist der nächste Schritt. Keine langen Zwischenberichte."). Prompts, die explizit eine Rolle zuweisen („Rolle: Release Manager — ausdrücklich nicht als Forscher/Autor/Framework-Architekt", wie in mehreren `00_project`-Berichten dokumentiert), scheinen zuverlässig zu verhindern, dass die Session über den Auftragsrahmen hinausarbeitet.

2. **Explizite Scope-Ausschlüsse werden eingehalten.** Mehrere Sprintberichte (`RC1_FREEZE_DECLARATION.md`, `VERSION_1_0_CLOSING_REPORT.md`) dokumentieren explizit, was *nicht* verändert wurde. Das deutet darauf hin, dass Prompts mit expliziter Verbotsliste („keine neuen Wissensobjekte, keine Framework-Änderungen, keine Repository-Umstrukturierung") wirksam Scope-Kriechen verhindern — ein Muster, das in Abschnitt 6 formalisiert wird.

3. **Fehlende Dateiobergrenzen fördern Dokumentwachstum, nicht Prompt-Verhalten.** Die Redundanz zwischen `CURRENT_STATE.md`, `NEXT_ACTION.md` und `SESSION_LOG.md` (Abschnitt 2, Punkt 9) entsteht nicht durch schlechtes Prompting, sondern durch Abschnitt „Arbeitsprinzipien" in `PROJECT_BOOTSTRAP.md` selbst, Punkt 6: „Am Ende jedes Jobs aktualisieren: CURRENT_STATE.md, NEXT_ACTION.md, SESSION_LOG.md" — ohne Längen- oder Kürzungsvorgabe. Jede Session befolgt diese Regel korrekt, aber die Regel selbst erzeugt Wachstum ohne Obergrenze.

**Abgeleitete Regeln:**

- Prompts, die Rolle **und** explizite Verbotsliste enthalten, sind der wirksamste beobachtete Hebel gegen Scope-Kriechen — beibehalten, in Abschnitt 6 als Standardformat.
- Die Anweisung „aktualisiere CURRENT_STATE/NEXT_ACTION/SESSION_LOG" braucht eine Längenobergrenze pro Update (siehe Abschnitt 8), sonst wächst die Pflichtlektüre mit jedem Sprint weiter.
- Prompts sollten den Dateikreis explizit eingrenzen („nur diese Dateien lesen/ändern"), statt sich auf die implizite Norm „nicht das ganze Repository lesen" zu verlassen — diese Norm steht zwar in `PROJECT_BOOTSTRAP.md`, wird aber durch die widersprüchliche „Operational"-Klassenliste im selben Dokument untergraben (Abschnitt 2, Punkt 1).

---

## 6. Optimaler Prompt-Aufbau

```
ZIEL: [Ein Satz, konkretes Ergebnis, kein offener Rahmen]

ARBEITSMODUS: [Rolle, z. B. "Editor", "Release Manager", "Research Assistant" —
und explizit NICHT: Framework-Architekt / Herausgeber, sofern nicht zutreffend]

ERLAUBTE DATEIEN:
- [explizite Pfade oder Muster, z. B. "nur 04_book_analysis/<Buch>/ und zugehörige
  03_knowledge_base/-Objekte mit Source-ID <SRC-XXXX>"]

VERBOTENE DATEIEN / AKTIONEN:
- Keine Framework-Änderungen ohne Freigabe
- Keine neuen Wissensobjekte außerhalb des genannten Buchs
- Kein Lesen von 00_project/*_REPORT.md, sofern nicht namentlich verlangt
- [ggf. weitere projektspezifische Verbote]

SUCHGRENZEN:
- Kein rekursiver Scan über 03_knowledge_base/ oder 00_project/ ohne
  ausdrückliche Freigabe in diesem Prompt
- Bei Unsicherheit über betroffene Dateien: Rückfrage statt Breitscan

ÄNDERUNGSGRENZEN:
- [z. B. "Nur die drei genannten Dateien ändern", "Keine Governance-Dateien
  außer CURRENT_STATE/NEXT_ACTION/SESSION_LOG"]

AUSGABEFORMAT:
- [Templatepfad aus 01_framework/08_templates/, falls Wissensobjekt]
- Chat-Antwort: erledigt / geänderte Dateien / nächster Schritt — keine
  Zwischenberichte im Chat

ABBRUCHBEDINGUNGEN:
- Primärquelle fehlt oder ist nicht zugänglich
- Canonicalisierungsentscheidung nicht eindeutig möglich
- Framework-Widerspruch blockiert die Aufgabe

RÜCKFRAGE-REGELN:
- Bei Unsicherheit über Klassifikation: Datei mit ⚠ anlegen, dokumentieren,
  weiterarbeiten (siehe COWORK_EXECUTION_PROTOCOL.md §3.1)
- Nur bei echter Herausgeberentscheidung anhalten, nicht bei normaler
  fachlicher Unsicherheit
```

Dieses Format macht explizit, was `PROJECT_BOOTSTRAP.md` implizit voraussetzt (Dateibegrenzung, keine Breitscans) und ergänzt es um das, was in der Stichprobe fehlte: eine harte Suchgrenze und eine explizite Änderungsgrenze pro Prompt statt einer allgemeinen Norm im Bootstrap-Dokument.

---

## 7. Sessionstart

Konkreter Ablauf, ersetzt die aktuell parallel geltenden vier Bootstrap-Varianten (Abschnitt 4):

1. `PROJECT_BOOTSTRAP.md` lesen (6,1 KB) — einziger Startpunkt.
2. `CURRENT_STATE.md` lesen — **nur der obere „Stand"-Block** (Zeilen 1–8 in der jetzigen Struktur), nicht die vollständige Sprint-Historie darunter. Maximale Ziellänge: ~40 Zeilen / ~1.500 Token (siehe Abschnitt 8 zur Umsetzung).
3. `00_project/NEXT_ACTION.md` lesen — **nur den aktuellen Abschnitt „Aktuelle Aktion"**, nicht die darunterliegenden „Vorheriger Sprint"-Blöcke. Maximale Ziellänge: ~30 Zeilen.
4. Erst danach: aufgabenspezifische Dateien laden, exakt die im Prompt genannten oder unmittelbar referenzierten.

Reihenfolge ist strikt sequenziell — Schritt 2 erst nach Schritt 1, da `PROJECT_BOOTSTRAP.md` die Interpretationsregel für `CURRENT_STATE.md` liefert (z. B. Statusdefinitionen).

**Wann weiterer Kontext geladen werden darf:** Sobald die Aufgabe einen konkreten Objekttyp, ein konkretes Buch oder eine konkrete Entscheidung benennt — dann gezielt die zugehörige(n) Datei(en), nie den übergeordneten Ordner.

**Wann vorher gefragt werden muss:** Wenn der Prompt weder eine Rolle noch einen Dateikreis nennt (siehe Abschnitt 6) und die Aufgabe mehr als eine plausible Interpretation zulässt — insbesondere bei Formulierungen wie „schau dir das Repository an" ohne weitere Eingrenzung.

**Wann `CURRENT_STATE.md` gelesen werden darf/muss:** Immer als Schritt 2 des Sessionstarts — aber nur der Statusblock, nicht die vollständige Datei. Eine Volllesung ist nur gerechtfertigt, wenn die Aufgabe selbst eine historische Rekonstruktion verlangt (z. B. „fasse die Entwicklung seit Version 0.9 zusammen").

---

## 8. Repository-Optimierung

Bewertung der in der Aufgabenstellung genannten Maßnahmen — nur mit praktischem Nutzen:

- **`SESSION_BRIEF.md` (neu):** Sinnvoll als Ersatz für die „Operational"-Sammelliste in `PROJECT_BOOTSTRAP.md`. Eine einzige Datei, hart begrenzt auf ca. 1 Bildschirmseite, die den aktuellen Statusblock aus `CURRENT_STATE.md` und die aktuelle Aktion aus `NEXT_ACTION.md` referenziert (nicht dupliziert). Ersetzt keine der Quelldateien, reduziert aber, was routinemäßig gelesen werden muss.
- **Kurzversionen großer Framework-Dateien:** Nicht notwendig — `01_framework/*` ist bereits klein (größte Datei 340 Zeilen, `canonical_knowledge_model.md`) und wird ohnehin nur bei Bedarf geladen (Abschnitt 3). Kein Hebel hier.
- **Strengere `NEXT_ACTION.md`:** Hoher Nutzen. Die Datei sollte bei jedem Sprintabschluss ersetzt, nicht ergänzt werden — der alte Inhalt wandert vollständig in `SESSION_LOG.md` (wo er sachlich hingehört), `NEXT_ACTION.md` bleibt bei der eigenen Titelzeile („genau eine nächste Aktion").
- **Kleinere Sprintdateien:** Kein genereller Bedarf — die Einzelberichte in `00_project/` sind für ihren Einmalzweck (Freeze, Audit, Release) angemessen detailliert. Das Problem ist Verbleib, nicht Größe (siehe Archivierung unten).
- **Bessere Indexdateien:** Der bestehende `08_knowledge_atlas` ist bereits ein guter Index (Knoten-/Kantenliste über alle Wissensobjekt-IDs). Er sollte aktiv für Referenz-/Konsistenzprüfungen genutzt werden, statt ungenutzt als Manifest zu verbleiben — kein neues Werkzeug nötig, nur Nutzung des vorhandenen.
- **Archivierung alter Reports:** Höchster Hebel mit geringstem Risiko. `99_archive/` existiert bereits als Zielort und enthält bislang nur 5 Dateien. Die ~25 abgeschlossenen Version-1.0-Freeze-/Audit-/Release-Berichte sind laut `CURRENT_STATE.md` selbst „unveränderlich" — sie können ohne Informationsverlust nach `99_archive/v1.0_release/` verschoben werden, mit einem Verweis in `CURRENT_STATE.md`. Das entlastet direkt jede Aufgabe, die versehentlich `00_project/` als Ganzes durchsucht.
- **Klare Dateiklassen:** Bereits vorhanden (Tabelle in `PROJECT_BOOTSTRAP.md`), aber die Klasse „Operational" ist zu weit gefasst (Abschnitt 2, Punkt 1) und CLAUDE_BOOTSTRAP.md trägt die Klasse „Archived", liegt aber weiterhin am Root neben aktiven Dateien. Empfehlung: Klassifizierung präzisieren (siehe unten) und tatsächlich danach verschieben, nicht nur deklarieren.
- **Verbot rekursiver Scans ohne Freigabe:** Sollte explizit in `PROJECT_BOOTSTRAP.md` ergänzt werden (aktuell nur implizit über „nicht unnötig das ganze Repository lesen"). Konkret: kein `find`/Volltextsuche über `03_knowledge_base/` oder `00_project/` ohne expliziten Auftrag im Prompt.

**Empfohlene Präzisierung der „Operational"-Klasse** (ersetzt die aktuelle 8-Dateien-Liste in `PROJECT_BOOTSTRAP.md`):

| Datei | Neue Klasse |
|---|---|
| `CURRENT_STATE.md` (nur Statusblock) | Operational — jede Session |
| `00_project/NEXT_ACTION.md` (nur aktuelle Aktion) | Operational — jede Session |
| `00_project/backlog.md` | Operational — nur bei Task-Auswahl |
| `00_project/SESSION_LOG.md` | Reference — nur bei Historienfrage |
| `00_project/OPEN_DECISIONS.md` | Reference — nur bei Entscheidungsarbeit |
| `00_project/task_rules.md` | Reference — nur bei Buchanalyse-Start |
| `00_project/SCIENTIFIC_DEBT.md` | Reference — nur bei Evidenz-/Qualitätsarbeit |
| `00_project/REPOSITORY_KPIS.md` | Reference — nur bei Reporting/Release |

---

## 9. Claude-Cowork-spezifische Regeln

Nicht allgemein für LLMs, sondern spezifisch für die hier beobachtbare Cowork-Konstellation (lokales Repository, direkte Dateibearbeitung, manuelle Git-Commits durch Felix, keine automatische Qualitätskontrolle außerhalb des Repositorys):

1. **Kein Directory-Scan ohne benannten Zweck.** Da Cowork direkten Dateizugriff hat, ist ein unspezifischer `find`/Volltext-Scan über `00_project/` oder `03_knowledge_base/` technisch billig auszuführen, aber teuer im Kontextfenster. Vor jedem rekursiven Scan: prüfen, ob eine gezielte Pfad- oder ID-Suche genügt.
2. **Git-Commit-Stand nicht als Wahrheitsquelle für „aktuell" behandeln.** Mit nur 4 Commits über die gesamte Historie liegt vermutlich uncommitteter oder in großen Blöcken committeter Stand vor. Cowork sollte sich auf den Dateisystemzustand verlassen, nicht auf `git log`, wenn es um aktuellen Inhalt geht — aber `git diff`/`git status` aktiv nutzen, bevor Dateien als „bereits erledigt" angenommen werden, falls Felix zwischen Sessions manuell per PowerShell committet hat.
3. **Keine Qualitätskontrolle außerhalb des Repositorys voraussetzen.** Da es keine externe CI/Validierung gibt, muss jede Session, die Wissensobjekte anlegt, die Canonicalisierungsprüfung selbst und vollständig durchführen (wie in `PROJECT_BOOTSTRAP.md` beschrieben) — Abkürzungen bei dieser Prüfung sind hier riskanter als in einem Setup mit nachgelagerter Prüfung.
4. **Transparenzlücke über Kontextverbrauch aktiv kompensieren.** Da Cowork keine native Anzeige des tatsächlichen Tokenverbrauchs pro Session hat, sollte jede Session, die mehr als die drei Kern-Bootstrap-Dateien lädt, dies im Chat kurz benennen („zusätzlich gelesen: X, weil Y"), damit Felix ohne technisches Tooling nachvollziehen kann, wo Kontext verbraucht wurde.
5. **Direkte Dateibearbeitung heißt: keine „Entwurf im Chat, dann Datei"-Schleifen bei bereits stabilen Formaten.** Für templatekonforme Wissensobjekte (ST/A/MEC/P/T/MOD) sollte direkt in die Datei geschrieben werden, nicht zuerst im Chat vorgeschlagen und nach Bestätigung erneut geschrieben — das verdoppelt Tokenverbrauch ohne Qualitätsgewinn, sofern das Template ohnehin bindend ist.

---

## 10. Qualitätsrisiken

| Maßnahme | Risiko | Gegenmaßnahme | Wann trotzdem sinnvoll | Wann nicht sinnvoll |
|---|---|---|---|---|
| `CURRENT_STATE.md` auf Statusblock kürzen | Verlust von Begründungskontext, der aktuell direkt im Statusblock mitgeliefert wird (z. B. warum eine Entscheidung fiel) | Verweise auf den vollständigen Sprintbericht statt Volltext-Duplikat im Statusblock | Immer, sofern der Verweis funktional bleibt | Nicht sinnvoll, wenn der referenzierte Sprintbericht selbst archiviert und schwer auffindbar wird — dann Verweispfad zusätzlich prüfen |
| „Operational"-Klasse verkleinern | Eine Session könnte eine tatsächlich relevante Datei (z. B. `OPEN_DECISIONS.md` bei einer Aufgabe mit versteckter Governance-Implikation) übersehen | Klare Reference-Klasse mit Trigger-Bedingung statt ersatzlosem Streichen (siehe Tabelle Abschnitt 8) | Bei klar abgegrenzten Aufgaben (Buchanalyse, Einzeldatei-Änderung) | Bei Aufgaben mit unklarem Umfang oder Release-/Freeze-Charakter — dort lieber einmal mehr laden |
| Archivierung der Version-1.0-Berichte nach `99_archive/` | Zukünftige Aufgaben, die einen alten Bericht brauchen, finden ihn nicht mehr am erwarteten Pfad | Verweisliste in `CURRENT_STATE.md` oder `INDEX.md` pflegen, die auf die neuen Archivpfade zeigt | Für alle als „unveränderlich" erklärten, abgeschlossenen Berichte (Version 1.0) | Nicht für `backlog.md`, `task_rules.md`, `NEXT_ACTION.md` — diese sind aktiv, keine Kandidaten |
| `SESSION_LOG.md` nicht mehr standardmäßig laden | Verlust der schnellen Anschlussfähigkeit an „was geschah in der letzten Session" ohne expliziten Prompt-Hinweis | `NEXT_ACTION.md`/Statusblock liefert bereits das Nötige für Anschlussfähigkeit; `SESSION_LOG.md` bleibt für explizite Historienfragen abrufbar | Wenn `NEXT_ACTION.md` diszipliniert auf eine Aktion begrenzt bleibt (siehe Abschnitt 8) | Wenn `NEXT_ACTION.md` weiterhin unkontrolliert wächst — dann ist es kein valider Ersatz mehr |
| Einen einzigen Bootstrap-Einstieg statt vier | Falls einzelne, in `CLAUDE_BOOTSTRAP.md`/`INDEX.md` genannte Dateien (z. B. `LANGUAGE_POLICY.md`) tatsächlich in jeder Session relevant sind, aber nicht in `PROJECT_BOOTSTRAP.md` erwähnt werden | Prüfen, ob `LANGUAGE_POLICY.md` (952 B, sehr klein) in `PROJECT_BOOTSTRAP.md` als Kurzverweis aufgenommen werden soll, bevor `CLAUDE_BOOTSTRAP.md`/`INDEX.md` archiviert werden | Nach einmaliger Inhaltsprüfung durch Felix, ob etwas Relevantes ausschließlich in den älteren Dateien steht | Nicht ohne diese Prüfung — sonst geht eine tatsächlich geltende Regel (z. B. Sprachregelung) verloren |

---

## 11. Maßnahmenplan

### Sofortmaßnahmen (kein Repository-Eingriff, nur Prompting/Verhalten)

| Maßnahme | Aufwand | Tokenersparnis | Geschwindigkeitsgewinn | Qualitätsauswirkung | Priorität |
|---|---|---|---|---|---|
| Prompt-Format aus Abschnitt 6 ab sofort verwenden (Rolle + Dateikreis + Verbotsliste) | Keiner (nur Prompting) | Mittel | Hoch (weniger Rückfragen/Fehlinterpretation) | Neutral bis positiv | Hoch |
| `CURRENT_STATE.md`/`NEXT_ACTION.md` bei Sessionstart nur Kopfabschnitt lesen, Rest nur bei Bedarf | Keiner | Hoch (~15.000 Token/Session) | Hoch | Neutral | Hoch |
| Rekursive Scans nur nach explizitem Prompt-Auftrag | Keiner | Mittel bis hoch (aufgabenabhängig) | Mittel | Neutral | Hoch |

### Maßnahmen für diese Woche (kleine, reversible Repository-Änderungen — zur Freigabe durch Felix)

| Maßnahme | Aufwand | Tokenersparnis | Geschwindigkeitsgewinn | Qualitätsauswirkung | Priorität |
|---|---|---|---|---|---|
| `NEXT_ACTION.md` auf „genau eine Aktion" zurückschneiden, alte „Vorheriger Sprint"-Blöcke nach `SESSION_LOG.md` verschieben (dort stehen sie inhaltlich bereits) | Gering | Hoch (~6.000 Token/Session) | Hoch | Neutral (kein Informationsverlust, nur Verschiebung) | Hoch |
| ~25 abgeschlossene Version-1.0-Berichte nach `99_archive/v1.0_release/` verschieben, Verweisliste in `CURRENT_STATE.md` ergänzen | Mittel (Prüfung jeder Datei nötig, ob wirklich abgeschlossen) | Hoch (~200.000 Token bei künftigen Volltextsuchen über `00_project/`) | Hoch für alle Aufgaben, die `00_project/` durchsuchen | Neutral, sofern Verweisliste gepflegt wird | Hoch |
| `CLAUDE_BOOTSTRAP.md` und `INDEX.md` gegen `PROJECT_BOOTSTRAP.md` abgleichen, danach `CLAUDE_BOOTSTRAP.md` nach `99_archive/` verschieben (Klassifizierung existiert bereits) | Gering | Gering direkt, aber verhindert Fehlleitung neuer Sessions | Hoch (verhindert Fehlstart) | Positiv (weniger Widerspruch) | Mittel-Hoch |
| „Operational"-Klasse in `PROJECT_BOOTSTRAP.md` gemäß Tabelle in Abschnitt 8 präzisieren | Gering | Hoch (~55.000 Token/Session, wenn zuvor wörtlich befolgt) | Hoch | Neutral | Hoch |

### Langfristige Architekturmaßnahmen (größerer Eingriff, nur mit Freigabe)

| Maßnahme | Aufwand | Tokenersparnis | Geschwindigkeitsgewinn | Qualitätsauswirkung | Priorität |
|---|---|---|---|---|---|
| `SESSION_BRIEF.md` als schlanker, referenzierender Ersatz für die heutige Pflichtlektüre-Rolle von `CURRENT_STATE.md`/`NEXT_ACTION.md` einführen | Mittel | Hoch, dauerhaft | Hoch, dauerhaft | Positiv, wenn diszipliniert gepflegt | Mittel |
| `08_knowledge_atlas` aktiv in Konsistenz-/Referenz-Prompts einbinden statt manueller Mehrfachprüfung | Mittel (Prompt-Gewohnheit ändern, kein Codeaufwand — Compiler existiert bereits) | Mittel bis hoch, aufgabenabhängig | Hoch bei Konsistenzprüfungen | Positiv (systematischer als Ad-hoc-Scan) | Mittel |
| Automatisierte Größen-/Wachstumsgrenze für `SESSION_LOG.md`/`CURRENT_STATE.md` (z. B. Skript, das älteste Einträge nach N Sprints automatisch nach `99_archive/` verschiebt) | Hoch (neues Tooling, Freigabepflicht) | Hoch, dauerhaft | Mittel | Neutral, wenn Archivpfad zuverlässig verweist | Niedrig-Mittel |

---

## 12. Konkrete Promptvorlagen

Jede Vorlage folgt dem Format aus Abschnitt 6, verkürzt auf das Nötige.

**1. Buchanalyse**
```
ZIEL: Buch <Titel> (SRC-XXXX) — Statements/Annahmen/Mechanismen/Prinzipien/
Techniken gemäß Pipeline extrahieren, Kapitel <X> bis <Y>.
ARBEITSMODUS: Editor, Wissensextraktion. Nicht Framework-Architekt.
ERLAUBTE DATEIEN: 04_book_analysis/<Titel>/, 02_sources/books/SRC-XXXX*,
zugehörige 03_knowledge_base/*-Objekte mit Source-ID SRC-XXXX,
01_framework/08_templates/*.
VERBOTEN: Framework-Änderungen, neue Templatekategorien, Objekte anderer Bücher.
SUCHGRENZE: Kein Scan über andere Bücher zur "Inspiration" — Canonicalisierung
nur gegen bestehende IDs desselben Objekttyps, per gezielter Suche.
AUSGABE: Wissensobjekte nach Template, Chat-Antwort: Anzahl neuer Objekte +
nächster Schritt.
```

**2. Review-Sprint**
```
ZIEL: Konsistenzreview für <Bereich/Buch/Objekttyp>, Ergebnis als VAL-Report.
ARBEITSMODUS: Reviewer, kein Autor. Keine inhaltlichen Korrekturen ohne
Kennzeichnung als Reviewbefund.
ERLAUBTE DATEIEN: Nur die zu prüfenden Objekte + zugehöriges Template als
Prüfmaßstab.
VERBOTEN: Neue Wissensobjekte, Framework-Änderungen.
SUCHGRENZE: Referenzprüfung über 08_knowledge_atlas/output/edges.csv,
nicht durch Einzelöffnen aller verlinkten Dateien.
AUSGABE: VAL-Report nach Template, offene Fragen explizit gekennzeichnet.
```

**3. Repository-Konsistenzprüfung**
```
ZIEL: Prüfen, ob <konkrete Regel, z. B. "alle P-Objekte referenzieren ≥2 MECs">
repositoryweit eingehalten wird.
ARBEITSMODUS: Auditor.
ERLAUBTE DATEIEN: Nur 03_knowledge_base/<betroffener Objekttyp>/ + Atlas-Output.
VERBOTEN: Korrekturen ohne separate Freigabe — nur Befund melden.
SUCHGRENZE: Ausdrücklich freigegeben für diesen einen Prompt: rekursiver Scan
über den genannten Ordner. Kein Scan über weitere Ordner ohne erneute Freigabe.
AUSGABE: Kurze Befundliste (Datei, Regelverstoß), keine Datei ändern.
```

**4. Framework-Arbeit**
```
ZIEL: <konkrete Framework-Frage/Änderung>, vorab von Felix als
Framework-Änderung freigegeben.
ARBEITSMODUS: Framework-Architekt (nur mit expliziter Freigabe in diesem Prompt).
ERLAUBTE DATEIEN: 01_framework/ + betroffene Templates.
VERBOTEN: Rückwirkende Änderung bestehender Wissensobjekte ohne separaten Auftrag.
SUCHGRENZE: Kein Scan über 03_knowledge_base/, sofern nicht zur Folgenabschätzung
ausdrücklich verlangt.
AUSGABE: Änderungsvorschlag mit Begründung, keine Direktänderung ohne
zweite Bestätigung bei Framework-Dateien.
```

**5. Quellenvalidierung**
```
ZIEL: Prüfen, ob SRC-XXXX korrekt vorliegt, referenziert und Statements
gegen Primärquelle konsistent sind.
ARBEITSMODUS: Validator, keine neue Extraktion.
ERLAUBTE DATEIEN: 02_sources/books/SRC-XXXX*, zugehörige
03_knowledge_base/statements/ mit dieser Source-ID, Primärquelle in 02_sources/.
VERBOTEN: Neue Statements ohne separaten Auftrag.
SUCHGRENZE: Nur Statements mit exakter Source-ID-Übereinstimmung, keine
Volltextsuche über alle Statements.
AUSGABE: Kurzer Validierungsbericht, keine Dateiänderung ohne Bestätigung.
```

**6. Architekturarbeit**
```
ZIEL: <konkrete Architekturfrage, z. B. Ordnerstruktur, Versionsschema>.
ARBEITSMODUS: Systemarchitekt, nur mit ausdrücklicher Freigabe für
strukturelle Vorschläge — keine Umsetzung ohne zweite Freigabe.
ERLAUBTE DATEIEN: Verzeichnisstruktur (Metadaten, nicht Volltext aller Dateien),
betroffene Governance-Dateien.
VERBOTEN: Tatsächliche Verschiebung/Umbenennung ohne explizite zweite Freigabe.
SUCHGRENZE: Struktur-Scan (find/ls) erlaubt, Volltextlesen einzelner Dateien
nur bei konkretem Bedarf.
AUSGABE: Vorschlag mit Vor-/Nachteilen, keine Ausführung in diesem Schritt.
```

**7. Kleiner Dateiänderungsauftrag**
```
ZIEL: <eine konkrete Änderung an einer benannten Datei>.
ARBEITSMODUS: Editor, punktuelle Änderung.
ERLAUBTE DATEIEN: Ausschließlich die genannte Datei + ggf. eine
Referenzdatei zur Prüfung.
VERBOTEN: Änderungen an weiteren Dateien, auch wenn "verwandt".
SUCHGRENZE: Keine — Datei ist bereits benannt.
AUSGABE: Diff-artige Kurzbeschreibung der Änderung im Chat, keine
Zusammenfassung des gesamten Dateiinhalts.
```

---

## Priorisierung (Zusammenfassung)

Höchster Hebel bei geringstem Risiko, in absteigender Reihenfolge: (1) „Operational"-Klasse in `PROJECT_BOOTSTRAP.md` präzisieren, (2) `NEXT_ACTION.md` auf eine Aktion zurückschneiden, (3) abgeschlossene Version-1.0-Berichte archivieren, (4) `CLAUDE_BOOTSTRAP.md` tatsächlich verschieben statt nur zu klassifizieren, (5) Promptformat aus Abschnitt 6 ab sofort anwenden. Alle fünf sind ohne inhaltlichen Eingriff in die Wissensbasis umsetzbar und ändern nichts an den 514 bestehenden Wissensobjekten.
