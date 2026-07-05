# Sales Codex — Project Bootstrap

Dieses Dokument ist der Einstiegspunkt für neue KI-Sessions (Claude, ChatGPT, Gemini, Perplexity o.ä.).

> **Das Repository ist die Quelle der Wahrheit. Der Chat ist eine temporäre Recheninstanz.**  
> Vertraue niemals dem Chatverlauf über den Stand des Projekts. Lies stattdessen `CURRENT_STATE.md` und `00_project/NEXT_ACTION.md`.

---

## Pflichtlektüre beim Session-Start

Minimale Pflichtlektüre (in dieser Reihenfolge):

1. `PROJECT_BOOTSTRAP.md` ← du bist hier
2. `SESSION_BRIEF.md`, falls vorhanden — sonst nur der Statusblock am Anfang von `CURRENT_STATE.md`, nicht die vollständige Sprint-Historie darunter
3. `00_project/NEXT_ACTION.md` — exakt eine nächste Aktion
4. Nur die direkt betroffenen Arbeitsdateien (nicht das gesamte Repository)

Nicht unnötig das gesamte Repository lesen. Nur laden, was der aktuelle Job erfordert. Kein rekursiver Scan über `00_project/` oder `03_knowledge_base/` ohne explizite Freigabe im Auftrag (siehe Dokumentklassifizierung unten).

---

## Projektziel

Der **Sales Codex** ist ein evidenzbasiertes Wissenssystem über Vertrieb, Verkauf, Verhandlung, Kommunikation und Käuferpsychologie.

Ziel: Ein strukturiertes, zitierfähiges, widerspruchsbewusstes Referenzsystem aufbauen — kein Selbsthilfebuch, sondern eine Wissensbasis mit Quellenbelegen, Mechanismen, Prinzipien, Techniken und Modellen.

---

## Rollenmodell

Der Herausgeber (Felix) gibt Freigaben und trifft Framework-Entscheidungen.  
KI-Systeme sind Redakteure: Sie lesen, extrahieren, strukturieren, canonicalisieren — aber erfinden keine Fakten und treffen keine Herausgeberentscheidungen.

Grundregel: **Keine eigene Erinnerung als Autorität. Keine erfundenen Quellen. Keine geglätteten Widersprüche.**

---

## Sales Codex OS — Wissenspipeline

Die Reihenfolge der Wissensverarbeitung ist verbindlich:

```
Primärquelle (PDF/Buch)
  → SRC (Quellobjekt anlegen)
  → ST (Statements direkt aus Primärquelle extrahieren)
  → A (Annahmen aus ST-Clustern, n:m-Beziehung)
  → MEC (Mechanismen ableiten, Canonicalisierung gegen bestehende MECs)
  → P (Prinzipien formulieren, je aus ≥2 MECs oder Annahmen)
  → T (Techniken erfassen, je aus ≥1 Prinzip)
  → MOD (Modelle aktualisieren oder neu anlegen)
  → VAL (Selbstreview / Konsistenzprüfung)
  → Abschlussbericht / BOOK_REVIEW_REPORT
```

**Grundsätze:**
- ST-Objekte: Nur aus Primärtext — kein Trainingswissen als Quellinformation
- A-Objekte: n:m-Beziehung zu STs (nicht 1:1)
- MEC-Objekte: Neues MEC nur wenn kein bestehendes MEC denselben psychologischen Prozess erklärt
- P-Objekte: Niemals Reformulierung eines einzelnen Mechanismus — muss aus ≥2 Quellen abstrahieren
- T-Objekte: Konkrete Handlungsanweisungen, je mindestens einem Prinzip zugeordnet

---

## Canonicalisierung

Vor jedem neuen Wissenselement prüfen: Gibt es bereits ein Objekt, das denselben Sachverhalt abdeckt?

Entscheidungslogik:
- Identische Kausalstruktur + identischer Kontext → **zusammenführen (merge)**
- Identische Kausalstruktur + unterschiedlicher Kontext → **bestehend erweitern + Canonicalisierungsentscheidung dokumentieren**
- Grundlegend andere Kausalstruktur → **neues Objekt anlegen**

Canonicalisierungsentscheidung immer explizit im Objekt dokumentieren.

---

## Rule of Three

Ein Mechanismus qualifiziert sich als eigenständiges MEC-Objekt erst, wenn er in ≥2 unabhängigen Kontexten als Erklärungskraft auftritt.  
(Hinweis: Gilt analog für andere Objekttypen, wenn nicht anderweitig spezifiziert.)

---

## Arbeitsprinzipien

1. Das Repository ist das Gedächtnis. Ergebnisse immer in Dateien speichern.
2. Chat ist temporär. Kein Verlass auf Chatverlauf über Sitzungsgrenzen hinaus.
3. Unsicherheit dokumentieren, nicht glätten. Widersprüche festhalten.
4. Keine Framework-Änderungen ohne Freigabe durch Felix.
5. Keine Primärquellen aus Gedächtnis — immer aus dem PDF/Buch.
6. Am Ende jedes Jobs aktualisieren: `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`.

---

## Abbruchbedingungen (wann anhalten)

Nur anhalten wenn:
- Primärquelle fehlt oder nicht zugänglich
- Repository-Dateien beschädigt
- Canonicalisierungsentscheidung eindeutig nicht möglich
- Framework-Widerspruch blockiert produktives Weiterarbeiten
- Herausgeberentscheidung zwingend erforderlich

