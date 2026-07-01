# Task-Vorschlag — B-0002 Influence

Erstellt: 2026-06-27  
Status: VORSCHLAG — wartet auf Herausgeber-Freigabe  
Erstellt durch: Cowork, gemäß `00_project/task_rules.md` v1.0

---

## Buchkontext

| Feld | Wert |
|---|---|
| Buch-ID | B-0002 |
| Titel | Influence |
| Autor | Robert B. Cialdini |
| Kategorie | Psychologie / Einfluss |
| Priorität | P1 |
| Rolle im Sales Codex | Psychologische Mechanismen und Einflussprinzipien |
| Notizen aus Catalog | nächstes Produktionsbuch |
| Erwartete SRC-ID | SRC-0002 |

---

## Erkannter Repository-Zustand

Basis: Repository-Scan vom 2026-06-27.  
Erkennungslogik: Prüfung auf Dateiexistenz und grep nach `SRC-0002` in `03_knowledge_base/`, gemäß `task_rules.md` Abschnitt 2.

| Objekt-Typ | Zustand | Befund |
|---|---|---|
| SRC-Datei | **fehlt** | Nur SRC-0001_SPIN_Selling.md vorhanden. Keine SRC-0002-Datei. |
| analysis.md | **fehlt** | Ordner `04_book_analysis/Influence/` existiert, ist aber leer. |
| Statements (ST) | **fehlt** | 0 Dateien mit SRC-0002-Referenz. Höchste vorhandene ID: ST-0023. |
| Annahmen (A) | **fehlt** | 0 Dateien mit SRC-0002-Referenz. Höchste vorhandene ID: A-0004. |
| Mechanismen (MEC) | **fehlt** | 0 Dateien mit SRC-0002-Referenz. Höchste vorhandene ID: MEC-0004. |
| Prinzipien (P) | **fehlt** | 0 Dateien mit SRC-0002-Referenz. Höchste vorhandene ID: P-0007. |
| Techniken (T) | **fehlt** | 0 Dateien mit SRC-0002-Referenz. Höchste vorhandene ID: T-0004. |
| Modelle (MOD) | **prüfungsbedürftig** | MOD-0001 (SPIN Selling) vorhanden. Kein Modell für Influence. Ob MOD-0001 ergänzt oder MOD-0002 angelegt wird, entscheidet sich inhaltlich in Task 8. |
| VAL-Report | **fehlt** | VAL-0001 (SPIN Selling / Pilot 001) vorhanden. Kein VAL für Influence. |
| Bestehender Task-Vorschlag | **keiner** | Keine `task_proposal_B-0002_*.md`-Datei vorhanden. |
| Aktive IN_PROGRESS-Tasks | **keine** | Backlog enthält keine aktiven Tasks. Abbruchbedingung nicht ausgelöst. |

**Ergebnis der Zustandsprüfung:** Alle Objekte für B-0002 fehlen vollständig. Das System startet bei Schritt 1 der Ableitungsmatrix.

---

## Abgeleitete Aufgaben

### Übersicht

| # | Task | Typ | Abhängigkeit | Auslösende Regel |
|---|---|---|---|---|
| 1 | Quelle erfassen — Influence | EXTRAKTION | — | task_rules.md § 5.2, Zeile 1 |
| 2 | Kapitelstruktur erfassen — Influence | ANALYSE | Task 1 | task_rules.md § 5.2, Zeile 2 |
| 3 | Statements extrahieren — Influence (kapitelweise) | EXTRAKTION | Task 2 | task_rules.md § 5.2, Zeile 3 + § 5.4 |
| 4 | Annahmen identifizieren — Influence | ANALYSE | Task 3 | task_rules.md § 5.2, Zeile 4 |
| 5 | Mechanismen ableiten — Influence | ANALYSE | Task 4 | task_rules.md § 5.2, Zeile 5 |
| 6 | Prinzipien formulieren — Influence | ANALYSE | Task 5 | task_rules.md § 5.2, Zeile 6 |
| 7 | Techniken erfassen — Influence | EXTRAKTION | Task 6 | task_rules.md § 5.2, Zeile 7 |
| 8 | Modelle aktualisieren nach Influence | INTEGRATION | Task 7 | task_rules.md § 5.2, Zeile 8 |
| 9 | Selbstreview durchführen — Influence | REVIEW | Task 8 | task_rules.md § 5.2, Zeile 9 |
| 10 | Abschlussbericht erstellen — Influence | REVIEW | Task 9 | task_rules.md § 5.2, Zeile 10 |

