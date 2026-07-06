# Open Decisions

Offene Entscheidungen, die nach Abschluss von Influence durch den Herausgeber zu treffen sind.
Neue Entscheidungen unten anfügen. Erledigte Entscheidungen als DONE markieren.

**Governance-Hinweis (2026-07-02):** Im Rahmen des OPEN DECISIONS RESOLUTION SPRINT wurde jede Entscheidung unten einzeln geprüft. Ursprünglicher Text bleibt vollständig erhalten (Prinzip: nicht rückwirkend glätten); jede geprüfte Entscheidung erhält einen Abschnitt „Auflösung (Governance-Sprint 2026-07)" mit Status, Begründung und Datum. Vollständiger Bericht: `00_project/OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`.

---

## OD-001 — Post-Mortem nach Influence

**Status:** ~~Offen — nach Abschluss TASK-0010 fällig~~ → **DONE (2026-06-30)**

**Frage:** Durchführung eines strukturierten Post-Mortems für B-0002 (Influence).

**Agenda:** `00_project/POST_MORTEM_INFLUENCE_PLAN.md`

**Abhängigkeit:** TASK-0010 abgeschlossen

### Auflösung (Governance-Sprint 2026-07)

**Status: DONE.** TASK-0010 wurde am 2026-06-30 abgeschlossen (BOOK_REVIEW_REPORT_B0002.md). Das Post-Mortem wurde durchgeführt und vollständig dokumentiert: `00_project/POST_MORTEM_B0002.md` (12 Workflow-Phasen, Architekturreview, CKM-Review, Ablauf-Review, Stateless-Architecture-Review, 6 Priorität-A-, 6 Priorität-B-Empfehlungen, 5 Priorität-C-Ideen). Die ursprüngliche Frage ist objektiv und vollständig beantwortet — keine Restlücke.

---

## OD-002 — Book Mode offiziell einführen

**Status:** ~~Offen — nach Post-Mortem~~ → **DONE (2026-06-30)**

**Frage:** Soll der "Book Mode" (vollständiger Workflow von SRC bis BOOK_REVIEW ohne Zwischenfreigaben) als offizieller Modus in das Operating Manual aufgenommen werden?

**Kontext:** B-0002 ist der erste Lauf des neuen Workflows. Das Post-Mortem evaluiert, ob der Modus funktioniert hat.

**Dokumente zu aktualisieren (nach Freigabe):**
- `00_project/SALES_CODEX_OPERATING_MANUAL.md`
- `00_project/COWORK_EXECUTION_PROTOCOL.md`
- `00_project/task_rules.md`

### Auflösung (Governance-Sprint 2026-07)

**Status: DONE.** Book Mode wurde mit dem Sales Codex OS v1.1 Release (2026-06-30) offiziell eingeführt: `SALES_CODEX_OPERATING_MANUAL.md` Abschnitt 10 (neu), `COWORK_EXECUTION_PROTOCOL.md` Abschnitt 8 (neu), `task_rules.md` Abschnitt 10 (neu) — bestätigt in `00_project/changelog.md`, Eintrag 2026-06-30. Alle drei in der ursprünglichen Frage genannten Dokumente wurden tatsächlich aktualisiert. Seither in sieben weiteren Buchanalysen angewendet (B-0003 Never Split the Difference bis B-0010 Thinking, Fast and Slow). Der Modus hat sich in der Praxis etabliert — keine Restlücke.

---

## OD-003 — Framework v1.1 einfrieren

**Status:** ~~Offen — nach Post-Mortem und OD-002~~ → **DONE (2026-06-30), mit dokumentierter Restlücke**

**Frage:** Nach Integration der Post-Mortem-Erkenntnisse: Framework v1.1 einfrieren.

**Inhalte von v1.1 (vorläufig):**
- Book Mode dokumentiert
- Stateless Agent Architecture dokumentiert
- Canonicalisierungsregeln präzisiert
- Zwischenfreigaben abgeschafft (außer bei Abbruchbedingungen)
- BOOK_REVIEW als Endstatus definiert
- Repository Health Check verpflichtend

### Auflösung (Governance-Sprint 2026-07)

**Status: DONE — die Freeze-Entscheidung wurde objektiv umgesetzt**, mit einer dokumentierten Ausnahme. `CURRENT_STATE.md` (Kopfzeile) bestätigt: „Workspace-Version: 1.1 (freigegeben 2026-06-30)". Prüfung der sechs geplanten Inhalte:

| Inhalt | Status | Beleg |
|---|---|---|
| Book Mode dokumentiert | ✓ Umgesetzt | Operating Manual Abschnitt 10, COWORK_EXECUTION_PROTOCOL Abschnitt 8, task_rules.md Abschnitt 10 |
| Stateless Agent Architecture dokumentiert | ✓ Umgesetzt | PROJECT_BOOTSTRAP.md, CURRENT_STATE.md, NEXT_ACTION.md, OPEN_DECISIONS.md, SESSION_LOG.md (seit 2026-06-30 in Betrieb) |
| Canonicalisierungsregeln präzisiert | ✓ Umgesetzt | `canonical_knowledge_model.md` Abschnitt 9 „Nicht-Anlage-Dokumentation" |
| Zwischenfreigaben abgeschafft | ✓ Umgesetzt | Deckungsgleich mit Book Mode (OD-002) |
| BOOK_REVIEW als Endstatus definiert | ✓ Umgesetzt | `book_review_template.md`, seither bei jeder Buchanalyse verwendet |
| Repository Health Check verpflichtend | ✗ **Nicht umgesetzt** | `POST_MORTEM_B0002.md`, Phase 11: „Der Repository Health Check ist kein formaler Schritt im aktuellen Workflow… Es gibt kein explizites Health-Check-Protokoll." Dieser Zustand hat sich seither nicht geändert. |

Fünf von sechs Inhalten sind vollständig umgesetzt; die Freeze-Entscheidung selbst wurde vollzogen und trägt seit acht Buchanalysen die Frameworkarbeit. Die Restlücke (kein formales Health-Check-Protokoll) wird hier dokumentiert statt geglättet, begründet aber **keine neue Open Decision** — es ist ein operativer Nacharbeitspunkt (Prozessschritt-Formalisierung), keine Architekturentscheidung. Nachverfolgung erfolgt über `NEXT_ACTION.md`.

---

## OD-004 — Nächstes Buch

