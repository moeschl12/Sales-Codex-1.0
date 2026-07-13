# PEER REVIEW DECISION REPORT — Sprint 2

**Dokumentklasse:** Governance
**Datum:** 2026-07-01
**Reviewer:** Unabhängiger wissenschaftlicher Gutachter (Journal Reviewer) — `WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md`
**Review-Paket:** Stand nach Sprint 2 (10 Bücher, ~368 Wissensobjekte)
**Sprint:** Academic Recovery Sprint (ARS-0001)
**Editor:** Claude / Cowork (Repository-Editor)
**Freigabe:** Felix (Herausgeber) — ausstehend

---

## Executive Summary

Das wissenschaftliche Gutachten nach Sprint 2 ist inhaltlich präzise, methodisch anspruchsvoll und vergibt die Gesamtnote **B**. Es enthält deutlich mehr Einzelempfehlungen als der Sprint-1-Review, da es sowohl neue Punkte als auch — teils wortgleich — bereits in Sprint 1 entschiedene Punkte (MEC-0006/MEC-0014-Fusion, Meme-Filter/CTX) erneut aufwirft.

Von den identifizierten Kernempfehlungen werden **sechs übernommen** (davon zwei vollständig, vier teilweise/als dokumentierte Kandidaten), **drei abgelehnt** mit expliziter Begründung, und **eine** (Einführung der CTX-Ebene) wird — wie im Auftrag vorgegeben — nicht umgesetzt, sondern ausschließlich als Open Decision dokumentiert.

Diese Entscheidung stützt sich ausschließlich auf: Operating Manual, Canonical Knowledge Model, Repository-Regeln (Arbeitsverbote, Abschnitt 8) und den bisherigen wissenschaftlichen Stand (Reifegradbericht, SPR-0002, Scientific Debt). Zusätzlich flossen die verifizierten Befunde aus `ACADEMIC_RECOVERY_REPORT.md` (Research Pack 1) ein, wo sie eine Entscheidung direkt stützen oder einschränken.

**Gesamturteil:** Das Gutachten ist wissenschaftlich fundiert und in seiner Kernkritik (B2B-Transferlücke, proprietäre Datenbasis, W-001-Blockade) zutreffend. Zwei Einzelbeispiele des Gutachtens (P-0038/MEC-0013-"Redundanz", MEC-0006/MEC-0014-Fusion) sind bei genauer Prüfung nicht haltbar bzw. bereits entschieden. Der Sales Codex ist bereit für die im Gutachten selbst geforderte Konsequenz: einen reinen Academic-Recovery-Sprint statt weiterer Practitioner-Buchanalyse.

---

## Einzelentscheidungen

---

### Empfehlung 1 — Fusion MEC-0006 und MEC-0014 (erneut)

**Empfehlung des Reviewers:** Zugunsten theoretischer Sparsamkeit (Ockhams Rasiermesser) sollen MEC-0006 (Social Proof) und MEC-0014 (Konsens in Gruppen) fusioniert werden — beide reduzierten kognitive Last und wahrgenommenes Risiko durch Orientierung an Mehrheiten (Abschnitt 3).

**Entscheidung: Ablehnen (bestätigt aus Sprint 1)**

**Begründung:** Diese Empfehlung wurde in Sprint 1 (Empfehlung 4, `99_archive/00_project_history/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_001.md`) bereits mit identischer Begründung abgelehnt: Das CKM definiert Mechanismen-Identität über den vollständigen kausalen Pfad (Stimulus X → Prozess Y → Reaktion Z), nicht über den Prozess Y allein. MEC-0006 (Stimulus: externes Marktverhalten → Korrektheitsbewertung) und MEC-0014 (Stimulus: interner Organisationskonsens → Risikoverteilung/Absicherung) haben unterschiedliche Stimuli und unterschiedliche Reaktionen — nach CKM-Regel "Gleicher Prozess Y, aber verschiedene Stimuli → Getrennt halten" bleiben sie getrennt.

