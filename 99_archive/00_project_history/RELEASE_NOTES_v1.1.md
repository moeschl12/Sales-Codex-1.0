# Sales Codex OS — Release Notes v1.1

Version: 1.1 — Release Candidate  
Stand: 2026-06-30  
Grundlage: POST_MORTEM_B0002.md  
Status: Entwurf — wartet auf Herausgeber-Freigabe zur Implementierung

---

## 1. Ziel von v1.1

Sales Codex OS v1.1 ist ein **Prozess- und Framework-Update**, kein Inhalts-Update. Die Wissensobjekte (ST, A, MEC, P, T, MOD) bleiben unverändert. Es werden ausschließlich die Arbeitsregeln, Templates und Ablagekonventionen optimiert — basierend auf den Erkenntnissen aus dem ersten vollständigen Produktivdurchlauf (B-0002 Influence).

**Leitfrage:** Was muss am OS geändert werden, damit der nächste Buchanalysedurchlauf (B-0003) effizienter, konsistenter und fehlerärmer abläuft als B-0002?

**Nicht-Ziele von v1.1:**
- Keine Änderungen an bestehenden Wissensobjekten
- Keine Änderungen an der Ordnerstruktur
- Kein Einfrieren oder Löschen von Dokumenten ohne explizite Herausgeber-Entscheidung
- Keine Überarbeitung der Methodik selbst (Evidenzsystem, Objekttypen, CKM-Grundlogik)

---

## 2. Entscheidungsübersicht

### 2.1 Übernommene Empfehlungen (11)

| ID  | Empfehlung                                        | Quelle      | Implementierungsphase |
|-----|---------------------------------------------------|-------------|----------------------|
| A1  | Book Mode offiziell einführen                     | Post-Mortem | Phase 3              |
| A2  | BOOK_REVIEW_REPORT-Template anlegen               | Post-Mortem | Phase 2              |
| A3  | "Nicht-Anlage"-Dokumentation als CKM-Pflicht      | Post-Mortem | Phase 3              |
| A4  | Stateless-Abschluss als Session-Pflicht           | Post-Mortem | Phase 3              |
| A5  | Ausgabe-Verifikationspflicht beim Source-Anlegen  | Post-Mortem | Phase 1              |
| A6  | OR-Formulierung für Prinzipien-Regel              | Post-Mortem | Phase 1              |
| B1  | VAL-Ablage vereinheitlichen (ab VAL-0003)         | Post-Mortem | Phase 3              |
| B2  | Kapitelstatus als Pflichtschritt in TASK-0003     | Post-Mortem | Phase 1              |
| B4  | Abbruchbedingungen in NEXT_ACTION mitführen       | Post-Mortem | Phase 1              |
| B5  | Technik-Kompetenz-Abgrenzung definieren           | Post-Mortem | Phase 2              |
| B6  | model_template.md ergänzen                        | Post-Mortem | Phase 2              |

### 2.2 Modifizierte Empfehlung (1)

| ID  | Empfehlung (original)         | Entscheidung                            |
|-----|-------------------------------|-----------------------------------------|
| B3  | Redundante Dokumente archivieren (löschen / entfernen) | Nicht in der ursprünglichen Form. Stattdessen: Dokumentklassifizierung einführen. Dokumente erhalten eine explizite Kategorie (Operational / Reference / Archived) und werden entsprechend eingeordnet — nicht gelöscht. |

### 2.3 Nicht übernommene Empfehlungen (C1–C5)

| ID  | Empfehlung                                     | Begründung für Zurückstellung              |
|-----|------------------------------------------------|--------------------------------------------|
| C1  | Cluster-Matrix als A-Objekt-Begleitung         | Aufwand > Nutzen in dieser Phase. Zurückgestellt auf v1.2. |
| C2  | ID-Counter-Skript                              | Nützlich, aber nicht kritisch. Zurückgestellt auf v1.2. |
| C3  | Gemini-Validierung als eigener Task-Typ        | Erfordert Konventionen, die noch nicht definiert sind. Zurückgestellt. |
| C4  | Vereinheitlichte Abschluss-Checkliste          | Wird durch Book Mode teilweise abgedeckt. Prüfen nach B-0003. |
| C5  | SPIN+Cialdini-Integrationsmodell (MOD-0003)    | Inhaltsarbeit, kein OS-Update. Für B-0003 oder danach. |

