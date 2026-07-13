# Task Types — Routing-Referenz für Claude Cowork

**Dokumentklasse:** Reference (aufgabenbezogenes Routing)
**Zweck:** Definiert 12 Task-Typen mit fester Dateiladestrategie, Suchgrenzen, Ausgabeformat und Arbeitsmodus. Ziel: Claude muss bei einer benannten Aufgabe nicht mehr selbst abwägen, welche Dateien/Verzeichnisse relevant sind — das Routing ist hier bereits festgelegt.
**Herkunft:** Übertragen aus `99_archive/00_project_history/SALES_CODEX_DECISION_ARCHITECTURE_AUDIT_2026-07-05.md` (Teil 2, 3, 5, 6, 7, 8). Begründungen, Alternativen-Abwägung und Roadmap stehen dort — diese Datei ist bewusst eine reine Referenz ohne Begründungstext.
**Status:** Statische Referenz, kein Log. Wird bei Bedarf inhaltlich korrigiert, nicht historisch fortgeschrieben. Änderungen an dieser Datei sind Framework-nahe Entscheidungen und erfordern Freigabe durch Felix.
**Zuletzt aktualisiert:** 2026-07-05 (Decision Architecture Sprint 2)

---

## Verwendung

1. Ein Auftrag nennt idealerweise ein `TASK_TYPE`-Feld (siehe Vorlagen unten). Dann direkt zur passenden Sektion springen — kein weiteres Abwägen nötig.
2. Nennt der Auftrag keinen Typ: wahrscheinlichsten Typ aus der Übersichtstabelle ableiten und im Chat kurz benennen. Bei echter Mehrdeutigkeit: rückfragen statt raten.
3. Diese Datei hebt keine bestehenden Grenzen auf — `PROJECT_BOOTSTRAP.md` (Suchgrenze, Abbruchbedingungen, Arbeitsprinzipien) gilt zusätzlich und vorrangig bei Konflikt.

## Directory-Routing-Grundregel

Claude wählt Verzeichnisse nicht mehr frei. Jeder Task-Typ definiert unten eine geschlossene Liste erlaubter Verzeichnisse/Dateien. Innerhalb eines erlaubten Verzeichnisses ist nicht-rekursives Auflisten (`ls`) immer zulässig. Rekursive Volltextsuche ist nur zulässig, wenn beim jeweiligen Typ ausdrücklich als Standard vermerkt (T6, T7) oder im Auftrag für genau diese Session explizit freigegeben. Jedes nicht gelistete Verzeichnis ist ohne Rückfrage tabu.

## Übersichtstabelle

| Typ | Name | Ziel (ein Satz) |
|---|---|---|
| T1 | Buchanalyse (Book Mode) | Ein Buch durch die Wissenspipeline (SRC→ST→A→MEC→P→T→MOD) verarbeiten |
| T2 | Framework-Arbeit | Methodik, Evidenzsystem, Canonical Knowledge Model oder Templates ändern |
| T3 | Repository-Wartung / Hygiene (inkl. Bugfix) | Tote Links, Duplikate, Pfadfehler beheben, ohne inhaltliche Bewertung |
| T4 | Architekturarbeit (inkl. Refactoring) | Struktur-/Prozessfragen bewerten, Vorschlag entwerfen (keine Ausführung) |
| T5 | Review / Validierung (VAL) | Konsistenz eines abgeschlossenen Bereichs prüfen, VAL-Report erstellen |
| T6 | Audit | Repositoryweite, rein lesende Bewertung mit definierter Scope-Grenze |
| T7 | Konsistenzprüfung | Eine einzelne, klar definierte Regel für einen Objekttyp repositoryweit prüfen |
| T8 | Governance / Decision Resolution | Offene Entscheidungen klären/dokumentieren, Editor Decisions verfassen |
| T9 | Release / Freeze | Versionsstand einfrieren, Release-Dokumente erstellen |
| T10 | Research Project (W-xxx Lifecycle) | Forschungsprojekt durch die 9-stufige Lifecycle-Architektur führen |
| T11 | Scientific Debt / Academic Recovery | Belegdefizite systematisch schließen |
| T12 | Publikationsarbeit (vorbereitet, noch nicht aktiv) | Wissensbasis in Buch/Workbook/Training/Vortrag überführen |

---