---

### Task 1 — Quelle erfassen — Influence

**Warum erzeugt:**  
Keine SRC-0002-Datei vorhanden. `task_rules.md` § 5.2, erste Bedingung: „Keine SRC-Datei vorhanden".

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 1  
**Template:** `01_framework/08_templates/source_template.md`  
**Ausgabepfad:** `02_sources/books/SRC-0002_influence.md`  
**Abhängigkeiten:** keine  
**Abbruchbedingung:** Primärquelle nicht zugänglich → Operating Manual § 7: Arbeit stoppen, Felix eskalieren.

**Pflichtinhalt der Ausgabedatei:**
- Titel, Autor (Robert B. Cialdini), Jahr der Erstausgabe und verwendeten Ausgabe
- Quellenklasse (A–F) mit Begründung
- Quellenkontext: Buch zur Überzeugungspsychologie, nicht primär Vertriebsbuch
- Hauptthese
- Grenzen der Quelle
- Bearbeitungsstatus: *Erfasst*

**Source-ID-Pflichtfeld (neu ab task_rules.md v1.0):**  
```
## Source ID
SRC-0002
```
Das Feld steht direkt nach der Objekt-ID, vor allen inhaltlichen Feldern.

**Voraussichtlich erstellte Dateien:** 1  
**Voraussichtlich geänderte Dateien:** keine

---

### Task 2 — Kapitelstruktur erfassen — Influence

**Warum erzeugt:**  
SRC-Datei fehlt noch (Abhängigkeit von Task 1) und analysis.md existiert nicht. `task_rules.md` § 5.2, zweite Bedingung: „SRC vorhanden, analysis.md fehlt".

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 2; § 6.1–6.2  
**Template:** `01_framework/08_templates/book_analysis_template.md`  
**Ausgabepfad:** `04_book_analysis/Influence/analysis.md`  
**Abhängigkeiten:** Task 1 abgeschlossen

**Pflichtinhalt der Ausgabedatei:**  
Die Datei muss unmittelbar nach dem Titel die Kapitelstruktur-Tabelle enthalten:

```markdown
## Kapitelstruktur

| Nr. | Titel (original) | Titel (DE) | Status |
|---|---|---|---|
| 1   | …                | …          | ausstehend |
```

Wenn der Primärtext nicht zugänglich ist:  
`⚠ Kapitelstruktur aus Trainingswissen — Verifikation gegen Primärtext erforderlich`

**Hinweis:** Die Kapitelanzahl in dieser Tabelle bestimmt direkt die Anzahl der Tasks in Task 3. Dieser Task ist der strukturelle Engpass des Systems für B-0002.

**Voraussichtlich erstellte Dateien:** 1  
**Voraussichtlich geänderte Dateien:** keine

---

### Task 3 — Statements extrahieren — Influence (kapitelweise)

**Warum erzeugt:**  
analysis.md vorhanden (nach Task 2), STs fehlen vollständig für SRC-0002. `task_rules.md` § 5.2, dritte Bedingung.

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 3; § 5.4  
**Template:** `01_framework/08_templates/statement_template.md`  
**Ausgabepfad:** `03_knowledge_base/statements/ST-XXXX_[slug].md`  
**Nächste freie ID:** ST-0024  
**Abhängigkeiten:** Task 2 abgeschlossen und Kapitelstruktur-Tabelle vollständig

**Besonderheit:**  
`task_rules.md` § 5.4: „ST-Extraktions-Tasks werden erst nach vollständiger Kapitelstruktur-Tabelle erzeugt. Die Kapitelanzahl aus der Tabelle bestimmt die Task-Anzahl."

