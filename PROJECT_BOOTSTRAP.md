# Sales Codex — Project Bootstrap

Dieses Dokument ist der Einstiegspunkt für neue KI-Sessions (Claude, ChatGPT, Gemini, Perplexity o.ä.).

> **Das Repository ist die Quelle der Wahrheit. Der Chat ist eine temporäre Recheninstanz.**  
> Vertraue niemals dem Chatverlauf über den Stand des Projekts. Lies stattdessen `CURRENT_STATE.md` und `00_project/NEXT_ACTION.md`.

---

## Pflichtlektüre beim Session-Start

Minimale Pflichtlektüre (in dieser Reihenfolge):

1. `PROJECT_BOOTSTRAP.md` ← du bist hier
2. `CURRENT_STATE.md` — aktueller Stand, was erledigt ist, was als nächstes kommt
3. `00_project/NEXT_ACTION.md` — exakt eine nächste Aktion
4. Nur die direkt betroffenen Arbeitsdateien (nicht das gesamte Repository)

Nicht unnötig das gesamte Repository lesen. Nur laden, was der aktuelle Job erfordert.

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

## Dokumentklassifizierung (v1.1)

Alle Dokumente im Repository haben eine Klasse. Die Klasse bestimmt, wann eine KI-Session das Dokument lesen muss.

| Klasse | Bedeutung | Beispiele |
|---|---|---|
| **Operational** | Aktiv genutzt — KI liest diese in jeder Session | `backlog.md`, `CURRENT_STATE.md`, `NEXT_ACTION.md`, `SESSION_LOG.md`, `OPEN_DECISIONS.md`, `task_rules.md`, `SCIENTIFIC_DEBT.md`, `REPOSITORY_KPIS.md` |
| **Reference** | Bei Bedarf nachschlagen — nur wenn relevant | Operating Manual, Execution Protocol, alle Templates, agent_protocols/, codex_methodology.md, canonical_knowledge_model.md, evidence_system.md |
| **Archived** | Historisch, nicht mehr aktiv — nicht löschen | `CLAUDE_BOOTSTRAP.md`, `roadmap.md`, `review_queue.md` |

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

*Zuletzt aktualisiert: 2026-06-30*
