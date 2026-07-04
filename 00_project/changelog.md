# Changelog

## 2026-07-04 — Sales Codex Version 1.0 — Repository Closing & Release Sprint

- Rolle: Editor-in-Chief / Release Manager / Repository Curator. Letzter Sprint für Version 1.0 — Zweck: finalen Zustand wissenschaftlich dokumentieren, Repository formal abschließen, Version 1.0 offiziell veröffentlichen. Kein Entwicklungssprint mehr.
- Drei externe Gutachten ("Wissenschaftliche Prüfung des Sales Codex", "Wissenschaftliche Begutachtung des Behavioral Science Sprints", "Sales Codex Release Audit"/Final RC-1 Release Audit) als Finaler RC-1-Audit verarbeitet.
- Neu: `00_project/FINAL_RC1_AUDIT_VALIDATION_REPORT.md` — alle 19 Einzelkritikpunkte der drei Gutachten punktweise gegen den tatsächlichen Repository-Zustand validiert (14 behoben, 1 teilweise behoben, 2 weiterhin gültig/nicht-blockierend, 1 durch Editor Decision abgelehnt bestätigt, 1 nicht reproduzierbar). Ursprünglich behauptete Release Blocker (SRC-0010 fehlend, fehlende Publication-Bias-Warnungen) als sachlich unzutreffend bzw. vollständig behoben festgestellt.
- Neu: `00_project/REPOSITORY_CLOSING_STATUS.md` — abschließender Status über 14 Prüfdimensionen (Konsistenz, Governance, Research Program, Evidence System, Scientific Debt, Open Decisions, Canonical Knowledge Model, Repositorystruktur, Release-Dokumente, Cross References, tote Links, Quellen, Wissensobjekte, Versionierung). Ergebnis: kein echter, unadressierter Release Blocker.
- Neu: `00_project/FINAL_EDITOR_ASSESSMENT_V1_0.md` — wissenschaftliche und editorische Gesamtbewertung (wesentliche Erkenntnisse, einflussreichste Architekturentscheidungen, gelöste/abgelehnte Kritikpunkte, bewusste Einschränkungen, Übergabe an Version 1.1).
- Neu: `00_project/SALES_CODEX_VERSION_1_0_RELEASE.md` — offizielle Veröffentlichungserklärung (Titel, Datum, Version, Herausgeber, Executive Summary, Ziel, Umfang, wissenschaftliche Grundlage, Governance, Research Program, Audit-Historie, Veröffentlichungsentscheidung, bekannte Einschränkungen, Ausblick auf Version 1.1).
- Neu: `00_project/VERSION_1_0_CLOSING_REPORT.md` — Abschlussbericht mit Executive Summary, Zusammenfassung aller externen Gutachten, Repository-/Governance-/Research-Program-/Scientific-Debt-/Open-Decisions-Endzustand, Releaseentscheidung, Lessons Learned, Empfehlung für Version 1.1. **Einstufung: VERSION 1.0 OFFICIALLY RELEASED.**
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`: aktualisiert (Sales-Codex-Gesamtversion jetzt 1.0, veröffentlicht am 2026-07-04; Framework-Version unverändert 1.1).
- Keine neuen Wissensobjekte, keine neuen Quellen, keine neue Forschung, keine Literature Reviews, keine Frameworkänderungen, keine Änderungen am Canonical Knowledge Model, Operating Manual, Research Program, Research Lifecycle oder an abgeschlossenen Forschungsprojekten/Editor Decisions, keine neuen Open Decisions, keine Repository-Umstrukturierungen.
- **Bedeutung:** Sales Codex Version 1.0 ist ab 2026-07-04 offiziell veröffentlicht und gilt ab sofort als unveränderlich. Die Entwicklungsphase von Version 1.0 ist abgeschlossen. Version 1.1 wurde noch nicht begonnen. Es dürfen keine weiteren Entwicklungssprints für Version 1.0 mehr eröffnet werden.

## 2026-07-04 — Sales Codex Version 1.0 RC-1 Release Candidate Freeze

- Rolle: Release Manager / Configuration Manager. Auftrag: veröffentlichungsreifen Zustand dokumentieren und als Version 1.0 RC-1 einfrieren — keine fachlichen, wissenschaftlichen oder Framework-Änderungen.
- Neu: `00_project/RELEASE_CANDIDATE_RC1.md` — 18 Freeze-Kennzahlen (Version, Datum, Repository-Status, Objektzahlen, Open Decisions, Scientific Debt, Research-Program-/W-001-/Audit-Status, bekannte Einschränkungen, Freigabestatus), unabhängig gegen Dateisystem und `FINAL_PRE_RELEASE_REPORT.md` verifiziert.
- Neu: `00_project/RELEASE_NOTES_v1.0_RC1.md` — Neuerungen, wissenschaftliche Ergebnisse, Architekturentscheidungen, Research Program, W-001, Behavioral Science, Repository Consolidation, Breaking Changes, Einschränkungen.
- Neu: `00_project/REPOSITORY_MANIFEST_RC1.md` — vollständiger Struktur-Snapshot (Ordnerstruktur, Objektanzahlen, Versionen, Governance-/Framework-Dokumente, Forschungsprojekte, wissenschaftliche Abdeckung), keine Inhaltsänderung.
- Release Verification (Phase 4) durchgeführt: Cross-Referenzen, Governance, CKM, Scientific Debt, Evidence System, Open Decisions, Repositorystruktur geprüft — keine sprintrelevanten Inkonsistenzen gefunden, keine bestehende Datei inhaltlich verändert.
- Neu: `00_project/RC1_FREEZE_DECLARATION.md` — formale Erklärung des Freeze; zulässige/unzulässige Änderungen bis Version 1.0; Umgang mit Version-1.1-Backlog.
- Neu: `00_project/RC1_FREEZE_REPORT.md` — Abschlussbericht mit Empfehlung **READY FOR FINAL RC-1 AUDIT** (mit dem Herausgeber während des Sprints abgestimmt — ausdrücklich nicht "READY FOR VERSION 1.0 RELEASE", da der im Release Plan definierte Finale RC-1-Audit und die formale Herausgeber-Freigabe durch diesen Freeze nicht ersetzt werden).
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`: aktualisiert (Sales-Codex-Gesamtversion jetzt RC-1 statt Pre-1.0).
- Keine neuen Wissensobjekte, keine neue Forschung, keine Frameworkänderungen, keine Änderungen am Canonical Knowledge Model, Operating Manual, Research Program oder an abgeschlossenen Forschungsprojekten/Editor Decisions, keine neuen Open Decisions, keine Repository-Umstrukturierungen.
- **Bedeutung:** Sales Codex Version 1.0 RC-1 gilt ab 2026-07-04 als eingefrorener Release Candidate. Änderungssperre gemäß `RC1_FREEZE_DECLARATION.md` aktiv bis zur formalen Herausgeber-Freigabe von Version 1.0.

