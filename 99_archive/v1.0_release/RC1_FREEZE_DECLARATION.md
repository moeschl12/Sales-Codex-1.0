# RC-1 Freeze Declaration — Sales Codex Version 1.0

**Dokumentklasse:** Release (Configuration Management)
**Rolle bei Erstellung:** Release Manager / Configuration Manager
**Datum:** 2026-07-04

---

## 1. Formale Erklärung

Hiermit wird erklärt:

**Sales Codex Version 1.0 RC-1 gilt ab dem 2026-07-04 als eingefrorener Release Candidate.**

Diese Erklärung stützt sich auf den in `RELEASE_CANDIDATE_RC1.md` dokumentierten Repository-Zustand: 15 vollständig verarbeitete Bücher, 514 Wissensobjekte, 15 Quellobjekte, ein vollständig ausgearbeitetes und praktisch validiertes Research Program, ein abgeschlossenes Forschungsprojekt (W-001) mit vollständigem neunstufigem Lifecycle, sowie die abgeschlossene Bearbeitung eines externen Release-Audits (External Audit Resolution Sprint, Ergebnis: READY FOR FINAL RC-1 AUDIT).

Mit dieser Erklärung endet der Entwicklungsmodus für den eingefrorenen Inhaltsbestand. Der Release-Modus beginnt.

**Ausdrücklicher Geltungsvorbehalt:** Diese Erklärung stellt **keine** Veröffentlichung von Version 1.0 dar und **ersetzt nicht** die beiden im Repository selbst bereits definierten nachfolgenden Schritte:

1. **Finaler RC-1-Audit** — definiert in `SALES_CODEX_1_0_RELEASE_PLAN.md`, Kapitel 5 (Critical Path, Schritt 5) als eigenständiger, umfassender Prüfschritt des jetzt eingefrorenen Gesamtzustands. Dieser Audit hat laut `NEXT_ACTION.md` (Stand 2026-07-04) noch nicht stattgefunden ("Herausgeberauftrag ausstehend").
2. **Formale Herausgeber-Freigabe** — gemäß `SALES_CODEX_1_0_RELEASE_PLAN.md`, Kapitel 2.2: "Version 1.0 gilt als veröffentlicht, wenn — und ausschließlich wenn — der Herausgeber (Felix) dies auf Basis eines RC1-Audits formal erklärt." Diese Erklärung ist niemals eine KI-Selbsteinschätzung.

Dieser Freeze dokumentiert den Kandidaten, der dem Finalen RC-1-Audit vorgelegt wird. Er ist der Vorbereitungsschritt für diesen Audit, nicht sein Ersatz.

## 2. Zulässige Änderungen bis Version 1.0

Zwischen diesem Freeze und der formalen Veröffentlichung von Version 1.0 sind ausschließlich folgende Änderungsarten zulässig:

| # | Zulässige Änderung | Bedingung |
|---|---|---|
| 1 | Korrektur von Dokumentationsfehlern, die unmittelbar den Freeze oder seine Verifikation betreffen | Nur Tippfehler, defekte interne Links, offensichtliche Zahlenfehler in den Freeze-Dokumenten selbst — keine inhaltliche Neubewertung |
| 2 | Durchführung des Finalen RC-1-Audits | Wie in `SALES_CODEX_1_0_RELEASE_PLAN.md` Kapitel 5 vorgesehen — read-only gegenüber dem Wissensbestand, es sei denn, der Audit selbst identifiziert einen Freeze-relevanten Fehler |
| 3 | Bearbeitung von im Finalen RC-1-Audit tatsächlich neu identifizierten, bestätigten Blockern | Nur nach Herausgeber-Freigabe, mit demselben Verifikationsstandard wie beim External Audit Resolution Sprint (Auditbehauptung gegen Repository-Realität prüfen, nicht blind übernehmen) |
| 4 | Fortführung der laufenden Session-Pflichtdokumentation | `CURRENT_STATE.md`, `NEXT_ACTION.md`, `SESSION_LOG.md`, `changelog.md` — reine Statusfortschreibung, keine inhaltliche Änderung an eingefrorenen Objekten |
| 5 | Die formale Herausgeber-Freigabe von Version 1.0 selbst | Ausschließlich durch Felix, ausschließlich auf Basis eines erfolgreichen Finalen RC-1-Audits |

## 3. Ausdrücklich NICHT mehr zulässige Änderungen (bis Version 1.0 formal freigegeben ist)

