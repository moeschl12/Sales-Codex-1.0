# SPR-0003 — Behavioral Science Expansion: Synthesebericht

**Dokumentklasse:** Synthesebericht
**Sprint-ID:** SPR-0003
**Sprint-Typ:** Wissenschaftlicher Vertiefungssprint ("Behavioral Science Expansion", kein Book Mode im synthetisierenden Teil — die fünf Einzelbuchanalysen selbst liefen im vollen Book Mode)
**Datum:** 2026-07-02
**Redakteur:** KI-Redaktion Sales Codex
**Status:** ABGESCHLOSSEN
**Phase:** Scientific Completion (Sales Codex 1.0 Program)

---

## Analysierte Wissensbasis

| Buch-ID | Titel | Autor(en) | Quelle | Buchanalyse |
|---|---|---|---|---|
| B-0011 | Emotional Intelligence | Daniel Goleman | SRC-0011 | `04_book_analysis/Emotional Intelligence/` |
| B-0012 | Predictably Irrational | Dan Ariely | SRC-0012 | `04_book_analysis/Predictably Irrational/` |
| B-0013 | Nudge: The Final Edition | Thaler & Sunstein | SRC-0013 | `04_book_analysis/Nudge/` |
| B-0014 | Priceless | William Poundstone | SRC-0014 | `04_book_analysis/Priceless/` |
| B-0015 | Made to Stick | Chip & Dan Heath | SRC-0015 | `04_book_analysis/Made to Stick/` |

**Codex-Stand bei SPR-0003-Beginn (nach SPR-0002, vor B-0011):** 21 Mechanismen (MEC-0001–MEC-0021), 10 Modelle, ~201 Statements, ~48 Annahmen, ~47 Prinzipien, ~41 Techniken, 10 Quellen (SRC-0001–SRC-0010).

**Codex-Stand nach SPR-0003 (nach B-0015):** 29 Mechanismen (MEC-0001–MEC-0029), 12 Modelle, 309 Statements, 60 Annahmen, 57 Prinzipien, 47 Techniken, 15 Quellen (SRC-0001–SRC-0015).

**Netto-Zuwachs durch diesen Sprint:** +8 Mechanismen, +2 Modelle, +108 Statements, +12 Annahmen, +10 Prinzipien, +6 Techniken, +5 Quellen.

---

## Zweck dieses Dokuments

Dieser Bericht fasst die fünf Einzel-Canonicalization-Reports (B-0011 bis B-0015) zu einer sprintweiten wissenschaftlichen Bilanz zusammen, wie im Auftrag "BEHAVIORAL SCIENCE EXPANSION – SPRINT 1" gefordert. Er beantwortet die neun mandatierten Fragen. Er erzeugt **keine neuen Wissensobjekte** und trifft **keine Governance-Entscheidungen** — er dokumentiert und bewertet, was in den fünf Buchanalysen bereits geschaffen wurde.

Alle Einzelangaben sind aus den bereits erstellten und verifizierten Dokumenten `CANONICALIZATION_REPORT_B0011.md` bis `CANONICALIZATION_REPORT_B0015.md`, den jeweiligen `BOOK_REVIEW_REPORT_*.md` sowie `00_project/SCIENTIFIC_DEBT.md` und `05_research/LITERATURE_INDEX.md` übernommen und nicht neu recherchiert. Wo eine Bewertung über die Einzelberichte hinausgeht (z. B. sprintweite Muster), ist dies als Synthese-eigene Einschätzung gekennzeichnet.

---

## 1. Gemeinsame wissenschaftliche Erkenntnisse

Über die fünf Bücher hinweg lassen sich vier wiederkehrende wissenschaftliche Muster identifizieren:

**Referenzpunkt-Abhängigkeit als Grundthema.** Vier der fünf Bücher (Predictably Irrational, Nudge, Priceless, und indirekt Emotional Intelligence über emotionale Zustände als Bewertungsfilter) bestätigen unabhängig voneinander, dass menschliche Bewertung fast nie absolut, sondern relativ zu einem Referenzpunkt erfolgt — sei dieser ein Anker (MEC-0021), ein Default (MEC-0002-Erweiterung), ein Kontraststimulus (MEC-0009) oder ein Fairness-Standard (MEC-0025, neu). Dies bestätigt und vertieft die bereits durch Kahneman (SRC-0010, SPR-0002) etablierte Prospect-Theory-Grundlage, statt sie infrage zu stellen — eine seltene, sprintübergreifende Konvergenz von vier unabhängigen Autorengruppen auf dasselbe Grundprinzip.