## T1 — Buchanalyse (Book Mode)

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, `02_sources/book_catalog.md`, `02_sources/books/SRC-XXXX*`, betroffene Objekttyp-Templates
- Optional laden: `04_book_analysis/<Titel>/analysis.md` (falls vorhanden)
- Nie automatisch laden: `OPEN_DECISIONS.md`, `SCIENTIFIC_DEBT.md`, andere Bücher
- Erlaubte Suche: Source-ID-gefilterte Suche in `03_knowledge_base/`
- Verbotene Suche: Volltextscan über andere Bücher „zur Inspiration"
- Ausgabeformat: Wissensobjekte nach Template; Chat: Anzahl neuer Objekte + nächster Schritt
- Arbeitsmodus: Editor, Wissensextraktion
- Decision Budget: 1 Dateientscheidung (Template-Wahl je Objekttyp), 1 Suchentscheidung (Source-ID-Filter ja/nein), 0 Kontextentscheidungen

**Prompt-Vorlage:**
```
TASK_TYPE: T1_BUCHANALYSE
ZIEL: Buch <Titel> (SRC-XXXX) — Kapitel <X>–<Y> durch die Pipeline verarbeiten.
ROLLE: Editor, Wissensextraktion.
ERLAUBTE DATEIEN: 02_sources/book_catalog.md, 02_sources/books/SRC-XXXX*,
04_book_analysis/<Titel>/, 03_knowledge_base/*-Objekte mit Source-ID SRC-XXXX,
01_framework/08_templates/*.
VERBOTENE DATEIEN: OPEN_DECISIONS.md, SCIENTIFIC_DEBT.md, andere Bücher.
SUCHGRENZE: Nur Source-ID-gefilterte Suche. Kein Scan über andere Bücher.
ÄNDERUNGSGRENZE: Nur neue Objekte mit dieser Source-ID, keine Änderung an
bestehenden Objekten außerhalb der Canonicalisierung.
AUSGABEFORMAT: Wissensobjekte nach Template. Chat: Anzahl neuer Objekte + nächster Schritt.
ABBRUCHBEDINGUNGEN: Primärquelle fehlt; Canonicalisierungskonflikt unauflösbar.
```

---

## T2 — Framework-Arbeit

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, betroffene `01_framework/`-Datei(en)
- Optional laden: `canonical_knowledge_model.md` zur Konsistenzprüfung
- Nie automatisch laden: `03_knowledge_base/` (außer Folgenabschätzung separat beauftragt)
- Erlaubte Suche: keine
- Verbotene Suche: Scan über `03_knowledge_base/` ohne Auftrag
- Ausgabeformat: Änderungsvorschlag mit Begründung
- Arbeitsmodus: Framework-Architekt (nur mit expliziter Freigabe)
- Decision Budget: 2 Dateientscheidungen, 1 Suchentscheidung, 0 Kontextentscheidungen

**Prompt-Vorlage:**
```
TASK_TYPE: T2_FRAMEWORK
ZIEL: <konkrete Framework-Frage/Änderung>, vorab von Felix freigegeben.
ROLLE: Framework-Architekt (nur mit dieser expliziten Freigabe).
ERLAUBTE DATEIEN: 01_framework/<betroffener Unterordner>/, betroffene Templates.
VERBOTENE DATEIEN: 03_knowledge_base/ (außer Folgenabschätzung separat beauftragt).
SUCHGRENZE: Keine Suche ohne expliziten Zusatzauftrag.
ÄNDERUNGSGRENZE: Nur die benannte Framework-Datei, keine rückwirkende
Änderung bestehender Wissensobjekte.
AUSGABEFORMAT: Änderungsvorschlag mit Begründung, keine Direktänderung ohne
zweite Bestätigung.
ABBRUCHBEDINGUNGEN: Framework-Widerspruch zu bestehendem Wissensmodell erkannt.
```

---

## T3 — Repository-Wartung / Hygiene (inkl. Bugfix)

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, die im Auftrag genannte(n) Datei(en)
- Optional laden: Referenzdatei zur Prüfung der Korrektheit
- Nie automatisch laden: alles außerhalb der genannten Dateien
- Erlaubte Suche: Cross-Reference-Check der genannten Dateien
- Verbotene Suche: jeder Scan über nicht genannte Ordner
- Ausgabeformat: Kurzdiff im Chat
- Arbeitsmodus: Editor, punktuelle Änderung
- Decision Budget: 0 Dateientscheidungen, 0 Suchentscheidungen, 0 Kontextentscheidungen (jede Entscheidung hier ist ein Prompt-Mangel, kein Ermessen)

