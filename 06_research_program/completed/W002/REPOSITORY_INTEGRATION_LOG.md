# Repository Integration Log

Projekt-ID: W-002
Stufe: 8 (`RESEARCH_LIFECYCLE.md`, Abschnitt 10; Ablauf: `REPOSITORY_INTEGRATION.md`)
Stand: 2026-07-05
Bearbeitet im Rahmen: Editor Decision W-002 (2026-07-05, Teilweise annehmen)
Grundlage: `06_EDITOR_DECISION.md`, Tabelle „Geplante Integration"

---

## 1. Zweck

Dieses Dokument protokolliert jede tatsächlich durchgeführte Integrationsaktion aus der Editor-Decision-Tabelle „Geplante Integration" — ID, Objekttyp, Aktion, Dateipfad, Bezug zur Editor-Decision-Zeile (`REPOSITORY_INTEGRATION.md`, Abschnitt 5).

## 2. Durchgeführte Aktionen

| # | Objekt-ID | Objekttyp | Aktion | Dateipfad | Bezug zur Editor-Decision-Zeile |
|---|---|---|---|---|---|
| 1 | MEC-0012 | Mechanismus (MEC) | ERWEITERT | `03_knowledge_base/mechanisms/MEC-0012_dual_process_system1_zu_system2.md` | Zeile 1 |
| 2 | MEC-0005 | Mechanismus (MEC) | ERWEITERT | `03_knowledge_base/mechanisms/MEC-0005_reciprocation_obligation.md` | Zeile 2 |
| 3 | MEC-0006 | Mechanismus (MEC) | ERWEITERT | `03_knowledge_base/mechanisms/MEC-0006_social_proof_correctness_signal.md` | Zeile 3 |
| 4 | MEC-0007 | Mechanismus (MEC) | ERWEITERT | `03_knowledge_base/mechanisms/MEC-0007_liking_transfer_to_product_judgment.md` | Zeile 4 |
| 5 | MEC-0008 | Mechanismus (MEC) | ERWEITERT | `03_knowledge_base/mechanisms/MEC-0008_authority_automatic_deference.md` | Zeile 5 |
| 6 | MEC-0018 | Mechanismus (MEC) | ERWEITERT | `03_knowledge_base/mechanisms/MEC-0018_pre_suasion_attentionale_vorbereitung.md` | Zeile 6 |
| 7 | MOD-0002 | Modell (MOD) | ERWEITERT | `03_knowledge_base/models/MOD-0002_cialdini_six_principles.md` | Zeile 7 |
| 8 | MEC-0009 | Mechanismus (MEC) | KEINE ÄNDERUNG (geprüft und begründet) | `03_knowledge_base/mechanisms/MEC-0009_perceptual_contrast.md` | Zeile 8 |
| 9 | MOD-0008 | Modell (MOD) | KEINE ÄNDERUNG (geprüft und begründet) | `03_knowledge_base/models/MOD-0008_pre_suasion_modell.md` | Zeile 9 |
| 10 | — | Scientific Debt (kein Wissensobjekt) | NEU | `00_project/SCIENTIFIC_DEBT.md`, neue Sektion „W-002" | Zeile 10 |

**Nicht durchgeführt (bewusst, per Editor Decision):** Keine Neuanlage eines MEC für ELM. Keine Integration einer B2B-/Buying-Center-Transferaussage. Keine Auflösung der NFC×Argumentqualität-Replikationskontroverse zugunsten einer Seite. Keine Framework-Änderung.

## 3. Herkunftskennzeichnung (`REPOSITORY_INTEGRATION.md`, Abschnitt 3)

Alle sieben erweiterten Objekte tragen nach Integration die kombinierte Referenz `<ursprüngliche SRC-ID>, W-002`: MEC-0005, MEC-0006, MEC-0007, MEC-0008 tragen jeweils explizite `## Source ID`-Felder, aktualisiert zu `SRC-0002, W-002`. MEC-0012 trägt `SRC-0003, W-002`. MEC-0018 führt kein separates `## Source ID`-Feld (wie bereits bei MEC-0013 in der W-001-Integration dokumentiert) — die Herkunft ist im neuen Erweiterungsabschnitt „ELM-Klassifikation — Periphere Route" selbst dokumentiert. MOD-0002 führt kein `## Source ID`-Feld, sondern `## Ursprung / Quelle` — dort wurde `W-002 (Research Program)` als dritte Quellenzeile ergänzt.

