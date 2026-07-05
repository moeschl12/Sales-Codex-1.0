# Knowledge Atlas Governance

**Dokumentklasse:** Reference (Governance-/Prozessdefinition, kein Wissensobjekt, keine Framework-Datei im Sinne von `01_framework/`)
**Rolle bei Erstellung:** Editor (Claude), im Auftrag des Herausgebers — Governance-Entwurf. Keine Framework-Änderung, keine Änderung am Canonical Knowledge Model, keine Codeänderung an `compile_atlas.py`, keine neue Analyse.
**Datum:** 2026-07-05
**Status:** **Freigegeben** (Herausgeberbeschluss, 2026-07-05) — nach Einarbeitung der vom Herausgeber verlangten Präzisierung in Abschnitt 2 (Buch-Batch-Trigger als Richtwert statt harte Zählregel formuliert). Mit dieser Freigabe gilt diese Governance als verbindlicher Standard des Sales Codex; die Aufbauphase des Knowledge Atlas ist damit abgeschlossen, der Atlas geht in den regulären Betriebs- und Wartungsmodus über. Siehe Abschnitt 9 (Herausgeberbeschluss) für den vollständigen Wortlaut der Entscheidung.
**Grundlage:** `08_knowledge_atlas/ATLAS_MANIFEST.md`, `08_knowledge_atlas/output/atlas_compiler_report.md`, `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, `TASK_TYPES.md`, `00_project/SALES_CODEX_OPERATING_MANUAL.md`, `00_project/REPOSITORY_KPIS.md`, `00_project/OPEN_DECISIONS.md` (insb. OD-009, Reifegrad-Statusübergang), `00_project/changelog.md`, `CURRENT_STATE.md`.
**Scope:** Ausschließlich Prozess- und Steuerungsfragen. Keine technische Spezifikation des Compilers, keine Erweiterung von Atlas v0.1 (`ATLAS_MANIFEST.md` Abschnitt 2–3 bleibt unverändert gültig), keine neue inhaltliche Analyse des Repositorys.

---

## 1. Zweck und Einordnung

Der Knowledge Atlas hat mit dem Content Analysis Sprint 1 (`00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, 2026-07-05) zum ersten Mal gezeigt, dass eine graphbasierte Betrachtung des Sales Codex redaktionell wertvolle, durch reines Lesen einzelner Objekte nicht sichtbare Befunde liefert (insb. die MEC-0018-Struktur-/Evidenzrisiko-Konstellation, Abschnitt 3.2 und 9 des Sprint-1-Reports). Dieser Sprint war jedoch ausdrücklich als **Einmalauswertung** angelegt — außerhalb des versionierten Compilers, ohne Wiederholungsmechanismus (Sprint-1-Report, Abschnitt 2.3).

Dieses Dokument beantwortet die daraus folgende Anschlussfrage: **Wie wird aus einer einmaligen Diagnoseleistung ein dauerhaftes Steuerungsinstrument, ohne dass jede künftige Analyse neu erfunden werden muss?**

Drei bestehende Dokumente regeln bereits benachbarte, aber andere Fragen und werden durch dieses Governance-Dokument nicht ersetzt:

| Dokument | Regelt | Verhältnis zu diesem Dokument |
|---|---|---|
| `08_knowledge_atlas/ATLAS_MANIFEST.md` | **Was** der Atlas technisch ist (Knoten-Basis, Kanten-Basis, Scope v0.1) | Bleibt unverändert die technische Grundlage. Dieses Dokument regelt **wann** und **wie oft** der bestehende Scope angewendet wird, nicht **was** er umfasst. |
| `08_knowledge_atlas/scripts/compile_atlas.py` (aktuell v0.1.3) | Wie der Compiler-Lauf technisch funktioniert | Reine Implementierung. Dieses Dokument trifft keine Aussage über Code, nur über Einsatzhäufigkeit und Anlass. |
| `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md` | Das konkrete inhaltliche Ergebnis eines einzelnen, bereits abgeschlossenen Analyselaufs | Bleibt als archivierter Sprint-Report unverändert stehen (siehe Abschnitt 6). Dieses Dokument macht sein Verfahren wiederholbar, ohne seinen Inhalt zu verändern. |

**Nicht Ziel dieses Sprints:** technischer Ausbau des Atlas (neue Layer, neue Metriken, Query Engine — all das bleibt laut `ATLAS_MANIFEST.md` Abschnitt 3 explizit ausgeschlossen und wird durch dieses Dokument nicht implizit freigegeben).