**Prompt-Vorlage:**
```
TASK_TYPE: T3_WARTUNG
ZIEL: <eine konkrete Korrektur an einer benannten Datei/einem benannten Link>.
ROLLE: Editor, punktuelle Korrektur.
ERLAUBTE DATEIEN: Ausschließlich die genannte(n) Datei(en).
VERBOTENE DATEIEN: Alles außerhalb der genannten Dateien, auch wenn „verwandt".
SUCHGRENZE: Keine — Datei ist bereits benannt.
ÄNDERUNGSGRENZE: Nur die genannte Korrektur, keine weiteren Verbesserungen
„nebenbei".
AUSGABEFORMAT: Kurzdiff im Chat, keine Zusammenfassung des gesamten Dateiinhalts.
ABBRUCHBEDINGUNGEN: Datei existiert nicht wie beschrieben.
```

---

## T4 — Architekturarbeit (inkl. Refactoring)

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, Verzeichnisstruktur (Metadaten)
- Optional laden: betroffene Governance-Dateien
- Nie automatisch laden: Volltext aller Dateien pauschal
- Erlaubte Suche: `find`/`ls` (Struktur)
- Verbotene Suche/Aktion: Umsetzung ohne zweite Freigabe
- Ausgabeformat: Vorschlag mit Vor-/Nachteilen und Aufwand/Risiko/Nutzen
- Arbeitsmodus: Systemarchitekt (Entwurf, keine Ausführung)
- Decision Budget: 3 Dateientscheidungen, 2 Suchentscheidungen, 1 Kontextentscheidung

**Prompt-Vorlage:**
```
TASK_TYPE: T4_ARCHITEKTUR
ZIEL: <konkrete Architekturfrage>.
ROLLE: Systemarchitekt — Entwurf, keine Ausführung ohne zweite Freigabe.
ERLAUBTE DATEIEN: Verzeichnisstruktur (Metadaten), betroffene Governance-Dateien.
VERBOTENE DATEIEN: Volltext aller Dateien pauschal.
SUCHGRENZE: find/ls (Struktur) erlaubt, gezieltes Volltextlesen nur bei Bedarf.
ÄNDERUNGSGRENZE: Keine Ausführung des Vorschlags in diesem Schritt.
AUSGABEFORMAT: Vorschlag mit Vor-/Nachteilen und Aufwand/Risiko/Nutzen.
ABBRUCHBEDINGUNGEN: Vorschlag würde bestehende Governance-Entscheidung widersprechen.
```

---

## T5 — Review / Validierung (VAL)

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, zu prüfende Objekte, `01_framework/08_templates/validation_report_template.md`
- Optional laden: `evidence_system.md`
- Nie automatisch laden: andere Objekttypen/Bücher
- Erlaubte Suche: Referenzprüfung via `08_knowledge_atlas/output/edges.csv`
- Verbotene Suche: Einzelöffnen aller verlinkten Dateien statt Atlas-Output
- Ausgabeformat: VAL-Report nach Template
- Arbeitsmodus: Reviewer, kein Autor
- Decision Budget: 1 Dateientscheidung, 1 Suchentscheidung, 0 Kontextentscheidungen

**Prompt-Vorlage:**
```
TASK_TYPE: T5_REVIEW
ZIEL: Konsistenzreview für <Buch/Objekttyp/Bereich>, Ergebnis als VAL-Report.
ROLLE: Reviewer, kein Autor.
ERLAUBTE DATEIEN: Zu prüfende Objekte, 01_framework/08_templates/validation_report_template.md,
08_knowledge_atlas/output/edges.csv.
VERBOTENE DATEIEN: Andere Objekttypen/Bücher.
SUCHGRENZE: Referenzprüfung über edges.csv, kein Einzelöffnen aller verlinkten Dateien.
ÄNDERUNGSGRENZE: Keine inhaltlichen Korrekturen — nur Befund, gekennzeichnet.
AUSGABEFORMAT: VAL-Report nach Template.
ABBRUCHBEDINGUNGEN: Referenzintegrität so beschädigt, dass Review nicht sinnvoll möglich ist.
```

---

## T6 — Audit

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, Verzeichnisstruktur, im Auftrag benannte Bereiche
- Optional laden: Stichprobe aus `03_knowledge_base/`
- Nie automatisch laden: — (einziger Typ ohne Pauschalverbot; Scope kommt aus dem Auftrag, nicht aus Ermessen)
- Erlaubte Suche: repositoryweite Struktur-/Stichprobenprüfung, mit Scope-Enddatum im Auftrag
- Verbotene Suche: Vollprüfung aller 514 Objekte ohne expliziten Auftrag dazu
- Ausgabeformat: Auditbericht mit explizitem Methodikabschnitt
- Arbeitsmodus: unabhängiger Auditor, rein lesend
- Decision Budget: 4 Dateientscheidungen, 3 Suchentscheidungen, 2 Kontextentscheidungen (bewusst höher — einziger strukturell offener Typ)

