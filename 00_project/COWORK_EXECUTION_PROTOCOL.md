# Cowork Execution Protocol

Version: 1.0  
Stand: 2026-06-27  
Geltungsbereich: Alle Arbeitssessions von Claude / Cowork im Sales Codex

---

## 1. Zweck

Dieses Dokument beschreibt, wie Claude / Cowork Arbeit im Sales Codex eigenständig organisiert, Entscheidungen trifft, Rückfragen stellt, Arbeitspakete abschließt und den nächsten Schritt ableitet.

Es ist keine allgemeine Projektmanagement-Anleitung. Es ist eine Verhaltensregel, die aus den konkreten Erfahrungen von Pilot 001 abgeleitet wurde.

---

## 2. Arbeit organisieren

### 2.1 Zu Beginn jeder Session

Vor dem ersten Schreibvorgang:

1. `PROJECT_BOOTSTRAP.md` lesen — Überblick über Projektziel, Wissenspipeline, Abbruchbedingungen.
2. `CURRENT_STATE.md` lesen — aktueller Stand: was ist fertig, welche IDs sind frei.
3. `00_project/NEXT_ACTION.md` lesen — exakt eine nächste Aktion und aktuelle Abbruchbedingungen.
4. Nur die direkt betroffenen Arbeitsdateien lesen — nicht das gesamte Repository.
5. Aufgabenliste anlegen (TaskCreate) — aufgeteilt nach Objekttyp oder Kapitel.

Keine Datei schreiben, bevor diese Lektüre abgeschlossen ist.

### 2.2 Sequenzierung

Reihenfolge der Objekterstellung:

```
Quelle (SRC) → Statements (ST) → Annahmen (A) → Mechanismen (MEC) → Prinzipien (P) → Techniken (T) → Modelle (MOD)
```

**Warum diese Reihenfolge:**  
Prinzipien müssen Mechanismen per ID referenzieren. Wenn Mechanismen vor Prinzipien angelegt werden, sind die IDs verfügbar. Umgekehrt entstehen Freitextreferenzen, die nachträglich korrigiert werden müssen.

*Gelernt aus Pilot 001: P-0001 und P-0002 mussten nach dem Konsistenz-Review nachträglich aktualisiert werden, weil MEC-Objekte erst nach ihnen angelegt wurden.*

### 2.3 Bündelung

Wenn Dateien keine Abhängigkeiten voneinander haben, werden sie in derselben Phase erstellt — nicht nacheinander mit unnötigen Zwischenschritten. Ordner werden vor den ersten Dateien angelegt.

### 2.4 Aufgabenstatus

- `in_progress` setzen, bevor mit einer Aufgabe begonnen wird.
- `completed` setzen, sobald die Ausgabe vollständig im Repository liegt.
- Nie eine Aufgabe als abgeschlossen markieren, ohne dass die zugehörige Datei existiert.

---

## 3. Entscheidungen treffen

### 3.1 Entscheidungsregeln für häufige Situationen

| Situation | Entscheidung |
|---|---|
| Kapitelzuordnung einer Aussage unklar | Statement anlegen, Zuordnung mit ⚠ markieren, weiterarbeiten |
| Aussage ist Beobachtung oder Interpretation? | Beide Ebenen im Objekt dokumentieren, nicht entscheiden — das ist Herausgeber-Aufgabe |
| Objekt passt in zwei Kategorien (z.B. Statement oder Annahme?) | Im Zweifel Statement — konservativste Klassifikation |
| Mechanismus-Kandidat erkennbar, aber noch kein Objekt vorhanden | Als offenen Kandidaten in P-Objekt markieren (⚠ noch kein MEC-Objekt), nicht spontan MEC anlegen |
| Neue Template-Kategorie sinnvoll? | Nicht anlegen. Als offene Frage dokumentieren, Herausgeber entscheiden lassen |
| Evidenzklasse unsicher | Niedrigere Klasse wählen, Begründung angeben |
| Ethisches Risiko unklar | "Mittel" setzen, offene Frage dokumentieren |

### 3.2 Was keine Entscheidung erfordert

- Dateinamen nach Namenskonvention: immer Englisch, ID-Präfix, beschreibender Slug.
- Inhaltssprache: immer Deutsch.
- Template-Auswahl: immer das engste passende Template aus `01_framework/08_templates/`.
- Unsicherheitsmarkierung: immer explizit, nie weglassen.

### 3.3 Was grundsätzlich nicht eigenständig entschieden wird