Die in ARS-0001 an MEC-0014 ergänzten Theorie-Referenzen (Webster & Wind 1972, Sheth 1973, Eisenhardt 1989 — siehe `ACADEMIC_RECOVERY_REPORT.md` Abschnitt 3.5) verstärken die Trennschärfe zusätzlich: MEC-0014 erhält damit eine eigenständige theoretische Anbindung an Agency-Risiko, die MEC-0006 nicht hat. Eine Fusion würde diese neu dokumentierte Differenzierung wieder einebnen.

**Betroffene Repository-Objekte:** `00_project/review_queue.md` (Update-Vermerk ergänzt)

**Herausgeber-Entscheidung weiterhin erforderlich**, wie in Sprint 1 dokumentiert. Diese Ablehnung ist eine Editor-Empfehlung, keine finale Schließung der Frage.

---

### Empfehlung 2 — Fehlende Mechanismen: Principal-Agent-Theorie und Pfadabhängigkeit

**Empfehlung des Reviewers:** Bezogen auf die Realität des B2B-Vertriebs fehlen fundamentale Mechanismen der Anreizökonomie (Principal-Agent-Theorie) sowie der Pfadabhängigkeit (organisationale Sunk-Cost-Effekte, nicht nur individuelle) (Abschnitt 3).

**Entscheidung: Teilweise übernehmen**

**Begründung:** Der Befund ist zutreffend — der Codex hat aktuell kein Mechanismus-Objekt, das organisationale Agency-Dynamik explizit modelliert. MEC-0014 beschreibt Konsensverhalten, aber nicht das zugrunde liegende Agency-Risiko-Kalkül des einzelnen Entscheiders.

Für den Principal-Agent-Teil wurde in ARS-0001 bereits eine erste, dokumentierte Antwort umgesetzt: Eisenhardt (1989) als Theorie-Referenz an MEC-0014 ergänzt (siehe Empfehlung 1). Eine vollständige Auflösung (eigenständiges MEC "Principal-Agent-Risiko im Buying Center") erfordert Primärtext-Extraktion nach Operating-Manual-Prozess und wird nicht in diesem Schritt vorgenommen (Begründung: Nachvollziehbarkeits-Standard, siehe `ACADEMIC_RECOVERY_REPORT.md` Abschnitt 1).

Für Pfadabhängigkeit/organisationale Sunk-Cost-Effekte existiert noch keine geprüfte Literatur im Repository. Dies wird als offene Lücke anerkannt und in den Academic Recovery Plan aufgenommen — keine Objekterstellung ohne Quellenbasis.

**Betroffene Repository-Objekte:** `03_knowledge_base/mechanisms/MEC-0014_konsens_als_kaufsicherheit_in_gruppen.md` (bereits erweitert, s.o.), `00_project/ACADEMIC_RECOVERY_PLAN.md` (neue Literaturpriorität)

---

### Empfehlung 3 — "Redundanz" zwischen P-0038 und MEC-0013

**Empfehlung des Reviewers:** Konstrukte wie P-0038 (Problem Finding, Pink) und MEC-0013 (Insight-Disruption/Reframing, Challenger) weisen "gravierende theoretische Schnittmengen" auf; dies belege eine "Begriffsinflation" durch zu starke Orientierung an Autoren-Nomenklatur statt am psychologischen Konstrukt (Abschnitt 5).

**Entscheidung: Ablehnen**

**Begründung:** Dies ist ein Kategorienfehler im Gutachten. P-0038 ist ein **Prinzip** (Handlungsableitung), MEC-0013 ist ein **Mechanismus** (kausale Erklärung) — unterschiedliche Objekttypen mit unterschiedlicher Funktion im Wissensmodell (Codex Methodology, Grundprinzip 3: "Trennung von Ebenen"). P-0038 referenziert MEC-0013 explizit unter "Verknüpfte Objekte" — das ist keine Redundanz, sondern die vom CKM vorgesehene "Erklärt"-Beziehung (CKM Abschnitt 8: "Mechanismus erklärt Prinzip", dokumentiert im `Mechanismus`-Feld des P-Objekts mit MEC-ID).

