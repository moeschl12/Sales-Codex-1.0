# PEER REVIEW DECISION REPORT — Sprint 1

**Dokumentklasse:** Governance  
**Datum:** 2026-07-01  
**Reviewer:** Peer Reviewer für verhaltensökonomische, sozialpsychologische und methodenorientierte Vertriebsforschung  
**Review-Paket:** SCRP-0001 – Sales Core (Sprint 1)  
**Editor:** Claude / Cowork (Repository-Editor)  
**Freigabe:** Felix (Herausgeber)

---

## Executive Summary

Der Peer Review von Sprint 1 ist wissenschaftlich fundiert, methodisch präzise und enthält sieben inhaltliche Empfehlungen unterschiedlicher Priorität. Keine der Empfehlungen ist pauschal falsch oder zu verwerfen — sie bewegen sich auf einem Spektrum von zwingend notwendig bis strukturell verfrüht.

Von den sieben Kernempfehlungen werden **vier übernommen** (davon zwei vollständig, zwei teilweise), **zwei abgelehnt** mit expliziter Begründung, und **eine** als offene Herausgeber-Entscheidung dokumentiert.

Zusätzlich zu den sieben Kernempfehlungen enthält der Review zwei weiterer Priorität-A-Korrekturen (MEC-0010 E-Level, B-0005-Vollständigkeit) und eine Literaturliste für Sprint 2. Diese werden ebenfalls entschieden.

**Gesamturteil:** Sprint 1 ist valide. Die Scientific Debt ist korrekt dokumentiert. Die Architektur hält akademischer Prüfung stand. Der Sales Codex ist bereit für Sprint 2 nach Umsetzung der übernommenen Korrekturen.

---

## Einzelentscheidungen

---

### Empfehlung 1 — Herabstufung MEC-0011 (Mirror Neurons / Neural Coupling)

**Empfehlung des Reviewers:**  
MEC-0011 soll als „rein spekulative Hypothese (E1)" isoliert werden. Die Verknüpfung von verbalem Spiegeln mit Spiegelneuronen-Theorien (Rizzolatti, Macaken-Basis) ist eine unzulässige populärwissenschaftliche Extrapolation durch Voss. Stephens/Hasson (2010) belegen neuronale Synchronisation bei gelungener Kommunikation allgemein — nicht beim strategischen Nachplappern von Satzenden. Priority: **A**.

**Entscheidung: Teilweise übernehmen**

**Begründung:**  
Der Reviewer hat mit seiner Kern-Kritik recht: Die in MEC-0011 implizierte Kausalkette `verbales Mirroring → Spiegelneuronen-Aktivierung → Neural Coupling` ist wissenschaftlich nicht belegt. Es handelt sich um eine didaktische Extrapolation von Voss, keine etablierte Forschungsaussage.

Eine vollständige Herabstufung auf E1 (`rein spekulativ`) für das gesamte Objekt ist jedoch nicht angemessen, weil MEC-0011 zwei konzeptionell trennbare Bestandteile enthält:

1. **Spiegelneuronen-Verbindung (Rizzolatti → Isopraxismus → Mirroring):** Diese ist E1 — spekulative Extrapolation vom Primaten-Experiment auf menschliche Verhandlungsinteraktion. Keine direkte Evidenz. → **E1-Status in der biologischen Begründung.**

2. **Neural Coupling (Stephens/Hasson 2010):** Eine methodisch solide fMRT-Studie mit echter akademischer Peer-Review. Belegt neuronale Synchronisation bei erfolgreicher Kommunikation allgemein. Die Einschränkung des Reviewers ist korrekt: Diese Studie belegt NICHT, dass spezifisch verbales Mirroring (1–3-Wort-Wiederholung) Neural Coupling auslöst. Sie belegt, dass erfolgreiche Kommunikation generell mit neuronaler Synchronisation einhergeht. → **E2-Status für den allgemeinen Neural-Coupling-Effekt.**