- Framework-Änderungen
- Neue Template-Kategorien
- Stufung eines Quellenprinzips zum Codex-Prinzip (E3+)
- Ethische Grenzfälle

Diese Punkte werden gestoppt, dokumentiert und an Felix eskaliert.

---

## 4. Rückfragen stellen

### 4.1 Wann eine Rückfrage nötig ist

Eine Rückfrage ist nötig, wenn ohne die Antwort ein substanzieller Teil der Arbeit falsch wäre — nicht wenn ein Teil unsicher ist.

Unsicherheit ist kein Grund für eine Rückfrage. Unsicherheit wird markiert.

Echte Rückfragegründe:
- Arbeitsauftrag ist inhaltlich widersprüchlich.
- Primärquelle ist nicht zugänglich und der Arbeitsauftrag setzt sie voraus.
- Eine ethische Grenzlinie ist erkennbar.

### 4.2 Wann keine Rückfrage gestellt wird

- Kapitelzuordnung unsicher → ⚠ setzen, weiterarbeiten.
- Evidenzklasse unsicher → konservativ einschätzen, begründen.
- Mechanismus unvollständig belegt → E-Niveau trennen (allg. Mechanismus / spez. Anwendung), offene Frage dokumentieren.
- Objektklassifikation unklar → konservativste Klasse wählen, Frage in Offene Fragen des Objekts festhalten.

### 4.3 Format einer Rückfrage

Rückfragen werden nicht als allgemeine Unsicherheitsbekundung formuliert.  
Format: Kontext — konkrete Frage — zwei Optionen mit Konsequenz.

Beispiel:  
*"Kapitel 2 oder 3 als Quelle für ST-0004 (Vier Gesprächsergebnisse)? Option A: Kapitel 2 → Objekt wird im Closing-Block abgelegt. Option B: Kapitel 1 → Objekt wird im Rahmensetzungsblock abgelegt. Derzeit als tentativ Kapitel 1 markiert."*

---

## 5. Arbeitspakete abschließen

### 5.1 Definition of Done für ein Wissensobjekt

Ein Wissensobjekt gilt als abgeschlossen, wenn:

- [ ] Die Datei liegt im richtigen Ordner mit korrekter ID und korrektem Dateinamen.
- [ ] Alle Pflichtfelder des Templates sind ausgefüllt.
- [ ] Unsicherheiten sind mit ⚠ markiert.
- [ ] Mechanismen sind per MEC-ID referenziert (nicht nur per Freitext).
- [ ] Evidenzklasse ist gesetzt und begründet.
- [ ] Grenzen und Gegenbeispiele sind vorhanden.
- [ ] Status ist gesetzt (Entwurf / geprüft / ...).

### 5.2 Definition of Done für eine Buchanalyse

Eine Buchanalyse gilt als abgeschlossen, wenn:

- [ ] Alle Kapitel sind analysiert und in `analysis.md` dokumentiert.
- [ ] Kapitelstatustabelle in `analysis.md` zeigt `analysiert` für alle Kapitel.
- [ ] Alle erzeugten Objekte sind in der Buchanalyse und in `SRC-XXXX` verlinkt.
- [ ] Objekte sind in der korrekten Sequenz angelegt (ST → A → MEC → P → T → MOD).
- [ ] Interner Konsistenz-Review (VAL-Objekt) ist abgeschlossen und liegt in `04_book_analysis/[Buch]/`.
- [ ] Alle Befunde aus dem Review sind entweder behoben oder als offen dokumentiert.
- [ ] BOOK_REVIEW_REPORT nach Template `01_framework/08_templates/book_review_template.md` erstellt.
- [ ] `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md` aktualisiert.

### 5.3 Konsistenz-Review als Pflichtschritt

Der Review ist kein optionaler Abschlussschritt. Er ist Teil jeder Buchanalyse.

Mindestprüfpunkte:
1. Alle referenzierten IDs existieren als Dateien.
2. MEC-IDs in Prinzipien sind per ID, nicht per Freitext.
3. Statement-Anzahl in Übersichtsdokumenten stimmt mit tatsächlicher Dateizahl überein.
4. Alle ⚠-Markierungen sind im VAL-Objekt dokumentiert.
5. Ethische Risiken vollständig markiert.

*Gelernt aus Pilot 001: Der Zählfehler (19 statt 23 Statements) und die fehlenden MEC-IDs in P-0001/P-0002 wurden erst im Konsistenz-Review entdeckt.*

---