## 2026-07-03 — Research Project W-001 Repository Integration Sprint (Post Editor Decision)

- Editor Decision zu W-001 durch den Herausgeber (Felix) getroffen: **Teilweise annehmen.** Mathematische Formalisierung des Socio-Cognitive Sensegiving Model (SCSM) nicht übernommen; Kernbefund übernommen (Diagnose- und Teaching-/Sensemaking-orientierte Vertriebsansätze stehen nicht in universellem Widerspruch, sondern beschreiben kontextabhängig koexistierende Wirkmechanismen). Keine neue Grand Theory, kein MOD, keine Differentialgleichung, kein neues Symbolsystem.
- `06_research_program/completed/W001/06_EDITOR_DECISION.md`: von Entwurf auf finale Entscheidung überführt (Begründung, Stellungnahme zu 3 Streitpunkten, Integrationstabelle, ethische Einschätzung, Datum/Unterschrift).
- **Repository Integration (6 Objekte erweitert, keine Neuanlage):** `A-0020`, `P-0021`, `P-0025`, `MEC-0013`, `T-0019`, `T-0023` — jeweils Kontextpräzisierung statt "Widerspruch"/"Methodologiekonflikt", Herkunftsfeld um `W-001` ergänzt, neuer Abschnitt "Erweiterung durch W-001" in jedem Objekt.
- Neu: `06_research_program/completed/W001/REPOSITORY_INTEGRATION_LOG.md`.
- `00_project/SCIENTIFIC_DEBT.md`: neue Sektion "W-001 — Teach First vs. Diagnose First (Research Program)" (OQ-2 bis OQ-4 technisch übergeben, Gartner-Quellenklassifizierung als offener Punkt); zwei bestehende Einträge (A-0020 vs. P-0025; MOD-0001 vs. MOD-0004) als kontextuell aufgelöst markiert, nicht gelöscht.
- `00_project/OPEN_DECISIONS.md`: neue Open Decision **OD-012** (Formalisierung der Kontextspezialisierung P-0021/P-0025 und MEC-0013/MEC-0001).
- `06_research_program/completed/W001/OPEN_QUESTIONS.md`: OQ-1 auf `beantwortet`; OQ-2–OQ-4 auf `übergeben — technisch vollzogen`; OQ-5 unverändert an OD-007.
- Echter Abschluss-Health-Check (Stufe 9, nach Integration) in `06_research_program/completed/W001/HEALTH_CHECK.md` durchgeführt und bestanden (eine bewusst akzeptierte Restlücke: Stufe-1/2-Alt-Lücke).
- Projektordner `06_research_program/active/W001/` → `06_research_program/completed/W001/` verschoben (unverändert). `06_research_program/RESEARCH_STATUS.md` entsprechend aktualisiert.
- Neues Dokument: `06_research_program/completed/W001/W001_REPOSITORY_INTEGRATION_REPORT.md`.
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`: aktualisiert.
- Keine neue Forschung, keine neue Literaturrecherche, keine Frameworkänderungen, keine Änderungen am Canonical Knowledge Model oder Operating Manual über die zur Integration zwingend notwendigen Herkunftsvermerke hinaus.
- **Bedeutung:** W-001 ist das erste Forschungsprojekt, das den vollständigen neunstufigen RC-1 Research Lifecycle erfolgreich durchlaufen hat.

## 2026-07-02 — Repository Consolidation Sprint 2 (Implementation Phase)

- Acht vom Herausgeber freigegebene Editor Decisions (ED-001 bis ED-008) aus `00_project/REPOSITORY_CONSOLIDATION_REPORT_RC1.md` umgesetzt. Rein struktureller Sprint — keine eigenen Architekturentscheidungen, keine zusätzlichen Optimierungen.
- **ED-001:** Leerer Duplikat-Ordner `04_book_analysis/Never_Split_The_Difference/` gelöscht.
- **ED-002:** `04_book_analysis/Emotional Intelligence/test_probe.md` (0-Byte-Debug-Datei) gelöscht.
- **ED-003:** `codex_knowledge_model.md` von `01_framework/05_knowledge_model/` nach `99_archive/` verschoben (unverändert). `INDEX.md` Zeile 21 korrigiert: verweist jetzt auf `canonical_knowledge_model.md` statt auf das archivierte Dokument.
- **ED-004:** `VAL-0001_consistency_review_pilot001.md` + `PILOT_001_ABSCHLUSSBERICHT.md` von `00_project/` nach `04_book_analysis/SPIN_Selling/` verschoben; `VAL-0002_consistency_review_influence.md` von `00_project/` nach `04_book_analysis/Influence/` verschoben. Alle drei Dokumente inhaltlich unverändert.
- **ED-005:** `SCRP-0001_Sales_Core.md` von der Repository-Root nach `00_project/peer_review/decisions/` verschoben (unverändert).
- **ED-006/007/008:** `decision_log.md`, `roadmap.md`, `task_proposal_B-0002_influence.md` von `00_project/` nach `99_archive/` verschoben (alle drei unverändert).
- Repositoryweite Cross-Reference- und Referenzprüfung durchgeführt: genau eine aktive Referenz korrekturbedürftig (`INDEX.md`), korrigiert; alle übrigen Fundstellen der acht Alt-Pfade liegen in datierten historischen Sprintberichten und bleiben bewusst unverändert (historische Zustandsbeschreibung).
- Repository Health Check: keine verwaisten Dateien, keine doppelten Dateiinhalte, leere Ordner 18 → 17 (nur der gelöschte Duplikat-Ordner entfällt).
- Git Status geprüft: `git log` funktionsfähig (3 Commits); `git status`/`git diff` schlagen mit einem vorbestehenden `.git/index`-Formatfehler fehl (`fatal: unknown index entry format 0x32380000`) — unabhängig von diesem Sprint, nicht behoben (außerhalb des Scopes), dem Herausgeber zur Kenntnis gegeben.
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`: aktualisiert.
- Keine Änderungen an `book_catalog.md`, Research Program, Open Decisions, Literature Index, Scientific Debt, Canonical Knowledge Model, Framework-Struktur, Top-Level-Ordnern, Ordnernummerierung oder README-Dateien.
- Neues Dokument: `00_project/REPOSITORY_CONSOLIDATION_IMPLEMENTATION_REPORT_RC1.md`.