**Status:** ~~Offen — nach Framework v1.1 Freeze~~ → **DONE (2026-06-30)**

**Frage:** Welches Buch wird als B-0003 analysiert?

**Kandidaten (nicht priorisiert):** Challenger Sale, Never Split the Difference, Gap Selling, Pitch Anything, Pre-Suasion (Cialdini 2), Thinking Fast and Slow (Kahneman).

### Auflösung (Governance-Sprint 2026-07)

**Status: DONE.** Die ursprüngliche Einzelfrage wurde beantwortet: B-0003 = Never Split the Difference (Voss/Raz), gestartet und abgeschlossen 2026-06-30. Von den sechs genannten Kandidaten wurden inzwischen vier weitere ebenfalls verarbeitet (Challenger Sale = B-0004, Gap Selling = B-0005, Pre-Suasion = B-0008, Thinking Fast and Slow = B-0010); nur „Pitch Anything" wurde nie aufgegriffen. Für die Bücher nach B-0003 wurde kein Rückgriff mehr auf diese OD genommen — die Auswahl folgte stattdessen einem etablierten Verfahren (Editor-Priorisierung + Empfehlungen aus `research_agenda.md`, S1-SYNTHESIS). Diese OD ist damit nicht nur beantwortet, sondern durch ein dauerhaftes Nachfolgeverfahren funktional abgelöst — es besteht keine offene Einzelentscheidung mehr.

---

## OD-005 — Gemini-Validierung der Mechanismen

**Status:** ~~Offen — nicht terminiert~~ → **ERSETZT (2026-07-02) durch OD-010**

**Frage:** Gemini-Validierung für Replikationsstatus der Cialdini-Mechanismen (insbes. MEC-0005, MEC-0006, MEC-0007, MEC-0008) ist in mehreren Objekten als "ausstehend" markiert. Soll das als eigener Validierungs-Task (VAL-0003) eingeplant werden?

**Kontext:** Im Rahmen des aktuellen Workflows wird Gemini-Validierung nicht als Pflicht-Schritt behandelt — sie ist als Empfehlung in den VAL-Objekten dokumentiert.

### Auflösung (Governance-Sprint 2026-07)

**Status: ERSETZT.** Die wörtliche Frage („Gemini als dedizierter VAL-0003-Task") wurde nie so umgesetzt — Gemini wurde in keinem dokumentierten Sprint tatsächlich eingesetzt, und einzelne MEC-Dateien (z. B. `MEC-0005_reciprocation_obligation.md`, Abschnitt „Evidenzlevel") tragen weiterhin wörtlich den Platzhaltersatz „Gemini-Validierung … ausstehend". Gleichzeitig wurde die *inhaltliche Absicht* hinter OD-005 — unabhängige externe Validierung der Cialdini- und Voss-Mechanismen — über andere Instrumente bereits erheblich vorangetrieben:

- Peer Review Sprint 1 (2026-07-01): MEC-0010 E3 → E2 herabgestuft, mit expliziter Begründung.
- Academic Recovery Sprint Phase 2 / Research Pack 3 & 4 (2026-07-01): unabhängige, websuchverifizierte Konvergenzbestätigung für MEC-0005, MEC-0006, MEC-0007, MEC-0008, MEC-0010, MEC-0011 (siehe `05_research/LITERATURE_INDEX.md`, `ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`).
- Sprint-3-Review (2026-07-01): MEC-0011 erneut geprüft, Language-Style-Matching-Literatur ergänzt.

Diese Instrumente haben die Kernfrage von OD-005 (bedarf es unabhängiger externer Prüfung?) mit Ja beantwortet und bereits praktisch umgesetzt — nur nicht über das ursprünglich vorgeschlagene Werkzeug (Gemini). Eine eigenständige OD-005 auf Gemini als Instrument wäre daher redundant. Diese OD wird durch **OD-010 — Validierungs-Governance** ersetzt, die die grundsätzlichere, langfristig relevante Frage stellt: welche Instrumente/Kadenz künftig als hinreichend gelten. Die textlichen Platzhalter-Reste in einzelnen MEC-Dateien sind ein redaktioneller Nacharbeitspunkt (kein Architekturthema) und werden hier vermerkt, nicht als eigene Open Decision geführt.

---

## OD-006 — Meme-Filter für QK-Rating-System

**Status:** ~~Offen — Herausgeber-Entscheidung erforderlich~~ → **ANGENOMMEN (2026-07-03) — Umsetzung ausstehend**
**Eingetragen:** 2026-07-01 (Peer Review Decision Report Sprint 1)

**Ausgangspunkt:** Der Peer Reviewer von Sprint 1 identifiziert ein methodologisches Risiko: Wenn drei Practitioner-Bücher (die nachweislich voneinander abschreiben oder auf denselben US-amerikanischen Corporate-Trainings-Zeitgeist reagieren) denselben Effekt behaupten, steigt das QK-Rating auf QK-3. Dies suggeriert fälschlicherweise wissenschaftliche Validität durch Konsens, wo eventuell nur eine erfolgreiche Meme-Replikation vorliegt.

**Konkrete Beispiele im Repository:**
Cialdini (1984) → Voss (2016, referenziert Cialdini) → Keenan (2018) — alle konvergieren auf ähnliche COI/Dringlichkeits-Narrative. Ist das echte unabhängige Beobachtung oder gemeinsamer Ursprung?

**Mögliche Maßnahme:** Neues Metadaten-Feld in QK-Objekten: `meme_risiko: hoch / mittel / niedrig` mit Begründung. Dies wäre eine Framework-Änderung (neues Template-Feld, neues Bewertungskriterium).

**Editor-Einschätzung:** Intellektuell valide. Umsetzung wäre eine Framework-Änderung → Operating Manual Abschnitt 8 verbietet eigenständige Modifikation. Herausgeber-Entscheidung erforderlich.

**Frage an Felix:** Soll ein Meme-Filter-Feld in das QK-Rating-System eingeführt werden? Wenn ja: welches Format, welche Bewertungsskala?