**Prompt-Vorlage:**
```
TASK_TYPE: T6_AUDIT
ZIEL: <Auditgegenstand und Scope-Grenze, z. B. "Evidenzfelder aller 57 Prinzipien,
Stichprobe von 15">.
ROLLE: Unabhängiger Auditor, rein lesend.
ERLAUBTE DATEIEN: Im Auftrag benannter Bereich + Verzeichnisstruktur.
VERBOTENE DATEIEN: Keine Änderungen an irgendeiner Datei.
SUCHGRENZE: Repositoryweite Struktur-/Stichprobenprüfung erlaubt, aber mit
der im Auftrag benannten Scope-Grenze — kein unbegrenzter Vollscan ohne diese Angabe.
ÄNDERUNGSGRENZE: Keine.
AUSGABEFORMAT: Auditbericht mit explizitem Methodikabschnitt (was wurde
tatsächlich geprüft, was nicht).
ABBRUCHBEDINGUNGEN: Scope-Grenze im Auftrag fehlt — dann zuerst rückfragen,
nicht mit unbegrenztem Scope beginnen.
```

---

## T7 — Konsistenzprüfung

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, der geprüfte Objekttyp-Ordner vollständig, die regeldefinierende Framework-Datei
- Optional laden: `08_knowledge_atlas/output/*.csv`
- Nie automatisch laden: andere Objekttypen
- Erlaubte Suche: rekursiver Scan über genau den einen geprüften Ordner — für diesen Typ Standard, keine erneute Freigabe pro Session nötig
- Verbotene Suche/Aktion: Korrektur ohne separate Freigabe
- Ausgabeformat: Befundliste (Datei, Regelverstoß), keine Datei ändern
- Arbeitsmodus: Auditor, nur Befund
- Decision Budget: 0 Dateientscheidungen, 0 Suchentscheidungen (Scanumfang durch Regel vorgegeben), 0 Kontextentscheidungen

**Prompt-Vorlage:**
```
TASK_TYPE: T7_KONSISTENZ
ZIEL: Prüfen, ob <konkrete Regel> für alle Objekte des Typs <ST/A/MEC/P/T/MOD>
eingehalten wird.
ROLLE: Auditor, nur Befund.
ERLAUBTE DATEIEN: 03_knowledge_base/<Objekttyp>/ vollständig (Standard für
diesen Task-Typ), regeldefinierende Framework-Datei.
VERBOTENE DATEIEN: Andere Objekttypen.
SUCHGRENZE: Rekursiver Scan über den genannten Ordner ist Standard für
diesen Auftrag — keine erneute Freigabe pro Session nötig.
ÄNDERUNGSGRENZE: Keine Korrektur ohne separaten Folgeauftrag.
AUSGABEFORMAT: Befundliste (Datei, Regelverstoß), keine Datei ändern.
ABBRUCHBEDINGUNGEN: Regel selbst widersprüchlich zur Framework-Datei.
```

---

## T8 — Governance / Decision Resolution

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, `00_project/OPEN_DECISIONS.md`, `01_framework/08_templates/decision_template.md`
- Optional laden: betroffenes Einzelobjekt
- Nie automatisch laden: `03_knowledge_base/` breit
- Erlaubte Suche: keine
- Verbotene Suche: jede Suche außerhalb der genannten Entscheidung
- Ausgabeformat: Decision-Dokument nach Template
- Arbeitsmodus: Redakteur, keine eigene Herausgeberentscheidung
- Decision Budget: 1 Dateientscheidung, 0 Suchentscheidungen, 0 Kontextentscheidungen

**Prompt-Vorlage:**
```
TASK_TYPE: T8_GOVERNANCE
ZIEL: <konkrete offene Entscheidung, z. B. OD-XXX> klären/dokumentieren.
ROLLE: Redakteur, keine eigene Herausgeberentscheidung.
ERLAUBTE DATEIEN: 00_project/OPEN_DECISIONS.md, 01_framework/08_templates/decision_template.md.
VERBOTENE DATEIEN: 03_knowledge_base/ breit.
SUCHGRENZE: Keine.
ÄNDERUNGSGRENZE: Nur die benannte Entscheidung, keine Statusänderung anderer
Entscheidungen.
AUSGABEFORMAT: Decision-Dokument nach Template.
ABBRUCHBEDINGUNGEN: Entscheidung erfordert Information, die nicht im Repository steht.
```

