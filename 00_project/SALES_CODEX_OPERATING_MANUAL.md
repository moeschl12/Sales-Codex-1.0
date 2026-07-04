# Sales Codex — Operating Manual

Version: 1.0  
Stand: 2026-06-27  
Geltungsbereich: Alle Buchanalysen im Sales Codex Repository

---

## 1. Zweck dieses Dokuments

Dieses Operating Manual ist die verbindliche Arbeitsanweisung für die systematische Verarbeitung von Büchern und anderen Primärquellen nach dem Sales-Codex-Standard.

Es regelt: wer was tut, in welcher Reihenfolge, nach welchem Standard — und unter welchen Bedingungen eine Arbeit abgebrochen oder eskaliert wird.

Das Repository ist die Quelle der Wahrheit. Dieses Dokument beschreibt, wie Wissen dorthinein gelangt.

---

## 2. Rollenmodell

### Felix — Herausgeber

Letztentscheid über:
- Aufnahme oder Ablehnung von Prinzipien
- methodische Richtungsänderungen
- ethische Grenzfragen
- Veröffentlichungsversionen
- Git-Commits

Felix ist nicht der Produzent. Felix ist der Entscheider.

### Claude / Cowork — Produktions- und Redaktionssystem

Zuständig für:
- Extraktion aller Wissensobjekte aus Primärquellen
- Anlage und Pflege von ST-, A-, MEC-, P-, T-, MOD-Objekten
- Stil, Einheitlichkeit, Vollständigkeit
- Internen Konsistenz-Review
- Abschlussbericht

Claude arbeitet ausschließlich auf Basis des Repositories. Eigene Erinnerung ist keine Quelle der Wahrheit.

### ChatGPT — Scientific & Systems Editor

Zuständig für:
- Aufbau und Stress-Test von Frameworks und Modellen
- Prinzip-Extraktion und Strukturkritik
- Identifikation logischer Widersprüche
- Modell- und Meta-Modell-Entwicklung

ChatGPT darf keine finalen Prinzipien setzen und keine Quellen erfinden.

### Gemini — Wissenschaftliche Validierung

Zuständig für:
- Prüfung von Mechanismus-Behauptungen gegen aktuelle Forschung
- Trennung Korrelation / Kausalität
- Identifikation fehlender oder widersprechender Primärstudien
- Einschätzung der Übertragbarkeit wissenschaftlicher Befunde auf Vertrieb

Gemini darf keine Codex-Prinzipien formulieren und keine Unsicherheiten glätten.

### Perplexity — Quellenrecherche

Zuständig für:
- Suche nach Büchern, Studien, Artikeln, Interviews, Gegenquellen
- Dokumentation mit Datum, Herkunft, Kontext
- Identifikation aktueller Forschungslage zu einem Thema

Perplexity liefert Rohmaterial, keine Analyse.

---

## 3. Standardprozess für jedes Buch

### Schritt 1 — Quelle erfassen

Datei anlegen: `02_sources/books/SRC-XXXX_[title].md`  
Template: `01_framework/08_templates/source_template.md`

Pflichtfelder: Titel, Autor, Jahr, Quellenklasse (A–F), Kontext, Hauptthese, Grenzen der Quelle.  
Status setzen: *Erfasst*.

### Schritt 2 — Statements extrahieren

Pro Kernaussage eine Datei anlegen: `03_knowledge_base/statements/ST-XXXX_[name].md`  
Template: `01_framework/08_templates/statement_template.md`

Pflicht:
- Originalaussage oder Paraphrase (mit Unsicherheitsmarkierung, falls kein Primärtext)
- Aussage-Typ (Definition / Beobachtung / Empfehlung / Methode / Prinzip / Hypothese / Meinung)
- Kontext und Kapitelzuordnung (mit ⚠ wenn unsicher)
- Trennung: Was ist Beobachtung, was ist Interpretation?

### Schritt 3 — Annahmen identifizieren

Pro zugrunde liegender Annahme eine Datei anlegen: `03_knowledge_base/assumptions/A-XXXX_[name].md`  
Template: `01_framework/08_templates/assumption_template.md`

Pflicht:
- Was passiert, wenn die Annahme falsch ist?
- Evidenzstatus
- Modellbezug

