# Evidence Architecture Check — 2026-07-06

**Dokumentklasse:** Archived (einmaliger Audit-Bericht nach Abschluss; nicht Reference, nicht Operational)
**TASK_TYPE:** T6_AUDIT
**Rolle:** Unabhängiger Auditor und Evidenzprüfer — nicht Framework-Architekt, nicht Forscher eines neuen W-Projekts, nicht Editor, nicht Repository-Integrator, nicht Governance-Designer.
**Auftrag:** Compact Evidence Architecture Check gemäß `00_project/RESEARCH_PORTFOLIO_CHECKPOINT_1.md`, Abschnitt 9 und 11.
**Stand:** 2026-07-06
**Methodik-Grundprinzip:** Repository ist Quelle der Wahrheit für den Ist-Zustand; externe Websuche ist Quelle für neue Primär-/Sekundärevidenz. Keine Erinnerung als Autorität. Keine erfundenen Quellen. „Nicht gefunden" ≠ „Evidenz dagegen".

---

## 1. Executive Summary

Dieser Audit prüft drei aus dem Research Portfolio Checkpoint 1 abgeleitete Punkte: (a) die dreifach konvergente B2B-/Vertikal-Transfer-Lücke aus W-002 (ELM), W-003 (ABI-Trust) und W-004 (Social Identity Theory), (b) die Fundamentalevidenz hinter MEC-0014 (CEB/Challenger Sale), und (c) die Aktualität der Buying-Center-Koalitionsliteratur.

**Kernbefunde in Kürze:**

