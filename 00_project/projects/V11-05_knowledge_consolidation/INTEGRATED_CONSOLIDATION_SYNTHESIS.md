# V11-05 — Integrated Consolidation & Synthesis

Status: Completed — Audited — PASS WITH CONDITIONS — CONDITION CLOSED (2026-07-07; siehe `REWORK_REPORT.md`, `AUDIT_REPORT.md`, `RE_AUDIT_REPORT.md`)
Date: 2026-07-07 (ursprünglich); Rework: 2026-07-07; Focused Re-Audit Closure (C-01): 2026-07-07
Executor: Claude (Cowork-Session)

**Korrekturhinweis (Rework, Finding F-01/F-02/F-03):** Dieses Dokument wurde nach einem unabhängigen Audit (`AUDIT_REPORT.md`, Verdict REWORK REQUIRED) an drei Stellen korrigiert: (1) Abschnitt 2/3.2/5/6/7 — W-001 wurde ursprünglich fälschlich als zwischen SPR-0002/SPR-0003 „orphaned" und weiterhin ungelöst dargestellt; tatsächlich ist W-001 ein am 2026-07-03 abgeschlossenes, „teilweise angenommenes" Forschungsprojekt. (2) Abschnitt 3.3/4/5 — der Widerspruch „Pre-Suasion vs. FOMU" wurde fälschlich als W-006 geführt; W-006 ist historisch bereits für „Kognitive Leichtigkeit vs. Rational Drowning" vergeben (`SCIENTIFIC_DEBT.md`, 2026-07-01) — korrigiert auf W-007. (3) Abschnitt 4 — P-0040 wurde mit veraltetem Atlas-Status („0 MEC-Verbindungen, vollständig isoliert") beschrieben; das aktuelle Objekt trägt seit 2026-07-05 (W-003) eine explizite MEC-0030-Verlinkung. Details: `REWORK_REPORT.md`.

**Korrekturhinweis (Focused Re-Audit, Condition C-01, 2026-07-07):** Der Rework selbst hatte die residuale W-001-Frage OQ-2 an mehreren Stellen (Abschnitte 3.2, 5, 6, 7) fälschlich mit „Problemreife als Moderator" gleichgesetzt. Die kanonische OQ-2-Identität (`06_research_program/completed/W001/OPEN_QUESTIONS.md`) ist der Omission-Kipppunkt im Buying Center (Komplexitätsgrad/Produktspezifikationsmenge als Kipppunktfaktoren zwischen Verlustvermeidung und Entscheidungslähmung) — nicht Problemreife. Problemreife bleibt als Kontextfaktor des akzeptierten W-001-Kernbefunds bestehen, ist aber nicht mit OQ-2 identisch. Alle betroffenen Stellen wurden korrigiert. Details: `RE_AUDIT_REPORT.md`, `00_project/CLOSURE_REPORT_V11-05_2026-07-07.md`.

---

## 1. Zweck und Methodik

Dieses Dokument erfüllt die inhaltliche Mission von `V11-05 — Knowledge Consolidation & Integrated Synthesis` (`00_project/projects/V11-05_knowledge_consolidation/PROJECT_BRIEF.md`): Konsolidierung des bestehenden Wissensstands durch Auswertung — nicht Wiederholung — bereits vorhandener Analysen.

**Ausdrücklich keine Neurecherche.** Alle Befunde stammen aus drei bereits existierenden Quellen, gegeneinander und gegen den aktuellen Objektbestand direkt geprüft:

1. `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md` (Graph-/Evidenzanalyse, Abschnitte 3–13)
2. `04_synthesis/SPR-0001_Sales_Core_Synthesis/contradiction_matrix.md`, `04_synthesis/SPR-0002_Research_Synthesis/SPR-0002_SYNTHESEBERICHT.md`, `04_synthesis/SPR-0003_Behavioral_Science_Synthesis/SPR-0003_BEHAVIORAL_SCIENCE_SYNTHESIS.md`
3. `00_project/projects/V11-04_early_delivery_vertical_slice/COMPLETION_REPORT.md` und `AUDIT_REPORT.md` (Gap-Klassifikation, T12-Frage, MEC-0002/P-0002-Harmonisierung)

Wo eine Behauptung aus einer dieser Quellen durch direkte Prüfung des aktuellen Objektbestands bestätigt, präzisiert oder widerlegt wurde, ist dies explizit gekennzeichnet (Abschnitt 3).

---

## 2. Konsolidierungsziele — Herleitung (DoD 1)

Drei Zielkategorien, jede mit expliziter Quelle:

- **Delivery-getrieben** (aus V11-04): Technik-Ebene hinter Mechanismus-Ebene zurück (MEC-0002s drei NSTD-Kandidaten); Evidenzlevel-Uneinheitlichkeit zwischen verknüpften Objekten (MEC-0002/P-0002); T12/Status-„Validiert"-Governance-Frage.
- **Evidenzgetrieben/Atlas-getrieben** (aus Sprint-1-Report): Struktur×Evidenz-Diskrepanzen (MEC-0018-Familie); evidenzstarke, strukturell unterintegrierte Mechanismen (MEC-0020, MEC-0021, MEC-0025, MEC-0026–0029); 18 Reference Orphans, davon 4 mit plausibler, nicht umgesetzter Verlinkung.
- **Synthese-Prozess-getrieben** (aus Cross-Sprint- und Cross-Corpus-Vergleich, korrigiert im Rework): W-001 wurde als abgeschlossenes Research-Program-Ergebnis (Editor Decision 2026-07-03, „Teilweise annehmen") identifiziert, das in den ursprünglichen SPR-0001/0002/0003-Synthesen naturgemäß nicht erscheinen konnte, da es zeitlich nach beiden Sprints abgeschlossen wurde — aber bislang nie in die Widerspruchsmatrix zurückgeführt wurde. Zusätzlich: eine seit SPR-0001 nicht aktualisierte Widerspruchsmatrix trotz einer in SPR-0002 benannten neuen Spannung (jetzt korrekt als W-007 geführt, siehe Rework-Korrektur zu F-02).

---

## 3. Direkt verifizierte Befunde (nicht nur aus Atlas-Report übernommen)

### 3.1 MEC-0018-Abhängigkeitskette — präzisiert gegenüber dem Atlas-Sprint-1-Report

Der Atlas-Sprint-1-Report (Abschnitt 3.2) formulierte als offene Frage, ob P-0035, P-0036, P-0041 und MOD-0008 die Evidenzunsicherheit von MEC-0018 „strukturell erben", ohne dies "im Rahmen dieses Sprints inhaltlich geprüft" zu haben. Diese Prüfung wurde jetzt direkt an den vier Objekten durchgeführt:

| Objekt | Eigene Evidenzklassifikation | Abhängigkeit von MEC-0018s Risiko-Kernaussage (Bargh/Dijksterhuis-Priming) | Einordnung |
|---|---|---|---|
| P-0035 (Rahmen zuerst) | E3, mit explizitem Verweis auf MEC-0018s differenzierte E2–E4-Aufschlüsselung, **bereits korrigiert 2026-07-03** | Hoch — P-0035s Kernaussage baut direkt auf der zeitlichen Priming-Logik auf | Risiko korrekt geerbt UND bereits sichtbar dokumentiert. Kein Handlungsbedarf. |
| P-0036 (Aufmerksamkeit lenken) | E4, gestützt auf Agenda-Setting/Attribution/Spotlight-Forschung (eigene, andere Literaturlinie) | Niedrig — MEC-0018 nur als Cross-Link gelistet, nicht als tragende Evidenzquelle | Kein tatsächliches Erbschaftsrisiko. Der Atlas-Report-Verdacht bestätigt sich hier nicht. |
| P-0041 (System-1-kompatible Darstellung) | E4, gestützt auf Kahneman/Dual-Process (ST-0194/196/197) | Niedrig — MEC-0018 nur als sekundärer Cross-Link ("zeitliche Dimension") | Kein tatsächliches Erbschaftsrisiko. |
| MOD-0008 (Pre-Suasion-Modell) | E3, mit identischer Differenzierung wie P-0035, **bereits korrigiert 2026-07-03** | Hoch (ist der Modell-Wrapper von MEC-0018 selbst) | Risiko korrekt geerbt UND bereits sichtbar dokumentiert. Enthält zusätzlich einen eigenen Abschnitt „W-001-Status" (s. 3.2). Kein Handlungsbedarf. |

**Ergebnis:** Von den vier durch den Atlas-Report als potenziell betroffen benannten Objekten trägt nur eines (P-0035) plus der Modell-Wrapper (MOD-0008) tatsächlich eine inhaltliche Abhängigkeit von MEC-0018s Risiko-Kernaussage — und beide haben dieses Risiko bereits seit 2026-07-03 sichtbar dokumentiert, vor Erstellung des Atlas-Sprint-1-Reports. P-0036 und P-0041 sind unabhängig fundiert; der im Atlas-Report vermutete Vererbungseffekt besteht dort nicht. Die in Abschnitt 13 des Atlas-Reports empfohlene „Editorial Review Priority" (Sichtbarkeits-Prüfung) ist damit **bereits erledigt, nicht offen** — dies aktualisiert die Priorität #1 der dortigen Priority Map von „Hoch, ausstehend" auf „Geprüft, bereits erfüllt".

**Wichtiger methodischer Hinweis:** Dieser Befund vermischt nicht strukturelle Zentralität mit Evidenzstärke — er prüft im Gegenteil, ob eine rein graphbasierte Vermutung (strukturelle Nachbarschaft = Evidenz-Vererbung) bei Einzelprüfung der Objekttexte tatsächlich zutrifft. In zwei von vier Fällen tat sie das nicht.

### 3.2 W-001 — korrigiert im Rework: abgeschlossenes Research-Program-Ergebnis, nicht orphaned

**Diese Teilsektion wurde im Rework (2026-07-07, Finding F-01) vollständig korrigiert.** Die ursprüngliche Fassung behauptete, die W-001-Problemreife-Frage sei zwischen SPR-0002 (2026-07-01, „Offene Fragen für SPR-0003") und SPR-0003 (2026-07-02, anderer Themenfokus) „verloren gegangen" und der Kernwiderspruch bleibe unverändert ungelöst. Das war falsch.

**Tatsächlicher Sachverhalt:** W-001 wurde als dediziertes Forschungsprojekt im Research Program geführt (`06_research_program/completed/W001/`) und am **2026-07-03** — zeitlich NACH sowohl SPR-0002 (07-01) als auch SPR-0003 (07-02) — vollständig abgeschlossen. Beide Sprintberichte konnten das Ergebnis also gar nicht referenzieren; es handelt sich nicht um eine zwischen zwei thematisch divergierenden Sprints verlorene Frage, sondern um eine Frage, die anschließend über den vollen neunstufigen Research Lifecycle (Master Review, Red Team Review, Theory Landscape, Decision Brief, Editor Decision, Repository Integration, Health Check) bearbeitet wurde.

**Editor Decision (2026-07-03, `06_research_program/completed/W001/06_EDITOR_DECISION.md`): Teilweise annehmen.** Kernbefund: Diagnose- und Teaching-/Sensemaking-orientierte Vertriebsansätze stehen **nicht in einem universellen Widerspruch**; ihre relative Angemessenheit ist kontextabhängig (Problemreife, Kontext, Sensemaking-Bedarf, Buying-Center-Dynamik). Die mathematische SCSM-Formalisierung wurde **abgelehnt** (Red-Team-Kritik gefolgt: 11/13 Prüfkriterien nicht erfüllt). Sechs Objekte wurden kontextbezogen erweitert (A-0020, P-0021, P-0025, MEC-0013, T-0019, T-0023). Health Check bestanden; Projekt abgeschlossen.

**Residuale, tatsächlich offene Frage:** OQ-2 (`06_research_program/completed/W001/OPEN_QUESTIONS.md`) — die direkte empirische Quantifizierung des Kipppunkts, ab welchem Komplexitätsgrad (Anzahl Buying-Center-Mitglieder, Menge bereitgestellter Produktspezifikationen) sich die kognitive Dominanz von Verlustvermeidung zu Entscheidungslähmung (Omission Bias) verschiebt — wurde an `00_project/SCIENTIFIC_DEBT.md` übergeben und bleibt als eigenständige empirische Forschungsfrage offen. Dies ist NICHT gleichbedeutend mit einem weiterhin ungelösten Kernwiderspruch. **Korrektur (Focused Re-Audit, Condition C-01, 2026-07-07):** OQ-2 ist NICHT „Problemreife als Moderator" — Problemreife ist ein Kontextfaktor des akzeptierten W-001-Kernbefunds (siehe oben), nicht die Identität von OQ-2. Beide dürfen nicht gleichgesetzt werden.

Gleichzeitig dokumentiert `MOD-0008` bereits seit seiner Anlage (2026-07-01, vor SPR-0002) einen eigenen Abschnitt „W-001-Status", der Pre-Suasion als orthogonal zu W-001 einordnet — dieser Befund bleibt unverändert gültig und unabhängig von der obigen Korrektur.

**Konsolidierungsmaßnahme (durchgeführt, im Rework korrigiert):** `contradiction_matrix.md`-Nachtrag zu W-001 vollständig überarbeitet: Status jetzt korrekt als „COMPLETED / Teilweise angenommen / kontextuell integriert" geführt, mit klarer Trennung zwischen abgeschlossenem Kernkonflikt und residualer empirischer OQ-2-Frage. Kein neues W-Projekt gestartet; W-001 nicht wiedereröffnet; keine bereits getroffene Editor Decision reinterpretiert.

### 3.3 W-007 (vormals fälschlich W-006) — nie formal nachgetragene Spannung (Pre-Suasion vs. FOMU)

SPR-0002 benannte eine „neue Spannung" (MEC-0018 vs. MEC-0016/FOMU), trug sie aber nie als vollwertigen Eintrag in `contradiction_matrix.md` nach.

**Korrektur im Rework (Finding F-02):** Diese Spannung wurde ursprünglich fälschlich als „W-006" formalisiert. Eine Prüfung der Repository-Historie ergab: „W-006" ist bereits seit 2026-07-01 (Peer Review Sprint 2/ARS-0001, `SCIENTIFIC_DEBT.md`) für einen anderen Widerspruchskandidaten vergeben — „Kognitive Leichtigkeit vs. Rational Drowning" (MEC-0012 vs. MEC-0013). Per konservativer Identitätserhaltung bleibt diese frühere Zuordnung unverändert; die Pre-Suasion/FOMU-Spannung wurde auf die nächste freie ID, **W-007**, umbenannt. Kein bestehender historischer Eintrag wurde gelöscht oder umgedeutet.

**Konsolidierungsmaßnahme (durchgeführt, korrigiert):** Formal als W-007 nachgetragen, Inhalt unverändert aus SPR-0002 übernommen, keine neue Bewertung. Die W-006-Kandidatur „Kognitive Leichtigkeit vs. Rational Drowning" bleibt unverändert in `SCIENTIFIC_DEBT.md` geführt, ohne im Rahmen dieses Reworks zu einem vollwertigen Matrixeintrag ausgebaut zu werden (außerhalb des Rework-Scopes).

---

## 4. Under-Integrated High-Value Objects (DoD 2, aus Atlas-Report übernommen und priorisiert, nicht neu erhoben)

| Objekt(e) | Evidenzlevel | Strukturbefund | Einordnung für Backlog |
|---|---|---|---|
| MEC-0021 (Anchoring) | **E5** — höchste Evidenzklasse im Codex | Nur 4 P-/2 T-Verbindungen trotz Spitzenevidenz und Grad 28 | Synthesis Priority, Mittel — prüfen ob unentdeckte Anwendungsfelder jenseits Anker-/Verhandlungstechnik bestehen |
| MEC-0020 (Machtperspektive, Galinsky) | E4, peer-reviewed | 0 P-Verbindungen — einziger MEC im gesamten Bestand mit diesem Wert | Synthesis Priority, Mittel — Buying-Center-/Verhandlungskontext als mögliches P-Feld |
| MEC-0025 (Altruistische Bestrafung) | E4, Metaanalyse über 37 Studien | Nur 1 P-Verbindung | Synthesis Priority, Niedrig |
| MEC-0026–0029 (Made-to-Stick-Familie) | E3–E4 | Durchgängig niedrige P-/T-Anbindung | **Kein Handlungsbedarf jetzt** — Atlas-Report identifiziert dies korrekt als wahrscheinlichen Recency-Effekt (B-0015 zuletzt integriert); Empfehlung: bei nächstem Atlas-Lauf erneut prüfen, nicht jetzt forcieren |
| P-0039 (Buoyancy) | E4 | 0 MEC-Verbindungen, weiterhin bestätigt (aktueller Objektstand direkt geprüft im Rework, Finding F-03: kein W-003- oder anderer Erweiterungsabschnitt vorhanden) | Synthesis Priority, Niedrig-Mittel — bleibt eigenständiger Kandidat für „Resilienz/Motivation als eigene Kategorie" |
| P-0040 (Purposeful Serving) | E4 | **Korrigiert im Rework (Finding F-03):** NICHT mehr 0 MEC-Verbindungen / nicht mehr vollständig isoliert. Das aktuelle Objekt trägt seit 2026-07-05 (W-003 Trust Formation Research Project) einen expliziten Erweiterungsabschnitt „Rückverweis zu MEC-0030" mit mehrfacher expliziter MEC-0030-ID-Nennung. Der ältere Atlas-Sprint-1-Befund (0 MEC/isoliert) ist damit veraltet. Kein Atlas-Compiler-Lauf allein wegen dieser redaktionellen Korrektur erzwungen. | Kein Synthesis-Priority-Handlungsbedarf mehr aus dieser Quelle — P-0040 ist über MEC-0030 bereits inhaltlich angebunden (siehe Abgrenzungstabelle in MEC-0030 selbst) |

**Getrennte Bewertung (Rework, Finding F-03):** Die ursprüngliche gemeinsame Formulierung „P-0039 und P-0040: 0 MEC-Verbindungen, mögliche eigenständige Kategorie Resilienz/Motivation" ist nach Einzelprüfung nicht mehr für beide Objekte gemeinsam haltbar. P-0039 bleibt tatsächlich MEC-isoliert und ein valider Synthesis-Priority-Kandidat. P-0040 ist über die W-003-Erweiterung bereits mit MEC-0030 (Trust Formation) verknüpft und damit kein Isolationsfall mehr — die „eigenständige Kategorie"-Hypothese wird für P-0040 nicht mehr aufrechterhalten, bleibt aber für P-0039 allein weiterhin plausibel und ungeprüft.
| ST-0068, ST-0084, ST-0152, ST-0171 (Reference Orphans mit plausibler Verlinkung) | E2–E3 | Orphan trotz inhaltlicher Anschlussfähigkeit (u. a. ST-0171 mit im Fließtext dokumentiertem, aber nicht ID-referenziertem Cross-Book-Bezug) | Graph Modeling Review, Niedrig — Herausgeberentscheidung, nicht automatisch umzusetzen |
| ST-0084 + ST-0228 (Deadline-Thema, zwei Bücher) | E2–E3 | Zwei Orphans über Voss/Ariely hinweg thematisch verwandt, nirgends zusammengeführt | Synthesis Priority, Niedrig — mögliches gemeinsames Deadline-/Tempo-Prinzip |
| MOD-0002 Terminologie-Präzision | — | „Cross-Domain"-Zuschreibung vermischt strukturelle Brückenfunktion mit Quellenvielfalt (2 von 3 SRC vom selben Autor) | Editorial Review, Niedrig — Formulierung in künftigen Berichten präzisieren |
| MEC-0002 — drei NSTD-Technik-Kandidaten (Anchoring, Negative Leverage, Ackerman-Modell) | — (aus V11-04) | Mechanismus-Ebene voraus, Technik-Ebene hinterher | Research/Synthesis Priority, Mittel — Kandidaten sind im MEC-0002-Objekt selbst bereits benannt und begründet |

**Bewusst nicht in dieser Tabelle:** MOD-0005/MOD-0010-Senken-Asymmetrie und Community-9-Isolation (Ariely-Dishonesty-Cluster) — beide bereits im Atlas-Report als „No Action, bereits anderweitig dokumentiert" korrekt disponiert; keine erneute Aufnahme ohne neuen Befund.

---

## 5. Widersprüche und ungelöste Transferprobleme — sichtbar gehalten, nicht geglättet (DoD 3)

| Punkt | Status | Wo dokumentiert |
|---|---|---|
| W-001 (Teach First vs. Diagnose First) | **Korrigiert im Rework, OQ-2-Identität präzisiert im Re-Audit (Condition C-01):** COMPLETED / Teilweise angenommen / kontextuell integriert (Editor Decision 2026-07-03). Kernkonflikt nicht mehr als universeller Widerspruch geführt. Residuale, tatsächlich offene Frage: OQ-2 — Omission-Kipppunkt im Buying Center (Komplexitätsgrad/Produktspezifikationsmenge), NICHT Problemreife | `contradiction_matrix.md`, Nachtrag (korrigiert); `06_research_program/completed/W001/`; `00_project/SCIENTIFIC_DEBT.md` |
| W-002 (Liking in B2B) | Teilaufgelöst, kein Schwellenwert bekannt | `contradiction_matrix.md` (unverändert) |
| W-006 (Kognitive Leichtigkeit vs. Rational Drowning) | Bestehender Kandidat seit 2026-07-01, unverändert — **nicht** Gegenstand dieses V11-05-Projekts | `00_project/SCIENTIFIC_DEBT.md` |
| W-007 (Pre-Suasion vs. FOMU, vormals fälschlich W-006) | Kontextgebunden, nicht abschließend geprüft | `contradiction_matrix.md`, neu formal nachgetragen, ID korrigiert im Rework |
| MEC-0002/P-0002 Evidenzlevel-Uneinheitlichkeit | Registriert, nicht aufgelöst (aus V11-04) | `00_project/SCIENTIFIC_DEBT.md` |
| MEC-0018-Familie Evidenzrisiko | Bereits korrekt dokumentiert und sichtbar (präzisiert in Abschnitt 3.1 dieses Berichts) | MEC-0018, P-0035, MOD-0008 direkt; `SCIENTIFIC_DEBT.md` B-0010 |
| B2B-/Buying-Center-Transferlücke (ELM, Trust Formation, Buying Center) | Bereits mehrfach dokumentiert (W-002/W-003/W-004 Forschungsprojekte, V11-02 Evidence-Backlog) | `SCIENTIFIC_DEBT.md` — **hier bewusst nicht erneut aufgerollt**, da V11-05 dies nicht wiederholen soll |
| T12/Status „Validiert" Governance-Frage | Deferred Governance Clarification (aus V11-04-Audit) | `00_project/NEXT_ACTION.md`, `ROADMAP_V1_1.md` |

---

## 6. Trennung Research- / Maintenance- / Governance- / Delivery-Folgebedarfe (DoD 4)

| Kategorie | Punkte |
|---|---|
| **Research** (neue W-Projekte — nicht in V11-05 gestartet) | **Korrigiert im Rework, OQ-2-Identität präzisiert im Re-Audit:** Nicht mehr „W-001 empirisch prüfen" (W-001 ist abgeschlossen) — stattdessen die engere residuale Frage OQ-2 (kanonisch: Omission-Kipppunkt im Buying Center, operationalisiert über Anzahl Buying-Center-Mitglieder und Produktspezifikationsmenge; NICHT Problemreife; bereits an `SCIENTIFIC_DEBT.md` übergeben); B2B-Transfer für MEC-0020/Machtperspektive in Buying-Center-Kontexten (nur als Kandidat, keine Aktivierung) |
| **Maintenance/Scientific Debt** | MEC-0002/P-0002-Harmonisierung (bereits registriert, V11-04); MOD-0002-Terminologiepräzisierung |
| **Governance** | T12/Status-„Validiert"-Grundsatzfrage (deferred, Felix vorbehalten) |
| **Delivery** (informiert künftige V11-04-artige Slices, nicht in V11-05 ausgeführt) | Technik-Lücke MEC-0002 (3 NSTD-Kandidaten) als nächster sinnvoller Kandidat für eine künftige T-Objekt-Anlage, sofern Editor freigibt |
| **Graph Modeling Review** (rein strukturell, keine inhaltliche Aussage) | 4 Orphan-STs mit plausibler Verlinkung; Deadline-Thema (ST-0084/ST-0228) |
| **Kein Handlungsbedarf jetzt** | MEC-0026–0029 (Recency-Effekt, bei nächstem Atlas-Lauf erneut prüfen); MOD-0005/MOD-0010-Senken; Community-9-Isolation |

---

## 7. Prioritized Consolidation Backlog (DoD 5)

| # | Punkt | Typ | Priorität | Nächster Schritt |
|---|---|---|---|---|
| 1 | T12/Status-„Validiert"-Grundsatzfrage entscheiden | Governance | Hoch | Editor-Entscheidung (Reserved Decision — nicht durch V11-05 selbst getroffen) |
| 2 | MEC-0002/P-0002-Evidenzlevel-Harmonisierung umsetzen | Maintenance/Scientific Debt | Mittel | T3_WARTUNG/T11_SCIDEBT-Folgeauftrag (bereits vorgemerkt) |
| 3 | MEC-0002s drei NSTD-Technik-Kandidaten prüfen (Anchoring, Negative Leverage, Ackerman-Modell) | Synthesis/Research | Mittel | Canonicalization-Prüfung gegen bestehende T-Objekte, sofern Editor freigibt |
| 4 | **Korrigiert im Rework, OQ-2-Identität präzisiert im Re-Audit (Condition C-01):** Nicht „W-001 erneut lösen" (W-001 ist COMPLETED, Editor Decision 2026-07-03) — sondern: residuale empirische Frage OQ-2 (kanonisch: Omission-Kipppunkt im Buying Center — Komplexitätsgrad/Produktspezifikationsmenge als Kipppunktfaktoren zwischen Verlustvermeidung und Entscheidungslähmung; NICHT Problemreife) eigenständig prüfen | Research | Niedrig-Mittel (bereits als Scientific-Debt-Punkt übergeben, keine Dringlichkeitseskalation) | Künftiges, eigenständiges W-Projekt zu OQ-2, kein automatischer Start; W-001 selbst bleibt geschlossen und wird nicht wiedereröffnet |
| 5 | MEC-0021 (Anchoring, E5) und MEC-0020 (Machtperspektive, E4) auf zusätzliche P-Ableitungen prüfen | Synthesis | Mittel-Niedrig | Inhaltliche Prüfung, ob neue P-Objekte sachlich gerechtfertigt sind — kein automatisches Anlegen |
| 6 | Deadline-/Tempo-Thema (ST-0084, ST-0228) als mögliches gemeinsames Prinzip prüfen | Synthesis | Niedrig | Inhaltliche Prüfung bei künftigem Synthese-Sprint |
| 7 | 4 Orphan-STs mit plausibler Verlinkung (ST-0068, ST-0084, ST-0152, ST-0171) | Graph Modeling Review | Niedrig | Herausgeberentscheidung, ob ID-Referenzen nachträglich ergänzt werden |
| 8 | MOD-0002 „Cross-Domain"-Terminologie präzisieren | Editorial | Niedrig | Sprachliche Präzisierung in künftigen Berichten, kein Objekt-Edit nötig |
| 9 | MEC-0026–0029 erneut nach nächstem Atlas-Lauf prüfen (Recency-Effekt-Hypothese testen) | Beobachtung | Niedrig | Kein Auftrag jetzt — Wiedervorlage |

**Nicht in den Backlog aufgenommen (bereits erledigt oder korrekt disponiert):** MEC-0018-Sichtbarkeitsfrage (siehe Abschnitt 3.1 — bereits erfüllt); MOD-0005/MOD-0010-Senken; Community-9-Isolation; B2B-Transferlücke allgemein (bereits in `SCIENTIFIC_DEBT.md` geführt).

---

## 8. Was V11-05 bewusst NICHT getan hat

- Keine breite mechanische Wissensobjekt-Überarbeitung.
- Kein CTX-Backfill der 18 Reference Orphans.
- Kein neues Forschungsprojekt aktiviert.
- Keine Evidence Levels eigenständig erhöht oder gesenkt (auch nicht für MEC-0002/P-0002, trotz Klärungsbedarf).
- Keine Open Decision inhaltlich verändert oder geschlossen.
- T12 nicht aktiviert, `TASK_TYPES.md` nicht verändert.
- V11-04 nicht wiederholt (Traceability Check, Gap-Klassifikation, Delivery-Artefakte unverändert übernommen als Input, nicht neu erstellt).

**Rework-Ergänzung (2026-07-07, siehe `REWORK_REPORT.md` für Details):**

- W-001 nicht wiedereröffnet, keine bestehende Editor Decision reinterpretiert oder erweitert.
- Kein neues W-Projekt für OQ-2 automatisch gestartet.
- Kein Wissensobjekt verändert (P-0040-Korrektur ist eine redaktionelle State-Korrektur an diesem Dokument, kein Edit an `P-0040_purposeful_serving.md` selbst).
- Kein Atlas-Compiler-Lauf erzwungen.
- W-006-Kandidat „Kognitive Leichtigkeit vs. Rational Drowning" nicht zu einem vollwertigen Matrixeintrag ausgebaut (außerhalb des Rework-Scopes).
- Engen Relevanzscan W-001–W-004 durchgeführt (siehe `REWORK_REPORT.md`, Abschnitt 3) — keine Master-Review-Wiederholung, keine neue Theory Competition, keine neue Literaturrecherche.

**Focused-Re-Audit-Ergänzung (2026-07-07, Condition C-01, siehe `RE_AUDIT_REPORT.md` und `00_project/CLOSURE_REPORT_V11-05_2026-07-07.md`):**

- Nur die OQ-2-Identitätsbezeichnung korrigiert, kein neuer Rework-Zyklus, kein neues Audit durchgeführt.
- W-001-Projektakten (`06_research_program/completed/W001/`) nicht verändert.
- Kein Wissensobjekt verändert.
- W-006/W-007 und P-0039/P-0040 nicht erneut bearbeitet (außerhalb des C-01-Scopes).
- MEC-0018 nicht erneut analysiert.