### Schritt 4 — Mechanismen ableiten

Pro kausaler Erklärung eine Datei anlegen: `03_knowledge_base/mechanisms/MEC-XXXX_[name].md`  
Template: `01_framework/08_templates/mechanism_template.md`

Mechanismen werden vor Prinzipien angelegt, damit Prinzipien direkt auf MEC-IDs referenzieren können.

Pflicht:
- Mechanismus-Typ (psychologisch / ökonomisch / kommunikativ / sozial / organisatorisch)
- Wissenschaftliche Grundlage (mit Unsicherheitsmarkierung, wenn nur allgemein belegt)
- Evidenzlevel: getrennt für allgemeinen Mechanismus und spezifische Vertriebsanwendung

### Schritt 5 — Prinzipien formulieren

Pro abstrahierter Erkenntnis eine Datei anlegen: `03_knowledge_base/principles/P-XXXX_[name].md`  
Template: `01_framework/08_templates/principle_template.md`

Pflicht:
- Prinzip-Aussage im Format: *Unter Bedingungen X führt Y tendenziell zu Z.*
- Vier Pflichtfragen: Was? Warum? Wann? Wann nicht?
- Evidenzklasse (E1–E5) mit Begründung
- Ethisches Risiko (niedrig / mittel / hoch)
- Verknüpfung mit MEC-IDs (nicht nur Freitextnamen)
- Quervergleich mit allen bestehenden P-Objekten: Abgrenzung explizit dokumentieren

**Quellen-Anforderung (v1.1):** Ein Prinzip muss auf **≥2 Mechanismen ODER ≥2 Annahmen** (oder eine Kombination) zurückgeführt werden. Ein Prinzip, das nur einen MEC referenziert, ist eine Reformulierung des Mechanismus — kein eigenständiges Prinzip. Abgrenzung vom Mechanismus ist Pflichtabschnitt.

### Schritt 6 — Techniken erfassen

Pro praktischem Werkzeug eine Datei anlegen: `03_knowledge_base/techniques/T-XXXX_[name].md`  
Template: `01_framework/08_templates/technique_template.md`

Pflicht:
- Angewendetes Prinzip (P-ID)
- Genutzter Mechanismus (MEC-ID)
- Gesprächszustand (aus Sales Process Decision System)
- Risiken und typische Fehlanwendung

### Schritt 7 — Modelle aktualisieren

Bestehende Modell-Objekte in `03_knowledge_base/models/` ergänzen oder neue anlegen.  
Template: `01_framework/08_templates/model_template.md`

Ein Modell-Objekt listet alle zugehörigen A-, P-, MEC-, T-IDs explizit. Es erklärt die kausallogische Struktur des Modells und dokumentiert Grenzen und Widersprüche zu anderen Modellen.

### Schritt 8 — Selbstreview durchführen

Datei anlegen: `04_book_analysis/[Buch]/VAL-XXXX_consistency_review_[source].md`  
(Hinweis: VAL-0001 und VAL-0002 liegen historisch in `00_project/` — ab VAL-0003 gilt die neue Ablage.)  
Template: `01_framework/08_templates/validation_report_template.md`

Pflichtprüfungen:
- Alle referenzierten IDs existieren als Dateien.
- Keine Mechanismus-Referenz nur als Freitext (immer MEC-IDs).
- Evidenzklassen konsistent und begründet.
- Ethische Risiken vollständig markiert.
- Kapitelzuordnungen unsicherer Aussagen mit ⚠ gekennzeichnet.
- Trennung Beobachtung/Interpretation in jedem ST-Objekt vorhanden.

### Schritt 9 — Abschlussbericht erstellen

Datei anlegen: `00_project/PILOT_XXX_ABSCHLUSSBERICHT.md` (oder entsprechend nummeriert)

Pflichtabschnitte:
1. Erzeugte Wissensobjekte (Tabelle: Typ / Anzahl / IDs)
2. Wichtigste Erkenntnisse (max. 5–7 Kernpunkte)
3. Offene Forschungsfragen (priorisiert)
4. Konsistenzbefunde aus dem Selbstreview
5. Empfehlung für nächste Schritte