**Dual-Process-Logik bestätigt sich, mit Grenzen.** Predictably Irrational, Nudge und Priceless liefern alle zusätzliche empirische Stützung für automatische, schnelle Bewertungsprozesse (System-1-artig), die dem rationalen Kalkül vorausgehen oder es verzerren (Zero-Preis-Effekt, Default-Wirkung, Anchoring-Robustheit gegen kognitive Reflexion — Oechssler/Roider/Schmitz 2009). Gleichzeitig bestätigt B-0014 (Priceless), dass diese Automatismen NICHT durch höhere kognitive Fähigkeit vermeidbar sind — eine wichtige Präzisierung gegenüber einer vereinfachten "Dummheits"-Interpretation von System-1-Fehlern.

**Emotion als eigenständiger, nicht auf Kognition reduzierbarer Kanal.** Emotional Intelligence (Emotional Contagion, MEC-0022) und Priceless (Fairness-Verzicht, MEC-0025) liefern konvergent neuronale Evidenz (Facial Feedback bzw. Insula-Aktivierung) dafür, dass emotionale Reaktionen eigenständige kausale Pfade sind, die sich nicht vollständig auf Verlustaversion oder Kontrastwahrnehmung zurückführen lassen. Made to Stick ergänzt dies um die Rolle von Emotion in der Erinnerbarkeit von Botschaften (mit dem wichtigen Vorbehalt eines gescheiterten Replikationsversuchs beim zentralen Anwendungsbeispiel, siehe Abschnitt 7).

**Practitioner-Bücher als akademischer Grenzfall — durchgängig kritisch geprüft.** Alle fünf Bücher sind Practitioner-Synthesen mit unterschiedlich starkem akademischem Fundament (Ariely und Thaler/Sunstein selbst aktive Forscher mit eigenen Primärstudien; Poundstone und die Heath-Brüder sind Wissenschaftsjournalisten/Kommunikationsberater ohne eigene Primärforschung). Der Sprint hat durchgängig zwischen den beiden Quellentypen unterschieden und dies in der Evidenzlevel-Vergabe abgebildet (z. B. E3 für Theorie/Synthese vs. E4/E5 für die zugrundeliegenden Einzelstudien).

---

## 2. Welche bestehenden Mechanismen am stärksten gestärkt wurden

**MEC-0021 (Anchoring) — die klare Nummer 1 des Sprints.** Erweitert in B-0012 (Ariely: SSN-Auktion, Arbitrary Coherence), B-0013 (Nudge: Default-als-Anker, Reaktanz-Grenzbedingung bei Trinkgeld-Defaults) und B-0014 (Priceless: vollständige Primärquellen-Rekonstruktion des UN-Glücksrad-Experiments, Northcraft & Neale-Feldstudie, Jury-Anchoring ohne Boomerang-Effekt, Consider-the-Opposite-Antidot, Robustheit gegen kognitive Reflexion, Einordnung von Preference Reversal und Money Illusion als Unterfälle). Dreifache unabhängige Erweiterung in drei aufeinanderfolgenden Büchern desselben Sprints — MEC-0021 hat dadurch die dichteste Evidenzbasis aller Nicht-Prospect-Theory-Mechanismen im Codex erreicht, blieb aber bewusst auf E5 (kein künstlicher Aufwertungsschritt, da bereits vor dem Sprint auf höchstem Niveau).

**MEC-0002 (Verlustaversion/Status-quo-Kosten) — zweitstärkste Vertiefung.** Erweitert in B-0012 (Endowment-Effekt, Duke-Ticket-Studie) und B-0013 (vollständige Default-Effekt-Zerlegung: Madrian & Shea 2001, Johnson & Goldstein 2003, Thaler & Benartzi 2004), jeweils mit eigenständigen Gründungsquellen unabhängig von Kahneman/Tversky. Die B-0013-Erweiterung ist zugleich mit der wichtigsten neuen Einschränkung des Sprints verknüpft (SD-SYS-005-Publikationsbias-Kontroverse, siehe Abschnitt 7) — eine seltene Kombination aus Stärkung UND dokumentierter Vorsicht im selben Mechanismus.