### 2.4 Neue Features (2)

| ID  | Feature                  | Typ           | Implementierungsphase |
|-----|--------------------------|---------------|-----------------------|
| N1  | Repository KPIs           | Neues Konzept | Phase 4               |
| N2  | Scientific Debt           | Neues Konzept | Phase 4               |

---

## 3. Entscheidungsbegründungen

### A1 — Book Mode offiziell einführen

**Entscheidung:** Übernehmen.

Der Influence-Durchlauf hat gezeigt, dass der vollständige Workflow (SRC → BOOK_REVIEW) ohne Zwischenfreigaben durchführbar ist, wenn die methodischen Regeln vorab etabliert sind. Zwischenfreigaben bei TASK-0003 bis TASK-0005 haben keinen messbaren Qualitätsbeitrag geleistet — die methodischen Impulse (n:m-Clustering, Abgrenzungspflicht) hätten ebenso gut als vorab definierte Regeln formuliert werden können.

Book Mode bedeutet: Nach Freigabe des Task-Proposals arbeitet die KI den vollständigen Workflow autonom durch, bis BOOK_REVIEW erstellt ist. Stopp nur bei definierten Abbruchbedingungen.

**Abbruchbedingungen (unverändert):**
1. Primärquelle nicht zugänglich
2. Unauflösbarer Canonicalisierungskonflikt
3. Ethischer Grenzfall
4. Framework-Änderung erforderlich

**Betroffene Dateien:** `00_project/task_rules.md`, `00_project/SALES_CODEX_OPERATING_MANUAL.md`, `00_project/COWORK_EXECUTION_PROTOCOL.md`

---

### A2 — BOOK_REVIEW_REPORT-Template anlegen

**Entscheidung:** Übernehmen.

`BOOK_REVIEW_REPORT_B0002.md` wurde ohne Template entwickelt. Für B-0003 benötigen wir ein Template, das das Format standardisiert und vergleichbare Ausgaben erzeugt. Das Template wird aus BOOK_REVIEW_REPORT_B0002.md abgeleitet.

**Betroffene Dateien:** NEU: `01_framework/08_templates/book_review_template.md`

---

### A3 — "Nicht-Anlage"-Dokumentation als CKM-Pflicht

**Entscheidung:** Übernehmen.

Bisher dokumentiert das CKM nur EXTEND- und NEW-Entscheidungen. Kandidaten, die bewusst NICHT angelegt werden (z.B. Scarcity-as-value-heuristic als eigenständiger MEC), sind nicht formal erfasst. Das Risiko: Spätere Sessions prüfen denselben Kandidaten erneut und kommen zu derselben Entscheidung — ohne zu wissen, dass diese bereits getroffen wurde.

Ergänzung im CKM: Abschnitt "Rejected Candidates" — Dokumentationspflicht bei bewusster Nicht-Anlage.

**Betroffene Dateien:** `01_framework/05_knowledge_model/canonical_knowledge_model.md`, `01_framework/08_templates/book_analysis_template.md` (optionaler Abschnitt "Rejected MEC-Kandidaten")

---

### A4 — Stateless-Abschluss als Session-Pflicht

**Entscheidung:** Übernehmen.

Die Stateless Architecture funktioniert nur, wenn CURRENT_STATE.md, NEXT_ACTION.md und SESSION_LOG.md am Ende jeder Session zuverlässig aktualisiert werden. Aktuell ist das eine Empfehlung, kein erzwungener letzter Schritt. Book Mode verankert diesen Schritt als Pflichtabschluss.

**Betroffene Dateien:** `00_project/task_rules.md`

---

### A5 — Ausgabe-Verifikationspflicht beim Source-Anlegen

**Entscheidung:** Übernehmen.

