# Sales Codex — Version 1.0 — Offizielle Veröffentlichung

**Titel:** Sales Codex — Ein evidenzbasiertes Wissenssystem über Vertrieb, Verkauf, Verhandlung, Kommunikation und Käuferpsychologie
**Veröffentlichungsdatum:** 2026-07-04
**Version:** 1.0 (Sales-Codex-Gesamtversion — unabhängig von der Framework-Version 1.1)
**Herausgeber:** Felix
**Dokumentklasse:** Release Declaration — formale Veröffentlichungserklärung, Phase 4 des Repository Closing & Release Sprints

---

## Executive Summary

Mit diesem Dokument erklärt der Herausgeber den Sales Codex offiziell als **Version 1.0**. Diese Erklärung erfolgt auf Basis des im Repository selbst definierten dreistufigen Freigabeprozesses (`SALES_CODEX_1_0_RELEASE_PLAN.md`, Kapitel 2.2 und 5): (1) RC-1 Release Candidate Freeze, abgeschlossen am 2026-07-04; (2) Finaler RC-1-Audit, durchgeführt durch drei unabhängige externe Gutachten und punktweise gegen den tatsächlichen Repository-Zustand validiert (`FINAL_RC1_AUDIT_VALIDATION_REPORT.md`); (3) formale Herausgeber-Freigabe, vollzogen durch dieses Dokument. Die Prüfung aller 19 Einzelbefunde aus den drei Gutachten sowie ein vollständiger, 14 Dimensionen umfassender Repository-Statuscheck (`REPOSITORY_CLOSING_STATUS.md`) ergaben keinen einzigen unadressierten Release Blocker. Version 1.0 umfasst 514 kanonische Wissensobjekte aus 15 vollständig analysierten Quellwerken, ein empirisch erprobtes Research Program und ein transparent geführtes wissenschaftliches Schuldenregister.

## Ziel des Sales Codex

Der Sales Codex überführt das historisch stark fragmentierte, häufig durch kommerzielle Interessen und anekdotische Evidenz geprägte Wissen über Vertrieb und Verkaufspsychologie in ein strukturiertes, wissenschaftlich kuratiertes Referenzwerk. Ziel ist nicht die Behauptung endgültiger Gewissheit, sondern ein System, das ehrlich und konsistent dokumentiert, was es weiß, was es nicht weiß, und warum — mit klar ausgewiesenen Evidenzklassen, offengelegten methodischen Schwächen und einem nachvollziehbaren Prozess für den Umgang mit wissenschaftlichen Kontroversen.

## Umfang von Version 1.0

- **514 kanonische Wissensobjekte:** 309 Statements, 60 Assumptions, 29 Mechanismen, 57 Prinzipien (davon 4 buchübergreifende Meta-Prinzipien), 47 Techniken, 12 Modelle.
- **15 vollständig analysierte Primärwerke** (B-0001–B-0015), von SPIN Selling und Influence über Never Split the Difference, The Challenger Sale und Gap Selling bis zur verhaltenswissenschaftlichen Erweiterung um Emotional Intelligence, Predictably Irrational, Nudge, Priceless und Made to Stick.
- **15 Quellobjekte** (SRC-0001–SRC-0015) mit vollständiger bibliografischer Dokumentation.
- **Ein abgeschlossenes Forschungsprojekt** (W-001), das den vollständigen neunstufigen Research Lifecycle inklusive unabhängigem Red-Team-Review und Editor Decision durchlaufen hat.
- **Ein vollständig ausgearbeitetes Research Program**, Governance-System und Canonical Knowledge Model.

## Wissenschaftliche Grundlage

Jedes Wissensobjekt ist über das Evidence-System (`evidence_system.md`, E1–E5) klassifiziert, mit vier Zusatzdimensionen (Kontext, Mechanismus, Reproduzierbarkeit, ethisches Risiko). Replikationsrisiken, Publication-Bias-Gefahren kommerziell finanzierter Studien und Autoren-Integritätsrisiken werden nicht verschwiegen, sondern im zentralen Register `SCIENTIFIC_DEBT.md` systematisch erfasst und an den betroffenen Objekten sichtbar gemacht (u. a. 29 Objekte mit explizitem Publication-Bias-Warnhinweis zu Challenger Sale und JOLT Effect). Wo Autoren wissenschaftlicher Integritätskontroversen unterlagen (Dan Ariely), wurde eine studienspezifische Entkopplung vorgenommen statt einer pauschalen Verbannung oder eines Verschweigens.

## Governance

Die Letztentscheidungskompetenz liegt ausnahmslos beim Herausgeber. KI-Sessions agieren als zuliefernde Zuarbeiter; jeder wertende Statuswechsel — Aufnahme eines Wissensobjekts, Abschluss eines Forschungsprojekts, Auflösung eines Widerspruchs — ist an eine explizite, dokumentierte Editor Decision gebunden. Die Stateless Agent Architecture (seit 2026-06-30) stellt sicher, dass jede Sitzung den Projektzustand ausschließlich aus dem Repository rekonstruiert. Die Governance-Dokumente (`SALES_CODEX_OPERATING_MANUAL.md`, `RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md`, `canonical_knowledge_model.md`, `task_rules.md`) sind vollständig, aufeinander abgestimmt und werden in der Praxis eingehalten.

## Research Program

Das Research Program (`06_research_program/`) ist ein eigenständiger, vom operativen Buchanalyse-Workflow getrennter Klärungsprozess für methodische Kontroversen mit einem neunstufigen Lifecycle (Forschungsfrage → Hypothesen → Master Review → Red-Team-Review → Theory Landscape → Decision Brief → Editor Decision → Repository Integration → Health Check). Seine Praxistauglichkeit wurde durch das Pilotprojekt W-001 nachgewiesen: eine spekulative mathematische Theorie (Socio-Cognitive Sensegiving Model) wurde nach Red-Team-Kritik verworfen, während der wissenschaftlich robuste Kernbefund in sechs bestehende Wissensobjekte integriert wurde.

