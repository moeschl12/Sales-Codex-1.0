# Open Decisions

Offene Entscheidungen, die nach Abschluss von Influence durch den Herausgeber zu treffen sind.  
Neue Entscheidungen unten anfügen. Erledigte Entscheidungen als DONE markieren.

---

## OD-001 — Post-Mortem nach Influence

**Status:** Offen — nach Abschluss TASK-0010 fällig

**Frage:** Durchführung eines strukturierten Post-Mortems für B-0002 (Influence).

**Agenda:** `00_project/POST_MORTEM_INFLUENCE_PLAN.md`

**Abhängigkeit:** TASK-0010 abgeschlossen

---

## OD-002 — Book Mode offiziell einführen

**Status:** Offen — nach Post-Mortem

**Frage:** Soll der "Book Mode" (vollständiger Workflow von SRC bis BOOK_REVIEW ohne Zwischenfreigaben) als offizieller Modus in das Operating Manual aufgenommen werden?

**Kontext:** B-0002 ist der erste Lauf des neuen Workflows. Das Post-Mortem evaluiert, ob der Modus funktioniert hat.

**Dokumente zu aktualisieren (nach Freigabe):**
- `00_project/SALES_CODEX_OPERATING_MANUAL.md`
- `00_project/COWORK_EXECUTION_PROTOCOL.md`
- `00_project/task_rules.md`

---

## OD-003 — Framework v1.1 einfrieren

**Status:** Offen — nach Post-Mortem und OD-002

**Frage:** Nach Integration der Post-Mortem-Erkenntnisse: Framework v1.1 einfrieren.

**Inhalte von v1.1 (vorläufig):**
- Book Mode dokumentiert
- Stateless Agent Architecture dokumentiert
- Canonicalisierungsregeln präzisiert
- Zwischenfreigaben abgeschafft (außer bei Abbruchbedingungen)
- BOOK_REVIEW als Endstatus definiert
- Repository Health Check verpflichtend

---

## OD-004 — Nächstes Buch

**Status:** Offen — nach Framework v1.1 Freeze

**Frage:** Welches Buch wird als B-0003 analysiert?

**Kandidaten (nicht priorisiert):** Challenger Sale, Never Split the Difference, Gap Selling, Pitch Anything, Pre-Suasion (Cialdini 2), Thinking Fast and Slow (Kahneman).

---

## OD-005 — Gemini-Validierung der Mechanismen

**Status:** Offen — nicht terminiert

**Frage:** Gemini-Validierung für Replikationsstatus der Cialdini-Mechanismen (insbes. MEC-0005, MEC-0006, MEC-0007, MEC-0008) ist in mehreren Objekten als "ausstehend" markiert. Soll das als eigener Validierungs-Task (VAL-0003) eingeplant werden?

**Kontext:** Im Rahmen des aktuellen Workflows wird Gemini-Validierung nicht als Pflicht-Schritt behandelt — sie ist als Empfehlung in den VAL-Objekten dokumentiert.

---

---

## OD-006 — Meme-Filter für QK-Rating-System

**Status:** Offen — Herausgeber-Entscheidung erforderlich  
**Eingetragen:** 2026-07-01 (Peer Review Decision Report Sprint 1)

**Ausgangspunkt:** Der Peer Reviewer von Sprint 1 identifiziert ein methodologisches Risiko: Wenn drei Practitioner-Bücher (die nachweislich voneinander abschreiben oder auf denselben US-amerikanischen Corporate-Trainings-Zeitgeist reagieren) denselben Effekt behaupten, steigt das QK-Rating auf QK-3. Dies suggeriert fälschlicherweise wissenschaftliche Validität durch Konsens, wo eventuell nur eine erfolgreiche Meme-Replikation vorliegt.

**Konkrete Beispiele im Repository:**  
Cialdini (1984) → Voss (2016, referenziert Cialdini) → Keenan (2018) — alle konvergieren auf ähnliche COI/Dringlichkeits-Narrative. Ist das echte unabhängige Beobachtung oder gemeinsamer Ursprung?

**Mögliche Maßnahme:** Neues Metadaten-Feld in QK-Objekten: `meme_risiko: hoch / mittel / niedrig` mit Begründung. Dies wäre eine Framework-Änderung (neues Template-Feld, neues Bewertungskriterium).

