# CODEX AUDIT 2026-07 — Vollständiger wissenschaftlicher Repository-Audit

**Dokumentklasse:** Audit / Reference
**Auditor:** KI-Redaktion Sales Codex, in Rolle als unabhängiger wissenschaftlicher Auditor
**Stichtag:** 2026-07-01
**Methodik:** Ausschließlich lesende Prüfung des gesamten Repositorys (keine Änderungen, keine neuen Wissensobjekte, keine Framework-Eingriffe)
**Grundlage:** Vollständige Sichtung von 03_knowledge_base (alle sechs Objektklassen), 04_book_analysis (10 Bücher), 00_project (alle Governance-, Sprint- und Debt-Dokumente), 01_framework (Methodik, Templates, Wissensmodell), 05_research/LITERATURE_INDEX.md, sowie stichprobenartige Vollprüfung einzelner Objekte gegen ihre eigenen Evidenzfelder.

---

# 1. Executive Summary

## Gesamtzustand

Der Sales Codex ist nach zehn Buchanalysen, zwei vollständigen Sprints, einem externen wissenschaftlichen Gutachten, zwei Peer-Review-Zyklen und einem zweiphasigen Academic Recovery Sprint ein ungewöhnlich reifes, selbstkritisches Wissenssystem für ein Projekt dieser Art. Es verfügt über eine durchgängige Objekt-Hierarchie (ST → A → MEC → P → T → MOD), ein funktionierendes Evidenzsystem (E1–E5), eine aktiv geführte Scientific-Debt-Matrix und eine Kultur der Selbstkorrektur, die in drei aufeinanderfolgenden Prüfzyklen tatsächlich zu Herabstufungen (MEC-0010, MEC-0011, MEC-0012/MacLean-Entfernung) und nicht nur zu Bestätigungen geführt hat.

Der Codex ist zugleich noch nicht in einem Zustand, der eine Version 1.0 im Sinne eines belastbaren, extern verteidigungsfähigen Wissenssystems rechtfertigt. Der zentrale methodische Widerspruch W-001 (Teach First vs. Diagnose First) ist seit Sprint 1 unaufgelöst und blockiert nach eigener und externer Einschätzung die operative Aussagekraft der gesamten P-Ebene. Die B2B-Kernaussagen (SPIN/Huthwaite, Challenger/CEB, JOLT/Tethr) beruhen weiterhin überwiegend auf proprietären, nicht unabhängig replizierten Datensätzen. Und dieser Audit deckt zusätzlich eine Reihe bislang nicht dokumentierter Konsistenzlücken auf (siehe unten), die in drei vorherigen Prüfzyklen nicht aufgefallen sind.

## Wichtigste Stärken

Der Codex verankert seinen psychologischen Kern (Verlustaversion, Dual-Process, Anchoring, Kontrasteffekt, Choice Overload) direkt in nobelpreisgewichteter Primärliteratur (Kahneman/Tversky) statt in Sekundärzitaten, und hat diese Verankerung durch zwei weitere Recherche-Phasen (Academic Recovery Sprint, Research Packs 1–4) mit websuchverifizierten Meta-Analysen (Schley & Weingarten 2023, Brown et al. 2024) weiter unterfüttert. Die vier induktiv abgeleiteten Meta-Prinzipien (P-S1-001 bis P-S1-004) sind eine genuine Syntheseleistung, die in keinem Einzelbuch so vorkommt, und weisen mit QK-6 bis QK-8+ die höchste Quellen-Konvergenz im gesamten Repository auf. Die Scientific-Debt-Praxis ist vorbildlich: Unsicherheit wird nicht geglättet, sondern mit Priorität, Kategorie und Objektbezug systematisch geführt (56 Einzeleinträge über 9 Bücher plus 6 systemische SD-SYS-Cluster).

## Größte Risiken

Erstens: W-001 bleibt nach drei Prüfzyklen ungelöst und ist — wie der externe Gutachter zutreffend feststellt — die „Sollbruchstelle" des gesamten methodischen Oberbaus. Zweitens: Die B2B-Kernmethodik hängt an drei proprietären, kommerziell interessierten Datensätzen (Huthwaite/SPIN, CEB/Challenger, Tethr/JOLT) ohne unabhängige Peer-Review-Replikation — ein strukturelles Publication-Bias-Risiko, das bisher nur dokumentiert, nicht reduziert wurde. Drittens — und das ist ein Neubefund dieses Audits: Es existiert eine bislang unentdeckte Synchronisationslücke zwischen Mechanismus-Objekten und den auf ihnen aufbauenden Techniken. Als MEC-0010 und MEC-0011 im Peer Review Sprint 1 von E3 auf E2 herabgestuft wurden, wurden die davon abhängigen Techniken T-0012 (Mirroring) und T-0013 (Labeling) nicht mit herabgestuft — sie tragen weiterhin E3. Zusätzlich fehlt bei neun Techniken (T-0019 bis T-0034, überwiegend aus B-0006/JOLT und B-0007/Getting to Yes) und acht Prinzipien (P-0027 bis P-0034, gleiche Bücher, plus alle vier P-S1-Meta-Prinzipien) das Evidenzklassifikations-Feld vollständig.

## Wichtigste Handlungsempfehlungen

Vor einer Version 1.0 sollten in dieser Reihenfolge geschlossen werden: (1) die neu entdeckte Evidenzlevel-Synchronisationslücke (T-0012/T-0013 und die fehlenden Evidenzfelder bei B-0006/B-0007-Objekten) als reine Konsistenzkorrektur ohne inhaltliche Neubewertung; (2) AR-001/AR-002 aus dem Academic Recovery Plan (direkter Test der Problemreife-Hypothese bzw. Publication-Bias-Klärung); (3) mindestens eine der acht offenen Herausgeber-Entscheidungen (OD-001 bis OD-008) tatsächlich final entscheiden — aktuell ist keine einzige als „DONE" markiert.

## Gesamtnote

**B+**

**Begründung:** Das letzte vollständige externe Gutachten (Stand nach Sprint 2, `WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md`) vergab die Note **B** mit der expliziten Bedingung, dass ein reiner Academic-Recovery-Sprint (keine weiteren Practitioner-Bücher) erfolgen müsse. Dieser Sprint hat in zwei Phasen plus einer gezielten Einzelprüfungsrunde (dieser Session vorausgehend) tatsächlich stattgefunden: acht bis elf externe akademische Quellen wurden websuchverifiziert integriert (u. a. Schley & Weingarten 2023, Brown/Imai/Vieider/Camerer 2024, Chartrand & Bargh 1999, Taylor & Thomas 2008, Ireland & Henderson 2014), eine Zitationskorrektur wurde transparent dokumentiert statt stillschweigend verbessert, und ein neuer Tier-1-Literaturkandidat (Tversky & Shafir 1992) wurde identifiziert, der direkt auf die Publication-Bias-Schwäche von B-0006 (JOLT) zielt. Das ist echte, nachprüfbare Bewegung gegenüber dem B-Zustand — der eigene Peer-Review-Report nach Phase 1 sprach bereits von „B in Richtung B+" (`PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`, Abschlussbewertung), und dieser Audit bestätigt diese Einschätzung unabhängig.