Task 3 ist zum Zeitpunkt dieses Proposals ein **Platzhalter**. Die genaue Anzahl der Kapitel-Tasks wird erst nach Abschluss von Task 2 bekannt. Das System erzeugt nach Task 2 automatisch einen Sub-Task pro Kapitel (je einen „Statements extrahieren — Influence Kapitel N"-Task).

**Pflichtinhalt je ST-Datei (ab task_rules.md v1.0):**
- Source-ID-Feld: `SRC-0002`
- Unsicherheitsmarkierung wenn kein Primärtext vorliegend (Operating Manual § 7 i.V.m. Execution Protocol § 7.4)
- Kapitelzuordnung — bei Unsicherheit sofort ⚠ (Execution Protocol § 7.3)

**Quervergleich mit bestehenden Objekten:**  
Gemäß Canonical Knowledge Model § 3.1 sind STs eindeutig durch Quelle + Kausalrichtung + Aussage-Typ. SRC-0002-Statements sind per Definition neu (andere Quelle). Doppelanlage ist bei STs kein Risiko.

**Voraussichtlich erstellte Dateien:** N (N = Kapitelanzahl × durchschnittliche Statements pro Kapitel; nicht vorhersagbar ohne Kapitelstruktur)  
**Voraussichtlich geänderte Dateien:** `04_book_analysis/Influence/analysis.md` (Kapitelabschnitte werden befüllt)

---

### Task 4 — Annahmen identifizieren — Influence

**Warum erzeugt:**  
STs vollständig (nach Task 3), As für SRC-0002 fehlen. `task_rules.md` § 5.2, vierte Bedingung.

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 4  
**Template:** `01_framework/08_templates/assumption_template.md`  
**Ausgabepfad:** `03_knowledge_base/assumptions/A-XXXX_[slug].md`  
**Nächste freie ID:** A-0005  
**Abhängigkeiten:** Task 3 vollständig abgeschlossen

**Pflichtinhalt je A-Datei (ab task_rules.md v1.0):**
- Source-ID-Feld: `SRC-0002`
- Falsifizierungsbedingung (Canonical Knowledge Model § 3.2)

**Quervergleich mit bestehenden Objekten (Pflicht):**  
Vor jeder Neuanlage: Canonical Knowledge Model § 4, Schritt 1: bestehende A-0001 bis A-0004 auf identische Falsifizierungsbedingung prüfen.

Bekannte Risikofälle (aus Trainingswissen, nicht als inhaltliches Urteil):
- A-0004 (Käufer-Verbalisierung als handlungsauslösend) könnte mit Cialdinins Commitment-und-Konsistenz-Prinzip verwandt sein. Prüfpflicht gemäß Canonical Knowledge Model § 3.2.

Wenn eine neue Annahme inhaltlich mit einer bestehenden identisch ist: Bestehende Datei ergänzen, keine neue A-Datei anlegen.

**Voraussichtlich erstellte Dateien:** variabel (mindestens 3–6 erwartet; nicht vorhersagbar)  
**Voraussichtlich geänderte Dateien:** ggf. bestehende A-Dateien (Erweiterung durch Stützquelle SRC-0002)

---

### Task 5 — Mechanismen ableiten — Influence

**Warum erzeugt:**  
As vollständig (nach Task 4), MECs für SRC-0002 fehlen. `task_rules.md` § 5.2, fünfte Bedingung.

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 5  
**Template:** `01_framework/08_templates/mechanism_template.md`  
**Ausgabepfad:** `03_knowledge_base/mechanisms/MEC-XXXX_[slug].md`  
**Nächste freie ID:** MEC-0005  
**Abhängigkeiten:** Task 4 vollständig abgeschlossen

**Pflichtinhalt je MEC-Datei (ab task_rules.md v1.0):**
- Source-ID-Feld: `SRC-0002`
- Mindestschwelle: mindestens zwei Auftreten als erklärende Kraft (Canonical Knowledge Model § 5)
- Eigenständiger kausaler Pfad

**Quervergleich mit bestehenden Objekten (Pflicht):**  
Canonical Knowledge Model § 3.3: MEC-0001 bis MEC-0004 auf identischen kausalen Pfad (Stimulus → Prozess → Reaktion) prüfen.

Bekannte Risikofälle (nicht als inhaltliches Urteil — Prüfpflicht):
- MEC-0001 (Selbstüberzeugung durch Verbalisierung): Kandidat für Überschneidung mit Cialdinins Commitment-und-Konsistenz-Mechanismus. Cialdini und die Selbst-Wahrnehmungstheorie (Bem, 1972) sind bereits in MEC-0001 zitiert.
- MEC-0004 (Kognitive Konsistenz durch explizites Need Statement): Kandidat für Überschneidung mit Cialdinins Commitment-Prinzip.
- Cialdinis Reziprozität, Soziale Bewährtheit, Autorität, Sympathie und Knappheit sind wahrscheinlich neue kausale Pfade ohne Entsprechung in MEC-0001 bis MEC-0004.

Entscheidung (Erweitern / Neu / Zusammenführen / Verwerfen) gemäß Canonical Knowledge Model § 4.

**Voraussichtlich erstellte Dateien:** variabel  
**Voraussichtlich geänderte Dateien:** ggf. MEC-0001, MEC-0004 (Stützquelle SRC-0002 hinzufügen)

---

### Task 6 — Prinzipien formulieren — Influence

**Warum erzeugt:**  
MECs vollständig (nach Task 5), Ps für SRC-0002 fehlen. `task_rules.md` § 5.2, sechste Bedingung.

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 6  
**Template:** `01_framework/08_templates/principle_template.md`  
**Ausgabepfad:** `03_knowledge_base/principles/P-XXXX_[slug].md`  
**Nächste freie ID:** P-0008  
**Abhängigkeiten:** Task 5 vollständig abgeschlossen

**Pflichtinhalt je P-Datei (ab task_rules.md v1.0):**
- Source-ID-Feld: `SRC-0002`
- Prinzip-Aussage: Format „Unter X führt Y tendenziell zu Z"
- MEC-ID-Referenz (kein Freitext) — Grund: Execution Protocol § 7.1 (Lernpunkt Pilot 001)
- Ethisches Risiko markieren — Pflicht gemäß Operating Manual § 5; bei Influence besonders relevant (Manipulationsrisiko)
- Einstufung: Quellenprinzip (nicht Codex-Prinzip); E1–E2, M1–M2 (Canonical Knowledge Model § 3.4)

**Quervergleich mit bestehenden Objekten (Pflicht):**  
P-0001 bis P-0007 auf identische Prinzip-Aussage, Mechanismus und Kontext prüfen.

Bekannte Risikofälle (Prüfpflicht, kein inhaltliches Urteil):
- P-0001 (Selbst-verbalisierte Erkenntnis) und Cialdinins Commitment-Mechanismus teilen möglicherweise strukturelle Ähnlichkeiten. Falsifizierungsbedingungen und kausale Pfade sind zu vergleichen.

**Hinweis ethisches Risiko:**  
Influence enthält Techniken (z.B. Knappheitsprinzip, Reziprozitätsprinzip), die manipulativ einsetzbar sind. Jedes abgeleitete Prinzip muss das Feld „Ethisches Risiko" ausgefüllt haben. Grenzfälle werden nicht eigenständig entschieden — Eskalation an Felix.

**Voraussichtlich erstellte Dateien:** variabel  
**Voraussichtlich geänderte Dateien:** ggf. bestehende P-Dateien (Stützquelle SRC-0002)

---

### Task 7 — Techniken erfassen — Influence

**Warum erzeugt:**  
Ps vollständig (nach Task 6), Ts für SRC-0002 fehlen. `task_rules.md` § 5.2, siebte Bedingung.

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 7  
**Template:** `01_framework/08_templates/technique_template.md`  
**Ausgabepfad:** `03_knowledge_base/techniques/T-XXXX_[slug].md`  
**Nächste freie ID:** T-0005  
**Abhängigkeiten:** Task 6 vollständig abgeschlossen

**Pflichtinhalt je T-Datei (ab task_rules.md v1.0):**
- Source-ID-Feld: `SRC-0002`
- Angewendetes Prinzip: P-ID (nicht Freitext)
- Genutzter Mechanismus: MEC-ID (nicht Freitext)
- Gesprächszustand: aus Sales Process Decision System
- Risiken und typische Fehlanwendung
- Ethisches Risiko: bei Techniken aus Influence besonders kritisch prüfen

**Voraussichtlich erstellte Dateien:** variabel  
**Voraussichtlich geänderte Dateien:** keine

---

### Task 8 — Modelle aktualisieren nach Influence

**Warum erzeugt:**  
Ts vollständig (nach Task 7), MOD-Status prüfungsbedürftig. `task_rules.md` § 5.2, achte Bedingung: „Ts vollständig, MODs veraltet".

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 8  
**Template:** `01_framework/08_templates/model_template.md`  
**Ausgabepfad:** `03_knowledge_base/models/MOD-XXXX_[slug].md` (neu) oder Ergänzung MOD-0001  
**Abhängigkeiten:** Task 7 vollständig abgeschlossen

**Entscheidung Neu vs. Ergänzen:**  
Die Frage „Wird MOD-0001 ergänzt oder wird MOD-0002 angelegt?" kann erst nach Abschluss der Extraktion inhaltlich beantwortet werden.

Kriterium: Canonical Knowledge Model § 3.4 (Modell erfordert mind. drei verknüpfte Prinzipien). Wenn Influence ein eigenständiges kausallogisches Modell beschreibt (Theorie der 6 Einflussprinzipien), ist MOD-0002 wahrscheinlich. Wenn Influence primär Mechanismen ergänzt, die bereits in MOD-0001 referenziert sind, wird MOD-0001 erweitert.

Diese Entscheidung ist inhaltlich und wird während Task 8 getroffen — nicht durch den Task Generator.

**Voraussichtlich erstellte Dateien:** 0–1 (MOD-0002 möglicherweise)  
**Voraussichtlich geänderte Dateien:** ggf. MOD-0001 (Ergänzung um SRC-0002-Querverweise)

---

### Task 9 — Selbstreview durchführen — Influence

**Warum erzeugt:**  
Alle Wissensobjekte vollständig (nach Task 8), kein VAL-Report für Influence vorhanden. `task_rules.md` § 5.2, neunte Bedingung.

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 9; Operating Manual § 3, Schritt 8; Execution Protocol § 5.3  
**Template:** `01_framework/08_templates/validation_report_template.md`  
**Ausgabepfad:** `00_project/VAL-0002_consistency_review_influence.md`  
**Abhängigkeiten:** Task 8 vollständig abgeschlossen

**Pflichtinhalt:**  
Gemäß Execution Protocol § 5.3 (Mindestprüfpunkte):
1. Alle referenzierten IDs existieren als Dateien.
2. MEC-IDs in Prinzipien sind per ID, nicht per Freitext.
3. Statement-Anzahl in Übersichtsdokumenten stimmt mit tatsächlicher Dateizahl überein.
4. Alle ⚠-Markierungen sind dokumentiert.
5. Ethische Risiken vollständig markiert.

Zusätzlich für Influence:
6. Quervergleich-Entscheidungen (Neu / Erweitern / Zusammenführen) dokumentiert.
7. Alle Objekte mit Source-ID-Feld SRC-0002 versehen.

**Voraussichtlich erstellte Dateien:** 1  
**Voraussichtlich geänderte Dateien:** keine

---

### Task 10 — Abschlussbericht erstellen — Influence

**Warum erzeugt:**  
VAL-Report vorhanden (nach Task 9), Abschlussbericht fehlt. `task_rules.md` § 5.2, zehnte Bedingung.

**Regelreferenz:** `task_rules.md` § 5.2, Zeile 10; Operating Manual § 9  
**Template:** (kein eigenes Template; Pflichtstruktur in Operating Manual § 9 definiert)  
**Ausgabepfad:** `00_project/ABSCHLUSSBERICHT_B-0002_influence.md`  
**Abhängigkeiten:** Task 9 vollständig abgeschlossen

**Pflichtstruktur (Operating Manual § 9):**
- 9.1 Erzeugte Objekte (Tabelle: Objekttyp / Anzahl / ID-Bereich)
- 9.2 Wichtigste Erkenntnisse (max. 7 Kernpunkte)
- 9.3 Offene Forschungsfragen (priorisiert)
- 9.4 Konsistenzbefunde (aus VAL-0002)
- 9.5 Empfehlung für nächsten Schritt (genau eine)

Nach Abschluss dieses Tasks: Catalog-Status B-0002 → `REVIEW`.

**Voraussichtlich erstellte Dateien:** 1  
**Voraussichtlich geänderte Dateien:** keine (Catalog-Statuswechsel ist Herausgeber-Entscheidung)

---

## Nächste freie IDs (Stand: 2026-06-27)

| Objekttyp | Nächste freie ID |
|---|---|
| SRC | SRC-0002 |
| ST | ST-0024 |
| A | A-0005 |
| MEC | MEC-0005 |
| P | P-0008 |
| T | T-0005 |
| MOD | MOD-0002 (falls neu angelegt) |
| VAL | VAL-0002 |

---

## Selbstprüfung

### 1. Fehlen Aufgaben?

**Mögliche fehlende Aufgabe: Verifikation der Rückwärtskompatibilität bestehender Objekte**

`task_rules.md` § 7.4 dokumentiert, dass bestehende Pilot-001-Objekte (ST-0001 bis ST-0023, A-0001 bis A-0004, MEC-0001 bis MEC-0004, P-0001 bis P-0007, T-0001 bis T-0004) kein Source-ID-Feld besitzen. Die Nachpflege ist als „sinnvoll, aber nicht blockierend" eingestuft.

Das Task-Generierungssystem erzeugt dafür keinen eigenen Task. Wenn Felix diese Nachpflege wünscht, müsste er einen separaten Auftrag geben. **Bewertung: bekannte Lücke, kein Fehler im System, aber Herausgeber-Entscheidung offen.**

**Mögliche fehlende Aufgabe: Primärtext-Beschaffung**

Das Operating Manual (§ 7) definiert: „Primärquelle nicht zugänglich → Arbeit stoppen." Das Task-Generierungssystem stellt jedoch keinen expliziten Task „Primärtext beschaffen" vor Task 1. Die Zugänglichkeit des Buches ist eine Voraussetzung, keine Aufgabe. **Bewertung: kein struktureller Fehler; Abbruchbedingung greift wenn nötig.**

**Mögliche fehlende Aufgabe: Expliziter Quervergleich-Task**

Das Canonical Knowledge Model erfordert systematischen Vergleich neuer Objekte mit bestehenden. Dieser Vergleich ist in Tasks 4, 5 und 6 als Prüfpflicht beschrieben, aber es gibt keinen eigenständigen Task „Quervergleich Influence vs. SPIN Selling". Die Vergleichsarbeit ist in die Extraktions-Tasks eingebettet — das ist die Entscheidung aus task_rules.md (kein eigener Vergleichsschritt). **Bewertung: Designentscheidung, nicht Fehler; könnte aber zu Aufwandsunterschätzung führen.**

### 2. Sind Aufgaben doppelt?

Nein. Jeder der 10 Tasks adressiert einen eindeutig anderen Objekttyp oder Prozessschritt. Keine inhaltlichen Überschneidungen festgestellt.

### 3. Ist die Reihenfolge deterministisch?

**Ja, bis auf eine Ausnahme.**

Tasks 1, 2, 9 und 10 sind vollständig deterministisch ableitbar.

Task 3 ist **bedingt deterministisch**: Die Anzahl der ST-Sub-Tasks ist erst nach Task 2 bekannt. Das System kann sie heute nicht vollständig auflisten. Das ist eine bekannte Eigenschaft des Systems (task_rules.md § 5.4) und kein Fehler, muss aber dem Herausgeber bekannt sein.

Tasks 4–8: vollständig deterministisch in der Reihenfolge, variabel in der Anzahl der erzeugten Objekte.

### 4. Gibt es Informationen, die das aktuelle Operating System noch nicht bereitstellt?

**Lücke 1 — Backlog-Format für Tasks:**  
`backlog.md` enthält nur Arbeitsregeln und einen Workflow-Diagram-Text, aber keine inhaltlichen Task-Abschnitte (keine READY/IN_PROGRESS-Sektionen). Nach Freigabe dieses Proposals ist unklar, in welchem Format Tasks in den Backlog übernommen werden. Das Backlog-Format für echte Tasks ist nicht spezifiziert.

**Empfehlung:** Felix sollte eine Backlog-Struktur mit Abschnitten (z.B. `## READY`, `## IN_PROGRESS`, `## DONE`) definieren, bevor der erste Task übernommen wird.

**Lücke 2 — Abschlussberichts-Dateiname nicht vollständig standardisiert:**  
`task_rules.md` nennt als Muster `00_project/PILOT_XXXX_ABSCHLUSSBERICHT.md oder equivalent`. Da Influence kein Pilotprojekt ist, ist „PILOT" als Präfix irreführend. Pilot 001 hatte einen eigenen Bericht (`PILOT_001_ABSCHLUSSBERICHT.md`). Dieses Proposal verwendet `ABSCHLUSSBERICHT_B-0002_influence.md` als Konvention — diese Benennung wurde nicht explizit durch ein OS-Dokument vorgegeben.

**Empfehlung:** Dateinamen-Konvention für Abschlussberichte ab B-0002 einmalig festlegen.

**Lücke 3 — MOD-Entscheidungsregel „veraltet" ist unscharf:**  
`task_rules.md` § 5.2 löst den MOD-Task aus, wenn „MODs veraltet". Eine Definition von „veraltet" fehlt. In diesem Proposal wird Task 8 generiert, weil kein MOD für SRC-0002 existiert — das ist plausibel, aber die Regel könnte präziser sein.

### 5. Welche Unsicherheiten bestehen?

**Unsicherheit 1 — Kapitelanzahl von Influence:**  
Influence (Cialdini, Originalausgabe 1984) enthält typischerweise 6 Hauptkapitel (entsprechend den 6 Einflussprinzipien) plus Einleitung und Nachwort. Ob die verwendete Ausgabe zusätzliche Kapitel enthält, ist ohne Primärtext nicht sicher. Task 3 wird nach Task 2 konkretisiert.

**Unsicherheit 2 — Primärtext-Zugänglichkeit:**  
Wie bei SPIN Selling (Pilot 001) ist nicht bekannt, ob Felix das Buch physisch vorhält oder ob mit Trainingswissen gearbeitet werden muss. Im zweiten Fall greifen die Pflichtmarkierungen (Execution Protocol § 7.4).

**Unsicherheit 3 — Anzahl neuer vs. erweiterter Objekte:**  
Da Influence inhaltlich verwandte Mechanismen zu SPIN Selling aufweist (besonders Commitment-und-Konsistenz vs. MEC-0001/MEC-0004), ist die Anzahl neuer MEC-Objekte vs. erweiterter bestehender Objekte im Voraus nicht bestimmbar. Das Canonical Knowledge Model gibt die Entscheidungslogik vor, nicht das Ergebnis.

**Unsicherheit 4 — Ethische Grenzfälle:**  
Influence enthält Prinzipien (z.B. Knappheit, Reziprozität), die im Kontext von High-Pressure Sales manipulativ eingesetzt werden können. Es ist wahrscheinlich, dass mindestens ein ethischer Grenzfall auftritt, der Felix-Eskalation erfordert. Das verzögert möglicherweise einzelne Tasks.

---

## Hinweis

Dieser Vorschlag wird erst nach ausdrücklicher Freigabe durch Felix in den Backlog übernommen.

Nach Freigabe: Tasks 1 und 2 erhalten Status READY. Tasks 3–10 erhalten Status WAITING, bis ihre jeweiligen Abhängigkeiten erfüllt sind.

Catalog-Status B-0002 bleibt `READY` bis zur Freigabe. Erst nach Freigabe setzt Cowork ihn auf `IN_PROGRESS`.

---

*Erstellt gemäß `task_rules.md` v1.0 — Änderungen am Proposal nur durch Felix oder durch neuen Vorschlag nach explizitem Verwurf dieses Vorschlags.*
