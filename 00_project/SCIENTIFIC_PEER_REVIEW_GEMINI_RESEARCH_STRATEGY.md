# Scientific Peer Review — Gemini Research Strategy

**Dokumentklasse:** Reference / Governance (Peer-Review-Bericht, kein Wissensobjekt, keine Framework-Datei)
**Rolle bei Erstellung:** Scientific Editorial Board (Claude), im Auftrag des Herausgebers — ausschließlich Begutachtung. Kein Autor, kein Research Director, kein Framework-Designer, kein Buchanalyst. Keine Herausgeberentscheidung.
**Datum:** 2026-07-05
**Gegenstand der Begutachtung:** „Wissenschaftlicher Strategiebericht zur Beseitigung der wissenschaftlichen Schuld und zur strategischen Weiterentwicklung des Sales Codex" (extern zugeliefert, Framing: Gemini Research Director; Datei: `Sales Codex Forschungsstrategie Review.md`)
**Grundlage:** Vollständige Lektüre des Gemini-Reports; `CURRENT_STATE.md`, `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, `00_project/KNOWLEDGE_ATLAS_GOVERNANCE.md`, `00_project/SCIENTIFIC_DEBT.md`, `00_project/OPEN_DECISIONS.md`, `00_project/NEXT_ACTION.md`, `05_research/LITERATURE_INDEX.md`, `04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md`, sowie stichprobenartige Direktprüfung der referenzierten Wissensobjekte (`MEC-0020`, `MEC-0021`, `MEC-0025`).
**Scope:** Ausschließlich Begutachtung der Verwertbarkeit des Gemini-Reports für den Sales Codex. Keine eigene Forschung, keine neuen Wissensobjekte, keine Framework-Änderung, keine Herausgeberentscheidung. Der Sales Codex wird nicht an den Gemini-Report angepasst — dieses Dokument entscheidet nur, welche seiner Empfehlungen einen tatsächlichen Mehrwert hätten.
**Wichtiger Kontext:** Sales Codex Version 1.0 ist veröffentlicht und gilt als unveränderlich (`CURRENT_STATE.md`, `NEXT_ACTION.md`). Version 1.1 wurde noch nicht formal eröffnet. Alle Roadmap-Empfehlungen dieses Reports sind daher als **Entscheidungsvorlage für ein künftiges Version-1.1-Programm** zu verstehen, nicht als sofort ausführbarer Sprintauftrag.
**Methodische Einschränkung:** Diese Begutachtung prüft die Vereinbarkeit des Gemini-Reports mit dem dokumentierten Repository-Zustand (Knowledge Atlas, Scientific Debt, Literature Index, Open Decisions) sowie die interne Plausibilität und Bekanntheit der zitierten Literatur nach bestem fachlichem Urteil. Es wurde in dieser Sitzung **keine eigene Websuche-Verifikation** einzelner externer Zitate durchgeführt (im Unterschied zum Standard der Academic-Recovery-Sprints, `ACADEMIC_RECOVERY_REPORT*.md`). Wo eine Quelle als "plausibel, aber nicht verifiziert" eingestuft wird, ist dies ausdrücklich vermerkt und keine Bestätigung ihrer Existenz oder Korrektheit.

---

## 1. Executive Summary

Der Gemini-Report enthält eine strategisch bedenkenswerte Grundthese (Kalibrierung und Operationalisierung vor weiterer Buchakquise) und eine Reihe akademisch legitimer Literaturhinweise. Er weist jedoch einen schwerwiegenden, bestätigten Sachfehler auf, der ausgerechnet seinen konkretesten und am stärksten mit dem Sales Codex verzahnten Abschnitt betrifft ("Underused Science"), sowie eine Executive-Summary-Diagnose ("Ratgeberliteratur ohne Peer-Review-Fundierung"), die dem tatsächlichen, bereits sehr umfangreichen akademischen Literaturbestand des Codex (`LITERATURE_INDEX.md`, >100 Einträge, davon zahlreiche E4/E5-Metaanalysen und Klassiker) klar widerspricht. Der Report liest sich streckenweise wie ein generischer, hochwertig formulierter Best-Practice-Text über B2B-Vertriebspsychologie, der erst nachträglich mit Sales-Codex-spezifischen Objekt-IDs versehen wurde — an mindestens einer Stelle nachweislich falsch.

**Gesamturteil:** Der Report ist **teilweise wissenschaftlich belastbar, teilweise strategisch hilfreich, in seinen codex-spezifischen Aussagen aber streckenweise spekulativ bis nachweislich falsch.** Er ist nicht als Ganzes verwertbar, liefert aber isoliert prüfbare, teils werthaltige Einzelbausteine (siehe Abschnitt 3, 6, 7).

Die wichtigste Einzelfeststellung dieser Begutachtung: Der Abschnitt „Underused Science" behauptet, die drei laut Knowledge-Atlas-Sprint-1 „unterausgeschöpften" Mechanismen MEC-0020, MEC-0021 und MEC-0025 zu erläutern — beschreibt dabei aber für alle drei Objekte einen **inhaltlich falschen Mechanismus**. Dies ist keine Interpretationsfrage, sondern gegen die tatsächlichen Repository-Dateien direkt verifizierbar (Abschnitt 5).

---

## 2. Scientific Assessment

**Wissenschaftliche Plausibilität der einzelnen Bausteine:** überwiegend hoch für die zitierten akademischen Kernkonzepte selbst (Trust-Formation-Forschung, Cognitive Load Theory, Elaboration Likelihood Model, Ultimatum-Spiel-Fairnessforschung, Reaktanztheorie, Self-Determination Theory sind sämtlich reale, etablierte Forschungslinien) — aber **niedrig bis nicht überprüfbar** für die Zuordnung dieser Konzepte zu konkreten Sales-Codex-Objekten. Der Report verwechselt an mehreren Stellen "diese akademische Theorie existiert und ist relevant für B2B-Vertrieb" (meist zutreffend) mit "diese Theorie füllt eine tatsächliche, noch unbesetzte Lücke im Sales Codex" (an mehreren Stellen nicht zutreffend, da der Codex die Lücke teilweise bereits besetzt oder bereits als offene Entscheidung dokumentiert hat, siehe Abschnitt 6).

**Vereinbarkeit mit dem bestehenden Sales Codex:** gemischt. Die Grundrichtung (Kalibrierung von Monokulturen, Operationalisierung evidenzstarker, aber schwach integrierter Mechanismen) deckt sich auffällig gut mit dem unabhängig erarbeiteten Befund aus `KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, Abschnitt 10 ("Underused Strengths"). Das ist ein echtes Konvergenzsignal — zwei unabhängige Analysen (interner Graph-Sprint, externes Gutachten) kommen strukturell zum selben Muster. Der Report verkennt jedoch, dass der Codex bereits ein aktives Instrumentarium für genau diese Fragen besitzt (`SCIENTIFIC_DEBT.md`, `OPEN_DECISIONS.md` OD-008, `research_agenda.md` F-001–F-012) und stellt mehrere seiner "neuen" Befunde als unentdeckt dar, obwohl sie bereits dokumentiert sind (Abschnitt 4, 6).

