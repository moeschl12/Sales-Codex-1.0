# Repository Integration

Version: RC-1
Stand: 2026-07-03
Geltungsbereich: Stufe 8 (Repository Integration) jedes Forschungsprojekts, siehe `RESEARCH_LIFECYCLE.md`, Abschnitt 10
Grundlage: `RESEARCH_PROGRAM_REVIEW_RC1.md`, Kapitel 3 ("Repository Integration — Keine Entsprechung gefunden", als "gravierendster Einzelbefund" bezeichnet) und Kapitel 6, "Fehlende Schnittstelle 2"

---

## 1. Zweck

Dieses Dokument schließt die von der Architekturprüfung als schwerwiegendste Einzellücke benannte Schnittstelle: *wie* genau ein durch Editor Decision angenommenes Forschungsergebnis zu einem oder mehreren Wissensobjekten im Sales Codex wird.

**Grundprinzip:** Die Repository Integration führt **keine neue, abweichende Logik** ein. Sie wendet die bestehende, im gesamten übrigen Repository verbindliche Logik aus `01_framework/05_knowledge_model/canonical_knowledge_model.md` unverändert an — genau wie bei jeder Buchanalyse. Das Research Program unterscheidet sich von einer Buchanalyse nur in der *Herkunft* des Materials (Forschungsprojekt statt Primärquelle/Buch), nicht in der *Art*, wie daraus Wissensobjekte werden.

## 2. Betroffene Objekttypen

Ein angenommenes Forschungsergebnis wird ausschließlich einem der im Canonical Knowledge Model bereits definierten Objekttypen zugeordnet:

| Objekttyp | Wann einschlägig |
|---|---|
| Statement (ST) | Das Ergebnis ist eine belegbare Einzelaussage aus dem Forschungsmaterial selbst (selten Hauptergebnis eines Forschungsprojekts, aber möglich als Zwischenobjekt). |
| Annahme (A) | Das Ergebnis formuliert eine falsifizierbare Grundannahme, die bislang unausgesprochen war. |
| Mechanismus (MEC) | Das Ergebnis beschreibt einen kausalen Pfad (Stimulus → Prozess → Reaktion), der bislang nicht oder anders erklärt war. |
| Prinzip (P) | Das Ergebnis formuliert eine abstrahierte, kontextgebundene Aussage im Format "Unter X führt Y zu Z". Dies ist der bei Forschungsprojekten wie W-001 (Auflösung eines Prinzipien-Widerspruchs) wahrscheinlichste Zieltyp. |
| Technik (T) | Das Ergebnis beschreibt ein konkretes, wiederholbares Verhalten mit Auslöse-/Abschlussbedingung. |
| Modell (MOD) | Das Ergebnis verknüpft mindestens drei Prinzipien zu einer kausallogischen Struktur (z. B. eine im Master Review entwickelte Synthese-Theorie, sofern angenommen). |

**Kein neuer Objekttyp:** Das Research Program legt keine neuen Objekttypen an (kein "RES", kein "THEORY" o. ä.). Dies gilt selbst dann, wenn ein Forschungsergebnis — etwa eine im Master Review vorgeschlagene mathematisch formalisierte Metatheorie — auf den ersten Blick nicht sauber in ST/A/MEC/P/T/MOD passt. In diesem Fall entscheidet die Editor Decision, welchem bestehenden Typ das Ergebnis am ehesten entspricht, oder stuft es (bei Nichtpassung) als nicht integrationsfähig in der aktuellen Form ein (→ Zurückstellen, `DECISION_POLICY.md` Abschnitt 2). Die Einführung eines neuen Objekttyps wäre eine Framework-Änderung und liegt außerhalb der Befugnis des Research Programs (vgl. `00_project/OPEN_DECISIONS.md`, OD-006, wo ein neues Metadatenfeld aus genau diesem Grund als Herausgeber-Entscheidung eingestuft wurde, nicht eigenständig umgesetzt).

## 3. Herkunftskennzeichnung: Source ID bei Research-Program-Ursprung

Jedes neu angelegte Wissensobjekt trägt gemäß `00_project/task_rules.md`, Abschnitt 7 ein Pflichtfeld "Source ID". Bei Objekten aus Buchanalysen ist dies eine `SRC-XXXX`-Referenz. Bei Objekten mit Ursprung im Research Program gilt folgende Konvention:

```markdown
## Source ID

W-XXX (Research Program)
```

Anstelle einer `SRC-ID` wird die Projekt-ID des Forschungsprojekts eingetragen, ergänzt um den Zusatz "(Research Program)" zur eindeutigen Unterscheidung von Buch-Quellen. Diese Konvention ist additiv — sie ändert das bestehende Source-ID-Pflichtfeld aus `task_rules.md` nicht, sie füllt es nur mit einem anderen Wertetyp. Ein entsprechender Hinweis wurde als kleine Ergänzung in `canonical_knowledge_model.md` aufgenommen (siehe Änderungsvermerk am Ende jenes Dokuments).

Wird ein Objekt aus mehreren Quellen gestützt (z. B. ein Forschungsprojekt bestätigt ein bereits aus einer Buchanalyse bestehendes Objekt), werden beide Referenzen kommagetrennt eingetragen, analog zu `task_rules.md`, Abschnitt 7.3: `SRC-0004, W-001`.