**Update ARS-0001 (2026-07-01):** Das wissenschaftliche Gutachten nach Sprint 2 wirft einen verwandten, aber nicht identischen Punkt auf: das Risiko, dass Wissensobjekte sich zu stark an der Nomenklatur einzelner Autoren statt am dahinterliegenden Konstrukt orientieren ("Begriffsinflation", niedrige 4%-Canonicalization-Rate als Symptom). Beide Sorgen (Meme-Replikation als Schein-Konvergenz; Begriffsinflation als Schein-Eigenständigkeit) betreffen dieselbe Grundfrage: Wie unterscheidet der Codex "echte" von "scheinbarer" konzeptueller (Un-)Abhängigkeit? Empfehlung: Beide Aspekte gemeinsam in einer künftigen Herausgeber-Entscheidung behandeln, statt zwei separate Felder/Kriterien zu entwickeln. Siehe `PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`, Empfehlung 4.

### Auflösung (Governance-Sprint 2026-07)

**Status: OFFEN — entscheidungsreif.** Gemäß Sprintvorgabe wird OD-006 nicht automatisch geschlossen. Seit dem letzten Update (2026-07-01) gibt es keine neuen Entwicklungen, die die Frage implizit beantwortet hätten — kein Meme-Risiko-Feld wurde eingeführt, keine Framework-Änderung vorgenommen. Die fachliche Analyse ist vollständig; die im Update dokumentierte Empfehlung (gemeinsame Behandlung mit der Begriffsinflations-Frage) bleibt gültig und wird nicht eigenständig vorweggenommen. Diese Entscheidung ist reif für eine Herausgeber-Entscheidung, bleibt aber bis dahin OFFEN.

### Herausgeberentscheidung (Final Pre-Release Sprint, 2026-07-03)

**Status: ANGENOMMEN.** Felix hat entschieden: Der Meme-Filter wird Bestandteil des QK-Rating-Systems. Ziel ist ausschließlich, wissenschaftliche Qualität von Popularität, Verbreitung oder wirtschaftlichem Erfolg zu entkoppeln. Der Meme-Filter ist **kein eigenes Evidenzkriterium**, sondern ein Korrekturmechanismus innerhalb des bestehenden Bewertungssystems.