## Audit-Historie

Version 1.0 wurde im Verlauf ihrer Entstehung wiederholt unabhängiger externer Prüfung unterzogen:

| Datum | Prüfung | Ergebnis |
|---|---|---|
| 2026-07-01 | Codex Audit 2026-07 | Gesamtnote B+ |
| 2026-07-01 | Wissenschaftlicher Reifegradsbericht | Gesamturteil B |
| 2026-07-02 | Wissenschaftliche Begutachtung des Behavioral Science Sprints | Accept after Minor Revision |
| 2026-07-04 | Wissenschaftliche Prüfung des Sales Codex | Major Revision Required (Kritikpunkte im Verlauf punktweise geprüft und größtenteils widerlegt bzw. behoben — Details: `FINAL_RC1_AUDIT_VALIDATION_REPORT.md`) |
| 2026-07-04 | Final RC-1 Release Audit | Ready for Release |
| 2026-07-04 | Punktweise Validierung aller drei Gutachten gegen aktuellen Repository-Zustand (dieser Sprint) | Kein unadressierter Release Blocker gefunden |

Jedes Gutachten wurde als Eingabe, nicht als Wahrheit behandelt: Kritikpunkte wurden unabhängig verifiziert, teilweise bestätigt, teilweise als sachlich unzutreffend zurückgewiesen (z. B. die Behauptung eines physisch fehlenden SRC-0010) und eine Empfehlung (Reklassifizierung von MOD-0011/MOD-0012 in neue Objektkategorien) nach Prüfung bewusst durch Editor Decision abgelehnt.

## Veröffentlichungsentscheidung

Auf Basis von `FINAL_RC1_AUDIT_VALIDATION_REPORT.md` (Phase 1) und `REPOSITORY_CLOSING_STATUS.md` (Phase 2) stellt der Herausgeber fest: Es besteht kein echter, unadressierter Release Blocker. Alle ursprünglich als blockierend eingestuften Kritikpunkte sind entweder sachlich widerlegt oder vollständig behoben; alle verbleibenden offenen Punkte sind transparent als Scientific Debt oder Open Decision dokumentiert und stellen keine Gefährdung der wissenschaftlichen Integrität des veröffentlichten Bestands dar. **Sales Codex Version 1.0 wird hiermit veröffentlicht.**

## Bekannte Einschränkungen

Version 1.0 wird mit vollem Bewusstsein folgender, bewusst nicht vor der Veröffentlichung geschlossener Einschränkungen freigegeben: (1) die zentrale B2B-Methodik (SPIN, Challenger, JOLT) beruht weiterhin auf proprietären, nicht unabhängig replizierten Datensätzen — offengelegt, nicht auflösbar durch Repository-Arbeit allein; (2) die Evidenzfeld-Abdeckung auf Statement-Ebene ist unvollständig; (3) der bestehende 514-Objekte-Kernbestand wurde nie einem systematischen, unabhängigen Peer-Review im Sinne des neuen Research-Program-Standards unterzogen; (4) OD-006 (Meme-Filter) und OD-007 (CTX-Ebene) sind inhaltlich entschieden, ihre technische Implementierung ist bewusst verschoben; (5) mehrere kosmetische Struktur- und Terminologiefragen (SRC-0010-Ordnerplatzierung, ein Fehlverweis in einem historischen Sprintbericht, unvollständige Terminologie-Nachziehung „Altruistische Bestrafung") bleiben bestehen.

## Ausblick auf Version 1.1

Folgende Themen werden ausdrücklich und namentlich an Version 1.1 übergeben, ohne in Version 1.0 bearbeitet worden zu sein:

- Technische Implementierung von OD-006 (Meme-Filter für das QK-Rating-System) und OD-007 (CTX-Kontextebene) im Rahmen eines dedizierten Framework Integration Sprints.
- Herausgeber-Entscheidungsrunde zu OD-008 (Literaturpriorisierung ELM/Trust Formation/PKM), OD-009 (Framework-RC1-Statusübergang), OD-010 (Validierungs-Governance, einschließlich der Frage eines retrospektiven Peer-Reviews des Kernbestands), OD-011 (Literature-Governance) und OD-012 (Formalisierung der W-001-Kontextspezialisierung).
- Repositoryweite Schließung der Evidenzfeld-Lücke auf Statement-Ebene.
- Vollständige Terminologie-Nachziehung „Altruistische Bestrafung" (P-0051, A-0056, fünf ST-Objekte, historische B-0014-Artefakte, Dateiname von MEC-0025).
- Ausweitung der organisationalen Boundary Conditions über MEC-0002, MEC-0021 und MEC-0022 hinaus.
- Korrektur der SRC-0010-Ordnerplatzierung und des Fehlverweises in `CANONICALIZATION_REPORT_B0013.md`.
- Strukturelle Bereinigung der Ordnernummern-Kollisionen (`04_book_analysis`/`04_synthesis`, `05_publications`/`05_research`).
- Fortsetzung des Academic Recovery Plan Tier 1, insbesondere eine vertiefte akademische Einordnung der Publication-Bias-Abhängigkeit der B2B-Kernmethodik.

Version 1.1 hat zum Zeitpunkt dieser Veröffentlichung **noch nicht begonnen**.

---

*Diese Erklärung wird durch `VERSION_1_0_CLOSING_REPORT.md` formal abgeschlossen.*
