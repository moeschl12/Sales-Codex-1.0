# Editor Decision — OD-009 bis OD-012 (Governance-Integration-Block)

Stufe: Reserved Decisions gemäß `00_project/OPEN_DECISIONS.md` (OD-009 bis OD-012, alle vier seit 2026-07-02/03 „Needs Editor Decision"). Ausschließlich Felix vorbehalten; durch diesen Herausgeberauftrag „Sales Codex — Großer Governance-Integration-Block nach V1.1 Release" (Felix, 2026-07-13) getroffen, hier von Claude (Cowork-Session, Executor-/Integrator-Rolle) dokumentiert.

**Bezug:** `00_project/DECISION_BRIEF_OD-009_TO_OD-012_2026-07-13.md` (Claude, 2026-07-13, durch Codex re-geprüft und freigegeben). Dieser Brief hat keine Entscheidung getroffen, nur Optionen und Empfehlungen vorgelegt. Die hier dokumentierten Entscheidungen folgen den im Herausgeberauftrag vorgegebenen, verbindlichen Festlegungen — sie sind nicht identisch mit den Brief-Empfehlungen, stimmen aber für OD-009, OD-010 und OD-011 mit der jeweils empfohlenen Option überein (OD-009: C; OD-010: B; OD-011: A). Für OD-012 folgt die Entscheidung der im Brief als „günstigere Lesart" bezeichneten Option A, unter der im Brief selbst benannten Prüfbedingung.

---

## Programmkontext

Sales Codex V1.1 ist **RELEASED — SCOPE-LIMITED** (`00_project/projects/V11-08_final_audit_release/EDITOR_RELEASE_DECISION.md`, 2026-07-13). Dieser Block ist kein neues Makroprojekt V11-09 ff. und keine Wiedereröffnung von V1.1 — er schließt ausschließlich die vier seit dem Release ausdrücklich offen gebliebenen Reserved Decisions OD-009 bis OD-012 sowie eine begrenzte Prüfung der Agentenhilfsschicht (`.agents/`, `.codex/`, `.claude/`, `.gitignore`) ab. Keine Websuche, kein Commit, kein Push.

---

## Entscheidung OD-009 — Framework RC1 / Reifegrad-Statusübergang

**Option: C — Zurückstellen.**

Kein formaler Reifegrad-Statusübergang (Konsolidiert → RC1 → Freeze) wird eingeführt. Keine `VERSIONING_POLICY.md` wird angelegt. Keine RC1-Schwellenwerte werden definiert.

**Begründung (Herausgeberauftrag):** Der Reifegradbericht selbst (`WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`) definiert keinen RC1-Schwellenwert; das einzige heute vorliegende strukturelle Analogon (V1.1-Release-Gate) ist gerade erst abgeschlossen, ohne dass seine Übertragbarkeit auf die *wissenschaftliche* Reifegrad-Ebene erprobt wäre. Eine verfrühte Schwellenwertfestlegung würde auf unkalibrierten Daten beruhen.

**Was konkret geschieht:** Nur Status-/Entscheidungsdokumentation wird aktualisiert (`OPEN_DECISIONS.md`, Control Plane). Der Reifegradbericht selbst bleibt unverändert Freitext-Instrument.

**Wann erneut vorlegen:** Sobald wesentliche neue reifegradrelevante Arbeit vorliegt (z. B. eine künftige Delivery- oder Research-Scaling-Phase) oder im Rahmen des nächsten Reifegradbericht-Updates — kein festes Datum, keine automatische Wiedervorlage.

**Nicht entschieden:** Ob der aktuelle Reifegrad B/B+ inhaltlich zutreffend ist; ob W-001-Restfragen oder die B2B-Generalisierbarkeitslücke geschlossen werden sollen; das Verhältnis zur V1.1-Release-Terminologie im Detail.

---

## Entscheidung OD-010 — Validierungs-Governance

**Option: B — Bestehende De-facto-Praxis dokumentieren, ohne neue Pflichtfelder.**

Peer Review Sprints, Academic Recovery Packs, Research-Lifecycle-Reviews (Master Review, Red Team Review, Health Check) und gezielte Einzelreviews (z. B. Sprint-3-Einzelprüfungen) werden als bestehende, gleichrangige Validierungsinstrumente beschrieben. Kein neues Evidenzpflichtfeld, keine neue Instrumenten-zu-Evidenzlevel-Zuordnungstabelle.

**Was konkret geschieht:**
1. `OPEN_DECISIONS.md`, OD-010-Eintrag: Auflösungsvermerk mit der Instrumentenbeschreibung.
2. Bereinigung der wörtlichen Platzhaltersätze „Gemini-Validierung ausstehend" — **nur dort, wo die Objektlage dies hergibt**, d. h. nur die Formulierung wird korrigiert (Gemini war nie das tatsächlich eingesetzte Instrument — OD-005 wurde durch OD-010 ersetzt), **ohne zu behaupten, dass die zugrunde liegende Evidenzlücke inzwischen geschlossen ist**. Die Reformulierung lautet einheitlich: *"Externe Validierung (ursprünglich als Gemini-Prüfung vorgesehen) ausstehend — Instrument gemäß OD-010 (2026-07-13) nicht mehr aktuell; inhaltliche Lücke bleibt offen, sofern nicht anderweitig dokumentiert."* Betroffene Objekte (9 Dateien, 10 Fundstellen — siehe Completion Report für die vollständige Liste): `A-0007`, `A-0009`, `A-0012`, `MOD-0002`, `P-0009`, `P-0012`, `P-0013`, `P-0015`, `BOOK_REVIEW_REPORT_B0002.md` (zwei Fundstellen).
3. **Bewusst NICHT verändert:** die beiden Fundstellen in `OPEN_DECISIONS.md` (Zeile 264, OD-010-Ausgangstext) und `ACADEMIC_RECOVERY_REPORT_PACK_2_4.md` (Zeile 88) — beide zitieren den Platzhaltersatz als historische Beschreibung eines Symptoms, nicht als aktiven Platzhalter; rückwirkende Änderung an einem bereits abgeschlossenen Bericht bzw. am eigenen OD-Ausgangstext widerspräche dem Append-only-Prinzip. Ebenso bewusst NICHT verändert: nahe Varianten ohne exakten Wortlaut „Gemini-Validierung ausstehend" (z. B. `MEC-0005` bis `MEC-0008`: „Gemini-Validierung für [Aspekt] ausstehend"; `A-0005`, `A-0006`, `A-0008`, `P-0003`) — diese liegen außerhalb der im Decision Brief gezählten 12 wörtlichen Fundstellen und würden den Scope dieses Blocks überschreiten. Empfehlung für einen künftigen, eigenständigen Nacharbeitspunkt im Completion Report vermerkt.
4. `SCIENTIFIC_DEBT.md`-Kategorie „Externe Validierung ausstehend" bleibt unverändert bestehen (Option B verlangt kein neues Feld) — ihre Definition wird nicht umformuliert, da sie bereits korrekt „Gemini- oder Perplexity-Prüfung noch nicht durchgeführt" beschreibt, ohne ein bestimmtes Instrument zwingend vorzuschreiben.

