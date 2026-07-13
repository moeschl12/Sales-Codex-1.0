# Decision Brief — OD-009 bis OD-012

Status: Entscheidungsvorlage für Felix — keine Entscheidung, keine verbindliche Priorisierung / keine Herausgeberentscheidung durch diese Sitzung. Alle Reihenfolge- und Bündelungsvorschläge weiter unten (insbesondere im Abschnitt „Gebündelte Empfehlung") sind Executor-Empfehlungen ohne Bindungswirkung, keine Festlegung.
Datum: 2026-07-13
Erstellt von: Claude (Cowork-Session), Executor-/Analyst-Rolle
Auftrag: „Sales Codex — OD-009 bis OD-012 Decision Brief Paket" (Felix, 2026-07-13)

**Kontext:** Sales Codex V1.1 ist formal abgeschlossen und gepusht (RELEASED — SCOPE-LIMITED, Release-Commit `b096786`, Post-Release-Git-Closure `cbed101`). Keine laufenden Makroprojekte innerhalb V1.1. Delivery-Scaling ist ausdrücklich nicht freigegeben. OD-009 bis OD-012 wurden durch V1.1 nicht entschieden — sie waren bereits im V11-03-Governance-Bundle (2026-07-06) einheitlich mit dem DoD-Status „Needs Editor Decision" versehen und sind seither unverändert.

**Primärquellen:** `00_project/OPEN_DECISIONS.md` (OD-009 bis OD-012, inkl. V11-03-Governance-Bundle-Tabelle), `00_project/DECISION_STACK_2026-07-13.md`, `00_project/ROADMAP_V1_1.md`, `00_project/NEXT_ACTION.md`, `CURRENT_STATE.md`, `00_project/WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`, `05_research/LITERATURE_INDEX.md`, `00_project/SCIENTIFIC_DEBT.md`, `00_project/review_queue.md`, `01_framework/05_knowledge_model/canonical_knowledge_model.md` Abschnitt 8, `00_project/projects/V11-03_governance_integrity_atlas/COMPLETION_REPORT.md`.

**Rollen-Hinweis:** Dieses Paket schließt keine OD, ändert kein Framework, kein Wissensobjekt, kein Template, kein CKM, kein Operating Manual, keinen Scientific-Debt-Eintrag. Es enthält keine neue Recherche und keine Websuche. Alle "Empfohlene Option"-Angaben sind Executor-Empfehlungen, keine Entscheidungen.

---

## OD-009 — Framework RC1 / Reifegrad-Statusübergang

**Aktueller Status laut Repository:** Offen — Herausgeber-Entscheidung erforderlich (seit 2026-07-02, im V11-03-Governance-Bundle 2026-07-06 als „Needs Editor Decision (unverändert)" bestätigt). Laut `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`: Gesamturteil **Reifegrad B** — „Solide Grundstruktur mit identifizierten Schwachzonen". Dimensionen: Evidenzqualität B+, Quellen-Konvergenz A-, Interne Konsistenz B, Domänenabdeckung B, **Generalisierbarkeit C+** (schwächste Dimension — B2B-Transferlücke strukturell), Scientific Debt Management A-. Der Bericht selbst definiert keinen Schwellenwert für „RC1" — er formuliert nur „bereit für operative Anwendung mit expliziten Vorbehalten", keine Release-Candidate-Sprache.

**Entscheidungsfrage in einem Satz:** Soll ein formaler inhaltlich-wissenschaftlicher Reifegrad-Statusübergang (Konsolidiert → RC1 → Freeze) eingeführt werden, und wenn ja, welche Schwellenwerte gelten für „RC1"?

**Warum die Entscheidung jetzt relevant ist:** V1.1 hat mit `ROADMAP_V1_1.md`/`V1_1_RELEASE_CRITERIA.md` bereits einen formalen Release-Gate-Mechanismus für die *Workspace-/Control-Plane-Ebene* etabliert (V11-01 bis V11-08 → Editor Release Decision, gerade erst vollzogen). OD-009 fragt nach einem benachbarten, aber nicht identischen Konzept: der *inhaltlich-wissenschaftlichen* Reifegrad-Schwelle. Die beiden Konzepte könnten jetzt, mit dem frischen V1.1-Präzedenzfall vor Augen, sinnvoll aufeinander bezogen werden — oder es entsteht sonst dauerhaft Verwechslungsrisiko zwischen „Repository-Release" und „wissenschaftlicher Reifegrad".

**Optionen:**

- **A — Formalen RC1-Statusübergang jetzt definieren.** Konsequenz: neues Dokument `VERSIONING_POLICY.md` (oder Erweiterung eines bestehenden), explizite Schwellenwerte (z. B. Reifegrad A- laut `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`, Auflösung von W-001, Schließung der B2B-Lücke auf mind. B). Bindet zukünftige Reifegrad-Aussagen an einen nachvollziehbaren Mechanismus statt an Freitext-Einzelurteile.
- **B — Keinen formalen Statusübergang einführen; Reifegradbericht bleibt Freitext-Instrument, punktuell aktualisiert nach Bedarf.** Konsequenz: kein neuer Governance-Aufwand, aber die Frage „wann ist der Codex wissenschaftlich reif genug für X" bleibt jedes Mal neu zu verhandeln, ohne Präzedenzfall.
- **C — Zurückstellen, bis mehr Reifegrad-relevante Arbeit vorliegt (z. B. nach einer möglichen künftigen Delivery-Scaling- oder Research-Scaling-Phase), dann gemeinsam mit dem nächsten Reifegradbericht-Update neu bewerten.** Konsequenz: keine Entscheidung heute, aber auch keine Festlegung, die sich als verfrüht herausstellen könnte.

**Empfohlene Option (Empfehlung, keine Entscheidung):** C, mit Verweis auf B als Fallback. Begründung: Der Reifegradbericht selbst formuliert keine RC1-Schwelle, und die einzige heute vorliegende `strukturelle Analogie` (V1.1-Release-Gate) ist gerade erst abgeschlossen — es fehlt an Erfahrungswerten, ob dieses Modell auf die *wissenschaftliche* Ebene übertragbar ist. Eine verfrühte Schwellenwertfestlegung liefe Gefahr, an denselben unkalibrierten Daten zu scheitern wie die in OD-007 bereits diskutierte CTX-Frage.

**Was bei Annahme (Option A) geändert werden müsste:** neues Dokument `VERSIONING_POLICY.md`; Versionsfeld in `CURRENT_STATE.md`; ggf. Ergänzung in `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` um einen Schwellenwert-Abschnitt. Dies wäre eine Framework-Ergänzung (neues Governance-Dokument) — wird hier nur als Konsequenz beschrieben, nicht umgesetzt.

**Was ausdrücklich NICHT entschieden wird:** ob der aktuelle Reifegrad B/B+ inhaltlich zutreffend ist; ob W-001 oder die B2B-Generalisierbarkeitslücke selbst geschlossen werden sollen (das sind eigene, unabhängige Forschungs-/Scientific-Debt-Fragen); das Verhältnis zur V1.1-Release-Terminologie im Detail.

**Risiken bei Nichtentscheidung:** gering bis mittel. Kein technischer Blocker, aber wachsendes Begriffsverwirrungsrisiko zwischen „V1.1 RELEASED" (Repository-Ebene) und einem unspezifizierten „wissenschaftlichen Reifegrad" (Inhaltsebene) — insbesondere falls künftig extern (z. B. gegenüber Dritten) über den „Status" des Sales Codex kommuniziert wird.

---

## OD-010 — Validierungs-Governance

**Aktueller Status laut Repository:** Offen — Herausgeber-Entscheidung erforderlich (Nachfolger von OD-005, seit 2026-07-02, im V11-03-Bundle 2026-07-06 bestätigt „unverändert"). Faktischer Zustand: mehrere parallele, nicht formal koordinierte Validierungsinstrumente sind bereits in Gebrauch (Peer-Review-Sprints, Academic-Recovery-Research-Packs, Sprint-Einzelreviews). `05_research/LITERATURE_INDEX.md` definiert bereits ein Verifikationsstatus-Feld je Quelle („verifiziert" / „codex-bestätigt" / „nicht verifiziert"). Gleichzeitig tragen noch **12 Fundstellen in 11 Dateien** den wörtlichen Platzhaltersatz „Gemini-Validierung ausstehend" (u. a. `OPEN_DECISIONS.md`, `ACADEMIC_RECOVERY_REPORT_PACK_2_4.md`, mehrere `03_knowledge_base/`-Objekte), obwohl Gemini in keinem dokumentierten Sprint tatsächlich eingesetzt wurde. `SCIENTIFIC_DEBT.md` führt zusätzlich eine eigene Kategorie „Externe Validierung ausstehend" mit derselben Gemini-/Perplexity-Referenz.

**Entscheidungsfrage in einem Satz:** Soll eine einheitliche Validierungs-Policy festgelegt werden — welches Instrument für welchen Evidenzlevel-Übergang erforderlich ist, in welcher Kadenz, und mit welchem einheitlichen Statusfeld statt Freitext-Platzhaltern?

**Warum die Entscheidung jetzt relevant ist:** RP-005 im Research Portfolio ist laut `NEXT_ACTION.md`/`DECISION_STACK_2026-07-13.md` **indirekt auf OD-010 blockiert**. Die 12 veralteten „Gemini ausstehend"-Platzhalter erzeugen zudem ein wachsendes Konsistenzrisiko: Objekte behaupten textlich eine ausstehende Prüfung, obwohl inhaltlich längst über andere Wege validiert wurde (dokumentiert in OD-005-Auflösung).

**Optionen:**

- **A — Einheitliche Validierungs-Policy jetzt definieren:** festes Instrumenten-Set (Peer Review Sprint, Academic Recovery Pack, ggf. externes Modell) mit Zuordnung zu Evidenzlevel-Übergängen (E2→E3, E3→E4), definierte Kadenz, einheitliches Statusfeld statt Freitext. Konsequenz: Framework-Ergänzung (neues Pflichtfeld oder Statuswert im Evidenzsystem), plus redaktionelle Nacharbeit zur Bereinigung der 12 veralteten Platzhalter — nicht in diesem Brief umgesetzt, nur als Konsequenz benannt.
- **B — Bestehende De-facto-Praxis nachträglich als Policy dokumentieren, ohne neue Pflichtfelder** (reine Beschreibung dessen, was bereits geschieht: Peer Review + Academic Recovery Packs als gleichwertige Instrumente), plus separate redaktionelle Bereinigung der 12 Platzhalter als eigenständiger kleiner Nacharbeitspunkt. Konsequenz: geringerer Aufwand, kein neues Pflichtfeld, aber auch keine echte Vorab-Zuordnung „welches Instrument für welchen E-Level".
- **C — Zurückstellen; RP-005 bleibt blockiert, Platzhalter bleiben unverändert stehen**, bis eine grössere Governance-Runde (ggf. zusammen mit OD-009) stattfindet.

**Empfohlene Option (Empfehlung, keine Entscheidung):** B. Begründung: Die inhaltliche Substanz der Frage ist laut OD-005-Auflösung bereits weitgehend beantwortet — die Instrumente existieren und werden angewendet, es fehlt nur die formale Benennung und die Bereinigung veralteter Textreste. Eine vollständige Policy mit E-Level-Zuordnung (Option A) wäre eine größere Framework-Änderung ohne erkennbaren dringenden Zusatznutzen gegenüber einer schlankeren Nachdokumentation.

**Was bei Annahme (Option A oder B) geändert werden müsste:** je nach Option ein neues Policy-Dokument oder ein neuer Abschnitt in einem bestehenden Governance-Dokument; bei Option A zusätzlich ein neues/geändertes Statusfeld im Evidenzsystem (`evidence_system.md` oder MEC-Template) — Framework-Änderung, hier nur als Konsequenz beschrieben. Redaktionelle Bereinigung der 12 „Gemini ausstehend"-Fundstellen wäre in beiden Fällen ein separater, nachgelagerter Schritt (keine Wissensobjektänderung durch diesen Brief).

**Was ausdrücklich NICHT entschieden wird:** ob einzelne konkrete Objekte (z. B. MEC-0005 bis MEC-0008) tatsächlich als „hinreichend validiert" gelten; die inhaltliche Freigabe von RP-005 selbst.

**Risiken bei Nichtentscheidung:** mittel. RP-005 bleibt blockiert; die Diskrepanz zwischen Freitext-Platzhaltern und tatsächlichem Validierungsstand wächst mit jedem weiteren Sprint, was das Risiko künftiger Fehlinterpretationen (z. B. durch externe Leser oder neue KI-Systeme im Projekt) erhöht.

---

## OD-011 — Literature-Governance

**Aktueller Status laut Repository:** Offen — Herausgeber-Entscheidung erforderlich (seit 2026-07-02, im V11-03-Bundle 2026-07-06 bestätigt „unverändert"). Drei parallele Dokumente ohne definierte Beziehung existieren: `00_project/SCIENTIFIC_DEBT.md` (465 Zeilen — dokumentierte Evidenzlücken je Quelle/Objekt, kategorisiert u. a. „Replikationsrisiko", „Externe Validierung ausstehend", „Unbelegte Annahme"). **Metadaten-/Aktualitätsvorbehalt:** Der Kopf des Dokuments trägt „Version: 1.0 / Stand: 2026-06-30", die Fußzeile (Zeile 465) einen abweichenden Stand „2026-07-06", während der Dokumentinhalt selbst bereits Ergänzungen bis mindestens 2026-07-12 enthält (Sektion „W-008 — Omission-Kipppunkt im Buying Center (Research Program, integriert 2026-07-12)", Zeile 430 ff.). Die drei Datumsangaben (Kopf, Fußzeile, jüngster Inhalt) sind intern inkonsistent — dies ist selbst ein kleines Symptom der in OD-011 beschriebenen fehlenden Pflegekadenz-Regel und wird hier nicht geglättet, sondern als Beleg für die Entscheidungsfrage gewertet. Für den aktuellen *inhaltlichen* Gesamtstand des Dokuments ist keines der drei Datumsfelder verlässlich — nur eine Direktprüfung der jeweils relevanten Sektion zeigt den tatsächlichen Stand. `00_project/review_queue.md` (160 Zeilen — offene Review-Punkte plus „Zusammenführungskandidaten", z. B. eine noch offene MEC-0006/MEC-0014-Fusionsfrage), `05_research/LITERATURE_INDEX.md` (185 Zeilen, v1.2 — Literaturverzeichnis mit APA-Zitaten, Evidenzlevel, MEC-/Principle-Verknüpfung, Verifikationsstatus je Quelle). V11-02 (`COMPLETION_REPORT.md`, Evidence Backlog Punkt 1) geht bereits von einer fortgesetzten faktischen Nutzung von `LITERATURE_INDEX.md` aus — das ist ein operativer Fakt, keine Governance-Entscheidung über den formalen Status.

**Entscheidungsfrage in einem Satz:** Soll `LITERATURE_INDEX.md` als dauerhafter, formal verankerter Framework-Bestandteil (mit Pflegekadenz und Operating-Manual-Referenz) etabliert werden, und wie grenzt es sich strukturell von `SCIENTIFIC_DEBT.md` und `review_queue.md` ab?

**Warum die Entscheidung jetzt relevant ist:** Das Dokument wird de facto bereits weiter genutzt (V11-02-Fakt), aber ohne formale Verankerung bleibt unklar, wer es pflegt, in welcher Kadenz, und wie Doppel-Erfassungen zwischen den drei Dokumenten vermieden werden. Mit V1.1-Abschluss und absehbar wachsendem Literaturbestand (bei jeder künftigen Research-Aktivität) steigt das Risiko struktureller Drift zwischen den drei Dokumenten, je länger die Abgrenzung unklar bleibt.

**Optionen:**

- **A — `LITERATURE_INDEX.md` formal als dauerhaften Framework-Bestandteil verankern**, mit definierter Abgrenzung (z. B. `LITERATURE_INDEX.md` = Quellenverzeichnis mit Verifikationsstatus; `SCIENTIFIC_DEBT.md` = objektbezogene Wissenslücken; `review_queue.md` = noch nicht angelegte Kandidaten) und Pflegekadenz (z. B. „bei jedem Research-Projekt-Abschluss aktualisieren"). Konsequenz: Ergänzung im Operating Manual bzw. einem Governance-Dokument (Framework-Ergänzung, nicht in diesem Brief umgesetzt).
- **B — Kein separates Governance-Dokument; stattdessen die bereits faktisch gelebte Praxis (fortgesetzte Nutzung, siehe V11-02) einfach fortführen, ohne formale Verankerung.** Konsequenz: kein zusätzlicher Governance-Overhead, aber die strukturelle Abgrenzungsfrage zu `SCIENTIFIC_DEBT.md`/`review_queue.md` bleibt implizit und personenabhängig.
- **C — Die drei Dokumente inhaltlich konsolidieren** (z. B. `review_queue.md` als Teilmenge von `LITERATURE_INDEX.md` führen). Konsequenz: größerer struktureller Eingriff, potenziell Datenverlust/Migrationsrisiko bei drei bereits gewachsenen, unterschiedlich strukturierten Dokumenten — höchster Aufwand der drei Optionen.

**Empfohlene Option (Empfehlung, keine Entscheidung):** A. Begründung: Die faktische Nutzung ist laut V11-02 bereits etabliert; eine formale Verankerung mit klarer Abgrenzung kostet vergleichsweise wenig (kein neuer Objekttyp, keine rückwirkende Migration) und schließt eine seit 2026-07-02 offene strukturelle Lücke, bevor der Literaturbestand weiter wächst. Option C erscheint unverhältnismäßig aufwendig für den erkennbaren Nutzen.

**Was bei Annahme (Option A) geändert werden müsste:** ein neuer oder erweiterter Abschnitt im Operating Manual bzw. einem Governance-Dokument, der die Abgrenzung der drei Dokumente und die Pflegekadenz für `LITERATURE_INDEX.md` festlegt. Keine Änderung an den drei Dokumenten selbst notwendig (nur an ihrer Governance-Einordnung) — dennoch eine Framework-Ergänzung, hier nur als Konsequenz beschrieben, nicht umgesetzt.

**Was ausdrücklich NICHT entschieden wird:** der Inhalt einzelner Literatureinträge; ob konkrete offene Punkte in `review_queue.md` (z. B. die MEC-0006/MEC-0014-Fusionsfrage) angenommen werden.

**Risiken bei Nichtentscheidung:** gering bis mittel. Kein akuter Blocker, aber strukturelle Drift zwischen den drei Dokumenten wird mit jedem weiteren Research-Zyklus wahrscheinlicher, was künftige Aufräumarbeit verteuert.

---

## OD-012 — Formalisierung der Kontextspezialisierung P-0021/P-0025 und MEC-0013/MEC-0001

**Aktueller Status laut Repository:** Offen — Herausgeber-Entscheidung erforderlich (seit 2026-07-03, im V11-03-Bundle 2026-07-06 bestätigt „unverändert"). Die inhaltliche Frage ist bereits gelöst: Die Editor Decision zu W-001 (2026-07-03, „Teilweise annehmen") hat den Methodologiekonflikt zwischen P-0021/P-0025 sowie MEC-0013/MEC-0001 als **kontextabhängig koexistierende Mechanismen** aufgelöst, bisher jedoch nur als Freitext dokumentiert („Erweiterung durch W-001"-Abschnitte in den vier Objekten).

**Wichtig — nicht geglättete Spannung zwischen zwei Repository-Quellen:** `OPEN_DECISIONS.md` (OD-012, 2026-07-03) formuliert die strukturelle Formalisierung ausdrücklich als **„eine kleinere Framework-Ergänzung (kein neuer Objekttyp, aber ggf. ein neues Feld)"**. Das V11-03-Governance-Bundle (2026-07-06) übernimmt diese Einschätzung wörtlich fort: **„Framework-Ergänzung (neues Metadatenfeld) — wie in der OD selbst festgehalten, außerhalb der Befugnis eines Ausführungssprints."** Beide Quellen gehen also davon aus, dass ein *neues* Feld nötig wäre. Bei der Recherche für diesen Brief wurde jedoch `01_framework/05_knowledge_model/canonical_knowledge_model.md`, Abschnitt 8, geprüft: dort ist bereits **formal ein Beziehungstyp „Spezialisiert"** dokumentiert („Objekt gilt unter engeren Bedingungen als das übergeordnete"), mit einer benannten Dokumentationsstelle („Kontext"-Feld + Verweis im übergeordneten Objekt). Diese Beobachtung ist eine **Executor-Re-Interpretation dieses Briefs, keine Korrektur der bestehenden OD-012-/V11-03-Klassifikation** — beide Lesarten werden hier bewusst nebeneinander stehen gelassen: entweder (a) die früheren Einschätzungen haben Abschnitt 8 nicht in dieser Tiefe geprüft und ein neues Feld wäre tatsächlich nicht nötig, oder (b) das bestehende „Kontext"-Feld wurde von den früheren Prüfungen bewusst als für diesen Zweck unzureichend beurteilt (z. B. zu unstrukturiert/freitextig für eine belastbare Formalisierung) und ein neues, präziseres Feld wäre trotzdem sinnvoll. Dieser Brief kann die Diskrepanz nicht auflösen — nur sichtbar machen.

**Entscheidungsfrage in einem Satz:** Sollen P-0021/P-0025 und MEC-0013/MEC-0001 strukturell markiert werden (entweder über den bereits vorhandenen CKM-Beziehungstyp „Spezialisiert" oder über ein neues Feld, falls Felix dessen bestehende Ausprägung für unzureichend hält), oder genügt die bestehende Freitext-Dokumentation dauerhaft?

**Warum die Entscheidung jetzt relevant ist:** Selbst in der günstigeren Lesart (bestehender Mechanismus genügt) ist hier kein neues Framework-Konzept nötig — das unterscheidet OD-012 von OD-007 (generelle CTX-Pflichtebene). Die Entscheidung wäre damit potenziell die am wenigsten aufwendige der vier ODs, wurde aber dennoch am längsten unbeachtet liegen gelassen (Ankündigung bereits im W-001-Integrationsplan, 2026-07-03).

**Optionen:**

- **A — Bestehenden „Spezialisiert"-Beziehungstyp auf die vier Objekte anwenden** (Kontext-Feld befüllen, gegenseitigen Verweis eintragen), gemäß der bereits im CKM dokumentierten Konvention. Konsequenz: kleine, gezielte Objektänderung an `P-0021`, `P-0025`, `MEC-0013`, ggf. `MEC-0001`/`A-0020` — nach dieser Brief-Re-Interpretation kein neuer Objekttyp, kein neues Pflichtfeld nötig. **Voraussetzung, die Felix prüfen müsste:** dass das bestehende „Kontext"-Feld für diesen Zweck tatsächlich ausreicht — das ist nicht durch diesen Brief verifiziert, nur durch die Existenz der CKM-Textstelle plausibilisiert. Dennoch eine inhaltliche Wissensobjektänderung, die außerhalb der Befugnis dieses Briefs liegt und nicht hier umgesetzt wird.
- **A' — Neues, präziseres Metadatenfeld einführen**, falls Felix der ursprünglichen OD-012-/V11-03-Einschätzung folgt, dass das bestehende „Kontext"-Feld nicht hinreichend strukturiert ist. Konsequenz: echte kleinere Framework-Ergänzung (CKM-Abschnitt-8-Erweiterung plus Template-Anpassung), größerer Aufwand als Option A.
- **B — Bestehende Freitext-Dokumentation („Erweiterung durch W-001") als dauerhaft ausreichend erklären**, keine strukturelle Nacharbeit. Konsequenz: kein Aufwand, aber die Objekte nutzen dann dauerhaft weder den bestehenden noch einen neuen CKM-Mechanismus — Inkonsistenz zwischen Konvention und Praxis bleibt bestehen.
- **C — Gemeinsam mit OD-007 (CTX-Ebene, bereits angenommen, Umsetzung auf Framework Integration Sprint verschoben) im selben künftigen Sprint bündeln**, da beide Fragen laut `OPEN_DECISIONS.md` „im Rahmen derselben Herausgeber-Entscheidungsrunde behandelt werden könnten, aber unabhängig entscheidbar sind".

**Empfohlene Option (Empfehlung, keine Entscheidung):** A, unter dem ausdrücklichen Vorbehalt, dass Felix die oben beschriebene Spannung selbst auflöst (ob das bestehende „Kontext"-Feld genügt oder Option A' nötig ist). Sollte sich A als nicht tragfähig erweisen, wäre A' die nächstliegende Alternative — beide sind der bisherigen Einschätzung „größere CTX-Pflichtebene" (OD-007, Option 1) klar vorzuziehen. Diese Empfehlung ersetzt nicht die frühere OD-012-/V11-03-Klassifikation, sondern ergänzt sie um eine seither nicht geprüfte Repository-Beobachtung.

**Was bei Annahme (Option A) geändert werden müsste:** `P-0021`, `P-0025`, `MEC-0013`, ggf. `MEC-0001`/`A-0020` — Kontext-Feld gemäß CKM Abschnitt 8 befüllen. Dies ist eine Wissensobjektänderung und liegt außerhalb der Befugnis dieses Analyse-Briefs; wird hier nur als Konsequenz beschrieben, nicht umgesetzt.

**Was ausdrücklich NICHT entschieden wird:** ob das bestehende „Kontext"-Feld (Option A) für diesen Zweck tatsächlich ausreicht oder ob es der ursprünglich in `OPEN_DECISIONS.md`/V11-03 angenommenen Framework-Ergänzung (Option A') bedarf — diese Spannung wird durch diesen Brief explizit offengelassen, nicht aufgelöst; ob der CKM-Beziehungstyp „Spezialisiert" selbst erweitert oder verändert werden soll (das wäre in jedem Fall eine echte Framework-Änderung); die inhaltliche Richtigkeit der W-001-Auflösung selbst (bereits 2026-07-03 entschieden).

**Risiken bei Nichtentscheidung:** gering. Kein Blocker für andere Projekte; rein strukturelle Konsistenzlücke zwischen Konvention und Praxis, die mit der Zeit als Präzedenzfall für andere ähnliche Objektbeziehungen fehlen könnte.

---

## Gebündelte Empfehlung

**Welche ODs gemeinsam entschieden werden sollten:** OD-011 und OD-012 eignen sich für eine gemeinsame, kurze Entscheidungsrunde — beide sind eng umrissen und lassen sich ohne größere Vorarbeit klären: OD-011 ist reine Governance-Zuordnung dreier bestehender Dokumente; OD-012 ist im günstigeren Fall (Option A) die Anwendung eines bereits existierenden CKM-Mechanismus, im weniger günstigen Fall (Option A', falls Felix das bestehende Feld für unzureichend hält) eine kleinere Framework-Ergänzung — die Unterscheidung selbst ist Teil dessen, was in dieser Runde zu klären wäre, siehe OD-012-Abschnitt oben. OD-009 und OD-010 sind inhaltlich schwerer und sollten nicht in derselben kurzen Runde behandelt werden wie OD-011/012, da beide (bei Annahme von Option A) echte neue Governance-Dokumente bzw. Policy-Festlegungen nach sich ziehen würden.

**Welche getrennt bleiben sollten:** OD-009 (Reifegrad-Statusübergang) sollte nicht vorschnell mit OD-010 (Validierungs-Governance) gekoppelt werden, obwohl beide „Governance-Policy"-Charakter haben — sie betreffen unterschiedliche Ebenen (wissenschaftliche Reifegrad-Schwelle vs. Validierungsinstrumente-Zuordnung) und haben unterschiedlichen Dringlichkeitsgrad (OD-010 blockiert aktiv RP-005; OD-009 blockiert nichts Konkretes). Empfehlung: OD-010 vorrangig vor OD-009 behandeln, falls eine Priorisierung nötig ist.

**Welche Umsetzungssprints daraus folgen könnten:** Bei Annahme von OD-011/OD-012 (Empfehlung A) genügt jeweils ein kleiner, eng umrissener Nacharbeitssprint (Governance-Dokument-Ergänzung bzw. vier Objektänderungen) — kein eigenes Makroprojekt nötig. Bei Annahme von OD-010 (Option A oder B) wäre ein kombinierter „Validierungs-Governance + Platzhalter-Bereinigung"-Sprint sinnvoll. Bei Annahme von OD-009 (Option A, falls doch gewählt) wäre ein eigenständiger „Versioning Policy"-Sprint nötig, sonst keiner.

**Ob ein Framework Integration Sprint sinnvoll ist:** Ja, aber erst nachdem die ODs entschieden sind, und dann gebündelt mit den bereits längst angenommenen, aber technisch noch nicht umgesetzten Punkten OD-006 (Meme-Filter) und OD-007 (CTX-Ebene) — beide warten laut `OPEN_DECISIONS.md` bereits seit 2026-07-03 auf genau einen solchen Sprint. Ein einzelner, größerer Framework Integration Sprint, der OD-006, OD-007 und die technischen Konsequenzen aus OD-010/OD-011/OD-012 (je nach Ausgang) gemeinsam umsetzt, wäre effizienter als mehrere kleine Einzelsprints — vorausgesetzt, die zugrunde liegenden Entscheidungen liegen dann alle vor.

**Welche Entscheidungen vor Delivery-Scaling nötig sind:** Keine der vier ODs ist eine formale Voraussetzung für eine künftige Delivery-Scaling-Freigabe laut `V11-04`/`V11-07`-Dokumentation — die dort benannten vier Delivery-Scaling-Blocker (T12, Technik-Kandidaten, Zielgruppen-Tagging, MEC-0002/P-0002-Evidenzlevel) sind von OD-009 bis OD-012 unabhängig. Am ehesten inhaltlich benachbart ist OD-010 (Validierungs-Governance), da eine klare Validierungs-Policy die Aussagekraft künftiger Delivery-Inhalte stärken würde — aber auch das ist keine harte Abhängigkeit, sondern eine Empfehlung zur Reihenfolge, keine Blockade.

---

## Nicht-Scope-Bestätigung

Dieser Brief hat keine OD als DONE/ACCEPTED/REJECTED markiert, kein neues Projekt angelegt, kein V11-09 angelegt, keine Wissensobjekte, Templates, das CKM, das Operating Manual oder `SCIENTIFIC_DEBT.md` verändert, keine neue Recherche oder Websuche durchgeführt, keine Release- oder Scope-Entscheidung getroffen. Kein Commit, kein Push.