Das Gesamtobjekt MEC-0011 wird daher von **E3 auf E2** herabgestuft, mit expliziter E1-Markierung für den Spiegelneuronen-Anteil. MEC-0011 bleibt als Objekt erhalten, da T-0012 (Mirroring) einen erklärenden Mechanismus benötigt — aber dieser Mechanismus muss korrekt eingestuft sein.

**Betroffene Repository-Objekte:**
- `03_knowledge_base/mechanisms/MEC-0011_neural_coupling_durch_isopraxismus.md`
- `00_project/SCIENTIFIC_DEBT.md`

**Notwendige Änderungen:**
1. E-Level im MEC-0011-Objekt: von E3 auf **E2 (gesamt) / E1 (Spiegelneuronen-Basis)**
2. Biologische Begründung (Rizzolatti-Abschnitt): explizit als **E1/spekulativ** kennzeichnen
3. Stephens/Hasson-Abschnitt: präzisieren — belegt allgemeine Kommunikations-Synchronisation, NICHT spezifisch verbales Mirroring
4. Scientific Debt: bestehenden Eintrag aktualisieren (Replikationsrisiko Spiegelneuronen → jetzt E1-Status)
5. Überschrift im Objekt anpassen: MacLean/Rizzolatti-Anteil als „Historische Erklärungsannahme (E1)" kennzeichnen

---

### Empfehlung 2 — Trennung der Triune-Brain-Theorie von MEC-0012

**Empfehlung des Reviewers:**  
Die von Voss eingewobene Triune-Brain-Theorie (MacLean) ist neurobiologisch seit den 1990er Jahren falsifiziert. Sie muss aus MEC-0012 eliminiert werden. Der Kahneman-Kern (System 1 vs. System 2) bleibt bestehen. Priority: **B**.

**Entscheidung: Übernehmen**

**Begründung:**  
MEC-0012 enthält bereits einen ⚠-Hinweis: „MacLean's Triune-Brain-Modell ist in der modernen Neurowissenschaft stark vereinfacht und teils kritisiert — Voss übernimmt die didaktische Version, nicht die wissenschaftliche Präzision." Diese Warnung ist korrekt, aber unzureichend.

Die Triune-Brain-Terminologie (Reptilian Brain / Limbisches System / Neokortex als evolutionäre Schichtung) ist in der neurowissenschaftlichen Literatur seit den 1990er Jahren als anatomisch überholt eingestuft. Sie in einem Wissensmodell zu verwenden, das auf E4-Evidenz (Kahneman) abzielt, senkt die wissenschaftliche Integrität des Objekts, ohne dass die didaktische Nomenklatur zum Erklärungsbeitrag notwendig wäre.