**Nicht entschieden:** Ob einzelne konkrete Objekte (z. B. MEC-0005 bis MEC-0008) tatsächlich als „hinreichend validiert" gelten; die inhaltliche Freigabe von RP-005 selbst (RP-005 bleibt blockiert, bis eine gesonderte Prüfung erfolgt — die Formalisierung der Instrumente allein hebt die Blockade nicht automatisch auf, siehe Completion Report).

---

## Entscheidung OD-011 — Literature-Governance

**Option: A — `05_research/LITERATURE_INDEX.md` formal als dauerhaften Governance-/Framework-Bestandteil verankern.**

**Abgrenzung (verbindlich ab sofort):**
- `LITERATURE_INDEX.md` = Quellenverzeichnis mit Verifikationsstatus je Quelle (verifiziert / codex-bestätigt / nicht verifiziert).
- `SCIENTIFIC_DEBT.md` = objekt-/programmbezogene Evidenzlücken, offene Forschungsfragen, Replikations-/Validierungsrisiken.
- `review_queue.md` = Kandidaten, Fusionsfragen, noch nicht angelegte Objekte/Quellen.

**Pflegekadenz:** Aktualisierung bei (a) Abschluss eines Research-Projekts, (b) Buchanalyse mit neuer Primärliteratur, (c) Academic-Recovery-/Validierungsrunde, oder (d) expliziter Editor-Freigabe.