Für alle drei Transferfragen (A1 ELM→B2B, A2 ABI-Trust→High-Ticket-B2C, A3 Social Identity Theory→Buying Center) gilt: Die in W-002/W-003/W-004 dokumentierten Negativbefunde („keine direkte Primärevidenz gefunden") sind im Kern durch diesen Audit **bestätigt**, aber in allen drei Fällen wurde durch systematischere Zwei-Runden-Suche **zusätzliche indirekte (Kategorie 2) Evidenz** gefunden, die in den ursprünglichen Ein-Sitzungs-Recherchen der W-Projekte nicht dokumentiert war. Direkte Primärevidenz (Kategorie 1) im engen Sinn der Auftragsdefinition wurde in keinem der drei Teilbereiche gefunden. Gegenevidenz (Kategorie 3) wurde in keinem der drei Teilbereiche gefunden.

Für die CEB-/Challenger-Sale-Fundamentalevidenz (Prüfbereich B) gilt: Es existiert entgegen einer möglichen Annahme tatsächlich eine substanzielle, mehrfach zitierte akademische Auseinandersetzung mit dem Challenger-Modell — allen voran Rapp, Bachrach, Panagopoulos & Ogilvie (2014, *Journal of Personal Selling & Sales Management*, 34(4), 245–259, prämiert mit dem Marvin Jolson Award), eine systematische, peer-reviewte akademische Kritik (Kategorie B3/B5). Eine echte unabhängige Replikation der originalen 53%/38%/9%-Zahlenaussage wurde jedoch **nicht** gefunden; der Originaldatensatz bleibt unzugänglich. Diese Differenzierung — akademische Kritik existiert, echte Zahlen-Replikation nicht — war im bisherigen Scientific-Debt-Eintrag (A-0019) nicht explizit unterschieden.

Für die Buying-Center-Koalitionsliteratur (Prüfbereich C) bestätigt eine Volltextprüfung von Cabanelas, Mora Cortez & Charterina (2023) den in W-004 nur sekundärquellenbasiert erschlossenen Befund vollständig: 89 systematisch ausgewählte Artikel (1967–2021), abnehmende Publikationszahlen seit den späten 2000er-Jahren, Spitzenjournale „nahezu still" seit den frühen 1990ern. Bemerkenswert: Der Begriff „coalition" kommt in diesem 54-Jahres-Review **kein einziges Mal** vor — ersetzt durch „power and influence", „conflict", „politics", „centralization". Gleichzeitig fand dieser Audit mindestens zwei aktive, methodisch moderne (2018–2022) Forschungslinien, die dasselbe zugrunde liegende Phänomen (interne Politik/Konflikt/Statuskämpfe in Buying-Center-nahen, cross-funktionalen Sourcing-Teams) unter neuer Terminologie empirisch untersuchen. Einstufung: **C-B** — direkte Literatur ist selten geworden, das Phänomen wird unter neuen Begriffen substanziell weiter untersucht.

Kohli (1989) konnte nicht im Volltext direkt beschafft werden, seine Kernaussage (Expertenmacht als stärkster Einflussfaktor in großen, zeitunkritischen Buying Centern; Reinforcement Power in kleinen, zeitkritischen) wird jedoch durch die unabhängige Sekundärquelle Cabanelas et al. (2023) wortwörtlich bestätigt und ist in der Literatur nach wie vor als Standardreferenz aktiv (nicht verdrängt, nicht widerlegt).

**Primäre Programme Recommendation (Details Abschnitt 14):** Kein neues Forschungsprojekt, kein Architecture Freeze. Empfohlen wird ein **begrenztes, punktuelles Folge-Update** dreier Scientific-Debt-Einträge (Cluster A, A-0019/MEC-0014, Kohli/Cabanelas-Einträge in W-004-Sektion) auf Basis der in diesem Audit gefundenen, verifizierten Zusatzquellen — kein neuer W-Prozess, kein Freeze.

---

## 2. Scope und Out of Scope

**Im Scope:**
- Prüfbereich A: drei Transferfragen (ELM→B2B, ABI-Trust→High-Ticket-B2C, Social Identity Theory→Buying Center), je mit epistemischer Klassifikation in Kategorien 1–4.
- Prüfbereich B: CEB-/Challenger-Sale-Fundamentalevidenz, getrennt bewertet je Claim-Baustein (53/38/9-Split, Challenger-Typologie, Commercial Teaching, Buying Consensus/Mobilizer).
- Prüfbereich C: Buying-Center-Koalitionsliteratur, Volltextprüfung Kohli (1989) und Cabanelas et al. (2023), Terminologieverschiebungsprüfung.
- Empfehlungen an den Herausgeber zu betroffenen Scientific-Debt-Einträgen (nur Empfehlung, keine Ausführung).
- Eine primäre Programme Recommendation für die nächste Phase.

**Out of Scope (verbindlich, nicht bearbeitet):**
- Keine neue Theorieentwicklung, keine neue Synthese.
- Keine Änderung an Wissensobjekten (`03_knowledge_base/*` wurde ausschließlich lesend verwendet).
- Keine Änderung an `SCIENTIFIC_DEBT.md`, `OPEN_DECISIONS.md`, `review_queue.md`, `RESEARCH_LIFECYCLE.md`, `RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md`, `RESEARCH_STATUS.md`, `RESEARCH_PORTFOLIO.md`, `CURRENT_STATE.md`, `NEXT_ACTION.md`.
- Keine Aktivierung eines neuen W-Projekts, keine Editor-Decision-Simulation, keine Repository-Integration.
- Keine Korrektur der in `RESEARCH_PORTFOLIO_CHECKPOINT_1.md`, Abschnitt 2.3, benannten Dokumentationsinkonsistenzen (separater T3-Auftrag).
- Keine vollständige Neubewertung des gesamten CEB-Challenger-Komplexes über die vier benannten Claim-Bausteine hinaus.

---

## 3. Methodik

Vorgehen in drei Phasen:

**Phase 1 — Repository-Verifikation (rein lesend).** Pflichtlektüre gemäß Auftrag: `PROJECT_BOOTSTRAP.md`, `SESSION_BRIEF.md`, `TASK_TYPES.md`, `CURRENT_STATE.md` (Statusblock + relevante Abschnitte), `00_project/NEXT_ACTION.md`, `00_project/RESEARCH_PORTFOLIO_CHECKPOINT_1.md` (vollständig), `00_project/SCIENTIFIC_DEBT.md` (vollständig), `06_research_program/RESEARCH_STATUS.md`, `06_research_program/RESEARCH_PORTFOLIO.md` (Kopf), `05_research/LITERATURE_INDEX.md` (Abschnitte A und B vollständig), sowie MEC-0005, MEC-0006, MEC-0007, MEC-0008, MEC-0009 (referenziert, nicht separat geöffnet, da nicht Teil des ELM-Erweiterungspfads), MEC-0012, MEC-0014, MEC-0018, MEC-0030, MOD-0002 im Volltext.

**Phase 2 — Externe Recherche.** Für A1, A2, A3 je mindestens zwei unabhängige, dokumentierte Suchdurchläufe mit unterschiedlichen Suchbegriffsfamilien (ein breiter theoriegeleiteter, ein kontextgeleiteter Durchlauf, teils zusätzliche Vertiefungsrunden bei vielversprechenden Treffern). Für B und C zusätzliche gezielte Suchdurchläufe zu Einzelclaims sowie Versuch der Volltextbeschaffung der beiden in C benannten Zielquellen.

**Phase 3 — Klassifikation und Synthese.** Jeder Treffer wurde einzeln gegen die im Auftrag vorgegebenen Kategorien (1–4 für A; B1–B6 für B; C-A bis C-D für C) geprüft, bevor er in die Matrizen (Abschnitt 12) übernommen wurde. Wo eine Quelle nicht im Volltext zugänglich war, wurde dies explizit vermerkt statt aus dem Titel/Abstract auf den Inhalt zu extrapolieren.

**Suchsättigungsregel:** Nach zwei unabhängigen Suchdurchläufen je Teilpunkt wurde geprüft, ob neue Treffer überwiegend Zitationsduplikate oder dieselben Sekundärquellen wiederholen. Bei A1, A2 und A3 wurde diese Sättigung nach dem zweiten bis vierten Durchlauf erreicht (Details Abschnitt 16).

---

## 4. Suchplattformen und Suchstrategie

Verwendetes Werkzeug: `WebSearch` (allgemeine Websuche, kein Zugriff auf ein einzelnes akademisches Datenbank-Frontend; Treffer stammen überwiegend aus ScienceDirect-, Wiley-, Taylor & Francis-, SAGE-, Emerald-, ResearchGate-, Semantic-Scholar- und Repository-Quellen, die von den jeweiligen Verlagen/Universitäten indexiert werden) sowie `web_fetch` für Volltext-/Abstract-Abruf, wo frei zugänglich (u. a. Open-Access-Repositorien der University of Southern Denmark und University of the Basque Country).

**Einschränkung (transparent zu machen):** Kein direkter Zugriff auf Google Scholar, Web of Science, Scopus oder EBSCO als strukturierte Datenbank-Suchmaske; keine Zitationsanzahl-gestützte systematische Vorwärtsverfolgung im engeren Sinn (Vorwärtsverfolgung erfolgte, wo möglich, über in Suchtreffern sichtbare "cited by"-Angaben von Semantic Scholar). Primärquellen wurden gegenüber Blogs/Beratungsseiten priorisiert; kommerzielle/Practitioner-Quellen wurden identifiziert, aber nicht als wissenschaftliche Evidenzbasis gewertet (Ausnahme: explizit als solche gekennzeichnete Analyse kommerzieller Evidenz in Prüfbereich B).

Vollständiges Suchprotokoll (Suchbegriffe, Datum, Plattform, Treffer, Ausschlussgründe): Abschnitt 16.

---

## 5. Prüfbereich A1 — ELM → B2B / komplexe Buying-Center-Kontexte

### Suchdurchlauf 1 (theoriegeleitet: „Elaboration Likelihood Model" + B2B/Buying-Center-Begriffe)

Treffer identifizierten zwei Kernquellen:

1. **„Understanding the persuasion process between industrial buyers and sellers"**, *Industrial Marketing Management*, 1994 (DOI-Muster 10.1016/0019-8501(94)00035-U, aus PII abgeleitet). Wendet ELM explizit auf die industrielle Käufer-Verkäufer-Persuasion an, entwickelt eine „Typologie kontextueller Unterschiede zwischen Konsumenten- und B2B-Marketingkommunikation" und einen „explanatory model of business-to-business marketing communications effects", der ausdrücklich mit bestehenden Buying-Center-Verhaltensmodellen kongruent sein soll. **Verifikationsvorbehalt:** Autorenname(n) konnten in dieser Sitzung trotz mehrerer Suchversuche nicht zweifelsfrei verifiziert werden — der Titel, das Journal, das Jahr (1994) und das abgeleitete DOI-Muster gelten als bestätigt, die Autorenschaft nicht. Diese Quelle wird daher mit ausdrücklichem Vorbehalt geführt, nicht mit erfundener Autorenangabe.
2. **Gilliland, D. I. & Johnston, W. J. (1997). „Toward a model of business-to-business marketing communications effects." *Industrial Marketing Management*, 26, 15–29.** — bibliografisch verifiziert (Semantic Scholar, ScienceDirect, ResearchGate übereinstimmend). Wendet sich laut Sekundärquellen explizit dem Elaboration Likelihood Model als Rahmen für B2B-Marketingkommunikation zu und fordert ein Modell, das sowohl interne Reaktionen als auch „externally directed influence toward other members of a buying center" erklärt.

**Wichtige methodische Einordnung:** Beide Quellen sind — soweit aus den zugänglichen Sekundärbeschreibungen erkennbar — **konzeptionelle/theoretische Modellarbeiten**, keine empirischen Primärstudien mit eigener Datenerhebung an einer Buying-Center-Stichprobe. Eine tatsächliche empirische Prüfung des ELM-Kernmechanismus (zentrale vs. periphere Route, moderiert durch Motivation/Fähigkeit) an echten Buying-Center-Entscheidern wurde in diesem Suchdurchlauf **nicht** gefunden. Eine 2019 erschienene Aktualisierung (Mora Cortez, R., Gilliland, D. I. & Johnston, W. J. (2019). „Revisiting the theory of business-to-business advertising." *Industrial Marketing Management*.) bestätigt indirekt, dass seit 1997 kein grundlegend neuer, empirisch abgesicherter Ersatz des ELM-basierten Modells etabliert wurde, sondern eine Aktualisierung um neue Kontextfaktoren (Social Media, Kultur, Markenwert) erfolgte — ohne dass diese Aktualisierung selbst eine primäre Buying-Center-Stichprobe verwendet.

### Suchdurchlauf 2 (kontextgeleitet: Quellenglaubwürdigkeit/Argumentqualität/Involvement in professionellen Kaufentscheidungen)

Zentraler Treffer: **Wilson, R. T. & Baack, D. W. (2023). „How the credibility of places affects the processing of advertising claims: A partial test of the B2B communication effects model." *Journal of Business Research*, 168.** Bibliografisch verifiziert (ScienceDirect, mehrere Sekundärquellen übereinstimmend). Dies ist ein **echtes empirisches Experiment** (Online-Between-Subjects-Design) mit einer Stichprobe von **Site-Selection-Managern** (professionelle, organisationale Entscheidungsträger für Standortwahl/Direktinvestitionen), das explizit Quellenglaubwürdigkeit, Argumentqualität und Involvement — die drei zentralen ELM-Moderatoren/Faktoren — testet und dabei ausdrücklich als „partial test of the [Gilliland/Johnston] B2B communication effects model" (also des ELM-abgeleiteten Modells) gerahmt ist. Kernbefund: Quellenglaubwürdigkeit hat in fast allen Bedingungen einen stärkeren Einfluss auf die Botschaftsüberzeugungskraft als Argumentqualität oder Involvement allein.

Weitere Recherche zu „strategic purchasing"/"professional procurement" + Persuasion/Argumentqualität ergab keine zusätzlichen direkten Treffer (überwiegend supply-chain-strategische, nicht persuasionspsychologische Literatur).

### Klassifikation A1

| Aspekt | Einstufung |
|---|---|
| Direkte Transferevidenz (Kategorie 1) | **Nicht gefunden.** Kein Primärexperiment identifiziert, das ELM-Kernmechanismus (zentrale/periphere Route × Motivation/Fähigkeit) direkt an einer echten Multi-Stakeholder-Buying-Center-Stichprobe testet. |
| Indirekte Transferevidenz (Kategorie 2) | **Gefunden.** (a) Zwei konzeptionelle B2B-Marketingkommunikationsmodelle (1994-Quelle mit Autorenvorbehalt; Gilliland & Johnston 1997, verifiziert), die ELM explizit als Rahmen für B2B/Buying-Center-Kommunikation postulieren, jedoch ohne eigene empirische Buying-Center-Stichprobe. (b) Wilson & Baack (2023): echtes empirisches Experiment mit professionellen organisationalen Entscheidungsträgern (Site-Selection-Managern), das ELM-Moderatoren direkt testet, aber in einem Standort-/Investitionsmarketing-, nicht klassischen Produkt-/Dienstleistungs-B2B-Buying-Center-Kontext. |
| Gegenevidenz/Boundary Conditions (Kategorie 3) | Nicht gefunden. |
| Bereits im Repository dokumentiert (W-002) | Deckungsgleich: W-002 fand ebenfalls keine direkte Primärevidenz; dieser Audit bestätigt den Negativbefund für echte Buying-Center-Primärdaten, erweitert ihn aber um die zuvor nicht dokumentierten Kategorie-2-Funde (Gilliland & Johnston 1997; Wilson & Baack 2023). |

---

## 6. Prüfbereich A2 — ABI Trust Model → High-Ticket-B2C

### Suchdurchlauf 1 (theoriegeleitet: ABI/Mayer-Davis-Schoorman + Immobilien/Hausbau/Hypothek)

Keine Studie identifiziert, die das ABI-Modell direkt und explizit an Immobilienkäufern, Hausbau-/Fertighauskunden oder Hypothekennehmern testet. Dieser Negativbefund deckt sich vollständig mit dem in MEC-0030 dokumentierten W-003-Befund.

### Suchdurchlauf 2 (kontextgeleitet: „credence services", hochinvolvierte Beratungsentscheidungen, Finanz-/Versicherungsberatung)

Drei relevante Treffer:

1. **Barnett White, T. (2005). „Consumer Trust and Advice Acceptance: The Moderating Roles of Benevolence, Expertise, and Negative Emotions." *Journal of Consumer Psychology*, 15(2), 141–148.** Bibliografisch verifiziert (Wiley Online Library, ScienceDirect, ResearchGate übereinstimmend). Testet explizit **zwei der drei ABI-Komponenten** (Benevolence und Expertise/Ability) als Trust-Treiber bei „high-stakes" Konsumentscheidungen (medizinische und finanzielle Entscheidungen) — mit dem empirischen Kernbefund, dass Experten-Rat bei geringer emotionaler Schwierigkeit bevorzugt wird, während bei hoher emotionaler Schwierigkeit überwiegend benevolente Anbieter bevorzugt werden (Stress-Buffering-Effekt). Integrity als dritte ABI-Komponente wird nicht separat getestet.
2. **Ho, P. S. S. & Wong, A. (2022/2023). „The role of customer personality in premium banking services." *Journal of Financial Services Marketing*, 28(2).** Bibliografisch verifiziert. Befragung von N=210 **High-Net-Worth-Premium-Banking-Kunden** — ein genuin hochpreisiger, hochinvolvierter B2C-Finanzdienstleistungskontext. Unterscheidet kognitives Trust (Kompetenz/Verlässlichkeit — entspricht Ability) und affektives Trust (Fürsorge/Anteilnahme — entspricht Benevolence); Integrity wird nicht als separate dritte Dimension geführt. Trust beeinflusst signifikant Zufriedenheit und Loyalität.
3. Finanzplaner-Klient-Vertrauensforschung (Sharpe et al., *Journal of Financial Counseling and Planning*, 1998, sowie eine 2022 aktualisierte strukturgleichungsmodellbasierte Untersuchung derselben Forschungslinie, Financial Planning Association) — nutzt ein Beziehungsmarketing- statt explizit ABI-benanntes Rahmenwerk, behandelt aber inhaltlich sehr ähnliche Trust-Antezedenzien (Kompetenz, Kommunikation, wahrgenommenes Wohlwollen) in einem hochinvolvierten Finanzberatungskontext.

### Klassifikation A2

| Aspekt | Einstufung |
|---|---|
| Direkte Transferevidenz (Kategorie 1) | **Nicht gefunden.** Kein Primärtest des vollständigen Drei-Komponenten-ABI-Modells (Ability + Benevolence + Integrity gemeinsam) in einem der explizit benannten High-Ticket-B2C-Zielkontexte (Hausbau, Immobilien, Automobil-Einzelhandel). |
| Indirekte Transferevidenz (Kategorie 2) | **Gefunden, robust.** Drei konvergente Quellen (Barnett White 2005; Ho & Wong 2022/2023; Finanzplaner-Trust-Forschungslinie) testen jeweils zwei der drei ABI-Komponenten (überwiegend Ability/Kompetenz und Benevolence) in genuin hochinvolvierten, teils explizit hochpreisigen (Premium Banking) Beratungs-/Dienstleistungskontexten. Keine dieser Studien deckt Integrity als dritte Komponente eigenständig ab, und keine testet den namentlich benannten Immobilien-/Hausbau-Kontext direkt. |
| Gegenevidenz/Boundary Conditions (Kategorie 3) | Nicht gefunden. |
| Bereits im Repository dokumentiert (W-003/MEC-0030) | MEC-0030 dokumentiert den Negativbefund für Immobilien/Hausbau spezifisch korrekt und vorsichtig. Dieser Audit bestätigt diesen engen Negativbefund, findet aber für die weiter gefassten „hochinvolvierte/credence services"-Suchbegriffe (wie vom Auftrag explizit vorgesehen) drei zusätzliche, in W-003 nicht dokumentierte Kategorie-2-Quellen. |

---

## 7. Prüfbereich A3 — Social Identity Theory → Buying Center

### Suchdurchlauf 1 (theoriegeleitet: „Social Identity Theory" + „buying center"/organisationale Beschaffung)

Keine Studie gefunden, die Social Identity Theory oder Self-Categorization Theory explizit und direkt auf Buying-Center-Koalitionen oder Procurement-Committees anwendet. Deckt sich mit dem W-004-Negativbefund.

### Suchdurchlauf 2 (kontextgeleitet: Self-Categorization/In-group-Out-group + cross-funktionale Einkaufs-/Sourcing-Teams)

Zwei bedeutsame Treffer:

1. **Ambrose, S. C., Matthews, L. M. & Rutherford, B. N. (2018). „Cross-functional teams and social identity theory: A study of sales and operations planning (S&OP)." *Journal of Business Research*, 92, 270–278.** DOI 10.1016/j.jbusres.2018.07.052, bibliografisch verifiziert (Semantic Scholar, ScienceDirect, RePEc übereinstimmend). Wendet Social Identity Theory **explizit und direkt** auf ein cross-funktionales Team an — S&OP-Teams sind organisationsintern, cross-funktional (Vertrieb, Operations, Finance) und strukturell dem Buying Center in Zusammensetzung und Dynamik sehr ähnlich, jedoch nicht identisch (S&OP betrifft Absatz-/Produktionsplanung, nicht direkt Einkaufsentscheidungen). Kernbefund: Superordinate Team Identity (übergeordnete, das Team als Ganzes umfassende Identität) ist positiv mit S&OP-Performance assoziiert; Faktoren, die diese Identitätsbildung fördern, werden identifiziert.
2. **Meschnig, G. & Kaufmann, L. (2015). „Consensus on supplier selection objectives in cross-functional sourcing teams: Antecedents and outcomes." *International Journal of Physical Distribution & Logistics Management*, 45(8), 774–793.** Bibliografisch verifiziert (Emerald, ResearchGate). Direkte empirische Untersuchung (N=88 Sourcing-Teams, 233 Teammitglieder, drei Fertigungsunternehmen) von Konsensbildung in **cross-funktionalen Sourcing-Teams** — dies ist ein echter Buying-Center-naher Kontext (Lieferantenauswahl = organisationale Beschaffung). Untersucht Team-Erfahrung, -Vertrautheit und demografische Diversität als Antezedenzien von Konsens; findet, dass Konsens positiv mit der Auswahl leistungsfähigerer Lieferanten korreliert. Nutzt jedoch **keine explizite Social-Identity-/Self-Categorization-Theorie-Rahmung** — die Nähe zur Fragestellung liegt im Thema (Konsens/Diversität in Buying-Center-nahen Teams), nicht in der Theoriewahl.

Ergänzend identifiziert, aber ohne direkten SIT-Bezug: allgemeine Faultline-/Subgroup-Forschung (Bezrukova, Jehn & Zanutto; van-Knippenberg-Linie) — etablierte, aktive Organisationsforschung zu Identitäts-Faultlines in Teams generell, nicht Procurement-/Buying-Center-spezifisch.

### Klassifikation A3

| Aspekt | Einstufung |
|---|---|
| Direkte Transferevidenz (Kategorie 1) | **Nicht gefunden.** Keine Studie wendet Social Identity Theory explizit auf Buying-Center-Koalitionen im engeren, vom Auftrag definierten Sinn an. |
| Indirekte Transferevidenz (Kategorie 2) | **Gefunden, bedeutsam.** Ambrose, Matthews & Rutherford (2018) — direkte SIT-Anwendung auf ein strukturell sehr ähnliches, aber nicht identisches cross-funktionales Organisationsteam (S&OP statt Buying Center). Meschnig & Kaufmann (2015) — echter Buying-Center-naher Kontext (Sourcing-Teams/Lieferantenauswahl), aber ohne explizite SIT-Rahmung. Diese Kombination ist die bislang im Repository nicht dokumentierte stärkste verfügbare Indizienlage für einen möglichen Transfer. |
| Gegenevidenz/Boundary Conditions (Kategorie 3) | Nicht gefunden. |
| Bereits im Repository dokumentiert (W-004) | W-004 dokumentiert den engen Negativbefund korrekt. Dieser Audit bestätigt ihn für die exakte Buying-Center-SIT-Kombination, findet aber zwei neue, thematisch sehr nahe Kategorie-2-Quellen, die in der W-004-Ein-Sitzungs-Recherche nicht auftauchten. |

---

## 8. Cross-Transfer-Synthese (A1–A3)

Ein einheitliches Muster zeigt sich über alle drei Transferfragen: Direkte Primärevidenz (Kategorie 1) im strengen, vom Auftrag definierten Sinn (exakter Zielkontext, expliziter Theorienname) fehlt in allen drei Fällen weiterhin. Das ist nach zwei zusätzlichen, unabhängigen Suchrunden je Teilpunkt eine robustere Aussage als der jeweilige Einzelbefund der W-Projekte allein (vierfache statt dreifache Konvergenz, wenn man diesen Audit als vierten unabhängigen Prüfschritt zählt).

Gleichzeitig widerlegt dieser Audit die stärkere Lesart „gar keine Evidenz vorhanden": In allen drei Fällen existiert **belastbare, akademisch verifizierbare indirekte Evidenz**, die in den jeweiligen W-Projekt-Recherchen (bewusst als „Ein-Sitzungs-Recherche, nicht systematisch" gekennzeichnet) nicht gefunden wurde. Diese indirekte Evidenz liegt durchgängig in strukturell sehr ähnlichen, aber nicht identischen Nachbarkontexten: professionelle/organisationale Entscheidungsträger statt expliziter Multi-Stakeholder-Buying-Center (A1); hochinvolvierte Finanzdienstleistungs-/Beratungskontexte statt der namentlich benannten Immobilien-/Hausbau-Kontexte (A2); cross-funktionale Sourcing-/Planungsteams statt expliziter SIT-Buying-Center-Studien (A3).

**Wichtige epistemische Einordnung:** Dieses Muster ist selbst informativ. Es deutet darauf hin, dass die B2B-/Vertikal-Transfer-Lücke weniger eine vollständige Forschungsleere ist als eine **Fragmentierung entlang von Fachbegriffen**: Die relevante Forschung existiert, wird aber unter anderen Bezeichnungen (Site-Selection-Manager statt Buying-Center-Mitglied; Premium-Banking-Kunde statt Hausbaukunde; S&OP-Team statt Buying Center) geführt und von der ursprünglichen Suchstrategie (die stärker an den Codex-eigenen Begriffen orientiert war) nicht erfasst. Dies ist eine Methodenbeobachtung, keine neue Theorieaussage.

---

## 9. CEB / Challenger Evidence Audit

### 9.1 Zentrale Fragestellungen — Kurzantworten

**1. Gibt es echte unabhängige Replikationen?** Nein — jedenfalls nicht für die 53/38/9-Zahlenaussage selbst. Der Originaldatensatz (N≈6.000 Verkäufer, ~90 Unternehmen) wurde ursprünglich nicht peer-reviewt, sondern 2009 als Kundenreport an CEB-Mitgliedsunternehmen veröffentlicht und erst 2011 in Buchform öffentlich gemacht. Eine vollständige methodische Offenlegung (Stichprobenziehung, Itemformulierung, statistisches Verfahren) wurde in dieser Recherche nicht gefunden.

**2. Gibt es akademische Kritik?** Ja, substanziell. Zentral: **Rapp, A., Bachrach, D. G., Panagopoulos, N. G. & Ogilvie, J. L. (2014). „Salespeople as knowledge brokers: A review and critique of the challenger sales model." *Journal of Personal Selling & Sales Management*, 34(4), 245–259.** Bibliografisch vollständig verifiziert (Semantic Scholar mit DOI 10.1080/08853134.2014.908126, 94 Zitationen, Volltext-Metadaten). Ausgezeichnet mit dem 2014 Marvin Jolson Award for Best Contribution to Selling and Sales Management Practice — ein Indikator für breite akademische Rezeption innerhalb der Vertriebsforschung, nicht nur Praktikerdiskussion. Die Autoren stellen fest, dass vor ihrer Arbeit „researchers have yet to complete a systematic, in-depth examination of the Challenger model" — bestätigt indirekt, dass vor 2014 keine systematische akademische Prüfung vorlag.

Zusätzlich identifiziert, mit Verifikationsvorbehalt: Ein Beitrag mit dem Titel „Challenger Selling: The Good; the Bad; the Ugly?" (Plank & Reid, ca. 2012) wird von mehreren Sekundärquellen (u. a. Semantic-Scholar-Referenzliste des Rapp-et-al.-Papers) als zitierte Referenz geführt. Die exakte Publikationsform (peer-reviewtes Journal vs. Konferenzbeitrag vs. Working Paper) konnte in dieser Sitzung **nicht abschließend verifiziert werden** — dieser Punkt wird als offene Verifikationslücke geführt, nicht als bestätigte zweite akademische Kritik.

**3. Gibt es methodische Kritik an der 53/38/9-Aufteilung spezifisch?** Keine Quelle wurde gefunden, die die exakte Kennzahl 53%/38%/9% eigenständig methodisch seziert (z. B. Itemvalidität, Varianzaufklärung, Stichprobenverzerrung dieser spezifischen Dreiteilung). Die vorhandene akademische Kritik (Rapp et al. 2014) bezieht sich auf das Challenger-Modell als Ganzes (Typologie, Kausalitätsanspruch, Konstruktvalidität der fünf Verkäuferprofile), nicht auf diese eine Kennzahl isoliert.

**4. Ist der Originaldatensatz zugänglich oder transparent dokumentiert?** Nein. Dies bestätigt den bereits im Repository dokumentierten Zustand (`SCIENTIFIC_DEBT.md`, A-0019, SD-SYS-001) unverändert.

**5. Sind Sampling, Operationalisierung und statistische Verfahren nachvollziehbar?** Nein, nicht auf Basis der öffentlich zugänglichen Buch-/Sekundärdarstellung. Dies deckt sich mit dem bestehenden Repository-Befund.

**6. Wie häufig werden Zahlen lediglich zirkulär weiterzitiert?** Sehr häufig — die überwältigende Mehrheit der in der Recherche gefundenen Web-Treffer zum 53%-Wert (Sales-Blogs, Methodik-Erklärseiten, Vertriebstrainer-Websites) zitiert die Zahl ohne jede eigene Prüfung oder zusätzliche Quelle weiter. Diese wurden gemäß Auftragsvorgabe **nicht** als Kategorie B4 oder B1/B2 gewertet, sondern korrekt als B6 (bloße Weiterzitation) erkannt und aus der Evidenzbewertung ausgeschlossen.

**7. Gibt es unabhängige Forschung, die zumindest die zugrunde liegenden Mechanismen bestätigt?** Teilweise, und dies ist bereits im Repository dokumentiert (Verbeke, Dietz & Verwaal 2011/Franke & Park 2006, ARS-0001): Adaptive-Selling-Verhalten und allgemeine Vertriebsleistungstreiber sind akademisch meta-analytisch gut belegt — aber diese Meta-Analysen bestätigen **nicht** die spezifische Challenger-Fünf-Profile-Taxonomie oder den 53%-Loyalitäts-Split, sondern andere, teils überlappende, teils abweichende Treiberkategorien (B2 — unabhängige akademische Teilbestätigung der zugrunde liegenden Logik, nicht des Originalbefunds).

**8. Trennung nach Claim-Baustein:** Erforderlich und im Folgenden vorgenommen.

### 9.2 Getrennte Bewertung der vier Claim-Bausteine

**Baustein 1 — CEB-Zahlenaussage (53%/38%/9%; Relationship Builder = 7% der Stars):** Keine unabhängige Replikation (B1) gefunden. Eine akademische Teilbestätigung der zugrunde liegenden Logik existiert (Franke & Park 2006; Verbeke et al. 2011 — bereits im Repository dokumentiert, B2), bestätigt aber nicht den Zahlenwert selbst. Akademische Kritik (Rapp et al. 2014) behandelt diesen Baustein im Rahmen der Gesamtmodellkritik, nicht isoliert. Originaldatensatz nicht zugänglich.

**Baustein 2 — Challenger-Typologie (fünf Profile):** Gegenstand der zentralen akademischen Kritik (Rapp et al. 2014, B3/B5). Diese Kritik stellt laut Sekundärbeschreibung die Konstruktvalidität und den Neuheitsanspruch der Typologie infrage („knowledge brokers" als alternative theoretische Einordnung des Kernphänomens). Keine unabhängige Replikation der Fünf-Profile-Struktur selbst gefunden.

**Baustein 3 — Commercial Teaching:** In dieser Recherche keine gesonderte, vom Gesamtmodell unabhängige akademische Prüfung gefunden. Dieser Baustein wird durch die vorhandene Rapp-et-al.-Kritik indirekt mitbehandelt (die Kritik bezieht sich laut Titel auf das Gesamtmodell „Challenger Sales Model", zu dem Commercial Teaching zentral gehört), aber keine isolierte Studie identifiziert.

**Baustein 4 — Buying Consensus / Mobilizer-Logik:** Diese Konzepte stammen aus dem Nachfolgebuch *The Challenger Customer* (2015, CEB-Team). Keine akademische Studie gefunden, die diese Konzepte unabhängig testet. Reiner Negativbefund (Kategorie 4 im Sinn von Prüfbereich A, analog auf B übertragen) — nicht als Gegenevidenz zu werten.

### 9.3 CEB-Bewertungsmatrix

Siehe Abschnitt 12.2.

---

## 10. Buying-Center Coalition Literature Audit

### 10.1 Kohli (1989) — Verifikationsstatus

**Kohli, A. (1989). „Determinants of Influence in Organizational Buying: A Contingency Approach." *Journal of Marketing*, 53(3), 50–65.**

Ein direkter Volltextzugriff auf diese Studie war in dieser Sitzung nicht möglich (Bezahlschranke). Die Kernaussage wurde jedoch **über eine unabhängige, im Volltext zugängliche Sekundärquelle verifiziert** (siehe 10.2): Cabanelas, Mora Cortez & Charterina (2023) zitieren Kohli (1989) wörtlich mit der Aussage, dass Expertenmacht der wichtigste Einflussfaktor in großen, kohäsiven, zeitlich nicht unter Druck stehenden Buying Centern ist, während Reinforcement Power (Belohnungs-/Bestrafungsmacht) in kleinen, wenig kohäsiven, zeitkritischen Buying Centern dominiert — und dass eine Feldstudie über 251 organisationale Kaufentscheidungen zugrunde liegt. Diese Zahlenangabe (N=251) und die Kernaussage stimmen mit einer zusätzlich unabhängig gefundenen SAGE-Publikationsseite überein. **Einschätzung:** Kohli (1989) ist eine gut etablierte, in der aktuellsten verfügbaren systematischen Übersichtsarbeit des Feldes (2023) weiterhin aktiv und unwidersprochen zitierte Primärstudie — kein Hinweis auf Widerruf, Kritik oder Nichtreplikation gefunden. Die im Repository (MEC-0014, W-004) offen gehaltene Frage „Volltextprüfung von Kohli (1989) steht aus" bleibt im strengen Sinn (eigener Volltextzugriff) unbeantwortet, wird aber durch diese unabhängige Zweitquelle substanziell erhärtet, nicht in Zweifel gezogen.

### 10.2 Cabanelas, Mora Cortez & Charterina (2023) — vollständige Volltextprüfung

**Cabanelas, P., Mora Cortez, R. & Charterina, J. (2023). „The buying center concept as a milestone in industrial marketing: Review and research agenda." *Industrial Marketing Management*, 108, 65–78.** DOI 10.1016/j.indmarman.2022.10.026. Open-Access-Volltext vollständig beschafft und gelesen (University of Southern Denmark Research Portal, CC-BY-Lizenz).

**Forschungsfrage:** (1) Welche zentralen Bausteine prägen die Buying-Center-Forschung im Marketing, und wie hängen sie zusammen? (2) Welche künftigen Herausforderungen bestehen, um erneutes Forschungsinteresse zu wecken?

**Theoretischer Rahmen:** Domänenbasierte systematische Literaturübersicht (nach Palmatier, Houston & Hulland 2018); Drei-Schichten-Modell (Konzeptualisierung, Prozess [Formation/Dynamik/Outcomes], Kontext).

**Methode:** Vier-Phasen-Prozess (Design, Durchführung, Analyse, Verfassen). Vorauswahl n=226 Artikel über EBSCO, Scopus, Web of Science, Google Scholar mit den Suchbegriffen „buying center", „buying centre", „decision making unit", „buying unit", „buying group" (Titel/Keywords/Abstract) in einer vordefinierten Journalliste (Top-Marketing-Journale, B2B-Marketing-Journale, AJG-2018-Ranking ≥3). Finale Auswahl n=89 Artikel nach Drei-Coder-Bewertung (Einschlusskriterium: Buying Center als Kernelement des Papers, Durchschnittsbewertung ≥3 auf 5er-Skala). Codierprotokoll extern validiert (Inter-Rater-Reliabilität).

**Zentrale Befunde:**
- Abnehmende Publikationszahlen seit den späten 2000er-Jahren; Top-Marketing-Journale „nahezu still" seit den frühen 1990er-Jahren.
- Bestehende integrative Reviews (z. B. Johnston & Lewin 1996) sind veraltet; empirische Artikel konvergieren nicht einheitlich in der Operationalisierung von Funktionen/Rollen.
- Macht und Einfluss (u. a. Kohli 1989, Venkatesh/Kohli/Zaltman 1995, McCabe 1987, Johnston & Bonoma 1981) werden als aktiver, wenn auch nicht wachsender Teilstrang geführt.
- Konflikt-Dynamik (Kommunikationsbarrieren zwischen Abteilungen, unterschiedliche „thought worlds", politische Informationsverarbeitung) wird als eigener, nach wie vor offener Forschungsstrang benannt.
- **Der Begriff „coalition" kommt im gesamten 89-Artikel-Review (1967–2021) an keiner Stelle vor.** Auch die im Repository (MEC-0014) als Koalitionsliteratur geführten Kernquellen Spekman & Stern (1979), Mummalaneni (1984), Morris & Freedman (1984) und Morris/Stanton/Calantone (1985) erscheinen **nicht** in der 226-Artikel-Vorauswahl oder der 89-Artikel-Endauswahl dieses Reviews. McCabe (1987) hingegen wird mehrfach zitiert und aktiv in die Zentralisierungs-Diskussion eingebunden.

**Kausalitätsanspruch:** Das Paper selbst erhebt keinen kausalen Anspruch — es ist eine deskriptive/integrative systematische Übersicht, kein Kausalmodelltest.

**Relevanz für MEC-0014:** Bestätigt direkt und im Volltext den in W-004 nur über Abstract/Sekundärquellen erschlossenen Befund zur rückläufigen Publikationsaktivität. Liefert zusätzlich eine wichtige, in W-004 nicht dokumentierte Präzisierung: Nicht das gesamte Buying-Center-Feld ist inaktiv — Macht-/Einfluss-/Konfliktforschung (Kohli-Linie) bleibt aktiv zitiert, während spezifisch die „Koalitions"-Terminologie/-Literaturlinie (Spekman & Stern, Mummalaneni, Morris & Freedman/Stanton/Calantone) in diesem maßgeblichen aktuellen Review nicht auftaucht.

**Grenzen dieser Prüfung:** Die Suchbegriffe des Reviews selbst enthielten nicht „coalition" — das Fehlen von Koalitions-Zitationen könnte teilweise ein Artefakt der eigenen Suchstrategie des Reviews sein (falls Koalitionspapiere nicht auch „buying center" im Titel/Abstract führen), nicht zwingend ein Beweis vollständigen Verschwindens dieser Literaturlinie aus der Gesamtliteratur. Diese Einschränkung wird in Abschnitt 15 explizit vermerkt.

### 10.3 Zusätzliche W-004-Scientific-Debt-Fragen

Die in `SCIENTIFIC_DEBT.md`, Sektion „W-004", offen gehaltene Frage zur Kausalrichtung Spekman & Stern (1979) vs. McCabe (1987) wird durch die Cabanelas-et-al.-Volltextprüfung **nicht aufgelöst**, aber indirekt gestützt: Cabanelas et al. (2023) referenzieren ausschließlich McCabe (1987) als aktive Quelle für den positiven Zusammenhang zwischen Unsicherheit und Zentralisierung — konsistent mit der bereits in MEC-0014 korrigierten Zuordnung (McCabe = positiver Befund; Spekman & Stern = keine empirische Unterstützung gefunden). Dies ist eine zusätzliche, unabhängige Bestätigung der bereits im Repository vorgenommenen Korrektur, keine neue Information.

---

## 11. Terminology Shift Analysis

**Zentrale Frage:** Ist die Koalitionsforschung verschwunden, oder hat sie sich terminologisch und theoretisch in Nachbarfelder verschoben?

**Befund: Beides, in unterschiedlichem Ausmaß.** Die spezifische Begriffskombination „buying center coalition"/„coalition formation" im industriellen Beschaffungskontext ist, soweit diese Recherche zeigen konnte, weitgehend aus der aktiven Zitationspraxis verschwunden (bestätigt durch Abschnitt 10.2). Gleichzeitig wurde das zugrunde liegende Phänomen — interne politische Dynamik, Statuskonflikte, Zielkonflikte und Konsensbildung in Gruppen, die Beschaffungs-/Sourcingentscheidungen treffen — in mindestens zwei methodisch modernen, aktiven Forschungslinien identifiziert, die unter neuer Begrifflichkeit dasselbe Grundphänomen untersuchen:

1. **Franke, H. & Foerstl, K. (2020). „Goals, Conflict, Politics, and Performance of Cross-Functional Sourcing Teams — Results from a Social Team Experiment." *Journal of Business Logistics*, 41(1), 6–30.** Strukturgleichungsmodell auf Basis eines Social-Team-Experiments mit N=468 Teilnehmenden. Untersucht explizit funktionale Zielinkongruenz, Konflikt und **„Politics"** (organisationspolitisches Verhalten) in cross-funktionalen Sourcing-Teams und deren Effekt auf Teamzufriedenheit, Rationalität und Performance-Outcomes — inhaltlich der historischen Koalitionsforschung (Spekman & Stern, Mummalaneni) sehr nahe, aber unter der Begrifflichkeit „Politics"/„Conflict" statt „Coalition".
2. **Franke, H., Eckerd, S. & Foerstl, K. (2022). „Rising to the Top: Motivational Forces Influencing Status Conflict in Sourcing Teams." *Production and Operations Management*.** Direkte Folgeuntersuchung zu Statuskonflikten in Sourcing-Teams — ebenfalls eine moderne, empirisch geprüfte Fortsetzung derselben Grundfragestellung (Wer setzt sich in einer Gruppe mit unterschiedlichen Interessen durch, und warum?) unter dem Begriff „Status Conflict" statt „Coalition Formation".
3. Ergänzend (aus Prüfbereich A3 bereits dokumentiert): Ambrose, Matthews & Rutherford (2018) — Social Identity Theory in S&OP-Teams; Meschnig & Kaufmann (2015) — Konsens in Sourcing-Teams.

**Einordnung:** Diese Forschungslinie (Franke, Foerstl, Eckerd und Koautoren, überwiegend *Journal of Business Logistics* und *Production and Operations Management*, 2020–2022) erscheint als die derzeit aktivste akademische Fortsetzung des Grundphänomens „Gruppendynamik/Macht/Politik in Beschaffungs-nahen Teams" — jedoch disziplinär stärker in Supply-Chain-Management/Operations-Forschung verankert als im klassischen Marketing-Buying-Center-Diskurs (Cabanelas et al. erscheinen in *Industrial Marketing Management*, Franke/Foerstl in *Journal of Business Logistics*/*Production and Operations Management*). Dies deutet auf eine **disziplinäre**, nicht nur terminologische Verschiebung hin: Das Phänomen wird zunehmend im SCM/Operations-Feld statt im Marketing-Feld untersucht.

---

## 12. Evidence Classification Matrix

### 12.1 Prüfbereich A — Transferfragen

| Prüfpunkt | Direkte Evidenz | Indirekte Evidenz | Gegenevidenz / Boundary Conditions | Keine Evidenz gefunden | Evidenzstärke | Empfehlung |
|---|---|---|---|---|---|---|
| A1 — ELM → B2B/Buying Center | Keine | Gilliland & Johnston (1997, konzeptionell); Wilson & Baack (2023, empirisch, Site-Selection-Manager) | Keine | Für echten Multi-Stakeholder-Buying-Center-Primärtest: ja | Niedrig-Mittel (gestiegen ggü. W-002 durch neue Kat.-2-Funde) | Scientific-Debt-Eintrag präzisieren (Kat.-2-Quellen ergänzen), nicht herabstufen |
| A2 — ABI-Trust → High-Ticket-B2C | Keine | Barnett White (2005); Ho & Wong (2022/23, Premium Banking); Finanzplaner-Trust-Linie | Keine | Für Immobilien/Hausbau spezifisch: ja | Niedrig-Mittel (gestiegen ggü. W-003 für weiter gefassten Kontext) | Scientific-Debt-Eintrag präzisieren; enger Immobilien-Negativbefund bleibt unverändert |
| A3 — Social Identity Theory → Buying Center | Keine | Ambrose, Matthews & Rutherford (2018, S&OP); Meschnig & Kaufmann (2015, Sourcing-Team-Konsens) | Keine | Für exakte SIT+Buying-Center-Kombination: ja | Niedrig-Mittel (gestiegen ggü. W-004) | Scientific-Debt-Eintrag präzisieren, Cross-Link zu Abschnitt 11 dieses Berichts |

### 12.2 CEB/Challenger — Bausteinbewertung

| Claim | Originalquelle | unabhängige Replikation | unabhängige Teilbestätigung | akademische Kritik | kommerzielle Replikation | bloße Weiterzitation | Bewertung |
|---|---|---|---|---|---|---|---|
| 53/38/9-Split (Kundenloyalität) | CEB-Kundenreport 2009 / Dixon & Adamson 2011, Datensatz nicht öffentlich | Keine gefunden | Ja (Franke & Park 2006; Verbeke et al. 2011 — bereits im Repository, bestätigt Logik nicht Zahl) | Ja, im Rahmen der Gesamtmodellkritik (Rapp et al. 2014) | Nicht systematisch geprüft, außerhalb Scope | Sehr häufig (Mehrheit der Web-Treffer) | Unverändert Priorität Hoch, Replikationsrisiko bestätigt |
| Challenger-Typologie (5 Profile) | Dixon & Adamson 2011 | Keine gefunden | Nicht spezifisch identifiziert | Ja, zentral (Rapp et al. 2014, JPSSM, Marvin-Jolson-Award) | Cars.com-Fallstudie (Isaac, Abraham & Richards 2019, JBIM) — Anwendungsfall, keine Replikation der Taxonomie | Häufig | Akademische Kritik jetzt konkret benannt und verifiziert — Scientific-Debt-Eintrag sollte dies aufnehmen |
| Commercial Teaching | Dixon & Adamson 2011 | Keine gefunden | Indirekt über Gesamtmodellkritik | Indirekt über Rapp et al. (2014) mitbehandelt, keine isolierte Studie | Nicht identifiziert | Häufig | Kategorie 4 (keine belastbare Evidenz gefunden, weder für noch gegen) |
| Buying Consensus / Mobilizer | Adamson/Dixon/Spenner/Toman 2015 (*The Challenger Customer*) | Keine gefunden | Keine gefunden | Keine gefunden | Nicht identifiziert | Häufig (Vertriebsblogs) | Kategorie 4 — reiner Negativbefund, kein Folgeforschungsprojekt automatisch ableiten |

### 12.3 Buying-Center-Koalitionsliteratur

| Prüfpunkt | Direkte Evidenz | Indirekte Evidenz | Gegenevidenz / Boundary Conditions | Keine Evidenz gefunden | Evidenzstärke | Empfehlung |
|---|---|---|---|---|---|---|
| Kohli (1989) Kernaussage | Nicht im Eigenvolltext, aber wörtlich bestätigt über Cabanelas et al. (2023) | — | Keine | Eigener Volltextzugriff weiterhin offen | Mittel-Hoch (unabhängig sekundärbestätigt) | OQ-4 (W-004) als „durch Sekundärquelle erhärtet, Volltextzugriff weiter offen" präzisieren |
| Aktualität Koalitionsfeld (Cabanelas et al. 2023) | Ja — Volltext vollständig geprüft | — | — | „Coalition"-Begriff: 0 Treffer in 89 Artikeln | Hoch (Volltext, systematische Methode, CC-BY) | OQ-3 (W-004) als vollständig beantwortet schließen (Empfehlung, keine Ausführung) |
| Terminologieverschiebung | — | Franke & Foerstl (2020); Franke, Eckerd & Foerstl (2022); Ambrose et al. (2018); Meschnig & Kaufmann (2015) | — | — | Mittel-Hoch | Neuer, punktueller Cross-Link-Vorschlag an MEC-0014 (Empfehlung, keine Ausführung) |

---

## 13. Auswirkungen auf bestehendes Scientific Debt

Empfehlungen an den Herausgeber — **keine Ausführung durch diesen Audit.**

| Betroffener Eintrag | Empfehlung | Begründung |
|---|---|---|
| `SCIENTIFIC_DEBT.md`, Sektion „W-002" (ELM→B2B/Buying-Center-Transferlücke) | **Präzisieren.** | Negativbefund für direkte Evidenz bestätigt; neu gefundene Kategorie-2-Quellen (Gilliland & Johnston 1997; Wilson & Baack 2023) sollten als „indirekte, nicht direkte Evidenz vorhanden" ergänzt werden. Nicht herabstufen (kein direkter Beleg), nicht hochstufen (kein neuer Kausalpfad). |
| `SCIENTIFIC_DEBT.md`, Sektion „W-003" (MEC-0030 High-Ticket-B2C-Evidenzlücke) | **Präzisieren.** | Enger Immobilien-/Hausbau-Negativbefund bleibt unverändert gültig; weiter gefasste „hochinvolvierte Beratungskontexte"-Lücke ist durch drei neue Quellen (Barnett White 2005; Ho & Wong 2022/23; Finanzplaner-Trust-Linie) teilweise geschlossen. |
| `SCIENTIFIC_DEBT.md`, Sektion „W-004" (Social Identity Theory→Buying-Center-Transferlücke) | **Präzisieren.** | Enger SIT+Buying-Center-Negativbefund bleibt gültig; zwei neue, thematisch sehr nahe Kategorie-2-Quellen (Ambrose et al. 2018; Meschnig & Kaufmann 2015) sollten ergänzt werden. |
| `SCIENTIFIC_DEBT.md`, Sektion „W-004", OQ-3 (Cabanelas-et-al.-Volltextprüfung) | **Als teilweise geschlossen markieren.** | Volltextprüfung wurde in diesem Audit vollständig durchgeführt; Kernbefund (rückläufiges Feld) bestätigt, zusätzlich präzisiert (Macht-/Einfluss-Teilstrang bleibt aktiv, „Koalition"-Terminologie verschwunden). |
| `SCIENTIFIC_DEBT.md`, Sektion „W-004", OQ-4 (Kohli-1989-Volltextprüfung) | **Präzisieren, nicht schließen.** | Eigener Volltextzugriff weiterhin nicht erfolgt; Kernaussage aber durch unabhängige, im Volltext geprüfte Sekundärquelle (Cabanelas et al. 2023) erhärtet — dies ist ein Zwischenschritt, kein vollständiger Abschluss. |
| `SCIENTIFIC_DEBT.md`, B-0004, A-0019 (CEB 53%/38%/9%-Replikationsrisiko) | **Unverändert lassen (Priorität Hoch bestätigt), aber Formulierung präzisieren.** | Bislang undifferenzierter Eintrag „keine externe Replikation bekannt" sollte um den jetzt konkret identifizierten und verifizierten akademischen Kritikpunkt (Rapp et al. 2014, JPSSM) ergänzt werden — dies ist keine Replikation, aber eine relevante, bislang nicht dokumentierte akademische Auseinandersetzung. |
| `SCIENTIFIC_DEBT.md`, SD-SYS-001 (proprietäre CEB-Studien) | **Unverändert lassen.** | Kein neuer Befund, der diese Einstufung ändert. |

---

## 14. Empfehlung zur nächsten Programmphase

**Primäre Empfehlung: Begrenztes, punktuelles Scientific-Debt-Update (kein neues W-Projekt, kein Architecture Freeze).**

**1. Was ist der nächste Schritt?** Ein kleiner, redaktioneller T3/T11-artiger Folgeauftrag, der die in Abschnitt 13 tabellierten Präzisierungsempfehlungen — nach Herausgeberprüfung und -freigabe — tatsächlich in `SCIENTIFIC_DEBT.md` und in den betroffenen Objekten (MEC-0014, MEC-0030, MOD-0002 und die ELM-Erweiterungsabschnitte in MEC-0005 bis MEC-0009) nachträgt, sowie die neu gefundenen Zitationen (Gilliland & Johnston 1997; Wilson & Baack 2023; Barnett White 2005; Ho & Wong 2022/23; Ambrose et al. 2018; Meschnig & Kaufmann 2015; Rapp et al. 2014; Cabanelas et al. 2023 mit vollständiger Zitation statt nur Abstract-Ebene) in `05_research/LITERATURE_INDEX.md` aufnimmt.

**2. Warum jetzt?** Dieser Audit hat für alle drei Scope-Punkte (a–c) neue, verifizierte, aber noch nicht in das Repository integrierte Evidenz gefunden. Diese Evidenz zu dokumentieren ist die naheliegende, risikoarme nächste Handlung, bevor eine größere Entscheidung (Freeze oder neues Forschungsprojekt) getroffen wird. Ein weiteres Liegenlassen würde denselben Zustand konservieren, den der Checkpoint 1 bereits als Anlass für diesen Audit benannt hatte.

**3. Welche Befunde tragen die Empfehlung?** Acht neue, bibliografisch verifizierte Quellen über die drei Prüfbereiche (A1: 2 Quellen; A2: 3 Quellen; A3: 2 Quellen; B: 1 zentrale Kritikquelle; C: 1 vollständig volltextgeprüfte Übersichtsarbeit plus 2 Terminologieverschiebungsquellen), die in den jeweiligen W-Projekten nicht gefunden wurden, aber keine davon verändert die bisherigen Kernentscheidungen (kein neues MEC, keine Integration einer B2B-Transferaussage) — sie präzisieren nur die Dokumentationslage.

**4. Warum nicht die wichtigsten Alternativen?**
- *Neues, umfassendes Forschungsprojekt (W-005) zu einem der drei Themen:* Nicht gerechtfertigt — keiner der drei Prüfpunkte liefert direkte (Kategorie 1) Evidenz, die eine tiefere Ausarbeitung rechtfertigen würde; die gefundene Evidenz ist durchgängig indirekt und reicht für eine einfache Dokumentationsergänzung.
- *Architecture Freeze:* Verfrüht — dieser Audit selbst hat neue, noch nicht integrierte Evidenz erzeugt; ein Freeze unmittelbar danach würde diese Erkenntnisse ungenutzt lassen. Zusätzlich bestehen laut Checkpoint 1 weiterhin zwei nicht-inhaltliche Governance-Hygiene-Lücken (veraltete Sessionstart-Dokumente, offene Open Decisions OD-008 Rest/OD-009–012), die unabhängig von diesem Audit vor einem Freeze zu klären wären.
- *Weiterer, größerer Evidence Check:* Nicht angezeigt — die Suchsättigung wurde in allen drei A-Teilbereichen und in Prüfbereich C erreicht (neue Suchrunden lieferten überwiegend Wiederholungen oder thematisch entferntere Treffer); ein noch umfangreicherer Check wäre unverhältnismäßig zum verbleibenden Erkenntnisgewinn.
- *Release-Readiness-Phase:* Nicht Gegenstand dieses Audits und weiterhin abhängig von den in Checkpoint 1 benannten, hier nicht behandelten Governance-Punkten.

**5. Welcher TASK_TYPE ist angemessen?** Für die Umsetzung der Präzisierungen: **T3_WARTUNG** für die reinen Zitationsergänzungen in `LITERATURE_INDEX.md` (mechanisch, keine inhaltliche Neubewertung); **T11_SCIDEBT** für die inhaltlichen Präzisierungen der Scientific-Debt-Einträge selbst (da diese eine begründete redaktionelle Einordnung der neuen Quellen erfordern, nicht nur mechanisches Einfügen).

**6. Welche Exit Criteria hätte die nächste Phase?** Alle in Abschnitt 13 tabellierten sieben Empfehlungen sind vom Herausgeber geprüft und (angenommen/abgelehnt/modifiziert) entschieden; die angenommenen Präzisierungen sind in den benannten Dateien nachgetragen; `LITERATURE_INDEX.md` enthält die acht neuen Quellen mit vollständiger Zitation und B2B-Transfer-Spalte; keine neue, unbelegte Behauptung wurde dabei eingeführt.

---

## 15. Unsicherheiten und Grenzen

- **Kein Zugriff auf strukturierte akademische Datenbanken** (Google Scholar, Scopus, Web of Science, EBSCO direkt) — alle Treffer stammen aus allgemeiner Websuche mit Verlags-/Repository-Snippets. Dies erhöht das Risiko, dass relevante, nicht gut suchmaschinenoptimierte Studien übersehen wurden, insbesondere ältere oder in Nicht-Marketing-Journalen publizierte Arbeiten.
- **Ein zentraler Quellenname (Autor der 1994-IMM-Studie zu A1) konnte nicht verifiziert werden** — dies wird transparent als Verifikationslücke geführt, nicht als bestätigtes Zitat behandelt.
- **Kohli (1989) wurde nicht im Eigenvolltext gelesen**, sondern über eine unabhängige, aber sekundäre Quelle (Cabanelas et al. 2023) erschlossen — dies ist eine Verbesserung gegenüber dem W-004-Zustand (reine Abstract-Ebene), aber kein vollständiger Abschluss der offenen Frage.
- **Plank & Reid „Challenger Selling: The Good; the Bad; the Ugly?" (ca. 2012)** konnte nicht bibliografisch vollständig verifiziert werden (Journal, Peer-Review-Status unklar) — nicht in die Bewertungsmatrix als bestätigte zweite akademische Kritik aufgenommen.
- **Das Fehlen des Begriffs „coalition" im Cabanelas-et-al.-Review** könnte teilweise methodisches Artefakt der eigenen Suchbegriffe dieses Reviews sein (siehe 10.2) — die stärkere Aussage „die Koalitionsliteratur ist inaktiv" stützt sich zusätzlich auf die in MEC-0014 bereits dokumentierte, ausschließlich historische (1979–1999) Datierung der Koalitionsquellen selbst, ist aber nicht durch eine eigene, gezielte Bibliometrie dieses Audits (z. B. Zitationszahlen pro Jahr für Spekman & Stern 1979 selbst) unabhängig bestätigt.
- **Die Terminologieverschiebungs-These (Abschnitt 11) beruht auf vier Quellen aus einem eng verwandten, aber nicht identischen Forschungscluster** (Franke/Foerstl/Eckerd, überwiegend SCM/Operations-Journale) — eine umfassendere Bibliometrie könnte weitere, hier nicht gefundene Cluster identifizieren.
- **Prüfbereich B beschränkt sich auf die vier explizit benannten Claim-Bausteine** — keine Aussage über weitere, im Buch enthaltene, aber nicht benannte CEB-Behauptungen.
- **Zeitliche Grenze:** Recherche durchgeführt am 2026-07-06 mit den zu diesem Zeitpunkt über die verfügbaren Suchwerkzeuge auffindbaren Quellen; nach diesem Datum publizierte Arbeiten sind naturgemäß nicht erfasst.

---

## 16. Vollständiges Suchprotokoll

**Plattform (alle Einträge, sofern nicht anders vermerkt):** `WebSearch` (allgemeine Websuche); Volltextabruf via `web_fetch` wo angegeben. **Suchdatum:** 2026-07-06 (durchgehend, eine Sitzung).

### A1 — ELM → B2B

| # | Suchbegriffe | Zweck | Zentrale Treffer | Ausgeschlossene Treffer (Grund) |
|---|---|---|---|---|
| 1 | "Elaboration Likelihood Model organizational buying B2B empirical test" | Breit, theoriegeleitet | ELM-Übersichten, keine B2B-Buying-Center-Primärstudie | Zahlreiche Konsumenten-/Online-Review-ELM-Studien (falscher Kontext) |
| 2 | "Elaboration Likelihood Model" "buying center" OR "industrial buying" OR "business-to-business" | Theoriegeleitet, Begriffsfamilie 2 | 1994-IMM-Studie; Gilliland & Johnston (1997) | Diverse B2C-E-Commerce-ELM-Studien |
| 3 | central route peripheral route processing organizational purchasing decisions argument quality | Kontextgeleitet | Allgemeine ELM-Erklärseiten, ein Hinweis auf B2B-Anwendung ohne Primärquelle | Populärwissenschaftliche Erklärseiten (keine Primärquelle) |
| 4 | source credibility expertise cues B2B sales persuasion professional purchasing | Kontextgeleitet, Begriffsfamilie 2 | Wilson & Baack (2023) über Folgesuche identifiziert | Vertriebs-Blogs (keine wissenschaftliche Quelle) |
| 5 | "Understanding the persuasion process between industrial buyers and sellers" (mehrere Varianten) | Vertiefung/Verifikation Quelle 1 | Titel/Journal/Jahr/DOI-Muster bestätigt, Autor nicht verifizierbar | — |
| 6 | Wilson Baack 2023 Journal of Business Research B2B communication effects model | Vertiefung/Verifikation | Autoren, Journal, Kernbefund bestätigt | — |
| 7 | "buying center" "elaboration likelihood" empirical study multiple stakeholders purchasing decision | Zusätzliche Sättigungsprüfung | Keine neuen Treffer über bereits gefundene hinaus | Allgemeine Buying-Center-Meta-Analysen ohne ELM-Bezug |
| 8 | "strategic purchasing" OR "professional procurement" persuasion argument quality involvement decision empirical | Sättigungsprüfung | Keine relevanten neuen Treffer (Supply-Chain-Performance-Literatur, falscher Fokus) | Ausgeschlossen: thematisch nicht Persuasion |
| 9 | Gilliland Johnston 1997 Toward a model ... elaboration likelihood buying center citing | Verifikation/Vorwärtsverfolgung | Autoren, Journal, Seiten bestätigt; Zitat zu Buying-Center-Bezug bestätigt | — |
| 10 | Revisiting the theory of business-to-business advertising Reid Plank OR Lohtia | Vorwärtsverfolgung | Mora Cortez, Gilliland & Johnston (2019) identifiziert | Autorennamen „Reid Plank/Lohtia" nicht bestätigt, nicht verwendet |

### A2 — ABI-Trust → High-Ticket-B2C

| # | Suchbegriffe | Zweck | Zentrale Treffer | Ausgeschlossene Treffer |
|---|---|---|---|---|
| 1 | "ability benevolence integrity" trust real estate agent OR "residential construction" empirical study | Theoriegeleitet | Keine direkten Treffer für Immobilien/Hausbau | Allgemeine ABI-Netzwerkstudien (falscher Kontext) |
| 2 | Mayer Davis Schoorman trust model financial advisor OR mortgage OR wealth management empirical test | Theoriegeleitet, Begriffsfamilie 2 | Allgemeine ABI-Übersichten, kein direkter Treffer | — |
| 3 | homebuyer trust real estate agent ability benevolence OR trustworthiness empirical survey | Kontextgeleitet | Nur Praktiker-/Verbands-Umfragen (NAR), keine akademische ABI-Studie | NAR-Umfrage nicht als wiss. Primärquelle gewertet |
| 4 | "credence services" consumer trust professional financial advisor insurance ABI trustworthiness model | Kontextgeleitet, Begriffsfamilie 2 | Keine akademische Studie mit diesem Begriffscluster gefunden | Kommerzielle Finanzberatungs-Websites |
| 5 | consumer trust financial advisor competence benevolence integrity high involvement purchase decision study | Vertiefung | Barnett White (2005) identifiziert | — |
| 6 | Barnett White 2005 Consumer Trust and Advice Acceptance domain medical financial decision high stakes abstract | Verifikation | Kernbefund, Journal, Jahr bestätigt | — |
| 7 | "financial planning" trust commitment structural equation modeling antecedents ability benevolence integrity client 2022 | Vertiefung | FPA-Update 2022, Sharpe et al. 1998 (JFCP) identifiziert | — |
| 8 | insurance advisor OR "private banking" OR "wealth management" client trust ability benevolence integrity academic study | Kontextgeleitet, Begriffsfamilie 3 | Ho & Wong (2022/23) identifiziert | Industrie-Websites (Morgan Stanley u. a., nicht akademisch) |
| 9 | homebuilder OR residential construction trust builder buyer ability benevolence integrity study | Sättigungsprüfung | Keine akademische Studie gefunden, nur Plattformen (TrustBuilder) | Kommerzielle Bewertungsplattformen |
| 10 | "role of customer personality in premium banking services" Journal of Financial Services Marketing author year | Verifikation | Ho & Wong, Journal, Jahr, N=210 bestätigt | — |

### A3 — Social Identity Theory → Buying Center

| # | Suchbegriffe | Zweck | Zentrale Treffer | Ausgeschlossene Treffer |
|---|---|---|---|---|
| 1 | "social identity theory" "buying center" organizational buying empirical study | Theoriegeleitet | Keine direkten Treffer | Konsumenten-Markenidentitäts-Studien (falscher Kontext) |
| 2 | self-categorization theory OR "social identity" procurement team cross-functional purchasing decision empirical | Theoriegeleitet, Begriffsfamilie 2 | Ambrose, Matthews & Rutherford (2018); „Social cross-functional vendor selection" (2022) identifiziert | — |
| 3 | "Cross-functional teams and social identity theory" "sales and operations planning" author journal citation abstract | Verifikation | Autoren, Journal, DOI, Abstract bestätigt | — |
| 4 | "Social cross-functional vendor selection in technologically uncertain sourcing situations" author abstract social identity | Vertiefung | Fallstudie bestätigt, aber keine explizite SIT-Rahmung erkennbar | Nicht als SIT-Direkttreffer gewertet |
| 5 | "Consensus on supplier selection objectives in cross-functional sourcing teams" antecedents outcomes author journal abstract | Kontextgeleitet, Begriffsfamilie 3 | Meschnig & Kaufmann (2015) vollständig bestätigt (N, Journal, Kernbefund) | — |
| 6 | functional identity conflict cross-functional purchasing team faultlines subgroup organizational buying | Kontextgeleitet, Begriffsfamilie 4 | Allgemeine Faultline-Literatur (Bezrukova et al.) identifiziert, nicht procurement-spezifisch | Nicht in Hauptmatrix aufgenommen (zu allgemein) |

### B — CEB/Challenger

| # | Suchbegriffe | Zweck | Zentrale Treffer | Ausgeschlossene Treffer |
|---|---|---|---|---|
| 1 | Challenger Sale CEB "53%" loyalty independent academic replication critique | Breit | Keine akademische Replikation, nur Praktikerquellen | Blogs/Zusammenfassungen (B6-Kategorie) |
| 2 | "Challenger sales" Dixon Adamson academic critique methodology sampling peer review | Vertiefung | Hinweis auf Adamson-Zitat zu Akademikerkritik (Quelle nicht abschließend verifiziert) | — |
| 3 | Brent Adamson "that is what the academics are criticizing" interview source | Verifikationsversuch | Nicht abschließend verifiziert (HBR-Artikel „The End of Solution Sales" als wahrscheinliche Quelle identifiziert, exaktes Zitat nicht bestätigt) | Zitat nicht in Bericht als bestätigt übernommen |
| 4 | "insight selling" OR "Challenger" sales typology academic peer-reviewed test "Journal of Personal Selling" | Zentral | Rapp, Bachrach, Panagopoulos & Ogilvie (2014) identifiziert | — |
| 5 | Rapp Bachrach Panagopoulos Ogilvie 2014 knowledge brokers challenger critique findings weaknesses abstract summary | Verifikation | Vollständige Zitation, DOI, 94 Zitationen, Award bestätigt (Semantic Scholar) | — |
| 6 | Plank Reid 2012 "Challenger Selling: The Good; the Bad; the Ugly" critique summary | Vertiefung | Titel bestätigt, Publikationsvenue nicht abschließend verifiziert | Nicht als bestätigte zweite Kritik in Matrix aufgenommen |
| 7 | Inks Avila Talbert 2019 "evolution of the sales process" relationship selling Challenger empirical findings | Vertiefung | Autoren, Journal bestätigt, primär konzeptioneller Vergleich | — |
| 8 | "buying consensus" "mobilizer" Challenger Customer academic independent study test | Baustein 4 | Keine akademische Studie gefunden — reiner Negativbefund | Praktiker-/Blog-Erklärungen von „Mobilizer"-Konzept |
| 9 | Verbeke Dietz Verwaal 2011 meta-analysis salesperson performance determinants loyalty CEB critique | Bestätigung bestehender Repository-Quelle | Vollständige Zitation bestätigt (bereits im Repository dokumentiert) | — |
| 10 | CEB Challenger Sale original survey data methodology published transparency sampling N=6000 available | Frage 4/5 | Bestätigt: 2009 Kundenreport, keine volle methodische Transparenz | — |

### C — Buying-Center-Koalition

| # | Suchbegriffe | Zweck | Zentrale Treffer | Ausgeschlossene Treffer |
|---|---|---|---|---|
| 1 | Kohli 1989 "Determinants of Influence in Organizational Buying" Journal of Marketing findings expert power | Volltextversuch/Verifikation | Kernaussage über SAGE-Metadaten bestätigt (N=251, Expert/Reinforcement Power) | Bezahlschranke — kein Eigenvolltext |
| 2 | Cabanelas Mora Cortez Charterina 2023 Industrial Marketing Management buying center coalition research field decline | Volltextbeschaffung | **Vollständiger Open-Access-Volltext beschafft und gelesen** | — |
| 3 | (Volltextlektüre, interne Grep-Suche nach „coalition", „Kohli", „Spekman", „McCabe", „conflict", „consensus", „stakeholder") | Inhaltsanalyse | Vollständige Ergebnisse in Abschnitt 10.2 dokumentiert | — |
| 4 | "political behavior" organizational buying OR procurement coalition formation modern research 2015..2024 | Terminologieverschiebung, Begriffsfamilie 1 | Franke & Foerstl (2020) identifiziert; historische Koalitionsquellen (Mummalaneni, Morris & Freedman) als Sekundärtreffer bestätigt | — |
| 5 | "stakeholder alignment" OR "strategic consensus" buying center purchasing decision organizational research recent | Terminologieverschiebung, Begriffsfamilie 2 | Überwiegend Praktikerquellen, keine neue akademische Primärquelle | B2B-Vertriebs-Blogs |
| 6 | Franke 2020 Journal of Business Logistics "Goals, Conflict, Politics..." abstract findings | Verifikation | Vollständige Zitation, Abstract, N=468 bestätigt; Folgestudie 2022 identifiziert | — |

---

## 17. Abschlussprüfung (interne Checkliste, gemäß Auftrag)

1. Prüfbereiche A, B, C vollständig bearbeitet — erfüllt.
2. A1, A2, A3 mit je mindestens zwei unabhängigen Suchdurchläufen — erfüllt (Abschnitt 16).
3. Direkte/indirekte Evidenz, Gegenevidenz und Nicht-Fund sauber getrennt — erfüllt (Abschnitte 5–7, 12).
4. Bei CEB keine bloße Weiterzitation als Replikation gewertet — erfüllt (Abschnitt 9, Matrix 12.2).
5. Bei Koalitionsliteratur Terminologieverschiebung explizit geprüft — erfüllt (Abschnitt 11).
6. Primärquellen gegenüber Sekundärquellen priorisiert, wo verfügbar (Cabanelas-Volltext) — erfüllt.
7. Negativbefunde epistemisch vorsichtig formuliert — erfüllt (durchgängig „nicht gefunden" statt „existiert nicht").
8. Keine Datei außerhalb dieses Auditberichts verändert — erfüllt (ausschließlich lesender Zugriff auf Repository während dieser Sitzung).
9. Bericht endet mit genau einer primären Programme Recommendation — erfüllt (Abschnitt 14).

---

*Ende des Auditberichts. Dieser Bericht trifft keine Herausgeberentscheidung, ändert keine bestehenden Repository-Inhalte und aktiviert kein neues Forschungsprojekt. Empfohlene Folgemaßnahmen (Abschnitt 13, 14) sind Empfehlungen an den Herausgeber, keine Ausführungen. Auftrag endet mit Fertigstellung dieses Dokuments.*