Der Codex verdient jedoch **nicht mehr** als B+, und insbesondere **kein A-**, aus drei Gründen: Erstens wurde keiner der beiden Tier-1-kritischen Punkte (W-001, Publication-Bias-Klärung CEB/Challenger/Tethr) inhaltlich aufgelöst — es gibt bislang nur Literaturkandidaten, keine verarbeiteten Primärtexte für diese beiden Kernlücken. Zweitens hat dieser Audit selbst neue, in drei vorherigen Prüfzyklen unentdeckte Konsistenzlücken aufgedeckt (Evidenzlevel-Desynchronisation T-0012/T-0013, fehlende Evidenzfelder bei 17 Objekten, E5-Zähler-Diskrepanz zwischen Reifegradbericht und tatsächlichen Objektwerten — siehe Kapitel 4) — das zeigt, dass die bisherige Prüfpraxis sich stark auf die MEC-Ebene konzentriert hat und die nachgelagerten P-/T-Ebenen nicht mit gleicher Sorgfalt mitgeprüft wurden. Drittens bleiben 8 von 8 Open Decisions unentschieden; ein Wissenssystem auf dem Weg zu Version 1.0 sollte nicht mit einer vollständig offenen Entscheidungs-Pipeline in die Konsolidierung gehen.

---

# 2. Repository-Statistiken

| Kategorie | Anzahl | Quelle/Nachweis |
|---|---|---|
| Bücher analysiert (B-0001–B-0010) | **10** | `04_book_analysis/` (10 Ordner), `02_sources/books/SRC-0001`–`SRC-0009`, `02_sources/SRC-0010` |
| SRC (Quellenobjekte) | **10** | SRC-0001 bis SRC-0010 |
| Statements (ST) | **201** | `03_knowledge_base/statements/` (ST-0001–ST-0201) |
| Assumptions (A) | **48** | `03_knowledge_base/assumptions/` (A-0001–A-0048) |
| Mechanisms (MEC) | **21** | `03_knowledge_base/mechanisms/` (MEC-0001–MEC-0021) |
| Principles (P) | **47** | 43 nummerierte (P-0001–P-0043) + 4 Meta-Prinzipien (P-S1-001–P-S1-004) |
| Techniques (T) | **41** | `03_knowledge_base/techniques/` (T-0001–T-0041) |
| Models (MOD) | **10** | `03_knowledge_base/models/` (MOD-0001–MOD-0010) |
| Validation Reports (VAL) | **10** | VAL-0001–VAL-0010, je eines pro Buch |
| Book Reviews | **9 formal + 1 Pilot** | BOOK_REVIEW_REPORT_B0002 bis B0010 (Template-Format); B-0001/SPIN über `PILOT_001_ABSCHLUSSBERICHT.md` (vor Template-Einführung) |
| Research-/Synthese-Reports (übergreifend) | **~15** | SPR-0001 (5 Dokumente), SPR-0002 (1), ACADEMIC_RECOVERY_REPORT.md, ACADEMIC_RECOVERY_REPORT_PACK_2_4.md, WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md, WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md, 2 Peer-Review-Decision-Reports, RELEASE_REPORT_SPRINT_001, SPRINT_2_ABSCHLUSSBERICHT.md, VALIDIERUNGSSPRINT_MEC0010-0012.md |
| Literature Sources (dediziertes Literaturverzeichnis) | **~55–62** | `05_research/LITERATURE_INDEX.md`, Abschnitte A–D |
| Scientific Debt Einträge | **56 Objekt-Zeilen** (+ 6 systemische SD-SYS-Cluster, in den 56 enthalten) | `00_project/SCIENTIFIC_DEBT.md` |
| Open Decisions | **8**, davon **0 als DONE markiert** | `00_project/OPEN_DECISIONS.md`, OD-001–OD-008 |

**Gesamtzahl kanonischer Wissensobjekte (ST+A+MEC+P+T+MOD):** 201+48+21+47+41+10 = **368** — deckungsgleich mit der im externen Gutachten genannten Zahl „~368 Wissensobjekte" (`WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md`, Zeile 4). Das ist eine positive Konsistenzprüfung: Die Objektzahl ist über mehrere unabhängig erstellte Dokumente hinweg stabil.

**Anmerkung zur Repository-Hygiene:** Es existiert ein leerer, verwaister Ordner `04_book_analysis/Never_Split_The_Difference/` (Unterstriche, ohne Inhalt) neben dem korrekt befüllten `04_book_analysis/Never Split the Difference/`. Vermutlich ein Artefakt einer frühen Namenskonvention-Änderung. Enthält keine Dateien, richtet keinen inhaltlichen Schaden an, sollte aber vor Version 1.0 bereinigt werden.

---

# 3. Canonicalisierung

## Canonicalization Rate im Zeitverlauf

| Buch | Canonicalization Rate | Quelle |
|---|---|---|
| B-0001 SPIN Selling | 0 % (erstes Buch, kein Vergleich möglich) | REPOSITORY_KPIS.md |
| B-0002 Influence | 37,5 % (3/8 MECs erweitert) | REPOSITORY_KPIS.md |
| B-0003 Never Split the Difference | 50 % (3/6) | BOOK_REVIEW_REPORT_B0003.md, VAL-0003 |
| B-0004 The Challenger Sale | 50 % (2/4) | BOOK_REVIEW_REPORT_B0004.md, VAL-0004 |
| B-0005 Gap Selling | 67 % (2/3) | BOOK_REVIEW_REPORT_B0005.md, VAL-0005 |
| B-0006 The JOLT Effect | 3 % (1/32) | BOOK_REVIEW_REPORT_B0006.md |
| B-0007 Getting to Yes | 4 % (1/24) | BOOK_REVIEW_REPORT_B0007.md |
| B-0008 Pre-Suasion | 4 % bzw. 25 % — **widersprüchlich, siehe unten** | analysis.md vs. BOOK_REVIEW_REPORT_B0008.md |
| B-0009 To Sell Is Human | 0 % (alle Objekte neu) | BOOK_REVIEW_REPORT_B0009.md |
| B-0010 Thinking, Fast and Slow | 15 % bzw. 22 % — **widersprüchlich, siehe unten** | BOOK_REVIEW_REPORT_B0010.md vs. analysis.md |

