# Canonicalization Report -- B-0014 (Priceless: The Myth of Fair Value, Poundstone 2010)

## Zweck

Detaillierte Dokumentation aller Canonicalization-Entscheidungen der B-0014-Buchanalyse, gemaess Editor-Auftrag "Behavioral Science Expansion" -- Prioritaet 1 (Kanonisierung vor Neuanlage). Ergaenzt VAL-0014 und BOOK_REVIEW_REPORT_B0014.md um die geforderten strukturierten Einzelabschnitte. Format und Anspruchsniveau folgen CANONICALIZATION_REPORT_B0011.md, CANONICALIZATION_REPORT_B0012.md und CANONICALIZATION_REPORT_B0013.md (Buecher 1-3 desselben Sprints).

**Formel (uebernommen aus SPR-0001/canonicalization_report.md, identisch zu B-0011/B-0012/B-0013):** Canonicalization Rate = Extensions / (Neue Objekte + Extensions) x 100, bezogen auf Mechanismen (MECs) -- die Objektkategorie, die im CKM primaer kanonisierbar ist.

---

## 1. Neue Statements

**Anzahl:** 20
**ID-Bereich:** ST-0267 bis ST-0286

Alle 20 Statements sind buchspezifische Einzelaussagen (per CKM-Definition nicht kanonisierbar/erweiterbar -- Statements werden immer neu angelegt, auch wenn ihr Inhalt zur Fundierung bestehender A/MEC/P-Objekte verwendet wird). Zuordnung zu den Erweiterungen/Neuanlagen: ST-0267 (UN-Gluecksrad-Primaerquelle) -> MEC-0021-Erweiterung; ST-0268 (Northcraft & Neale) -> MEC-0021-Erweiterung; ST-0269 (Ritov Erstangebot) -> A-0048/P-0042-Erweiterung; ST-0270 (Consider the Opposite) -> T-0046 (neu); ST-0271 (Jury-Anchoring) -> P-0042-Erweiterung; ST-0272/ST-0273/ST-0274 (Weber/Fechner/Stevens/Helson) -> MEC-0009-Erweiterung; ST-0275/ST-0276/ST-0277/ST-0278 (Ultimatum-Spiel-Gruendungsstudien, Sanfey-fMRI, Zwei-Angebote-Variante, Outrage Theory) -> MEC-0025 (neu); ST-0279 (Preference Reversal) -> MEC-0021-Erweiterung (verworfener MEC-Kandidat, eingeordnet); ST-0280 (Transaction Utility) -> Kontext-Statement, keine Objekt-Erweiterung; ST-0281 (Money Illusion) -> MEC-0021-Erweiterung (verworfener MEC-Kandidat, eingeordnet); ST-0282 (Zero-Preis-Konvergenz) -> Dokumentation ohne MEC-0023-Erweiterung (keine neue Evidenz); ST-0283/ST-0284 (Diskriminierung, Hormonforschung) -> Nicht-Anlage-Dokumentation mit explizitem Ethik-Warnhinweis; ST-0285 (kulturelle Generalisierbarkeit) -> MEC-0025-Grenzen; ST-0286 (Cognitive-Reflection-Unabhaengigkeit) -> MEC-0021-Erweiterung.

---

## 2. Neue Assumptions

**Anzahl:** 1
**ID:** A-0056

- **A-0056** (Fairness-Normverletzung motiviert kostenpflichtige Bestrafung unabhaengig von Verlustaversion): Postuliert, dass ein als unfair wahrgenommenes Angebot eine emotionale Bestrafungsmotivation ausloest, die stark genug ist, einen strikt positiven eigenen Gewinn zu opfern -- unabhaengig davon, ob der Verzicht selbst einen "Verlust" relativ zu einem Referenzpunkt darstellt. Abgrenzung zu MEC-0002 (reine Verlustaversion) explizit dokumentiert: Im Standard-Ultimatum-Spiel wird kein Verlust vermieden, sondern ein sicherer Gewinn aktiv geopfert -- reine Verlustaversion erklaert dies nicht vollstaendig. Grundlage fuer MEC-0025 (neu) und P-0051 (neu). Evidenzstatus E4 (Ultimatum-Spiel-Grundphaenomen, Metaanalyse 37 Studien) / E3 (spezifische neuronale Fundierung, Sanfey et al. 2003, Einzelstudie).