Der Ausgabenfehler (2021 statt 2007) entstand, weil die Ausgabe aus dem Gedächtnis angenommen wurde. Lösung: Ein neues Pflichtfeld im Source-Template — "Ausgabe aus Impressum verifiziert: [Seite X]" — stellt sicher, dass die Ausgabe direkt aus dem Primärtext belegt wird, bevor die SRC-Datei als vollständig gilt.

**Betroffene Dateien:** `01_framework/08_templates/source_template.md`

---

### A6 — OR-Formulierung für Prinzipien-Regel

**Entscheidung:** Übernehmen.

task_rules.md enthält aktuell die Anforderung, dass Prinzipien auf mehrere Wissensobjekte zurückgeführt werden müssen — aber die OR-Bedingung ("mehrere Mechanismen ODER mehrere Annahmen") ist nicht explizit formuliert. Fünf Prinzipien aus B-0002 referenzieren einen Hauptmechanismus und zwei Annahmen — korrekt, aber ohne explizite Regelgrundlage.

**Betroffene Dateien:** `00_project/task_rules.md`

---

### B1 — VAL-Ablage vereinheitlichen

**Entscheidung:** Übernehmen (prospektiv, keine Rückwirkung).

VAL-0001 und VAL-0002 liegen in `00_project/` — historisch begründet, aber konzeptuell inkonsistent (sie sind quellspezifische Reviews, keine projektweiten Dokumente). Ab VAL-0003 gilt: VAL-Objekte werden in `04_book_analysis/[Buch]/` abgelegt. VAL-0001 und VAL-0002 bleiben wo sie sind.

**Betroffene Dateien:** `00_project/task_rules.md` (Ablageregel aktualisieren), `00_project/SALES_CODEX_OPERATING_MANUAL.md`

---

### B2 — Kapitelstatus als Pflichtschritt in TASK-0003

**Entscheidung:** Übernehmen.

Nach Abschluss von TASK-0003 muss die Kapitelstatustabelle in analysis.md auf "analysiert" gesetzt werden. Das wird als expliziter Sub-Schritt in der task_rules.md TASK-0003-Beschreibung verankert.

**Betroffene Dateien:** `00_project/task_rules.md`, `01_framework/08_templates/book_analysis_template.md`

---

### B3 (modifiziert) — Dokumentklassifizierung statt Archivierung

**Entscheidung:** Modifiziert übernehmen.

Statt Dokumente zu löschen oder zu archivieren, erhalten alle Dokumente in `00_project/` und `01_framework/` eine explizite Klassifizierung:

| Klasse | Bedeutung | Beispiele |
|--------|-----------|-----------|
| **Operational** | Aktiv genutzt in jeder Session; KI muss diese kennen | backlog.md, CURRENT_STATE.md, NEXT_ACTION.md, SESSION_LOG.md, task_rules.md |
| **Reference** | Bei Bedarf nachschlagen; KI liest nur wenn relevant | Operating Manual, Execution Protocol, alle Templates, agent_protocols/, codex_methodology.md, canonical_knowledge_model.md |
| **Archived** | Historisch; nicht mehr aktiv genutzt; nicht löschen | CLAUDE_BOOTSTRAP.md, roadmap.md, review_queue.md |

Implementierung: Ein `## Dokumentklasse` Feld in der Kopfzeile jedes betroffenen Dokuments.

**Begründung für Modifikation:** Dokumente zu löschen birgt Risiko des Informationsverlusts. Klassifizierung ermöglicht dasselbe Ziel (kognitiver Fokus auf operative Dokumente) ohne destruktive Aktion. PROJECT_BOOTSTRAP.md kann die Klassen-Unterschiede explizit benennen.

**Betroffene Dateien:** PROJECT_BOOTSTRAP.md (Klassifizierungssystem dokumentieren), alle zu klassifizierenden Dokumente (Header-Update)

---

### B4 — Abbruchbedingungen in NEXT_ACTION mitführen

**Entscheidung:** Übernehmen.