**Neubefund dieses Audits:** Bei zwei Büchern (Pre-Suasion, Thinking Fast and Slow) weichen die in `analysis.md` und im zugehörigen `BOOK_REVIEW_REPORT` berechneten Canonicalization Rates voneinander ab (25 % vs. 4 % bei Pre-Suasion; 22 % vs. 15 % bei Thinking Fast and Slow). Das deutet auf unterschiedliche Zähllogiken zwischen Zwischenstand (`analysis.md`, während der Verarbeitung) und Abschlussdokument (`BOOK_REVIEW_REPORT`, nach vollständiger Objektanlage) hin — vermutlich weil im Analyse-Zwischenstand noch nicht alle später tatsächlich neu angelegten Objekte gezählt waren. Es handelt sich damit wahrscheinlich nicht um einen Rechenfehler, sondern um einen Snapshot-Unterschied — dies ist aber nirgends explizit vermerkt und sollte vor Version 1.0 durch eine Fußnote in beiden Dokumenten klargestellt werden, um Verwirrung bei künftigen Lesern zu vermeiden.

**Gesamteinschätzung Canonicalisierung:** Der externe Gutachter bewertet die durchschnittliche Rate (er zitiert 4 % für Sprint 2) als Warnsignal für „Begriffsinflation" — dass Objekte zu stark an der Autoren-Nomenklatur statt am zugrundeliegenden Konstrukt hängen. Dieser Audit teilt die Einschätzung nur teilweise: Bücher mit hoher konzeptueller Nähe zu bereits abgedeckten Themen (Influence, Never Split the Difference, Challenger, Gap Selling — alle im Bereich Käuferpsychologie/Discovery) zeigen tatsächlich brauchbare Wiederverwendung (37,5–67 %). Bücher mit strukturell andersartigem Fokus (JOLT: Indecision-Diagnostik; Getting to Yes: formale Verhandlungstheorie; To Sell Is Human: Motivationspsychologie) zeigen niedrige Raten, weil sie tatsächlich neue Konstrukte einführen, nicht zwingend weil Begriffsinflation vorliegt. Die niedrige Rate ist damit teils ein echtes Signal für Redundanzrisiko, teils ein Artefakt der bewussten Auswahl thematisch diverser Bücher.

## Redundanz und Fragmentierung

Der ungelöste Fusionskandidat MEC-0006 (Social Proof, externe Marktbeobachtung) vs. MEC-0014 (Konsens im Buying Center, interne Organisationsbeobachtung) ist seit Sprint 1 dokumentiert und wurde in Sprint 2 sowie im Academic Recovery Sprint erneut aufgeworfen, aber bewusst nicht fusioniert (unterschiedliche Stimuli, CKM-konforme Trennung). Dies ist eine begründete, keine vernachlässigte Entscheidung — aber sie ist eine der acht seit Monaten unentschiedenen Open Decisions (siehe Kapitel 7).

## Objektqualität — Neubefund: Evidenzfeld-Vollständigkeit

Eine vollständige Durchsicht aller Evidenzfelder (nicht nur der MEC-Ebene, wie in früheren Prüfungen) ergibt:

- **Techniken ohne Evidenzklassifikation:** T-0019, T-0020, T-0021, T-0026, T-0027, T-0028, T-0029, T-0030, T-0031, T-0032, T-0033, T-0034 — zwölf von 41 Techniken (29 %). Betrifft fast ausschließlich B-0006 (JOLT, T-0026–T-0030) und B-0007 (Getting to Yes, T-0031–T-0034), plus zwei Objekte aus B-0004/B-0007 (T-0019/T-0020/T-0021).
- **Prinzipien ohne Evidenzklassifikation:** P-0027 bis P-0034 (acht von 43 nummerierten Prinzipien, aus B-0006/B-0007) sowie alle vier Meta-Prinzipien P-S1-001 bis P-S1-004 — obwohl für Letztere QK-Werte (QK-6 bis QK-8+) in `SPR-0002_SYNTHESEBERICHT.md` dokumentiert sind, fehlt im jeweiligen Objekt selbst ein formales Evidenzklassifikations-Feld.
- **Evidenzlevel-Desynchronisation:** T-0012 (Mirroring, E3) und T-0013 (Labeling, E3) referenzieren MEC-0011 bzw. MEC-0010, die beide im Peer Review Sprint 1 von E3 auf E2 herabgestuft wurden (`PEER_REVIEW_DECISION_REPORT_SPRINT_001.md`). Die Technik-Objekte wurden bei dieser Herabstufung nicht mitaktualisiert und zitieren ihre alten E3-Werte weiter — mit derselben Primärquelle (Stephens/Hasson 2010 bzw. Lieberman 2007), die im MEC-Objekt inzwischen als nicht hinreichend für E3 bewertet wird.

Dies ist ein Konsistenzrisiko, kein Beleg für falsche Inhalte — die zugrunde liegende Vorsicht ist in den MEC-Objekten korrekt dokumentiert. Aber ein Nutzer, der nur T-0012 liest, sieht E3 statt der zutreffenderen E2-Einschätzung.

## Top 10 Kernmechanismen

Rangfolge nach Kombination aus Evidenzlevel, Quellen-Konvergenz (QK) und dokumentierter Vertriebsrelevanz:

1. **MEC-0021** — Anchoring-Mechanismus (E5, QK-5) — einziger MEC mit doppelt bestätigtem E5 (Kahneman/Tversky-Primärquelle + Schley & Weingarten 2023 Meta-Analyse mit 2.603 Effektgrößen)
2. **MEC-0002** — Loss Aversion / Status-Quo-Kosten (E4 mit E5-Primärquellen-Anker) — trägt P-S1-001 (COI), die am stärksten konvergierte Aussage des Codex
3. **MEC-0012** — Dual-Process System 1/2 (E4, MacLean-bereinigt) — Meta-Rahmen für Tactical-Empathy-Begründung
4. **MEC-0009** — Perceptual Contrast (E4) — Abgrenzung zu MEC-0021 vollständig geklärt
5. **MEC-0015** — Kognitive Überlastung / Choice Overload (E5)
6. **MEC-0005–MEC-0008** — Cialdini-Kernprinzipien (Reziprozität, Social Proof, Liking, Authority; alle E4) — breiteste Einzelanwendung im Codex
7. **MEC-0016** — FOMU/Indecision (E4, aber B2B-proprietär gestützt — Tier-1-Risiko)
8. **MEC-0018** — Pre-Suasion/Priming (E4, aber unter Replikationskrisen-Druck — SD-B010-001, höchste Scientific-Debt-Priorität)
9. **MEC-0020** — Perspektivübernahme (E4, direkte Konvergenz mit Research Pack 3/4 bestätigt)
10. **MEC-0010/MEC-0011** — Amygdala-Regulation/Neural Coupling (E2, riskanteste, aber am transparentesten dokumentierte Objekte des Codex — Musterbeispiel für Scientific-Debt-Kultur)