**MEC-0009 (Perzeptueller Kontrast) — von Sekundärkonzept zu psychophysikalisch fundiertem Mechanismus.** B-0012 (Huber/Payne/Puto-Decoy-Effekt) und B-0014 (vollständige psychophysikalische Grundlegung: Weber's Law, Fechnersches Gesetz, Stevens' Machtgesetz, Helsons Adaptationsniveau-Theorie) schließen zusammen eine seit B-0002 offen dokumentierte Frage zur Anchoring-Verwandtschaft von MEC-0009.

**MEC-0018 (Pre-Suasion-Aufmerksamkeitsvorbereitung) — geringste, aber thematisch wichtigste Erweiterung.** Einzige Erweiterung durch B-0015 (Querverweis zur neuen Gap-Theorie der Neugier, MEC-0027), mit expliziter Abgrenzung als komplementärer, nicht identischer Mechanismus. Bedeutsam, weil MEC-0018 laut SPR-0002 "offene Fragen" (Priming-Replikationskrise, SD-B010-001) als eine der unsichersten Codex-Komponenten markiert war — der Sprint hat diese Unsicherheit nicht aufgelöst, aber die konzeptionelle Abgrenzung zu einem benachbarten neuen Mechanismus sauber dokumentiert.

**Sonstige einmalig erweiterte Mechanismen:** MEC-0005 (Marktnorm-Verdrängung, B-0012: Gneezy & Rustichini Kita-Bußgeld-Studie), MEC-0006 (Konformität, B-0013: Asch 1956, Bond & Smith 1996 Meta-Analyse), MEC-0008 (Autorität, B-0013), MEC-0010 und MEC-0020 (Affect Labeling/Perspektivübernahme, B-0011: LeDoux-Primärquellen, PONS-Test-Reliabilität), MEC-0011 (Mirroring, B-0011, unverändert bestätigt statt erweitert), MEC-0015 (Kognitive Überlastung/Sludge, B-0013).

---

## 3. Welche bestehenden Modelle erweitert wurden

Von den 10 zu Sprint-Beginn bestehenden Modellen wurde **keines** inhaltlich erweitert außer **MOD-0010** (Kahneman Kognitive-Bias-Karte): B-0014 vertiefte Kategorie 2 (psychophysikalische Grundlage, Erstangebots-Vorteil) und fügte eine neue Kategorie 6 "Sozial-normative Verzerrungen" (Fairness-Verzicht) hinzu, mit expliziter Begründung, warum eine neue Kategorie statt Einordnung in Kategorien 1–5 nötig war. Eine geprüfte MOD-0012-Neuanlage als eigenes Container-Modell wurde in B-0014 bewusst verworfen (Container-Dopplungsprüfung negativ).

Zwei **neue** Modelle wurden im Sprint canonicalisiert: **MOD-0011 (Choice Architecture, B-0013)** und **MOD-0012 (SUCCESS-Framework, B-0015)** — beide als vom jeweiligen Buch selbst vorgeschlagene, in sich konsistente Integrationsrahmen mit mehreren canonicalisierten Komponenten (MOD-0011: Defaults, Framing, Sludge; MOD-0012: Simple/Unexpected/Concrete/Credible/Emotional/Stories). Für beide gilt ein dokumentierter Vorbehalt: Das Gesamtmodell selbst (nicht seine Einzelkomponenten) ist nicht als integriertes Konstrukt empirisch getestet — dies ist bei MOD-0011 zusätzlich durch die SD-SYS-005-Kontroverse verschärft (siehe Abschnitt 7).

---

## 4. Welche neuen Mechanismen tatsächlich notwendig waren

Acht neue Mechanismen wurden sprintweit angelegt, jeder mit vollständiger Canonicalization-Rejection-Dokumentation (Stimulus/Prozess/Reaktion-Vergleichstabelle gegen die besten bestehenden Kandidaten, CKM-Schritt-1-3-Logik):

