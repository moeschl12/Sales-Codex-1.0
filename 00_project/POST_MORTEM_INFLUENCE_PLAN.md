# Post-Mortem Plan — B-0002 Influence

**Zweck:** Strukturierte Auswertung des Influence-Workflows zur Vorbereitung des Book Mode v1.1 und des Framework-Updates.  
**Voraussetzung:** TASK-0010 abgeschlossen (✓ 2026-06-30)  
**Durchführung:** Felix (Herausgeber) + KI-System  
**Status:** Bereit zur Durchführung

---

## Agenda

### 1. Repository-Review

**Ziel:** Qualitätsprüfung der Wissensobjekte.

Fragen:
- Sind alle Wissensobjekte sauber (Source-ID, Querverweise, Evidenzklassen)?
- Gibt es Redundanzen zwischen SRC-0001- und SRC-0002-Objekten?
- Hat das Canonical Knowledge Model funktioniert? (3 MEC-Erweiterungen statt Doppelanlage — war das korrekt?)
- Gibt es verwaiste Referenzen (IDs, die in einem Objekt erwähnt werden, aber keine Datei haben)?
- Sind die Canonicalisierungsentscheidungen (MEC-0001/0003/0004) nachvollziehbar begründet?
- P-0002 aus Pilot-001: MEC-0009 nachpflegen (VAL-0002 Empfehlung)?

**Input:** VAL-0002, analysis.md, BOOK_REVIEW_REPORT_B0002.md

---

### 2. Prozess-Review

**Ziel:** Den Workflow von TASK-0001 bis TASK-0010 auf Effizienz und Engpässe untersuchen.

Fragen:
- Welche Schritte waren unnötig oder überproportional aufwändig?
- Wo musste die KI warten oder nachfragen?
- Wo gab es unnötige Rückfragen oder Unsicherheiten?
- Welche Schritte lassen sich automatisieren (z.B. ID-Vergabe, Source-ID-Check)?
- Hat die Abschaffung der Zwischenfreigaben (ab TASK-0007) die Arbeit beschleunigt?
- War die stateless Agent Architecture effektiv (Repository als Gedächtnis)?
- Wie viel Tokenverbrauch hat eine Context-Window-Grenze verursacht und wie wurde sie überbrückt?

**Beobachtung aus Influence:** Die n:m-Clustering-Methodik für A-Objekte (statt 1:1 aus STs) hat die Qualität der Annahmen merklich verbessert. Die explizite Abgrenzungspflicht für P-Objekte hat tieferes Analysieren erzwungen.

---

### 3. Operating-System-Review

**Ziel:** Entscheidung über Framework-Updates für v1.1.

Punkte:
- **Book Mode offiziell einführen:** Workflow SRC → BOOK_REVIEW als eigenständiger Modus mit definierten Startbedingungen (Primärquelle vorhanden? Backlog angelegt?)
- **Zwischenfreigaben abschaffen:** Nur noch Freigabe am Anfang (Task-Proposal) und am Ende (Post-Mortem). Nicht für jeden TASK einzeln.
- **BOOK_REVIEW als Endstatus definieren:** `BOOK_REVIEW_REPORT_B*.md` als verbindliches Abschlussdokument mit standardisiertem Format.
- **Repository Health Check verpflichtend machen:** VAL-Objekt für jede Quelle als Pflicht-Schritt.
- **Abschlussbericht standardisieren:** BOOK_REVIEW_REPORT-Template anlegen.
- **Abbruchbedingungen schärfen:** Die 5 Abbruchbedingungen sind korrekt — aber brauchen sie einen expliziten "Checkpoint" im Workflow?
- **SESSION_LOG + CURRENT_STATE als Pflicht am Job-Ende:** Bereits eingeführt — in Operating Manual dokumentieren.

---

### 4. Anpassungen nach Post-Mortem

Dokumente, die nach Post-Mortem-Freigabe zu aktualisieren sind:

| Dokument | Änderungsumfang |
|---|---|
| `00_project/SALES_CODEX_OPERATING_MANUAL.md` | Book Mode, Abbruchbedingungen, Session-Log-Pflicht |
| `00_project/COWORK_EXECUTION_PROTOCOL.md` | Stateless Architecture, SESSION_LOG, CURRENT_STATE |
| `00_project/task_rules.md` | Zwischenfreigaben-Regel, BOOK_REVIEW als Endstatus |
| `00_project/backlog.md` | WARTEND-Zeilen für TASK-0005 entfernen (Duplikat) |
| `02_sources/book_catalog.md` | B-0002 auf Status ABGESCHLOSSEN setzen |
| `CURRENT_STATE.md` | Influence als ABGESCHLOSSEN markieren, nächstes Buch |
| `00_project/NEXT_ACTION.md` | Post-Mortem-Ergebnisse als nächste Aktion |
| `01_framework/08_templates/` | BOOK_REVIEW_REPORT-Template anlegen |

---

### 5. Freigabe

**Reihenfolge:**
1. Post-Mortem durchführen (Felix + KI)
2. Framework-Änderungen formulieren (KI-Entwurf)
3. Felix prüft und freigibt Framework v1.1
4. Framework v1.1 einfrieren
5. Nächstes Buch auswählen (OD-004)
6. B-0003 starten

**Grundsatz:** Framework v1.1 wird nicht während der Bucharbeit geändert. Erst Post-Mortem, dann Freeze, dann neues Buch.

---

## Offene Fragen für das Post-Mortem

1. Soll Unity (7. Prinzip, Ausgabe 2021) als Ergänzungsquelle zu B-0002 behandelt werden oder als eigene Quelle (SRC-0003)?
2. Soll Pre-Suasion (Cialdini 2016) direkt nach dem Post-Mortem als B-0003 eingeplant werden?
3. Soll die Gemini-Validierung als eigener TASK-Typ (VAL-extern) in den Workflow aufgenommen werden?
4. Wie wird mit dem Kahneman-Quervergleich umgegangen: als Teil von MOD-0002, als MOD-0003, oder als P-Objekt?

---

*Erstellt: 2026-06-30*