**Strategischer Mehrwert:** mittel. Die Kernbotschaft "keine weiteren Praktikerbücher, mehr akademische Kalibrierung" ist keine neue Erkenntnis für den Sales Codex — sie ist bereits die gelebte Praxis seit dem Academic Recovery Sprint (2026-07-01) und dem Behavioral Science Expansion Sprint (2026-07-02), siehe Abschnitt 8. Der Report liefert dazu aber eine nützliche Außenperspektive und einige konkrete, bislang nicht im Codex geführte Literaturkandidaten.

**Tatsächlicher Grenznutzen:** Nach Abzug der bereits bekannten Punkte, der hallucinierten Objektzuordnungen und der thematisch redundanten Empfehlungen verbleibt ein kleiner, aber nicht trivialer Kern an neuem, prüfenswertem Material — in erster Linie einzelne Literaturkandidaten (Abschnitt 7) und die Anregung, GAP-01 (Buying-Center-Gruppendynamik) und GAP-03 (Cognitive Load) als eigenständige künftige Themenblöcke zu benennen.

---

## 3. Valid Recommendations

**Empfehlung 1 — Kognitive Überlastung (Cognitive Load) als eigenständiger, aktuell fehlender Mechanismus (GAP-03)**
Kurzbeschreibung: Der Codex hat aktuell keinen MEC, der Arbeitsgedächtnis-Kapazitätsgrenzen bei komplexen Kaufentscheidungen (Choice Overload, Angebots-/Demo-Komplexität) direkt modelliert.
Begründung: Zutreffend — im vollständigen MEC-Bestand (29 Mechanismen laut Atlas-Sprint-1, Abschnitt 3.4) existiert kein "Cognitive Load"-MEC. Die bislang nächstliegenden Objekte (MEC-0015, T-0022 „6-Feature-Regel" aus Gap Selling) beruhen auf Miller's Law (1956), nicht auf moderner Cognitive-Load-Forschung (Sweller).
Erwarteter Mehrwert: Würde eine bestehende, bereits als Scientific-Debt-Punkt vermerkte Lücke (F-009 „6-Feature-Regel: Empirische Basis jenseits von Miller's Law", `research_agenda.md`) direkt adressieren.
Empfehlung: **übernehmen** — als Literaturkandidat für einen künftigen Recherche-/Buchanalyse-Baustein in einem Version-1.1-Programm, nicht als sofortige Maßnahme.

**Empfehlung 2 — Palmatier, Dant, Grewal & Evans (2006), Meta-Analyse zu Relationship Marketing**
Kurzbeschreibung: Reale, breit zitierte Meta-Analyse im *Journal of Marketing* zu Wirkfaktoren des Beziehungsvertriebs.
Begründung: Schließt eine Lücke, die der Codex selbst bereits als offen führt — OD-008 benennt „Trust Formation" (dort: Mayer, Davis & Schoorman 1995) explizit als zweithöchste Priorität unter den nicht angelegten Literaturkandidaten, `LITERATURE_INDEX.md` Zeile 104. Palmatier et al. wäre eine sinnvolle Ergänzung auf Meta-Analyse-Ebene zur selben Fragestellung.
Erwarteter Mehrwert: Hoch — Meta-Analysen sind laut eigenem methodischem Grundsatz des Codex (Evidenzsystem, Priorisierung E4/E5) werthaltiger als Einzelstudien.
Empfehlung: **übernehmen** — nach Standard-Websuche-Verifikation (Autor/Jahr/Journal/DOI) gemäß dem etablierten Verfahren aus `ACADEMIC_RECOVERY_REPORT*.md`, dann Aufnahme in `LITERATURE_INDEX.md` als Ergänzung zu OD-008, nicht als Ersatz.

**Empfehlung 3 — Sweller, Ayres & Kalyuga (2011), Cognitive Load Theory (Standardwerk)**
Kurzbeschreibung: Standardwerk der Cognitive-Load-Forschung.
Begründung: Direkt einschlägig für Empfehlung 1 (GAP-03). Realer, oft zitierter Titel aus dem Bildungsbereich; Transferleistung auf Vertriebspräsentationen/Angebotsgestaltung wäre eigenständige redaktionelle Arbeit, keine 1:1-Übernahme.
Erwarteter Mehrwert: Mittel-hoch, abhängig von der Qualität der Transferarbeit.
Empfehlung: **später prüfen** — sinnvoll erst, wenn GAP-03 als eigener Recherche-Baustein priorisiert wird (siehe Roadmap, Abschnitt 9).

**Empfehlung 4 — Petty & Cacioppo (1986), Elaboration Likelihood Model**
Kurzbeschreibung: Zentrales Dual-Route-Modell der Persuasionsforschung.
Begründung: Der Report nennt dieses Modell im Abschnitt „Recommended Sources" nicht explizit, wohl aber implizit über die Persuasions-/Kalibrierungslogik. Wichtiger: Das ELM ist bereits **unabhängig vom Gemini-Report** als höchste Priorität unter den nicht angelegten Literaturkandidaten in OD-008 dokumentiert (`OPEN_DECISIONS.md`, 2026-07-01) und in `LITERATURE_INDEX.md` (Zeile 103) mit dem Vermerk „Nicht angelegt — höchste Priorität unter den Literaturkandidaten" geführt.
Erwarteter Mehrwert: Hoch, aber **nicht dem Gemini-Report zuzuschreiben** — dieser bestätigt lediglich eine bereits getroffene, seit einem Jahr wartende Priorisierung.
Empfehlung: **übernehmen** — im Rahmen der bereits bestehenden OD-008, nicht als neue, durch diesen Report ausgelöste Maßnahme.

**Empfehlung 5 — Strategische Grundausrichtung „Kalibrierung vor Akquise"**
Kurzbeschreibung: Kein weiterer reiner Praktikerbuch-Import; stattdessen Gegenüberstellung bestehender Frameworks mit konkurrierenden Theorien und Operationalisierung bereits vorhandener, unterintegrierter Mechanismen.
Begründung: Deckt sich mit der bereits vollzogenen Kurskorrektur des Codex seit 2026-07-01 (Academic Recovery Sprint, Behavioral Science Expansion Sprint) sowie mit dem unabhängigen Befund aus Atlas-Sprint-1, Abschnitt 12 („Codex war mancherorts konservativer in der Prinzipien-Ableitung, als die zugrundeliegende Wissenschaft es erlauben würde").
Erwarteter Mehrwert: Bestätigend, nicht neu — aber als externe Zweitbestätigung eines bereits eingeschlagenen Weges wertvoll.
Empfehlung: **übernehmen** (als Bestätigung der bestehenden Strategie, nicht als neue Strategie).

---

## 4. Overstatements

**Overstatement 1 — Pauschale Abwertung der bestehenden Praktiker-Frameworks in der Executive Summary.** Die Aussage, der Codex bestehe „fast ausschließlich" aus Frameworks „kommerziell motivierter Ratgeberliteratur … deren empirische Validität im Peer-Review-Verfahren unbestätigt ist", ist nach Prüfung von `LITERATURE_INDEX.md` unzutreffend. Der Codex führt bereits über 100 verifizierte akademische Primärquellen und Meta-Analysen (u. a. Kahneman & Tversky 1979, Tversky & Kahneman 1974/1981, Brown et al. 2024, Schley & Weingarten 2023, Asch 1951/1956, Bond & Smith 1996, Festinger 1957, Brehm 1966, Galinsky et al. 2001/2008, Güth/Schmittberger/Schwarze 1982, Henrich et al. 2001/2004, Mertens et al. 2021, Maier et al. 2022) — durchgängig mit Evidenzlevel E4–E5 und dokumentiertem Verifikationsstatus. Die Coverage-Tabelle des Reports selbst widerspricht der Executive Summary bereits intern (Behavioral Economics und Entscheidungspsychologie werden dort korrekt als „wissenschaftlich stark" markiert). Die globale Eingangsdiagnose ist damit überzogen; zutreffend ist sie nur für die Domänen Vertriebsmethodik/Verhandlung/Buying-Center, nicht für den Gesamtcodex.

**Overstatement 2 — Pauschale Formulierung „Challenger Sale triggert bei hochkompetenten Einkäufern fast augenblicklich psychologische Reaktanz" (Theory-Competition-Tabelle).** Dies überzeichnet einen tatsächlich existierenden, aber bereits differenziert bearbeiteten Sachverhalt: Der Sales Codex hat den Konflikt zwischen Challenger-Konfrontation und reaktanzsensiblen Ansätzen bereits durch das Forschungsprojekt W-001 („Teach First vs. Diagnose First") systematisch geprüft und per Editor Decision (2026-07-03) als **kontextabhängig koexistierend**, nicht als universellen Gegensatz, aufgelöst (`06_research_program/completed/W001/06_EDITOR_DECISION.md`). Die Reaktanz-Kritik selbst ist wissenschaftlich legitim (MEC-0003 ist bereits im Codex verankert), aber die pauschale Formulierung „fast augenblicklich" ignoriert diese bereits vorliegende, differenziertere Repository-Position.

**Overstatement 3 — „Systematische Fundierung fehlt vollständig" bei mehreren Missing-Mechanism-Punkten.** Mehrere der zehn „fehlenden Mechanismen" sind im Codex nicht vollständig abwesend, sondern bereits mit angrenzender, teils identischer Literatur vertreten: Gross (1998) „Emotion Regulation" ist bereits als Quelle für MEC-0012 geführt (`LITERATURE_INDEX.md` Zeile 35); Dwyer, Schurr & Oh (1987), das vom Report als „Missing Mechanism 10" präsentierte Beziehungsphasenmodell, ist bereits **wörtlich identisch** als Quelle für MEC-0007 im Literature Index dokumentiert (Zeile 114). Der Report präsentiert hier eine bereits vorhandene Quelle als neue Lücke — ein Indiz dafür, dass der Bericht ohne aktuellen Abgleich mit `LITERATURE_INDEX.md` erstellt wurde.

**Overstatement 4 — Pseudo-mathematische Formalisierung von MEC-0020 („Cognitive Load"-Fehlzuschreibung, s. Abschnitt 5) mit eingebetteten Formelgrafiken.** Die Darstellung einer additiven Formel für „kognitive Belastung" mit Schwellenwertüberschreitung suggeriert einen Grad an quantitativer Validierung, den die zugrunde gelegte Literatur (Sweller) in dieser exakten Form nicht in einer einzigen, allgemein anerkannten Gleichung liefert. Dies ist keine Fälschung im engeren Sinn, aber eine über die tatsächliche Quellenlage hinausgehende Präzisionssuggestion — genau das Risiko, das der Codex mit seinem eigenen Prinzip „Keine unbelegte Verallgemeinerung" adressiert (vgl. bereits geführte Diskussion zu diesem Prinzip in OD-007).

---

## 5. Halluzinationen oder fragwürdige Quellen

**Befund 1 (schwerwiegend, verifiziert) — Falsche Objektzuordnung im Abschnitt „Underused Science".** Der Report behauptet, MEC-0020, MEC-0021 und MEC-0025 zu beschreiben — mit Verweis auf den Knowledge Atlas Sprint 1, der diese drei Objekt-IDs tatsächlich als "evidenzstark, aber strukturell unterintegriert" identifiziert hat (`KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, Abschnitt 10). Die inhaltliche Beschreibung ist jedoch für alle drei Objekte nachweislich falsch:

| Objekt-ID | Tatsächlicher Inhalt (verifiziert gegen Repository-Datei) | Vom Gemini-Report behaupteter Inhalt |
|---|---|---|
| MEC-0020 | Perspektivübernahme-Asymmetrie durch Macht (Galinsky) — Machtungleichgewicht verändert Fähigkeit/Bereitschaft zur Perspektivübernahme | „Cognitive Load & Information Overload in Multi-Attribute Decisions" |
| MEC-0021 | Anchoring-Mechanismus (Tversky/Kahneman-Tradition) | „Affective Forecasting & Anticipated Regret" |
| MEC-0025 | Altruistische Bestrafung / Fairness im Ultimatum-Spiel (Sanfey et al., Güth et al.) | „Psychological Reactance & Autonomy-Supportive Communication" |

Diese Verwechslung ist folgenreich, nicht kosmetisch: Reaktanz ist im Codex bereits als eigenständiges, gut dokumentiertes Objekt (MEC-0003) vorhanden — der Report beschreibt MEC-0025 im Wortlaut nahezu deckungsgleich mit MEC-0003, nicht mit dem tatsächlichen Ultimatum-Spiel-Fairnessmechanismus. Ebenso wird die für GAP-03 zentrale Behauptung „Kognitive Belastungstheorie … nur theoretisch erwähnt (MEC-0020)" hinfällig, da MEC-0020 nichts mit kognitiver Belastung zu tun hat — der eigentliche Befund (Cognitive Load ist im Codex tatsächlich nicht vertreten, siehe Abschnitt 3, Empfehlung 1) bleibt zwar korrekt, aber seine im Report gegebene Begründung ist falsch hergeleitet. Der gesamte Abschnitt „Underused Science" ist in seiner jetzigen Form **nicht verwertbar** und dürfte ohne inhaltliche Neuerstellung anhand der tatsächlichen Objektinhalte nicht übernommen werden.

**Befund 2 (schwerwiegend, verifiziert) — Referenzliste ohne erkennbaren inhaltlichen Bezug.** Die sechs Fußnoten am Ende des Reports verweisen nicht auf wissenschaftliche Quellen, sondern auf thematisch unpassende Treffer, die vermutlich aus einer Websuche nach dem Stichwort „Codex" stammen: eine Unternehmens-Verantwortungsseite einer Lebensmittelfirma („Diversa Spezialitäten GmbH"), eine Stellenanzeige für einen „Solutions Engineer" bei einem Unternehmen namens „Codex", ein Scribd-Dokument „Codex Sales Integration Strategy" ohne erkennbaren Fachbezug, sowie drei Treffer zum **OpenAI-Codex-Coding-Tool** (Composio-Blogartikel „Best Codex apps for founders", eesel-AI-Guide zu OpenAI Codex, ein GitHub-Repository „CodexKit"). Diese Fußnoten sind im Fließtext an inhaltlich unpassenden Stellen plaziert (u. a. an Aussagen zu McAllister 1995, Goal-Gradient-Effekt, Buyer-Seller-Relationship-Modellen) und liefern erkennbar **keine** Stützung für die dort getroffenen wissenschaftlichen Aussagen. Dies ist der klarste Beleg dafür, dass der Report zumindest teilautomatisiert mit einer generischen Web-Recherche zum Begriff „Codex" erstellt und die Fußnoten nachträglich mechanisch verteilt wurden, ohne inhaltliche Prüfung. **Empfehlung: Die gesamte Referenzliste ist zu verwerfen und darf nicht als Beleg in den Sales Codex übernommen werden.**

**Befund 3 (moderat, nicht verifiziert, aber prüfenswert) — „Autonomy in the Workplace" (Deci & Ryan, 2008).** Dieser exakte Buchtitel unter diesen Autoren konnte in dieser Begutachtung nicht mit Sicherheit bestätigt werden. Deci & Ryan haben umfangreich zu Self-Determination Theory am Arbeitsplatz publiziert (u. a. als Zeitschriftenartikel, z. B. Gagné & Deci 2005, sowie als Kapitel im *Handbook of Self-Determination Research*), aber ein monografisches Werk exakt dieses Titels und Jahres ist der Redaktion nicht bekannt. Empfehlung: vor Übernahme zwingend bibliografisch verifizieren (Standard-Websuche gemäß Academic-Recovery-Verfahren) — nicht ungeprüft in `LITERATURE_INDEX.md` aufnehmen.

**Befund 4 (gering, Kennzeichnungsfrage) — „Relational Capital Theory (Palmatier, 2006)" als benannte Theorie.** Palmatiers 2006-Arbeit ist eine reale Meta-Analyse (siehe Abschnitt 3, Empfehlung 2), aber „Relational Capital Theory" ist, soweit hier beurteilbar, keine von Palmatier selbst so benannte, etablierte Theorie-Bezeichnung, sondern eine im Report vereinfachend zugeschriebene Sammelbezeichnung. Dies ist keine Fälschung, aber eine ungenaue Etikettierung, die vor Übernahme präzisiert werden sollte (die zugrundeliegende Meta-Analyse selbst bleibt eine valide Empfehlung, siehe Abschnitt 3).

---

## 6. Research Gap Review

| Gap | Tatsächlich relevant? | Bereits (teilweise) abgedeckt? | Grenznutzen | Priorität (Editorial Board) |
|---|---|---|---|---|
| GAP-01 — Social Identity Theory & Group Dynamics im Buying Center | Ja — B2B-Kaufentscheidungen sind Gruppenentscheidungen; MEC-0006 (Social Proof/Konformität) deckt nur einen Teilaspekt ab | Teilweise — MEC-0006 (Asch, Sherif, Deutsch & Gerard) behandelt Konformität, nicht Gruppenidentität/Koalitionsbildung im engeren Sinn; „Extrem gering (< 5%)" im Report ist daher leicht überzeichnet, aber die Grundrichtung stimmt | Hoch — schließt eine echte strukturelle Lücke (Organisationspsychologie ist laut eigener Coverage-Tabelle des Reports korrekt als durchgängig schwach markiert) | **Hoch**, aber erst nach formaler Eröffnung eines Version-1.1-Programms |
| GAP-02 — Konversationsanalyse & Psycholinguistik | Bedingt — die Kritik an Voss-Anekdoten ist berechtigt (bereits in `SCIENTIFIC_DEBT.md` B-0003 mit „Hoch" geführt: Mirroring/Sprachstil-Matching, Ireland & Henderson 2014 bereits dokumentiert) | Teilweise bereits abgedeckt — MEC-0011 trägt bereits einen differenzierten Replikationsvorbehalt inkl. Sprachstil-Matching-Literatur | Mittel — der Report fügt hier keine neue Erkenntnis hinzu, die nicht schon in B-0003 dokumentiert ist | **Niedrig** (Doppelarbeit vermeiden) |
| GAP-03 — Cognitive Load & Metakognition | Ja — echte, nicht triviale Lücke (siehe Abschnitt 3) | Nein — im Bestand nicht vorhanden, nur benachbart über Miller's Law (T-0022) | Hoch | **Hoch**, aber Begründung im Report selbst fehlerhaft hergeleitet (Abschnitt 5, Befund 1) — bei Übernahme neu begründen |
| GAP-04 — Principal-Agent-Theorie & Mikropolitik | Ja — plausible, im Codex nicht vertretene Domäne | Nein, aber thematisch verwandt zu OD-008 (Trust Formation) und zur bereits dokumentierten CEB-Loyalitätsdiskussion (A-0019) | Mittel-hoch | **Mittel** |

**Zusammenfassung:** Zwei der vier Gaps (GAP-01, GAP-03) sind nach Prüfung tatsächlich echte, im Codex unbesetzte Lücken mit hohem Grenznutzen — unabhängig davon, dass GAP-03 im Report selbst fehlerhaft begründet ist. GAP-02 ist größtenteils bereits abgedeckt und bringt keinen neuen Erkenntnisgewinn. GAP-04 ist plausibel, aber diffuser und stärker redundant mit bereits laufenden Entscheidungssträngen (OD-008).

---

## 7. Literature Review

| Quelle | Typ | Liefert voraussichtlich neuen Erkenntnisgewinn? | Bewertung |
|---|---|---|---|
| Palmatier, Dant, Grewal & Evans (2006), Meta-Analyse | Meta-Analyse | Ja — quantifizierte Effektstärken zu Beziehungsvertrieb, direkt an OD-008 anschlussfähig | **Hoch** |
| Sweller, Ayres & Kalyuga (2011), Cognitive Load Theory | Standardwerk | Ja, sofern GAP-03 tatsächlich als Themenblock geöffnet wird | **Hoch, aber bedingt** (abhängig von Priorisierungsentscheidung) |
| Petty & Cacioppo (1986), Elaboration Likelihood Model | Theoriewerk | Ja — schließt bereits identifizierte Lücke (OD-008, höchste Priorität seit 2026-07-01) | **Hoch** (aber nicht dem Report zuzuschreiben, s. Abschnitt 3) |
| Miller & Rollnick (2012), Motivational Interviewing | Standardwerk (klinisch validiert) | Bedingt — Methode selbst exzellent belegt, aber B2B-Sales-Transfer ist eigenständige, unbewiesene Übersetzungsleistung; Risiko einer unkritischen Übernahme therapeutischer Begriffe (vom Report selbst benannt) | **Mittel** |
| Gigerenzer et al. (1999), Simple Heuristics That Make Us Smart | Theoriewerk | Ja — echtes akademisches Gegengewicht zur Heuristik-als-Bias-Perspektive; passt zur bereits im Codex dokumentierten Nudge/Boost-Kontroverse (SD-SYS-005) | **Mittel-hoch** |
| Malhotra & Bazerman (2007), Negotiation Genius | Praktiker-akademischer Grenzfall | Bedingt — akademisch fundierter als Voss, aber selbst ein kommerziell vertriebenes Praktikerbuch; steht in einem gewissen Spannungsverhältnis zur eigenen Kernthese des Reports gegen Praktikerliteratur | **Mittel**, Inkonsistenz im Report vermerken |
| Katz & Kahn (1978), The Social Psychology of Organizations | Klassiker | Ja, aber sehr allgemein und alt; hoher Transferaufwand | **Niedrig-mittel** |
| Cohen & Bradford (2005), Influence Without Authority | Praktikerwerk | Eher gering — ähnlich anekdotisch wie bereits vorhandene Praktikerquellen, die der Report selbst kritisiert | **Niedrig** |
| Deci & Ryan (2008), „Autonomy in the Workplace" | Unklar/nicht verifiziert | Nicht bewertbar vor Verifikation (Abschnitt 5, Befund 3) | **Zurückgestellt bis Verifikation** |
| Baron (2008), Thinking and Deciding | Standardwerk | Ja, als Nachschlagewerk, aber sehr voraussetzungsvoll — geringe unmittelbare Priorität | **Niedrig-mittel** |
| Sechs Fußnoten-„Referenzen" (Diversa GmbH, BeBee-Stellenanzeige, Scribd, Composio, eesel AI, CodexKit-GitHub) | Keine wissenschaftlichen Quellen | Nein | **Verwerfen** (Abschnitt 5, Befund 2) |

---

## 8. Strategic Alignment

Die zentrale Reportempfehlung — weniger neue Praktikerbücher, mehr wissenschaftliche Kalibrierung, mehr Operationalisierung — ist **im Grundsatz zutreffend, aber nicht neu**. Der aktuelle Repository-Zustand unterstützt diese Strategie bereits aktiv:

- Der Academic Recovery Sprint (ARS-0001, 2026-07-01) und der Behavioral Science Expansion Sprint (2026-07-02) haben bereits denselben Kurswechsel vollzogen: von reiner Buchakquise hin zu verifizierter akademischer Literaturintegration (`LITERATURE_INDEX.md` selbst ist das direkte Ergebnis dieses Kurswechsels).
- Der Knowledge Atlas Sprint 1 hat unabhängig dieselbe strukturelle Beobachtung gemacht wie der Gemini-Report (evidenzstarke, aber strukturell unterintegrierte Mechanismen) — nur mit korrekter Objektzuordnung.
- `NEXT_ACTION.md` zeigt, dass der Codex sich aktuell ohnehin in einer bewussten Konsolidierungsphase befindet (Version 1.0 eingefroren, Version 1.1 noch nicht eröffnet) — die im Report geforderte „radikale Kehrtwende" ist damit bereits im Gange, nicht ausstehend.

**Ein Vorbehalt gegen die Reportstrategie:** Der Report unterschätzt, dass ein Teil der von ihm kritisierten „Monokulturen" (SPIN, Challenger, Voss) bereits durch das Research Program (insbesondere W-001) kontextuell kalibriert wurde — nicht durch pauschale Zurückweisung, sondern durch dokumentierte Kontextspezialisierung. Die im Report implizit geforderte Form der Kalibrierung (Gegenüberstellung mit konkurrierenden Theorien wie Reaktanz- oder Integrativer Verhandlungstheorie) ist methodisch sinnvoll, aber sollte als **Fortsetzung**, nicht als Ersatz des W-001-Präzedenzfalls behandelt werden.

**Fazit:** Der aktuelle Repository-Zustand unterstützt die vorgeschlagene Strategie – sie beschreibt im Wesentlichen den bereits eingeschlagenen Weg zutreffend, auch wenn der Report selbst diese Kontinuität nicht erkennt und seine Diagnose (Abschnitt 4, Overstatement 1) teils veraltet oder zu pauschal ist.

---

## 9. Roadmap Recommendations

Ausdrücklicher Hinweis: Da Version 1.0 eingefroren ist und Version 1.1 noch nicht formal eröffnet wurde (`NEXT_ACTION.md`), sind alle folgenden Punkte **Entscheidungsvorlagen für die Eröffnung eines Version-1.1-Programms**, keine sofort ausführbaren Aufträge.

**Sofort** (keine Ressourcenbindung, reine Dokumentationspflege):
- Diesen Peer-Review-Bericht als Eingabe für die Herausgeber-Entscheidungsrunde zu OD-008 hinterlegen (Abschnitt 3, Empfehlungen 2 und 4 stützen die dortige Priorisierungsfrage direkt).
- Referenzliste des Gemini-Reports als nicht verwertbar kennzeichnen (Abschnitt 5, Befund 2) — keine Übernahme in `LITERATURE_INDEX.md` oder `review_queue.md`.

**Kurzfristig** (Teil eines künftigen Version-1.1-Programms, geringer Aufwand):
- Palmatier, Dant, Grewal & Evans (2006) und Petty & Cacioppo (1986) nach Standard-Websuche-Verifikation in `LITERATURE_INDEX.md` aufnehmen, verknüpft mit OD-008.
- „Autonomy in the Workplace" (Deci & Ryan, 2008) bibliografisch verifizieren, bevor über Aufnahme entschieden wird.

**Mittelfristig** (erfordert Herausgeber-Priorisierungsentscheidung, größerer Aufwand):
- GAP-03 (Cognitive Load) als eigenen Recherche- oder Buchanalyse-Baustein prüfen (Primärquelle: Sweller, Ayres & Kalyuga 2011), mit korrekter, neu formulierter Begründung statt der fehlerhaften MEC-0020-Herleitung des Gemini-Reports.
- GAP-01 (Social Identity Theory & Buying-Center-Gruppendynamik) als eigenständigen künftigen Themenblock prüfen — thematisch anschlussfähig an die bereits im Codex bestehende Cialdini/Challenger-Schnittstelle (Community 7 im Atlas-Sprint-1, „Unity/Credibility-Brücke").
- Den Abschnitt „Underused Science" **vollständig neu erstellen** — auf Basis der tatsächlichen Inhalte von MEC-0020, MEC-0021, MEC-0025 (Perspektivübernahme-Macht, Anchoring, Altruistische Bestrafung), nicht auf Basis der im Gemini-Report gegebenen (falschen) Beschreibungen. Dies deckt sich mit der bereits in `KNOWLEDGE_ATLAS_GOVERNANCE.md` Abschnitt 11 als „Synthesis Priority" (mittel) geführten Empfehlung Nr. 2.

**Beobachten** (kein aktueller Handlungsbedarf, aber im Blick behalten):
- GAP-02 (Konversationsanalyse/Psycholinguistik) — bereits größtenteils über B-0003/MEC-0011 abgedeckt, nur bei neuem Primärquellenzugriff erneut prüfen.
- GAP-04 (Principal-Agent-Theorie) — thematisch verwandt mit A-0019/OD-008, aber diffuser; erst nach GAP-01 priorisieren.
- Miller & Rollnick (2012) und Gigerenzer et al. (1999) als mögliche spätere Buchkandidaten, nachrangig zu den bereits in `research_agenda.md` (F-001–F-012) geführten Prioritäten.

---

## 10. Herausgeberempfehlung

**Empfehlung: Bericht teilweise übernehmen — nur einzelne, geprüfte Punkte, keine pauschale Adoption.**

Begründung: Der Report enthält einen bestätigten, nicht trivialen Sachfehler in seinem konkretesten Abschnitt (Underused Science, Abschnitt 5) sowie eine nicht verwertbare Referenzliste (Abschnitt 5), die beide gegen eine pauschale Übernahme sprechen. Gleichzeitig ist die strategische Grundrichtung zutreffend (wenn auch nicht neu, Abschnitt 8), und mehrere Einzelbausteine — insbesondere die Literaturkandidaten Palmatier et al. (2006) und die Bestätigung der bereits in OD-008 dokumentierten ELM-Priorität sowie die Identifikation von Cognitive Load als echter Lücke (GAP-03) — sind eigenständig prüfenswert und würden den Sales Codex tatsächlich verbessern.

Der Report sollte **nicht** als Ganzes in eine künftige Version-1.1-Planung übernommen werden. Er sollte auch nicht verworfen werden, da er trotz seiner Mängel echte, isoliert verwertbare Impulse liefert. Die sachgerechte Behandlung ist die in Abschnitt 9 vorgeschlagene selektive Übernahme einzelner Punkte über die bestehenden Kanäle (OD-008-Entscheidungsrunde, künftiges Version-1.1-Programm) — nicht über eine eigene, aus diesem Report abgeleitete Sonderinitiative.

---

*Dieses Dokument ist ein Begutachtungsbericht, kein Wissensobjekt und keine Framework-Datei. Es trifft keine Herausgeberentscheidung und verändert kein bestehendes Wissensobjekt. Es ersetzt nicht die in Abschnitt 9 empfohlene formale Herausgeber-Entscheidungsrunde zu OD-008 und einem künftigen Version-1.1-Programm.*