---

## T9 — Release / Freeze

**Routing:**
- Immer laden: `CURRENT_STATE.md` (nur Kopf), `00_project/NEXT_ACTION.md`, `00_project/REPOSITORY_KPIS.md`
- Optional laden: `SCIENTIFIC_DEBT.md`-Zeilenzahl (nur Zählung)
- Nie automatisch laden: inhaltliche Neubewertung einzelner Objekte
- Erlaubte Suche: Dateisystemzählung (`find`/`wc`)
- Verbotene Suche: inhaltliche Bewertung (das ist T6, nicht T9)
- Ausgabeformat: Release-Dokument nach etabliertem Muster (Formatreferenz: `99_archive/v1.0_release/`)
- Arbeitsmodus: Release Manager / Configuration Manager, keine fachliche Bewertung
- Decision Budget: 2 Dateientscheidungen, 0 Suchentscheidungen, 1 Kontextentscheidung (Vorgängerbericht als Basis ja/nein)

**Prompt-Vorlage:**
```
TASK_TYPE: T9_RELEASE
ZIEL: <Release-/Freeze-Schritt gemäß Release Plan>.
ROLLE: Release Manager / Configuration Manager — keine fachliche Bewertung.
ERLAUBTE DATEIEN: CURRENT_STATE.md, NEXT_ACTION.md, REPOSITORY_KPIS.md,
Zieldateiname im Release-Namensraum.
VERBOTENE DATEIEN: Inhaltliche Neubewertung einzelner Wissensobjekte (das ist T6).
SUCHGRENZE: Dateisystemzählung (find/wc), keine inhaltliche Prüfung.
ÄNDERUNGSGRENZE: Nur Status-/Zähldokumente, keine Wissensobjekte.
AUSGABEFORMAT: Release-Dokument nach etabliertem Muster.
ABBRUCHBEDINGUNGEN: Zählwerte lassen sich nicht gegen das Dateisystem verifizieren.
```

---

## T10 — Research Project (W-xxx Lifecycle)

**Routing:**
- Immer laden: `06_research_program/RESEARCH_LIFECYCLE.md`, projektlokaler Ordner (`active/<W-xxx>/` bzw. `completed/<W-xxx>/`)
- Optional laden: `RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md`
- Nie automatisch laden: `03_knowledge_base/` breit (außer Stufe 8)
- Erlaubte Suche: projektlokal
- Verbotene Suche/Aktion: Integration betroffener Objekte ohne vorherige Editor Decision (Stufe 7)
- Ausgabeformat: stufenspezifisches Template aus `06_research_program/templates/`
- Arbeitsmodus: je Lifecycle-Stufe unterschiedlich, siehe `RESEARCH_LIFECYCLE.md`
- Decision Budget: 1 Dateientscheidung (Template der aktuellen Stufe), 0 Suchentscheidungen, 0 Kontextentscheidungen

**Prompt-Vorlage:**
```
TASK_TYPE: T10_RESEARCH
ZIEL: <W-xxx>, Stufe <1-9> gemäß RESEARCH_LIFECYCLE.md durchführen.
ROLLE: gemäß Stufendefinition in RESEARCH_LIFECYCLE.md.
ERLAUBTE DATEIEN: 06_research_program/active/<W-xxx>/ bzw. completed/<W-xxx>/,
passendes Template aus 06_research_program/templates/.
VERBOTENE DATEIEN: 03_knowledge_base/ breit (außer Stufe 8, dann nur die im
Editor-Decision-Dokument benannten Objekte).
SUCHGRENZE: Projektlokal.
ÄNDERUNGSGRENZE: Nur die aktuelle Stufe, keine vorgezogene Integration.
AUSGABEFORMAT: Stufenspezifisches Template.
ABBRUCHBEDINGUNGEN: Vorherige Stufe nicht abgeschlossen/freigegeben.
```

---

## T11 — Scientific Debt / Academic Recovery