## Top 10 zentrale Prinzipien

1. **P-S1-001** — Cost of Inaction als universeller Kaufmotivator (QK-8+, höchste Konvergenz des Codex)
2. **P-S1-003** — Problem-Zentrierung als universelles Differenzierungsprinzip (QK-6+, aber mit explizitem W-001-Vorbehalt)
3. **P-S1-004** — Informationssparsamkeit als Wirkungsverstärker (QK-7)
4. **P-S1-002** — Mikro-Commitment-Sequenz (QK-6)
5. **P-0002** — Solution Value Follows Problem Weight (E4)
6. **P-0016** — Tactical Empathy / emotionale Regulation (E3, trägt MEC-0010/0011-Vorbehalt weiter)
7. **P-0021** — Commercial Teaching Pitch als Wirkungssequenz (E3, Kern von W-001)
8. **P-0025** — Vollständige Gap-Diagnose vor Lösung (E2, Gegenposition zu P-0021 in W-001)
9. **P-0042** — Ankerkontrolle im Preisgespräch (E4, direkt gestützt durch MEC-0021)
10. **P-0031** — Interessen statt Positionen (Getting to Yes — kein Evidenzfeld, s. o., aber hohe konzeptuelle Zentralität für M0D-0007)

## Top 5 wichtigste Modelle

1. **MOD-0010** — Kahneman Kognitive-Bias-Karte (integriert MEC-0002, 0012, 0018, 0021 — höchste MEC-Dichte)
2. **MOD-0002** — Cialdini Sieben Prinzipien (breiteste Einzelanwendung, sieben MECs)
3. **MOD-0004** — Challenger Sale TTC-Modell (Kern von W-001, proprietär gestützt)
4. **MOD-0007** — Principled Negotiation (Fisher/Ury — einziges Modell mit institutioneller statt Labor-/proprietärer Fundierung)
5. **MOD-0003** — BCSM/Voss-Verhandlungssystem (höchstes Vertriebsrelevanz-Rating, aber niedrigstes durchschnittliches Evidenzniveau der Top-5-Modelle)

---

# 4. Wissenschaftliche Evidenz

## Evidence-Level-Verteilung (Mechanismen, vollständig gegen die Objekte selbst geprüft)

| Level | Anzahl MECs | Objekte |
|---|---|---|
| E5 | **2** | MEC-0015, MEC-0021 |
| E4 | **15** | MEC-0001–0009, MEC-0012, MEC-0016–0020 |
| E3 | **2** | MEC-0013, MEC-0014 |
| E2 | **2** | MEC-0010, MEC-0011 |
| E1 | **0** | — (E1-Anteile existieren nur als Unteraspekte, z. B. Spiegelneuronen-Erklärung in MEC-0011, nicht als Gesamtobjekt-Rating) |

**Neubefund — Diskrepanz zwischen Selbstbericht und Objektstand:** `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (Abschnitt 1.1, Zeile 33) behauptet: „5 Mechanismen auf E5 (replizierter Konsens): MEC-0002, MEC-0009, MEC-0012, MEC-0015, MEC-0021". Eine Vollprüfung der tatsächlichen `## Evidenzlevel`-Abschnitte in den Objektdateien selbst zeigt: MEC-0002 trägt E4 (mit einer E4/E3/E2-Staffelung je nach Anwendungsebene), MEC-0009 trägt E4, MEC-0012 trägt E4. **Nur MEC-0015 und MEC-0021 tragen tatsächlich E5 als Gesamtobjekt-Rating.** Die Zahl „5" im Reifegradbericht ist damit um 150 % zu hoch gegenüber dem, was die Objekte selbst dokumentieren. Interessant: Die betroffenen Objekte selbst sind korrekt und konservativ gestuft (E4 mit granularer Aufschlüsselung) — die Inflation liegt ausschließlich in der zusammenfassenden Erzählebene des Reifegradberichts, nicht im Wissensobjekt. Das ist ein Beleg für genau das Risiko, vor dem der externe Gutachter warnt (Abschnitt 1: „Epistemologie-Falle" durch Aggregation), diesmal aber in der Selbstbewertung des Codex, nicht in den Quellinterpretationen.

## Andere Objektklassen (E-Level, soweit Feld vorhanden)

- **Assumptions (48):** E1×1 (A-0016), E2×~20, E3×~19, E4×~7, fehlend×1 (A-0044) — brauchbare Normalverteilung, kein auffälliges Muster.
- **Techniques (41):** E2×13, E3×16, E4×3, fehlend×12 (s. Kapitel 3) — Verteilung unter den bewerteten Objekten plausibel, aber 29 % fehlende Werte sind ein Vollständigkeitsproblem.
- **Principles (47):** E2×8, E3×22, E4×9, fehlend×12 (8 nummerierte + 4 Meta-Prinzipien) — gleiches Muster wie bei Techniken.

## Bewertung: Realistische Verteilung?

Im Kern ja. Die Konzentration von E4/E5 im behavioral-economics-nahen Kern (Kahneman/Cialdini-Objekte) und von E2/E3 im Verhandlungs- und B2B-Methodik-Bereich (Voss, Challenger, JOLT, Gap Selling) spiegelt die tatsächliche akademische Literaturlage korrekt wider — hier liegt keine systematische Überschätzung vor. Die Objekt-Ebene selbst ist überwiegend ehrlich kalibriert.

**Inflationsrisiken identifiziert:**
1. Die oben beschriebene E5-Zähler-Diskrepanz im Reifegradbericht (Erzählebene, nicht Objektebene).
2. QK-Rating-Risiko (bereits vom Codex selbst als OD-006 dokumentiert): Konvergenz zwischen Cialdini → Voss → Keenan könnte teilweise Meme-Replikation statt unabhängiger Beobachtung sein — ungelöst seit Sprint 1.
3. T-0012/T-0013 tragen ein höheres E-Level (E3) als ihre Basis-Mechanismen (E2) — lokale Inflation auf Technik-Ebene (s. Kapitel 3).

**Unterbewertungsrisiken identifiziert:**
1. MEC-0020 (Perspektivübernahme) ist trotz doppelter unabhängiger Konvergenzbestätigung (Research Pack 3 UND 4, `SCIENTIFIC_DEBT.md` SD-SYS-006) weiterhin nur E4 — konservativ, aber nicht falsch.
2. Die neue LSM-Literatur (Taylor & Thomas 2008, Ireland & Henderson 2014, in dieser Session zu MEC-0011 ergänzt) verbessert die Beleglage für „verbale Synchronität wirkt in Verhandlungen" spürbar, ohne dass dies zu einer Anhebung führte — bewusst konservative, aber vertretbare Zurückhaltung, da Voss' spezifische Technik weiterhin nicht direkt getestet ist.