---

## 2. Trigger — wann wird der Atlas erneut aktiv?

Nicht jedes Ereignis rechtfertigt einen vollständigen Content-Analysis-Sprint wie Sprint 1. Es werden zwei Reaktionsstufen unterschieden:

- **Compiler-Baseline-Check:** ein einzelner Lauf von `compile_atlas.py` (Nodes, Edges, Reference Orphans, Duplicate IDs, unaufgelöste Referenzen) gegen die zuletzt bekannte Baseline. Kosten: gering, deterministisch, bereits vollständig automatisiert (Atlas v0.1 Scope).
- **Volle Content Analysis:** das in Sprint 1 etablierte, aber weiterhin ad hoc auszuführende Verfahren (Zentralitäts- und Cluster-Ebene über mehrere Graphansichten, Structure-×-Evidence-Abgleich, vollständige Orphan-Einzelprüfung). Kosten: hoch, editorische Arbeitszeit, kein automatisierter Bestandteil des Compilers.

| Ereignis | Empfohlene Reaktion | Begründung |
|---|---|---|
| Einzelnes Buch abgeschlossen | Compiler-Baseline-Check | Ein einzelnes Buch verändert den Graphen zu inkrementell, um eine vollständige Metrik-Neuinterpretation zu rechtfertigen. Sprint 1 selbst zeigt, dass strukturelle Verschiebungen erst über mehrere Bücher hinweg sichtbar werden (z. B. MEC-0026–0029, siehe Sprint-1-Report Abschnitt 10, dort explizit als "Recency-Effekt" nach einem Fünf-Bücher-Sprint eingeordnet). |
| Buch-Batch / Themen-Sprint (Richtwert: ab etwa 3 Büchern in einem zusammenhängenden Sprint — kein hartes Zählkriterium, siehe Grundsatz unten) | Volle Content Analysis empfohlen | Der Behavioral Science Expansion Sprint 1 (5 Bücher, `CURRENT_STATE.md`) ist genau die Art von Ereignis, nach der Sprint 1 tatsächlich durchgeführt wurde — Bündel-Zuwachs ist der Punkt, an dem sich Hub- und Cluster-Struktur beobachtbar verschiebt. |
| Größerer Synthese-Sprint (SPR-XXXX) | Volle Content Analysis empfohlen | Synthese-Sprints (z. B. SPR-0001 bis SPR-0003) verändern typischerweise die Kantenstruktur am stärksten (neue P-/MOD-Querverweise über Bücher hinweg) — genau die Kantenart, die Hub- und Cluster-Metriken am empfindlichsten abbilden. |
| Release Candidate (RC) | Volle Content Analysis **verpflichtend**, Ergebnis Teil des RC-Auditpakets | Ein RC-Freeze dokumentiert bereits mehrere Reifedimensionen (vgl. `REPOSITORY_CLOSING_STATUS.md`, 14 Prüfdimensionen bei v1.0). Die Graphstruktur ist eine weitere, bisher fehlende Dimension. |
| Major Version Release | Volle Content Analysis **verpflichtend**, Snapshot wird Teil der Release-Dokumentation | Der Strukturzustand zum Veröffentlichungszeitpunkt wird spätere Vergleichsbasis (siehe Abschnitt 7, KPI-Verlauf). |
| Scientific-Debt-Update (einzelne neue Einträge) | Kein Atlas-Trigger | Reine Evidenzänderung ohne Graphstrukturänderung — der Graph selbst (Knoten/Kanten) ändert sich dadurch nicht. |
| Scientific-Debt-Update (mehrere neue Hoch-Priorität-Einträge gebündelt, z. B. wie beim External Audit Resolution Sprint) | Gezielter Structure-×-Evidence-Review (siehe Abschnitt 3), nicht voller Sprint | Nur die Schnittstelle Struktur/Evidenz ist betroffen — ein vollständiger Hub-/Cluster-Neulauf wäre hier unverhältnismäßig. |
| Größere Framework-Änderung (neue Objekttyp-Semantik, neue Beziehungstypen, z. B. eine künftige Umsetzung von OD-007/CTX oder OD-012) | Volle Content Analysis nach Umsetzung | Ändert die in `ATLAS_MANIFEST.md` Abschnitt 2 definierte Knoten-/Kanten-Basis selbst — der Graph muss danach neu interpretiert werden. |
| Reine Repository-Hygiene (Linkfixes, Tippfehlerkorrekturen, T3-Aufgaben) | Kein Trigger | Keine inhaltliche Strukturänderung; ein Compiler-Baseline-Check läuft ohnehin regelmäßig mit und würde eine unbeabsichtigte Strukturänderung ohnehin auffangen. |

