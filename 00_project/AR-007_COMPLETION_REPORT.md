# AR-007 Completion Report — Prospect Theory / Anchoring / Framing: Primärquellen direkt verarbeitet

**Datum:** 2026-07-14
**Task-Typ:** T11_SCIDEBT (`TASK_TYPES.md`)
**Auftrag:** AR-007 aus `00_project/ACADEMIC_RECOVERY_PLAN.md` — Forschungsfrage: Können die bisher über Sekundärsynthese (SRC-0010) geführten Behavioral-Economics-Grundlagen direkt über die Originalquellen von Kahneman & Tversky / Tversky & Kahneman abgesichert werden, ohne bestehende MECs oder Evidenzlevel zu überdehnen?
**Ergebnis in einem Satz:** Ja — alle drei Originalquellen wurden im Volltext verarbeitet; sie machen die bestehende Evidenz sauberer tracebar, ändern sie inhaltlich nicht, und liefern drei dokumentierte Quellenzuordnungs-Präzisierungen; keine E-Level- und keine P-0002-Änderung.

---

## 1. Zugriffslage je Primärquelle

Alle drei Papers sind offiziell paywalled — Unpaywall-API (2026-07-14): `is_oa: false`, `has_repository_copy: false`, `oa_status: closed` für alle drei DOIs (10.1126/science.185.4157.1124; 10.2307/1914185; 10.1126/science.7455683). Volltextzugriff gelang dennoch über legitime, universitätsgehostete Digitalisate — dieselbe Zugriffsklasse, die im AR-013-Präzedenzfall (SRC-0016, `bear.warrington.ufl.edu`) bereits dokumentiert und akzeptiert wurde:

| Quelle | Zugriffsweg | Status |
|---|---|---|
| Tversky & Kahneman (1974), *Science* 185 | JSTOR-Digitalisat via UCI-Fakultätsseite (`sites.socsci.uci.edu/~bskyrms/`) + vollständige HTML-Transkription (`chsasank.com`); Schlüsselzitate zeichengenau gegen das Digitalisat verifiziert | **Volltext gelesen** |
| Kahneman & Tversky (1979), *Econometrica* 47 | JSTOR-Digitalisat mit Textlayer via University-of-Puget-Sound-Kursseite (`webspace.pugetsound.edu/facultypages/gmilam/`); erster Versuch (`courses.washington.edu`) war ein Scan ohne Textlayer und wurde verworfen | **Volltext gelesen** (inkl. Appendix/Axiomatik) |
| Tversky & Kahneman (1981), *Science* 211 | Science-Digitalisat via Stanford-Kursseite (`web.stanford.edu/class/psych205/`) | **Volltext gelesen** |

Kein Sci-Hub, keine Umgehung von Zugriffsschutz. **Dokumentierte Restunsicherheit (nicht geglättet):** Universitäts-Kurs-/Fakultätsseiten sind keine Verlags-Open-Access-Quellen. Frühere AR-Sitzungen haben diese Zugriffsklasse unterschiedlich behandelt (AR-013: UF-Fakultätsseite genutzt; AR-006: Kurs-Hosting-Spiegel bewusst nicht genutzt, weil ein besserer institutioneller OA-Weg existierte). Hier existierte kein OA-Weg; die Nutzung folgt dem AR-013-Präzedenzfall und ist in jeder Quellenakte transparent protokolliert. Falls Felix diese Zugriffsklasse enger regeln will, wäre das eine gesonderte Governance-Entscheidung.

## 2. Vollständig gelesene Volltexte

Alle drei. 1974: gesamter Artikel (Repräsentativität, Verfügbarkeit, Anchoring, Diskussion, Summary, References). 1979: gesamter Artikel S. 263–292 (Kritik, Theorie, Wert-/Gewichtungsfunktion, Diskussion, Appendix, References). 1981: gesamter Artikel S. 453–458 (alle zehn Probleme, Diskussion, References/Notes). Kein Abstract-only-Anteil.

## 3. Angelegte/ergänzte Quellenakten

Neu (Duplikatprüfung vorab: keine der drei Quellen existierte als SRC-Objekt; höchste Bestands-ID SRC-0028):

- `02_sources/studies/SRC-0029_tversky_kahneman_1974_judgment_under_uncertainty.md`
- `02_sources/studies/SRC-0030_kahneman_tversky_1979_prospect_theory.md`
- `02_sources/studies/SRC-0031_tversky_kahneman_1981_framing_of_decisions.md`

Jeweils mit vollständigem Zugriffsprotokoll, Quellenklasse A, Grenzen und Präzisierungsbefunden.