**Gesamturteil Kapitel 4:** Die Objektebene ist überwiegend realistisch und konservativ bewertet. Die Risiken liegen nicht in systematischer Überbewertung einzelner Mechanismen, sondern in (a) einer optimistischeren Erzählebene in Zusammenfassungsdokumenten und (b) unvollständiger Weitergabe von Korrekturen an nachgelagerte Objekte (T-Ebene).

---

# 5. Literature Coverage

| Bereich | Abdeckung | Begründung |
|---|---|---|
| Meta-Analysen | **Gut** | Schley & Weingarten (2023, Anchoring, 2.603 Effektgrößen), Brown/Imai/Vieider/Camerer (2024, Loss Aversion, 607 Schätzungen), Mertens et al. (2021, Nudging, mit dokumentierter Kontroverse), Franke & Park (2006, Adaptive Selling) — vier echte Meta-Analysen websuchverifiziert im Repository verankert |
| Reviews/Theoriewerke | **Mittel-Gut** | Evans (2008), Stanovich (2011), Strack & Deutsch (2004) für Dual-Process-Theorie; Petty & Cacioppo (ELM), Mayer/Davis/Schoorman (Trust) als hochkarätige, aber noch nicht formal integrierte Kandidaten (`review_queue.md`) |
| Primärstudien | **Gut im Kern, dünn in der Peripherie** | Kahneman/Tversky (1974/1979/1981), Asch (1951), Milgram (1963), Festinger (1957), Brehm (1966) — klassische, hochzitierte Primärquellen im Zentrum; JOLT/Getting-to-Yes-Peripherie deutlich dünner |
| Practitioner-Literatur | **Sehr gut, aber strukturell dominant** | Alle 10 Bücher vollständig (bis auf Gap Selling, dokumentierter Quellenvorbehalt SD-SYS-002) mit hoher Extraktionsdichte verarbeitet |
| B2B-Literatur | **Schwach** | Nur Abstract-Ebene für Ohiomah et al. (2020), Marcos-Cuevas et al. (2023), Verbeke/Dietz/Verwaal (2010/2011), Johnston & Lewin (1996), Webster & Wind (1972), Sheth (1973), Eisenhardt (1989), Plouffe et al. (2013, neu identifiziert) — kein einziges davon volltextverarbeitet. Dies ist die am häufigsten und konsistentesten benannte Schwäche über alle drei Prüfzyklen hinweg. |
| Verhandlungsforschung | **Mittel-Gut** | Fisher/Ury/Patton (Primärtext verarbeitet), Thompson (1990), Bazerman & Neale (1992), Galinsky & Mussweiler (2001), neu: Taylor & Thomas (2008), Ireland & Henderson (2014, LSM), Tversky & Shafir (1992, neu identifiziert als Tier-1-Kandidat) |
| Behavioral Economics | **Sehr gut** | Der am akademisch stärksten fundierte Bereich des gesamten Codex |
| Sozialpsychologie | **Gut** | Cialdini-Kern vollständig primärtextverarbeitet; Ergänzungsliteratur (Asch, Sherif, Deutsch & Gerard, Goldstein et al.) websuchverifiziert nachgezogen |

**Zusammenfassung:** Die akademische Literaturbreite ist im Kernbereich (Entscheidungspsychologie, Compliance-Psychologie) exzellent, im B2B-spezifischen Bereich strukturell schwach — bei sämtlichen relevanten Quellen fehlt der Volltextzugriff, was jede tiefere Integration bisher verhindert hat. Dies ist der konsistenteste, am längsten bekannte und am wenigsten adressierte Befund über alle Prüfzyklen des Codex.

---

# 6. Scientific Debt

## Umfang und Cluster

56 individuelle Objekt-Zeilen, gruppiert in neun buchspezifische Tabellen (B-0001 bis B-0010) plus sechs systemische Cluster (SD-SYS-001 bis SD-SYS-006) plus zwei sprintübergreifende Ergänzungsabschnitte (ARS-0001 Research Pack 1; Research Pack 2–4).

**Schweregrad-Verteilung (nach dokumentierter Priorität):**

| Priorität | Ungefähre Anzahl | Beispiele |
|---|---|---|
| Hoch | ~12 | SD-SYS-001 (Huthwaite/CEB-Replikationsrisiko), SD-SYS-004 (Publication Bias CEB/JOLT), SD-B010-001 (Priming-Replikationskrise MEC-0018), SD-SYS-002 (Gap-Selling-Quellenlücke), A-0019/53%-Split |
| Mittel | ~35 | Großteil der buchspezifischen Einträge, inkl. der beiden in dieser Session neu dokumentierten MEC-0011-Einträge (LSM-Timing-Widerspruch, Trennungsbestätigung) |
| Niedrig | ~9 | Kulturelle Generalisierungsfragen, kleinere Abgrenzungsfragen |

## Tier-Gruppierung (nach ACADEMIC_RECOVERY_PLAN.md-Logik übertragen auf Scientific Debt)

- **Tier 1 (zwingend vor Version 1.0 zu schließen):** SD-SYS-001/SD-SYS-004 (Publication Bias proprietärer B2B-Studien), W-001 (kein SD-Eintrag im engeren Sinn, aber die zentrale Blockade), SD-B010-001 (Priming-Replikationskrise, direkt MEC-0018 betreffend).
- **Tier 2 (wichtig, aber nicht blockierend):** SD-SYS-002 (Gap-Selling-Quellenvorbehalt), die MEC-0006/MEC-0014-Fusionsfrage, MEC-0011-Gesamtkomplex (Neural Coupling, inkl. neuer LSM-Timing-Widerspruch).
- **Tier 3 (kann nach Version 1.0 weiterverfolgt werden):** Kulturelle Generalisierungsfragen, kleinere Kontext-Abgrenzungen, SD-SYS-003 (Meme-Filter-Frage), SD-SYS-005 (Nudging-Kontroverse, betrifft kein bestehendes Objekt).

## Bewertung: Was muss vor Version 1.0 zwingend geschlossen werden?