**Grundsatz:** Im Zweifel zuerst der günstigere Compiler-Baseline-Check. Zeigt dieser eine auffällige Verschiebung (neue Duplicate ID, spürbarer Sprung der Orphan-Zahl, neue unaufgelöste Referenz), wird daraus — nicht automatisch, sondern durch Editor-Einschätzung — die Empfehlung für eine volle Content Analysis abgeleitet.

**Klarstellung zum Buch-Batch-Richtwert (Herausgeberbeschluss, 2026-07-05):** Die "ab etwa 3 Büchern"-Angabe ist ausdrücklich **kein hartes Zählkriterium**, sondern eine Orientierungsgröße ohne bindende Wirkung. Weder unterschreitet noch überschreitet eine bestimmte Buchzahl automatisch eine Schwelle — maßgeblich bleibt die Editor-Einschätzung im Einzelfall, gestützt auf das tatsächliche Ergebnis des Compiler-Baseline-Checks (Abschnitt 5) und die inhaltliche Kohärenz des Buch-Batches, nicht die reine Stückzahl. Zwei eng zusammenhängende Bücher können diesen Trigger rechtfertigen, vier lose verbundene Einzelanalysen dagegen nicht zwingend.

---

## 3. Analyse-Ebenen — was wird standardisiert?

| Analyse-Ebene | Kurzbeschreibung | Einordnung | Begründung |
|---|---|---|---|
| **Compiler Validation** (Node/Edge-Zählung, Duplicate IDs, unaufgelöste Referenzen) | Bereits vollständig in `compile_atlas.py` automatisiert | **Immer sinnvoll** | Kostenlos (deterministischer Skriptlauf), bildet die Integritäts-Grundlage für jede weitere Analyseebene. Ohne saubere Validation sind alle folgenden Ebenen auf unsicherem Grund. |
| **Structural Health** (Reference-Orphan-Zählung, Konnektivität des konzeptuellen Graphen ohne ST) | Ebenfalls bereits im Atlas-v0.1-Scope enthalten (`ATLAS_MANIFEST.md` Abschnitt 2.3) | **Immer sinnvoll** | Fällt als Nebenprodukt der Compiler Validation kostenlos an; liefert das früheste Warnsignal für eine "zweite, verborgene Parallelwissensbasis" (Sprint-1-Report, Abschnitt 12). |
| **Orphan Review** (qualitative Einzelklassifikation jedes Orphans, wie Sprint-1-Report Abschnitt 8) | Redaktionelle Prüfung pro Orphan gegen Objektinhalt und `SCIENTIFIC_DEBT.md` | **Nur vor Releases** (zusätzlich: sofort, wenn die Orphan-Zahl gegenüber der letzten Prüfung ungewöhnlich stark steigt) | Arbeitsintensiv (18 Orphans banden in Sprint 1 den größten Einzelaufwand). Rechtfertigt sich vor allem dort, wo Release-Dokumentation eine belastbare Aussage "alle Orphans geprüft" tragen soll. |
| **Hub Changes** (Zentralitätsvergleich der MEC-Rangfolge über Zeit) | Ad-hoc-Metrikebene außerhalb des Compilers (Sprint-1-Methodik, Abschnitt 2.3) | **Nur bei Bedarf** — konkret: bei jedem Trigger aus Abschnitt 2, der eine volle Content Analysis auslöst | Rechenaufwändiger als Compiler Validation, ohne Vergleichsbasis (mind. zwei Messpunkte) wenig aussagekräftig; sinnvoll gebündelt mit den ohnehin ausgelösten vollen Sprints. |
| **Cluster Changes** (Community-Detection über Zeit) | Gleiche Ad-hoc-Ebene wie Hub Changes | **Nur bei Bedarf**, gekoppelt an dieselben Trigger wie Hub Changes | Clustergrenzen sind bei kleinen Zuwächsen instabil (Ergebnis eines Optimierungsalgorithmus, nicht redaktionell kuratiert — Sprint-1-Report Abschnitt 2.6). Ein Vergleich lohnt erst bei größerem Zuwachs. |
| **Structure × Evidence Review** (Abgleich Zentralität/Cluster gegen `SCIENTIFIC_DEBT.md` und Evidenzlevel) | Der laut Sprint-1-Report (Abschnitt 9, 12, 13) strategisch wertvollste Einzelbefund-Typ | **Verpflichtender Bestandteil jeder vollen Content Analysis**, unabhängig davon, welcher Trigger sie ausgelöst hat | Genau diese Kombination (hohe Struktur bei bekanntem Risiko, niedrige Struktur bei hoher Qualität) war der zentrale Mehrwert von Sprint 1 gegenüber reinem Einzelobjekt-Lesen — sie darf in künftigen Zyklen nicht zur optionalen Randnotiz werden. |
| **Scientific Debt Cross-Check** (Abgleich: sind isolierte/randständige Graphbereiche bereits in `SCIENTIFIC_DEBT.md` als bewusste Entscheidung dokumentiert, wie beim Ariely-Dishonesty-Cluster, Sprint-1-Report Abschnitt 7/8) | Bestätigungsprüfung, kein neuer Befund-Typ | **Nur vor Releases** | Dient primär dazu, zum Snapshot-Zeitpunkt zu bestätigen, dass Scientific-Debt-Ledger und Atlas-Struktur widerspruchsfrei zueinanderstehen — eine Aussage, die vor allem in Release-Dokumentation Gewicht hat, nicht im laufenden Betrieb. |