| MEC-ID | Name | Buch | Kernabgrenzung gegen bestehende Objekte |
|---|---|---|---|
| MEC-0022 | Emotional Contagion durch Facial Feedback | B-0011 | Unwillkürlich/nicht-intentional vs. MEC-0011 (bewusstes, gesteuertes Mirroring) |
| MEC-0023 | Zero-Preis-Effekt | B-0012 | Kategorialer, sprunghafter Bewertungswechsel bei Preis = 0 vs. graduelle Anchoring-/Kontrasteffekte |
| MEC-0024 | Sludge (künstliche Transaktionsreibung) | B-0013 | Aktive Reibungserhöhung als Verhaltensblockade, unabhängig von Informations-/Aufklärungsdefiziten (Kontrollgruppen-Beleg) |
| MEC-0025 | Fairness-Verzicht (Ultimatum-Spiel) | B-0014 | Aktive kostenpflichtige Bestrafung eines intentionalen Akteurs vs. passive Verlustvermeidung (MEC-0002) oder rein perzeptueller Kontrast (MEC-0009) |
| MEC-0026 | Curse of Knowledge | B-0015 | Strukturell eigenständiges Kommunikations-/Perspektivübernahme-Defizit, nicht deckungsgleich mit bestehenden Aufmerksamkeits- oder Empathie-Mechanismen |
| MEC-0027 | Gap-Theorie der Neugier | B-0015 | Eigenständige informationslückenbasierte Motivationsquelle, komplementär, aber nicht identisch mit MEC-0018 (Aufmerksamkeitsvorbereitung durch Priming) |
| MEC-0028 | Konkretheits-Encoding (Dual Coding) | B-0015 | Gedächtniskodierungsmechanismus (verbal+bildhaft), keine Überschneidung mit Entscheidungs- oder Einflussmechanismen |
| MEC-0029 | Narrative Transportation | B-0015 | Immersionsbasierte Einstellungsübernahme unabhängig vom Fiktions-/Faktizitätsstatus, strukturell verschieden von rhetorischer Persuasion (Cialdini-Prinzipien, MOD-0002) |

**Sprint-eigene Bewertung:** Alle acht Neuanlagen sind sachlich begründbar — vier davon (MEC-0026 bis MEC-0029, alle aus B-0015) erschließen mit "Kommunikationspsychologie/Gedächtnis/Narrativpersuasion" ein für den Codex zuvor nahezu unbesetztes Themenfeld (daher die niedrige Canonicalization Rate von B-0015, siehe Abschnitt 5 — dies ist Wissenslückenschließung, keine Mechanismus-Inflation). Für jede Neuanlage wurden mindestens ein, meist zwei bis drei geprüfte und explizit abgelehnte Alternative-Kandidaten dokumentiert (z. B. Preference Reversal und Money Illusion als Anchoring-Unterfälle statt eigener MECs in B-0014; Chunking/Miller 1956 und SUCCESS-als-Gesamt-MEC in B-0015 bewusst nicht canonicalisiert).

---

## 5. Canonicalization Rate über alle fünf Bücher

**Berechnungsbasis (mechanismus-spezifisch, konsistent mit allen fünf Einzelberichten):** Canonicalization Rate = Erweiterungen / (Neue MECs + Erweiterungen) × 100.

| Buch | Neue MECs | Erweiterte MECs | Canonicalization Rate |
|---|---|---|---|
| B-0011 (Emotional Intelligence) | 1 | 3 | 75,0 % |
| B-0012 (Predictably Irrational) | 1 | 5 | 83,3 % |
| B-0013 (Nudge) | 1 | 5 | 83,3 % |
| B-0014 (Priceless) | 1 | 2 | 66,7 % |
| B-0015 (Made to Stick) | 4 | 1 | 20,0 % |
| **Sprint gesamt** | **8** | **16** | **66,7 %** |

**Gesamtformel:** 16 Erweiterungen / (8 neue MECs + 16 Erweiterungen) × 100 = 16/24 × 100 = **66,7 %**.

**Einordnung:** Die sprintweite Rate von 66,7 % liegt über dem im B-0014-Report benannten Sprint-Zielwert (≥ 60 %) und ist, gewichtet über fünf Bücher mit sehr unterschiedlichen Themenfeldern, als hoch einzustufen. Die niedrige Einzelrate von B-0015 (20 %) senkt den Durchschnitt spürbar, ist aber – wie im Einzelbericht begründet – Ausdruck einer echten, zuvor unbesetzten Wissenslücke (Kommunikations-/Gedächtnispsychologie) und keine Qualitätsschwäche: Ohne die vier B-0015-Neuanlagen läge die Rate der übrigen vier Bücher (Entscheidungspsychologie-Kernthema) bei 15 Erweiterungen / (4 neue + 15 Erweiterungen) × 100 = **78,9 %** — ein Beleg dafür, dass der Codex im Kernbereich Entscheidungspsychologie bereits vor dem Sprint gut abgedeckt war und der Sprint dort überwiegend vertieft statt neu aufgebaut hat.

