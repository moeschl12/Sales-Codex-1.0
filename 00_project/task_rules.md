# Task Rules — Deterministisches Task-Generierungssystem

Version: 1.0  
Stand: 2026-06-27  
Geltungsbereich: Alle Buchanalysen im Sales Codex Repository  
Autorität: Dieses Dokument gilt ab v1.0. Änderungen nur durch Felix.

---

## 1. Zweck

Dieses Dokument definiert die Regeln, nach denen Cowork aus dem Book Catalog (`02_sources/book_catalog.md`) deterministisch konkrete Arbeitsaufträge ableitet.

Ziel ist, dass der Herausgeber keine einzelnen Tasks mehr formulieren muss. Es genügt, ein Buch im Catalog auf `READY` zu setzen. Cowork leitet daraus alle notwendigen Arbeitsschritte ab, erstellt einen Vorschlag und wartet auf Freigabe.

Dieses Dokument ist keine allgemeine Projektmanagement-Anleitung. Es ist eine Verhaltensregel für Cowork, die auf der Sequenzierungslogik des Operating Manual und den Erkenntnissen aus Pilot 001 aufbaut.

---

## 2. Eingaben

Das Task-Generierungssystem benötigt folgende Eingaben:

| Eingabe | Pfad | Pflichtinhalt |
|---|---|---|
| Book Catalog | `02_sources/book_catalog.md` | Buch-ID, Titel, Autor, Status, Priorität |
| Repository-Scan | `03_knowledge_base/` | Existierende Wissensobjekte mit Source-ID-Feld |
| Book Analysis | `04_book_analysis/[Titel]/analysis.md` | Kapitelstruktur-Tabelle (falls vorhanden) |
| Quellen-Verzeichnis | `02_sources/books/` | Existierende SRC-Dateien |
| Projekt-Verzeichnis | `00_project/` | Existierende VAL-Dateien |

Das System liest ausschließlich diese Dateien. Es nutzt keine Erinnerung aus vergangenen Sessions.

---

## 3. Ausgaben

Das Task-Generierungssystem erzeugt ausschließlich eine Vorschlagsdatei:

```
00_project/task_proposal_[B-ID]_[slug].md
```

Beispiel: `00_project/task_proposal_B-0002_influence.md`

Der Slug entspricht dem Buchtitel in Kleinbuchstaben, Leerzeichen durch Unterstriche ersetzt.

**Was die Ausgabe enthält:**

- Buchkontext (ID, Titel, Autor, Priorität)
- Erkannter Repository-Zustand (was existiert bereits, was fehlt)
- Vollständige Aufgabenliste in Ausführungsreihenfolge
- Je Task: Typ, Abhängigkeiten, Ausgabepfad, anzuwendendes Template, Abbruchbedingungen
- Hinweis auf erforderliche Herausgeber-Freigabe

**Was die Ausgabe nicht enthält:**

- Inhaltliche Urteile über das Buch
- Evidenzklassen-Entscheidungen
- Empfehlungen zur Framework-Änderung
- Git-Commit-Anweisungen

---

## 4. Statuslogik aus dem Book Catalog

### 4.1 Statusdefinitionen

Das System arbeitet mit diesen Statusstufen aus `02_sources/book_catalog.md`:

| Status | Bedeutung für das System |
|---|---|
| IDEA | Kein Task wird erzeugt. |
| WAITING | Kein Task wird erzeugt. |
| READY | **Auslöser:** Cowork erzeugt einen Task-Vorschlag. |
| IN_PROGRESS | Cowork arbeitet den freigegebenen Backlog ab. |
| REVIEW | Cowork wartet auf Herausgeber-Entscheidung. Kein neuer Task-Vorschlag. |
| DONE | Abgeschlossen. Kein Task wird erzeugt. |
| ARCHIVED | Kein Task wird erzeugt. |

### 4.2 Aktivierungsregel

Das System aktiviert sich auf genau einem Buch: dem ersten Eintrag im Catalog mit Status `READY`.

Wenn mehrere Bücher `READY` sind, wird das mit der niedrigsten Buch-ID (B-XXXX) gewählt. Abweichungen erfordern eine ausdrückliche Herausgeberanweisung.

### 4.3 Statusübergänge durch Cowork

Cowork darf folgende Statusübergänge eigenständig vornehmen:

| Von | Nach | Bedingung |
|---|---|---|
| READY | IN_PROGRESS | Herausgeber hat Task-Vorschlag freigegeben und ersten Task bestätigt |
| IN_PROGRESS | REVIEW | Alle Tasks abgeschlossen, VAL-Report erstellt |