---

## 4. KPIs — wenige mit echtem Steuerungswert

Von den in der Aufgabenstellung genannten Kandidaten werden **fünf** empfohlen. Die übrigen werden nicht aufgenommen — mit Begründung, nicht stillschweigend.

### 4.1 Empfohlene KPIs

| KPI | Definition | Steuerungswert |
|---|---|---|
| **Duplicate IDs** | Anzahl doppelt vergebener Objekt-IDs (Compiler-Ausgabe) | Kein Qualitätsspektrum, sondern ein Integritäts-Gate: Zielwert ist immer exakt 0. Jede Abweichung ist ein sofortiger, unzweideutiger Handlungsauslöser — kein Interpretationsspielraum nötig. |
| **Reference Orphans (Anzahl + Δ zur letzten Baseline)** | Knoten ohne eingehende oder ausgehende explizite Referenz (`ATLAS_MANIFEST.md` Abschnitt 2.3) | Ist bereits der einzige in Atlas v0.1 definierte Analyse-Zweck — ein Kernkennwert, kein Zusatz. Die Δ-Betrachtung (nicht nur der Absolutwert) zeigt, ob neue Inhalte strukturell angebunden werden oder Orphans systematisch anwachsen. |
| **Connected Components im konzeptuellen Graphen (A/MEC/P/T/MOD, ohne ST)** | Anzahl getrennter Zusammenhangskomponenten | Ein Sprung von 1 auf ≥2 wäre das stärkste mögliche Alarmsignal ("zweite, verborgene Parallelwissensbasis") — in Sprint 1 lag dieser Wert bei exakt 1 (Abschnitt 2.4). Ein einzelner, leicht überwachbarer Schwellenwert. |
| **Scientific-Debt-Dichte unter den strukturell zentralen Objekten** (Anteil der Top-Decile-Degree-MECs mit offenem `SCIENTIFIC_DEBT.md`-Eintrag der Priorität Hoch) | Operationalisiert den zentralen Sprint-1-Befund (MEC-0018-Konstellation, Abschnitt 3.2/9) als wiederholbare Kennzahl statt als einmalige Beobachtung | Macht sichtbar, ob strukturelles Gewicht und dokumentiertes Evidenzrisiko im Zeitverlauf auseinanderlaufen oder konvergieren — genau die Frage, die Sprint 1 als wichtigsten Einzelbefund einstufte. |
| **Anteil E4/E5 unter den strukturell zentralen Objekten** (Top-Decile Degree, nicht repositoryweit) | Wie oben, gespiegelt: prüft, ob strukturelle Zentralität mit hoher statt niedriger Evidenzlage einhergeht | Ergänzt die vorherige Kennzahl um die positive Kontrollprobe (MEC-0002/MEC-0003 als robuster Kern, Sprint-1-Report Abschnitt 3.1) — beide zusammen zeigen, ob der "robuste Kern" die Ausnahme oder die Regel bleibt. |

### 4.2 Bewusst nicht aufgenommen