---

## 6. Veränderung der wissenschaftlichen Reife des Sales Codex

**Quantitativ:** Mechanismen 21 → 29 (+38 %), Modelle 10 → 12 (+20 %), Quellen 10 → 15 (+50 %), Statements 201 → 309 (+54 %).

**Qualitativ, drei Dimensionen:**

1. **Primärquellen-Tiefe:** Mehrere zuvor nur über Practitioner-Sekundärzitate bekannte Befunde wurden auf ihre akademischen Gründungsarbeiten zurückgeführt (z. B. Preference Reversal auf Lichtenstein & Slovic 1971 und Grether & Plott 1979 statt nur auf Poundstones Darstellung; Curse of Knowledge auf Camerer/Loewenstein/Weber 1989 statt nur auf die Heath-Brüder-Anekdoten). Dies erhöht die Prüfbarkeit und Zitierfähigkeit des Codex strukturell.

2. **Replikationskritik als etablierte Praxis, nicht Ausnahme.** Der Sprint hat in allen fünf Büchern systematisch nach Replikationsstatus gesucht und dabei zwei prominente Negativbefunde selbst eingebracht statt sie zu glätten: die gescheiterte Ten-Commandments-Replikation (Verschuere et al. 2018, B-0012) und die gescheiterte Identifiable-Victim-Effect-Replikation (Maier et al. 2023, B-0015). Beide sind mit expliziten Warnhinweisen (⚠⚠) in den betroffenen Statements/Mechanismen verankert, nicht stillschweigend weggelassen. Dies ist ein struktureller Reifegewinn: Der Codex dokumentiert jetzt aktiv gegen seine eigenen Kernbehauptungen gerichtete Evidenz.

3. **Autoren-Integritäts- und Publikationsbias-Transparenz als durchgängiges Prinzip.** Die in B-0012 neu eingeführte Kategorie "Autoren-Integritätsrisiko" (Ariely-Datenfälschungskontroverse) und die in B-0013 vertiefte SD-SYS-005-Kontroverse (Mertens et al. 2021 vs. Maier/Szaszi et al. 2022) wurden nicht als Einzelfälle behandelt, sondern als Präzedenz für den gesamten weiteren Sprint genutzt (konsistent konservative Behandlung methodisch fragiler Einzelstudien in B-0014 und B-0015).

**Verbleibende strukturelle Schwäche (sprintübergreifend, nicht durch diesen Sprint behoben):** Die B2B-Transfer-Lücke bleibt in allen fünf Büchern ungelöst und wird explizit als "durchgängig" dokumentiert (kein einziges der acht neuen Mechanismen wurde an einer direkten B2B-Vertriebsstichprobe getestet). Dies ist keine Verschlechterung, aber auch kein Fortschritt gegenüber dem Codex-Zustand vor dem Sprint.

---

## 7. Neue Scientific Debt

Vollständig dokumentiert in `00_project/SCIENTIFIC_DEBT.md`, Abschnitte "B-0011" bis "B-0015". Sprintweit wichtigste Einträge:

- **Autoren-Integritätsrisiko (B-0012):** Dan Ariely, Data-Colada-Untersuchung, Retraction von Shu/Mazar/Gino/Ariely/Bazerman (2012, PNAS) wegen nachgewiesener Datenfälschung. Differenzierte Prüfung ergab: Die in SRC-0012 zentral genutzten Kernexperimente (Decoy, Anchoring, Zero-Preis, Endowment) beruhen auf unabhängigen Gründungs- bzw. Replikationsquellen und sind nicht direkt betroffen — Ten-Commandments-Priming-Befund (nicht Ariely-Fälschungsgegenstand, aber unabhängig durch Verschuere et al. 2018 nicht repliziert) wurde bewusst NICHT canonicalisiert.
- **SD-SYS-005 — Nudge-/Choice-Architecture-Publikationsbias-Kontroverse (B-0013, mit Ergänzung nach Korrektur einer Duplizierung):** Mertens et al. (2021, PNAS, d=0,43) vs. Maier et al. (2022) und Szaszi et al. (2022, beide PNAS, Robust Bayesian Reanalyse, keine verlässliche Evidenz nach Publikationsbias-Korrektur). Betrifft MEC-0002 (Default-Erweiterung), MOD-0011 und P-0048 unmittelbar — bewusst NICHT auf höheres Evidenzlevel gehoben trotz neuer B-0013-Stützbelege.
- **Kulturelle Generalisierungsgrenze des Ultimatum-Spiels (B-0014):** Henrich et al. (2001, 2004) — Fairness-Verzicht-Muster ist an Marktökonomie-Einbindung gekoppelt, nicht universell. Höchste Priorität unter den neuen kulturellen Generalisierungs-Einträgen.
- **Gescheiterte Identifiable-Victim-Effect-Replikation (B-0015):** Maier et al. (2023, Collabra: Psychology) fand keine Stützung für den zentralen "Rokia"-Befund (Small/Loewenstein/Slovic), der im Buch als Kernbeleg der EMOTIONAL-Komponente dient. Bewusst nur als Anwendungsfall von MEC-0028 mit prominentem ⚠⚠-Warnhinweis dokumentiert, nicht als eigenständiger Mechanismus verwendet.
- **Zwei ethisch nicht verwertete Befundlinien (B-0014):** Demografische Preisdiskriminierung und Testosteron-/Oxytocin-Korrelate der Bestrafungsbereitschaft — bewusst nicht in anwendbare Codex-Objekte überführt (Kennzeichnungspflicht, hohe Priorität).
- **Mehrere bibliografisch nicht vollständig verifizierbare Quellen:** Zwei unveröffentlichte/schwer auffindbare Stanford-Dissertationen (Newton 1990, Bechky 1999, B-0015), eine UCLA-Studie ohne vollständige Autorenangabe (B-0015), die "Barr Scale" (B-0014) — durchgängig als offene bibliografische Fragen markiert statt spekulativ vervollständigt.
- **Survivorship-Bias-Risiko (B-0015, durchgängig):** Hoher Anteil unkontrollierter Fallstudien/Anekdoten (Nordstrom, Southwest, Subway u. a.) ohne systematischen Vergleich mit gescheiterten Kommunikationsversuchen ähnlicher Struktur.

---

## 8. Neue Tier-1-Forschungskandidaten

Zur Aufnahme in `00_project/ACADEMIC_RECOVERY_PLAN.md` vorgeschlagen (reine Dokumentation in diesem Bericht, keine Eintragung — außerhalb des Sprint-Scopes):

- **Oosterbeek, Sloof & van de Kuilen (2004)** — Ultimatum-Spiel-Metaanalyse (37 Studien): zentrale Evidenzbasis für MEC-0025, starker Kandidat.
- **Henrich et al. (2001, 2004)** — interkulturelle Ultimatum-Spiel-Feldstudie: wertvoller Beitrag zur sprintübergreifend offenen B2B-Internationalisierungsfrage.
- **Schley & Weingarten (2023/2026)** — Anchoring-Metaanalyse (2.603 Effektgrößen, bereits vor diesem Sprint verifiziert, hier erneut als Kernstütze für MEC-0021 bestätigt).
- **Mertens et al. (2021) / Maier et al. (2022) / Szaszi et al. (2022)** — die drei PNAS-Arbeiten der Nudge-Publikationsbias-Kontroverse als zusammenhängendes Tier-1-Trio; eine gemeinsame Aufnahme würde die SD-SYS-005-Dokumentation zusätzlich absichern.
- **Maier et al. (2023, Collabra: Psychology)** — Identifiable-Victim-Effect-Replikationsstudie: wichtigster neuer Replikationsbefund des Sprints, sollte mit vergleichbarer Priorität wie Verschuere et al. (2018, B-0012) behandelt werden.
- **Camerer, Loewenstein & Weber (1989)** — Curse-of-Knowledge-Gründungsarbeit: mittlerer Kandidat, würde MEC-0026 zusätzlich absichern.
- **Sanfey et al. (2003, Science)** — neuronale Ultimatum-Spiel-Studie: mittlerer Kandidat, Tier-1-Prüfung sollte gezielt nach Replikationen des spezifischen Insula-Befunds suchen.

---

## 9. Empfehlungen für Sales Codex Version 1.0

Diese Empfehlungen sind Beobachtungen zur Weiterverarbeitung, keine Governance-Entscheidungen — sie schließen keine Open Decisions und ändern kein Framework.