Folgende Statusübergänge sind ausschließlich Herausgeber-Entscheidung:

| Von | Nach |
|---|---|
| WAITING | READY |
| REVIEW | DONE |
| DONE | ARCHIVED |

---

## 5. Ableitungsmatrix

Die Ableitungsmatrix definiert, welcher fehlende Zustand welchen Task erzeugt. Die Reihenfolge ist verbindlich. Spätere Tasks werden nicht freigegeben, bevor die Abhängigkeiten erfüllt sind.

### 5.1 Ausführungsreihenfolge

```
SCHRITT 1 — Quelle erfassen (SRC)
SCHRITT 2 — Kapitelstruktur erfassen (analysis.md anlegen)
SCHRITT 3 — Statements extrahieren (ST), kapitelweise
SCHRITT 4 — Annahmen identifizieren (A)
SCHRITT 5 — Mechanismen ableiten (MEC)
SCHRITT 6 — Prinzipien formulieren (P)
SCHRITT 7 — Techniken erfassen (T)
SCHRITT 8 — Modelle aktualisieren (MOD)
SCHRITT 9 — Selbstreview durchführen (VAL)
SCHRITT 10 — Abschlussbericht erstellen
```

Diese Reihenfolge entspricht dem Operating Manual (Kapitel 3) und der im Execution Protocol (Abschnitt 2.2) dokumentierten Sequenzierungslogik.

### 5.2 Task-Ableitungsregeln

| Bedingung | Erzeugter Task | Template | Ausgabepfad |
|---|---|---|---|
| Keine SRC-Datei vorhanden | „Quelle erfassen — [Titel]" | `source_template.md` | `02_sources/books/SRC-XXXX_[slug].md` |
| SRC vorhanden, analysis.md fehlt | „Kapitelstruktur erfassen — [Titel]" | `book_analysis_template.md` | `04_book_analysis/[Titel]/analysis.md` |
| analysis.md vorhanden, STs fehlen oder unvollständig | „Statements extrahieren — [Titel] Kapitel N" (ein Task pro Kapitel) | `statement_template.md` | `03_knowledge_base/statements/ST-XXXX_[slug].md` |
| STs vollständig, As fehlen | „Annahmen identifizieren — [Titel]" | `assumption_template.md` | `03_knowledge_base/assumptions/A-XXXX_[slug].md` |
| As vollständig, MECs fehlen | „Mechanismen ableiten — [Titel]" | `mechanism_template.md` | `03_knowledge_base/mechanisms/MEC-XXXX_[slug].md` |
| MECs vollständig, Ps fehlen | „Prinzipien formulieren — [Titel]" | `principle_template.md` | `03_knowledge_base/principles/P-XXXX_[slug].md` |
| Ps vollständig, Ts fehlen | „Techniken erfassen — [Titel]" | `technique_template.md` | `03_knowledge_base/techniques/T-XXXX_[slug].md` |
| Ts vollständig, MODs veraltet | „Modelle aktualisieren nach [Titel]" | `model_template.md` | `03_knowledge_base/models/MOD-XXXX_[slug].md` |
| Alle Objekte vollständig, VAL fehlt | „Selbstreview durchführen — [Titel]" | `validation_report_template.md` | `04_book_analysis/[Titel]/VAL-XXXX_consistency_review_[slug].md` |
| VAL vorhanden, Abschlussbericht fehlt | „Abschlussbericht erstellen — [Titel]" | (Abschnitt 9 des Operating Manual) | `00_project/PILOT_XXXX_ABSCHLUSSBERICHT.md` oder equivalent |

### 5.3 Vollständigkeitsdefinition

Ein Objekt-Typ gilt als **vollständig**, wenn:

1. Mindestens ein Objekt dieses Typs existiert, das diese SRC-ID im Source-ID-Feld trägt, **und**
2. Das Statusfeld dieser Objekte nicht den Wert `Entwurf` hat, **und**
3. Keine offenen ⚠-Markierungen in der analysis.md auf fehlende Objekte dieses Typs hinweisen.

Ein Kapitel gilt als **vollständig analysiert**, wenn die analysis.md für dieses Kapitel einen Abschnitt mit Statements, Annahmen und Mechanismen enthält und der Abschnitt nicht mit `[ausstehend]` oder equivalent markiert ist.

### 5.4 Umgang mit unvollständiger Kapitelstruktur