## 2026-07-02 — Behavioral Science Review Sprint (Editor Decision + Umsetzung)

- Unabhängiges externes wissenschaftliches Gutachten zum Behavioral Science Expansion Sprint (SPR-0003) geprüft; verbindliche Editor Decision erstellt: `00_project/BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md` (8 Reviewer-Empfehlungen einzeln bewertet: 4× Übernehmen, 3× Teilweise übernehmen, 1× Ablehnen).
- **ED-001 (Übernehmen):** MEC-0025 umbenannt von "Fairness-Verzicht" in "Altruistische Bestrafung (Altruistic Punishment)" — reine Namenskorrektur, keine Neuanlage, kausale Struktur unverändert. Henrich-Boundary-Conditions bereits vollständig dokumentiert, keine Ergänzung nötig. Betroffen: `MEC-0025_fairness_verzicht_ultimatum.md`, `MOD-0010_kahneman_kognitive_bias_karte.md`, `SCIENTIFIC_DEBT.md`.
- **ED-002 (Übernehmen, teilweise bereits erfüllt):** Geprüft, ob B-0011-Scientific-Debt-Lücken (Marshmallow, Ekman/Barrett, Konstruktvalidität) bestehen. Ergebnis: Marshmallow (ST-0213) und Ekman/Barrett (ST-0214) waren bereits vollständig dokumentiert — Reviewer-Behauptung eines fehlenden Eintrags traf nicht zu (Widerspruch dokumentiert, nicht geglättet). Neuer Eintrag ausschließlich für die tatsächlich fehlende Konstruktvalidität-EI-vs.-Big-Five-Lücke ergänzt (mit Quellenvorbehalt, da Harms & Credé 2010/Landy 2005/Locke 2005 nicht eigenständig websuchverifiziert). MEC-0022 unverändert, Goleman bleibt Sekundärquelle in SRC-0011.
- **ED-003/ED-004 (Teilweise übernehmen):** Geprüft, ob die bestehende CKM-MOD-Definition (`canonical_knowledge_model.md` Abschnitt 5: "≥3 verknüpfte Prinzipien, kausallogische Struktur beschreibbar") die aktuelle MOD-Einordnung von MOD-0011 (Choice Architecture) und MOD-0012 (SUCCESS-Framework) bereits erlaubt. Ergebnis: Ja, beide Modelle erfüllen die Codex-eigene Schwelle bereits nachweisbar. Konsequenz: Klassifikationshinweis in beiden MOD-Dateien ergänzt (macht die vom Reviewer zu Recht benannte Einschränkung — kein formal-empirisches Gesamtmodell — explizit sichtbar), keine Umklassifizierung, keine Frameworkänderung.
- **ED-005 (Übernehmen, eng ausgelegt):** Boundary Conditions "Individual→Organisation" an den drei vom Reviewer namentlich benannten Sprint-Objekten ergänzt: MEC-0002 (Default-Erweiterung), MEC-0021 (Anchoring), MEC-0022 (Emotional Contagion). Keine repositoryweite Massenänderung.
- **ED-006 (Teilweise übernehmen):** Ariely-Autoren-Integritätsrisiko-Eintrag in `SCIENTIFIC_DEBT.md` (B-0012-Sektion) nicht geschlossen, sondern Status auf "partially mitigated" präzisiert — entschärft für die vier namentlich genannten Kernmechanismen, unverändert offen für die Ehrlichkeits-/Dishonesty-Forschungslinie und die generelle Integritätsrisiko-Kategorie.
- **ED-007 (Übernehmen, bereits erfüllt):** Geprüft, ob Literature-Index-Lücken (Carmon & Ariely fragmentiert, Newton/Bechky/UCLA unverifiziert) bestehen. Ergebnis: Carmon-&-Ariely-Eintrag bereits vollständig (Reviewer-Behauptung traf nicht zu, Widerspruch dokumentiert); Newton/Bechky/UCLA waren bereits korrekt als unresolved gekennzeichnet. Prüfvermerk in `LITERATURE_INDEX.md` ergänzt, keine inhaltliche Korrektur nötig.
- **ED-008 (Ablehnen):** Neue Objektkategorien PRX/TAX abgelehnt — Framework-Änderung außerhalb des Sprintumfangs (CKM Abschnitt 10: Einführung neuer Objekttypen ist Herausgeber-Entscheidung). Keine Datei geändert.
- Keine neuen Objekt-IDs, keine neuen Kategorien, keine neuen Templates, keine Framework-Versionsänderung, keine Open Decisions geändert, kein Eingriff in Operating Manual oder Canonical Knowledge Model.
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`: aktualisiert.

## 2026-07-02 — BEHAVIORAL SCIENCE EXPANSION SPRINT 1 (B-0011 bis B-0015)

- Fünf Bücher vollständig im Book Mode verarbeitet, Phase "Scientific Completion" des Sales Codex 1.0 Programms: B-0011 Emotional Intelligence (Goleman), B-0012 Predictably Irrational (Ariely), B-0013 Nudge: The Final Edition (Thaler & Sunstein), B-0014 Priceless (Poundstone), B-0015 Made to Stick (Heath & Heath).
- Neue Mechanismen (8, je mit vollständiger Canonicalization-Rejection-Dokumentation): MEC-0022 (Emotional Contagion), MEC-0023 (Zero-Preis-Effekt), MEC-0024 (Sludge), MEC-0025 (Fairness-Verzicht/Ultimatum-Spiel), MEC-0026 (Curse of Knowledge), MEC-0027 (Gap-Theorie der Neugier), MEC-0028 (Konkretheits-Encoding), MEC-0029 (Narrative Transportation).
- Mechanismus-Erweiterungen (16): MEC-0002, MEC-0005, MEC-0006, MEC-0008, MEC-0009 (×2), MEC-0010, MEC-0011, MEC-0015, MEC-0018, MEC-0020, MEC-0021 (×3) — vollständige Zuordnung je Buch in `04_synthesis/SPR-0003_Behavioral_Science_Synthesis/SPR-0003_BEHAVIORAL_SCIENCE_SYNTHESIS.md` Abschnitt 2.
- Zwei neue Modelle: MOD-0011 (Choice Architecture, B-0013), MOD-0012 (SUCCESS-Framework, B-0015). MOD-0010 zweifach erweitert (B-0012, B-0014).
- Neue Quellen SRC-0011 bis SRC-0015; 108 neue Statements, 12 neue Annahmen, 10 neue Prinzipien, 6 neue Techniken.
- Sprintweite Canonicalization Rate (MEC-basiert): 66,7 % (16 Erweiterungen / 24 Gesamtentscheidungen).
- `00_project/SCIENTIFIC_DEBT.md`: fünf neue Buchsektionen (B-0011 bis B-0015); Autoren-Integritätsrisiko-Kategorie neu eingeführt (B-0012, Ariely-Datenfälschungskontroverse); duplizierte SD-SYS-005-Sektion (fälschlich durch B-0013-Subagent angelegt) korrigiert und gemergt.
- `05_research/LITERATURE_INDEX.md`: ~50 neue verifizierte Quellen, neue Sektion E "Kommunikationspsychologie, Gedächtnis & Narrativpersuasion" (B-0015). Version 1.1 → 1.2.
- Zwei Replikationsversagen unabhängig recherchiert und transparent dokumentiert: Verschuere et al. (2018, Ten-Commandments-Priming) und Maier et al. (2023, Identifiable Victim Effect).
- Neues Dokument `04_synthesis/SPR-0003_Behavioral_Science_Synthesis/SPR-0003_BEHAVIORAL_SCIENCE_SYNTHESIS.md` — sprintweite Synthese mit 9 Pflichtabschnitten.
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`: aktualisiert.
- Keine Framework-Änderungen, keine Governance-Entscheidungen, keine Open Decisions geschlossen, keine Repository-Restrukturierung.
- Bekanntes offenes Housekeeping-Item (nicht blockierend): `04_book_analysis/Emotional Intelligence/test_probe.md` — leere Debug-Datei eines Subagenten, im geschützten Workspace-Ordner, erfordert Nutzerfreigabe zur Löschung.

