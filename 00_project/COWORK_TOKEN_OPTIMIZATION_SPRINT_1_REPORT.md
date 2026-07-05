# Cowork Token Optimization Sprint 1 — Abschlussbericht

**Dokumentklasse:** Operational (Sprint-Abschlussbericht)
**Rolle bei Erstellung:** Repository Curator / Performance Editor — ausdrücklich nicht als Autor, Research Assistant, Framework-Architekt oder Wissensarbeiter
**Sprint:** Cowork Token Optimization Sprint 1
**Datum:** 2026-07-05
**Grundlage:** `00_project/COWORK_PERFORMANCE_AUDIT_2026-07-05.md`
**Scope:** Ausschließlich die fünf im Sprintauftrag benannten, risikoarmen Maßnahmen. Keine Änderungen an `03_knowledge_base/`, `02_sources/`, `04_book_analysis/`, Wissensobjekten, Evidenz-Leveln, Canonical Knowledge Model, Templates, Methodik oder Framework-Logik. Keine neuen Wissensobjekte, keine neue Forschung, keine inhaltlichen Bewertungen, keine rückwirkende Änderung von Version-1.0-Inhalten (nur Ablageort geändert, kein Wortlaut).

---

## 1. Executive Summary

Alle fünf Maßnahmen aus dem Sprintauftrag wurden umgesetzt: `NEXT_ACTION.md` wurde von 25.280 Byte (≈ 6.300 Token, 13 gestapelte „Vorheriger Sprint"-Blöcke plus ein stiller, veralteter Fragment-Rest aus der Academic-Recovery-Phase) auf eine einzige aktuelle Aktion mit Arbeitsmodus, erlaubten/verbotenen Dateien und Abbruchbedingungen zurückgeschnitten (46 Zeilen). Die „Operational"-Klasse in `PROJECT_BOOTSTRAP.md` wurde in „jede Session" (2 Dateien) und „aufgabenabhängig" (5 Dateien) aufgeteilt, ergänzt um ein explizites Verbot rekursiver Scans. 16 eindeutig abgeschlossene Version-1.0-Sprint-, Audit-, Freeze-, Release- und Programmberichte (zusammen ≈ 331 KB) wurden nach `99_archive/v1.0_release/` verschoben, mit Alt-/Neu-Pfad-Index. `CLAUDE_BOOTSTRAP.md` wurde nach `99_archive/` verschoben (war bereits von `PROJECT_BOOTSTRAP.md` selbst als „Archived" klassifiziert, verwies aber noch auf die längst abgeschlossene SPIN-Selling-Pilotaufgabe). Zusätzlich wurde `SESSION_BRIEF.md` (28 Zeilen) als kompakter Ersatz für den vollständigen `CURRENT_STATE.md`-Lesevorgang im Regelfall angelegt.

Kein Wissensobjekt, keine Quelle, keine Buchanalyse, kein Framework-Dokument und kein Template wurde verändert. Alle verschobenen Dateien sind byteidentisch am neuen Ort erhalten.

---

## 2. Geänderte Dateien

| Datei | Änderung |
|---|---|
| `00_project/NEXT_ACTION.md` | Vollständig neu geschrieben: genau eine aktuelle Aktion, Arbeitsmodus, erlaubte Dateien, verbotene Dateien, Abbruchbedingungen, Pflichtabschluss-Regel (jetzt mit „ersetzen, nicht anhängen"). Alte, gestapelte Sprint-Historie entfernt. |
| `PROJECT_BOOTSTRAP.md` | Dokumentklassifizierung (Abschnitt „Operational") in zwei Unterklassen aufgeteilt, explizites Scan-Verbot ergänzt, Pflichtlektüre-Liste um `SESSION_BRIEF.md`/Statusblock-Hinweis ergänzt, Datumszeile aktualisiert. |
| `SESSION_BRIEF.md` (neu) | 28 Zeilen: aktueller Status, aktuelle Arbeitsregel, aktuelle nächste Aktion, Standard-Laderegel, Verweis auf `PROJECT_BOOTSTRAP.md`. Keine Historie. |
| `99_archive/v1.0_release/INDEX.md` (neu) | Alt-Pfad-→-Neu-Pfad-Tabelle für alle 16 verschobenen Dateien, Auswahlkriterium dokumentiert. |

---

## 3. Verschobene Dateien

**Nach `99_archive/v1.0_release/` (16 Dateien, ≈ 331 KB):**
`EXTERNAL_AUDIT_RESOLUTION_REPORT.md`, `FINAL_EDITOR_ASSESSMENT_V1_0.md`, `FINAL_PRE_RELEASE_REPORT.md`, `FINAL_RC1_AUDIT_VALIDATION_REPORT.md`, `RC1_FREEZE_DECLARATION.md`, `RC1_FREEZE_REPORT.md`, `RELEASE_CANDIDATE_RC1.md`, `RELEASE_NOTES_v1.0_RC1.md`, `REPOSITORY_CLOSING_STATUS.md`, `REPOSITORY_CONSOLIDATION_IMPLEMENTATION_REPORT_RC1.md`, `REPOSITORY_CONSOLIDATION_REPORT_RC1.md`, `REPOSITORY_MANIFEST_RC1.md`, `SALES_CODEX_1_0_PROGRAM.md`, `SALES_CODEX_1_0_RELEASE_PLAN.md`, `SALES_CODEX_VERSION_1_0_RELEASE.md`, `VERSION_1_0_CLOSING_REPORT.md`.

Auswahlkriterium: Datei deklariert sich selbst (Kopfzeile „Dokumentklasse") eindeutig als abgeschlossener Sprint-/Audit-/Freeze-/Releasebericht der Version-1.0-Schließung, **oder** ein Nachfolgedokument erklärt sie explizit für historisch (`SALES_CODEX_1_0_PROGRAM.md`, laut `SALES_CODEX_1_0_RELEASE_PLAN.md` „bleibt unverändert... als historische Planungsgrundlage erhalten"; `SALES_CODEX_1_0_RELEASE_PLAN.md` selbst, dessen eigene Gültigkeitsklausel „Pflichtlektüre bis Version 1.0 erreicht ist" durch die Veröffentlichung erfüllt ist).

**Nach `99_archive/` (1 Datei):**
`CLAUDE_BOOTSTRAP.md` — bereits in `PROJECT_BOOTSTRAP.md` v1.1 als „Archived" klassifiziert; verwies zudem noch auf die abgeschlossene SPIN-Selling-Pilotaufgabe als „Erste Aufgabe".

---

## 4. Nicht verschobene Grenzfälle

Folgende Dateien wurden geprüft (Kopfzeile gelesen), aber **nicht** verschoben, weil sie nicht eindeutig in die Kategorie „abgeschlossener Version-1.0-Sprint-/Audit-/Freeze-/Releasebericht" fallen:

| Datei | Grund für „nicht entschieden" |
|---|---|
| `CODEX_AUDIT_2026-07.md` | Genereller Repository-Audit vom 2026-07-01, nicht V1.0-gebrandet; wird von `CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md` als Grundlage referenziert (Meilenstein-Kette) |
| `CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md` | Direkte Fortsetzung von `CODEX_AUDIT_2026-07.md`, gleiche Unsicherheit |
| `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` | Wissenschaftlicher Reifegradbericht vom 2026-07-01, nicht V1.0-gebrandet, möglicherweise Vorstufe eines der drei „externen Gutachten" |
| `WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md` | Enthält `[cite: ...]`-Markup, wirkt wie roher externer Input (Primärquelle des Audits), nicht wie ein von Cowork verfasster Bericht — Verschiebung könnte Audit-Trail-Wert mindern |

Zusätzlich beobachtet, aber außerhalb des Sprintauftrags (nicht geprüft/entschieden, nur zur Kenntnis): `review_queue.md` ist in der alten `PROJECT_BOOTSTRAP.md`-Tabelle (v1.1) bereits als „Archived"-Beispiel genannt, liegt aber weiterhin aktiv in `00_project/`. Da weder im Sprintauftrag noch in der Nicht-verschieben-Liste namentlich behandelt, wurde die Datei nicht angefasst — Empfehlung: separate Prüfung durch Felix.

**Explizit nicht verschoben, weil klar außerhalb der Kategorie** (Governance-/Draft-/Reference-Dokumente, keine V1.0-Abschlussberichte): `ACADEMIC_RECOVERY_PLAN.md`, `ACADEMIC_RECOVERY_REPORT.md`, `ACADEMIC_RECOVERY_REPORT_PACK_2_4.md` (Scientific-Debt-Arbeit, an `SCIENTIFIC_DEBT.md` gekoppelt), `BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md` und `OPEN_DECISION_RESOLUTION_REPORT_2026-07.md` (bindende Editor-/Governance-Entscheidungen, weiterhin zitiert), `POST_MORTEM_B0002.md` und `POST_MORTEM_INFLUENCE_PLAN.md` (Status „Entwurf"/buchspezifisch, nicht V1.0), `RELEASE_NOTES_v1.1.md` (explizit „Entwurf — wartet auf Herausgeber-Freigabe", also nicht abgeschlossen), `SALES_CODEX_CONTEXT.md` und `SALES_CODEX_OPERATING_MANUAL.md` (aktive Referenzdokumente), `SPRINT_2_ABSCHLUSSBERICHT.md` und `VALIDIERUNGSSPRINT_MEC0010-0012.md` (Buchanalyse-/Validierungssprints vor dem V1.0-Programm), `PROCESS_PATTERN_ANALYSIS_2026-07.md` (offener Vorschlag, noch nicht durch Felix geprüft), `changelog.md` und `review_queue.md` (laufende, nicht abgeschlossene Dokumente).

Explizit geschützt laut Sprintauftrag, nicht angefasst: `NEXT_ACTION.md` (bearbeitet, nicht verschoben), `SESSION_LOG.md`, `OPEN_DECISIONS.md`, `SCIENTIFIC_DEBT.md`, `task_rules.md`, `REPOSITORY_KPIS.md`, `backlog.md`, `COWORK_EXECUTION_PROTOCOL.md`.

---

## 5. Erwartete Tokenersparnis

Grobe Schätzung, ≈ 4 Zeichen/Token:

- **`NEXT_ACTION.md`:** 25.280 → ≈ 4.000–4.500 Byte (≈ 6.300 → ≈ 1.000–1.100 Token). Ersparnis ≈ 5.200–5.300 Token pro Session, in der die Datei gelesen wird.
- **„Operational"-Pflichtlektüre laut `PROJECT_BOOTSTRAP.md`:** Die bisherige wörtliche Lesart (8 Dateien, ≈ 71.000 Token „in jeder Session") entfällt. Realistische Pflichtlektüre jetzt: `SESSION_BRIEF.md` (≈ 400 Token) oder `CURRENT_STATE.md`-Statusblock (≈ 300–400 Token) + `NEXT_ACTION.md` (≈ 1.000 Token) ≈ 1.400–1.700 Token. Ersparnis ≈ 69.000–70.000 Token pro Session, **sofern** künftige Sessions die präzisierte Klassifizierung tatsächlich befolgen (kein automatischer Mechanismus, siehe Abschnitt 6).
- **Archivierung (16 Dateien, ≈ 331 KB ≈ 83.000 Token):** Kein Effekt auf normale, gezielte Sessions (diese Dateien wurden ohnehin nur bei explizitem Verweis gelesen). Effekt ausschließlich bei Aufgaben, die `00_project/` als Ganzes durchsuchen oder auflisten — dort entfällt dieser Anteil vollständig aus dem Suchraum.
- **`PROJECT_BOOTSTRAP.md` selbst:** leicht gewachsen (ca. +250 Token durch die präzisierte Tabelle) — beabsichtigt, da dies die viel größere „Operational"-Ersparnis oben erst ermöglicht.
- **`SESSION_BRIEF.md`:** neu, ≈ 400 Token, ersetzt im Regelfall die vollständige `CURRENT_STATE.md` (467 Zeilen, ≈ 12.800 Token) — Ersparnis ≈ 12.400 Token pro Session, sofern genutzt.

Größenordnung insgesamt, bei diszipliniert befolgter neuer Klassifizierung: ≈ 75.000–85.000 Token weniger Pflicht-Kontext pro durchschnittlicher Session gegenüber dem wörtlichen Vorzustand.

---

## 6. Verbliebene Risiken

- **Kein technischer Durchsetzungsmechanismus.** Die neue Klassifizierung in `PROJECT_BOOTSTRAP.md` ist eine Konvention, kein erzwungenes Verhalten. Eine Session, die die Datei nicht liest oder ignoriert, kann weiterhin alle acht ehemals „Operational" markierten Dateien laden.
- **Dangling-Pfad-Zitate in eingefrorenen Version-1.0-Dokumenten.** `CURRENT_STATE.md` und mehrere Einträge in `SESSION_LOG.md`/`changelog.md` zitieren die 16 verschobenen Dateien weiterhin mit dem alten Pfad `00_project/<Datei>.md`. Diese Zitate wurden bewusst nicht rückwirkend geändert (Version-1.0-Inhalte gelten als eingefroren) — `99_archive/v1.0_release/INDEX.md` löst die Zuordnung auf, ersetzt aber keine automatische Link-Korrektur.
- **Vier Grenzfälle unentschieden** (Abschnitt 4) — verbleiben vorerst in `00_project/`, tragen weiterhin zur Ordnergröße bei (~157 KB zusammen).
- **`review_queue.md`** trägt laut alter `PROJECT_BOOTSTRAP.md`-Klassifizierung bereits das Label „Archived", wurde aber nicht verschoben, da außerhalb des expliziten Sprintauftrags — Inkonsistenz bleibt bestehen, bis separat entschieden.
- **Beobachtung zur Arbeitsumgebung (kein Repository-Risiko):** Bei der Verifikation dieses Sprints zeigte die Shell-Sandbox für soeben überschriebene Dateien (`NEXT_ACTION.md`, `PROJECT_BOOTSTRAP.md`) zwischenzeitlich veraltete Byte-Größen (identisch mit dem Vorzustand), obwohl der tatsächliche Dateiinhalt bereits korrekt aktualisiert war (verifiziert über direktes Lesen der Datei). Reine Cache-Verzögerung der Mount-Ansicht, keine Datenintegritätsfrage — für exakte Größenprüfung künftig direktes Lesen statt Shell-`wc`/`du` auf gerade bearbeiteten Dateien verwenden.

---

## 7. Nächster empfohlener Schritt

Entscheidung durch Felix zu den vier Grenzfällen aus Abschnitt 4 (insbesondere `WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md` und `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` — vermutlich externe Primärquellen mit Audit-Trail-Wert, nicht ohne Rücksprache zu verschieben) sowie zu `review_queue.md`. Danach, falls gewünscht: ein Folgesprint, der die in `COWORK_PERFORMANCE_AUDIT_2026-07-05.md` Abschnitt 11 als „langfristig" eingestuften Maßnahmen angeht (z. B. aktive Einbindung von `08_knowledge_atlas` in Konsistenzprüfungs-Prompts) — außerhalb des Scopes dieses Sprints.