NEXT_ACTION.md ist das erste Dokument, das eine neue Session liest. Die Abbruchbedingungen stehen aktuell in PROJECT_BOOTSTRAP.md. Für den Book Mode sollen die aktuell gültigen Abbruchbedingungen direkt in NEXT_ACTION.md sichtbar sein — als kompakter Block, nicht als vollständige Beschreibung.

**Betroffene Dateien:** `00_project/NEXT_ACTION.md` (Template-Konvention), `00_project/task_rules.md` (Regel für NEXT_ACTION-Format)

---

### B5 — Technik-Kompetenz-Abgrenzung definieren

**Entscheidung:** Übernehmen.

Die Grenze zwischen T-Objekt (Technik) und "Verknüpfte Kompetenz" ist nicht explizit definiert. Rapport/Ähnlichkeits-Signalisierung wurde als Kompetenz eingestuft, aber ohne formale Regelgrundlage. Das technique_template.md erhält einen Hinweisabschnitt, und task_rules.md erhält eine Definition.

**Operationale Definition:**
- **Technik (T-Objekt):** Eine konkrete, wiederholbare Handlung mit definierten Auslöse- und Abschlussbedingungen. Sie kann in einem einzelnen Gespräch gezielt eingesetzt werden.
- **Kompetenz:** Eine übergeordnete Fähigkeit, die Hintergrundvoraussetzung für Techniken ist, aber keine einzelne Handlung darstellt. Sie entwickelt sich über Zeit.

**Betroffene Dateien:** `00_project/task_rules.md`, `01_framework/08_templates/technique_template.md`

---

### B6 — model_template.md ergänzen

**Entscheidung:** Übernehmen.

Das existierende model_template.md ist unvollständig: Es fehlen das Source-ID-Feld, ein Canonicalisierungsabschnitt und das Quervergleichs-Feld (Vergleich mit bestehenden MOD-Objekten). MOD-0002 wurde ohne Template erstellt — das Risiko für B-0003 ist ein inkonsistentes drittes Modellobjekt.

**Betroffene Dateien:** `01_framework/08_templates/model_template.md`

---

### N1 — Repository KPIs

**Entscheidung:** Als neues Konzept aufnehmen.

KPIs ermöglichen quantitativen Vergleich zwischen Buchanalysen und Erkennung von Mustern (z.B. "Cialdini produziert mehr Mechanismen pro Statement als SPIN"). Sie sind auch ein Qualitätssignal: Eine Canonicalization Rate von 0% bedeutet, dass keine bestehenden Objekte wiederverwendet wurden — möglicherweise ein Zeichen für Duplikatrisiken.

**Definierte KPIs:**

| KPI | Definition | Beispiel B-0002 |
|-----|------------|-----------------|
| Statements pro Buch | Anzahl ST-Objekte | 26 |
| Annahmen pro Buch | Anzahl A-Objekte (neu) | 8 |
| Mechanismen pro Buch | Anzahl MEC-Objekte (neu + erweitert) | 8 (5 neu + 3 ext.) |
| Prinzipien pro Buch | Anzahl P-Objekte (neu) | 8 |
| Techniken pro Buch | Anzahl T-Objekte (neu) | 7 |
| Canonicalization Rate | Erweiterte MECs / (neue + erweiterte MECs) | 3/8 = 37,5% |
| Reuse Rate | Objekte mit Source-ID aus >1 Buch / Gesamtobjekte | TBD nach B-0003 |
| Neue Objekte gesamt | Alle neu angelegten Objekte (ST+A+MEC+P+T+MOD) | 59 |
| Scientific Confidence | Anteil Objekte mit E3 oder höher | TBD |
| Open Questions | Anzahl dokumentierter offener Fragen in VAL | 5 |

**Implementierung:** Neues Dokument `00_project/REPOSITORY_KPIS.md` als Konzept und Tracking-Tabelle. Wird nach jedem Buch manuell aktualisiert.

---

### N2 — Scientific Debt

**Entscheidung:** Als neues Konzept aufnehmen.

Analogie zu technischen Schulden: Wissenschaftliche Schulden sind Wissensobjekte oder Behauptungen, bei denen die Evidenzbasis bekanntermaßen unvollständig ist — und die für eine spätere Validierung vorgemerkt sind.

