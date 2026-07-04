# Release Notes — Sales Codex Version 1.0 RC-1

**Dokumentklasse:** Release (Configuration Management)
**Rolle bei Erstellung:** Release Manager / Configuration Manager — reine Zusammenfassung bereits abgeschlossener, dokumentierter Arbeit. Keine neue fachliche Bewertung, keine neuen Inhalte.
**Datum:** 2026-07-04
**Bezug:** `RELEASE_CANDIDATE_RC1.md` (Freeze-Kennzahlen), alle unten zitierten Sprintberichte

---

## 1. Wichtigste Neuerungen gegenüber dem Ausgangszustand

Der Sales Codex ist seit dem Pilotprojekt (B-0001, SPIN Selling, 2026-06-27) von einem Einzelbuch-Test zu einer Wissensbasis mit **15 vollständig verarbeiteten Büchern**, **514 Wissensobjekten** (309 Statements, 60 Assumptions, 29 Mechanismen, 57 Prinzipien, 47 Techniken, 12 Modellen) und **15 Quellobjekten** gewachsen.

Wichtigste strukturelle Neuerungen:

- **Book Mode** als offizieller, im Operating Manual verankerter Workflow (vollständiger Prozess von Quelle bis Buchreview ohne Zwischenfreigaben) — eingeführt mit Sales Codex OS v1.1 (2026-06-30), seither in 14 weiteren Buchanalysen angewendet.
- **Stateless Agent Architecture** (seit 2026-06-30): Jede Session rekonstruiert den Projektzustand ausschließlich aus dem Repository selbst (`CURRENT_STATE.md`, `NEXT_ACTION.md`, `SESSION_LOG.md`) statt aus Konversationskontext.
- **Research Program** (`06_research_program/`) als eigenständiger, methodisch vollständiger Prozess für offene wissenschaftliche Streitfragen — neunstufiger Lifecycle, Governance, Decision Policy, 11 Templates, praktisch erprobt an W-001.
- **Scientific Debt** als dauerhaftes, transparentes Tracking-System für unvollständig gesicherte Wissensobjekte (kein Mangel, sondern bewusstes Ehrlichkeitsinstrument, analog zu technischen Schulden in der Softwareentwicklung).

## 2. Wichtigste wissenschaftliche Ergebnisse

- **W-001 (Teach First vs. Diagnose First):** Der seit dem ersten Synthese-Sprint (S1-SYNTHESIS, 2026-07-01) dokumentierte Methodologiekonflikt zwischen diagnoseorientierten (SPIN, Gap Selling) und teaching-/insight-orientierten (Challenger) Vertriebsansätzen wurde durch das Research Program systematisch geprüft (Master Review, Red-Team-Review, Theory Landscape) und per Editor Decision **teilweise angenommen**: kein universeller Widerspruch, sondern kontextabhängige Koexistenz (Problemreife, Buying-Center-Dynamik, Sensemaking-Bedarf entscheiden). Die vorgeschlagene mathematische Formalisierung (SCSM) wurde nach Red-Team-Kritik (11/13 Prüfkriterien nicht erfüllt) **abgelehnt** — der Codex führt keine unbelegte Formalisierung ein, nur weil sie intellektuell reizvoll wäre.
- **Behavioral-Science-Fundierung erheblich verbreitert:** Fünf zusätzliche Bücher (Emotional Intelligence, Predictably Irrational, Nudge, Priceless, Made to Stick) haben die Kernontologie um 8 neue Mechanismen, 2 neue Modelle (Choice Architecture, SUCCESS-Framework) und zentrale sozialpsychologische/verhaltensökonomische Konzepte erweitert, bei einer sprintweiten Canonicalization Rate von 66,7 % (überwiegend Erweiterung statt Neuanlage bestehender Mechanismen).
- **Zwei prominente Replikationsversagen unabhängig recherchiert und transparent dokumentiert statt geglättet:** Verschuere et al. (2018, Ten-Commandments-Priming, widerlegt Mazar/Amir/Ariely 2008) und Maier et al. (2023, Identifiable-Victim-Effect, widerlegt Small/Loewenstein/Slovic). Beide Fälle wurden bewusst **nicht** zu eigenen Wissensobjekten erhoben.
- **Autoren-Integritätsrisiko als neue, differenzierte Scientific-Debt-Kategorie eingeführt** (Ariely-Datenfälschungskontroverse 2021/2024) — Bewertung erfolgt je Einzelstudie, nicht pauschal je Autor.
- **Mehrere unabhängige Academic-Recovery-Phasen** haben zentrale Cialdini- und Voss-Mechanismen sowie die B2B-Transferfrage gegen aktuelle Meta-Analysen abgeglichen (u. a. Verbeke/Dietz/Verwaal 2010/2011, Marcos-Cuevas et al. 2023, Schley & Weingarten 2023, Brown/Imai/Vieider/Camerer 2024).