## 4. Identitätsprüfung (`canonical_knowledge_model.md`, Abschnitt 4; `REPOSITORY_INTEGRATION.md`, Abschnitt 4)

Für jedes der sieben erweiterten Objekte wurde geprüft, ob die ELM-Klassifikation (zentral/peripher) bereits durch die bestehende Kausalstruktur des Objekts abgedeckt ist. Ergebnis: Ja — kein Objekt erhielt einen neuen Kausalpfad; jede Erweiterung ordnet den bereits bestehenden, unveränderten Kausalpfad (z. B. MEC-0005: Gabe → Verpflichtungsgefühl → Gegenleistung) zusätzlich in die ELM-Prozessarchitektur ein. Für MEC-0005–0008 und MEC-0018 wurden dabei ausschließlich bereits bestehende, im jeweiligen Objekt schon dokumentierte Verhaltensgrenzen (z. B. „schwächer bei Experten") theoretisch kontextualisiert — es wurde keine neue empirische Grenze behauptet, die nicht bereits im Objekt stand. Für MEC-0007 wurde zusätzlich eine explizite Konvergenzbeobachtung mit der bereits bestehenden Challenger-Grenze dokumentiert. Daraus folgt gemäß Entscheidungsbaum: **ERWEITERN**, nicht Neuanlage, für alle sieben Objekte.

## 5. Begründete Nicht-Änderung: MEC-0009 und MOD-0008

Die Editor Decision verlangt für diese beiden Objekte eine explizite, unabhängige Begründung statt einer mechanischen Übernahme der im Master Review skizzierten Repository Impact Analysis — mit dem ausdrücklichen Verbot, Änderungen allein zur Herstellung formaler Symmetrie mit den übrigen sieben Objekten vorzunehmen. Beide Fälle wurden im Rahmen dieser Integration erneut eigenständig geprüft:

**MEC-0009 (Perzeptueller Kontrast) — keine Änderung.** MEC-0009 beschreibt einen psychophysikalischen Wahrnehmungsmechanismus (Weber-Fechner-Stevens-Helson-Tradition, siehe Objekt selbst, Erweiterungsabschnitt „Psychophysikalische Grundlagen"): Die relative Wahrnehmung eines Reizes im Verhältnis zu einem vorangegangenen Reiz verändert sich unabhängig davon, ob der Beobachter hoch oder niedrig elaboriert verarbeitet — ein $100-Preisunterschied wirkt bei einem $300-Produkt größer als bei einem $3.000-Produkt, unabhängig von Motivation oder Fähigkeit des Käufers zur inhaltlichen Prüfung. Die ELM-Unterscheidung zentral/peripher betrifft, WIE eine Botschaft kognitiv verarbeitet wird (argumentbasiert vs. cue-basiert); MEC-0009 betrifft eine der Verarbeitung vorgelagerte, allgemeine Wahrnehmungsverzerrung, die auch bei vollständig zentraler, sorgfältiger Prüfung eines Angebots weiterhin wirkt (ein sorgfältiger Prüfer unterliegt demselben Kontrasteffekt wie ein oberflächlicher). Eine Zuordnung zu „überwiegend peripher" wäre daher wissenschaftlich nicht sauber begründbar — dies bestätigt unabhängig den bereits im Master Review dokumentierten Befund („Beziehung zu ELM ist nicht eindeutig nachweisbar — keine Beziehung konstruieren"). **Ergebnis: keine Änderung ist die wissenschaftlich korrekte Entscheidung, nicht nur die bequemste.**

**MOD-0008 (Pre-Suasion-Modell) — keine Änderung.** MOD-0008 ist ein reines Prozess-/Sequenzmodell, das seine Mechanismus- und Prinzipinhalte ausschließlich über Verweise führt, ohne sie zu duplizieren (Phase 1 verweist auf „Mechanismus: MEC-0018"; Phase 3 verweist auf „6+1 Cialdini-Prinzipien (MOD-0002 + Unity)"). Da sowohl MEC-0018 als auch MOD-0002 in dieser Integration bereits direkt mit der ELM-Klassifikation und dem entsprechenden Vorbehalt versehen wurden, würde eine zusätzliche, separate ELM-Ergänzung in MOD-0008 entweder (a) den bereits in MEC-0018/MOD-0002 dokumentierten Inhalt redundant wiederholen, ohne neue Aussage, oder (b) eine genuine neue Modell-Ebenen-Synthese erfordern, die weder im Master Review noch im Decision Brief mit hinreichender Prüftiefe entwickelt und von der Editor Decision auch nicht ausdrücklich freigegeben wurde (die „Geplante Integration"-Tabelle der Editor Decision listet MOD-0008 nicht unter den freigegebenen Elementen). Eine Ergänzung nur deshalb, weil MOD-0008 in derselben Repository-Impact-Analyse-Tabelle wie MEC-0018 stand, wäre exakt die vom Herausgeber ausgeschlossene Änderung „allein zur Herstellung formaler Symmetrie". **Ergebnis: keine Änderung, da der relevante Inhalt bereits transitiv über die bestehenden Verweise auf MEC-0018 und MOD-0002 zugänglich ist und keine eigenständige neue Aussage für MOD-0008 selbst identifiziert wurde.**

## 6. Qualitätsprüfung (`canonical_knowledge_model.md`, Abschnitt 5)

Keine neuen Objekte angelegt — die Mindestschwellen-Prüfung für eine MEC-Neuanlage entfällt entsprechend. Die Ablehnung eines eigenständigen ELM-MEC ist in der Editor Decision (Abschnitt 1) ausdrücklich als editorische Sparsamkeitsentscheidung gekennzeichnet, nicht als zwingende Schwellenwert-Prüfung — dies wird hier nicht erneut hergeleitet, sondern unverändert übernommen.

## 7. Zusammenführungskandidaten

Keine identifiziert. Alle sieben erweiterten Objekte bleiben eigenständig; keine Fusion vorgeschlagen oder erforderlich.

## 8. Nachgelagerte Dokumentation außerhalb der sieben Objekte

| Dokument | Änderung | Bezug |
|---|---|---|
| `00_project/SCIENTIFIC_DEBT.md` | Neue Sektion „W-002 — Persuasion Architecture / Elaboration Likelihood Model" mit drei Einträgen (B2B-/Buying-Center-Transferlücke; NFC×Argumentqualität-Replikationskontroverse; offene Theory-Competition-Frage ELM/HSM/Unimodel) | Editor Decision, Abschnitt 3, 4, 5 (OQ-2, OQ-3, OQ-5) |
| `06_research_program/active/W002/OPEN_QUESTIONS.md` | OQ-1 an Governance-Ebene übergeben; OQ-2 als offene Kontroverse übergeben; OQ-3 als nicht blockierend übergeben; OQ-4 beantwortet (Cross-Link angenommen); OQ-5 beantwortet (Scientific Debt, kein Folgeprojekt) | Editor Decision, Abschnitt 5 |
| `06_research_program/RESEARCH_STATUS.md` | W-002-Zeile nach Health Check von `active/`- in `completed/`-Tabelle zu verschieben (siehe `HEALTH_CHECK.md`) | Health Check, Stufe 9 |
| `06_research_program/RESEARCH_PORTFOLIO.md` | RP-001-Status nach Health Check auf `Integrated` zu setzen, mit Verweis auf verbleibende Scientific-Debt-Position | Health Check, Stufe 9 |

## 9. Versionierung

Kein Git-Commit im Rahmen dieser Integration durchgeführt — Git-Operationen bleiben ausschließlich Aufgabe des Herausgebers (`00_project/task_rules.md`, Abschnitt 9.1; `REPOSITORY_INTEGRATION.md`, Abschnitt 7). Alle Änderungen liegen als Working-Tree-Änderungen vor und sind über dieses Log vollständig nachvollziehbar.

## 10. Status

Vollständig — alle zehn in der Editor-Decision-Tabelle benannten Zeilen bearbeitet (sieben Erweiterungen, zwei begründete Nicht-Änderungen, ein neuer Scientific-Debt-Eintrag). Übergabekriterium an Stufe 9 (`RESEARCH_LIFECYCLE.md`, Abschnitt 10) erfüllt.