**A-0048-Erweiterung (keine Neuanlage, Erweiterung eines bestehenden Objekts):** A-0048 (Anker sollten proaktiv gesetzt werden) enthielt bereits vor dieser Buchanalyse eine explizit dokumentierte Evidenzluecke ("die strategische Implikation ist normativ/strategisch, nicht empirisch gemessen"). Ritov (1996, ST-0269) schliesst diese Luecke empirisch (kontrollierte Verhandlungssimulation, N=148, Erstangebots-Vorteil unabhaengig von Kaeufer-/Verkaeuferrolle). Als Erweiterungsabschnitt in A-0048 dokumentiert, keine neue Assumption-ID vergeben, da die inhaltliche Kernannahme unveraendert bleibt und lediglich empirisch gestuetzt wird.

---

## 3. Neue Mechanismen

**Anzahl:** 1
**ID:** MEC-0025 -- "Fairness-Verzicht: Kostenpflichtige Bestrafung wahrgenommener Unfairness"

### Canonicalization-Rejection-Begruendung (vollstaendig, aus MEC-0025-Datei zusammengefasst)

Geprueft bestehende Objekte: **MEC-0002 (Verlustaversion und Kosten des Status quo)**, **MEC-0009 (Perzeptueller Kontrast)**.

**CKM-Schritt 1 (Suche):** MEC-0002 ist der naheliegendste Kandidat, da Ultimatum-Spiel-Ablehnungen oberflaechlich wie "Verlustvermeidung" wirken koennten. MEC-0009 ist ebenfalls naheliegend, da die Fairness-Bewertung auf einem Vergleich zum Referenzstandard beruht. Eine gezielte Grep-Pruefung des bestehenden Repository-Bestands bestaetigte: Kein bestehendes MEC- oder P-Objekt deckt das spezifische Ultimatum-Spiel-/Fairness-Bestrafungsphaenomen ab; ST-0085 (SRC-0003, Voss) erwaehnt "fair" nur als rhetorische Taktik, nicht als kausalen Mechanismus.

**CKM-Schritt 2 (Identitaetspruefung nach kausaler Struktur):**