**Editor-Einschätzung:** Intellektuell valide. Umsetzung wäre eine Framework-Änderung → Operating Manual Abschnitt 8 verbietet eigenständige Modifikation. Herausgeber-Entscheidung erforderlich.

**Frage an Felix:** Soll ein Meme-Filter-Feld in das QK-Rating-System eingeführt werden? Wenn ja: welches Format, welche Bewertungsskala?

**Update ARS-0001 (2026-07-01):** Das wissenschaftliche Gutachten nach Sprint 2 wirft einen verwandten, aber nicht identischen Punkt auf: das Risiko, dass Wissensobjekte sich zu stark an der Nomenklatur einzelner Autoren statt am dahinterliegenden Konstrukt orientieren ("Begriffsinflation", niedrige 4%-Canonicalization-Rate als Symptom). Beide Sorgen (Meme-Replikation als Schein-Konvergenz; Begriffsinflation als Schein-Eigenständigkeit) betreffen dieselbe Grundfrage: Wie unterscheidet der Codex "echte" von "scheinbarer" konzeptueller (Un-)Abhängigkeit? Empfehlung: Beide Aspekte gemeinsam in einer künftigen Herausgeber-Entscheidung behandeln, statt zwei separate Felder/Kriterien zu entwickeln. Siehe `PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`, Empfehlung 4.

---

## OD-007 — Kontext-/Domänen-Modifikator-Ebene (CTX)

**Status:** Offen — Herausgeber-Entscheidung erforderlich (ausdrücklich NICHT als Framework-Änderung umgesetzt)
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

---

---

## OD-008 — Priorisierung eines Recherche-/Buchanalyse-Sprints für ELM, Trust Formation, Persuasion Knowledge Model

**Status:** Offen — Herausgeber-Entscheidung erforderlich
**Eingetragen:** 2026-07-01 (Academic Recovery Sprint Phase 2, Research Pack 2–4)

**Ausgangspunkt:** Die Verarbeitung von Research Pack 3 (Sozialpsychologie/Persuasion) hat drei strukturelle Lücken im Sales Codex identifiziert, die nicht formalisiert wurden, weil kein Primärtextzugriff vorlag (siehe `00_project/ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`, Abschnitt 5):

1. **Elaboration Likelihood Model** (Petty & Cacioppo 1986) — höchste Priorität. Würde MEC-0012, MEC-0018 und die Cialdini-MECs unter ein gemeinsames theoretisches Dach bringen.
2. **Trust Formation** (Mayer, Davis & Schoorman 1995) — konvergent in Pack 3 und Pack 4 identifiziert.
3. **Persuasion Knowledge Model** (Friestad & Wright 1994) — kleinere Priorität, teilweise bereits über MEC-0003-Zitat abgedeckt.

**Frage an Felix:** Soll einer dieser drei Kandidaten als nächster Recherche- oder sogar Buchanalyse-Sprint (Primärtext beschaffen, vollständiger Operating-Manual-Prozess Schritt 1–9) priorisiert werden? Oder bleibt die Priorität bei `ACADEMIC_RECOVERY_PLAN.md` Tier 1 (AR-001 Problemreife-Hypothese, AR-002 Publication-Bias-Klärung CEB/Challenger), wie in ARS-0001 empfohlen?

**Editor-Einschätzung:** Beide Stränge (Behavioral-Economics-/Sozialpsychologie-Vertiefung vs. Buying-Center-/Organisationale-Kaufentscheidung-Vertiefung) sind wissenschaftlich gerechtfertigt. Der Academic Recovery Plan (Tier 1/2) hat einen expliziten Fokus auf die B2B-Transferlücke — ELM/Trust/PKM sind eher allgemeinpsychologische Vertiefungen mit hoher, aber nicht B2B-spezifischer Integrationskraft. Ohne Herausgeber-Priorität empfiehlt der Editor, `ACADEMIC_RECOVERY_PLAN.md` Tier 1 weiterhin vorzuziehen — OD-008 dokumentiert die Alternative, trifft aber keine Vorentscheidung.

---

*Zuletzt aktualisiert: 2026-07-01 (OD-008 ergänzt, Academic Recovery Sprint Phase 2)*