**Was konkret geschieht:**
1. `OPEN_DECISIONS.md`, OD-011-Eintrag: Auflösungsvermerk mit Abgrenzung und Pflegekadenz.
2. `05_research/LITERATURE_INDEX.md`, Abschnitt „Zweck": Ergänzung um den formalen Verankerungsvermerk, dieselbe Abgrenzung und Pflegekadenz (redaktionell, keine inhaltliche Änderung der Quelleneinträge).

**Bewusst NICHT verändert:** `00_project/SALES_CODEX_OPERATING_MANUAL.md`. Dieses Dokument trägt die ausdrückliche Fußzeile „Änderungen nur durch Felix" — die Governance-Verankerung wird daher ausschließlich in `OPEN_DECISIONS.md` und im Zielobjekt selbst (`LITERATURE_INDEX.md`) dokumentiert, nicht durch eine eigenständige Ergänzung des Operating Manual. Dies ist eine bewusste Scope-Einschränkung dieser Session, kein Widerspruch zur Editor Decision — falls Felix eine Verankerung auch im Operating Manual wünscht, ist das ein separater, expliziter Schritt.

**Nicht entschieden:** Der Inhalt einzelner Literatureinträge; ob konkrete offene Punkte in `review_queue.md` (z. B. die MEC-0006/MEC-0014-Fusionsfrage) angenommen werden; die in `SCIENTIFIC_DEBT.md` selbst dokumentierte Datumsinkonsistenz (Kopf „Stand: 2026-06-30" vs. Fußzeile „Stand: 2026-07-06" vs. jüngster Inhalt bis 2026-07-12) — diese bleibt ein offener, bereits im Decision Brief dokumentierter Befund, nicht Teil des OD-011-Scopes.

---

## Entscheidung OD-012 — Kontextspezialisierung P-0021/P-0025 und MEC-0013/MEC-0001

**Option: A bevorzugt — bestehenden CKM-Beziehungstyp „Spezialisiert" nutzen — mit differenziertem Ergebnis nach Vorprüfung.**

**Vorprüfung durchgeführt (`01_framework/05_knowledge_model/canonical_knowledge_model.md`, Abschnitt 8):** Der Beziehungstyp „Spezialisiert" ist dort bereits dokumentiert, mit Dokumentationsort „Kontext-Feld + Verweis in übergeordnetem Objekt". Die tatsächliche Feldlage in den betroffenen Objekten weicht jedoch je Objekttyp voneinander ab:

| Objekt | Typ | Canonical-Feld für Kontext (laut Template) | Tatsächlich vorhanden? |
|---|---|---|---|
| A-0020 | Assumption | `## Kontext` (`assumption_template.md`) | Ja — exakt |
| P-0021 | Principle | `## Kontextlabel` (`principle_template.md`) | Ja — befüllt |
| P-0025 | Principle | `## Kontextlabel` (`principle_template.md`) | Nein — Feld im Template vorgesehen, in dieser Objektinstanz nie angelegt |
| MEC-0013 | Mechanism | Kein Kontext-Feld in `mechanism_template.md` (nur „Grenzen") | Nein — Template selbst hat kein Äquivalent |
| MEC-0001 | Mechanism | Kein Kontext-Feld in `mechanism_template.md` (nur „Grenzen") | Nein — Template selbst hat kein Äquivalent |

**Ergebnis der Prüfung:** Für A-0020 und P-0021 reicht das bestehende Feld strukturell aus — hier wird strukturell markiert (Feld befüllt/ergänzt, kein neues Feld). Für P-0025 existiert das Feld im Template, wurde aber für dieses Objekt nie angelegt — Ergänzung des vorgesehenen, bereits canonical existierenden Feldes ist keine Framework-Änderung, sondern Vervollständigung gemäß bestehendem Template. Für MEC-0013 und MEC-0001 existiert kein Kontext-Feld im Mechanism-Template — hier wird **freitextlich**, nicht strukturell, innerhalb der bereits bestehenden bzw. neu anzulegenden „Erweiterung durch W-001"-Abschnitte markiert, ausdrücklich ohne ein neues Feld einzuführen. Dies entspricht der im Herausgeberauftrag vorgesehenen Formulierung „strukturell/freitextlich sauber markieren" — kein Hard Stop für A' ist damit für die vier Kernobjekte nötig.

**Zusätzlicher, im Rahmen dieser Prüfung entdeckter Befund (kein Hard Stop, aber dokumentationspflichtig):** Die CKM-Definition von „Spezialisiert" ist hierarchisch („Objekt gilt unter engeren Bedingungen als das übergeordnete"). Die tatsächliche W-001-Auflösung für beide Objektpaare beschreibt jedoch **keine Über-/Unterordnung**, sondern zwei eigenständige, kontextabhängig **koexistierende** Mechanismen/Prinzipien gleichen Rangs (siehe `04_THEORY_LANDSCAPE.md`, Abschnitt 3, und die bereits bestehenden „Erweiterung durch W-001"-Abschnitte in P-0021, MEC-0013, A-0020). „Spezialisiert" ist damit die begrifflich nächstliegende, aber nicht perfekt passende bestehende CKM-Kategorie. Die Markierung wird in allen vier/fünf Objekten mit diesem ausdrücklichen Vorbehalt versehen — CKM Abschnitt 8 wird dadurch **nicht** verändert oder erweitert (keine neue siebte Beziehungskategorie „kontextabhängig koexistierend" wird eingeführt; dies wäre selbst eine Framework-Änderung und bleibt eine Empfehlung an Felix, keine Umsetzung).

**Weiterer, unabhängiger Befund bei P-0025 (kein OD-012-Gegenstand, aber im selben Objekt entdeckt):** Die Datei `P-0025_vollstaendige_gap_diagnose_vor_loesung.md` bricht am Dateiende (Zeile 64) mitten im Satz ab ("...Diese ursprünglich spekulative Kont[...]") und referenziert einen Abschnitt „Erweiterung durch W-001" ("siehe Abschnitt ... unten"), der im Objekt nicht existiert — mutmaßlich eine unvollständig gespeicherte Bearbeitung aus der ursprünglichen W-001-Integration (2026-07-03). Diese Session hat den bestehenden (unvollständigen) Satz **nicht** verändert oder rückwirkend vervollständigt (kein Erfinden von Inhalten), sondern ausschließlich einen neuen, klar datierten und abgegrenzten Abschnitt direkt danach ergänzt, der (a) den Befund dokumentiert und (b) die OD-012-Kontextspezialisierungsmarkierung auf Basis der bereits andernorts (P-0021, MEC-0013, A-0020, `06_EDITOR_DECISION.md`) dokumentierten, längst entschiedenen W-001-Fakten nachträgt. Empfehlung an Felix: eigenständige redaktionelle Prüfung/Vervollständigung von P-0025 außerhalb dieses Blocks.

**Was konkret geschieht (fünf Objekte):**
1. `A-0020` — Abschnitt „Kontext": Spezialisierungs-/Kontextbeziehungs-Verweis zu P-0025 ergänzt.
2. `P-0021` — Abschnitt „Kontextlabel": Spezialisierungs-/Kontextbeziehungs-Verweis zu P-0025 ergänzt.
3. `P-0025` — neuer Abschnitt „Kontextlabel" (gemäß Template erstmals angelegt) mit Verweis zu P-0021, plus neuer, klar abgegrenzter Befund-/Ergänzungsabschnitt (siehe oben).
4. `MEC-0013` — bestehender Abschnitt „Erweiterung durch W-001": freitextliche Ergänzung mit explizitem Spezialisierungs-/Kontextbeziehungs-Verweis zu MEC-0001.
5. `MEC-0001` — neuer Abschnitt „Erweiterung durch W-001 (Research Program) — Kontextspezialisierung (OD-012)", da dieses Objekt in der ursprünglichen W-001-Integration nicht erweitert wurde; Inhalt ausschließlich aus bereits dokumentierten W-001-Fakten (`06_EDITOR_DECISION.md`, MEC-0013-Text), keine neue Recherche.
6. `OPEN_DECISIONS.md`, OD-012-Eintrag: Auflösungsvermerk mit dieser differenzierten Begründung.

**Kein neues Feld, keine CKM-Änderung, keine neue Objekt-ID.**

**Nicht entschieden:** Ob CKM Abschnitt 8 künftig um eine eigene, nicht-hierarchische „koexistiert"-Kategorie erweitert werden soll (Empfehlung, keine Umsetzung); die inhaltliche Richtigkeit der W-001-Auflösung selbst (bereits 2026-07-03 entschieden); die vollständige redaktionelle Instandsetzung von P-0025 (Befund dokumentiert, nicht behoben).

---

## Agentenhilfsschicht (`.agents/`, `.codex/`, `.claude/`, `.gitignore`)

**Prüfung durchgeführt:** Alle Dateien in `.agents/` (README, `rules/`, `roles/`, `commands/`, `workflows/`), die Compatibility-Pointer `.codex/README.md` und `.claude/README.md` sowie `.gitignore` wurden gelesen.

**Ergebnis:** Die Hilfsschicht ist bereits sauber als Pointer-Layer formuliert — `.agents/README.md` definiert einen expliziten Autoritäts-Stack (`AGENTS.md` → `PROJECT_BOOTSTRAP.md` → `SESSION_BRIEF.md` → `NEXT_ACTION.md` → `TASK_TYPES.md` → Task-Dateien → `.agents/*`), keine neue Methodik, keine neuen Wissensobjekt-Regeln, keine Secrets, keine absoluten lokalen Pfade. `.codex/` und `.claude/` sind reine Compatibility-Pointer auf `.agents/`.

**Eine kleine, im Rahmen dieser Prüfung gefundene Korrektur (redaktionell, keine Autoritätsänderung):**
1. `.agents/roles/scientific-editor.md` referenziert `01_framework/03_evidence_system/` und `01_framework/06_knowledge_model/` — beide Pfade existieren im Repository nicht (verifiziert per Verzeichnisabgleich); die tatsächlichen Pfade sind `01_framework/02_evidence_system/` und `01_framework/05_knowledge_model/`. Korrigiert (reiner Pfadfehler, keine inhaltliche Änderung der Rolle).

**Geprüft, aber kein Handlungsbedarf:** `.gitignore` enthält bereits alle vier lokalen Override-Blöcke (`.codex/*.local.*`, `.agents/*.local.*`, `.claude/*.local.*`) vollständig und korrekt — ein erster Prüfzugriff über ein Sandbox-Mount hatte fälschlich eine Kürzung nahegelegt; ein direkter Dateizugriff (Read-Tool) widerlegte das. Festgehalten hier explizit, um eine fälschliche Korrektur einer bereits korrekten Datei zu vermeiden (Grundsatz: nicht auf Basis eines einzelnen, nicht gegengeprüften Werkzeugbefunds handeln). Die Datei enthält am Ende eine harmlose Dopplung des OS-/Python-/IDE-Blocks (Zeilen 1–17 vs. 45–58) — funktional wirkungslos (gitignore-Einträge sind idempotent), nicht verändert.

**Nicht verändert:** Struktur, Autoritäts-Stack, Rollenkarten, Befehls-Rezepte und Workflow-Pointer selbst — inhaltlich bereits korrekt.

---

## Scope / Nicht-Scope

**Im Scope:** OD-009 bis OD-012 (Entscheidung und begrenzte redaktionelle Integration), Bereinigung der 9 realen „Gemini-Validierung ausstehend"-Fundstellen, formale Verankerung von `LITERATURE_INDEX.md`, Kontextspezialisierungsmarkierung an fünf benannten Objekten, zwei kleine Korrekturen an der Agentenhilfsschicht, Control-Plane-Konsistenzpflege.

**Nicht im Scope:** Keine neuen Makroprojekte V11-09 ff., keine Framework-Methodikänderung, keine CKM-Erweiterung, keine Änderung an `SALES_CODEX_OPERATING_MANUAL.md`, keine Neubewertung einzelner Evidenzlevel, keine Auflösung der SCIENTIFIC_DEBT.md-Datumsinkonsistenz, keine Freigabe von RP-005, keine Websuche, kein Commit, kein Push.

---

## Umsetzungskriterien

- Jede der vier OD-Entscheidungen erhält einen datierten Auflösungsvermerk in `OPEN_DECISIONS.md`, mit Ursprungstext vollständig erhalten (Append-only).
- Jede Objektänderung ist minimal, additiv, klar als „OD-012 / Governance-Integration 2026-07-13" gekennzeichnet und verändert keine bestehende Kausalstruktur oder Evidenzklasse.
- Alle Control-Plane-Dateien werden konsistent, aber nur soweit nötig, aktualisiert — keine stillschweigenden Überschreibungen.

## Hard Stops (in diesem Block nicht ausgelöst)

Geprüft und **nicht** ausgelöst: OD-012 war ohne neues Feld sauber umsetzbar (siehe Vorprüfungstabelle oben); OD-010 erforderte keine echte Evidenz-Neubewertung einzelner Objekte (nur Instrumentenbenennung); kein bestehendes Framework-Dokument enthielt redaktionell unauflösbare Widersprüche; der Scope blieb innerhalb der vier ODs, der Agentenhilfsschicht und der Control Plane.

## Erwartete geänderte Dateien

`00_project/OPEN_DECISIONS.md`, `00_project/DECISION_STACK_2026-07-13.md`, `00_project/NEXT_ACTION.md`, `CURRENT_STATE.md`, `SESSION_BRIEF.md`, `00_project/SESSION_LOG.md`, `05_research/LITERATURE_INDEX.md`, neun Wissensobjekt-/Berichtsdateien für die Gemini-Platzhalter-Bereinigung, fünf Wissensobjekte für OD-012, `.agents/roles/scientific-editor.md`, plus dieses Dokument und das Abschlussartefakt `00_project/GOVERNANCE_INTEGRATION_OD-009_TO_OD-012_COMPLETION_REPORT_2026-07-13.md`.

---

## Datum und Unterschrift

Entschieden von: Felix (Herausgeber), im Rahmen des Herausgeberauftrags „Sales Codex — Großer Governance-Integration-Block nach V1.1 Release" (2026-07-13).
Dokumentiert und umgesetzt von: Claude (Cowork-Session), Executor-/Integrator-Rolle.

---

## Status

**OD-009 bis OD-012 entschieden am 2026-07-13** (OD-009: zurückgestellt/Option C; OD-010: Option B; OD-011: Option A; OD-012: Option A mit differenziertem, dokumentiertem Ergebnis). Umsetzung durch dieselbe Session unmittelbar im Anschluss — siehe `00_project/GOVERNANCE_INTEGRATION_OD-009_TO_OD-012_COMPLETION_REPORT_2026-07-13.md` für den vollständigen Umsetzungsnachweis.