**Nicht anhalten bei normaler Unsicherheit.** Unsicherheit dokumentieren, Abbruchbedingung prüfen, weiterarbeiten.

---

## Kommunikation im Chat

Kompakte Antworten:
- Was wurde erledigt
- Welche Dateien geändert
- Was ist der nächste Schritt

Keine langen Zwischenberichte. Ergebnisse gehören in Dateien, nicht in den Chat.

---

## Dokumentklassifizierung (v1.2 — präzisiert 2026-07-05, Cowork Token Optimization Sprint 1)

Alle Dokumente im Repository haben eine Klasse. Die Klasse bestimmt, wann eine KI-Session das Dokument lesen muss. Die vorherige v1.1-Fassung dieser Tabelle deklarierte acht Dateien als „liest KI in jeder Session" unabhängig vom Aufgabentyp (≈ 71.000 Token) — das widersprach der obigen Regel „nicht unnötig das gesamte Repository lesen". Diese Fassung löst den Widerspruch auf, indem „Operational" in zwei Unterklassen aufgeteilt wird.

| Klasse | Bedeutung | Dateien |
|---|---|---|
| **Operational — jede Session** | Tatsächlich sessionsunabhängig nötig | `CURRENT_STATE.md` (nur der Statusblock am Dateianfang, nicht die vollständige Sprint-Historie darunter), `00_project/NEXT_ACTION.md`, `SESSION_BRIEF.md` (kompakter Ersatz für den Statusblock, falls vorhanden) |
| **Operational — aufgabenabhängig** | Nur laden, wenn der konkrete Aufgabentyp zutrifft | `00_project/backlog.md` (Task-Auswahl), `00_project/task_rules.md` (Buchanalyse-Start), `00_project/OPEN_DECISIONS.md` (Entscheidungs-/Governance-Arbeit), `00_project/SCIENTIFIC_DEBT.md` (Evidenz-/Qualitätsarbeit), `00_project/REPOSITORY_KPIS.md` (Reporting/Release) |
| **Reference** | Bei Bedarf nachschlagen — nur wenn fachlich relevant | Operating Manual, Execution Protocol, alle Templates, agent_protocols/, codex_methodology.md, canonical_knowledge_model.md, evidence_system.md |
| **Reference — nur bei Historienfrage** | Nur bei expliziter Nachfrage nach vergangenen Sessions, nicht routinemäßig | `00_project/SESSION_LOG.md`, `00_project/changelog.md` |
| **Archived** | Historisch, nicht mehr aktiv — nicht löschen, nicht standardmäßig laden | `99_archive/` (inkl. `CLAUDE_BOOTSTRAP.md`, `99_archive/v1.0_release/`), einmalige Sprint-/Freeze-/Audit-/Release-Berichte nach Abschluss des jeweiligen Sprints |

**Suchgrenze (verbindlich):** Kein rekursiver Scan (Volltextsuche, `find`, Mehrfach-Dateizugriff über einen ganzen Ordner) über `00_project/` oder `03_knowledge_base/` ohne explizite Freigabe im Auftrag für genau diesen einen Scan. Bei Unsicherheit über den Umfang: Rückfrage statt Breitscan.

## Task-Type-Routing

`TASK_TYPES.md` ist die Reference-Datei für aufgabenbezogenes Routing (12 Task-Typen, je mit fester Dateiladestrategie, Suchgrenze, Ausgabeformat und Arbeitsmodus). Nennt ein Auftrag ein `TASK_TYPE`-Feld, gilt direkt die dortige Routing-Definition — kein weiteres Abwägen nötig. Nennt ein Auftrag keinen Task-Typ, leitet Claude den wahrscheinlichsten Typ aus der Aufgabe ab und benennt ihn kurz im Chat; bei echter Mehrdeutigkeit wird stattdessen rückgefragt. Kein Task-Typ hebt die in diesem Dokument definierten Such- und Änderungsgrenzen automatisch auf — `TASK_TYPES.md` ergänzt `PROJECT_BOOTSTRAP.md`, ersetzt es nicht.

---

## Relevante Framework-Dateien

| Datei | Inhalt |
|---|---|
| `01_framework/01_project_charter/` | Projektziel, Qualitätsstandards |
| `01_framework/02_methodology/` | Wissenspipeline, Canonical Knowledge Model |
| `01_framework/03_evidence_system/` | Evidenzklassen E1–E5 |
| `01_framework/04_source_standards/` | Quellenstandards |
| `01_framework/05_extraction_standards/` | Extraktionsstandards |
| `01_framework/06_knowledge_model/` | Wissensmodell |
| `01_framework/07_agent_protocols/` | Agenten-Protokolle |
| `01_framework/08_templates/` | Templates für alle Objekttypen |
| `00_project/task_rules.md` | Verbindliche Task-Regeln |
| `00_project/backlog.md` | Aufgabenliste |
| `00_project/OPEN_DECISIONS.md` | Offene Entscheidungen |

---

*Zuletzt aktualisiert: 2026-07-05 (Task-Type-Routing ergänzt, Decision Architecture Sprint 2 — siehe `00_project/DECISION_ARCHITECTURE_SPRINT_2_REPORT.md`; Dokumentklassifizierung präzisiert, Cowork Token Optimization Sprint 1 — siehe `00_project/COWORK_TOKEN_OPTIMIZATION_SPRINT_1_REPORT.md`)*