**Kategorien:**

| Kategorie | Definition | Beispiel aus B-0002 |
|-----------|------------|---------------------|
| Replikationsrisiko | Studie existiert, aber Replikationsstatus unklar | Cialdini-Studien (Milgram-Variationen, Langer-Xerox) |
| Externe Validierung ausstehend | Gemini- oder Perplexity-Prüfung noch nicht durchgeführt | MEC-0005 bis MEC-0009 |
| Unbelegte Annahme | A-Objekt ohne direkte Primärquelle | A-0007 (evolutionäre Verankerung) |
| Widersprüchliche Evidenz | Zwei Quellen widersprechen sich, kein Urteil möglich | SPIN vs. Cialdini (Methodik-Ebene) |
| Offene Forschungsfrage | Bekannte Lücke, kein Beleg vorhanden | B2B-Reziprozitätsbelege |

**Tracking:** Scientific Debt wird im VAL-Objekt jedes Buches dokumentiert und in einem zentralen Dokument `00_project/SCIENTIFIC_DEBT.md` konsolidiert. Kein aktiver Schuldenabbau bis zur Gemini-Validierungsphase.

---

## 4. Bewertungsmatrix

| ID  | Empfehlung                          | Nutzen | Risiko | Aufwand | Betroffene Dateien (Anzahl) |
|-----|-------------------------------------|--------|--------|---------|-----------------------------|
| A1  | Book Mode                           | Hoch   | Mittel | Mittel  | 3                           |
| A2  | BOOK_REVIEW Template                | Hoch   | Niedrig| Niedrig | 1 (neu)                     |
| A3  | Nicht-Anlage-Dokumentation          | Mittel | Niedrig| Niedrig | 2                           |
| A4  | Stateless-Abschluss als Pflicht     | Hoch   | Niedrig| Minimal | 1                           |
| A5  | Source-Verifikationspflicht         | Hoch   | Niedrig| Minimal | 1                           |
| A6  | OR-Formulierung Prinzipien          | Mittel | Niedrig| Minimal | 1                           |
| B1  | VAL-Ablage vereinheitlichen         | Mittel | Niedrig| Minimal | 2                           |
| B2  | Kapitelstatus als Pflichtschritt    | Mittel | Niedrig| Minimal | 2                           |
| B3m | Dokumentklassifizierung             | Mittel | Niedrig| Mittel  | 10–15                       |
| B4  | Abbruchbedingungen in NEXT_ACTION   | Mittel | Niedrig| Minimal | 2                           |
| B5  | Technik-Kompetenz-Abgrenzung        | Mittel | Niedrig| Niedrig | 2                           |
| B6  | model_template ergänzen             | Mittel | Niedrig| Niedrig | 1                           |
| N1  | Repository KPIs                     | Mittel | Niedrig| Niedrig | 1 (neu)                     |
| N2  | Scientific Debt                     | Mittel | Niedrig| Niedrig | 1 (neu)                     |

**Risikohinweis A1 (Book Mode):**
Das Hauptrisiko ist, dass methodische Fehler ohne Zwischenfreigaben erst im Post-Mortem sichtbar werden. Mitigation: Die Abbruchbedingungen werden schärfer formuliert, und VAL (TASK-0009) bleibt als interner Qualitätsstopp erhalten.

---

## 5. Breaking Changes

Folgende Verhaltensänderungen betreffen die KI direkt — sie verändern das erwartete Verhalten gegenüber v1.0:

| # | Change | Betroffen ab |
|---|--------|--------------|
| 1 | **Kein Task-by-Task-Freigabemodus** nach Task-Proposal-Freigabe. Book Mode ist Standard. | B-0003 |
| 2 | **VAL-Objekte** werden nicht mehr in `00_project/` angelegt, sondern in `04_book_analysis/[Buch]/`. | B-0003 / VAL-0003 |
| 3 | **Abschluss jeder Session** erfordert Aktualisierung von CURRENT_STATE.md, NEXT_ACTION.md, SESSION_LOG.md. | sofort |
| 4 | **Nicht-Anlage-Entscheidungen** bei MEC/P/T-Kandidaten müssen formal dokumentiert werden. | sofort |
| 5 | **Source-Anlage** ohne verifizierten Impressum-Beleg ist unvollständig. | B-0003 |