Nach diesem Audit sind das konkret: (1) SD-B010-001 — MEC-0018 (Pre-Suasion) braucht eine explizite, für Nutzer sichtbare Kurzwarnung direkt im Vertriebsrelevanz-Abschnitt, nicht nur im Scientific-Debt-Dokument, da eine Priming-Technik sonst unreflektiert angewendet werden könnte; (2) die in diesem Audit neu gefundene Evidenzfeld-Lücke bei 20 Objekten (T- und P-Ebene) — dies ist eine reine Vollständigkeitskorrektur ohne inhaltliches Risiko, aber ohne sie ist die Evidenzbasis für ein Drittel der Techniken/Prinzipien aus zwei Büchern schlicht nicht auffindbar; (3) mindestens eine dokumentierte, nachvollziehbare Positionierung zu SD-SYS-001/004 (Publication Bias), auch wenn diese lautet „strukturell ungelöst, aber Grenzen explizit an jedem betroffenen Objekt markiert" statt einer vollständigen Auflösung.

---

# 7. Open Decisions

| ID | Thema | Status | Wissenschaftliche Relevanz | Priorität | Empfehlung |
|---|---|---|---|---|---|
| OD-001 | Post-Mortem nach Influence | Offen (Abhängigkeit TASK-0010 längst erfüllt — Post-Mortem existiert bereits als `POST_MORTEM_B0002.md`) | Niedrig — de facto bereits erledigt | Niedrig | **DONE** — Dokument existiert, OD-001 sollte formal geschlossen werden. Reine Buchführungslücke. |
| OD-002 | Book Mode offiziell einführen | Offen (im Text selbst, aber Book Mode wird seit B-0003 durchgängig angewendet und ist in `task_rules.md` Abschnitt 10 dokumentiert) | Niedrig — de facto bereits erledigt | Niedrig | **DONE** — Faktisch längst umgesetzt und dokumentiert; OD-002 ist ein veralteter Eintrag. |
| OD-003 | Framework v1.1 einfrieren | Offen im Text, mit v1.1-Release seit `RELEASE_NOTES_v1.1.md` (2026-06-30) faktisch vollzogen | Niedrig — de facto bereits erledigt | Niedrig | **DONE** — Formal schließen. |
| OD-004 | Nächstes Buch nach B-0002 | Offen im Text, aber durch B-0003 bis B-0010 (acht weitere Bücher) längst überholt | Keine mehr | Keine | **ARCHIVIEREN** — Vollständig durch Repository-Realität überholt. |
| OD-005 | Gemini-Validierung der Cialdini-Mechanismen | Offen | Mittel — echte externe Validierung (Zweitmodell) wurde nie durchgeführt, nur durch websuchgestützte Konvergenzprüfungen ersetzt | Mittel | **ERSETZEN** — Die ursprüngliche Idee (Gemini als Zweitmodell) wurde faktisch durch Research-Pack-Websuchverifikation ersetzt; OD-005 sollte entweder als „durch alternative Methode erledigt" umformuliert oder aktiv weiterverfolgt werden, falls ein echtes Zweitmodell-Review noch gewünscht ist. |
| OD-006 | Meme-Filter für QK-Rating | Offen, mit substanzieller Analyse in ARS-0001 ergänzt | Hoch — direkt relevant für die Verlässlichkeit des QK-Konvergenz-Arguments, das die stärkste Einzelaussage des Codex (P-S1-001) trägt | Hoch | **OFFEN, aber priorisieren** — Dies ist keine kosmetische Frage; sie betrifft die Validität der am meisten zitierten Stärke des Codex. |
| OD-007 | CTX-Kontextebene | Offen, mit sehr detaillierter, beidseitig abgewogener wissenschaftlicher Bewertung bereits vorliegend | Hoch — direkt relevant für Generalisierbarkeit (schwächste Reifegrad-Dimension, C+) | Mittel | **OFFEN** — Die vorliegende Analyse ist bereits entscheidungsreif; es fehlt nur noch die Herausgeber-Entscheidung selbst, keine weitere Recherche. |
| OD-008 | Priorisierung ELM/Trust/PKM-Sprint vs. Academic Recovery Plan Tier 1 | Offen | Mittel — strategische Priorisierungsfrage, keine inhaltliche Blockade | Niedrig-Mittel | **OFFEN** — Kann parallel zu AR-001/002/013 entschieden werden, ist nicht zeitkritisch. |

**Zusammenfassender Befund:** Von acht Open Decisions sind vier (OD-001 bis OD-004) durch die Repository-Realität faktisch bereits erledigt, aber formal nie geschlossen worden — ein reines Nachpflegeversäumnis ohne wissenschaftliches Risiko. Die verbleibenden vier (OD-005 bis OD-008) sind inhaltlich substanziell und sollten vor einer Version 1.0 tatsächlich entschieden werden, da sie strukturelle Fragen betreffen (Konvergenz-Validität, Generalisierbarkeit, Validierungsmethodik), nicht nur redaktionelle Details.

---

# 8. Architektur

## Repository-Struktur

Die Ordnerstruktur (00–07 plus 99_archive) ist klar, konsequent und wird eingehalten. `05_publications`, `06_media` und `07_scripts` sind angelegt, aber inhaltlich leer (nur README-Platzhalter) — konsistent mit dem Reifegrad des Projekts (noch keine Publikationsphase), kein Mangel, sondern korrekter Zustand für den aktuellen Sprint-Stand.

## Wissensmodell

Das Canonical Knowledge Model (`01_framework/05_knowledge_model/canonical_knowledge_model.md`, 334 Zeilen) ist detailliert, mit Entscheidungslogik (Neu/Erweitern/Zusammenführen/Verwerfen), Mindestschwellen und einer expliziten Nicht-Anlage-Dokumentationspflicht (Abschnitt 9, seit v1.1). Dies ist eine der methodisch stärksten Komponenten des gesamten Repositorys.

**Architektur-Risiko (neu identifiziert):** Im selben Ordner liegt eine zweite, ältere Datei `codex_knowledge_model.md` (69 Zeilen, deutlich einfacher, keine Versionsangabe), die inhaltlich von `canonical_knowledge_model.md` abgelöst wurde, aber nicht als archiviert markiert oder gelöscht ist. Da beide Dateien ähnlich benannt sind, besteht ein reales Verwechslungsrisiko für neue Mitwirkende (menschlich oder KI), die versehentlich die veraltete Datei statt des aktuellen CKM referenzieren könnten.

## Governance

Die Stateless Agent Architecture (PROJECT_BOOTSTRAP.md, CURRENT_STATE.md, NEXT_ACTION.md, SESSION_LOG.md, OPEN_DECISIONS.md) ist ein durchdachtes Muster für ein Projekt, das über viele einzelne, gedächtnislose Arbeitssitzungen hinweg konsistent bleiben muss. Das Session Log ist lückenlos und chronologisch sauber geführt. Die „Pflichtabschluss jeder Session"-Regel in NEXT_ACTION.md wird sichtbar eingehalten.

## Operating Manual