## 2026-07-02 — SALES CODEX 1.0 PROGRAM

- Neues zentrales Steuerungsdokument `00_project/SALES_CODEX_1_0_PROGRAM.md` angelegt — definiert den offiziellen Entwicklungsplan bis Version 1.0 (12 Kapitel: Vision, Mission, Ist-Zustand, 5 Entwicklungsphasen, Qualitätskriterien, Blocker, Nicht-Blocker, Governance nach 1.0, Versionierungsschema, Roadmap, Definition of Done, Executive Summary).
- Ersetzt die bisherige rein sprintorientierte Entwicklungslogik als übergeordneten Rahmen; einzelne Sprint-Typen (Book Mode, Academic Recovery, Peer Review, Consistency Correction, Governance) bleiben operative Werkzeuge innerhalb der neuen Phasenstruktur.
- Zwei inhaltliche Kernblocker und zwei Governance-Blocker für Version 1.0 identifiziert und priorisiert; acht Nicht-Blocker mit Begründung dokumentiert.
- Versionierungsschema eingeführt: Framework-Version (aktuell 1.1) und Sales-Codex-Gesamtversion (Ziel 1.0) als zwei getrennte Achsen.
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md` aktualisiert.
- Keine neuen Wissensobjekte, keine neue Recherche, keine Framework-Änderungen, keine Repository-Strukturänderungen, keine Open Decisions geschlossen.

## 2026-07-02 — Open Decisions Resolution Sprint

- Reiner Governance-Sprint: alle acht bestehenden Open Decisions (OD-001–OD-008) einzeln geprüft, keine neue Recherche, keine neuen Wissensobjekte, keine Framework-Änderungen.
- `00_project/OPEN_DECISION_RESOLUTION_REPORT_2026-07.md` neu angelegt.
- `00_project/OPEN_DECISIONS.md`: OD-001–OD-004 auf DONE gesetzt (OD-003 mit dokumentierter Restlücke: Repository Health Check nie formalisiert); OD-005 auf ERSETZT gesetzt (→ OD-010); OD-006/OD-007 geprüft und weisungsgemäß nicht automatisch geschlossen (bleiben OFFEN, bestätigt entscheidungsreif); OD-008 geprüft, bleibt OFFEN; drei neue Einträge angelegt — OD-009 (Framework RC1/Reifegrad-Statusübergang), OD-010 (Validierungs-Governance, Nachfolger OD-005), OD-011 (Literature-Governance).
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`: aktualisiert.
- Keine neuen Wissensobjekte, keine neue Recherche, keine Framework-Änderungen, keine inhaltliche Priorität verschoben.