Wenn die analysis.md zwar existiert, aber noch keine Kapitelstruktur-Tabelle enthält (z.B. weil sie nur teilweise befüllt wurde), erzeugt das System keinen ST-Extraktions-Task. Stattdessen erzeugt es zunächst den Task „Kapitelstruktur ergänzen — [Titel]".

ST-Extraktions-Tasks werden erst nach vollständiger Kapitelstruktur-Tabelle erzeugt. Die Kapitelanzahl aus der Tabelle bestimmt die Task-Anzahl.

---

## 6. Regeln für die Kapitelstruktur

### 6.1 Pflichtfeld am Anfang der analysis.md

Jede `analysis.md`-Datei muss unmittelbar nach dem Titel eine Kapitelstruktur-Tabelle enthalten. Diese Tabelle ist Voraussetzung für die Erzeugung kapitelweiser ST-Extraktions-Tasks.

**Pflichtformat der Kapitelstruktur-Tabelle:**

```markdown
## Kapitelstruktur

| Nr. | Titel (original) | Titel (DE) | Status |
|---|---|---|---|
| 1 | [Originaltitel] | [Übersetzung] | ausstehend / analysiert |
| 2 | … | … | … |
```

**Status-Werte:**

| Wert | Bedeutung |
|---|---|
| `ausstehend` | Kapitel noch nicht analysiert |
| `analysiert` | Kapitel vollständig analysiert, Objekte angelegt |

### 6.2 Woher kommt die Kapitelstruktur?

Die Kapitelstruktur wird aus dem Primärtext des Buches entnommen. Wenn der Primärtext nicht zugänglich ist, wird die Tabelle mit `⚠ Kapitelstruktur aus Trainingswissen — Verifikation gegen Primärtext erforderlich` markiert.

Kapitelstruktur aus Trainingswissen ist erlaubt, um die Arbeit zu starten. Sie wird nicht als vollständig behandelt, bis sie gegen das physische Buch geprüft wurde.

### 6.3 Änderungen an der Kapitelstruktur

Wenn sich im Verlauf der Analyse herausstellt, dass die Kapitelstruktur unvollständig oder fehlerhaft ist, wird die Tabelle korrigiert und die Abweichung im VAL-Report dokumentiert. Es werden keine neuen Tasks eigenständig erzeugt — die Korrektur wird dem Herausgeber mitgeteilt.

---

## 7. Regeln für die Source-ID

### 7.1 Pflichtfeld in allen neu erzeugten Wissensobjekten

Jedes Wissensobjekt, das ab diesem Dokument (v1.0) erstellt wird, muss ein explizites Source-ID-Feld enthalten. Dieses Feld ermöglicht dem State Inspector, Objekte einem Buch zuzuordnen.

**Pflichtfeld:**

```markdown
## Source ID

SRC-XXXX
```

Dieses Feld steht direkt nach der Objekt-ID und dem Namen — vor allen inhaltlichen Feldern.

### 7.2 Positionierung im Objekt

```markdown
# [Objekt-Typ]-XXXX — [Name]

## [Objekt-Typ] ID
[Objekt-Typ]-XXXX

## Source ID
SRC-XXXX

## Name
[Vollständiger Name]

[...weitere Felder gemäß Template...]
```

### 7.3 Mehrere Quellen

Wenn ein Objekt auf mehrere Quellen zurückgeführt wird (z.B. ein Mechanismus, der in zwei Büchern beschrieben wird), werden alle Source-IDs kommagetrennt eingetragen:

```markdown
## Source ID

SRC-0001, SRC-0002
```

### 7.4 Bestehende Objekte ohne Source-ID-Feld

Objekte, die vor diesem Dokument erstellt wurden (Pilot 001 — SPIN Selling), haben kein Source-ID-Feld. Der State Inspector erkennt diese als zu SRC-0001 gehörend, wenn sie im Freitext-Feld `## Quelle` eine SRC-0001-Referenz enthalten.

Eine rückwirkende Ergänzung des Source-ID-Feldes in bestehenden Objekten ist sinnvoll, aber kein blockierender Schritt. Sie kann als separater Task aufgenommen werden, wenn der Herausgeber dies entscheidet.

### 7.5 Source-ID bei Herkunft aus dem Research Program (RC-1)

Objekte, die aus einem Forschungsprojekt des Research Program (`06_research_program/`) integriert werden, tragen im Pflichtfeld "Source ID" die Projekt-ID statt einer `SRC-ID`:

```markdown
## Source ID

W-XXX (Research Program)
```