Deckungsgleich mit dem Sprintauftrag dieses Freeze:

- Keine neuen Wissensobjekte (ST, A, MEC, P, T, MOD, Meta-Modelle, Kompetenzen, Beobachtungen)
- Keine neuen Quellen (SRC)
- Keine neuen Buchanalysen (B-0016 ff.)
- Keine neuen Modelle
- Keine neuen Mechanismen
- Keine neuen Statements
- Keine neuen Annahmen
- Keine Frameworkänderungen jeder Art
- Keine Änderungen am Canonical Knowledge Model (`01_framework/05_knowledge_model/canonical_knowledge_model.md`)
- Keine Änderungen am Operating Manual (`00_project/SALES_CODEX_OPERATING_MANUAL.md`)
- Keine Änderungen am Research Program (`06_research_program/README.md`, `RESEARCH_GOVERNANCE.md`, `RESEARCH_LIFECYCLE.md`, `REPOSITORY_INTEGRATION.md`, `DECISION_POLICY.md`, Templates)
- Keine Änderungen am Research Lifecycle
- Keine Änderungen an abgeschlossenen Forschungsprojekten (`06_research_program/completed/W001/`)
- Keine Änderungen an Editor Decisions (weder OD-Auflösungsvermerke noch W-001-Editor-Decision)
- Keine neuen Open Decisions
- Keine neue Forschung
- Keine Literature Reviews
- Keine Architekturänderungen
- Keine Repository-Umstrukturierungen (Ordner, Nummerierung, Top-Level-Struktur)

**Diese Sperre gilt unabhängig davon, wie fachlich sinnvoll eine Änderung erscheinen mag.** Jede als sinnvoll erkannte, aber gesperrte Änderung ist stattdessen zu dokumentieren (z. B. als Vormerkung für den Framework Integration Sprint oder das Version-1.1-Backlog) statt umgesetzt zu werden.

## 4. Umgang mit Version 1.1

Alle Themen, die während dieses Freeze oder in vorangegangenen Sprints als "nicht Teil von 1.0, aber wertvoll" identifiziert wurden, verbleiben im Version-1.1-Backlog gemäß `SALES_CODEX_1_0_RELEASE_PLAN.md`, Kapitel 6, unverändert:

1. OD-006/OD-007 technische Umsetzung (QK-Meme-Filter, CTX-Kontextebene) — separater **Framework Integration Sprint**, ausdrücklich erst nach formaler Veröffentlichung von Version 1.0.
2. AR-003 bis AR-012 (Academic Recovery Tier 2–4).
3. OD-008-Umsetzung (ELM/Trust Formation/Persuasion Knowledge Model als Recherche-/Buchanalyse-Sprint).
4. AR-001/AR-013 volle akademische Vertiefung (Plouffe et al. 2013, Tversky & Shafir 1992).
5. Terminologie-Nachziehung ("Altruistische Bestrafung") und Boundary-Conditions-Ausweitung auf weitere Objekte.
6. Formales, repositoryweites Health-Check-Protokoll (über das projektspezifische Research-Program-Muster hinaus).
7. Neue Buchanalysen (B-0016 ff. aus `book_catalog.md`) — explizit erst nach Version-1.0-Freigabe.
8. `book_catalog.md`/`REPOSITORY_KPIS.md`-Vollsynchronisierung, falls nicht bereits vor 1.0 erledigt.
9. Erreichen der Reifegrad-Note "A-" (kein 1.0-Ziel, langfristiges Qualitätsziel).
10. Fünf verbleibende Open Decisions (OD-008–OD-012), sofern nicht im Rahmen der Herausgeber-Entscheidungsrunde vor der 1.0-Freigabe geklärt.

**Governance-Grundsatz für 1.1:** Jede dieser Änderungen erfordert nach Veröffentlichung von Version 1.0 einen eigenen, explizit beauftragten Sprint mit eigenem Scope — keine implizite Fortsetzung "nebenbei". Dieser Freeze legt keine Reihenfolge für 1.1 fest; das bleibt Sache künftiger Herausgeber-Priorisierung, konsistent mit `SALES_CODEX_1_0_RELEASE_PLAN.md`, das bewusst kein Roadmap-Kapitel führt.

---

*Diese Erklärung ist Teil des Sales Codex Version 1.0 RC-1 Release Candidate Freeze, 2026-07-04. Erstellt in der Rolle Release Manager / Configuration Manager — keine fachliche, wissenschaftliche oder Framework-Autorität beansprucht.*