---

## 6. Implementierungsplan

Die Implementierung erfolgt in vier Phasen. Phasen sind sequenziell — keine Phase beginnt, bevor die vorherige freigegeben ist (oder alle Schritte einer Phase können in einem Schritt freigegeben werden).

---

### Phase 1 — Minimale Regelkorrekturen (Aufwand: sehr gering)

Ziel: Sofort wirksame, risikoarme Regeländerungen in bestehenden Dokumenten.

| Schritt | Datei | Änderung |
|---------|-------|----------|
| 1.1 | `01_framework/08_templates/source_template.md` | Pflichtfeld ergänzen: `## Ausgabe aus Impressum verifiziert` |
| 1.2 | `00_project/task_rules.md` | OR-Formulierung in Prinzipien-Regel explizit machen (Abschnitt 5) |
| 1.3 | `00_project/task_rules.md` | Sub-Schritt nach TASK-0003 ergänzen: "Kapitelstatus auf 'analysiert' setzen" |
| 1.4 | `01_framework/08_templates/book_analysis_template.md` | Hinweis auf Kapitelstatus-Pflichtschritt nach Extraktion |
| 1.5 | `00_project/NEXT_ACTION.md` (Template-Konvention) | Abbruchbedingungen-Block als Pflichtbestandteil definieren; bereits in aktuellem NEXT_ACTION.md umgesetzt — als Konvention in task_rules.md dokumentieren |

---

### Phase 2 — Neue und ergänzte Templates (Aufwand: gering)

Ziel: Vollständige Template-Abdeckung für alle Objekttypen und Ausgabeformate.

| Schritt | Datei | Änderung |
|---------|-------|----------|
| 2.1 | NEU: `01_framework/08_templates/book_review_template.md` | Template aus BOOK_REVIEW_REPORT_B0002.md ableiten |
| 2.2 | `01_framework/08_templates/model_template.md` | Source-ID-Feld ergänzen; Canonicalisierungsabschnitt; Quervergleichs-Feld |
| 2.3 | `01_framework/08_templates/technique_template.md` | Hinweis zur Technik-vs-Kompetenz-Abgrenzung ergänzen |

---

### Phase 3 — Workflow-Regeln und Ablagekonventionen (Aufwand: mittel)

Ziel: Book Mode, Stateless-Pflicht, CKM-Ergänzung, VAL-Ablage.

| Schritt | Datei | Änderung |
|---------|-------|----------|
| 3.1 | `00_project/task_rules.md` | Book Mode als Standardworkflow definieren; Abschluss-Pflicht (CURRENT_STATE + NEXT_ACTION + SESSION_LOG) als letzten Schritt verankern |
| 3.2 | `00_project/SALES_CODEX_OPERATING_MANUAL.md` | Book Mode beschreiben; VAL-Ablage-Regel auf `04_book_analysis/[Buch]/` aktualisieren |
| 3.3 | `00_project/COWORK_EXECUTION_PROTOCOL.md` | Book Mode Verhaltensregeln für KI ergänzen |
| 3.4 | `01_framework/05_knowledge_model/canonical_knowledge_model.md` | Neuer Abschnitt: "Rejected Candidates — Nicht-Anlage-Dokumentation" |
| 3.5 | `00_project/task_rules.md` | VAL-Ablageregel aktualisieren: ab VAL-0003 → `04_book_analysis/[Buch]/` |
| 3.6 | `00_project/task_rules.md` | Technik-vs-Kompetenz-Unterschied als Definition ergänzen |

---

### Phase 4 — Neue Konzeptdokumente und Klassifizierung (Aufwand: gering–mittel)

Ziel: Scientific Debt, Repository KPIs, Dokumentklassifizierung.