## 3. Größte Architekturentscheidungen

- **Framework v1.1 Freeze** (2026-06-30): Book Mode, Stateless Architecture, Canonicalisierungsregeln, Abschaffung von Zwischenfreigaben, BOOK_REVIEW als verbindlicher Endstatus.
- **OD-006 (Meme-Filter für QK-Rating):** Angenommen (2026-07-03) — Korrekturmechanismus zur Entkopplung wissenschaftlicher Qualität von Popularität/Verbreitung. **Technische Umsetzung ausdrücklich auf einen Framework Integration Sprint nach Version 1.0 verschoben.**
- **OD-007 (CTX-Kontextebene):** Angenommen (2026-07-03) — strukturierte Kontextdokumentation (Boundary Conditions, Problemreife, Buying-Center-Kontext) für bestehende Wissensobjekte, **kein neuer Objekttyp**. Technische Umsetzung ebenfalls auf einen Framework Integration Sprint nach Version 1.0 verschoben.
- **Research Program als eigenständige Governance-Ebene** (RC-1 Finalization Sprint, 2026-07-03): entkoppelt offene wissenschaftliche Streitfragen vom laufenden Buchanalyse-Workflow, mit eigenem neunstufigem Lifecycle und Repository-Integrationsmechanik.
- **Zwei getrennte Versionsachsen** (Framework vs. Sales-Codex-Gesamtversion) — verhindert, dass ein Framework-Freeze fälschlich als inhaltlicher Reifegrad-Abschluss gelesen wird.
- **Repository Consolidation** (zwei Sprints): acht Editor Decisions zur strukturellen Bereinigung (Duplikate, Fehlplatzierungen, Archivierung veralteter Dokumente) umgesetzt, ohne Top-Level-Ordnerstruktur oder Nummerierung zu verändern.

## 4. Research Program

Vollständig ausgearbeitet (Governance, Decision Policy, neunstufiger Lifecycle, Repository-Integrationsmechanik, 11 Templates) und **praktisch validiert**: W-001 ist das erste Projekt, das den gesamten Lifecycle — von der Research Question bis zum Abschluss-Health-Check — tatsächlich durchlaufen hat, inklusive einer echten, vom Herausgeber getroffenen Editor Decision. Aktueller Bestand: 0 aktive, 1 abgeschlossenes, 0 archivierte Projekte.

## 5. W-001

Siehe Abschnitt 2. Governance-seitig vollständig abgeschlossen (2026-07-03). Eine tiefere akademische Restfrage (direkter empirischer Vergleichstest, RCT) bleibt bewusst als nicht-blockierender Scientific-Debt-Posten offen — dies ist eine dokumentierte Grenze, kein unentdeckter Mangel.

## 6. Behavioral Science

Fünf Bücher (B-0011–B-0015) im Rahmen der Behavioral Science Expansion Sprint 1 (2026-07-02) vollständig verarbeitet: Emotional Intelligence (Goleman), Predictably Irrational (Ariely), Nudge: The Final Edition (Thaler & Sunstein), Priceless (Poundstone), Made to Stick (Heath & Heath). Ein unabhängiges externes Gutachten zu diesem Sprint wurde geprüft und in 8 Editor Decisions verarbeitet (Behavioral Science Review Sprint, 2026-07-02) — u. a. Umbenennung von MEC-0025 ("Altruistische Bestrafung"), Klassifikationshinweise für MOD-0011/MOD-0012, Boundary-Conditions-Ergänzungen für drei Mechanismen.

## 7. Repository Consolidation