## 4. Ablauf der Integration

Die Repository Integration folgt exakt der in `canonical_knowledge_model.md`, Abschnitt 4 beschriebenen Entscheidungslogik:

1. **Bestehendes Objekt suchen** (Abschnitt 4, Schritt 1): Der Research Lead durchsucht alle Objekte des in der Editor Decision benannten Zieltyps nach gleicher Kausalrichtung und gleichem Kontext.
2. **Identitätsprüfung** (Abschnitt 4, Schritt 2): Ist die kausale Struktur identisch und der Kontext identisch → **Erweitern**. Ist die Struktur identisch, der Kontext verschieden → **Neu anlegen als Kontextspezialisierung**. Ist die Struktur verschieden → **Neu anlegen**.
3. **Qualitätsprüfung vor Neuanlage** (Abschnitt 4, Schritt 3): Mindestschwelle des Objekttyps (`canonical_knowledge_model.md`, Abschnitt 5) muss erfüllt sein.
4. **Zusammenführungskandidaten**: Werden nicht eigenständig vom Research Lead zusammengeführt, sondern in `review_queue.md` eingetragen — identisch zum Vorgehen bei Buchanalysen (`canonical_knowledge_model.md`, Abschnitt 4.3).

Jeder dieser vier Schritte wird für jedes einzelne, in der Editor-Decision-Tabelle "Geplante Integration" benannte Element separat durchlaufen — nicht pauschal für das gesamte Forschungsergebnis.

## 5. Dokumentationspflichten

Für jede durchgeführte Integrationsaktion gilt eine doppelte Dokumentationspflicht (Objekt → Projekt, Projekt → Objekt):

**Im Wissensobjekt selbst:**
- Pflichtfeld "Source ID" gemäß Abschnitt 3.
- Bei Erweiterung eines bestehenden Objekts: Eintrag unter "Unterstützende Quellen" (oder "Widersprechende Quellen", falls das Forschungsergebnis dem Objekt widerspricht — nie löschen, immer dokumentieren, `canonical_knowledge_model.md` Abschnitt 8).

**Im Projektordner:**
- `REPOSITORY_INTEGRATION_LOG.md` (neu angelegt bei Beginn von Stufe 8, siehe `templates/`-Hinweis in `RESEARCH_LIFECYCLE.md` Abschnitt 10) protokolliert jede Aktion: ID des betroffenen/neuen Objekts, Objekttyp, Aktion (NEU/ERWEITERT), Dateipfad, Datum, Bezug zur Editor-Decision-Zeile.
- `RESEARCH_LOG.md` erhält einen zusammenfassenden Eintrag über den Integrationsvorgang als Ganzes.

## 6. Nachvollziehbarkeit

Die Nachvollziehbarkeit einer Repository Integration ist bidirektional geprüft:

- **Von der Editor Decision zum Objekt:** Jede Zeile der Tabelle "Geplante Integration" (`DECISION_POLICY.md`, Abschnitt 5) muss im `REPOSITORY_INTEGRATION_LOG.md` wiederzufinden sein.
- **Vom Objekt zum Projekt:** Jedes integrierte Objekt trägt die Projekt-ID im Source-ID-Feld (Abschnitt 3) und ist damit auch ohne den Projektordner selbst als Research-Program-Ergebnis erkennbar.

Diese doppelte Verankerung ist Pflichtprüfpunkt 2 und 5 des Health Check (`RESEARCH_LIFECYCLE.md`, Abschnitt 12.3).

## 7. Versionierung

Die Repository Integration folgt derselben Commit-Regel wie die Standard-Buchanalyse (`00_project/SALES_CODEX_OPERATING_MANUAL.md`, Kapitel 6, Stufe 5): Kein Git-Commit vor Abschluss der vollständigen Integration und — bei Objekten mit Evidenzklasse E3 oder höher — nicht ohne Herausgeber-Freigabe der konkret integrierten Objekte (nicht nur der ursprünglichen Editor Decision im Prinzip). Die Commit-Nachricht beschreibt Projekt-ID, Anzahl und Typ der integrierten Objekte sowie Bezug zur Editor Decision.

Git-Operationen selbst bleiben — wie im gesamten Repository — ausschließlich Aufgabe des Herausgebers (`00_project/task_rules.md`, Abschnitt 9.1).

## 8. Verhältnis zur Evidenzentwicklung

Ein aus dem Research Program integriertes Objekt unterliegt ab dem Zeitpunkt seiner Integration denselben Auf- und Abstiegsregeln für Evidenzklassen (E1–E5) und Reifegrade (M1–M5) wie jedes andere Objekt (`canonical_knowledge_model.md`, Abschnitt 7). Der Umstand, dass ein Objekt aus einem mehrstufigen Forschungsprojekt mit Peer Review stammt, begründet keine automatisch höhere Einstufung — die Einstufung folgt weiterhin den dort definierten Bedingungen (z. B. E3 erst nach Herausgeber-Freigabe und drei unabhängigen Quellen/Forschungssträngen).

---

*Dieses Dokument gilt ab RC-1 (2026-07-03). Änderungen nur durch Felix. Keine Änderung an `canonical_knowledge_model.md` selbst außer dem in Abschnitt 3 genannten, punktuellen Hinweis.*