Wird ein Objekt sowohl durch eine Buchquelle als auch durch ein Forschungsprojekt gestützt, gilt Abschnitt 7.3 (kommagetrennte Mehrfachangabe) entsprechend: `SRC-0004, W-001`. Der vollständige Integrationsablauf ist beschrieben in `06_research_program/REPOSITORY_INTEGRATION.md`; die Kompatibilität mit der Objektidentitätslogik dieses Abschnitts ist in `01_framework/05_knowledge_model/canonical_knowledge_model.md`, Abschnitt 11 bestätigt.

---

## 8. Regeln für Task-Proposals

### 8.1 Vorschlag vor Ausführung

Das Task-Generierungssystem führt keine Arbeit eigenständig aus. Es erzeugt ausschließlich einen Vorschlag. Erst nach ausdrücklicher Freigabe durch den Herausgeber wird die Aufgabenliste in `00_project/backlog.md` übertragen.

**Freigabe bedeutet:** Der Herausgeber bestätigt den Vorschlag explizit. Eine stillschweigende Übernahme findet nicht statt.

### 8.2 Inhalt der Vorschlagsdatei

```markdown
# Task-Vorschlag — [B-ID] [Titel]

Erstellt: [Datum]
Status: VORSCHLAG — wartet auf Herausgeber-Freigabe

## Buchkontext

| Feld | Wert |
|---|---|
| Buch-ID | B-XXXX |
| Titel | … |
| Autor | … |
| Priorität | P1–P4 |
| Erwartete SRC-ID | SRC-XXXX |

## Erkannter Repository-Zustand

| Objekt-Typ | Zustand |
|---|---|
| SRC-Datei | vorhanden / fehlt |
| analysis.md | vorhanden (N Kapitel) / fehlt |
| Statements (ST) | N vorhanden / fehlt |
| Annahmen (A) | N vorhanden / fehlt |
| Mechanismen (MEC) | N vorhanden / fehlt |
| Prinzipien (P) | N vorhanden / fehlt |
| Techniken (T) | N vorhanden / fehlt |
| Modelle (MOD) | aktuell / veraltet / fehlt |
| VAL-Report | vorhanden / fehlt |

## Abgeleitete Aufgaben

| # | Task | Typ | Abhängigkeit | Ausgabepfad |
|---|---|---|---|---|
| 1 | … | EXTRAKTION / ANALYSE / REVIEW / INTEGRATION | — | … |
| 2 | … | … | Task 1 | … |

## Hinweis

Dieser Vorschlag wird erst nach ausdrücklicher Freigabe durch Felix in den Backlog übernommen.
```

### 8.3 Übernahme in den Backlog

Nach Freigabe durch den Herausgeber werden die Tasks in `00_project/backlog.md` unter `READY` eingetragen. Der erste Task erhält den Status `READY`, alle weiteren den Status `WAITING` (bis die Abhängigkeit erfüllt ist).

### 8.4 Nachträgliche Änderungen

Wenn der Herausgeber einen Task-Vorschlag teilweise ablehnt oder ändert, wird der Vorschlag entsprechend angepasst und neu vorgelegt. Cowork interpretiert keine Teilfreigaben — es gibt entweder eine vollständige Freigabe oder eine neue Vorschlagsversion.

### 8.5 Gleichzeitige Vorschläge

Es darf nur ein aktiver Vorschlag gleichzeitig existieren. Bevor ein neuer Vorschlag erzeugt wird, muss der vorherige entweder freigegeben oder explizit verworfen sein.

---

## 9. Grenzen des Systems

### 9.1 Was das System nicht tut

| Bereich | Regel |
|---|---|
| Git-Commits | Niemals. Git-Operationen sind ausschließlich Herausgeber-Aufgabe. |
| Evidenzklassen | Das System erzeugt Tasks, keine Evidenzurteile. Evidenzklassen werden im Zuge der Extraktion vergeben, nicht durch das Task-Generierungssystem. |
| Framework-Änderungen | Das System erzeugt keine Tasks, die Templates, Ordnerstrukturen oder Methodik ändern. |
| Neue Template-Kategorien | Das System verwendet ausschließlich bestehende Templates aus `01_framework/08_templates/`. |
| Inhaltsvorannahmen | Das System antizipiert keine Kapitelinhalte. Kapitelstruktur und Objektanzahl werden aus der analysis.md gelesen. |
| Quellen erfinden | Das System erfindet keine bibliographischen Angaben. Fehlt ein physisches Buch, wird dies markiert — nicht umgangen. |
| Ethische Entscheidungen | Ethische Grenzfälle werden immer an Felix eskaliert. Das System markiert sie im Task-Vorschlag, trifft aber keine Urteile. |