## 2026-07 — Codex Audit 2026-07 + Consistency Correction Sprint (Meilenstein 1)

- **Audit (rein lesend):** `00_project/CODEX_AUDIT_2026-07.md` neu angelegt — vollständiger 12-Kapitel-Repository-Audit, Gesamtnote B+. Keine Repository-Änderungen im Audit-Schritt selbst.
- **Consistency Correction Sprint (nur Meilenstein 1 aus Audit Kapitel 11):** `00_project/CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md` neu angelegt.
- `T-0012_mirroring.md`, `T-0013_labeling.md`: Evidenzlevel E3 → E2 synchronisiert mit MEC-0011/MEC-0010.
- `T-0019_commercial_teaching_pitch.md`, `T-0020_stakeholder_tailoring.md`, `T-0021_prozessausstieg_bei_unguenstigen_bedingungen.md`, `T-0026`–`T-0034` (JOLT- und Getting-to-Yes-Techniken): Evidenzlevel-Feld neu ergänzt (Cross-Referenz auf verlinkte Objekte, keine neue Bewertung).
- `T-0022`–`T-0025` (Gap Selling): Feldname „Evidenzgrad" → „Evidenzlevel" harmonisiert, Werte unverändert.
- `P-0027`–`P-0034` (JOLT- und Getting-to-Yes-Prinzipien): Evidenzklassifikations-Feld neu ergänzt.
- `P-S1-001`–`P-S1-004`: Sichtbarkeits-Spiegel des bestehenden YAML-`e_level`-Feldes ergänzt; Audit-Falschbefund („Feld fehlt") richtiggestellt.
- `01_framework/05_knowledge_model/codex_knowledge_model.md`: Veraltet-Banner ergänzt (Datei nicht gelöscht), Empfehlung an Herausgeber dokumentiert.
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`: aktualisiert.
- **Nicht verändert, nur dokumentiert:** `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (E5-Zähler-Erratum als separater Vermerk, Original nicht editiert); `04_book_analysis/Never_Split_The_Difference/` (leerer Duplikat-Ordner, zur Entfernung vorgemerkt, nicht gelöscht).
- Keine neuen Wissensobjekte, keine neue Recherche, keine Framework-Änderungen.

## 2026-07-01 — ARS-0001 Academic Recovery Sprint, Phase 2: Research Pack 2, 3, 4

- Drei Research Packs (Entscheidungspsychologie/Behavioral Economics, Sozialpsychologie/Persuasion, Verhandlungsforschung) geprüft und integriert: `00_project/ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`
- Neuer Repository-Bereich `05_research/` mit `LITERATURE_INDEX.md` (kein Wissensobjekt — Literaturverzeichnis, ~50 Quellen)
- Drei Meta-Analysen websuchverifiziert: Brown/Imai/Vieider/Camerer (2024, Loss Aversion), Schley & Weingarten (Anchoring, Zitationskorrektur), Mertens et al. (2021, Nudging — Publication-Bias-Kontroverse dokumentiert)
- 15 bestehende Objekte um Literaturreferenzen erweitert (CKM 4.1): MEC-0002, MEC-0003, MEC-0005–0008, MEC-0010, MEC-0011, MEC-0012, MEC-0017, MEC-0019, MEC-0020, MEC-0021, MOD-0007, A-0038
- `00_project/SCIENTIFIC_DEBT.md`: SD-SYS-005 (Nudging-Publication-Bias), SD-SYS-006 (Konvergenzbestätigungen B-0002/B-0003)
- `00_project/review_queue.md`: 5 neue Literaturkandidaten (ELM, Trust Formation, Persuasion Knowledge Model, Fairness/Equity, Choice Architecture)
- `00_project/OPEN_DECISIONS.md`: OD-008 neu
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md` aktualisiert
- Keine neuen Wissensobjekte, keine Framework-Änderungen, keine E-Level-Kategoriewechsel (nur Quantifizierungs-Präzisierungen bei MEC-0002, MEC-0021)

## 2026-07-01 — ARS-0001 Academic Recovery Sprint: Peer Review Sprint 2 + Research Pack 1

- Wissenschaftliches Gutachten nach Sprint 2 bewertet: `00_project/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md` (12 Empfehlungen einzeln entschieden und begründet)
- Research Pack 1 (8 externe Quellen) verifiziert und integriert: `00_project/ACADEMIC_RECOVERY_REPORT.md`
- `00_project/ACADEMIC_RECOVERY_PLAN.md` neu angelegt — priorisierte Literatur-Roadmap
- `00_project/SCIENTIFIC_DEBT.md`: neue Kategorie "Publication Bias (kommerzielle Studien)", SD-SYS-004, ARS-0001-Abschnitte ergänzt
- `03_knowledge_base/mechanisms/MEC-0014_konsens_als_kaufsicherheit_in_gruppen.md`: Theorie-Referenzen ergänzt (Webster & Wind 1972, Sheth 1973, Eisenhardt 1989); E-Level unverändert
- `00_project/review_queue.md`: MEC-0006/0014-Update, neue Kandidaten (MEC "Adaptive Selling Behavior", Meta-Prinzip "Asymmetrische Risikoverteilung im Buying Center")
- `00_project/OPEN_DECISIONS.md`: OD-007 (CTX-Ebene) neu — wissenschaftlich bewertet, nicht eingeführt; OD-006 ergänzt
- `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md` aktualisiert
- Keine neuen Wissensobjekte, keine Framework-Änderungen, keine E-Level-Änderungen an bestehenden Objekten

## 2026-06-27 — v0.2 Workspace Bootstrap

- Umstellung auf englische Ordner- und Dateinamen.
- Inhalte konsequent deutschsprachig.
- `CONTRIBUTING.md` ergänzt.
- `LANGUAGE_POLICY.md` ergänzt.
- Framework-Dokumente angelegt.
- Agentenleitfäden angelegt.
- Templates angelegt.
- Erste SPIN-Selling-Pilotobjekte angelegt.


## 2026-06-27 — Pilot 001 SPIN Selling vollständig analysiert

- Kapitel 1 bis 8 von SPIN Selling nach Codex-Methodik durchgearbeitet.
- 19 Statement-Objekte angelegt (ST-0001 bis ST-0023).
- 4 Annahmen-Objekte (A-0001 bis A-0004).
- 7 Prinzip-Objekte (P-0001 bis P-0007).
- 4 Mechanismus-Objekte angelegt (erste im Repository: MEC-0001 bis MEC-0004).
- 4 Technik-Objekte angelegt (erste im Repository: T-0001 bis T-0004).
- MOD-0001 vollständig ausgebaut.
- Buchanalyse für alle 8 Kapitel abgeschlossen.
- Ordner 03_knowledge_base/mechanisms/ und /techniques/ angelegt.
- Interner Konsistenz-Review durchgeführt.
- Abschlussbericht Pilot 001 erstellt.

## 2026-06-30 — v1.1 Sales Codex OS Release

Grundlage: POST_MORTEM_B0002.md + RELEASE_NOTES_v1.1.md (freigegeben durch Felix 2026-06-30)

### Geänderte Dateien

**Templates:**
- `01_framework/08_templates/source_template.md` — Pflichtfelder "Ausgabe/Edition" und "Ausgabe aus Impressum verifiziert" ergänzt (A5)
- `01_framework/08_templates/book_analysis_template.md` — Kapitelstruktur-Tabelle mit Status-Spalte + Pflichthinweis auf Kapitelstatus-Update nach TASK-0003 (B2); vollständiges Template mit allen Sektions-Tabellen
- `01_framework/08_templates/technique_template.md` — Source-ID-Feld ergänzt; Technik-vs-Kompetenz-Abgrenzung als Pflichthinweis; Ethisches Risiko Feld ergänzt (B5)
- `01_framework/08_templates/model_template.md` — Source-ID-Feld ergänzt; Canonicalisierungsentscheidung-Abschnitt; Quervergleich-mit-bestehenden-MOD-Abschnitt (B6)

**Workflow-Dokumente:**
- `00_project/task_rules.md` — Abschnitt 10 (Book Mode) neu: Definition, Stopp-Bedingungen, Pflichtabschluss, Prinzipien-OR-Regel, Technik-vs-Kompetenz-Definition, Nicht-Anlage-Dokumentationspflicht; VAL-Ablageregel auf `04_book_analysis/[Buch]/` aktualisiert (A1, A3, A4, A6, B1, B2, B4, B5)
- `00_project/SALES_CODEX_OPERATING_MANUAL.md` — Schritt 5: Prinzipien-OR-Regel + Abgrenzungspflicht ergänzt; Schritt 8: VAL-Ablage auf `04_book_analysis/[Buch]/` aktualisiert; Abschnitt 10 (Book Mode) neu (A1, A6, B1)
- `00_project/COWORK_EXECUTION_PROTOCOL.md` — Abschnitt 2.1: Session-Start auf PROJECT_BOOTSTRAP + CURRENT_STATE + NEXT_ACTION umgestellt; Abschnitt 5.2: Definition of Done aktualisiert (Kapitelstatus, VAL-Ablage, BOOK_REVIEW-Template, Stateless-Abschluss); Abschnitt 6.1: NEXT_ACTION.md als primäre Quelle; Abschnitt 8 (Book Mode) neu (A1, A4, B2)
- `01_framework/05_knowledge_model/canonical_knowledge_model.md` — Abschnitt 9 "Nicht-Anlage-Dokumentation" neu: Wann dokumentieren, Format, Beispiel aus B-0002 (A3)
- `PROJECT_BOOTSTRAP.md` — Dokumentklassifizierungssystem (Operational / Reference / Archived) ergänzt (B3 modifiziert)

### Neue Dateien

- `01_framework/08_templates/book_review_template.md` — Standardtemplate für BOOK_REVIEW_REPORT (A2)
- `00_project/SCIENTIFIC_DEBT.md` — Scientific-Debt-Konzept + initiale Einträge für B-0001 und B-0002 (N2)
- `00_project/REPOSITORY_KPIS.md` — KPI-Framework + initiale Messwerte für B-0001 und B-0002 (N1)

### Nicht geändert (bewusste Entscheidung)

- Bestehende Wissensobjekte (ST, A, MEC, P, T, MOD): keine Änderungen
- Ordnerstruktur: unverändert
- `CLAUDE_BOOTSTRAP.md`, `roadmap.md`, `review_queue.md`: erhalten, als Archived klassifiziert

---

## 2026-06-30 — B-0002 Influence vollständig abgeschlossen

- 59 neue Wissensobjekte: ST-0024–ST-0049, A-0005–A-0012, MEC-0005–MEC-0009, MEC-0001/0003/0004 erweitert, P-0008–P-0015, T-0005–T-0011, MOD-0002, VAL-0002
- Canonicalization Rate: 37,5% (3 von 8 MECs)
- Stateless Agent Architecture eingeführt: PROJECT_BOOTSTRAP.md, CURRENT_STATE.md, NEXT_ACTION.md, OPEN_DECISIONS.md, SESSION_LOG.md

---

## 2026-06-27 — v1.0 Infrastruktur-Freeze

- `VISION.md` ergänzt.
- `CURRENT_STATE.md` ergänzt.
- `INDEX.md` ergänzt.
- `SETUP.md` ergänzt.
- `CLAUDE_BOOTSTRAP.md` ergänzt.
- zusätzliche Templates ergänzt:
  - `decision_template.md`
  - `validation_report_template.md`
  - `research_question_template.md`
  - `comparison_template.md`
  - `meeting_notes_template.md`
- Framework ab v1.0 eingefroren.