| Schritt | Datei | Änderung |
|---------|-------|----------|
| 4.1 | NEU: `00_project/SCIENTIFIC_DEBT.md` | Scientific-Debt-Konzept + initiale Einträge aus B-0001 und B-0002 |
| 4.2 | NEU: `00_project/REPOSITORY_KPIS.md` | KPI-Framework + initiale Messwerte für B-0001 und B-0002 |
| 4.3 | `PROJECT_BOOTSTRAP.md` | Dokumentklassifizierungssystem (Operational / Reference / Archived) beschreiben |
| 4.4 | Operational-Dokumente (6) | Header-Update: `## Dokumentklasse: Operational` |
| 4.5 | Reference-Dokumente (ca. 12) | Header-Update: `## Dokumentklasse: Reference` |
| 4.6 | Archived-Dokumente (3) | Header-Update: `## Dokumentklasse: Archived` |

**Dokumentklassifizierung — vorläufige Zuordnung:**

| Dokument | Klasse |
|----------|--------|
| backlog.md | Operational |
| CURRENT_STATE.md | Operational |
| NEXT_ACTION.md | Operational |
| SESSION_LOG.md | Operational |
| OPEN_DECISIONS.md | Operational |
| task_rules.md | Operational |
| SALES_CODEX_OPERATING_MANUAL.md | Reference |
| COWORK_EXECUTION_PROTOCOL.md | Reference |
| canonical_knowledge_model.md | Reference |
| codex_methodology.md | Reference |
| evidence_system.md | Reference |
| principle_extraction_standard.md | Reference |
| codex_source_standard.md | Reference |
| sales_process_decision_system.md | Reference |
| Alle Templates (08_templates/) | Reference |
| Alle Agent-Protokolle (07_agent_protocols/) | Reference |
| CLAUDE_BOOTSTRAP.md | Archived |
| roadmap.md | Archived |
| review_queue.md | Archived |

---

## 7. Neue Dateien (Gesamtübersicht)

| Datei | Phase | Typ |
|-------|-------|-----|
| `01_framework/08_templates/book_review_template.md` | 2 | Neues Template |
| `00_project/SCIENTIFIC_DEBT.md` | 4 | Neues Konzeptdokument |
| `00_project/REPOSITORY_KPIS.md` | 4 | Neues Konzeptdokument |

---

## 8. Geänderte Dateien (Gesamtübersicht)

| Datei | Phase | Art der Änderung |
|-------|-------|-----------------|
| `01_framework/08_templates/source_template.md` | 1 | Pflichtfeld ergänzt |
| `00_project/task_rules.md` | 1, 3 | Mehrere Regelergänzungen |
| `01_framework/08_templates/book_analysis_template.md` | 1 | Hinweis Kapitelstatus |
| `01_framework/08_templates/model_template.md` | 2 | Fehlende Felder ergänzt |
| `01_framework/08_templates/technique_template.md` | 2 | Technik-Kompetenz-Hinweis |
| `00_project/SALES_CODEX_OPERATING_MANUAL.md` | 3 | Book Mode + VAL-Ablage |
| `00_project/COWORK_EXECUTION_PROTOCOL.md` | 3 | Book Mode Verhaltensregeln |
| `01_framework/05_knowledge_model/canonical_knowledge_model.md` | 3 | Rejected Candidates Abschnitt |
| `PROJECT_BOOTSTRAP.md` | 4 | Dokumentklassifizierung |
| Ca. 21 Dokumente | 4 | Header: Dokumentklasse |

---

## 9. Was sich für den Herausgeber ändert

- Der Herausgeber gibt **ein Task-Proposal** frei, nicht mehr jeden einzelnen Task.
- Der Herausgeber erhält nach dem Workflow direkt **ein BOOK_REVIEW_REPORT** und das **Post-Mortem**.
- Bei Abbruchbedingungen wird weiterhin sofort eskaliert.
- Alle Framework-Änderungen bleiben unter Herausgeber-Freigabe.

---

*Dieser Release Candidate gilt als Entwurf bis zur expliziten Freigabe durch Felix. Nach Freigabe beginnt die Implementierung mit Phase 1.*