1. **Die sprintweite Canonicalization Rate von 66,7 % sollte als Referenzwert für künftige Sprints dienen**, nicht als Mindestschwelle: B-0015 zeigt, dass ein niedrigerer Wert bei echter Themenfelderweiterung sachlich gerechtfertigt ist. Eine undifferenzierte Mindestquote würde falsche Anreize setzen.
2. **MEC-0021 (Anchoring) als am dichtesten belegter Mechanismus des Nicht-Kahneman-Bestands** ist ein guter Kandidat für eine gesonderte Tiefenprüfung/Peer Review vor Version 1.0, da er nun Primärquellen aus vier verschiedenen Büchern (B-0002/Cialdini indirekt, B-0010/Kahneman, B-0012/Ariely, B-0013/Nudge, B-0014/Priceless) bündelt.
3. **Die B2B-Transfer-Lücke bleibt der wichtigste ungelöste strukturelle Schwachpunkt** des gesamten Codex, nicht nur dieses Sprints. Für Version 1.0 sollte geprüft werden, ob ein eigener Forschungssprint (kein Book-Mode-Sprint) gezielt nach B2B-Feldstudien zu den zehn am häufigsten zitierten Mechanismen sucht.
4. **Die vier neuen B-0015-Mechanismen (Kommunikationspsychologie) öffnen ein Themenfeld, das bislang nur einen Vertreter (SRC-0015) hat.** Vor Version 1.0 sollte geprüft werden (Governance-Entscheidung, nicht Teil dieses Berichts), ob ein zusätzliches Buch zu Gedächtnis/Kommunikation den Bestand absichern soll, oder ob dies bewusst ein schlanker werdender Bereich bleibt.
5. **Zwei Replikationsversagen (Verschuere et al. 2018 zu Ten Commandments; Maier et al. 2023 zu Identifiable Victim) sind jetzt im Codex verankert.** Für Version 1.0 wird empfohlen, eine sprintübergreifende Übersicht "bekannte Replikationsversagen" zu führen (z. B. als Ergänzung zu `00_project/SCIENTIFIC_DEBT.md`), damit diese nicht in Einzelbuchsektionen verstreut bleiben — dies ist ein Vorschlag zur redaktionellen Auffindbarkeit, keine Framework-Änderung.
6. **Die Autoren-Integritätsrisiko-Kategorie (eingeführt in B-0012) hat sich bewährt** und sollte als Standardprüfschritt in künftige Buchanalysen-Checklisten aufgenommen werden (redaktionelle Empfehlung, keine CKM-Änderung).
7. **MOD-0011 und MOD-0012 sind beide neu und ungetestet als Gesamtkonstrukt.** Vor Version 1.0 wird empfohlen, beide Modelle in einem künftigen Peer-Review-Sprint (analog Sprint 1/2) auf internen Konsistenzbedarf zu prüfen, bevor sie als vollwertig etablierte Codex-Modelle kommuniziert werden.
8. **Dieser Sprint bestätigt erneut (wie SPR-0002), dass hohe Canonicalization Rate und wissenschaftliche Tiefe zusammengehen, nicht im Widerspruch stehen** — ein wichtiger Beleg für die Sales-Codex-1.0-Programm-These, dass "Scientific Completion" nicht gleichbedeutend mit Objektwachstum ist.

---

## Abschluss SPR-0003

Der Sprint "Behavioral Science Expansion" ist mit Abschluss dieses Syntheseberichts vollständig abgearbeitet. Alle fünf Bücher wurden vollständig im Book Mode verarbeitet, alle Pflicht-Deliverables (SRC, Wissensobjekte, VAL, BOOK_REVIEW_REPORT, CANONICALIZATION_REPORT je Buch) wurden erstellt und stichprobenartig gegen den tatsächlichen Repository-Zustand verifiziert (Read-Tool-Verifikation, nicht nur Agentenbericht). `00_project/SCIENTIFIC_DEBT.md` und `05_research/LITERATURE_INDEX.md` wurden für alle fünf Bücher tatsächlich aktualisiert (nicht nur in den Einzelberichten angekündigt).

Keine Framework-Änderungen, keine Governance-Entscheidungen, keine Schließung von Open Decisions und keine Repository-Restrukturierung wurden in diesem Sprint vorgenommen — wie im Auftrag gefordert.

Gemäß Auftrag endet der Sprint hiermit automatisch.

---

*Erstellt: 2026-07-02 | SPR-0003 | KI-Redaktion Sales Codex | Behavioral Science Expansion Sprint 1, Bücher 1–5 von 5*