| Kandidat | Warum nicht |
|---|---|
| Node Count / Edge Count (absolut) | Reines Wachstumsmaß ohne Steuerungsaussage — wird bereits in `00_project/REPOSITORY_KPIS.md` pro Buch getrackt (Statements/Buch, Objekte gesamt). Eine zweite, redundante Zählung im Atlas-Kontext schafft keinen zusätzlichen Steuerungswert. |
| MEC/P/T-Verhältnis | Strukturell interessant, aber es existiert noch kein aus Daten abgeleiteter Zielkorridor ("gesunder" Bereich) — Sprint 1 hat keinen Referenzwert etabliert. Eine Kennzahl ohne Schwellenwert hat noch keine Entscheidungskonsequenz. Kandidat für eine spätere Aufnahme, sobald über mehrere Messpunkte hinweg ein Korridor erkennbar wird (siehe KPI-Verlauf, Abschnitt 7). |
| Anteil E4/E5 (repositoryweit, nicht auf Hubs beschränkt) | Bereits als "Scientific Confidence" in `00_project/REPOSITORY_KPIS.md` geführt — Doppelerhebung ohne Zusatznutzen. Der hier empfohlene KPI (4.1) unterscheidet sich davon gerade durch die Beschränkung auf strukturell zentrale Objekte. |
| Durchschnittliche Source Diversity | Wissenschaftlich interessant (vgl. MOD-0002-Befund, Sprint-1-Report Abschnitt 6: scheinbare vs. echte Quellenvielfalt), aber in Sprint 1 nur für MEC/MOD ad hoc berechnet, ohne repositoryweit einheitliche Definition. Bleibt vorerst Diagnoseinstrument innerhalb einzelner Content-Analysis-Sprints, nicht dauerhafter KPI, bis eine einheitliche Berechnungsregel definiert ist. |

---

## 5. Governance-Prozess

Der im Auftrag vorgeschlagene Zyklus wird übernommen und um zwei Punkte präzisiert: eine explizite Abzweigung Baseline-Check vs. volle Analyse, und eine explizite Firewall gegen direkte Repository-Schreibzugriffe durch den Atlas selbst.

```
1. Trigger-Erkennung          (Abschnitt 2: Ereignis eingetreten?)
        ↓
2. Compiler-Lauf               (immer, Pflicht — compile_atlas.py)
        ↓
3. Baseline-Vergleich          (Δ zur letzten bekannten Baseline)
        ↓
   ── Abzweigung ──
   Auffällig / Trigger für volle Analyse erfüllt?
        │                              │
       Nein                            Ja
        │                              ↓
   Ende (Baseline-Check           4. Content Analysis
   dokumentiert, s. Abschnitt 6)     (Hub/Cluster/Structure×Evidence,
                                       gemäß Abschnitt 3)
                                       ↓
                                    5. Editorial Review
                                       (Editor ordnet ein, entscheidet nicht)
                                       ↓
                                    6. Decision
                                       (Herausgeber Felix entscheidet)
                                       ↓
                                    7. Repository Update
                                       (über bestehende Kanäle, s. u.)
                                       ↓
                                    8. Release-Dokumentation
                                       (nur bei RC-/Release-Trigger)
```

**Zu Schritt 5 (Editorial Review):** Gilt exakt das in `SALES_CODEX_OPERATING_MANUAL.md` Abschnitt 2 definierte Rollenmodell. Der Editor (Claude) ordnet Befunde ein und formuliert Empfehlungen (wie in Sprint-1-Report Abschnitt 11–13), trifft aber keine Herausgeberentscheidung.

**Zu Schritt 6 (Decision):** Führt, falls die Befunde eine Handlung nahelegen, entweder zu einer neuen Eintragung in `00_project/OPEN_DECISIONS.md` (bei grundsätzlichen Fragen) oder zu einer direkten Freigabe eines punktuellen Folgeauftrags (bei klar umrissenen Einzelbefunden, wie der in Sprint 1 empfohlenen MEC-0018-Sichtbarkeitsprüfung).

**Zu Schritt 7 (Repository Update) — wichtigste Klarstellung dieses Abschnitts:** Der Atlas selbst verändert nie Wissensobjekte, Templates oder Framework-Dateien. Jede aus einer Atlas-Analyse resultierende Änderung läuft ausschließlich über die bereits bestehenden Kanäle: Buchanalyse (T1), Framework-Arbeit (T2), Governance/Decision Resolution (T8), Research Program (T10) — je nachdem, welcher Kanal fachlich zuständig ist. Der Atlas ist und bleibt ein reines Diagnoseinstrument (vgl. `ATLAS_MANIFEST.md` Abschnitt 4, "Nicht-Ziele").