### 9.2 Abbruchbedingungen

Das System stoppt und eskaliert an Felix, wenn:

- Kein Buch mit Status `READY` im Catalog vorhanden ist.
- Für das aktive Buch bereits ein nicht-freigegebener Vorschlag existiert.
- Die Kapitelstruktur in analysis.md fehlt und der Primärtext ist nicht zugänglich.
- Ein Task-Vorschlag erzeugt würde, der Framework-Änderungen impliziert.
- Ein aktiver IN_PROGRESS-Task existiert — in diesem Fall werden keine neuen Vorschläge erzeugt, bevor der aktive Task abgeschlossen ist.

### 9.3 Verhältnis zu anderen Steuerungsdokumenten

Dieses Dokument ergänzt das Operating Manual und das Execution Protocol — es ersetzt sie nicht. Bei Widersprüchen gilt:

1. Operating Manual (Schritt-Definitionen und Abbruchbedingungen)
2. Execution Protocol (Entscheidungsregeln und Verhaltensregeln)
3. Dieses Dokument (Task-Generierungslogik)

---

---

## 10. Book Mode (v1.1)

**Dokumentklasse: Operational**

Book Mode ist der Standardarbeitsablauf für alle Buchanalysen ab Sales Codex OS v1.1.

### 10.1 Definition

Nach Freigabe des Task-Proposals durch Felix arbeitet Cowork den vollständigen Workflow durch:

```
SRC → ST → A → MEC → P → T → MOD → VAL → BOOK_REVIEW
```

Keine Zwischenfreigaben. Kein Pausieren nach einzelnen Tasks.

### 10.2 Stopp-Bedingungen

Nur bei folgenden Bedingungen anhalten und eskalieren:

1. Primärquelle (PDF/Buch) nicht zugänglich
2. Unauflösbarer Canonicalisierungskonflikt (zwei korrekte Entscheidungen möglich, keine klare Präferenz)
3. Ethischer Grenzfall
4. Framework-Änderung zur Fortsetzung erforderlich

Normale Unsicherheit ist kein Stopp-Grund. Unsicherheit dokumentieren (⚠), weiterarbeiten.

### 10.3 Pflichtabschluss jeder Session

Am Ende jeder Session — unabhängig davon, ob ein Task abgeschlossen wurde — gilt als letzter Pflichtschritt:

1. `CURRENT_STATE.md` aktualisieren (Task-Status, nächste freie IDs)
2. `00_project/NEXT_ACTION.md` aktualisieren (exakt eine nächste Aktion)
3. `00_project/SESSION_LOG.md` Eintrag ergänzen (was getan, was geändert)

Keine Session endet ohne diesen Schritt.

### 10.4 Pflichtschritte innerhalb des Workflows

**Nach TASK-0003 (Statements):**
Kapitelstatustabelle in `analysis.md` aktualisieren — alle analysierten Kapitel auf `analysiert` setzen.

**Prinzipien-Regel (A6):**
Ein Prinzip muss auf **mehrere Mechanismen ODER mehrere Annahmen** zurückgeführt werden — nicht auf einen einzelnen Mechanismus allein. Die OR-Bedingung ist explizit: ≥2 MECs ODER ≥2 A-Objekte (oder eine Kombination). Ein Prinzip, das nur einen MEC und eine A referenziert, erfüllt diese Bedingung nicht.

**Technik vs. Kompetenz:**
Ein T-Objekt wird nur angelegt, wenn das beschriebene Verhalten eine konkrete, wiederholbare Handlung mit definierbaren Auslöse- und Abschlussbedingungen ist. Übergeordnete Fähigkeiten (z.B. Rapport-Aufbau, aktives Zuhören) sind Kompetenzen — sie werden im Feld "Verknüpfte Kompetenzen" referenziert, nicht als T-Objekte angelegt.

### 10.5 Nicht-Anlage-Dokumentation

Wenn ein Kandidat (MEC, P, T) bewusst nicht als eigenes Objekt angelegt wird, muss diese Entscheidung explizit dokumentiert werden — ebenso wie EXTEND- und NEW-Entscheidungen. Dokumentationsort: Übergeordnetes Objekt + ggf. Abschnitt "Verworfene Kandidaten" in `analysis.md`.

---

*Dieses Dokument gilt ab v1.0. Änderungen nur durch Felix. Zuletzt aktualisiert: v1.1 (2026-06-30)*