**Routing:**
- Immer laden: `00_project/SCIENTIFIC_DEBT.md`, `00_project/ACADEMIC_RECOVERY_PLAN.md`
- Optional laden: `05_research/LITERATURE_INDEX.md`
- Nie automatisch laden: Objekte außerhalb des Plans
- Erlaubte Suche: externe Websuche zur Quellenverifikation
- Verbotene Suche: interne Volltextsuche als Ersatz für Recherche
- Ausgabeformat: Erweiterung bestehender Objekte + Plan-Update
- Arbeitsmodus: Rechercheur, keine neuen Objekte ohne Plan-Bezug
- Decision Budget: 1 Dateientscheidung, 0 Suchentscheidungen (intern), 0 Kontextentscheidungen

**Prompt-Vorlage:**
```
TASK_TYPE: T11_SCIDEBT
ZIEL: <AR-XXX> gemäß ACADEMIC_RECOVERY_PLAN.md bearbeiten.
ROLLE: Rechercheur, keine neuen Wissensobjekte ohne Plan-Bezug.
ERLAUBTE DATEIEN: SCIENTIFIC_DEBT.md, ACADEMIC_RECOVERY_PLAN.md, LITERATURE_INDEX.md,
die im Plan benannten Zielobjekte.
VERBOTENE DATEIEN: Objekte außerhalb des Plans.
SUCHGRENZE: Externe Websuche zur Quellenverifikation; keine interne Volltextsuche
als Ersatz für Recherche.
ÄNDERUNGSGRENZE: Nur Erweiterung bestehender Objekte, kein neues Objekt ohne
Plan-Bezug.
AUSGABEFORMAT: Plan-Update + erweiterte Zielobjekte.
ABBRUCHBEDINGUNGEN: Quelle nicht auffindbar/verifizierbar.
```

---

## T12 — Publikationsarbeit (vorbereitet, noch nicht aktiv)

**Routing:**
- Immer laden: `SESSION_BRIEF.md`, thematisch benannte, validierte Objekte
- Optional laden: —
- Nie automatisch laden: Entwurfsobjekte (Status ≠ „Validiert")
- Erlaubte Suche: thematische Mehrfachsuche innerhalb `03_knowledge_base/`, rein lesend
- Verbotene Suche/Aktion: jede Schreiboperation in `03_knowledge_base/`
- Ausgabeformat: Publikations-Textentwurf im Zielordner
- Arbeitsmodus: Lektor/Autor für Zielformat, liest nur
- Decision Budget: 3 Dateientscheidungen, 2 Suchentscheidungen, 0 Kontextentscheidungen

**Prompt-Vorlage:**
```
TASK_TYPE: T12_PUBLIKATION
ZIEL: <Zielformat, z. B. Workbook-Kapitel> aus validierten Objekten erstellen.
ROLLE: Lektor/Autor für Zielformat, liest nur aus der Wissensbasis.
ERLAUBTE DATEIEN: 05_publications/<Zielordner>/, thematisch benannte
03_knowledge_base/-Objekte mit Status "Validiert".
VERBOTENE DATEIEN: Entwurfsobjekte (Status ≠ "Validiert"), jede Schreiboperation
in 03_knowledge_base/.
SUCHGRENZE: Thematische Mehrfachsuche in 03_knowledge_base/ erlaubt, rein lesend.
ÄNDERUNGSGRENZE: Nur Dateien in 05_publications/.
AUSGABEFORMAT: Publikations-Textentwurf im Zielordner.
ABBRUCHBEDINGUNGEN: Zu wenige validierte Objekte für das Thema vorhanden.
```

---

## Anhang: Context-Budget-Referenz (grobe Schätzung, ≈ 4 Zeichen/Token)

| Komponente | Token (≈) |
|---|---|
| Bootstrap (`PROJECT_BOOTSTRAP.md`) | ≈ 1.900 |
| Session Brief (`SESSION_BRIEF.md`) | ≈ 420 |
| Next Action (`00_project/NEXT_ACTION.md`) | ≈ 1.100 |
| **Fixer Sessionstart-Anteil** | **≈ 3.400** |
| Framework (variabel je Typ) | 0–2.500 |
| Task-spezifische Dateien (variabel je Typ) | ≈ 500–15.000 |
| Knowledge Objects (≈ 850 Token/Objekt, variabel je Typ) | 0 bis N × 850 |

Details und Beispielrechnungen je Task-Typ: `99_archive/00_project_history/SALES_CODEX_DECISION_ARCHITECTURE_AUDIT_2026-07-05.md`, Teil 6.

---

*Änderungen an dieser Datei: nur mit Begründung, analog zu Framework-Dateien. Erweiterung um weitere Task-Typen erst nach realem Bedarf (z. B. T12, sobald ein erster Publikations-Sprint tatsächlich stattfindet), nicht spekulativ vorab.*