**Zu Schritt 8 (Release-Dokumentation):** Nur relevant, wenn der Trigger ein RC- oder Version-Release-Ereignis war (Abschnitt 2). Die Kernbefunde fließen in das ohnehin bestehende Release-Dokument ein (Muster: `99_archive/v1.0_release/`), nicht in ein zusätzliches, separates Atlas-Release-Dokument (siehe Abschnitt 7).

---

## 6. Reporting

| Dokument(typ) | Dauerhaft / einmalig / Release-Bestandteil / reiner Diagnosebericht |
|---|---|
| `08_knowledge_atlas/ATLAS_MANIFEST.md` | **Dauerhaft**, Reference. Wird bei Scope-Erweiterung fortgeschrieben (neue Versionsnummer), nicht bei jedem Analysezyklus. |
| `08_knowledge_atlas/output/*.csv`, `atlas_compiler_report.md`, `atlas_network.dot` | **Dauerhaft, aber lebende Artefakte** — werden bei jedem Compiler-Lauf überschrieben, nicht einzeln versioniert. Versionierung erfolgt implizit über Git-Historie, nicht über Dateikopien. |
| `KNOWLEDGE_ATLAS_GOVERNANCE.md` (dieses Dokument) | **Dauerhaft**, Reference. Wird bei Prozessänderungen fortgeschrieben (analog `TASK_TYPES.md`), nicht gestapelt. |
| `KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_N_REPORT.md` (N fortlaufend) | **Einmalig je Zyklus, dauerhaft archiviert.** Wird nie überschrieben oder rückwirkend geglättet — jeder abgeschlossene Zyklus erhält einen neuen, eigenständigen Report (Sprint 1 trägt bereits selbst die Kennzeichnung "Archived" im Kopf). |
| Release-Dokumentation (z. B. künftige `SALES_CODEX_VERSION_X_RELEASE.md`) | **Release-Bestandteil.** Enthält nur die Executive-Summary-Ebene eines Content-Analysis-Zyklus (Kernbefunde, KPI-Snapshot), nicht die vollständigen Zentralitäts-/Clustertabellen — diese bleiben im zugehörigen Sprint-Report. |
| Technische Compiler-Berichte (`ATLAS_HARDENING_SPRINT_*`, `ATLAS_ARCHITECTURE_REVIEW_*`, `ATLAS_RELEASE_VERIFICATION_*`) | **Reine Diagnose-/Engineering-Berichte, außerhalb dieses Governance-Zyklus.** Sie dokumentieren Compiler-Code-Änderungen (technische Sprints), nicht inhaltliche Content-Analysis-Zyklen — bewusst nicht Gegenstand dieses Dokuments (Scope: Prozesse, keine Technik). |

**Kein neuer Dokumenttyp für Compiler-Baseline-Checks:** Ein einzelner Baseline-Check (Abschnitt 2/5, "Ende"-Zweig) erzeugt keine eigene Datei. Er wird, falls in einer Session durchgeführt, als Eintrag in `00_project/SESSION_LOG.md` festgehalten. Ein auffälliger Befund führt nicht zu einem eigenen Log-Eintrag, sondern direkt zur Eskalation in einen vollen Content-Analysis-Zyklus (Abschnitt 2). Diese bewusste Zurückhaltung vermeidet unnötige neue Dateitypen für ein Ereignis, das im Regelfall unauffällig verläuft.

---

## 7. Versionierung

**Ja, Atlas-Analysen sollten versioniert werden — aber mit möglichst wenigen, bereits im Repository etablierten Mitteln, statt einer neuen Versionierungsachse.**

Zur Einordnung: Der Compiler selbst trägt bereits eine eigene technische Version (`v0.1`, `v0.1.1`, `v0.1.2`, `v0.1.3` — siehe `ATLAS_HARDENING_SPRINT_V0_1_3_REPORT.md`). Diese Versionsachse ist Gegenstand technischer Engineering-Sprints und bleibt außerhalb des Scopes dieses Dokuments (siehe Abschnitt 1 und 6). Die hier zu klärende Frage betrifft ausschließlich die **Analyseergebnisse**, nicht den Code, der sie erzeugt.

Empfohlen werden zwei Ebenen statt drei:

1. **Sprint Reports** (`KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_N_REPORT.md`, N fortlaufend) als primäre, unveränderliche Versionierungseinheit — jeder real durchgeführte volle Analysezyklus (Abschnitt 2) erhält genau einen neuen, nummerierten Report. Dies deckt sowohl reguläre Zyklen als auch RC-/Release-ausgelöste Zyklen ab.
2. **Kein eigener "Release Report"-Dateityp.** Fällt ein Sprint-Report mit einem RC- oder Release-Ereignis zusammen, wird dies im Kopf des jeweiligen Sprint-Reports vermerkt ("Release-verknüpft: <Release-Name>"), und die Kernbefunde werden zusätzlich in das ohnehin bestehende Release-Dokument übernommen (Abschnitt 6). Ein dritter, paralleler Dokumenttyp würde Struktur-Sprawl erzeugen, ohne einen Informationsgewinn zu bieten, den nicht bereits die Kombination aus Sprint-Report + Release-Dokument leistet.
3. **Kein eigener "Major-Version Report".** Stattdessen führt dieses Governance-Dokument selbst — sobald erste Zyklen tatsächlich durchgeführt wurden — einen fortlaufend ergänzten **KPI-Verlauf** (Anhang, wird nach dem ersten reale angewendeten Zyklus eröffnet): eine einzige Tabelle mit den fünf KPIs aus Abschnitt 4 je abgeschlossenem Zyklus. Diese Verlaufstabelle ist der zentrale Ort für jede künftige Reifegrad-/Statusübergangs-Entscheidung (vgl. OD-009), statt dass Trendinformation über mehrere Einzelreports verstreut bleibt.

**Begründung für zwei statt drei Ebenen:** Das Repository verfolgt bereits an anderer Stelle den Grundsatz, keine neuen Dokumentklassen ohne echten Bedarf einzuführen (vgl. OD-011, Diskussion um das Verhältnis dreier bereits bestehender Literatur-/Debt-Dokumente zueinander). Zwei klar abgegrenzte Ebenen (unveränderliche Einzel-Reports + eine lebende Trendtabelle) genügen, um sowohl Nachvollziehbarkeit einzelner Zyklen als auch Langzeittrend abzubilden.

### Anhang: KPI-Verlauf

*Wird nach dem ersten gemäß dieser Governance durchgeführten Zyklus eröffnet. Sprint 1 (2026-07-05) diente der Methodenentwicklung und wird hier als Ausgangsmessung nachträglich referenziert, sobald ein zweiter Messpunkt vorliegt — ein Einzelwert allein bildet noch keinen Verlauf.*

| Zyklus | Datum | Trigger | Duplicate IDs | Reference Orphans (Δ) | Connected Components (konzept.) | SciDebt-Dichte Top-Decile | Anteil E4/E5 Top-Decile |
|---|---|---|---|---|---|---|---|
| Sprint 1 (Referenz, Methodenentwicklung) | 2026-07-05 | Herausgeberauftrag (ad hoc, kein Trigger gemäß Abschnitt 2, da vor Verabschiedung dieser Governance) | 0 | 18 (—, erste Messung) | 1 | nicht separat beziffert (siehe Sprint-1-Report Abschnitt 9, qualitativ: MEC-0018-Familie) | nicht separat beziffert (siehe Sprint-1-Report Abschnitt 3.1, qualitativ: MEC-0002/0003) |

---

## 8. Grenzen — was der Atlas ausdrücklich NICHT übernimmt

Diese Liste ergänzt, wiederholt aber bewusst auch, was `ATLAS_MANIFEST.md` Abschnitt 4 bereits als Nicht-Ziel festhält — Governance darf diese Grenze nicht stillschweigend verschieben.