Ein Prinzip, das seinen erklärenden Mechanismus korrekt zitiert, ist nach CKM kein Duplikat dieses Mechanismus — im Gegenteil, das wäre exakt die geforderte Praxis (Operating Manual Schritt 5: "Verknüpfung mit MEC-IDs, nicht nur Freitextnamen"). Der vom Gutachten konstatierte Befund widerspricht damit der eigenen Methodik des Codex, nicht einer Schwäche des Codex.

Das übergeordnete Anliegen des Reviewers (Risiko der Begriffsinflation durch Autoren-Nomenklatur) bleibt für andere Fälle prüfenswert — siehe Empfehlung 4 — aber dieses konkrete Beispiel stützt die These nicht.

**Betroffene Repository-Objekte:** keine

---

### Empfehlung 4 — Generelles Begriffsinflations-Risiko (4%-Canonicalization-Rate)

**Empfehlung des Reviewers:** Die niedrige Canonicalization-Rate (4% in Sprint 2) sei ein methodisches Warnsignal für Overfitting; das System orientiere sich zu stark an Autoren-Nomenklatur statt am dahinterliegenden Konstrukt (Abschnitt 5).

**Entscheidung: Teilweise übernehmen**

**Begründung:** Die niedrige Fusionsrate ist zunächst eine **beabsichtigte Konsequenz** der CKM-Identitätsregel (vollständiger kausaler Pfad X→Y→Z muss übereinstimmen, nicht nur thematische Ähnlichkeit) — das ist in Abschnitt 2 des CKM explizit als Faustregel verankert ("Im Zweifel getrennt halten"). Zudem hat SPR-0002 alle sechs neuen Sprint-2-Mechanismen einem expliziten, nachvollziehbar begründeten Fusionscheck unterzogen (`SPR-0002_SYNTHESEBERICHT.md`, Abschnitt "Canonicalisierungs-Review Sprint 2") — das ist keine unreflektierte Übernahme von Autoren-Terminologie, sondern dokumentierte Einzelfallprüfung.

Das konkrete Beispiel des Reviewers (P-0038/MEC-0013) ist widerlegt (Empfehlung 3). Dennoch ist die grundsätzliche Sorge — dass linguistische Nuancen von Practitioner-Autoren die Trennschärfe verwässern könnten — nicht identisch mit, aber verwandt zu dem bereits dokumentierten Risiko SD-SYS-003 (Meme-Replikation, aus Sprint 1, offen in OD-006). Eine strukturelle Änderung der Canonicalization-Schwelle wäre eine Framework-Änderung (CKM Abschnitt 5) und damit laut Operating Manual Abschnitt 8 nicht eigenständig umsetzbar.

**Maßnahme:** Keine Schwellenänderung. Empfehlung an Herausgeber: OD-006 (Meme-Filter) inhaltlich um die Frage "Autoren-Nomenklatur vs. Konstrukt" zu erweitern, da beide Sorgen denselben Kern haben (scheinbare vs. echte Eigenständigkeit von Wissensobjekten).

**Betroffene Repository-Objekte:** keine strukturelle Änderung; Verweis in `OPEN_DECISIONS.md` OD-006 ergänzt (s.u.)

---

### Empfehlung 5 — Neues Meta-Prinzip: Asymmetrische Risikoverteilung im Buying Center

**Empfehlung des Reviewers:** Ein Meta-Prinzip fehlt, das beschreibt, dass das persönliche Karriererisiko des internen Champions strukturell schwerer wiegt als der rationale Unternehmensgewinn — konvergent aus SPIN, Challenger und JOLT (Abschnitt 4).

**Entscheidung: Teilweise übernehmen (als dokumentierter Kandidat)**