---

## 4. Qualitätsstandard für jedes Wissensobjekt

Ein Wissensobjekt ist nur brauchbar, wenn es alle dieser Bedingungen erfüllt:

| Kriterium | Beschreibung |
|---|---|
| Nachvollziehbar | Quelle und Herleitung sind angegeben |
| Eingeordnet | Objekttyp und ID sind korrekt |
| Unsicherheit markiert | Unsichere Aussagen, Kapitelzuordnungen, Quellenangaben sind gekennzeichnet |
| Kontext benannt | Gilt universell / kontextabhängig / branchenspezifisch / situationsgebunden |
| Grenzen beschrieben | Wann funktioniert es nicht? |
| Nicht meinungsbasiert | Keine unbelegte Meinung als Tatsache |
| Template-konform | Entspricht dem passenden Template aus `01_framework/08_templates/` |

---

## 5. Rule of Three: Quellenprinzip vs. Codex-Prinzip

Ein Quellenprinzip ist das, was ein Autor behauptet.  
Ein Codex-Prinzip ist das, was nach kritischer Prüfung über mehrere Quellen hinweg gilt.

**Quellenprinzip:** E1–E2 — aus einer Quelle, noch nicht breit validiert.  
**Codex-Prinzip:** E3–E5 — durch mindestens drei unabhängige Quellen oder Forschungsstränge gestützt.

Neue Codex-Prinzipien entstehen frühestens nach drei unabhängigen Stützquellen oder nach expliziter Herausgeber-Freigabe.

Bis dahin gelten alle extrahierten Prinzipien als Quellenprinzipien mit vorläufigem Evidenzstatus.

---

## 6. Review-Prozess

### Stufe 1 — Technischer Review (Claude / Cowork)

Prüft: ID-Integrität, Template-Konformität, Sprachpolitik, Zählungen, Querverweise.  
Ergebnis: VAL-Objekt im Repository.

### Stufe 2 — Methodischer Review (Claude / ChatGPT)

Prüft: Trennung Beobachtung/Interpretation, Evidenzklassen, Mechanismus-Erklärungen, logische Konsistenz.  
Ergebnis: Annotiertes VAL-Objekt oder korrigierte Wissensobjekte.

### Stufe 3 — Wissenschaftliche Validierung (Gemini)

Prüft: Mechanismus-Behauptungen gegen aktuelle Psychologie- und Verhaltensforschung.  
Ergebnis: Evidenzklassen bestätigt, angehoben oder mit Vorbehalt versehen.

### Stufe 4 — Herausgeber-Freigabe (Felix)

Felix entscheidet: Objekte werden akzeptiert, zurückgestellt oder abgelehnt.  
Keine finale Integration ohne Freigabe bei E3-Stufung oder höher.

### Stufe 5 — Git-Commit

Erst nach Stufe 4.  
Commit-Nachricht beschreibt Quelle, Anzahl Objekte und Review-Status.

---

## 7. Abbruchbedingungen

Folgende Zustände führen zu einem Arbeitsstopp und Eskalation an Felix:

| Bedingung | Maßnahme |
|---|---|
| Primärquelle nicht zugänglich | Arbeit stoppen. Nur mit expliziter Freigabe auf Trainingswissen ausweichen — dann vollständige Unsicherheitsmarkierung |
| Kapitelzuordnung nicht klärbar | Statement mit ⚠ tentativ anlegen; nicht für Prinzipextraktion verwenden, bis geklärt |
| Widersprüchliche Evidenz zwischen Quellen | Widerspruch dokumentieren, nicht auflösen. Kein Codex-Prinzip formulieren, bis Widerspruch geklärt |
| Unsicherheit bei Objektklassifikation | Lieber als Statement anlegen als falsch als Prinzip klassifizieren. Klassifikationsfrage in Offene Fragen dokumentieren |
| Ethischer Grenzfall | Sofortige Eskalation an Felix. Keine eigenständige Entscheidung |

---

## 8. Arbeitsverbote

Diese Handlungen sind unter allen Umständen verboten:

- **Keine Framework-Änderungen** — Ordnerstruktur, Templates und Methodik werden nicht eigenständig modifiziert.
- **Keine neuen Templates** — Templates entstehen nur nach expliziter Herausgeber-Entscheidung.
- **Keine erfundenen Quellen** — Jede Quellenangabe muss real und nachvollziehbar sein.
- **Keine glättende Zusammenfassung** — Widersprüche werden dokumentiert, nicht wegformuliert.
- **Keine unbelegte Verallgemeinerung** — Was für eine Quelle gilt, gilt nicht automatisch für alle Kontexte.
- **Kein Bestsellerstatus als Wahrheitsbeweis** — Popularität ist kein Evidenzargument.
- **Keine manipulativen Techniken neutral darstellen** — Ethisches Risiko immer markieren.
- **Keine Chatverläufe als Wissensbasis** — Wissen lebt im Repository, nicht in Sessions.
- **Keine Kapitel vorwegnehmen** — Extraktion beschränkt sich auf den analysierten Textteil.

---

## 9. Standardausgabe nach jedem Buch

Jeder Buchanalyse-Abschluss liefert exakt diese Ausgabe — nicht mehr, nicht weniger:

### 9.1 Erzeugte Objekte

Tabellarische Übersicht: Objekttyp / Anzahl / ID-Bereich.

### 9.2 Wichtigste Erkenntnisse

Maximal 7 Kernpunkte. Konkret, direkt aus den Wissensobjekten abgeleitet. Keine neuen Behauptungen.

### 9.3 Offene Forschungsfragen

Priorisierte Liste. Mindestens:
- Welche Aussagen müssen extern validiert werden?
- Welche Mechanismen sind noch nicht ausreichend belegt?
- Welche Vergleiche mit anderen Quellen stehen aus?

### 9.4 Konsistenzbefunde

Zusammenfassung des Selbstreviews (VAL-Objekt):
- Behobene Befunde
- Offene Befunde
- Keine Befunde (wenn sauber)

### 9.5 Empfehlung für nächsten Schritt

Genau eine konkrete Empfehlung:
- Welche Quelle als nächstes?
- Oder: Welche Validierungsaufgabe zuerst?
- Oder: Welcher Widerspruch muss zuerst aufgelöst werden?

---

---

## 10. Book Mode (v1.1)

**Dokumentklasse: Reference**

Ab Sales Codex OS v1.1 ist Book Mode der Standardmodus für alle Buchanalysen.

**Definition:** Nach Freigabe des Task-Proposals arbeitet Cowork den vollständigen Workflow (Schritte 1–9) ohne Zwischenfreigaben durch. Cowork eskaliert nur bei den definierten Stopp-Bedingungen (s. Abschnitt 7). Alle anderen Unsicherheiten werden dokumentiert und es wird weitergearbeitet.

**Pflichtabschluss jeder Session:** CURRENT_STATE.md + NEXT_ACTION.md + SESSION_LOG.md aktualisieren — als letzter Schritt, bevor die Session endet.

---

## 11. Verhältnis zum Research Program (RC-1)

Dieses Operating Manual regelt die Verarbeitung von Büchern und anderen Primärquellen (Schritte 1–9). Offene Forschungsfragen, die sich nicht allein durch diesen Workflow klären lassen — insbesondere Widersprüche zwischen bereits verarbeiteten Quellen wie SPIN Selling und The Challenger Sale — werden stattdessen im Research Program (`06_research_program/`, siehe dortige `RESEARCH_GOVERNANCE.md` und `RESEARCH_LIFECYCLE.md`) bearbeitet. Ergebnisse aus dem Research Program erreichen `03_knowledge_base/` erst nach einer positiven Editor Decision und Repository Integration (`06_research_program/REPOSITORY_INTEGRATION.md`) — ab diesem Zeitpunkt gelten für sie exakt dieselben Regeln dieses Operating Manual und des Canonical Knowledge Model wie für jedes Buchanalyse-Ergebnis. Das Research Program ist kein Ersatz und keine Abkürzung für diesen Standardprozess.

---

*Dieses Dokument gilt ab v1.0. Änderungen nur durch Felix. Zuletzt aktualisiert: v1.1 (2026-06-30); RC-1 (2026-07-03) — Abschnitt 11 (Verhältnis zum Research Program) ergänzt.*