## 4. Extrahierte Statements

Vier neue source-grounded Statements (`03_knowledge_base/statements/`), alle direkt aus dem gelesenen Primärtext mit wörtlichen Zitaten:

- **ST-0315** — Wertfunktion: referenzpunktabhängig, S-förmig, steiler für Verluste (SRC-0030). Inkl. Präzisierung: keine 2×-Quantifizierung im 1979-Paper.
- **ST-0316** — Certainty Effect und Reflection Effect (SRC-0030).
- **ST-0317** — Anchoring: Definition, Glücksrad-Experiment (Anker 10/65 → Mediane 25 %/45 %), Anreiz-Robustheit (SRC-0029); Zitate zeichengenau gegen JSTOR-Digitalisat verifiziert.
- **ST-0318** — Framing-Präferenzumkehr bei identischen Optionen (Asian Disease, Surcharge/Discount; SRC-0031).

Keine neuen A-, MEC-, P- oder T-Objekte (Scope-Disziplin; Rule of Three / Canonicalisierung nicht berührt, da keine neuen Mechanismen behauptet werden).

## 5. Betroffene bestehende MECs

Alle drei Zielobjekte wurden ausschließlich um einen Traceability-Abschnitt „AR-007 — Primärquellen-Verankerung/-Prüfung" erweitert:

- **MEC-0002:** 1979 verankert Kerndefinition + Certainty Effect (bislang nur SRC-0003/Practitioner); 1981 verankert den Framing-Anteil der Definition (bislang nur SRC-0010-Sekundärsynthese). Präzisierungsbefund zur 2×-Formulierung dokumentiert (Wortlaut des Erklärung-Abschnitts bewusst nicht verändert — das wäre eine redaktionelle Umformulierung ohne Auftrag).
- **MEC-0012:** Negativbefund dokumentiert — keines der drei Papers enthält das System-1/2-Modell; die 1979-Referenz trägt die Bias-Seite, nicht die Dual-Process-Architektur. Verwechslungswarnung Editing/Evaluation (1979) vs. System 1/2 ergänzt. SRC-0010 bleibt kanonische Dual-Process-Quelle.
- **MEC-0021:** 1974 verankert Definition, Glücksrad-Experiment und (neu aus der Originalquelle) Anreiz-Robustheit. Präzisierungsbefund: 1974 trägt nur Pfad 2 (Insufficient Adjustment), nicht Pfad 1 (S1-Priming/Selective Accessibility — spätere Forschung).

## 6. Machen die Primärquellen die Evidenz nur sauberer tracebar oder ändern sie inhaltlich etwas?

**Sauberer tracebar — keine inhaltliche Änderung.** Kein Widerspruch zwischen Originalquellen und Bestandsobjekten gefunden. Drei Quellenzuordnungs-Präzisierungen (2×-Quantifizierung, Pfad-1-Zuordnung, Dual-Process-Zuordnung) betreffen die Attribution von Aussagen an Quellen, nicht die Aussagen selbst. Zusätzlich gewonnen: die Anreiz-Robustheit des Anchoring (1974) und die Ethik-Aussage zur Frame-Wahl (1981) als direkte Primärquellen-Stützen bestehender Grenzen-/Ethik-Abschnitte. Das im Plan-Ziel erwähnte „potenzielle E-Level-Upgrade auf ‚Primärquelle direkt'" wurde NICHT vollzogen: Die E5-Einstufungen bestehen bereits; eine Kennzeichnungsänderung wäre eine Editorentscheidung und ist fachlich nicht erforderlich.

## 7. Ergibt sich ein Editorentscheid zu P-0002?