**Umsetzungsstatus:** Ausdrücklich **nicht Bestandteil dieses Sprints**. Die Einführung des Meme-Filters ist eine Framework-Änderung (QK-Rating-System) und fällt damit außerhalb des Scopes des Final Pre-Release Sprints (der ausschließlich Konsistenzarbeit vor dem RC-1-Audit umfasst — siehe Sprintauftrag, Abschnitt „Nicht zulässig"). Die technische Umsetzung (Definition des Korrekturmechanismus, betroffene Dokumente, ggf. Anwendung auf bestehende QK-bewertete Objekte) erfolgt in einem separaten Framework Integration Sprint nach Abschluss von Version 1.0.

**Für den RC-1-Audit relevant:** OD-006 ist nicht mehr offen im Sinne einer ausstehenden Herausgeber-Entscheidung — die Entscheidung liegt vor. Offen ist ausschließlich die technische Umsetzung, die bewusst auf einen Folgesprint verschoben wurde.

---

## OD-007 — Kontext-/Domänen-Modifikator-Ebene (CTX)

**Status:** ~~Offen — Herausgeber-Entscheidung erforderlich (ausdrücklich NICHT als Framework-Änderung umgesetzt)~~ → **ANGENOMMEN (2026-07-03) — Umsetzung ausstehend**
**Eingetragen:** 2026-07-01 (Wissenschaftliches Gutachten nach Sprint 2, ARS-0001)

**Ausgangspunkt:** Das Gutachten (`WISSENSCHAFTLICHES_GUTACHTEN_SALES_CODEX.md`, Abschnitt 2 und 10, Kategorie B) fordert eine neue Modell-Ebene CTX zwischen/parallel zu Prinzipien (P) und Techniken (T): strukturelle Kontextattribute (z.B. Transaktionsvolumen/ACV, Buying-Center-Größe, regulatorischer Rahmen), die jedes P- und T-Objekt verpflichtend tragen müsste. Begründung des Reviewers: Das System vermenge fundamentale Laborbefunde (Kahneman, Cialdini) unzulässig mit komplexen B2B-Interaktionen (Dixon, Rackham) — ohne formale Kontextschranke drohe unzulässige Universalisierung von Einzeleffekten.

**Auftrag für ARS-0001:** CTX ausdrücklich **nicht** einführen. Stattdessen ausschließlich bewerten, ob eine solche Ebene wissenschaftlich gerechtfertigt wäre.

### Wissenschaftliche Bewertung

**Für die Einführung spricht:**

- Der Grundbefund ist zutreffend: Der Reifegradbericht bewertet „Generalisierbarkeit" bereits selbst mit C+ (schwächste von sechs Dimensionen) und benennt die B2B-Transferlücke explizit als strukturelles Problem (Reifegradbericht Abschnitt 1.5, 4).
- Akademische Stützung existiert: Marcos-Cuevas et al. (2023, „Reclaiming the contingent nature of the determinants of salesperson performance", JPSSM 44(4) — verifiziert in ARS-0001/Research Pack 1) etabliert empirisch eine Drei-Klassen-Taxonomie von Erfolgstreibern (universal / kontextspezifisch / notwendig-aber-nicht-hinreichend) über 150 Studien und 936 Effekte. Das zeigt: Die akademische Vertriebsforschung behandelt Kontextspezifität als eigene, messbare Kategorie — nicht als bloßes Rauschen. Das stärkt die grundsätzliche wissenschaftliche Berechtigung der CTX-Frage unabhängig vom Sales Codex.
- Der Codex hat bereits einen unstrukturierten Vorläufer: `evidence_system.md` kennt die Dimension „Kontext" (universell/kontextabhängig/branchenspezifisch/situationsgebunden) je Aussage, und P-Objekte wie P-S1-003 führen bereits Freitext-Abschnitte „Kontextgrenzen". CTX wäre in diesem Sinne eine Formalisierung eines bereits vorhandenen, aber unstrukturierten Prinzips — keine Erfindung einer neuen Kategorie aus dem Nichts.

**Gegen eine (vorschnelle) Einführung spricht:**

- **Fehlende empirische Granularität:** Eine strukturierte Pflichtangabe wie „ACV > $100k, Buying Center > 3 Personen" (Beispiel des Reviewers) würde für die meisten der 21 MECs und ~47 Prinzipien eine Präzision suggerieren, die durch keine im Repository verarbeitete Quelle tatsächlich gemessen wurde. Keine der zehn analysierten Bücher liefert kalibrierte Schwellenwerte für ACV oder Buying-Center-Größe als Moderatorvariable. Eine erzwungene Pflichtangabe würde entweder (a) auf Schätzungen ohne Evidenzbasis beruhen — ein Verstoß gegen „Keine unbelegte Verallgemeinerung" in die andere Richtung — oder (b) bei den meisten Objekten als „unbekannt" markiert werden müssen, was den praktischen Nutzen der Pflichtangabe zum jetzigen Zeitpunkt einschränkt.
- **Kosten-Nutzen:** Eine verpflichtende neue Pflichtdimension für alle P- und T-Objekte (Operating Manual Schritt 5–6) wäre eine Framework-Änderung mit Rückwirkung auf ~47 bestehende Prinzipien und ~41 Techniken — erheblicher Nacharbeitsaufwand ohne, dass für die meisten Objekte neue Primärquellen zur Kalibrierung vorlägen.
- **Redundanzrisiko mit Bestehendem:** Die bereits vorhandenen Freitext-Kontextgrenzen-Abschnitte (s.o.) leisten inhaltlich einen Teil dessen, was CTX strukturell erzwingen würde — nur unstrukturiert. Es ist nicht ausgemacht, dass eine strukturierte Pflichtangabe gegenüber gutem Freitext einen Wissenschaftlichkeitsgewinn bringt, solange die zugrunde liegende Evidenz ohnehin nicht granular genug ist.

### Editor-Einschätzung

Die CTX-Frage ist **wissenschaftlich legitim und akademisch gestützt** (Marcos-Cuevas et al. 2023 liefert echtes Präzedenzargument für „Kontextspezifität als eigene Kategorie"). Sie ist aber **im jetzigen Reifestadium des Codex vermutlich verfrüht** als verpflichtende Strukturänderung: Die Evidenzbasis für kalibrierte Schwellenwerte fehlt für die meisten Objekte. Eine Einführung würde eher scheinbare Präzision erzeugen als tatsächliche wissenschaftliche Schärfe gewinnen — das wäre eine neue Form der schon im Gutachten selbst kritisierten Überinterpretation.

Dies ist eine Einschätzung, keine Entscheidung. Beide Wege (Einführung vs. Nicht-Einführung, sowie Zwischenformen) sind mit dem aktuellen wissenschaftlichen Stand vereinbar.

**Mögliche Zwischenform (nur zur Orientierung, keine Empfehlung):** Ein optionales (nicht verpflichtendes) CTX-Feld, das nur dort ausgefüllt wird, wo die Quelle tatsächlich eine Kontextgrenze explizit misst oder benennt — als Erweiterung des bereits bestehenden „Kontextgrenzen"-Freitextabschnitts um eine strukturierte Kurzform, nicht als neue Pflichtebene.

**Frage an Felix:**
1. Soll CTX als verpflichtende neue Ebene eingeführt werden (Framework-Änderung, hoher Nacharbeitsaufwand, vom Reviewer vorgeschlagen)?
2. Soll CTX als optionales Feld eingeführt werden (nur wo Evidenz vorliegt)?
3. Soll CTX nicht eingeführt werden, und der bestehende Freitext-Mechanismus (Kontextgrenzen-Abschnitte, Kontext-Dimension im Evidence System) bleibt der Standard?

**Betroffene Dokumente (nur bei Freigabe von Option 1 oder 2):** `01_framework/05_knowledge_model/canonical_knowledge_model.md`, `01_framework/08_templates/principle_template.md`, `01_framework/08_templates/technique_template.md`, `00_project/SALES_CODEX_OPERATING_MANUAL.md` (Schritt 5–6)

### Auflösung (Governance-Sprint 2026-07)

**Status: OFFEN — entscheidungsreif.** Gemäß Sprintvorgabe wird OD-007 nicht automatisch geschlossen. Die wissenschaftliche Bewertung ist vollständig, drei klar formulierte Optionen liegen vor, keine neuen Entwicklungen seit 2026-07-01 verändern die Analyse. Diese Entscheidung ist die am weitesten ausgearbeitete offene Entscheidung im Repository und wartet ausschließlich auf die Herausgeberwahl zwischen den drei genannten Optionen.

### Herausgeberentscheidung (Final Pre-Release Sprint, 2026-07-03)

**Status: ANGENOMMEN.** Felix hat entschieden: CTX wird eingeführt, jedoch **nicht als neuer Wissensobjekttyp**. CTX beschreibt die standardisierte Kontextebene bestehender Wissensobjekte — insbesondere Boundary Conditions, Anwendungsbereich, Voraussetzungen, Problemreife, Entscheidungskontext, Buying-Center-Kontext und Sensemaking-Bedarf — und wird künftig strukturiert dokumentiert. CTX ergänzt bestehende Wissensobjekte; es entsteht kein neuer Objekttyp. Damit ist von den im Herausgeber-Fragenkatalog genannten drei Optionen sinngemäß eine Zwischenform zwischen Option 1 und der in der wissenschaftlichen Bewertung skizzierten „optionalen Zwischenform" gewählt worden — verpflichtend als Konzept, aber ohne neue Objektklasse.

**Umsetzungsstatus:** Ausdrücklich **nicht Bestandteil dieses Sprints**. Die Einführung von CTX berührt den Canonical Knowledge Model (neuer Abschnitt), die Templates `principle_template.md`/`technique_template.md` sowie das Operating Manual (Schritt 5–6) — alles Framework-Änderungen, die außerhalb des Scopes des Final Pre-Release Sprints liegen (siehe Sprintauftrag, Abschnitt „Nicht zulässig": keine Frameworkänderungen, keine Änderungen am Canonical Knowledge Model, keine Änderungen am Operating Manual, keine Template-Anpassungen). Insbesondere die rückwirkende CTX-Befüllung der ~47 bestehenden Prinzipien und ~41 Techniken ist ausdrücklich keine Konsistenzkorrektur, sondern inhaltliche Redaktionsarbeit, die eigene Quellenprüfung pro Objekt erfordert. Die technische Umsetzung erfolgt in einem separaten Framework Integration Sprint nach Abschluss von Version 1.0.

**Für den RC-1-Audit relevant:** OD-007 ist nicht mehr offen im Sinne einer ausstehenden Herausgeber-Entscheidung — die Entscheidung liegt vor, inklusive der Festlegung, dass CTX kein neuer Objekttyp wird. Offen ist ausschließlich die technische Umsetzung, die bewusst auf einen Folgesprint verschoben wurde.

---

## OD-008 — Priorisierung eines Recherche-/Buchanalyse-Sprints für ELM, Trust Formation, Persuasion Knowledge Model

**Status:** ~~Offen — Herausgeber-Entscheidung erforderlich~~ → **TEILWEISE ENTSCHIEDEN (2026-07-05, aktualisiert 2026-07-05)** — ELM priorisiert, als Forschungsprojekt W-002 bearbeitet und teilweise integriert; Trust Formation priorisiert, als Forschungsprojekt W-003 bearbeitet, teilweise integriert und abgeschlossen (siehe „Editor Decision und Abschluss (W-003, 2026-07-05)" unten); Persuasion Knowledge Model bleibt offen
**Eingetragen:** 2026-07-01 (Academic Recovery Sprint Phase 2, Research Pack 2–4)

**Ausgangspunkt:** Die Verarbeitung von Research Pack 3 (Sozialpsychologie/Persuasion) hat drei strukturelle Lücken im Sales Codex identifiziert, die nicht formalisiert wurden, weil kein Primärtextzugriff vorlag (siehe `00_project/ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`, Abschnitt 5):

1. **Elaboration Likelihood Model** (Petty & Cacioppo 1986) — höchste Priorität. Würde MEC-0012, MEC-0018 und die Cialdini-MECs unter ein gemeinsames theoretisches Dach bringen.
2. **Trust Formation** (Mayer, Davis & Schoorman 1995) — konvergent in Pack 3 und Pack 4 identifiziert.
3. **Persuasion Knowledge Model** (Friestad & Wright 1994) — kleinere Priorität, teilweise bereits über MEC-0003-Zitat abgedeckt.

**Frage an Felix:** Soll einer dieser drei Kandidaten als nächster Recherche- oder sogar Buchanalyse-Sprint (Primärtext beschaffen, vollständiger Operating-Manual-Prozess Schritt 1–9) priorisiert werden? Oder bleibt die Priorität bei `ACADEMIC_RECOVERY_PLAN.md` Tier 1 (AR-001 Problemreife-Hypothese, AR-002 Publication-Bias-Klärung CEB/Challenger), wie in ARS-0001 empfohlen?

**Editor-Einschätzung:** Beide Stränge (Behavioral-Economics-/Sozialpsychologie-Vertiefung vs. Buying-Center-/Organisationale-Kaufentscheidung-Vertiefung) sind wissenschaftlich gerechtfertigt. Der Academic Recovery Plan (Tier 1/2) hat einen expliziten Fokus auf die B2B-Transferlücke — ELM/Trust/PKM sind eher allgemeinpsychologische Vertiefungen mit hoher, aber nicht B2B-spezifischer Integrationskraft. Ohne Herausgeber-Priorität empfiehlt der Editor, `ACADEMIC_RECOVERY_PLAN.md` Tier 1 weiterhin vorzuziehen — OD-008 dokumentiert die Alternative, trifft aber keine Vorentscheidung.

### Auflösung (Governance-Sprint 2026-07)

**Status: OFFEN — weiterhin relevant.** Keine implizite Entscheidung seit 2026-07-01: `NEXT_ACTION.md` referenziert OD-008 unverändert als offene Priorisierungsfrage, AR-001/AR-002/AR-013 bleiben laut Editor-Empfehlung vorrangig, ohne dass Felix bislang priorisiert hätte. Diese OD ist keine der in der Sprintvorgabe genannten OD-001–005 (kein automatischer Schluss zulässig) und wurde auch nicht implizit durch spätere Entwicklungen beantwortet — der Kandidatenstatus (ELM/Trust/PKM vs. Tier-1-Fortsetzung) ist unverändert. Bleibt offen.

### Herausgeberentscheidung (RP-001 Activation, 2026-07-05)

**Status: TEILWEISE ENTSCHIEDEN.** Im Rahmen der Research Portfolio Initialization Sprint (2026-07-05, `06_research_program/RESEARCH_PORTFOLIO.md`, Theme RP-001) wurde ELM als seit dem Academic Recovery Sprint dokumentierte und bislang offene Top-Priorität unter den drei OD-008-Kandidaten identifiziert. Felix hat daraufhin mit dem Auftrag „RP-001 Activation — ELM Persuasion Architecture Research Project" (2026-07-05) verbindlich entschieden:

1. **ELM wird vor Trust Formation priorisiert** und als reguläres Forschungsprojekt **W-002** („Persuasion Architecture — Elaboration Likelihood Model in Complex Sales Contexts") im Research Program aktiviert (`06_research_program/active/W002/`).
2. **Trust Formation (Mayer, Davis & Schoorman 1995) wird dadurch nicht abgelehnt oder zurückgestellt im Sinne einer Ablehnung** — es bleibt als bevorzugter nächster Kandidat validiert geführt (`RESEARCH_PORTFOLIO.md`, Theme RP-002, Status weiterhin „Validated", mit Vermerk „bevorzugter nächster Kandidat nach W-002").
3. **Persuasion Knowledge Model** (Friestad & Wright 1994) bleibt unverändert unpriorisiert — von dieser Entscheidung nicht berührt.

W-002 hat zum Zeitpunkt dieses Eintrags Stufe 6 (Decision Brief) des Research Lifecycle erreicht und wartet auf die Editor Decision (Stufe 7) — siehe `06_research_program/active/W002/05_DECISION_BRIEF.md`. Diese OD-008-Aktualisierung dokumentiert ausschließlich die Priorisierungsentscheidung (welcher Kandidat zuerst bearbeitet wird), nicht das inhaltliche Forschungsergebnis selbst und nicht die noch ausstehende Entscheidung über eine etwaige Repository-Integration.

**Für den Gesamtstatus von OD-008 relevant:** OD-008 ist damit nicht vollständig geschlossen — die ursprüngliche Frage betraf drei Kandidaten, von denen bislang nur einer (ELM) priorisiert wurde. OD-008 bleibt als Eintrag bestehen, bis auch über Trust Formation und Persuasion Knowledge Model entschieden ist oder diese Entscheidung durch ein Nachfolgeverfahren (analog zum Research Portfolio) strukturell abgelöst wird.

### Herausgeberentscheidung (RP-002 Activation, 2026-07-05)

**Status: TEILWEISE ENTSCHIEDEN — Trust Formation jetzt ebenfalls priorisiert.** W-002 (RP-001/ELM) wurde am 2026-07-05 vollständig bearbeitet: Editor Decision „Teilweise annehmen" liegt vor, sieben Wissensobjekte wurden erweitert (MEC-0012, MEC-0005–0008, MEC-0018, MOD-0002), zwei begründet unverändert gelassen (MEC-0009, MOD-0008); Repository Integration abgeschlossen (`06_research_program/completed/W002/REPOSITORY_INTEGRATION_LOG.md`). Mit dem Herausgeberauftrag „RP-002 Activation — Trust Formation & Relationship Marketing Research Project" (2026-07-05) hat Felix verbindlich entschieden:

1. **Trust Formation (Mayer, Davis & Schoorman 1995; Palmatier et al. 2006) wird als nächster Research-Investment-Kandidat aktiviert** und als reguläres Forschungsprojekt **W-003** („Trust Formation & Relationship Marketing in Complex Sales Relationships") im Research Program eröffnet (`06_research_program/active/W003/`).
2. Das Projekt wird gemäß bestehendem Research Lifecycle vollständig bis Status `AWAITING_EDITOR_DECISION` bearbeitet. **Keine Wissensbasis-Integration vor Herausgeberentscheidung.**
3. Ergebnisoffenheit ist verbindlich — insbesondere ist es zulässig, dass kein neues MEC, mehrere getrennte Konstrukte statt eines einheitlichen Trust-Mechanismus, eine strukturelle Trennung von Trust Formation und Relationship Marketing, reine Objekterweiterungen oder ein geringerer Grenznutzen als angenommen empfohlen werden.
4. **Persuasion Knowledge Model** (Friestad & Wright 1994) bleibt unverändert unpriorisiert — von dieser Entscheidung nicht berührt.

**Für den Gesamtstatus von OD-008 relevant:** Mit dieser Entscheidung sind zwei der ursprünglich drei OD-008-Kandidaten priorisiert (ELM → integriert via W-002; Trust Formation → aktiv via W-003). OD-008 bleibt als Eintrag bestehen, bis auch über das Persuasion Knowledge Model entschieden ist oder diese Restfrage durch ein Nachfolgeverfahren strukturell abgelöst wird.

### Editor Decision und Abschluss (W-003, 2026-07-05)

**Status: TEILWEISE ENTSCHIEDEN — Trust Formation abgeschlossen.** W-003 wurde am 2026-07-05 vollständig bearbeitet: Felix hat mit „Editor Decision — W-003" **teilweise angenommen** — Option E (strukturelle Trennung von Trust Formation und Relationship Marketing) angenommen; genau ein eng geschnittenes neues Mechanismus-Objekt (MEC-0030, „Vertrauensbildung aus wahrgenommener Vertrauenswürdigkeit") für die Ability/Benevolence/Integrity→Trustworthiness→Trust-Kette angelegt, unter ausdrücklicher, vom Herausgeber selbst korrigierter Einbeziehung von P-0040/A-0045; kein separates Cognitive-/Affective-Trust-MEC; kein neues MOD für Relationship Marketing — stattdessen 13 bestehende Wissensobjekte erweitert (MEC-0007, MEC-0008, MEC-0006, MEC-0014, MOD-0003, MOD-0007, A-0019, A-0029, A-0034, ST-0161, ST-0146, P-0012, P-0040, A-0045); Relationship Marketing als eigenständiges MEC/MOD, mehrere Trust-MECs und direkte High-Ticket-B2C-/Fertighaus-Techniken nicht integriert. Repository Integration und Health Check (Stufe 8–9) abgeschlossen, Projekt nach `06_research_program/completed/W003/` verschoben; `RESEARCH_PORTFOLIO.md` (RP-002 → `Integrated`) und `RESEARCH_STATUS.md` entsprechend aktualisiert. Neun offene Fragen als Scientific Debt dokumentiert (`00_project/SCIENTIFIC_DEBT.md`, Sektion „W-003"), kein automatisches Folgeprojekt.

**Für den Gesamtstatus von OD-008 relevant:** Mit dieser Entscheidung sind zwei der ursprünglich drei OD-008-Kandidaten vollständig bearbeitet und abgeschlossen (ELM → integriert via W-002; Trust Formation → integriert via W-003). OD-008 bleibt als Eintrag bestehen, bis auch über das Persuasion Knowledge Model entschieden ist oder diese Restfrage durch ein Nachfolgeverfahren strukturell abgelöst wird.

---

## OD-009 — Framework RC1 / Reifegrad-Statusübergang *(neu, 2026-07-02)*

**Status:** Offen — Herausgeber-Entscheidung erforderlich
**Eingetragen:** 2026-07-02 (Open Decisions Resolution Sprint)

**Ausgangspunkt:** Der Sales Codex hat inzwischen zehn vollständige Buchanalysen, zwei Synthese-Sprints (SPR-0001, SPR-0002), zwei Peer-Review-Sprints, zwei Academic-Recovery-Phasen, einen Sprint-3-Einzelreview und einen vollständigen Repository-Audit (`CODEX_AUDIT_2026-07.md`, Gesamtnote B+) durchlaufen. Es existiert aber kein formaler Mechanismus, der definiert, wann das Repository von „wissenschaftlich konsolidiert" (aktueller Zustand laut Auftrag) in einen nächsten benannten Reifegrad-Status (z. B. „Framework RC1") übergeht.

**Frage an Felix:** Soll ein formaler Statusübergang definiert werden (Analogie zu Software-Release-Stufen: Konsolidiert → RC1 → Freeze)? Falls ja: Welche Kriterien müsste ein RC1-Status erfüllen — z. B. Reifegrad A- laut `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (aktuell B/B+, A- „noch nicht erreicht" laut mehreren Sprintberichten), Auflösung von W-001 (Teach First vs. Diagnose First, seit S1-SYNTHESIS ungelöst), Schließung der B2B-Generalisierbarkeitslücke (aktuell C+)?

**Editor-Einschätzung:** Dies ist eine reine Versionsgovernance-Frage (wann gilt ein Reifegrad als erreicht, welche Schwellenwerte gelten), keine inhaltliche Forschungsaufgabe. Die Rohdaten für eine Entscheidung liegen bereits vor (Reifegradbericht, Audit); es fehlt nur der formale Übergangsmechanismus.

**Betroffene Dokumente (nur bei Einführung):** `CURRENT_STATE.md` (Versionsfeld), `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`, ggf. neues Dokument `VERSIONING_POLICY.md`.

---

## OD-010 — Validierungs-Governance *(neu, 2026-07-02 — Nachfolger von OD-005)*

**Status:** Offen — Herausgeber-Entscheidung erforderlich
**Eingetragen:** 2026-07-02 (Open Decisions Resolution Sprint, ersetzt OD-005)

**Ausgangspunkt:** OD-005 schlug ursprünglich Gemini als spezifisches Validierungsinstrument vor. In der Praxis wurde seither über mehrere verschiedene, nicht formal koordinierte Instrumente validiert: Peer-Review-Sprints (menschlich zugelieferte Gutachten), Academic-Recovery-Research-Packs (zugelieferte Literatursammlungen, websuchverifiziert), Sprint-3-Einzelreviews (gezielte Redaktionsaufträge). Jedes Instrument hat eigene Gründlichkeit, Dokumentationsform und Auslöser — es gibt keine einheitliche Policy, wann welches Instrument greift oder wann ein Objekt als „hinreichend validiert" gilt. Symptom: Einzelne MEC-Dateien tragen noch wörtliche Platzhaltersätze („Gemini-Validierung ausstehend"), obwohl inhaltlich bereits über andere Wege validiert wurde.

**Frage an Felix:** Soll eine einheitliche Validierungs-Policy festgelegt werden — z. B.: welches Instrument für welchen Evidenzlevel-Übergang (E2→E3, E3→E4 etc.) erforderlich ist, in welcher Kadenz Validierungssprints stattfinden, und wie ein Objekt als „extern validiert" markiert wird (einheitliches Statusfeld statt Freitext-Vermerke)?

**Editor-Einschätzung:** Langfristige Methodik-/Governance-Frage, keine Einzel-Forschungsaufgabe. Direkte Fortsetzung der in OD-005 aufgeworfenen, aber nie policy-seitig beantworteten Frage.

---

## OD-011 — Literature-Governance *(neu, 2026-07-02)*

**Status:** Offen — Herausgeber-Entscheidung erforderlich
**Eingetragen:** 2026-07-02 (Open Decisions Resolution Sprint)

**Ausgangspunkt:** Mit ARS-0001 Phase 2 wurde `05_research/LITERATURE_INDEX.md` neu angelegt (~50 Quellen über drei Domänen, mit Verifikationsstatus). Das Repository führt damit inzwischen drei parallele „offene Fragen/Quellen"-Dokumente ohne definierte Beziehung zueinander: `SCIENTIFIC_DEBT.md` (dokumentierte Evidenzlücken je Objekt), `review_queue.md` (nicht angelegte Literaturkandidaten), `05_research/LITERATURE_INDEX.md` (Literaturverzeichnis mit Verifikationsstatus). Es ist nicht festgelegt, ob `LITERATURE_INDEX.md` ein dauerhafter, strukturell verankerter Framework-Bestandteil ist (mit Pflege-Kadenz, Referenz im Operating Manual) oder ein Nebenprodukt eines einzelnen Sprints bleibt.

**Frage an Felix:** Soll `05_research/LITERATURE_INDEX.md` als dauerhafter Framework-Bestandteil formal verankert werden? Falls ja: Wie grenzt es sich strukturell von `SCIENTIFIC_DEBT.md` und `review_queue.md` ab, und wer pflegt es in welcher Kadenz?

**Editor-Einschätzung:** Strukturelle/architektonische Frage über die Beziehung dreier bestehender Dokumente zueinander — keine neue Recherche, keine neuen Wissensobjekte.

---

## OD-012 — Formalisierung der Kontextspezialisierung P-0021/P-0025 und MEC-0013/MEC-0001 *(neu, 2026-07-03)*

**Status:** Offen — Herausgeber-Entscheidung erforderlich
**Eingetragen:** 2026-07-03 (Research Project W-001 Repository Integration Sprint, im Repository-Integrationsplan `06_research_program/completed/W001/W001_COMPLETION_REPORT_RC1.md`, Abschnitt 5.5, bereits als voraussichtlich erforderlich angekündigt)

**Ausgangspunkt:** Die Editor Decision zu W-001 (`06_research_program/completed/W001/06_EDITOR_DECISION.md`, 2026-07-03, "Teilweise annehmen") hat den seit SPR-0001 dokumentierten Methodologiekonflikt zwischen P-0021/P-0025 (Commercial Teaching Pitch vs. vollständige Gap-Diagnose) sowie zwischen MEC-0013/MEC-0001 (Insight-Disruption durch Reframing vs. Selbstüberzeugung durch Verbalisierung) inhaltlich aufgelöst: Beide Objektpaare stehen nicht in universellem Widerspruch, sondern beschreiben kontextabhängig koexistierende Wirkmechanismen. Diese Auflösung wurde bei der Repository Integration bislang ausschließlich als Freitext dokumentiert (neue Abschnitte "Erweiterung durch W-001" in den vier betroffenen Objekten) — nicht als strukturell formalisierte "Kontextspezialisierung" im Sinne von `01_framework/05_knowledge_model/canonical_knowledge_model.md`, Abschnitt 8 (Beziehungstyp "Spezialisiert").

**Frage an Felix:** Sollen P-0021/P-0025 und MEC-0013/MEC-0001 künftig strukturell (z. B. über ein einheitliches Metadatenfeld oder eine explizite Kontextspezialisierungs-Kennzeichnung) als kontextuelle Spezialisierungen zueinander markiert werden, oder genügt die jetzt vorliegende Freitext-Dokumentation ("Erweiterung durch W-001"-Abschnitte in den vier Objekten) dauerhaft? Eine strukturelle Formalisierung wäre eine kleinere Framework-Ergänzung (kein neuer Objekttyp, aber ggf. ein neues Feld) und liegt außerhalb der Befugnis dieses Sprints (`REPOSITORY_INTEGRATION.md`, Abschnitt 2).

**Editor-Einschätzung:** Verwandt, aber nicht identisch mit OD-007 (CTX-Ebene) — OD-007 fragt nach einer generellen, verpflichtenden Kontext-Modifikator-Ebene für alle P-/T-Objekte; OD-012 fragt spezifisch nach der Formalisierung dieser vier bereits jetzt inhaltlich aufgelösten W-001-Objektbeziehungen. Beide könnten im Rahmen derselben Herausgeber-Entscheidungsrunde behandelt werden, sind aber getrennt geführt, da OD-012 unabhängig von einer OD-007-Entscheidung beantwortbar ist.

**Betroffene Dokumente (nur bei Formalisierung):** `01_framework/05_knowledge_model/canonical_knowledge_model.md` (Abschnitt 8), die vier betroffenen Objekte selbst (`A-0020`, `P-0021`, `P-0025`, `MEC-0013`, ggf. `MEC-0001`).

---

---

## V11-03 Governance-Bundle (2026-07-06) — Statuspräzisierung OD-006, OD-007, OD-009 bis OD-012

**Hinweis:** Gemäß `00_project/projects/V11-03_governance_integrity_atlas/PROJECT_BRIEF.md`, Abschnitt 2 ("Decision Bundles für OD-006, OD-007, OD-009, OD-010, OD-011, OD-012 vorbereiten"). Dies ist **keine neue Herausgeberentscheidung** und schließt keine der sechs ODs — es ordnet jede in eines der vier DoD-Statusfelder (`implemented` / `partially implemented` / `deferred` / `needs Editor Decision`) ein, damit der Bündelungszustand für Felix auf einen Blick sichtbar ist, statt in Freitext über mehrere Sprints verstreut zu bleiben.

| OD | DoD-Status | Begründung |
|---|---|---|
| OD-006 (Meme-Filter QK-Rating) | **Deferred** | Editor Decision liegt bereits vor (angenommen, 2026-07-03) — technische Umsetzung ausdrücklich auf einen künftigen, separaten Framework Integration Sprint verschoben, noch nicht terminiert. Kein Handlungsbedarf durch V11-03 (Umsetzung wäre eine Framework-/Template-Änderung, außerhalb des V11-03-Dateiscopes). |
| OD-007 (CTX-Ebene) | **Deferred** | Analog zu OD-006: Editor Decision liegt vor (angenommen, CTX kein neuer Objekttyp), technische Umsetzung (Canonical Knowledge Model, Templates, Operating Manual Schritt 5–6) explizit auf künftigen Framework Integration Sprint verschoben. |
| OD-009 (Framework RC1 / Reifegrad-Statusübergang) | **Needs Editor Decision** (unverändert) | Reine Schwellenwert-/Governance-Frage (welcher Reifegrad gilt als „RC1"), keine technische Ausführungsfrage — kann nicht durch den Executor vorentschieden werden. **Kontextuelle Klarstellung (keine Auflösung):** Das V1.1-Programm (`ROADMAP_V1_1.md`, `V1_1_RELEASE_CRITERIA.md`) etabliert seit 2026-07-06 einen formalen Release-Gate-Mechanismus für die *Workspace/Control-Plane*-Ebene (V11-01 bis V11-08 → Release Decision). Dies ist ein benachbartes, aber nicht identisches Konzept zur in OD-009 gefragten *inhaltlich-wissenschaftlichen* Reifegrad-Schwelle (Basis: `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`). Beide könnten in derselben künftigen Entscheidungsrunde behandelt werden, sind aber nicht automatisch dasselbe. |
| OD-010 (Validierungs-Governance) | **Needs Editor Decision** (unverändert) | Policy-Frage (welches Validierungsinstrument für welchen E-Level-Übergang), keine Repository-Integritätsfrage im technischen Sinn — bewusst getrennt von den in dieser V11-03-Runde neu definierten Atlas-/Repository-Integritätsprüfungen (Abschnitt „Atlas-Refresh- und Repository-Integritätsprüfung" in `KNOWLEDGE_ATLAS_GOVERNANCE.md` und `V1_1_RELEASE_CRITERIA.md` Abschnitt 1), die technische, nicht wissenschaftliche Integrität betreffen. |
| OD-011 (Literature-Governance) | **Needs Editor Decision** (unverändert) | Strukturfrage (Verhältnis `LITERATURE_INDEX.md`/`SCIENTIFIC_DEBT.md`/`review_queue.md`). **Kontextuelle Beobachtung (keine Auflösung):** V11-02 (`00_project/projects/V11-02_evidence_architecture_resolution/COMPLETION_REPORT.md`, Evidence Backlog Punkt 1) geht von einer fortgesetzten Nutzung von `LITERATURE_INDEX.md` aus — das ist ein operativer Fakt (das Dokument wird de facto weiter befüllt), keine Governance-Entscheidung über seinen formalen Status. |
| OD-012 (Kontextspezialisierung P-0021/P-0025, MEC-0013/MEC-0001) | **Needs Editor Decision** (unverändert) | Framework-Ergänzung (neues Metadatenfeld) — wie in der OD selbst festgehalten, außerhalb der Befugnis eines Ausführungssprints. Bleibt wie in der OD selbst vermerkt inhaltlich verwandt mit, aber unabhängig entscheidbar von OD-007. |

**Für V11-03 relevant:** Keine der sechs ODs verhindert den Abschluss von V11-03 (kein Hard Block, keine Reserved Decision wurde durch diese Einordnung selbst ausgelöst — sie modelliert nur den bestehenden Zustand). Zwei (OD-006, OD-007) sind bereits entschieden und warten nur auf einen künftigen Umsetzungssprint; vier (OD-009 bis OD-012) bleiben unverändert bei Felix.

---

*Zuletzt aktualisiert: 2026-07-06 (V11-03 Governance-Bundle — OD-006/OD-007 auf DoD-Status „Deferred" präzisiert, OD-009/OD-010/OD-011/OD-012 auf „Needs Editor Decision" bestätigt, keine inhaltliche Entscheidung getroffen). Zuvor: 2026-07-05 (RP-001 Activation — OD-008 auf TEILWEISE ENTSCHIEDEN gesetzt: ELM priorisiert und als W-002 aktiviert, Trust Formation/PKM unberührt). Zuvor: 2026-07-03 (Research Project W-001 Repository Integration Sprint — OD-012 neu angelegt). Davor: 2026-07-02 (Open Decisions Resolution Sprint — OD-001 bis OD-004 auf DONE gesetzt, OD-005 auf ERSETZT gesetzt [→ OD-010], OD-006/OD-007/OD-008 geprüft und als weiterhin OFFEN bestätigt, OD-009/OD-010/OD-011 neu angelegt). Vollständiger Bericht (2026-07-02): `00_project/OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`.*