- **Keine automatische Qualitätsbewertung.** Ein Reference Orphan, ein niedriger Zentralitätswert oder ein dichter Ein-Quellen-Cluster ist ausschließlich eine strukturelle Beobachtung, keine Aussage über fachliche Qualität (`ATLAS_MANIFEST.md` Abschnitt 4).
- **Keine Evidenzbewertung.** Der Atlas ändert nie ein Evidenzlevel (E1–E5) und ersetzt keine Stufe-3-Validierung (`SALES_CODEX_OPERATING_MANUAL.md` Abschnitt 6). Er stellt Struktur- und Evidenzbefunde nebeneinander (Abschnitt 3, Structure × Evidence Review), bewertet Evidenz aber nicht selbst.
- **Keine Forschungsentscheidung.** Befunde wie "MEC-0020 hat null Prinzip-Anbindungen trotz E4" (Sprint-1-Report Abschnitt 10) werden als Frage, nicht als Auftrag formuliert. Ob daraus tatsächlich neue Forschung oder ein neues Prinzip wird, ist ausschließlich Herausgeberentscheidung.
- **Keine automatische Priorisierung.** Die Research and Synthesis Priority Map (Sprint-1-Report Abschnitt 11) ist eine editorische Einschätzung, kein verbindliches Ranking. Der Atlas erzeugt keine automatisch sortierte Aufgabenliste, die ohne Herausgeberprüfung abgearbeitet würde.
- **Keine eigenständige Repository-Änderung.** Wie in Abschnitt 5 (Schritt 7) festgehalten: Der Atlas hat keinen eigenen Schreibpfad in `03_knowledge_base/`, `01_framework/` oder andere Wissensobjekt-Bereiche. Jede Änderung läuft über bestehende, bereits definierte Kanäle.
- **Keine Auflösung offener Entscheidungen.** Der Atlas kann eine Open Decision anregen (z. B. eine strukturelle Beobachtung, die eine neue OD-Eintragung rechtfertigt), schließt aber nie selbst eine bestehende Open Decision aus `OPEN_DECISIONS.md`.
- **Keine Aussage über Kausalität oder inhaltliche Richtigkeit einer Kante.** Wie in `ATLAS_MANIFEST.md` Abschnitt 2.2 festgelegt, ist jede Kante ungerichtet-neutral — der Atlas unterscheidet nicht "unterstützt" von "widerspricht". Diese Einschränkung gilt unverändert auch für jede künftige Content Analysis.

**Zusammenfassender Grundsatz:** Der Atlas unterstützt redaktionelle Urteilsbildung, indem er sichtbar macht, was durch reines Lesen einzelner Objekte verborgen bliebe. Er ersetzt diese Urteilsbildung nicht.

---

## 9. Herausgeberbeschluss

**Status: Freigegeben (2026-07-05).** Felix hat entschieden: Mit dieser Freigabe gelten der Editorial Review Sprint (siehe `00_project/EDITORIAL_REVIEW_SPRINT_MEC0018_REPORT.md`, Status: Abgeschlossen/Archived) und die Aufbauphase des Knowledge Atlas als abgeschlossen. Die Knowledge Atlas Governance gilt — nach Einarbeitung der in Abschnitt 2 vorgenommenen Präzisierung (Buch-Batch-Trigger als Richtwert statt harte Zählregel) — als verbindlicher Standard des Sales Codex.

**Umgesetzte Präzisierung:** Die ursprüngliche Formulierung "Faustregel: ≥3 Bücher" wurde durch einen ausdrücklich als unverbindlich gekennzeichneten Richtwert ersetzt (Abschnitt 2, Trigger-Tabelle und die dort neu ergänzte Klarstellung). Keine weiteren inhaltlichen Änderungen an diesem Dokument waren Teil dieses Beschlusses.

**Bedeutung für den Betrieb:** Der Knowledge Atlas geht damit vom Aufbau- in den regulären Betriebs- und Wartungsmodus über und dient künftig als dauerhaftes Diagnose- und Steuerungsinstrument des Sales Codex gemäß Abschnitt 2–8 dieses Dokuments. Weitere Entwicklungsarbeiten am Atlas (technischer Ausbau, Compiler-Änderungen, Scope-Erweiterungen über `ATLAS_MANIFEST.md` hinaus) erfolgen nur noch bei begründetem Bedarf oder im Rahmen künftiger, separat freizugebender Architekturentscheidungen — nicht im Rahmen des laufenden Betriebs.

**Projektperspektive:** Der nächste Hauptarbeitsblock des Sales Codex verlagert den Schwerpunkt von der Entwicklung der Wissensinfrastruktur (Compiler, Atlas, Framework-Ausbau) auf die Nutzung und Weiterentwicklung des vorhandenen Wissensbestands. Diese Verlagerung selbst ist nicht Gegenstand dieses Dokuments — sie wird an anderer Stelle (`00_project/NEXT_ACTION.md`, `CURRENT_STATE.md`) nachvollzogen, sobald sie dort formal abgebildet wird.

---

*Dieses Dokument ist ab dem in Abschnitt 9 dokumentierten Herausgeberbeschluss (2026-07-05) verbindlicher Governance-Standard für den Knowledge Atlas — kein Wissensobjekt und keine Framework-Datei im Sinne von `01_framework/`. Es trifft keine inhaltliche Bewertung einzelner Wissensobjekte. Änderungen an dieser Governance erfordern künftig dieselbe Form der Herausgeberentscheidung wie ihre ursprüngliche Freigabe.*