| Merkmal | MEC-0002 (Verlustaversion) | MEC-0009 (Perzeptueller Kontrast) | MEC-0025 (Fairness-Verzicht) |
|---|---|---|---|
| Stimulus (X) | Wahrgenommener potenzieller Verlust relativ zu einem Referenzpunkt | Vorangegangener/gleichzeitiger Vergleichsreiz (graduell) | Angebot unterhalb eines sozial-normativen Fairness-Standards (kategorial: fair/unfair) |
| Prozess (Y) | Verlustgewichtung ca. doppelt so stark wie Gewinngewichtung -- motiviert VERMEIDUNG eigener Verluste | Relative, kontinuierliche Kontrastwahrnehmung (Weber'sches Gesetz) | Emotionale Normverletzungs-/Empoerungsreaktion (Insula-Aktivierung) -- motiviert AKTIVE BESTRAFUNG des Gegenuebers |
| Reaktion (Z) | Vermeidung/Festhalten am Status quo | Graduell veraenderte Bewertung proportional zur Kontraststaerke | Aktive Ablehnung eines strikt positiven eigenen Gewinns, um dem Gegenueber zu schaden |
| Kernevidenz | Kahneman/Tversky 1979 | Weber's Law, Decoy-Effekt | Gueth et al. 1982, Sanfey et al. 2003 (fMRI), Oosterbeek/Sloof/van de Kuilen 2004 (Metaanalyse) |

**Entscheidender Beleg fuer die kausale Nicht-Identitaet:** Im Standard-Ultimatum-Spiel wird durch die Ablehnung kein Verlust VERMIEDEN -- ein sicherer positiver Gewinn wird AKTIV GEOPFERT. Reine Verlustaversion erklaert die Ablehnung strikt positiver Angebote nicht. Kontrastwahrnehmung (MEC-0009) ist zudem ein rein perzeptuelles, nicht-soziales Phaenomen (wirkt auch bei unbelebten Reizen ohne Interaktionspartner); Fairness-Verzicht erfordert einen intentionalen sozialen Akteur und aktive Bestrafungsmotivation -- gestuetzt durch qualitativ unterschiedliche neuronale Korrelate (Insula-Aktivierung als Ekel-/Normverletzungskorrelat, kein typisches Kontrast- oder Verlustaversions-Areal).

**CKM-Schritt 3 (Qualitaetspruefung, alle vier Bedingungen erfuellt):**
1. Nicht bereits durch bestehendes Objekt abgedeckt -- siehe Kontrastanalyse oben.
2. Eigenstaendiger erklaerender Beitrag: Ja -- kostenpflichtige Bestrafung entgegen dem eigenen materiellen Interesse ist ein explizit als eigenstaendiges Phaenomen behandelter Befund.
3. Mindestschwelle (>=2 unabhaengige Auftreten als erklaerende Kraft): Erfuellt -- Ultimatum-Spiel-Ablehnungen, Zwei-Angebote-Verschiebung (Bazerman/White/Loewenstein), Jury-Strafzumessung/Outrage Theory (Kahneman/Schkade/Sunstein) sind drei unabhaengige Anwendungen; zusaetzlich mehrfach repliziert (Metaanalyse 37 Studien) und neuronal fundiert.
4. Keine blosse Umbenennung: Erfuellt -- beschreibt eine qualitativ andere, sozial-normative Wirkform.

**Ergebnis:** Alle vier Bedingungen erfuellt -> Neuanlage gerechtfertigt. Evidenzlevel E4 (Ultimatum-Spiel-Grundphaenomen, breite Metaanalyse-Stuetzung) / E3 (spezifische neuronale Fundierung, Einzelstudie -- konservativ getrennt ausgewiesen, kein pauschales E4/E5).

**Keine weiteren neuen Mechanismen wurden angelegt.** Zwei geprueften Kandidaten (Preference Reversal, Money Illusion) wurden als Erweiterungen von MEC-0021 eingeordnet (siehe Abschnitt 4); zwei weitere Kandidaten (Testosteron/Oxytocin, demografische Diskriminierung) wurden aus ethischen Gruenden bewusst nicht in anwendbare Objekte ueberfuehrt (siehe Abschnitt 4, Ethik-Hinweis).

---

## 4. Erweiterte Objekte

**Anzahl:** 6 (2 MEC, 1 A, 2 P, 1 MOD)

| Objekt | Art der Erweiterung |
|---|---|
| **MEC-0021 (Anchoring-Mechanismus)** | Vollstaendige Primaerquellen-Rekonstruktion des UN-Gluecksrad-Experiments (ST-0267), praezisierte Northcraft & Neale-Feldstudiendetails mit websuchverifizierten Korrelationswerten (r=0,41 Experten / r=0,48 Laien), neuer Jury-Schadenersatz-Anchoring-Beleg ohne "Boomerang-Effekt" (Chapman & Bornstein 1996), Erstangebots-Vorteil-Verweis (Ritov 1996), Consider-the-Opposite-Antidot-Referenz (Mussweiler/Strack/Pfeiffer 2000), neuer Robustheitsbeleg gegen kognitive Reflexionsneigung (Oechssler/Roider/Schmitz, N=1.250). Zusaetzlich zwei geprueft-und-eingeordnete Kandidaten: Preference Reversal (Lichtenstein & Slovic 1971; Grether & Plott 1979) als Unterfall von Pfad 1, Money Illusion (Shafir/Diamond/Tversky 1997, von den Originalautoren selbst als "a form of anchoring" bezeichnet) als Unterfall von Pfad 2. Kein E-Level-Wechsel (bleibt E5). |
| **MEC-0009 (Perzeptueller Kontrast)** | Erstmalige vollstaendige psychophysikalische Fundierung: Weber's Law (1834), Fechnersches Gesetz (1850), Stevens' Machtgesetz (1957, mit websuchverifizierter Methodenkritik), Helsons Adaptationsniveau-Theorie (1947) als historischer Begriffsursprung von "Anker" -- mit expliziter Abgrenzung zu Tversky/Kahneman-Anchoring (Kontrast-/Adaptationseffekt vs. assoziativ-kognitiver Pfad + Adjustment-Pfad). Schliesst eine zuvor im Bestand offen dokumentierte Frage zur Anchoring-Verwandtschaft. Kein E-Level-Wechsel (bleibt E4/E3). |
| A-0048 (Anker sollten proaktiv gesetzt werden) | Empirische Schliessung der zuvor als "normativ, nicht empirisch gemessen" dokumentierten Luecke durch Ritov (1996, N=148, kontrollierte Verhandlungssimulation, Erstangebots-Vorteil unabhaengig von Rolle). |
| P-0042 (Ankerkontrolle im Preisgespraech) | Empirischer Beleg fuer Umsetzungsrichtlinie 2 (extreme Eroeffnung) durch Ritov (1996) und Widerlegung des "Boomerang-Effekts" durch Chapman & Bornstein (1996). |
| P-0014 (Referenzrahmen-Kontrolle) | Schliessung der offenen Frage zur Anchoring-Verwandtschaft durch Verweis auf die MEC-0009-Erweiterung (keine inhaltliche Neuanlage, reine Verweisergaenzung). |
| MOD-0010 (Kahneman Kognitive-Bias-Karte) | Vertiefung Kategorie 2 (psychophysikalische Grundlage, Erstangebots-Vorteil) sowie neue Kategorie 6 "Sozial-normative Verzerrungen" (Fairness-Verzicht) mit vollstaendiger Begruendung, warum eine neue Kategorie (statt Einordnung in Kategorien 1-5) erforderlich ist. Keine MOD-0012-Neuanlage (Container-Dopplungs-Pruefung negativ, siehe Abschnitt 3 der MOD-0010-Erweiterung). |

**Repository-Anomalie-Hinweis (unveraendert, nicht durch B-0014 verursacht):** MEC-0021 enthaelt weiterhin den bereits vor B-0013 dokumentierten, abgeschnittenen Erweiterungsabschnitt ("Erweiterung: Meta-analytische B") mit Warnvermerk -- unveraendert belassen, ausserhalb des Scopes dieser Buchanalyse.

---

## 5. Canonicalization Rate

**Berechnungsbasis (MEC-spezifisch, wie in SPR-0001/B-0011/B-0012/B-0013 definiert):**

- Neue MECs: 1 (MEC-0025)
- Erweiterte MECs: 2 (MEC-0021, MEC-0009)
- **Canonicalization Rate B-0014 = 2 / (1 + 2) x 100 = 66,7%**

**Vergleich mit vorherigen Buechern des Sprints:**

| Buch | Canonicalization Rate (MEC-basiert) | Neue MECs | Erweiterte MECs |
|---|---|---|---|
| B-0011 (Emotional Intelligence, Goleman) | 75,0% | 1 | 3 |
| B-0012 (Predictably Irrational, Ariely) | 83,3% | 1 | 5 |
| B-0013 (Nudge, Thaler & Sunstein) | 83,3% | 1 | 5 |
| **B-0014 (Priceless, Poundstone)** | **66,7%** | **1** | **2** |

B-0014 liegt niedriger als die drei vorangegangenen Buecher, bleibt aber deutlich ueber dem Sprint-1-Zielwert (>=60%) und ueber dem urspruenglichen Sprint-1-Hoechstwert vor dieser Erweiterung (B-0005: 67% -- nahezu identisch). Dies ist inhaltlich plausibel und KEIN Qualitaetsmangel: Priceless behandelt mit dem Ultimatum-Spiel-/Fairness-Komplex ein Themenfeld (soziale/normative Verhandlungspsychologie), fuer das im bisherigen Codex-Bestand kein passendes MEC existierte -- eine gezielte Grep-Pruefung vor Buchbeginn bestaetigte dies. Die Neuanlage von MEC-0025 ist daher eine echte Wissensluecken-Schliessung, keine vermeidbare Mechanismus-Vervielfachung: Zwei zusaetzliche, oberflaechlich naheliegende MEC-Kandidaten (Preference Reversal, Money Illusion) wurden bewusst NICHT neu angelegt, sondern korrekt als Unterfaelle von MEC-0021 identifiziert -- ohne diese beiden bewussten Ablehnungen waere die Canonicalization Rate ceteris paribus noch niedriger ausgefallen, wenn sie faelschlich als eigene MECs gezaehlt worden waeren. Die Sprintvorgabe ("hohe Canonicalization Rate ist Guetemerkmal, keine Wachstumspflicht") bleibt durch die vollstaendige CKM-Pruefung und explizite Rejection-Dokumentation fuer MEC-0025 sowie die zwei Nicht-Anlage-Entscheidungen vollstaendig erfuellt.

**Codex-weite Rate (alle Objekttypen, informativ, nicht die primaere Kennzahl):** 6 Extensions / (24 Neue + 6 Extensions) x 100 = 20,0%. Hoeher als bei B-0013 (15,6%), da bei B-0014 anteilig mehr bestehende Nicht-MEC-Objekte (A-0048, P-0042, P-0014, MOD-0010) erweitert statt neu angelegt wurden.

---

## 6. Neue Scientific Debt

Vollstaendig einzutragen in `00_project/SCIENTIFIC_DEBT.md`:

1. **Neue Sektion "B-0014 -- Priceless (SRC-0014)"** mit buchspezifischen Debt-Punkten: MEC-0025-neuronale-Fundierung-Einzelstudie (Sanfey et al. 2003, E3), MEC-0025-kulturelle-Generalisierbarkeitsgrenze (Henrich et al.), A-0056-externe-Validierung-ausstehend, T-0046-keine-Multi-Labor-Replikation, Testosteron/Oxytocin-Forschung-methodisch-schwach-und-ethisch-nicht-verwertbar (ST-0284), demografische-Diskriminierungsstudie-ethisch-nicht-verwertbar (ST-0283), durchgaengige B2B-Transferluecke.

Zusammenfassung der wichtigsten neuen Eintraege:

| Objekt-ID | Kategorie | Prioritaet |
|---|---|---|
| MEC-0025, A-0056 | Externe Validierung ausstehend (neuronale Fundierung) | Mittel -- Sanfey et al. 2003 ist Einzelstudie (E3), wenn auch vielfach nachfolgend zitiert |
| MEC-0025, P-0051 | Kulturelle Generalisierungsgrenze | Hoch -- Henrich et al.: Ultimatum-Spiel-Grundphaenomen ist an Marktoekonomie-Einbindung gekoppelt, nicht universell |
| T-0046 | Externe Validierung ausstehend | Niedrig -- zwei unabhaengige Anwendungskontexte (Mussweiler/Strack/Pfeiffer 2000), aber keine grosse Multi-Labor-Replikation bekannt |
| ST-0283, ST-0284 | Ethisches Risiko, bewusst nicht verwertet | Hoch (Kennzeichnungspflicht) -- Diskriminierungs- und Hormonforschung explizit als Nicht-Technik markiert |
| Durchgaengig (alle B-0014-Objekte) | Kulturelle Generalisierung / Transferluecke | Hoch -- Labor-/Studierendenstichproben und US-Rechtskontexte, kein direkter B2B-Vertriebstest |
| "Barr Scale" (informelle Fairness-Norm-Metrik) | Unbelegte Annahme | Niedrig -- im Buch nur als Experteneinschaetzung erwaehnt, keine validierte Metrik identifiziert |

---

## 7. Neue Literaturquellen

Vollstaendig einzutragen in `05_research/LITERATURE_INDEX.md`, Abschnitt A (Entscheidungspsychologie & Behavioral Economics). Zusammenfassung:

| APA-Zitation | Verifikationsstatus | Unterstuetzt |
|---|---|---|
| Gueth, W., Schmittberger, R. & Schwarze, B. (1982). An Experimental Analysis of Ultimatum Bargaining. *Journal of Economic Behavior & Organization*, 3(4), 367-388. | Verifiziert (2026-07-02) | MEC-0025 (neu), A-0056, P-0051 |
| Kahneman, D., Knetsch, J.L. & Thaler, R.H. (1986). Fairness and the Assumptions of Economics. *Journal of Business*, 59(4). | Verifiziert (2026-07-02) | MEC-0025 (neu) |
| Sanfey, A.G., Rilling, J.K., Aronson, J.A., Nystrom, L.E. & Cohen, J.D. (2003). The Neural Basis of Economic Decision-Making in the Ultimatum Game. *Science*, 300(5626), 1755-1758. | Verifiziert (2026-07-02) | MEC-0025 (neu), A-0056 |
| Oosterbeek, H., Sloof, R. & van de Kuilen, G. (2004). Cultural Differences in Ultimatum Game Experiments: Evidence from a Meta-Analysis. *Experimental Economics*, 7(2), 171-188. | Verifiziert (2026-07-02) | MEC-0025 (neu), zentrale Metaanalyse-Stuetzung |
| Kahneman, D., Schkade, D. & Sunstein, C.R. (1998). Shared Outrage and Erratic Awards: The Psychology of Punitive Damages. *Journal of Risk and Uncertainty*, 16(1). | Verifiziert (2026-07-02) | MEC-0025 (neu) |
| Henrich, J. et al. (2001, 2004). In Search of Homo Economicus: Behavioral Experiments in 15 Small-Scale Societies. *American Economic Review*, 91(2). | Verifiziert (2026-07-02) | MEC-0025 (Grenzen), ST-0285 |
| Northcraft, G.B. & Neale, M.A. (1987). Experts, Amateurs, and Real Estate: An Anchoring-and-Adjustment Perspective on Property Pricing Decisions. *Organizational Behavior and Human Decision Processes*, 39(1), 84-97. | Verifiziert (2026-07-02, Korrelationswerte aus Sekundaerzitation) | MEC-0021 (Erweiterung) |
| Mussweiler, T., Strack, F. & Pfeiffer, T. (2000). Overcoming the Inevitable Anchoring Effect: Considering the Opposite Compensates for Selective Accessibility. *Personality and Social Psychology Bulletin*, 26(9), 1142-1150. | Verifiziert (2026-07-02) | T-0046 (neu) |
| Chapman, G.B. & Bornstein, B.H. (1996). The More You Ask For, the More You Get: Anchoring in Personal Injury Verdicts. *Applied Cognitive Psychology*, 10(6), 519-540. | Verifiziert (2026-07-02) | MEC-0021 (Erweiterung), P-0042 (Erweiterung) |
| Shafir, E., Diamond, P. & Tversky, A. (1997). Money Illusion. *Quarterly Journal of Economics*, 112(2), 341-374. | Verifiziert (2026-07-02) | MEC-0021 (Erweiterung, Money-Illusion-Einordnung) |
| Lichtenstein, S. & Slovic, P. (1971). Reversals of Preference Between Bids and Choices in Gambling Decisions. *Journal of Experimental Psychology*, 89(1), 46-55. | Verifiziert (2026-07-02) | MEC-0021 (Erweiterung, Preference-Reversal-Einordnung) |
| Grether, D.M. & Plott, C.R. (1979). Economic Theory of Choice and the Preference Reversal Phenomenon. *American Economic Review*, 69(4), 623-638. | Verifiziert (2026-07-02) | MEC-0021 (Erweiterung, gescheiterte Widerlegung -> Replikation) |
| Stevens, S.S. (1957). On the Psychophysical Law. *Psychological Review*, 64(3), 153-181. | Verifiziert (2026-07-02, inkl. spaetere Methodenkritik) | MEC-0009 (Erweiterung) |
| Oechssler, J., Roider, A. & Schmitz, P.W. (2009). Cognitive Abilities and Behavioral Biases. *Journal of Economic Behavior & Organization*, 72(1). | Verifiziert (2026-07-02) | MEC-0021 (Erweiterung) |
| Poundstone, W. (2010). Priceless: The Myth of Fair Value (and How to Take Advantage of It). | Vollstaendig verarbeitet als SRC-0014 | Alle B-0014-Objekte |

**Nicht bibliografisch vollstaendig verifizierbar (offene Fragen, nicht erfunden):** Weber, E.H. (1834) und Fechner, G.T. (1850) -- Primaerwerke aus der fruehen Psychophysik, im Buch nur sekundaer zitiert, vollstaendige Originaltitel/Verlagsangaben nicht im Fliesstext angegeben; die "Barr Scale" (informelle Fairness-Norm-Einschaetzung) ohne validierte Quellenangabe.

---

## 8. Publikationsbias-Risiken

Struktur wie VAL-0014 Punkt 6, hier als eigenstaendiger Berichtsabschnitt mit drei klar getrennten Ebenen:

1. **Kulturelle Generalisierbarkeitsgrenze des Ultimatum-Spiel-Grundphaenomens (direkt DIESES Buch betreffend):** Henrich et al. (2001, 2004) zeigen, dass das aus westlichen Studien bekannte Fairness-Verhandlungsmuster an die Existenz von Marktoekonomie/Tauschhandel gekoppelt ist -- in isolierten Kleingesellschaften ohne ausgepraegten Markthandel weicht das Muster stark ab (sowohl schwaecher als "Hyperfairness" ausgepraegt). Dies ist keine Publikationsbias-Frage im engeren Sinn, sondern eine Boundary-Conditions-Frage, die die generelle Anwendbarkeit von MEC-0025/P-0051 auf internationale B2B-Kontexte einschraenkt -- explizit dokumentiert, nicht geglaettet.
2. **Neuronale Fundierung als Einzelstudie (Sanfey et al. 2003):** Bewusst NICHT auf ein hoeheres Evidenzlevel als E3 gehoben, trotz haeufiger Nachfolgezitation in der Literatur -- konservative Einstufung analog zur B-0013-Behandlung von MEC-0024.
3. **Stevens' Machtgesetz (1957), spaetere Methodenkritik:** Websuchverifizierte Kritik an der verwendeten Magnitude-Estimation-Technik relativiert die Allgemeingueltigkeit des exakten Exponenten. Der Grundbefund (nichtlineare, kompressive Reiz-Empfindungs-Beziehung) gilt weiterhin als robust -- die Kritik ist methodisch, nicht auf systematische Nicht-Publikation negativer Ergebnisse zurueckzufuehren, daher als geringes Publikationsbias-Risiko (aber real vorhandenes Methodenrisiko) eingestuft.

**Zusaetzlich, ethisch relevant (kein Publikationsbias, aber verwandtes Qualitaetsrisiko):** Zwei Befundlinien (Testosteron/Oxytocin-Korrelate, ST-0284; demografische Preisdiskriminierung, ST-0283) beruhen auf methodisch schwachen (kleine Stichproben) bzw. ethisch nicht verwertbaren Studien. Beide wurden bewusst NICHT in anwendbare Codex-Objekte (MEC/T/P) ueberfuehrt, um weder eine unkritische Verstaerkung schwacher Evidenz noch eine ethisch bedenkliche Handlungsanweisung zu erzeugen -- konsistent mit der bereits in B-0012/B-0013 etablierten Praxis konservativer Behandlung methodisch fragiler oder ethisch riskanter Befunde.

**Sauberkeit der Trennung:** Kein Statement/Objekt in dieser Buchanalyse uebertraegt die schwaechere Einzelstudien-Fundierung (Sanfey et al.) automatisch auf das robuste Ultimatum-Spiel-Metaanalyse-Ergebnis (Oosterbeek/Sloof/van de Kuilen) oder umgekehrt -- beide Evidenzquellen werden getrennt und mit eigenem E-Level in MEC-0025 gefuehrt.

---

## 9. Neue Tier-1-Kandidaten (nur Dokumentation, keine Eintragung)

Gemaess Auftrag: Diese Quellen werden hier nur als moegliche Kandidaten fuer `00_project/ACADEMIC_RECOVERY_PLAN.md` dokumentiert -- eine tatsaechliche Eintragung dort ist ausserhalb des Scopes dieser Buchanalyse.

- **Oosterbeek, Sloof & van de Kuilen (2004) -- Ultimatum-Game-Metaanalyse:** Starker Kandidat fuer Tier-1. Eine der umfassendsten Metaanalysen zur Ultimatum-Spiel-Forschung (37 Studien, 75 Ergebnisse), zentrale Evidenzbasis fuer MEC-0025. Wuerde die Fairness-Verzicht-Erweiterung zusaetzlich absichern.
- **Sanfey et al. (2003) -- Neural Basis of Economic Decision-Making:** Mittlerer Kandidat -- einflussreiche Science-Publikation, aber Einzelstudie ohne bekannte direkte Replikation im selben Design; eine Tier-1-Pruefung muesste gezielt nach Replikationsstudien der spezifischen Insula-Befunde suchen.
- **Henrich et al. (2001, 2004) -- Interkulturelle Ultimatum-Spiel-Forschung:** Starker Kandidat -- grosse, koordinierte interkulturelle Feldstudie (Dutzende Kulturen), waere ein wertvoller Beitrag zur B2B-internationalen-Generalisierbarkeitsfrage, die in mehreren Scientific-Debt-Eintraegen als offen markiert ist.
- **Mussweiler, Strack & Pfeiffer (2000) -- Consider the Opposite:** Mittlerer Kandidat -- einzige im bisherigen Codex-Bestand dokumentierte, empirisch gepruefte Anchoring-Gegenmassnahme; eine Tier-1-Pruefung waere sinnvoll, falls T-0046 in kuenftigen Sprints als Kern-Verhandlungstechnik priorisiert wird.

---

## Status

Abgeschlossen -- 2026-07-02
