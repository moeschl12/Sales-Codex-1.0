# Editor Release Decision — Version 1.1

Stufe: Reserved Decision gemäß `00_project/V1_1_AUTONOMY_AND_AUDIT_POLICY.md` (§4.2) und `00_project/projects/V11-08_final_audit_release/PROJECT_BRIEF.md` (DoD 5). Ausschließlich Felix vorbehalten; von keiner Session dieses Programms vorweggenommen oder simuliert.

**Ablageort-Hinweis:** Diese Datei wurde im V11-08-Projektordner abgelegt (nicht an einer alternativen Stelle), da V11-08 (`Final Program Audit & Version 1.1 Release Decision`) explizit das Makroprojekt ist, dessen Definition of Done Punkt 5 genau dieses Dokument verlangt. Die Wahl wurde gemäß Hard-Stop-Vorgabe im Arbeitsauftrag getroffen, ohne Rückfrage.

---

## Projekt-/Programm-ID

Sales Codex Version 1.1 (Makroprojekt-Programm `00_project/ROADMAP_V1_1.md`, V11-01 bis V11-08)

---

## Bezug zum Entscheidungspaket

`00_project/projects/V11-08_final_audit_release/RELEASE_DECISION_PACKAGE.md` (Executor-Zusammenfassung), `RELEASE_CRITERIA_VERIFICATION.md` (Kriterien-Prüfung), `COMPLETION_REPORT.md` (Executor-DoD-Status), unabhängiger Final Audit + Re-Check (Codex, 2026-07-13, PASS mit anschließend vollständig geschlossenen Findings — dokumentiert in `00_project/SESSION_LOG.md`).

---

## Entscheidung

**Option:** RELEASED — SCOPE-LIMITED