Der Kahneman Dual-Process-Rahmen (E4) ist selbsttragend und für Vertriebsanwendungen vollständig hinreichend. Die MacLean-Terminologie wird aus dem Erklärungsabschnitt entfernt. Sie wird als historische Fußnote (Voss' Quell-Nomenklatur) erhalten, mit explizitem Falsifizierungsvermerk.

**Betroffene Repository-Objekte:**
- `03_knowledge_base/mechanisms/MEC-0012_dual_process_system1_zu_system2.md`

**Notwendige Änderungen:**
1. Im Erklärungsabschnitt: „Dreistufiger Emotionskanal (Voss/MacLean)" entfernen oder als historische Quell-Notiz markieren (mit Falsifizierungsvermerk)
2. Voss' Leit-Aphorismus bleibt erhalten (er ist inhaltlich korrekt, unabhängig von der MacLean-Begründung)
3. E-Level: Anpassung auf E4 (Kahneman, Hauptkern) / E3 (Verhandlungsanwendung) — E1-Anteil für MacLean wird eliminiert, da er die Aussage nicht mehr trägt
4. In der Wissenschaftlichen Grundlage: MacLean-Referenz mit explizitem Falsifizierungsvermerk behalten (dokumentarische Integrität), aber aus dem kausalen Erklärungspfad entfernen

---

### Empfehlung 3 — Neubewertung proprietärer Practitioner-Studien (Huthwaite/CEB)

**Empfehlung des Reviewers:**  
Wissensobjekte, die exklusiv auf CEB-Daten (Challenger, N=6.000) oder Huthwaite-Daten (SPIN) beruhen, sollen von E3 auf E2 herabgestuft werden, solange keine unabhängige Peer-Review-Replikation vorliegt. Priority: **A**.

**Entscheidung: Teilweise übernehmen**

**Begründung:**  
Der Reviewer hat methodisch recht: Eine Studie, deren Rohdaten, Faktorladungen und Signifikanztests nicht öffentlich einsehbar und replizierbar sind, erfüllt streng genommen nicht die Anforderungen von E3 im Codex-Sinne (drei unabhängige Quellen oder Forschungsstränge, Herausgeber-Freigabe). Die CEB-Befragung (N=6.000) und Huthwaites Feldbeobachtungen sind proprietär und nicht peer-reviewed.

Eine sofortige Massenherabstufung aller betroffenen Objekte ist jedoch aus zwei Gründen nicht angemessen:

1. **Scope-Problem:** Es gibt mehr als 20 Objekte, die auf CEB oder Huthwaite referenzieren. Eine korrekte Einzelprüfung jedes Objekts, ob es noch weitere Stützquellen hat, die E3 rechtfertigen, würde den Rahmen dieses Decision Reports sprengen und ist eine Sprint-2-Aufgabe.

2. **Nuanciertes Kriterium:** Das Wissensmodell erlaubt E3 auch für „gut begründete Primärstudien mit klarer Methodik" — das trifft auf CEB und Huthwaite mit Einschränkungen zu. Die Frage ist, ob das Fehlen öffentlicher Rohdaten allein eine Herabstufung rechtfertigt.

**Übernommene Maßnahme:** Ergänzung eines neuen Scientific-Debt-Eintrags in `SCIENTIFIC_DEBT.md` mit der expliziten Kategorie „Proprietäre-Studien-Validierung". Dieser Eintrag benennt systematisch alle Objekte, die exklusiv auf CEB oder Huthwaite-Daten beruhen ohne unabhängige Stützquelle, und markiert sie für individuelle Prüfung in Sprint 2.

Einzelne E-Level-Korrekturen erfolgen only für Objekte, bei denen im Review bereits klar wurde, dass keine zusätzliche Stützquelle vorliegt und E3 deshalb nicht haltbar ist.

**Betroffene Repository-Objekte:**
- `00_project/SCIENTIFIC_DEBT.md`
- Alle Objekte mit exklusivem CEB/Huthwaite-Verweis (Prüfung Sprint 2)

**Notwendige Änderungen:**
1. SCIENTIFIC_DEBT.md: Neuer Abschnitt „Systemischer Scientific Debt — Proprietäre Studien"
2. Konkrete Auflistung: ST-0107 bis ST-0132 (Challenger Sale), ST-0001 bis ST-0023 (SPIN-Huthwaite-Bereich) als Kandidaten für E-Level-Review

---

### Empfehlung 4 — Mögliche Fusion von MEC-0006 und MEC-0014

**Empfehlung des Reviewers:**  
MEC-0006 (Social Proof) und MEC-0014 (Konsens in Gruppen) sind konzeptionell redundant. Sie beschreiben denselben psychologischen Entlastungsmechanismus unter Unsicherheit. Fusion empfohlen für nächsten Sprint. Priority: **B**.

**Entscheidung: Ablehnen**

**Begründung:**  
Diese Empfehlung widerspricht dem Canonical Knowledge Model des Sales Codex in einem entscheidenden Punkt.

Das CKM definiert Mechanismen als eindeutig durch ihren **kausalen Pfad**: `Stimulus X → psychologischer Prozess Y → Reaktion Z`. Zwei Mechanismen sind nur dann identisch (und damit fusionierbar), wenn X, Y **und** Z jeweils gleich sind. Wenn der Prozess Y gleich ist, aber die Stimuli verschieden sind, gilt: **„Getrennt halten; Verweis aufeinander in Offene Fragen."**

MEC-0006 und MEC-0014 haben denselben psychologischen Prozess Y (soziale Signale reduzieren Unsicherheit), aber fundamental verschiedene Stimuli und Reaktionen:

| | MEC-0006 | MEC-0014 |
|---|---|---|
| **Stimulus X** | Externes Marktverhalten (andere Kunden kaufen) | Interner Organisationskonsens (Kollegen stimmen zu) |
| **Prozess Y** | Unsicherheitsreduktion durch soziales Signal | Unsicherheitsreduktion durch soziales Signal |
| **Reaktion Z** | Korrektheitsbewertung der Entscheidung | Risikoverteilung / persönliche Absicherung |
| **Kontext** | B2C und B2B, externe Referenz | B2B-Gruppenkauf, intern |

MEC-0014 selbst dokumentiert bereits korrekt: „Unterschied: Korrektheitssignal (MEC-0006) vs. Sicherheitsmechanismus (MEC-0014)." Diese Unterscheidung ist vertrieblich hochrelevant: T-0009 (Branchenreferenz) aktiviert MEC-0006. T-0020 (Stakeholder-Tailoring) aktiviert MEC-0014. Wer beide auf einen Mechanismus reduziert, verliert die differenzierte Technikazuweisung.

Darüber hinaus: Fusionen sind laut Operating Manual und CKM **Herausgeber-Entscheidungen** — nicht Redaktionsentscheidungen. Eine Ablehnung durch den Editor schließt eine spätere Herausgeber-Entscheidung zur Fusion nicht aus.

**Maßnahme:** Eintrag beider Objekte als Fusion-Kandidaten in `review_queue.md` mit Begründung für Herausgeber-Entscheidung.

**Betroffene Repository-Objekte:**
- `00_project/review_queue.md`
- MEC-0006 und MEC-0014: gegenseitige Verweise ergänzen (bereits teilweise vorhanden)

---

### Empfehlung 5 — Bewertung der Meta-Prinzipien (P-S1-001 bis P-S1-004)

**Empfehlung des Reviewers:**  
Die vier Meta-Prinzipien stellen den höchsten wissenschaftlichen Mehrwert von Sprint 1 dar. Sie sind eigenständig und sollen keinesfalls in bestehende Einzelprinzipien integriert werden. Sie beweisen die Syntheseleistung des Codex. Priority: **implizite Bestätigung, keine Änderung empfohlen**.

**Entscheidung: Bestätigung ohne Änderung**

**Begründung:**  
Der Reviewer bestätigt explizit, dass P-S1-001 bis P-S1-004 methodisch korrekt platziert sind. Es ist keine Änderung empfohlen — die Empfehlung lautet, das Bestehende zu erhalten.

Keine Repository-Änderungen erforderlich. Diese Entscheidung wird hier dokumentiert als Bestätigung des Status quo.

**Betroffene Repository-Objekte:** keine

---

### Empfehlung 6 — Priorisierung von The JOLT Effect (B-0006)

**Empfehlung des Reviewers:**  
Die Analyse des JOLT Effect (Matthew Dixon & Ted McKenna, 2022) ist der vielversprechendste theoretische Hebel zur Auflösung von W-001 (Teach First vs. Diagnose First). Priority: **B**.

**Entscheidung: Übernehmen**

**Begründung:**  
Der Reviewer nennt einen konkreten, wissenschaftlich begründeten Grund für die Priorisierung: W-001 ist der zentrale ungelöste Widerspruch des Sales Codex Sprint 1. The JOLT Effect ist das direkte Folgewerk von Matthew Dixon (Co-Autor von The Challenger Sale) und adressiert explizit die Frage, warum Käufer trotz Überzeugtsein nicht kaufen. Dies ist die präzise Fragestellung hinter W-001 (Status-quo-Präferenz als Kaufblocker vs. Insight als Kaufauslöser).

Das Buch liegt bereits im Repository (`02_sources/books/_OceanofPDF.com_The_JOLT_Effect_-_Matthew_Dixon_Ted_McKenna.epub`). Die Priorisierung ist ohne Framework-Änderung umsetzbar und erfordert nur einen Backlog-Eintrag.

**Betroffene Repository-Objekte:**
- `00_project/backlog.md`

**Notwendige Änderungen:**
1. Eintrag in backlog.md: B-0006 / The JOLT Effect als nächster Buchanalyse-Task mit explizitem Verweis auf W-001

---

### Empfehlung 7 — Einführung eines Meme-Filters

**Empfehlung des Reviewers:**  
Ergänzung des Modells um eine qualitative Variable, die erfasst, ob QK-Konvergenz auf echter unabhängiger Beobachtung beruht oder auf gegenseitiger literarischer Beeinflussung (Meme-Replikation). Priority: **C (optional)**.

**Entscheidung: Nicht übernehmen (offene Empfehlung)**

**Begründung:**  
Die intellektuelle Substanz dieser Empfehlung ist valide. Der Reviewer benennt ein reales methodologisches Risiko: Wenn Cialdini → Voss → Keenan alle denselben US-amerikanischen Corporate-Training-Zeitgeist abbilden, steigt der QK-Wert auf 3, ohne dass echter unabhängiger Beobachtungsgeist dahintersteht. Das ist kein triviales Problem.

Die Einführung eines Meme-Filters wäre jedoch eine **Framework-Änderung**: Neues Metadatenfeld für alle Wissensobjekte, neues Bewertungskriterium für das QK-Rating-System, neue Dokumentationsanforderung für alle zukünftigen Objekte. Das Operating Manual ist eindeutig: „Keine Framework-Änderungen — Ordnerstruktur, Templates und Methodik werden nicht eigenständig modifiziert."

**Maßnahme:** Dokumentation als offene Empfehlung in `00_project/OPEN_DECISIONS.md` für Herausgeber-Entscheidung in Sprint 2.

---

### Zusatzentscheidung A — MEC-0010 E-Level-Korrektur

**Empfehlung des Reviewers:**  
MEC-0010 (Amygdala-Regulation durch affektives Labeling) muss von E3 auf E2 herabgestuft werden. Der direkte Transfer von Liebermans fMRT-Laborstudie auf verbale Interaktionen in B2B-Verhandlungsumgebung ist nicht belegt. Priority: **A (zwingend)**.

**Entscheidung: Übernehmen**

**Begründung:**  
Diese Korrektur ist sachlich korrekt. MEC-0010 hat aktuell E3 mit einer Einschränkungsnotiz. Die Einschränkung ist jedoch nicht stärker als E2 rechtfertigt: Lieberman (2007) ist eine Laborstudie mit Bildmaterial (keine Verhandlungssituation). Der Transfer auf verbales Labeling in echten Gesprächen ist plausibel, aber nicht direkt getestet. Scientific Debt-Einträge F-001 und F-002 dokumentieren dies bereits — aber das E-Level am Objekt selbst spiegelt dies noch nicht.

**Betroffene Repository-Objekte:**
- `03_knowledge_base/mechanisms/MEC-0010_amygdala_regulation_durch_labeling.md`

**Notwendige Änderungen:**
1. E-Level: von E3 auf **E2** (mit Vermerk: Lieberman 2007 als Laborstudie, Transfer auf verbale B2B-Interaktion plausibel aber unbelegt)

---

### Zusatzentscheidung B — B-0005 Gap Selling Vollständigkeit

**Empfehlung des Reviewers:**  
Die „partielle PDF-Quelle" (B-0005) stellt ein unzulässiges Risiko für die systematische Absicherung des Modells dar. Priority: **A**.

**Entscheidung: Übernehmen als Scientific Debt**

**Begründung:**  
B-0005 (Gap Selling) wurde auf Basis einer partiellen Quelle analysiert. Der Reviewer identifiziert dies korrekt als Risikofaktor. Da keine sofortige Beschaffung einer vollständigen Quelle ohne Herausgeber-Aktion möglich ist, wird dies als Scientific Debt dokumentiert — nicht als Sperrung bestehender Objekte.

**Betroffene Repository-Objekte:**
- `00_project/SCIENTIFIC_DEBT.md`
- `02_sources/books/SRC-0005_gap_selling.md`

---

## Übernommene Änderungen

| # | Empfehlung | Entscheidung | Betroffene Objekte | Status |
|---|---|---|---|---|
| 1 | MEC-0011 E-Level | Teilweise übernehmen | MEC-0011, SCIENTIFIC_DEBT | Umsetzung |
| 2 | MEC-0012 MacLean-Entfernung | Übernehmen | MEC-0012 | Umsetzung |
| 3 | Proprietäre Studien | Teilweise übernehmen | SCIENTIFIC_DEBT | Umsetzung |
| 5 | Meta-Prinzipien | Bestätigung | keine | Abgeschlossen |
| 6 | JOLT Effect Priorisierung | Übernehmen | backlog.md | Umsetzung |
| A | MEC-0010 E-Level | Übernehmen | MEC-0010 | Umsetzung |
| B | B-0005 Vollständigkeit | Übernehmen als SD | SCIENTIFIC_DEBT | Umsetzung |

---

## Bewusst nicht übernommene Empfehlungen

| # | Empfehlung | Entscheidung | Begründung |
|---|---|---|---|
| 4 | Fusion MEC-0006/MEC-0014 | Abgelehnt | Verschiedene kausale Pfade (CKM: X verschieden → getrennt). Herausgeber-Entscheidung nötig. |
| 7 | Meme-Filter | Nicht jetzt | Framework-Änderung → Operating Manual verbietet eigenständige Modifikation |

---

## Offene Forschungsfragen

Die folgenden Forschungsagenden entstehen aus dem Peer Review als neue oder bestätigte offene Fragen:

1. **F-003 — Unabhängige Replikation Challenger/CEB-Daten:** Verbeke, Dietz & Verwaal (2011) als Korrektiv prüfen. Existiert eine peer-reviewed Meta-Analyse, die CEB-Befunde (53% Loyalität durch Sales Experience, 5 Verkäufer-Profile) unabhängig bestätigt oder widerlegt?

2. **F-004 — Mirroring-Wirkungsnachweis:** Gibt es kontrollierte Studien zu verbalen Mirroring-Effekten in echten Verhandlungs- oder Verkaufssituationen (RCT oder Feldstudie)? Die Kellnerstudie (Trinkgeld-Effekt) ist nicht in SRC-0003 referenziert und muss separat geprüft werden.

3. **F-005 — B2B-spezifischer COI-Test:** Direkter empirischer Vergleich zwischen COI-First vs. Solution-First Gesprächsstruktur im B2B-Kontext (kein Laborexperiment, kein Practitioner-Claim).

4. **Literaturlücken (aus Review-Abschnitt 8):** Für Sprint 2+ zu integrieren:
   - Verbeke, W. et al. (2011): Meta-Analyse Vertriebsleistungstreiber (JAMS)
   - Johnston, W.J. & Lewin, J.E. (1996): B2B Buyer Behavior (JBR)
   - Kahneman, D. (2011): Thinking, Fast and Slow (als Direktquelle statt Sekundärzitat über Voss)

---

## Changelog

| Datum | Objekt | Änderungstyp | Beschreibung |
|---|---|---|---|
| 2026-07-01 | MEC-0011 | E-Level-Korrektur | E3 → E2 (gesamt), E1 für Spiegelneuronen-Basis |
| 2026-07-01 | MEC-0012 | Inhaltliche Bereinigung | MacLean-Terminologie aus Erklärungspfad entfernt |
| 2026-07-01 | MEC-0010 | E-Level-Korrektur | E3 → E2 (Lieberman-Laborstudie, kein B2B-Transfer) |
| 2026-07-01 | SCIENTIFIC_DEBT | Ergänzung | Neuer Abschnitt: Proprietäre Studien + B-0005 Vollständigkeit |
| 2026-07-01 | backlog.md | Priorisierung | B-0006 JOLT Effect als nächster Buchanalyse-Task |
| 2026-07-01 | review_queue.md | Fusion-Kandidat | MEC-0006/MEC-0014: Herausgeber-Entscheidung erforderlich |
| 2026-07-01 | OPEN_DECISIONS.md | Ergänzung | Meme-Filter als offene Herausgeber-Entscheidung |