Zwei Sprints (Audit + Implementation): Entfernung eines leeren Duplikat-Ordners und einer Zero-Byte-Debug-Datei, Verschiebung eines veralteten Knowledge-Model-Dokuments nach `99_archive/`, Umplatzierung dreier fehlplatzierter Dateien in die korrekten Buchordner, Archivierung dreier veralteter Root-Level-Dokumente. Alle acht umgesetzten Maßnahmen entstammen zuvor vom Herausgeber freigegebenen Editor Decisions; keine eigenständigen Strukturentscheidungen.

## 8. Breaking Changes gegenüber frühen Repository-Versionen

Der Sales Codex ist kein Software-Produkt; "Breaking Changes" bezeichnen hier Änderungen, die frühere Annahmen, Dateipfade oder Feldbenennungen ungültig machen:

- **Evidenzfeld-Umbenennung (Final Pre-Release Sprint + External Audit Resolution Sprint):** 6 uneinheitliche Feldnamen (`Evidenzlevel`, `Evidenzklasse`, `Evidenzklassifikation`, `Evidenzstatus`, `Evidenzlage`, `Evidenzgrad`) wurden auf das je Objekttyp templatekonforme Schema vereinheitlicht (insgesamt 84 Dateien: 70 in der ersten Runde, 14 weitere Assumptions/Modelle in der zweiten). Frühere Referenzen auf die alten Feldnamen in externer Dokumentation sind dadurch veraltet.
- **`codex_knowledge_model.md` (archiviert):** Ersetzt durch `01_framework/05_knowledge_model/canonical_knowledge_model.md` als alleinige aktive Wissensmodell-Referenz. Alte Verweise auf den archivierten Pfad sind ungültig.
- **`book_catalog.md`-Nummerierung korrigiert:** Sieben Kandidaten-IDs (ursprünglich B-0006, B-0008–B-0013) kollidierten mit inzwischen real vergebenen Buch-IDs und wurden auf B-0041–B-0047 verschoben. Jede externe Referenz auf die alten Kandidaten-IDs dieser sieben Bücher ist veraltet.
- **Dateiverschiebungen (Repository Consolidation Sprint 2):** `VAL-0001`/`PILOT_001_ABSCHLUSSBERICHT.md`, `VAL-0002`, `SCRP-0001_Sales_Core.md` sowie drei archivierte Root-Dokumente (`decision_log.md`, `roadmap.md`, `task_proposal_B-0002_influence.md`) liegen nicht mehr an ihrem ursprünglichen Pfad.
- **Statement-Feldkonvention:** `Evidenzklasse` ist jetzt die einheitliche informelle Bezeichnung für Statement-Evidenzangaben (vorher teils `Evidenzlevel`), obwohl ST kein Pflichtfeld dafür im Template trägt.

## 9. Bekannte Einschränkungen

Vollständige Liste: `RELEASE_CANDIDATE_RC1.md`, Abschnitt 17. Wichtigste Punkte in Kurzform:

- Finaler RC-1-Audit steht noch aus (siehe `RC1_FREEZE_DECLARATION.md`).
- Publication-Bias-Grundrisiko der drei proprietären B2B-Kernstudien (SPIN/Huthwaite, Challenger/CEB, JOLT/Tethr) bleibt bestehen — nur die Objektsichtbarkeit wurde hergestellt, nicht das Risiko aufgelöst.
- OD-006/OD-007 sind entschieden, ihre technische Umsetzung ist auf einen Framework Integration Sprint nach Version 1.0 verschoben.
- Fünf Open Decisions (OD-008–OD-012) bleiben unentschieden, keine davon ist ein MUST-HAVE-Blocker.
- W-001s tiefere akademische Frage (RCT-Vergleich Diagnose-First vs. Insight-First) bleibt offen.
- Ein vorbestehender, infrastruktureller Git-Index-Formatierungsfehler ist unverändert nicht behoben.

---

*Erstellt im Rahmen des Sales Codex Version 1.0 RC-1 Release Candidate Freeze, 2026-07-04. Reine Zusammenfassung bereits abgeschlossener und an anderer Stelle vollständig dokumentierter Arbeit — keine neue fachliche Bewertung.*