**Wortlaut der Entscheidung (Herausgeberauftrag „Sales Codex — V1.1 Release Closure nach Editor Decision", Felix, 2026-07-13):**

„Version 1.1 wird freigegeben als: RELEASED — SCOPE-LIMITED. V1.1 ist als evidenz-, governance- und auditkonsolidierter Repository-Stand freigegeben. Die Freigabe umfasst NICHT breite Delivery-Skalierung. Delivery-Scaling bleibt begrenzt und gesondert entscheidungsbedürftig. Offene Punkte wie OD-009 bis OD-012, Delivery-Scaling-Blocker, additives Synthesemuster, OQ-2/Scientific Debt und mögliche V11-09 ff. werden nicht im Release stillschweigend gelöst."

**Voraussetzung erfüllt:** V11-08 Final Audit (Codex) — PASS; Re-Check nach Nacharbeit — PASS. Beide zugehörigen Findings (1 Major: stale Roadmap-Zeile; 1 Minor: Working-Tree-Zählung) sind vor dieser Entscheidung vollständig geschlossen worden (siehe `00_project/SESSION_LOG.md`, Einträge „V11-08 Nacharbeit nach Codex Final-Audit" und „DECISION_STACK_2026-07-13.md Nacharbeit nach Codex Re-Check", beide 2026-07-13).

---

## Verbindliche Einzelfestlegungen

1. **Was freigegeben wird:** der evidenz-, governance- und auditkonsolidierte Repository-Stand von V1.1 — d. h. die Ergebnisse von V11-01 bis V11-08 in der Form, wie sie durch die jeweiligen Completion-/Audit-/Closure-Reports und den finalen Release-Kriterien-Check dokumentiert sind.
2. **Was NICHT freigegeben wird:** breite Delivery-Skalierung. Der V11-04-Befund „begrenzt, keine breite Skalierung" bleibt in Kraft und wird durch dieses Release nicht überschrieben oder stillschweigend aufgewertet.
3. **Was durch dieses Release NICHT entschieden wird:** OD-009 bis OD-012 (weiterhin klassifiziert offen, Reserved Decisions), die vier V11-04-Delivery-Scaling-Blocker, das additive Synthesemuster (R-1, Methoden-Review-Kandidat), OQ-2 und die zugehörigen Einträge in `SCIENTIFIC_DEBT.md`, sowie mögliche zukünftige Makroprojekte V11-09 ff. Alle diese Punkte bleiben in ihrem bisherigen, dokumentierten Status offen und werden separat entschieden.
4. **Working Tree / Git:** Der Working Tree ist zum Zeitpunkt dieser Entscheidung weiterhin nicht clean (siehe `RELEASE_CRITERIA_VERIFICATION.md` Abschnitt 9 — Zeitpunkt-Snapshot, keine fixe Zahl). Commit und Push sind und bleiben ausschließlich Felix' Aufgabe; keine Session dieses Programms committet oder pusht. Das Release gilt als inhaltlich erteilt, unabhängig vom Zeitpunkt des tatsächlichen Commits.
5. **Kein neues Wissensobjekt, kein neues Projekt:** Diese Entscheidung selbst verändert keine Wissensobjekte, aktiviert kein neues Forschungsprojekt und legt kein V11-09 an.

---

## Stellungnahme zu den zentralen Einschränkungen

- **Delivery-Scaling-Status („begrenzt"):** wurde in `RELEASE_CRITERIA_VERIFICATION.md` §5 als inhaltliche Einschränkung (nicht als Kriteriums-Fail) markiert und in `RELEASE_DECISION_PACKAGE.md` §4 explizit an die Entscheidung weitergereicht. Die Editor-Entscheidung bestätigt diese Einschränkung ausdrücklich als fortbestehend — RELEASED — SCOPE-LIMITED ist die direkte Konsequenz daraus, kein neuer Befund.
- **Working-Tree-Zustand:** klassifiziert (Owner Felix), kein inhaltlicher Defekt, keine Blockade der Editor-Entscheidung selbst — bereits in `COMPLETION_REPORT.md` und `RELEASE_CRITERIA_VERIFICATION.md` so disponiert.
- **Offene Reserved Decisions (OD-009–012) und Scientific-Debt-Punkte:** ausdrücklich nicht Gegenstand dieser Entscheidung; bleiben unverändert im Status „klassifiziert, entscheidungsreif" bzw. „registriert" stehen.

---

## Geplante Integration in die Control Plane

| Dokument | Aktion |
|---|---|
| `00_project/ROADMAP_V1_1.md` | Programmstatus auf V1.1 RELEASED — SCOPE-LIMITED aktualisiert |
| `00_project/NEXT_ACTION.md` | Launcher auf Post-Release-Zustand aktualisiert, kein automatischer nächster Makroprojekt-Start |
| `CURRENT_STATE.md` | Opening Note aktualisiert |
| `SESSION_BRIEF.md` | Vollständig ersetzt (eigene Policy) |
| `00_project/SESSION_LOG.md` | Abschlusseintrag ergänzt |
| `00_project/DECISION_STACK_2026-07-13.md` | Abschließender Update-Vermerk ergänzt |

Keine Wissensobjekte, keine `05_publications/`- oder `06_research_program/`-Inhalte betroffen.

---

## Bei künftiger Erweiterung des Scopes (Delivery-Skalierung, V11-09 ff.)

Nicht zutreffend für diese Entscheidung selbst — festgehalten als Hinweis: jede Ausweitung auf breite Delivery-Skalierung oder die Eröffnung neuer Makroprojekte (V11-09 ff.) erfordert eine eigene, gesonderte Editor-Entscheidung mit eigenem Brief bzw. eigener Roadmap-Eintragung. Diese Datei ersetzt eine solche zukünftige Entscheidung nicht.

---

## Datum und Unterschrift

Entschieden von: Felix (Herausgeber)
Datum: 2026-07-13
Dokumentiert von: Claude (Cowork-Session), Executor-Rolle — reine Protokollierung der Herausgeberentscheidung, keine inhaltliche Mitentscheidung.

---

## Status

**V1.1 — RELEASED — SCOPE-LIMITED, entschieden von Felix am 2026-07-13.** Working Tree bleibt bis zum Editor-Commit uncommittet. Delivery-Scaling nicht freigegeben. Alle in Abschnitt „Verbindliche Einzelfestlegungen" Punkt 3 genannten offenen Punkte bleiben unverändert offen.
