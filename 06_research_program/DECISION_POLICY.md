# Decision Policy

Version: RC-1
Stand: 2026-07-03
Geltungsbereich: Editor Decisions für alle Forschungsprojekte (`W-XXX`)
Grundlage: `RESEARCH_GOVERNANCE.md` Abschnitt 4.1, `RESEARCH_PROGRAM_REVIEW_RC1.md` Kapitel 4 ("Entscheidungslogik") und Kapitel 8, Empfehlung 2

---

## 1. Grundsatz

**Nur Editor Decisions erlauben eine Übernahme in den Codex.**

Dieser Grundsatz aus der Vorgängerversion bleibt unverändert gültig und ist der Kern dieses Dokuments. Alles Weitere in diesem Dokument beantwortet die Frage, die die Vorgängerversion offenließ: *Wann fällt eine Editor Decision positiv aus, und was folgt daraus konkret?*

## 2. Entscheidungsoptionen

Eine Editor Decision (`06_EDITOR_DECISION.md`) muss sich für genau eine der folgenden vier Optionen entscheiden. Eine Editor Decision ohne eindeutige Options-Zuordnung ist unvollständig und blockiert den Übergang zu Stufe 8 (Repository Integration).

| Option | Bedeutung | Folge |
|---|---|---|
| **Annehmen** | Das geprüfte Ergebnis wird vollständig in den Sales Codex übernommen. | Repository Integration (Stufe 8) beginnt für das gesamte Ergebnis. |
| **Teilweise annehmen** | Nur bestimmte, im Editor-Decision-Dokument einzeln benannte Teilaussagen werden übernommen; andere werden verworfen oder zurückgestellt. | Repository Integration beginnt ausschließlich für die benannten Teile. Die Editor Decision muss die Trennlinie explizit benennen (welche Teilaussage, warum angenommen/verworfen). |
| **Zurückstellen** | Weder Annahme noch Ablehnung ist auf Basis der vorliegenden Reviews möglich; es fehlt eine benannte, konkrete Voraussetzung (z. B. eine externe Studie, eine weitere Review-Runde). | Projekt bleibt `ACTIVE`, kehrt zur benannten Stufe zurück (z. B. zusätzliche Peer-Review-Runde). Keine Repository Integration. Zurückstellung ist keine Ablehnung — sie muss eine konkrete, prüfbare Bedingung für die erneute Vorlage benennen, sonst verkommt sie zur impliziten Ablehnung ohne Begründung. |
| **Ablehnen** | Das geprüfte Ergebnis wird nicht in den Sales Codex übernommen. | Keine Repository Integration. Projekt wird nach `archived/` verschoben (`RESEARCH_GOVERNANCE.md` Abschnitt 6.3). |

## 3. Kriterien für eine positive Entscheidung (Annehmen / Teilweise annehmen)

Eine Editor Decision darf **Annehmen** oder **Teilweise annehmen** nur wählen, wenn für den jeweils angenommenen Teil alle folgenden Bedingungen erfüllt sind. Diese Liste ist identisch mit dem Qualitätsstandard für jedes Wissensobjekt im Hauptcodex (`00_project/SALES_CODEX_OPERATING_MANUAL.md`, Kapitel 4) — das Research Program erhält keine abweichenden, laxeren Anforderungen, nur weil es außerhalb des Standard-Buchanalyse-Workflows liegt.

| Kriterium | Prüffrage |
|---|---|
| Nachvollziehbar | Sind Quelle und Herleitung des angenommenen Teils vollständig angegeben (Master Review, Theory Landscape)? |
| Eingeordnet | Ist bereits absehbar, welchem Objekttyp (ST/A/MEC/P/T/MOD gemäß `canonical_knowledge_model.md`) das Ergebnis bei der Integration entsprechen wird? |
| Unsicherheit markiert | Sind alle unsicheren Teilaussagen als solche gekennzeichnet, statt als gesicherte Erkenntnis formuliert? |
| Kontext benannt | Gilt das Ergebnis universell, kontextabhängig, branchenspezifisch oder situationsgebunden (Evidenzsystem, Zusatzdimension "Kontext")? |
| Grenzen beschrieben | Benennt die Editor Decision, wann das angenommene Ergebnis *nicht* gilt? |
| Widersprüche verarbeitet, nicht geglättet | Wurde jeder dokumentierte Widerspruch zwischen Master Review und Peer Review (siehe `RESEARCH_GOVERNANCE.md` Abschnitt 7) in der Editor Decision explizit adressiert — angenommen, verworfen oder als offene Frage weitergereicht — statt stillschweigend übergangen? |
| Evidenzklasse zugeordnet | Trägt der angenommene Teil eine begründete Evidenzklasse E1–E5 gemäß `01_framework/02_evidence_system/evidence_system.md`? |