`SALES_CODEX_OPERATING_MANUAL.md` (315 Zeilen) und `task_rules.md` (403 Zeilen) definieren den Book-Mode-Workflow, Abbruchbedingungen und Pflichtfelder detailliert genug, um von unterschiedlichen KI-Sitzungen konsistent ausgeführt zu werden — belegt durch die tatsächliche Konsistenz der Objektstruktur über zehn unabhängig verarbeitete Bücher hinweg.

## Academic Recovery / Peer Review / Literature Index

Der zweiphasige Academic Recovery Sprint (ARS-0001) mit vorgeschaltetem externem Gutachten und zwei formalen Peer-Review-Decision-Reports ist ein außergewöhnlich gut dokumentierter Selbstkorrektur-Zyklus. Bemerkenswert: In beiden Decision Reports wurden nicht alle Gutachter-Empfehlungen unkritisch übernommen (z. B. Ablehnung der sofortigen MEC-0006/0014-Fusion, Ablehnung einer vorschnellen CTX-Einführung) — echte redaktionelle Unabhängigkeit statt reflexhafter Anpassung an externe Kritik. `05_research/LITERATURE_INDEX.md` ist ein sauber strukturiertes, mit Verifikationsstatus versehenes Literaturverzeichnis, das Doppelrecherche verhindert — eine gute strukturelle Ergänzung, die es vor dem Academic Recovery Sprint noch nicht gab.

## Architektur-Risiken (Zusammenfassung)