**Begründung:** Die Empfehlung ist wissenschaftlich gut begründet und erfüllt die formale Mindestanforderung für Meta-Prinzipien (≥3 unabhängige Quellen, hier bereits vollständig im Codex verarbeitete Primärquellen). Anders als bei extern zugelieferter, nur abstract-geprüfter Literatur (Research Pack 1) besteht hier grundsätzlich eine Statement-Basis im Repository.

Eine sofortige Anlage als P-Objekt würde jedoch den in Operating Manual Schritt 5 vorgeschriebenen Prozess (Vier-Pflichtfragen, Evidenzklasse mit Begründung, Abgrenzung zu MEC-0014 und A-0019, vollständiger Quervergleich mit allen bestehenden P-Objekten) überspringen. Das widerspricht der Projektregel "Priorität hat immer die Qualität der Wissensbasis, nicht die Geschwindigkeit."

**Maßnahme:** Als Kandidat in `review_queue.md` dokumentiert, mit betroffenen Objekten und Bearbeitungsempfehlung für SPR-0003. Nicht als P-Objekt angelegt.

**Betroffene Repository-Objekte:** `00_project/review_queue.md`

---

### Empfehlung 6 — Bestätigung Timing/Bildung der Meta-Prinzipien

**Empfehlung des Reviewers:** Die Induktion der vier Meta-Prinzipien nach 10 Büchern war zeitlich präzise gewählt; keine Kritik (Abschnitt 4).

**Entscheidung: Bestätigung ohne Änderung**

**Begründung:** Keine Handlung erforderlich — analog zu Sprint 1, Empfehlung 5.

**Betroffene Repository-Objekte:** keine

---

### Empfehlung 7 — Fehlende Scientific-Debt-Kategorie: Publication Bias kommerzieller Studien

**Empfehlung des Reviewers:** Der "Publication Bias" der zugrunde liegenden kommerziellen Studien (CEB/Challenger N=6.000, JOLT/Tethr) fehlt als explizite Kategorie in der Debt-Matrix; wird bisher nur mild unter "proprietäre Methodik" subsumiert (Abschnitt 6).

**Entscheidung: Übernehmen**

**Begründung:** Diese Kritik ist präzise und direkt umsetzbar — analog zu Sprint 1, Empfehlung 3 (dort wurde "Proprietäre-Studien-Validierung" als neue SD-Kategorie ergänzt; das ist ein etablierter Präzedenzfall für Erweiterungen der Scientific-Debt-Kategorientabelle als operative, nicht framework-ändernde Maßnahme). "Replikationsrisiko" (bestehende Kategorie) beantwortet die Frage "wurde es unabhängig wiederholt?" — "Publication Bias" beantwortet die andere, eigenständige Frage "gab es einen strukturellen Anreiz zur selektiven Berichterstattung?". Beide sind analytisch trennbar und beide relevant.

Allgemeine akademische Literatur zu Industry-Sponsorship-Bias (primär aus der medizinischen Forschung, aber strukturell übertragbar) stützt die Plausibilität des Risikos, ohne dass eine sales-spezifische Studie zu CEB/Tethr konkret vorliegt — dies wird als Grenze der Aussage explizit markiert.