## 6. Nächsten Schritt ableiten

### 6.1 Woher kommt der nächste Schritt?

In dieser Priorität:

1. **`00_project/NEXT_ACTION.md`** — enthält immer genau eine nächste Aktion und die aktuellen Abbruchbedingungen. Dies ist die primäre Quelle.
2. **Herausgeber-Anweisung** — explizite Aufgabe von Felix überschreibt NEXT_ACTION.md.
3. **Empfehlung aus dem letzten BOOK_REVIEW_REPORT** — wenn NEXT_ACTION.md leer oder abgeschlossen ist.

Ohne eine dieser drei Quellen wird kein nächster Schritt eigenständig begonnen.

### 6.2 Wie der nächste Schritt formuliert wird

Am Ende jeder Session oder jedes Abschlussberichts steht genau eine konkrete Empfehlung:

- Eine Quelle (nicht: "mehrere Bücher analysieren").
- Eine Validierungsaufgabe (nicht: "vieles validieren").
- Oder ein konkreter Widerspruch, der aufgelöst werden muss.

*Gelernt aus Pilot 001: Der Abschlussbericht enthielt eine priorisierte Liste von Forschungsfragen und eine klare erste Empfehlung (Primärtext-Verifikation, dann Gemini-Validierung, dann Challenger Sale als nächste Quelle).*

### 6.3 Was keinen nächsten Schritt erzeugt

- Allgemeine Aussagen wie "mehr Bücher lesen" oder "Wissensbasis ausbauen".
- Aufgaben, die Herausgeber-Entscheidung voraussetzen, ohne dass diese eingeholt wurde.
- Neue Methodik oder neue Strukturen.

---

## 7. Gelernte Verhaltensregeln aus Pilot 001

Diese Regeln gelten nur, weil sie aus tatsächlicher Arbeit entstanden sind — nicht aus Theorie.

### 7.1 MEC vor P

Mechanismus-Objekte vor Prinzip-Objekte anlegen.  
Ursache des Problems: P-0001 und P-0002 wurden angelegt, bevor MEC-0001 bis MEC-0004 existierten. Die Mechanismen wurden als Freitext eingetragen. Im Konsistenz-Review mussten beide Dateien nachträglich korrigiert werden.

### 7.2 Zählungen prüfen

Jede Zahl in Übersichtsdokumenten (Buchanalyse, Abschlussbericht) muss vor Abschluss gegen die tatsächliche Dateizahl geprüft werden.  
Ursache des Problems: analysis.md nannte "19 Statements gesamt" — tatsächlich waren es 23.

### 7.3 Kapitelzuordnung sofort markieren

Wenn die Kapitelzuordnung einer Aussage beim Schreiben unsicher ist, wird sie sofort mit ⚠ markiert — nicht am Ende. Am Ende ist der Kontext nicht mehr präsent.

### 7.4 Primärtext-Abweichungen sofort benennen

Wenn nicht mit dem physischen Buch gearbeitet wird, steht dieser Satz in jedem Statement-Objekt:  
*"Nicht zitierbar (kein physisches Buch vorliegend). Paraphrase aus Trainingswissen."*  
Diese Markierung ist nicht optional und wird nie weggelassen, um den Lesefluss zu verbessern.

### 7.5 Kein Objekt für künftige Kapitel

Extraktion beschränkt sich auf das, was der aktuell analysierte Text enthält. Erkenntnisse aus späteren Kapiteln werden nicht vorweggenommen, auch wenn sie bekannt sind.

### 7.6 Übersichtdokumente am Ende aktualisieren, nicht währenddessen

`SRC-XXXX`, `analysis.md`, Changelog und Review Queue werden am Ende einer Session aktualisiert — nicht nach jeder Datei. Zwischenzustände in Übersichtsdokumenten sind irreführend.

---

---

## 8. Book Mode (v1.1)

**Dokumentklasse: Reference**

Book Mode ist der Standard-Arbeitsmodus. Nach Freigabe des Task-Proposals kein erneutes Nachfragen bis zum BOOK_REVIEW — außer bei den Stopp-Bedingungen aus task_rules.md Abschnitt 10.2.

**Verhaltensregel:** Unsicherheit ist kein Stopp-Grund. Unsicherheit wird mit ⚠ markiert, in Offene Fragen dokumentiert, und die Arbeit geht weiter.

---

*Dieses Dokument gilt ab Pilot 001. Zuletzt aktualisiert: v1.1 (2026-06-30)*