1. Zwei koexistierende Knowledge-Model-Dateien (Verwechslungsrisiko).
2. Evidenzfeld-Namenskonvention nicht einheitlich („Evidenzlevel", „Evidenzklasse", „Evidenzklassifikation", „Evidenzstatus", „Wie gut ist sie belegt?" — mindestens fünf verschiedene Formulierungen für dasselbe Konzept über verschiedene Templates/Bücher hinweg).
3. Kein automatisierter Konsistenz-Check zwischen MEC-Evidenzlevel und abhängigen T-/P-Objekten (führte zur in Kapitel 3 dokumentierten Desynchronisation).
4. Leerer Duplikat-Ordner (Never_Split_The_Difference).

## Architektur-Stärken (Zusammenfassung)

1. Durchgängige, nachvollziehbare Objekt-Hierarchie mit funktionierender Nicht-Anlage-Dokumentation.
2. Stateless Agent Architecture ermöglicht tatsächlich konsistente Fortsetzung über viele einzelne Sitzungen.
3. Aktiv geführte, granulare Scientific-Debt-Matrix mit Kategorien, Prioritäten und Objektbezug.
4. Nachweisliche Selbstkorrektur-Kultur (E-Level-Herabstufungen, Ablehnung von Gutachter-Empfehlungen, transparente Zitationskorrekturen).

---

# 9. Fehlende Bereiche

Priorisiert nach objektivem Schwächungsgrad, nicht nach Wunschliste:

**Tier 1 (schwächt den Codex strukturell):**
- **B2B-spezifische Primärforschung mit Volltextzugriff.** Dies ist die am häufigsten wiederholte, am längsten bekannte Lücke (seit Reifegradbericht, bestätigt im externen Gutachten, bestätigt in ARS-0001 Phase 1 und 2, bestätigt in diesem Audit). Ohne sie bleibt die gesamte B2B-Methodik-Ebene (SPIN, Challenger, JOLT) auf proprietären Daten aufgebaut.
- **Auflösung oder formale Modellierung von W-001.** Kein neues Themenfeld, sondern eine strukturelle Lücke in der bestehenden Methodik-Ebene, die die praktische Anwendbarkeit der P-Ebene einschränkt.

**Tier 2 (spürbare Lücke, aber nicht blockierend):**
- **Account Management / Customer Success** — kein Buch, kein Objekt deckt die Post-Sale-Phase ab; der Codex ist ein reines Erstkauf-Modell.
- **Pricing Psychology im B2B-Kontext** — Anchoring-Technik vorhanden (T-0040), aber kein dediziertes Preisverhandlungswerk verarbeitet.
- **Principal-Agent-/Anreizökonomie-Mechanismus** — vom externen Gutachten explizit gefordert, in ACADEMIC_RECOVERY_PLAN.md als AR-005 vorbereitet, aber noch nicht mit Primärtext verarbeitet.

**Tier 3 (Erweiterungspotenzial, kein aktueller Mangel):**
- **Geografisch-kulturelle Diversifizierung** — alle zehn Bücher nordamerikanisch/westeuropäisch prägt; als Tier-4-Punkt im Academic Recovery Plan bereits selbst korrekt niedrig priorisiert.
- **Digitale Verkaufsprozesse / Inside Sales** — kein Buch, aber auch keine zwingende Lücke für den aktuellen Kernscope (Käuferpsychologie, Verhandlung).

---

# 10. Readiness Assessment

**Ist der Sales Codex bereit für Version 1.0? Nein — noch nicht.**

Objektive Kriterien, die nach diesem Audit fehlen:

1. **Mindestens eine der beiden Tier-1-Kernlücken (W-001 oder Publication-Bias-Klärung) muss inhaltlich bearbeitet sein** — nicht notwendigerweise vollständig gelöst, aber mit tatsächlich verarbeitetem Primärtext statt Abstract-Ebene. Aktuell: keine der beiden Lücken hat diesen Status erreicht.
2. **Die in diesem Audit gefundene Evidenzfeld-Lücke (20 Objekte ohne Klassifikation, 2 Objekte mit veralteter Klassifikation) muss geschlossen sein.** Dies ist reine Konsistenzarbeit ohne neue Recherche, aber notwendig, damit die Evidenzbasis für ein Drittel der B-0006/B-0007-Objekte überhaupt auffindbar ist.
3. **Mindestens die vier faktisch bereits erledigten Open Decisions (OD-001 bis OD-004) müssen formal geschlossen werden**, und mindestens eine der vier substanziellen (OD-005 bis OD-008) muss eine tatsächliche Herausgeber-Entscheidung erhalten. Ein System mit 0 von 8 entschiedenen Open Decisions sollte nicht in eine „1.0"-Konsolidierung gehen.
4. **Eine einheitliche Feldbenennung für Evidenzklassifikation** über alle Objekttypen hinweg (aktuell mindestens fünf verschiedene Formulierungen) sollte vor einer Versionsfreigabe vereinheitlicht werden — nicht inhaltlich kritisch, aber ein Qualitätsmerkmal für ein Repository, das als „1.0" nach außen vertretbar sein soll.

**Was bereits erreicht ist und für Version 1.0 spricht:** Die Kernmethodik ist stabil (kein Framework-Wechsel seit v1.1), die Objekt-Hierarchie ist über zehn Bücher hinweg konsistent angewendet, die Scientific-Debt-Kultur ist vorbildlich, und der psychologische Kern des Codex ruht auf einer der stärksten verfügbaren akademischen Grundlagen (Kahneman/Tversky), unabhängig verifiziert und mehrfach nachgeschärft.

---

# 11. Roadmap

Maximal fünf Meilensteine, streng nach wissenschaftlichem Nutzen priorisiert:

1. **Konsistenzkorrektur-Sprint (kein neuer Content, reine Synchronisation):** T-0012/T-0013 E-Level an MEC-0010/0011 angleichen; Evidenzfeld bei den 20 identifizierten Objekten (T-0019–T-0034, P-0027–P-0034, P-S1-001–004) ergänzen; Feldbenennung vereinheitlichen. Höchster Aufwand-Nutzen-Quotient aller vorgeschlagenen Schritte, da es sich um reine Repository-Hygiene ohne neue Recherche handelt.
2. **AR-001 + AR-013 gemeinsam bearbeiten (Problemreife-Hypothese + Tversky & Shafir-Volltextverarbeitung):** Beide zielen auf dieselbe strukturelle Schwäche (W-001-Kontext bzw. Indecision-Publication-Bias) und lassen sich in einem Rechercheblock effizient gemeinsam bearbeiten.
3. **AR-002 (Publication-Bias-Klärung proprietärer B2B-Studien) — Volltextauswertung von Ohiomah et al. (2020) und Marcos-Cuevas et al. (2023) statt Abstract-Ebene**, um zu prüfen, ob diese Meta-Analysen die CEB/Challenger/JOLT-Befunde tatsächlich unabhängig einschließen und bewerten.
4. **Herausgeber-Entscheidungsrunde für alle acht Open Decisions** (vier formale Abschlüsse, vier substanzielle Entscheidungen) — kein Rechercheaufwand, reine Entscheidungsarbeit, die aber Voraussetzung für eine glaubwürdige Version-1.0-Freigabe ist.
5. **AR-003 bis AR-006 (Buying-Center-Cluster: Johnston & Lewin, Webster & Wind, Sheth, Eisenhardt, jetzt ergänzt um March & Simon 1958) vollständig mit Primärtext verarbeiten**, um mindestens ein akademisch (nicht-proprietär) fundiertes MEC für die B2B-Kaufentscheidungsdynamik zu etablieren — der vom externen Gutachten explizit als fehlend benannte Mechanismus der Anreizökonomie.

---

# 12. Herausgeberbewertung

Als unabhängiger wissenschaftlicher Auditor, nicht als Teil der Redaktion, die dieses System aufgebaut hat, komme ich zu folgendem Urteil.

**Wurde das Ziel des Sales Codex erreicht?** Teilweise, und in einer Weise, die für ein Projekt dieses Umfangs bemerkenswert ist. Das erklärte Ziel — ein evidenzbasiertes Wissenssystem über Vertrieb, Verkauf, Verhandlung und Käuferpsychologie, das Quellen nicht unkritisch zusammenfasst, sondern bewertet, einordnet und in Frage stellt — ist im Kernbereich (Kahneman/Cialdini-nahe Mechanismen) tatsächlich erreicht. Im B2B-methodischen Kernbereich (die Frage, wie man ein komplexes Verkaufsgespräch tatsächlich führt) ist das Ziel nicht erreicht, und das System weiß das selbst — was der eigentlich bemerkenswerte Punkt ist. Ein Wissenssystem, das seine eigene größte Schwäche über drei unabhängige Prüfzyklen hinweg konsistent und ohne Beschönigung benennt, hat einen zentralen Teil des wissenschaftlichen Ideals bereits verwirklicht, auch wenn der Inhalt selbst noch unvollständig ist.

**Ist das Repository wissenschaftlich belastbar?** Für den psychologischen Kern: ja, in einem Maß, das über viele kommerzielle Vertriebstrainings-Ökosysteme hinausgeht. Für die B2B-Methodik-Ebene: nein, und das System hat das nie anders behauptet — es dokumentiert seine proprietäre Abhängigkeit explizit, statt sie zu verstecken. Belastbarkeit ist hier keine binäre Eigenschaft, sondern eine, die je nach Teilbereich unterschiedlich ausfällt, und der Codex kommuniziert diesen Unterschied ungewöhnlich ehrlich.

**Wo besteht das größte Risiko?** Nicht in den bekannten, seit Sprint 1 dokumentierten Lücken (W-001, Publication Bias) — diese sind identifiziert, priorisiert und werden aktiv bearbeitet, auch wenn langsam. Das größere, weil unentdeckte Risiko liegt in der Divergenz zwischen der MEC-Ebene (die in drei Prüfzyklen intensiv geprüft wurde) und der T-/P-Ebene (die das nicht wurde). Ein System, das seine Kernobjekte sorgfältig korrigiert, aber die davon abgeleiteten praktischen Techniken nicht mitkorrigiert, riskiert, dass die Vorsicht der Wissenschaftler nie bei den Anwendern der Techniken ankommt. Das ist das eigentliche Risiko dieses Audits: nicht was der Codex weiß, sondern was er weiß, aber nicht konsistent weitergibt.

**Was ist die größte Stärke?** Die nachweisliche, wiederholte Bereitschaft, sich selbst zu widersprechen, wenn die Evidenz es verlangt. Ein KI-gestütztes Redaktionssystem, das eigene frühere Einstufungen herabstuft (MEC-0010, MEC-0011, MacLean-Entfernung aus MEC-0012), Gutachter-Empfehlungen ablehnt, wenn sie fachlich nicht überzeugen, und Zitationsfehler transparent korrigiert statt stillschweigend zu bereinigen, verhält sich wissenschaftlicher als viele menschlich geführte Projekte mit vergleichbarem Umfang. Das ist keine rhetorische Floskel — es ist in diesem Repository mehrfach, konkret und nachprüfbar dokumentiert.

**Welche Entscheidung würde ich als Herausgeber als nächstes treffen?** Ich würde keinen weiteren Recherche-Sprint beginnen, bevor der in Kapitel 11, Meilenstein 1 beschriebene Konsistenzkorrektur-Sprint abgeschlossen ist. Der Codex hat in drei Zyklen wiederholt neue Literatur integriert, aber nie systematisch geprüft, ob ältere Korrekturen vollständig durch das System propagiert wurden. Das ist die verantwortungsvollere nächste Handlung als ein weiterer Zuwachs an Breite — Konsolidierung vor Expansion, was im Übrigen genau dem eigenen Leitsatz des Projekts entspricht: „Priorität hat immer die Qualität der Wissensbasis, nicht die Geschwindigkeit."

---

*Erstellt: 2026-07-01 | CODEX AUDIT 2026-07 | Ausschließlich lesende Prüfung, keine Repository-Änderungen vorgenommen.*