**Kein neuer Entscheidungsbedarf — der bestehende bleibt offen und wird geschärft.** Die Primärquellen stützen ausschließlich den allgemeinen Grundmechanismus (MEC-0002-Ebene). Sie enthalten keinerlei Vertriebs-/Kaufentscheidungskontext und liefern damit keine von MEC-0002/SRC-0001 unabhängige zweite Evidenzbasis für P-0002. Der dokumentierte Befund vom 2026-07-13 (P-0002s „E4-Kandidat"-Status nicht eigenständig gerechtfertigt; empfohlene Herausgeberentscheidung offen) bleibt unverändert bestehen — P-0002 wurde auftragsgemäß nicht geändert. Siehe `SCIENTIFIC_DEBT.md`, MEC-0002/P-0002-Sektion, AR-007-Update.

## 8. Grenzen der Übertragung auf Vertrieb/B2B

1. Alle drei Papers arbeiten mit Schätz-/Lotterie-/Fragebogenaufgaben (Studierende, teils Fakultät/Ärzte; Israel/Schweden/USA/Kanada, 1970er–1981) — null Vertriebs-, Verhandlungs- oder B2B-Kaufkontexte. Jede Sales-Anwendung (SPIN Implication Questions, COI, Ackerman-Anchoring, Loss Framing im Pitch) ist Transfer, nicht Befund.
2. Die bestehende E-Level-Differenzierung (E5/E4 Grundmechanismus vs. E3 Vertriebsanwendung vs. E2 Verhandlungsanwendung) bildet genau diese Transferlücke ab und wird durch AR-007 bestätigt.
3. Die bereits dokumentierten Boundary Conditions Individual- vs. Organisationsebene (ED-005: Buying Center, Genehmigungsstufen) gelten unverändert — die Originalquellen messen ausnahmslos Individualentscheidungen.
4. Effektstärken im modernen Sinn fehlen in den Originalquellen; Quantifizierung und Grenzbedingungen stammen aus der späteren, bereits indexierten Literatur (Brown et al. 2024; Schley/Weingarten 2023/2026).
5. Nicht geprüft (außerhalb Scope): spätere Framing-Meta-Analysen (z. B. Kühberger 1998) — offene Vertiefungsmöglichkeit, in SRC-0031 vermerkt.

## 9. Geänderte/neu angelegte Dateien

**Neu (8):** SRC-0029, SRC-0030, SRC-0031 (`02_sources/studies/`); ST-0315, ST-0316, ST-0317, ST-0318 (`03_knowledge_base/statements/`); dieser Bericht (`00_project/AR-007_COMPLETION_REPORT.md`).

**Geändert (6):** `03_knowledge_base/mechanisms/MEC-0002_loss_aversion_and_status_quo_cost.md`, `MEC-0012_dual_process_system1_zu_system2.md`, `MEC-0021_anchoring_mechanismus.md` (je ein AR-007-Erweiterungsabschnitt; MEC-0012 zusätzlich Status-Zeile); `05_research/LITERATURE_INDEX.md` (Sektion A, drei Bemerkungen-Felder); `00_project/SCIENTIFIC_DEBT.md` (AR-007-Status-Update in der MEC-0002/P-0002-Sektion); `00_project/ACADEMIC_RECOVERY_PLAN.md` (AR-007-Status-Update).

**Nicht geändert (auftragsgemäß):** P-0002, Evidenzlevel aller Objekte, Completed-W-Dateien, Templates/Framework. Kein Commit, kein Push.

## 10. Durchgeführte Prüfungen

1. **Pflichtstart:** `PROJECT_BOOTSTRAP.md`, `SESSION_BRIEF.md`, `00_project/NEXT_ACTION.md`, `TASK_TYPES.md` (T11-Routing) vor Arbeitsbeginn gelesen.
2. **Duplikatprüfung:** `02_sources/` (books + studies) vollständig gelistet — keine der drei Quellen existierte als SRC; höchste IDs SRC-0028/ST-0314 bestätigt (keine ID-Kollision).
3. **Bibliografische Verifikation:** alle drei DOIs über Unpaywall/Crossref-Metadaten gegengeprüft (Titel, Autoren, Datum, Journal, Verlag); Autorenreihenfolge 1981 korrigiert (Tversky & Kahneman, nicht Kahneman & Tversky wie im Plan-/Auftragswortlaut).
4. **Zitatverifikation:** Alle in ST-0317 verwendeten 1974-Zitate zeichengenau per Substring-Abgleich gegen das JSTOR-Digitalisat geprüft (Anchoring-Definition, Mediane 25/45, Anker 10/65, Payoff-Satz — alle wortidentisch). 1979-/1981-Zitate direkt aus den gelesenen Digitalisaten übernommen.
5. **Zielobjekt-Abgleich:** MEC-0002/0012/0021 und P-0002 vollständig gelesen; LITERATURE_INDEX Sektion A und SCIENTIFIC_DEBT MEC-0002/P-0002-Sektion gelesen, bevor geschrieben wurde.
6. **Scope-/Regel-Check am Ende:** keine E-Level-Änderung, keine P-0002-Änderung, keine neuen Objekte ohne Plan-Bezug, keine Completed-W-Dateien berührt, kein Commit/Push, keine rekursive Suche außerhalb der erlaubten Verzeichnisse (einzige Listung: `02_sources/` für die auftragsgemäße Duplikatprüfung, plus gezielte Greps in den beiden erlaubten Plandateien).

---

*Erstellt: 2026-07-14 | AR-007 | T11_SCIDEBT | KI-Redaktion Sales Codex (Claude)*