**Betroffene Repository-Objekte:** `00_project/SCIENTIFIC_DEBT.md` (neue Kategorie „Publication Bias (kommerzielle Studien)" + SD-SYS-004 mit zwei Einträgen)

---

### Empfehlung 8 — Fehlender Widerspruch: Kognitive Leichtigkeit vs. Rational Drowning

**Empfehlung des Reviewers:** Der Konflikt zwischen "Kognitiver Leichtigkeit" (Kahneman, System 1 bevorzugt geringe Last) und "Rational Drowning/Challenger" (bewusste Maximierung kognitiver Last und Dissonanz) fehle und werde fälschlich als "keine echte Spannung" abgetan (Abschnitt 8).

**Entscheidung: Teilweise übernehmen**

**Begründung:** Bei Prüfung der bestehenden Dokumente (`contradiction_matrix.md`, `SPR-0002_SYNTHESEBERICHT.md`) ist diese exakte Spannung — kognitive Leichtigkeits-**Präferenz** vs. bewusste kognitive Last-**Maximierung als Strategie** — tatsächlich nicht explizit erfasst. Was existiert, ist Spannungsfeld 3 aus SPR-0002 ("Tactical Empathy vs. Provokation", MEC-0010 vs. MEC-0013), das eine verwandte, aber nicht identische Frage behandelt (emotionale Amygdala-Regulation vs. kognitive Dissonanz-Erzeugung, dort als Sequenz aufgelöst). Die Behauptung des Reviewers, der Codex habe diese *spezifische* Spannung "fälschlich abgetan", trifft nicht exakt zu — sie wurde schlicht nicht in dieser Form behandelt.

Der inhaltliche Punkt ist dennoch berechtigt: Ein potenzieller Widerspruch zwischen MEC-0012 (Cognitive Ease als S1-Präferenz) und MEC-0013/Rational-Drowning (gezielte Erhöhung kognitiver Last) ist real und bisher nicht dokumentiert.

**Maßnahme:** `contradiction_matrix.md` ist ein abgeschlossenes Sprint-1-Artefakt (Status: Abgeschlossen) und wird nicht rückwirkend editiert — dieselbe Konvention, nach der SPR-0002 neue Spannungsfelder in einem neuen Dokument statt durch Rückwirkung in Sprint-1-Dateien behandelt hat. Der Kandidat wird stattdessen in `SCIENTIFIC_DEBT.md` dokumentiert und für die nächste Synthese-Sprint-Runde (SPR-0003) als W-006-Kandidat vorgemerkt.

**Betroffene Repository-Objekte:** `00_project/SCIENTIFIC_DEBT.md`

---

### Empfehlung 9 — Forschungsagenda: Verbeke, Johnston & Lewin, Tuli/Kohli/Bharadwaj

**Empfehlung des Reviewers:** Für die drei genannten Forschungsrichtungen (B2B-Verhaltensökonomie-Replikation, organisationale Entscheidungsforschung, Sequenzierungs-Paradoxon) werden konkrete Literaturhinweise gegeben (Abschnitt 9).

**Entscheidung: Übernehmen**

**Begründung:** Direkt umsetzbar und wissenschaftlich einschlägig — alle drei Quellen wurden verifiziert (Verbeke bereits vollständig verarbeitet in ARS-0001/Research Pack 1, siehe `ACADEMIC_RECOVERY_REPORT.md`; Johnston & Lewin und Tuli/Kohli/Bharadwaj verifiziert, aber noch nicht inhaltlich verarbeitet).

**Betroffene Repository-Objekte:** `00_project/ACADEMIC_RECOVERY_PLAN.md` (Priorität 1 und 2)

---

### Empfehlung 10 — Kategorie C: Geografisch-kulturelle Monokultur

**Empfehlung des Reviewers:** Ausschließliche Fokussierung auf westliche/nordamerikanische Literatur schränkt die externe Validität drastisch ein (Abschnitt 7, 10).

**Entscheidung: Bestätigung, bereits dokumentiert**

**Begründung:** Dieser Befund ist im Codex bereits umfassend erfasst (Reifegradbericht 1.5 "Generalisierbarkeit C+", mehrere SD-Einträge zu kultureller Generalisierung, u.a. SD-B006-003, SD-B009-002). Der Reviewer selbst stuft dies als "Kategorie C — Optional" ein. Keine neue Repository-Änderung nötig; als niedrige Priorität in den Academic Recovery Plan übernommen.

**Betroffene Repository-Objekte:** keine (bereits dokumentiert)

---

### Empfehlung 11 — Formale Schließung von W-001 durch Problemreife-Hypothese (WENN…DANN…)

**Empfehlung des Reviewers:** Das Paradoxon müsse über eine Bedingungslogik formalisiert werden ("WENN Problemreife niedrig, DANN Teach First; WENN Problemreife hoch, DANN Diagnose First") (Abschnitt 11, "Nächste Schritte" #2).

**Entscheidung: Ablehnen (in dieser Form, jetzt)**

**Begründung:** Wie in `ACADEMIC_RECOVERY_REPORT.md` Abschnitt 4 im Detail dokumentiert, liefert die geprüfte Literatur (Franke & Park 2006; Verbeke et al. 2010/2011) nur **indirekte, analogieschlüssige** Stützung für die allgemeine Logik "Anpassung an Käufersignale wirkt" — keine der Quellen testet die spezifische Dreistufung der Problemreife-Hypothese oder eine Teach-First/Diagnose-First-Bedingungslogik direkt. Eine formale WENN-DANN-Regel jetzt einzuführen würde gegen die Projektregel "Keine unbelegte Verallgemeinerung" verstoßen und den Quellenprinzip-vs-Codex-Prinzip-Standard (Operating Manual Abschnitt 5: mindestens drei unabhängige Quellen mit direktem Bezug zur konkreten Aussage) unterlaufen.

Die Forschungsrichtung selbst wird nicht abgelehnt — im Gegenteil, sie ist jetzt literaturgestützt (statt rein redaktionell) im Academic Recovery Plan priorisiert. Abgelehnt wird ausschließlich die **vorzeitige Formalisierung als Codex-Regel**.

**Betroffene Repository-Objekte:** keine Änderung an W-001/contradiction_matrix.md; Priorität im Academic Recovery Plan

---

### Empfehlung 12 — Einführung der CTX-Ebene

**Empfehlung des Reviewers:** Jedes P und T müsse zwingend mit strukturellen Kontextattributen versehen werden (Abschnitt 2, 10, 11).

**Entscheidung: Nicht umgesetzt — nur Open Decision (gemäß explizitem Auftrag)**

**Begründung:** Der Auftrag für ARS-0001 schreibt ausdrücklich vor, die CTX-Ebene nicht einzuführen, sondern ausschließlich ihre wissenschaftliche Rechtfertigung zu bewerten und als Open Decision zu dokumentieren. Diese Bewertung erfolgt in `OPEN_DECISIONS.md` OD-007. Eine Einführung wäre ohnehin eine Framework-Änderung (neues Pflichtfeld für alle P-/T-Objekte) und laut Operating Manual Abschnitt 8 nicht eigenständig umsetzbar.

**Betroffene Repository-Objekte:** `00_project/OPEN_DECISIONS.md` (OD-007 neu)

---

## Übernommene Änderungen

| # | Empfehlung | Entscheidung | Betroffene Objekte | Status |
|---|---|---|---|---|
| 2 | Principal-Agent/Pfadabhängigkeit | Teilweise übernehmen | MEC-0014, ACADEMIC_RECOVERY_PLAN | Umgesetzt (Theorie-Referenzen) / Plan offen |
| 4 | Begriffsinflations-Risiko | Teilweise übernehmen | OPEN_DECISIONS OD-006 (Verweis ergänzt) | Umgesetzt |
| 5 | Meta-Prinzip Risikoverteilung | Teilweise übernehmen (Kandidat) | review_queue.md | Umgesetzt |
| 7 | Publication-Bias-Kategorie | Übernehmen | SCIENTIFIC_DEBT.md (SD-SYS-004) | Umgesetzt |
| 8 | Kognitive Leichtigkeit vs. Rational Drowning | Teilweise übernehmen | SCIENTIFIC_DEBT.md (W-006-Kandidat) | Umgesetzt |
| 9 | Literaturagenda (Verbeke/Johnston&Lewin/Tuli) | Übernehmen | ACADEMIC_RECOVERY_REPORT.md, ACADEMIC_RECOVERY_PLAN.md | Verbeke umgesetzt; Rest priorisiert |
| 12 | CTX als Open Decision | Wie beauftragt umgesetzt | OPEN_DECISIONS.md (OD-007) | Umgesetzt |

---

## Bewusst nicht übernommene Empfehlungen

| # | Empfehlung | Entscheidung | Begründung |
|---|---|---|---|
| 1 | Fusion MEC-0006/MEC-0014 | Abgelehnt (bestätigt) | CKM-Identitätsregel; bereits in Sprint 1 entschieden; durch ARS-0001-Ergänzungen weiter untermauert |
| 3 | "Redundanz" P-0038/MEC-0013 | Abgelehnt | Kategorienfehler — P zitiert MEC korrekt als Erklärung, keine Duplikation |
| 11 | Formale WENN-DANN-Schließung W-001 | Abgelehnt (jetzt) | Literaturlage liefert nur indirekte Stützung; Formalisierung würde Evidenzstandard unterlaufen |

---

## Offene Forschungsfragen (neu oder bestätigt)

1. **Direkter empirischer Test der Problemreife-Hypothese:** Existiert eine Studie, die Insight-First vs. Diagnose-First unter Kontrolle des Käufer-Problemreifegrads direkt vergleicht? Nach ARS-0001-Recherche weiterhin nicht bekannt (siehe `ACADEMIC_RECOVERY_REPORT.md`).
2. **Principal-Agent im Buying Center:** Rechtfertigt eine vollständige Eisenhardt-Auswertung ein eigenständiges MEC?
3. **Kognitive Leichtigkeit vs. Rational Drowning:** Ist dies eine echte Spannung oder — analog zu Spannungsfeld 3 — durch Sequenzierung/Kontext auflösbar?
4. **Meta-Prinzip Risikoverteilung im Buying Center:** Vollständige Ausarbeitung nach Operating-Manual-Prozess aussstehend.
5. **Pfadabhängigkeit/organisationale Sunk-Cost-Effekte:** Keine Literatur im Repository geprüft — vollständig offen.
6. **Vollständige Autorenverifikation** für Marcos-Cuevas et al. (2023) und "Advancing Value-Based Selling Research" (2023) — siehe `ACADEMIC_RECOVERY_REPORT.md` Abschnitt 2.

---

## Changelog

| Datum | Objekt | Änderungstyp | Beschreibung |
|---|---|---|---|
| 2026-07-01 | SCIENTIFIC_DEBT.md | Ergänzung | Verbeke-Eintrag präzisiert; neuer Abschnitt „ARS-0001 Research Pack 1" (6 Einträge); neue Kategorie „Publication Bias (kommerzielle Studien)"; SD-SYS-004 (2 Einträge); W-006-Kandidat dokumentiert |
| 2026-07-01 | MEC-0014 | Erweiterung (CKM 4.1) | Abschnitt „Ergänzende Theorie-Referenzen (ARS-0001)" — Webster & Wind 1972, Sheth 1973 (korrigiert von „1987"), Eisenhardt 1989. E-Level unverändert. |
| 2026-07-01 | review_queue.md | Ergänzung | MEC-0006/0014-Fusionskandidat mit ARS-0001-Update versehen; neuer MEC-Kandidat „Adaptive Selling Behavior"; neuer Meta-Prinzip-Kandidat „Asymmetrische Risikoverteilung im Buying Center" |
| 2026-07-01 | ACADEMIC_RECOVERY_REPORT.md | Neu angelegt | Vollständige Prüfung und Integration von Research Pack 1 |
| 2026-07-01 | PEER_REVIEW_DECISION_REPORT_SPRINT_002.md | Neu angelegt | Dieses Dokument |
| 2026-07-01 | OPEN_DECISIONS.md | Ergänzung (separat) | OD-007 CTX-Ebene; OD-006 um Begriffsinflations-Aspekt ergänzt |
| 2026-07-01 | ACADEMIC_RECOVERY_PLAN.md | Neu angelegt (separat) | Priorisierte Literatur-Roadmap für ARS-0001 Fortsetzung |

---

## Abschlussbewertung: Reifegradsprung B → A-?

**Frage:** Kann der Sales Codex nach dem Academic Recovery Sprint (ARS-0001) den wissenschaftlichen Reifegrad von B auf A- anheben?

**Einschätzung: Noch nicht — ARS-0001 schafft die Voraussetzungen dafür, vollzieht den Sprung aber nicht.**

**Begründung:**

Ein Reifegrad-Sprung von B auf A- würde eine substanzielle Verbesserung mehrerer der sechs bewerteten Dimensionen erfordern (vgl. `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`, Abschnitt 2). ARS-0001 hat in dieser Sitzung geleistet:

- **Prozess- und Integritätsgewinn:** Alle acht Quellen aus Research Pack 1 wurden unabhängig verifiziert (eine Zitationskorrektur dokumentiert statt stillschweigend übernommen); zwei Gutachten-Empfehlungen wurden mit fachlicher Begründung abgelehnt (P-0038/MEC-0013-Kategorienfehler, vorschnelle W-001-Formalisierung) statt reflexhaft übernommen; keine Wissensobjekte wurden ohne Primärtextbasis neu angelegt. Das ist echte methodische Reife und stärkt die bereits mit A- bewertete Dimension „Scientific Debt Management" weiter.
- **Transparenzgewinn:** Neue Scientific-Debt-Kategorie (Publication Bias), neue dokumentierte Kandidaten (Meta-Prinzip, W-006, MEC-Kandidat Adaptive Selling), CTX-Bewertung mit echter akademischer Stützung (Marcos-Cuevas et al. 2023) statt bloßer Meinungsäußerung.
- **Was NICHT geleistet wurde:** Keine der beiden Tier-1-kritischen Schwächen aus dem Reifegradbericht wurde inhaltlich aufgelöst. W-001 bleibt ungelöst — jetzt mit einer literaturgestützten, aber weiterhin nur indirekten Analogie (Adaptive-Selling-Meta-Analysen), nicht mit einem direkten empirischen Test. Die Generalisierbarkeits-Schwäche (C+, schwächste Dimension) wurde nicht durch neue Primärtextintegration verbessert — die B2B-spezifischen Meta-Analysen (Ohiomah et al., Marcos-Cuevas et al.) liegen weiterhin nur auf Abstract-Ebene vor. Kein einziges bestehendes MEC hat ein E-Level-Upgrade auf Basis neuer, vollständig verarbeiteter Primärquellen erhalten — die einzige Erweiterung (MEC-0014) fügt Theorie-Referenzen hinzu, ohne das Evidenzlevel zu ändern (bewusst, s.o.).

**Konsequenz für die Bewertung:** Ein Peer Reviewer, der ausschließlich auf Objektebene prüft (E-Level, neue Statements, aufgelöste Widersprüche), würde nach diesem Sprint keine Verbesserung der Kern-Evidenzbasis feststellen — nur eine verbesserte Prozess- und Dokumentationsqualität. Reifegrad-Sprünge im hier verwendeten Bewertungsschema sind an inhaltliche, nicht nur prozedurale Fortschritte gebunden.

**Realistische Einschätzung:** Der Codex bewegt sich von **B in Richtung B+**, primär durch die gestärkte Scientific-Debt-Disziplin und die jetzt konkret geplante (statt nur postulierte) Schließung der Kernlücken. **A- ist erreichbar**, aber erst nach Umsetzung von mindestens AR-001 und AR-003 bis AR-005 aus `ACADEMIC_RECOVERY_PLAN.md` mit vollständiger Primärtext-Verarbeitung (nicht Abstract-Ebene) — insbesondere: entweder eine belastbare Auflösung oder eine gut begründete, literaturgestützte Nicht-Auflösung von W-001, sowie mindestens ein neues oder substanziell gestärktes MEC mit akademischer (nicht-proprietärer) Primärquellenbasis für die B2B-Buying-Center-Dynamik.

Diese Einschätzung selbst folgt der Projektregel „Priorität hat immer die Qualität der Wissensbasis, nicht die Geschwindigkeit": Eine optimistischere Eigenbewertung wäre nicht durch die tatsächlich vorgenommenen Änderungen gedeckt.

---

*Erstellt: 2026-07-01 | ARS-0001 | KI-Redaktion Sales Codex | Freigabe durch Felix ausstehend*
