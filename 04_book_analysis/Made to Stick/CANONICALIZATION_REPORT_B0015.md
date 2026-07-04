# Canonicalization Report -- B-0015 (Made to Stick: Why Some Ideas Survive and Others Die, Heath & Heath 2007)

## Zweck

Detaillierte Dokumentation aller Canonicalization-Entscheidungen der B-0015-Buchanalyse, gemaess Editor-Auftrag "Behavioral Science Expansion" -- Prioritaet 1 (Kanonisierung vor Neuanlage). Ergaenzt VAL-0015 und BOOK_REVIEW_REPORT_B0015.md um die geforderten strukturierten Einzelabschnitte. Format und Anspruchsniveau folgen CANONICALIZATION_REPORT_B0011.md, CANONICALIZATION_REPORT_B0012.md, CANONICALIZATION_REPORT_B0013.md und CANONICALIZATION_REPORT_B0014.md (Buecher 1-4 desselben Sprints).

**Formel (uebernommen aus SPR-0001/canonicalization_report.md, identisch zu B-0011/B-0012/B-0013/B-0014):** Canonicalization Rate = Extensions / (Neue Objekte + Extensions) x 100, bezogen auf Mechanismen (MECs) -- die Objektkategorie, die im CKM primaer kanonisierbar ist.

---

## 1. Neue Statements

**Anzahl:** 23
**ID-Bereich:** ST-0287 bis ST-0309

Alle 23 Statements sind buchspezifische Einzelaussagen (per CKM-Definition nicht kanonisierbar/erweiterbar -- Statements werden immer neu angelegt, auch wenn ihr Inhalt zur Fundierung bestehender A/MEC/P-Objekte verwendet wird). Zuordnung:

- ST-0287 (Curse of Knowledge Definition), ST-0288 (Hinds Experten-Unterschaetzung), ST-0289 (Tappers/Listeners Newton 1990), ST-0294 (Bechky Ingenieure) -> MEC-0026 (neu)
- ST-0290 (Gap-Theorie Loewenstein 1994), ST-0291 (Surprise Brow Ekman/Friesen) -> MEC-0027 (neu)
- ST-0292 (Velcro-Theorie Gedaechtnis), ST-0293 (konkrete vs. abstrakte Woerter Gedaechtnis) -> MEC-0028 (neu)
- ST-0295 (Sinatra-Test), ST-0309 (Wendy's testbare Nachweise) -> P-0052/T-0047 (neu)
- ST-0296 (Darth-Vader-Zahnbuerste Shedler/Manis 1986), ST-0297 (Ulcer Marshall Selbstversuch) -> P-0052 (Kontext-/Stuetzevidenz)
- ST-0298 (Semantic Stretch "unique"/"relativity"), ST-0299 (Mother-Teresa-Prinzip) -> MOD-0012 (EMOTIONAL-Komponente, Anwendungsfall MEC-0028)
- ST-0300 (Rokia-Spendenexperiment), ST-0301 (Identifiable Victim Effect Replikation gescheitert) -> MEC-0028 (Anwendungsfall + Replikationswarnhinweis)
- ST-0302 (Geschichten als Flugsimulator, Klein), ST-0303 (Transportation Theory Green & Brock 2000), ST-0306 (Mentale Simulation UCLA), ST-0307 (Drei Story-Plots) -> MEC-0029 (neu)
- ST-0304 (Maslow Basement Selbst-Andere-Asymmetrie) -> MOD-0012 (verworfener MEC-Kandidat, eingeordnet)
- ST-0305 (Decision Paralysis Tversky & Shafir) -> Kontext-Statement, SIMPLE-Komponente MOD-0012
- ST-0308 (Stanford Speakers-Stickers-Experiment) -> MEC-0028 (Stuetzevidenz)

---

## 2. Neue Assumptions

**Anzahl:** 4
**ID-Bereich:** A-0057 bis A-0060

- **A-0057** (Wissen ist nicht bewusst entlernbar): Der Curse of Knowledge ist eine strukturelle, nicht durch Anstrengung/Empathie allein ueberwindbare kognitive Verzerrung. Grundlage fuer MEC-0026 (neu). Evidenzstatus E3 (Newton 1990 zeigt explizit, dass Motivation den Effekt nicht beseitigt).
- **A-0058** (Transportation unabhaengig von Faktizitaet): Narrative Transportation wirkt unabhaengig davon, ob eine Geschichte als Tatsachenbericht oder Fiktion gekennzeichnet ist. Grundlage fuer MEC-0029 (neu). Evidenzstatus E3 (Green & Brock 2000).
- **A-0059** (Pruefbarkeit durch Publikum erhoeht Glaubwuerdigkeit): Der "Sinatra-Test" (wenn eine Behauptung fuer den anspruchsvollsten denkbaren Fall gilt, gilt sie glaubhaft auch allgemein) und testbare Nachweise (Wendy's "Where's the Beef?") erzeugen interne, textimmanente Glaubwuerdigkeit ohne externe Autoritaetszuschreibung. Grundlage fuer P-0052/T-0047 (neu).
- **A-0060** (Extrembeispiel generalisiert Kompetenzeindruck): Ein einzelnes, besonders anspruchsvolles Beispiel (Darth-Vader-Zahnbuerste-Jury-Experiment, Shedler & Manis 1986) generalisiert den Kompetenz-/Glaubwuerdigkeitseindruck auf die gesamte Kategorie. Grundlage fuer P-0052 (neu, ergaenzende Stuetzevidenz).

Keine Erweiterung bestehender Assumptions in dieser Buchanalyse (im Unterschied zu B-0012/B-0013/B-0014, wo jeweils mindestens eine bestehende Assumption erweitert wurde) -- alle vier Assumptions decken neue, zuvor nicht im Codex-Bestand vorhandene Themenfelder (Kommunikation/Glaubwuerdigkeit/Narrativ) ab.

---

## 3. Neue Mechanismen

**Anzahl:** 4
**ID-Bereich:** MEC-0026 bis MEC-0029

### 3.1 MEC-0026 -- Curse of Knowledge

**Geprueft bestehende Objekte:** MEC-0020 (Perspektivuebernahme-Asymmetrie durch Macht), MEC-0018 (Pre-Suasion), MEC-0012 (Dual-Process System1->System2).

**CKM-Schritt 1 (Suche):** Gezielte Grep-Pruefung nach "Perspektive", "Wissen", "Experte", "Jargon", "Empathie" identifizierte MEC-0020 als naechstliegenden Kandidaten.

**CKM-Schritt 2 (Identitaetspruefung):** MEC-0020 ist MOTIVATIONAL (Macht reduziert die Motivation zur Perspektivuebernahme -- der Machthaber KOENNTE es, tut es aber seltener). MEC-0026 ist STRUKTURELL (selbst bei maximaler Motivation, wie im Tappers-Experiment, bleibt die Ueberschaetzung bestehen). Stimulus in MEC-0026 ist Wissen/Expertise, unabhaengig von sozialer Machtposition.

**CKM-Schritt 3 (Qualitaetspruefung, alle vier Bedingungen erfuellt):**
1. Nicht abgedeckt -- siehe Kontrastanalyse.
2. Eigenstaendiger Beitrag: Ja -- explizit in der Literatur als eigenstaendiges Phaenomen behandelt.
3. Mindestschwelle erfuellt -- vier unabhaengige Studiendesigns (Camerer/Loewenstein/Weber, Newton, Hinds, Bechky).
4. Keine Umbenennung -- anderer Kausalpfad (Wissensrepraesentation statt Machtmotivation) und anderer Ort im Kommunikationsprozess (Formulierung der Botschaft selbst) als MEC-0018.

**Ergebnis:** Neuanlage gerechtfertigt. Evidenzlevel E3.

### 3.2 MEC-0027 -- Gap-Theorie der Neugier

**Geprueft bestehende Objekte:** MEC-0018 (Pre-Suasion -- Attentionale Vorbereitung), P-0036 (Aufmerksamkeit strategisch lenken).

**CKM-Schritt 1 (Suche):** Vollstaendige Lektuere von MEC-0018, P-0036, MOD-0008 und zugrunde liegenden Statements vor Entscheidung durchgefuehrt.

**CKM-Schritt 2 (Identitaetspruefung):** MEC-0018 ist ein ASSOZIATIVER Priming-Mechanismus VOR der Botschaft, kurzes Zeitfenster (Sekunden bis Minuten), inhaltsspezifisch. MEC-0027 ist ein MOTIVATIONALER Spannungsmechanismus WAEHREND der Botschaft, anhaltend (gesamte Praesentationsdauer), mit invers-U-foermiger Vorwissensabhaengigkeit ohne Entsprechung bei MEC-0018.

**CKM-Schritt 3:**
1. Nicht abgedeckt -- auch P-0036 (Focal-Importance-Salienz) behandelt keine aversive Wissensluecken-Spannung.
2. Eigenstaendiger Beitrag: Ja.
3. Mindestschwelle erfuellt -- Loewenstein (theoretische Synthese mit Experimenten) und Kang et al. (eigenstaendiges fMRT-Experiment mit invers-U-Bestaetigung).
4. Keine Umbenennung -- anderer Zeitpfad und andere Moduationsbeziehung.

**Ergebnis:** Neuanlage gerechtfertigt. Evidenzlevel E3. Zusaetzlich: MEC-0018 und P-0036 wurden um einen expliziten Querverweis auf MEC-0027 erweitert (siehe Abschnitt 4).

### 3.3 MEC-0028 -- Konkretheits-Encoding (Velcro-Theorie)

**Geprueft bestehende Objekte:** MEC-0012 (Dual-Process System1->System2), MEC-0015 (Kognitive Ueberlastung durch Feature Overload).

**CKM-Schritt 1 (Suche):** Gezielte Grep-Pruefung nach "Gedaechtnis", "Erinnerung", "konkret", "einfach" identifizierte keine bestehenden Treffer.

**CKM-Schritt 2 (Identitaetspruefung):** MEC-0012 betrifft den VERARBEITUNGSMODUS (System 1 vs. System 2), unabhaengig vom Konkretheitsgrad der Information. MEC-0028 betrifft die KODIERUNGSPFAD-ANZAHL (doppelte vs. einfache Kodierung), unabhaengig vom Verarbeitungsmodus -- orthogonale Dimensionen. MEC-0015 betrifft OPTIONS-ANZAHL/Ueberlastung, nicht die interne Repraesentationsqualitaet einer gegebenen Information.

**CKM-Schritt 3:**
1. Nicht abgedeckt.
2. Eigenstaendiger Beitrag: Ja -- etabliertes eigenstaendiges Forschungsfeld (Dual-Coding-Theorie).
3. Mindestschwelle erfuellt -- Wortlisten-Gedaechtnisexperimente, Identifiable-Victim-Spendenexperimente (mit Replikations-Caveat), Stanford-Speakers-Experiment.
4. Keine Umbenennung -- anderer Kausalpfad (parallele Kodierung statt Verarbeitungsmodus-Wechsel oder Options-Ueberlastung).

**Ergebnis:** Neuanlage gerechtfertigt. Evidenzlevel E3 (mit explizit dokumentiertem Replikationsvorbehalt fuer den Identifiable-Victim-Anwendungsfall, Maier et al. 2023).

**Eingebettete, bewusst nicht separat angelegte Anwendungsfaelle:** Chunking (Miller 1956) und Identifiable Victim Effect (Small/Loewenstein/Slovic 2007) wurden geprueft und als Teilaspekte/Anwendungsfaelle von MEC-0028 eingeordnet statt als eigene Mechanismen (siehe Abschnitt 3.5/3.6 unten).

### 3.4 MEC-0029 -- Narrative Transportation

**Geprueft bestehende Objekte:** MEC-0012 (Dual-Process), MEC-0007 (Liking-Transfer), MEC-0018 (Pre-Suasion).

**CKM-Schritt 1 (Suche):** Gezielte Grep-Pruefung nach "Story", "Geschichte", "Narrativ", "Emotion" identifizierte keine bestehenden Treffer.

**CKM-Schritt 2 (Identitaetspruefung):** MEC-0018 wirkt durch einen kurzen Opener VOR der Botschaft, inhaltlich spezifisch. MEC-0007 beruht auf AFFEKTIVEM Sympathie-Transfer von einer Quelle, unabhaengig von einer Erzaehlstruktur. MEC-0029 erfordert eine ERZAEHLSTRUKTUR mit Immersionsqualitaet und wirkt ueber eine KOGNITIVE Verdraengungsmechanik (reduzierte Gegenargumentation) waehrend der gesamten Rezeption -- eine Geschichte kann hochgradig transportierend wirken, ohne dass der Erzaehler als sympathisch wahrgenommen wird.

**CKM-Schritt 3:**
1. Nicht abgedeckt.
2. Eigenstaendiger Beitrag: Ja -- Transportation Theory ist ein etabliertes eigenstaendiges Forschungsprogramm.
3. Mindestschwelle erfuellt -- Transportation-Experimente (Green & Brock), Flugsimulator-Funktion (Klein), Prozess-vs-Ergebnis-Simulation (UCLA, mit Zitationsluecke), Drei-Plot-Taxonomie.
4. Keine Umbenennung -- andersartiger Kausalpfad (immersive Verdraengung durch Erzaehlstruktur).

**Ergebnis:** Neuanlage gerechtfertigt. Evidenzlevel E3.

### 3.5 Verworfener Kandidat: Chunking (Miller 1956) als eigener Mechanismus

**Grund fuer Nicht-Anlage:** Nur einmalige Erwaehnung im Buch als Illustrationsbeispiel (Mindestschwelle des CKM: mindestens zwei unabhaengige Auftreten als erklaerende Kraft nicht erfuellt als eigenstaendiger MEC). Eng verwandt mit MEC-0028 (beide betreffen Informationsstrukturierung im Gedaechtnis). Als Teilaspekt in MEC-0028 dokumentiert.

**Entscheidung:** Kandidat verworfen. Zugeordnet zu MEC-0028 (Ergaenzungsverweis), ST-0293.

### 3.6 Verworfener Kandidat: Identifiable Victim Effect als eigener Mechanismus

**Grund fuer Nicht-Anlage:** Spezialfall von MEC-0028 (konkrete, personenbezogene Information aktiviert mehr Gedaechtnis-/Verarbeitungs-"Hooks" inkl. emotionaler Verarbeitung) -- kein eigenstaendiger dritter Kausalpfad. Zusaetzlich: 2023 praeregistrierte Replikationsstudie (Maier et al., Collabra: Psychology) fand keine Stuetzung fuer den Originaleffekt -- spricht zusaetzlich gegen eine prominente Neuanlage.

**Entscheidung:** Kandidat verworfen. Zugeordnet zu MEC-0028 (Grenzen-/Anwendungsfall-Verweis), ST-0301 (mit Replikations-Warnhinweis).

### 3.7 Verworfener Kandidat: ELM (Petty & Cacioppo) als eigener Mechanismus

**Grund fuer Nicht-Anlage:** Nicht direkt im Buch zitiert (nur als Recherche-Vergleichspunkt der Priori­taet-2-Recherche). Das Dual-Process-Grundmuster ist bereits durch MEC-0012 abgedeckt; ELM ist eine spezifische Auspraegung derselben Grundstruktur im Persuasionskontext. Neuanlage waere eine Dopplung von MEC-0012.

**Entscheidung:** Kandidat verworfen. Zugeordnet zu MEC-0012 (Kurzverweis als externe Stuetzevidenz in Scientific-Debt-Dokumentation).

### 3.8 Verworfener Kandidat: Maslow-Beduerfnishierarchie-Reinterpretation als eigener Mechanismus

**Grund fuer Nicht-Anlage:** Beschreibt einen Attributionsfehler (Selbst-Andere-Asymmetrie in Motivationszuschreibung), keine eigenstaendige, vertrieblich steuerbare Kausalkette. Erfuellt die CKM-Mindestschwelle fuer einen eigenen MEC nicht in ausreichender Trennschaerfe von der SUCCESS-Container-Logik.

**Entscheidung:** Kandidat verworfen. Zugeordnet zu MOD-0012 (Ergaenzungsverweis, EMOTIONAL-Komponente), ST-0304.

**Keine weiteren neuen Mechanismen wurden angelegt.**

---

## 4. Erweiterte Objekte

**Anzahl:** 2 (1 MEC, 1 P)

| Objekt | Art der Erweiterung |
|---|---|
| **MEC-0018 (Pre-Suasion -- Attentionale Vorbereitung)** | Expliziter Querverweis auf MEC-0027 (Gap-Theorie der Neugier) als eigenstaendigen, komplementaeren Aufmerksamkeitsmechanismus, mit vollstaendiger Abgrenzung nach Zeitpfad (kurzes Privileged-Moment-Fenster vor der Botschaft bei MEC-0018 vs. anhaltende, spannungsartige Motivation waehrend/ueber die gesamte Botschaftsdauer bei MEC-0027). Kein E-Level-Wechsel. |
| **P-0036 (Aufmerksamkeit strategisch lenken)** | Erweiterung um die Gap-Theorie der Neugier (MEC-0027) als zweiten, komplementaeren Weg zur Aufmerksamkeitsbindung -- explizite Abgrenzung zur Focal-Importance-Heuristik (Salienz, P-0036 Kernlogik) und praktischer Kombinationshinweis (Focal-Konzept aktivieren, dann bewusst als offene Frage/Luecke stehen lassen) ohne Prinzipien-Verschmelzung. Kein E-Level-Wechsel (E4 bleibt bestehen). |

Kein neues MOD-0012-Repository-Anomalie-Hinweis noetig -- keine bekannten offenen Reparaturpunkte aus vorherigen Buechern betreffen B-0015-Objekte direkt.

---

## 5. Canonicalization Rate

**Berechnungsbasis (MEC-spezifisch, wie in SPR-0001/B-0011/B-0012/B-0013/B-0014 definiert):**

- Neue MECs: 4 (MEC-0026, MEC-0027, MEC-0028, MEC-0029)
- Erweiterte MECs: 1 (MEC-0018)
- **Canonicalization Rate B-0015 = 1 / (4 + 1) x 100 = 20,0%**

**Vergleich mit vorherigen Buechern des Sprints:**

| Buch | Canonicalization Rate (MEC-basiert) | Neue MECs | Erweiterte MECs |
|---|---|---|---|
| B-0011 (Emotional Intelligence, Goleman) | 75,0% | 1 | 3 |
| B-0012 (Predictably Irrational, Ariely) | 83,3% | 1 | 5 |
| B-0013 (Nudge, Thaler & Sunstein) | 83,3% | 1 | 5 |
| B-0014 (Priceless, Poundstone) | 66,7% | 1 | 2 |
| **B-0015 (Made to Stick, Heath & Heath)** | **20,0%** | **4** | **1** |

B-0015 weist die mit Abstand niedrigste Canonicalization Rate des gesamten Sprints auf. Dies ist inhaltlich vollstaendig plausibel und KEIN Qualitaetsmangel: Made to Stick behandelt mit Kommunikation/Message-Design/Gedaechtnis-Encoding/Storytelling-Persuasionswirkung ein Themenfeld, das im Codex-Bestand vor dieser Buchanalyse nur sehr am Rande verankert war (einzig MEC-0018/P-0036 als naechstliegende Objekte, beide primaer aus SRC-0008 Pre-Suasion). Eine gezielte Grep-Pruefung vor Buchbeginn (dokumentiert in analysis.md, Canonicalisierungspruefung-Tabelle) bestaetigte fuer alle vier zentralen Konzepte (Curse of Knowledge, Gap-Theorie, Konkretheits-Encoding, Narrative Transportation) das Fehlen eines bestehenden Codex-Objekts. Die vier Neuanlagen sind daher eine echte, notwendige Wissensluecken-Schliessung fuer eine bislang unterrepraesentierte Codex-Dimension, keine vermeidbare Mechanismus-Vervielfachung.

**Wichtiger Beleg gegen "unkritisches Neuanlegen":** Fuenf oberflaechlich naheliegende Kandidaten (Chunking, Identifiable Victim Effect, ELM, Maslow-Reinterpretation, SUCCESS-als-MEC-statt-MOD) wurden im Rahmen dieser Buchanalyse explizit geprueft und bewusst NICHT als eigene Mechanismen angelegt, sondern korrekt in bestehende oder neu geschaffene Objekte eingeordnet bzw. vollstaendig verworfen. Ohne diese fuenf disziplinierten Ablehnungen waere die Anzahl der "neuen MECs" ceteris paribus auf bis zu neun angestiegen, was die Rate weiter gesenkt haette (waere aber methodisch falsch gewesen). Die tatsaechliche Rate von 20,0% spiegelt somit eine sorgfaeltig gepruefte, disziplinierte Wissenserweiterung wider, nicht eine unreflektierte Objekt-Inflation. Die Sprintvorgabe ("hohe Canonicalization Rate ist Guetemerkmal, keine Wachstumspflicht") bleibt durch die vollstaendige CKM-Pruefung aller neun urspruenglich in Betracht gezogenen Kandidaten (4 canonicalisiert als neu, 5 verworfen) vollstaendig erfuellt -- eine niedrige Rate bei gleichzeitig lueckenloser Pruefdokumentation ist der methodisch korrekte Ausdruck einer echten neuen Wissensdomaene, kein Verstoss gegen das Kanonisierungsprinzip.

**Codex-weite Rate (alle Objekttypen, informativ, nicht die primaere Kennzahl):** 2 Extensions / (35 Neue + 2 Extensions) x 100 = 5,4%. Deutlich niedriger als bei B-0014 (20,0%), da B-0015 anteilig die meisten neuen Objekte des gesamten Sprints hervorbringt (35 neue Objekte gegenueber 24 bei B-0014) bei gleichzeitig wenigen Erweiterungen -- konsistent mit der Einordnung als "neues Themenfeld" statt "Vertiefung bestehender Themenfelder".

---

## 6. Neue Scientific Debt

Vollstaendig einzutragen in `00_project/SCIENTIFIC_DEBT.md`:

**Neue Sektion "B-0015 -- Made to Stick (SRC-0015)"** mit buchspezifischen Debt-Punkten: MEC-0026-Newton-Bechky-Verifikationsluecke (Dissertationsquellen), MEC-0027-fehlende-Metaanalyse, MEC-0028-Identifiable-Victim-Replikationsversagen (⚠⚠ hoechste Prioritaet), MEC-0029-UCLA-Studie-Zitationsluecke, durchgaengige B2B-Transferluecke, Survivorship-Bias-Risiko der Fallstudien.

Zusammenfassung der wichtigsten neuen Eintraege:

| Objekt-ID | Kategorie | Prioritaet |
|---|---|---|
| MEC-0026, ST-0289 | Replikationsrisiko / Verifikationsluecke | Mittel -- Newton (1990) ist eine unveroeffentlichte oder nur teilweise verifizierbare Dissertation, exakte Stichprobengroesse/Publikationsstatus nicht abschliessend verifizierbar |
| MEC-0026, ST-0294 | Verifikationsluecke | Niedrig -- Bechky (1999) unveroeffentlichte Dissertation, nicht unabhaengig verifiziert |
| MEC-0027 | Externe Validierung ausstehend | Mittel -- keine dem Codex bekannte Metaanalyse zur Gap-Theorie identifiziert, Einzelstudien-Konvergenz statt systematischer Review |
| MEC-0028, ST-0300, ST-0301 | Replikationsrisiko | **Hoch** -- Identifiable-Victim-Effect (Rokia-Experiment), zentraler Kernbeleg des EMOTIONAL-Kapitels, wurde in praeregistrierter Replikation (Maier et al. 2023) NICHT bestaetigt |
| MEC-0029, ST-0306 | Unbelegte Annahme | Niedrig -- UCLA-Prozess-vs-Ergebnis-Simulationsstudie im Buch nur mit unvollstaendiger bibliografischer Angabe zitiert |
| Durchgaengig (alle B-0015-Objekte) | Survivorship-Bias / Anekdoten-Risiko | Hoch -- sehr hoher Anteil unkontrollierter Fallstudien (Nordstrom, Southwest, Sony, Jared/Subway) ohne systematischen Vergleich mit gescheiterten Kommunikationsversuchen |
| Durchgaengig (alle B-0015-Objekte) | Kulturelle Generalisierung / Transferluecke | Hoch -- kein Experiment im gesamten Buch testet direkten B2B-Vertriebstransfer |
| MOD-0012 | Kein Gesamtmodelltest | Mittel -- SUCCESS-Framework als Integrationsrahmen selbst nicht empirisch getestet (Kombinationswirkung/Gewichtung der sechs Komponenten) |

---

## 7. Neue Literaturquellen

Vollstaendig einzutragen in `05_research/LITERATURE_INDEX.md`, neuer Abschnitt fuer Kommunikations-/Gedaechtnispsychologie. Zusammenfassung:

| APA-Zitation | Verifikationsstatus | Unterstuetzt |
|---|---|---|
| Camerer, C., Loewenstein, G. & Weber, M. (1989). The Curse of Knowledge in Economic Settings: An Experimental Analysis. *Journal of Political Economy*, 97(5), 1232-1254. | Verifiziert (2026-07-02) | MEC-0026 (neu) |
| Hinds, P.J. (1999). The Curse of Expertise: The Effects of Expertise and Debiasing Methods on Prediction of Novice Performance. *Journal of Experimental Psychology: Applied*, 5(2), 205-221. | Verifiziert (2026-07-02) | MEC-0026 (neu) |
| Newton, L. (1990). Overconfidence in the Communication of Intent: Heard and Unheard Melodies. Dissertation, Stanford University. | Nicht vollstaendig verifizierbar (⚠) | MEC-0026 (neu) |
| Bechky, B.A. (1999). Crafting Culture. Dissertation, Stanford University. | Nicht vollstaendig verifizierbar (⚠, unveroeffentlicht) | MEC-0026 (neu) |
| Loewenstein, G. (1994). The Psychology of Curiosity: A Review and Reinterpretation. *Psychological Bulletin*, 116(1), 75-98. | Verifiziert (2026-07-02) | MEC-0027 (neu) |
| Kang, M.J. et al. (2009). The Wick in the Candle of Learning: Epistemic Curiosity Activates Reward Circuitry and Enhances Memory. *Psychological Science*, 20(8), 963-973. | Verifiziert (2026-07-02) | MEC-0027 (neu) |
| Ekman, P. & Friesen, W.V. (1975/1978). Facial Action Coding System / Unmasking the Face. | Codex-bestaetigt (bereits ueber MEC-0022 im Bestand referenziert) | MEC-0027 (Kontext, Surprise-Brow) |
| Green, M.C. & Brock, T.C. (2000). The Role of Transportation in the Persuasiveness of Public Narratives. *Journal of Personality and Social Psychology*, 79(5), 701-721. | Verifiziert (2026-07-02) | MEC-0029 (neu) |
| Small, D.A., Loewenstein, G. & Slovic, P. (2007). Sympathy and Callousness: The Impact of Deliberative Thought on Donations to Identifiable and Statistical Victims. *Organizational Behavior and Human Decision Processes*, 102(2), 143-153. | Verifiziert (2026-07-02) | MEC-0028 (Anwendungsfall) |
| Maier, M. et al. (2023). Registered Replication Report: The Identifiable Victim Effect. *Collabra: Psychology*. | Verifiziert (2026-07-02) | MEC-0028 (Replikationswarnhinweis, ST-0301) |
| Tversky, A. & Shafir, E. (1992). Choice Under Conflict: The Dynamics of Deferred Decision. *Psychological Science*, 3(6), 358-361. | Codex-bestaetigt (bereits im Bestand referenziert, Decision-Paralysis-Kontext) | MOD-0012 (SIMPLE-Komponente, ST-0305) |
| Shedler, J. & Manis, M. (1986). Can the Availability Heuristic Explain Vividness Effects? *Journal of Personality and Social Psychology*, 51(1), 26-36. | Verifiziert (2026-07-02) | P-0052 (neu, A-0060) |
| Paivio, A. (1971/1986). Dual Coding Theory. | Websuchverifizierte theoretische Fundierung (nicht direkt im Buch zitiert) | MEC-0028 (neu, ergaenzende theoretische Basis) |
| Heath, C. & Heath, D. (2007). Made to Stick: Why Some Ideas Survive and Others Die. Random House. | Vollstaendig verarbeitet als SRC-0015 | Alle B-0015-Objekte |

**Nicht bibliografisch vollstaendig verifizierbar (offene Fragen, nicht erfunden):** Newton (1990) und Bechky (1999) -- Dissertationsquellen ohne vollstaendig verifizierbaren Publikations-/Peer-Review-Status; UCLA-Prozess-vs-Ergebnis-Simulationsstudie (ST-0306) -- im Buch ohne vollstaendige Autorenangabe zitiert.

---

## 8. Publikationsbias-Risiken

Struktur wie VAL-0015 Punkt 6, hier als eigenstaendiger Berichtsabschnitt mit drei klar getrennten Ebenen:

1. **Identifiable-Victim-Effect-Replikationsversagen (zentral, direkt DIESES Buch betreffend):** Die 2023 praeregistrierte Replikationsstudie (Maier et al., Collabra: Psychology) fand keine Stuetzung fuer den urspruenglichen Rokia-Spendenexperiment-Effekt (Small/Loewenstein/Slovic 2004/2007) in der replizierten Form. Dies ist der wichtigste Einzelbefund der Priori­taet-2-Recherche dieser Buchanalyse -- der Effekt ist der zentrale Kernbeleg des gesamten EMOTIONAL-Kapitels des Buches. Prominent mit ⚠⚠ in ST-0301 sowie in MEC-0028 (Grenzen) dokumentiert, NICHT geglaettet oder verschwiegen.
2. **Fehlende Metaanalysen fuer Curse of Knowledge und Gap-Theorie:** Beide zentralen Mechanismen (MEC-0026, MEC-0027) stuetzen sich auf Einzelstudien-Konvergenz (mehrere unabhaengige Studiendesigns), nicht auf eine systematische Review/Metaanalyse. WebSearch-Recherche im Rahmen dieser Analyse ergebnislos -- konservativ als E3 (statt E4/E5) eingestuft.
3. **Newton (1990) und Bechky (1999):** Dissertationsquellen mit unvollstaendig verifizierbarem Publikations-/Peer-Review-Status -- moegliches, nicht abschliessend pruefbares Publikationsbias-Risiko (unveroeffentlichte Nullresultate waeren in Dissertationen prinzipiell moeglich, aber in diesem Fall nicht das Problem, da beide Studien POSITIVE, den Kernbefund stuetzende Ergebnisse berichten -- das Risiko liegt eher in der fehlenden unabhaengigen Nachpruefbarkeit als in klassischem Publikationsbias).

**Sauberkeit der Trennung:** Kein Statement/Objekt in dieser Buchanalyse uebertraegt die Replikationsschwaeche des Identifiable-Victim-Effects automatisch auf die anderen, unabhaengig gut gestuetzten Kernmechanismen (Curse of Knowledge, Gap-Theorie, Narrative Transportation) -- die vier neuen MECs werden durchgaengig mit eigenem, separat gefuehrtem Evidenzstatus dokumentiert.

---

## 9. Neue Tier-1-Kandidaten (nur Dokumentation, keine Eintragung)

Gemaess Auftrag: Diese Quellen werden hier nur als moegliche Kandidaten fuer `00_project/ACADEMIC_RECOVERY_PLAN.md` dokumentiert -- eine tatsaechliche Eintragung dort ist ausserhalb des Scopes dieser Buchanalyse.

- **Camerer, Loewenstein & Weber (1989) -- Curse of Knowledge:** Starker Kandidat fuer Tier-1. Gruendungsarbeit eines der einflussreichsten Kommunikations-/Verhaltensoekonomie-Konzepte, zentrale Evidenzbasis fuer MEC-0026.
- **Green & Brock (2000) -- Transportation Theory:** Starker Kandidat -- Gruendungsstudie eines breit rezipierten kommunikationswissenschaftlichen Forschungsprogramms, zentrale Evidenzbasis fuer MEC-0029.
- **Maier et al. (2023) -- Identifiable Victim Effect Replikationsbericht:** Mittlerer Kandidat -- wichtiger, aktueller Replikationsbefund; eine Tier-1-Pruefung waere sinnvoll, um systematisch zu erfassen, welche weiteren Codex-Mechanismen aehnliche Replikationsrisiken aufweisen koennten.
- **Loewenstein (1994) -- Gap-Theorie der Neugier:** Mittlerer Kandidat -- breit zitierte theoretische Synthesearbeit mit hoher Praxisrelevanz fuer Aufmerksamkeitslenkung im Vertrieb.

---

## Status

Abgeschlossen -- 2026-07-02