**Zusatzanforderung ab Evidenzklasse E3:** Bei geplanter Integration mit Evidenzklasse E3 oder höher soll vor der Editor Decision zusätzlich die Rolle "Wissenschaftliche Validierung" (`RESEARCH_GOVERNANCE.md` Abschnitt 4.5) hinzugezogen werden. Dies ist eine Empfehlung, keine Abbruchbedingung — der Herausgeber kann begründet davon abweichen; die Abweichung wird in der Editor Decision vermerkt.

## 4. Umgang mit widersprüchlichen Reviews

Der in der Review (`RESEARCH_PROGRAM_REVIEW_RC1.md`, Executive Summary) als "wichtigste Schwäche" benannte Fall — Master Review und Peer Review kommen zu entgegengesetzten Schlussfolgerungen — ist **kein Abbruchgrund** und **keine automatische Ablehnung**. Er ist der Normalfall, für den die Theory Landscape (Stufe 5) und der Decision Brief (Stufe 6) da sind.

Die Editor Decision muss in diesem Fall explizit Stellung nehmen:

- Welcher Seite folgt die Entscheidung, und warum (mit Bezug auf konkrete Kriterien aus Master Review/Peer Review, nicht auf allgemeine Präferenz)?
- Falls keiner Seite vollständig gefolgt wird: Welcher Teil wird übernommen (→ Teilweise annehmen), welcher zurückgestellt oder abgelehnt?
- Wird der Widerspruch selbst als offene Forschungsfrage in `OPEN_QUESTIONS.md` oder `00_project/SCIENTIFIC_DEBT.md` weitergereicht?

## 5. Bezug zur Repository Integration

Jede Editor Decision mit Ergebnis "Annehmen" oder "Teilweise annehmen" muss eine Tabelle **"Geplante Integration"** enthalten, die für jeden zu integrierenden Bestandteil mindestens angibt: voraussichtlicher Objekttyp (ST/A/MEC/P/T/MOD), Arbeitstitel, vorgeschlagene Evidenzklasse. Diese Tabelle ist die Übergabe an Stufe 8 (Repository Integration) — Details zum Ablauf: `REPOSITORY_INTEGRATION.md`.

Eine Editor Decision, die "Annehmen" beschließt, ohne diese Tabelle auszufüllen, ist unvollständig im Sinne von `RESEARCH_LIFECYCLE.md`, Stufe 7 (Übergabekriterien) und blockiert den Beginn von Stufe 8.

## 6. Abbruchbedingungen bei der Entscheidungsfindung selbst

| Bedingung | Maßnahme |
|---|---|
| Ethischer Grenzfall im geprüften Ergebnis | Keine Entscheidung ohne gesonderte Prüfung; ethisches Risiko wird in der Editor Decision explizit als niedrig/mittel/hoch eingestuft (analog Evidenzsystem, Zusatzdimension "Ethisches Risiko"). |
| Zwei gleichermaßen vertretbare Entscheidungen ohne klare Präferenz | Zurückstellen statt eine der beiden Optionen ohne belastbare Begründung zu wählen. Die fehlende Präferenz selbst wird dokumentiert. |
| Editor Decision würde eine Framework-Änderung voraussetzen (z. B. neuer Objekttyp) | Keine eigenständige Entscheidung. Eskalation als eigene Open Decision (`00_project/OPEN_DECISIONS.md`) — das Research Program führt keine neuen Objekttypen ein (siehe `REPOSITORY_INTEGRATION.md`, Abschnitt 2). |

---

*Dieses Dokument gilt ab RC-1 (2026-07-03). Änderungen nur durch Felix.*
