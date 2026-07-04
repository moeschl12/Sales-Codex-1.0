# Canonicalization Report — B-0012 (Predictably Irrational, Ariely 2008/2009)

## Zweck

Detaillierte Dokumentation aller Canonicalization-Entscheidungen der B-0012-Buchanalyse, gemäß Editor-Auftrag "Behavioral Science Expansion" — Priorität 1 (Kanonisierung vor Neuanlage). Ergänzt VAL-0012 und BOOK_REVIEW_REPORT_B0012.md um die geforderten strukturierten Einzelabschnitte. Format und Anspruchsniveau folgen CANONICALIZATION_REPORT_B0011.md (Buch 1 desselben Sprints).

**Formel (übernommen aus SPR-0001/canonicalization_report.md, identisch zu B-0011):** Canonicalization Rate = Extensions / (Neue Objekte + Extensions) × 100, bezogen auf Mechanismen (MECs) — die Objektkategorie, die im CKM primär kanonisierbar ist.

---

## 1. Neue Statements

**Anzahl:** 31
**ID-Bereich:** ST-0218 bis ST-0248

Alle 31 Statements sind buchspezifische Einzelaussagen (per CKM-Definition nicht kanonisierbar/erweiterbar — Statements werden immer neu angelegt, auch wenn ihr Inhalt zur Fundierung bestehender A/MEC/P-Objekte verwendet wird). Ein Großteil der Statements diente als Belegquelle für Erweiterungen bestehender Objekte: ST-0219/ST-0220/ST-0221 → MEC-0009; ST-0222/ST-0223/ST-0224 → MEC-0021; ST-0225/ST-0226 → MEC-0023 (neu) und A-0050; ST-0229/ST-0230/ST-0231/ST-0232 → MEC-0002; ST-0235/ST-0236 → MEC-0018; ST-0238/ST-0239 → A-0008/A-0052; ST-0240/ST-0246 → MEC-0005/A-0051. Zwei Statements (ST-0241, ST-0242) tragen einen prominenten, doppelten Replikations-Warnhinweis (⚠⚠) und wurden explizit NICHT als P/MEC-Grundlage verwendet.

---

## 2. Neue Assumptions

**Anzahl:** 4
**IDs:** A-0050, A-0051, A-0052, A-0053

Jede neue Annahme trägt eine explizite Abgrenzungsbegründung (aus VAL-0012 Punkt 4 übernommen):

- **A-0050** (Null-Preis wird kategorial anders verarbeitet als jeder positive Preis): Abgrenzung zu A-0008 dokumentiert unterschiedliche Falsifizierungsbedingungen — A-0008 wäre falsch, wenn Wertwahrnehmung absolut statt relativ wäre; A-0050 wäre falsch, wenn der Nullpreis-Effekt sich als reiner Spezialfall der allgemeinen Relativitätslogik erweisen würde (rein graduell, ohne kategorialen Sprung). Da beide Bedingungen unabhängig voneinander verletzt sein können, ist A-0050 gemäß CKM §3.2 eigenständig, nicht als Unterfall von A-0008 zu führen. Grundlage für MEC-0023.
- **A-0051** (Marktnormen verdrängen Sozialnormen irreversibel): Abgrenzung zu MEC-0005 selbst dokumentiert — A-0051 ist eine zusätzliche, empirisch eigenständige PERSISTENZ-Eigenschaft (Irreversibilität des Crowding-out), nicht nur ein Restatement des in MEC-0005 dokumentierten Grenzbedingungs-Befunds (dass Reziprozität im Marktrahmen kollabiert). MEC-0005 beschreibt das Kollabieren selbst; A-0051 beschreibt dessen Nicht-Umkehrbarkeit als eigenständigen empirischen Zusatzbefund.
- **A-0052** (Preis wirkt kausal, nicht nur korrelativ, auf erlebte Wirkung): Explizit als Grenzfall diskutiert — enge Verwandtschaft zur A-0008-Erweiterung (beide beruhen auf denselben zwei Ariely-Preis-Placebo-Studien), aber unterschiedlicher Evidenztyp: A-0008 beschreibt primär einen Bewertungs-/Wahrnehmungseffekt, A-0052 postuliert einen kausalen Effekt auf die tatsächliche Erfahrung/Leistung (inkl. objektiv gemessener Aufgabenperformance im SoBe-Experiment). Beide Wege (Erweiterung von A-0008 UND Neuanlage A-0052) wurden aus Transparenzgründen parallel dokumentiert statt sich für nur einen zu entscheiden — als offener Restpunkt für eine künftige Herausgeber-Konsolidierung markiert (siehe Abschnitt 4).
- **A-0053** (Optionsverlust-Angst unabhängig von Besitz und Überlastung): Abgrenzung sowohl zu MEC-0002 (Verlustaversion, setzt reales Eigentum voraus) als auch zu MEC-0015 (Choice Overload, betrifft Entscheidungslähmung durch Informationsvolumen bei vielen Optionen) explizit dokumentiert — postuliert einen dritten, eigenständigen psychologischen Zustand (Angst vor Verlust des Zugriffsrechts selbst, auch bei nur einer bedrohten Option). Erfüllt jedoch nicht die CKM-Mindestschwelle für eine MEC-Neuanlage (nur ein Auftreten im aktuellen Codex-Bestand) — daher als A-Objekt mit Kandidatenstatus für Re-Prüfung bei B-0013 dokumentiert.

Zusätzlich wurde A-0008 erweitert (siehe Abschnitt 4).

---

## 3. Neue Mechanismen

**Anzahl:** 1
**ID:** MEC-0023 — "Zero-Preis-Effekt: Kategoriale Sonderverarbeitung von 'Kostenlos'"

### Canonicalization-Rejection-Begründung (vollständig, aus MEC-0023-Datei zusammengefasst)

Geprüfte bestehende Kandidaten: **MEC-0009 (Perzeptueller Kontrast)** und **MEC-0002 (Verlustaversion und Kosten des Status quo)**.

**CKM-Schritt 1 (Suche):** Beide sind naheliegende Kandidaten, da "kostenlos" sowohl mit Kontrastwahrnehmung (Preisvergleich) als auch mit Verlustvermeidung (kein Kaufrisiko bei Gratis-Angeboten) plausibel in Verbindung stehen könnte.

**CKM-Schritt 2 (Identitätsprüfung nach kausaler Struktur):**

| Merkmal | MEC-0009 (Perzeptueller Kontrast) | MEC-0002 (Verlustaversion) | MEC-0023 (Zero-Preis-Effekt) |
|---|---|---|---|
| Stimulus (X) | Vorangegangener/gleichzeitiger Vergleichsreiz (beliebiger Referenzpunkt) | Wahrgenommener potenzieller Verlust eines bereits vorhandenen oder in Aussicht stehenden Gutes | Spezifisch: Preis = exakt Null (kategorial, nicht graduell) |
| Prozess (Y) | Relative, kontinuierliche Kontrastwahrnehmung (Weber'sches Gesetz, graduell) | Verlustgewichtung ca. doppelt so stark wie Gewinngewichtung (kontinuierliche Wertfunktion, Prospect Theory) | Kategoriale Elimination des wahrgenommenen Verlustrisikos (Sprungfunktion, nicht Teil der kontinuierlichen Wertfunktion) |
| Reaktion (Z) | Graduell veränderte Bewertung proportional zur Kontraststärke | Graduell verstärkte Vermeidungsmotivation proportional zur Verlustgröße | Sprunghafte, disproportionale Präferenzänderung NUR am exakten Nullpunkt |
| Kernevidenz | Weber's Law, Decoy-Effekt-Experimente | Kahneman/Tversky 1979, Brown et al. 2024 Meta-Analyse | Shampanier/Mazar/Ariely 2007, Marketing Science |

**Entscheidender Beleg für die kausale Nicht-Identität:** Die Kontrollbedingungs-Logik ist zentral. Wäre der Zero-Preis-Effekt vollständig durch Kontrast (MEC-0009) erklärbar, müsste die Wirkung proportional zur absoluten Preisdifferenz skalieren — eine Senkung von **2 auf 1 Cent** sollte dann ähnlich stark wirken wie eine Senkung von **1 auf 0 Cent**, da beide Male die Differenz exakt 1 Cent beträgt. Shampanier/Mazar/Ariely widerlegen dies explizit durch genau diese Kontrollbedingung: Die 2→1-Cent-Senkung veränderte das Wahlverhalten kaum, während die 1→0-Cent-Senkung es dramatisch veränderte, obwohl die absolute Differenz identisch ist. Wäre der Effekt vollständig durch Verlustaversion (MEC-0002) erklärbar, müsste er kontinuierlich mit sinkendem Preis zunehmen (da das wahrgenommene Verlustrisiko kontinuierlich sinkt) — auch dies widerlegt die beobachtete Sprunghaftigkeit exakt am Nullpunkt.

**CKM-Schritt 3 (Qualitätsprüfung, alle vier Bedingungen erfüllt):**
1. Nicht bereits durch bestehendes Objekt abgedeckt — siehe Kontrastanalyse und 2→1-vs-1→0-Cent-Kontrollbedingung oben.
2. Eigenständiger erklärender Beitrag: Ja — kategoriale statt kontinuierliche Verarbeitung ist ein spezifischer, in der Literatur explizit als eigenständiges Phänomen behandelter Befund.
3. Mindestschwelle (≥2 unabhängige Auftreten als erklärende Kraft): Erfüllt — Hershey's-Kiss-Experiment, Halloween-Snickers-Experiment, Amazon-Gratisversand-Beispiel; zusätzlich unabhängig repliziert (Vosgerau et al., hedonische Produkte).
4. Keine bloße Umbenennung: Erfüllt — beschreibt eine andere, spezifischere Wirkform (kategorialer Sprung) als beide bestehenden MECs (kontinuierliche Prozesse).

**Ergebnis:** Alle vier Bedingungen erfüllt → Neuanlage gerechtfertigt. Evidenzlevel E3 (Primärstudie gut etabliert und mehrfach zitiert, mindestens eine unabhängige Replikationsstudie identifiziert; kein E4 mangels großer Multi-Labor-Replikation und ungetestetem B2B-Transfer).

**Keine weiteren neuen Mechanismen wurden angelegt.** Der Kandidat "Keeping Doors Open"/Optionsverlust-Angst (Kap. 8) wurde geprüft, ist strukturell eigenständig (weder MEC-0015 noch MEC-0002), erfüllt aber die CKM-Mindestschwelle (≥2 unabhängige Auftreten) nicht — als A-0053 mit Kandidatenstatus dokumentiert, nicht als MEC angelegt.

---

## 4. Erweiterte Objekte

**Anzahl:** 8 (5 MEC, 1 A, 1 P, 1 MOD)

| Objekt | Art der Erweiterung |
|---|---|
| MEC-0009 (Perzeptueller Kontrast) | Decoy-Effekt/Asymmetrische Dominanz (Huber/Payne/Puto 1982 als unabhängige Gründungsquelle vor Ariely) als spezifischere, choice-set-basierte Ausprägung desselben Kausalpfads ergänzt (Economist-Abo-, Foto-Dating-Experiment). Kein E-Level-Wechsel (E4/E3 bleibt bestehen). |
| MEC-0021 (Anchoring-Mechanismus) | Arbitrary-Coherence-Präzisierung ergänzt: ein einmaliger, sogar erkennbar willkürlicher Anker prägt dauerhaft alle nachfolgenden Bewertungen verwandter Produkte, nicht nur die unmittelbare Entscheidung. Erstmals mit vollständiger Primärquelle (Ariely, Loewenstein & Prelec 2003, QJE) statt nur sekundärer Bezugnahme. Kein E-Level-Wechsel. |
| MEC-0002 (Verlustaversion und Kosten des Status quo) | Endowment-Effekt als Anwendungsfall ergänzt: Duke-Basketballticket-Lotterie-Experiment (Carmon & Ariely 2000) als methodisch besonders starke, weil auf echter Zufallszuteilung beruhende Evidenzquelle. Drei-Quirks-Taxonomie (emotionale Verbundenheit, Verlustfokus, Perspektivübernahme-Fehler), Ikea-Effekt und virtuelles Eigentum bei Online-Auktionen ergänzt. Offene "mere ownership"-Debatte (Morewedge & Giblin 2015) transparent als Grenze dokumentiert, nicht aufgelöst. Kein E-Level-Wechsel. |
| MEC-0005 (Reziprozitätspflicht) | Neue Grenzbedingung ergänzt: Reziprozitätsnormen wirken nur innerhalb eines Social-Norm-Rahmens und kollabieren beim Eintritt eines Market-Norm-Rahmens (auch nur durch Erwähnung eines Geldbetrags, ohne tatsächlichen Geldfluss) — bislang im Codex nicht dokumentierte Randbedingung. Gneezy & Rustichini (2000) als Irreversibilitäts-Beleg ergänzt. Kein E-Level-Wechsel. |
| MEC-0018 (Pre-Suasion/attentionale Vorbereitung) | Neuronale Vertiefung ergänzt: Bier-Essig-, Kaffee-Ambiente- und Coke-Pepsi-fMRT-Experimente (McClure et al. 2004) zeigen, dass vorherige Erwartung nicht nur die Bewertung, sondern die tatsächliche sensorische/neuronale Verarbeitung der Erfahrung selbst verändert (VMPFC/DLPFC-Aktivierung). Kein E-Level-Wechsel. |
| A-0008 (Wahrnehmung von Wert ist relativ) | Erweiterung von einer primär korrelativ/heuristischen Preis-Qualitäts-These um kausale, teils objektiv gemessene experimentelle Evidenz (Veladone-Rx-Schmerzmittel-Experiment, SoBe-Wortpuzzle-Experiment mit objektivem Leistungsmaß; Waber/Shiv/Carmon/Ariely 2008, JAMA). Enge, dokumentierte Überschneidung mit der parallel neu angelegten A-0052 (siehe Abschnitt 2 und Restpunkte unten). Kein E-Level-Wechsel. |
| P-0042 (Ankerkontrolle im Preisgespräch) | Zeitliche Vertiefung ergänzt: Arbitrary-Coherence-Befund zur Dauerhaftigkeit des Erstankers über die gesamte Kundenbeziehung hinweg, nicht nur für die unmittelbare Preisverhandlung. Kein neues Prinzip nötig — reine Vertiefung eines bestehenden. Kein E-Level-Wechsel. |
| MOD-0010 (Kahneman Kognitive Bias-Karte) | Sechs neue Bias-Einträge in bestehende Kategorien 1 (Urteilsbildung: Decoy-Effekt, Erwartung prägt Erfahrung) und 2 (Numerische Schätzung/Preiswahrnehmung: Arbitrary Coherence, Zero-Preis-Effekt, Preis-Placebo-Kopplung) integriert, plus neue, thematisch kohärente fünfte Kategorie "Besitz- und Optionsverzerrungen" (Endowment-Effekt, Optionsverlust-Angst, Social-vs-Market-Norms-Kollaps). Keine MOD-0011-Neuanlage, da dies eine reine Container-Dopplung wäre (CKM §6 "zu allgemein"-Warnung korrekt angewendet und geprüft). Kein E-Level-Wechsel (E5 Grundbefunde / E3 Sales-Integration bleibt bestehen). |

---

## 5. Canonicalization Rate

**Berechnungsbasis (MEC-spezifisch, wie in SPR-0001/B-0011 definiert):**

- Neue MECs: 1 (MEC-0023)
- Erweiterte MECs: 5 (MEC-0009, MEC-0021, MEC-0002, MEC-0005, MEC-0018)
- **Canonicalization Rate B-0012 = 5 / (1 + 5) × 100 = 83,3%**

**Vergleich mit B-0011:** B-0011 (Emotional Intelligence) erreichte 75% (3 Extensions / 4 bearbeitete MECs). B-0012 übertrifft dies mit 83,3% (5 Extensions / 6 bearbeitete MECs) — der bislang höchste MEC-Canonicalization-Wert im gesamten Sprint "Behavioral Science Expansion" und deutlich über dem Sprint-1-Zielwert (≥60%, siehe canonicalization_report.md) sowie über dem Sprint-1-Höchstwert (B-0005: 67%). Dies ist ein noch stärkerer quantitativer Beleg für die Sprint-Priorität "wissenschaftliche Vertiefung statt Wachstum" als B-0011: Von sechs bearbeiteten Mechanismen wurde nur einer (MEC-0023) tatsächlich neu angelegt, und diese Neuanlage selbst ist durch eine besonders sorgfältig dokumentierte, zweifache Canonicalization-Rejection-Prüfung (gegen MEC-0009 UND MEC-0002, inkl. expliziter Kontrollbedingungs-Logik) gerechtfertigt.

**Codex-weite Rate (alle Objekttypen, informativ, nicht die primäre Kennzahl):** 8 Extensions / (41 Neue + 8 Extensions) × 100 = 16,3%. Niedriger als die MEC-spezifische Rate, methodisch erwartbar (siehe B-0011-Begründung: Statements — hier 31 von 41 Neuanlagen — werden per CKM-Definition immer neu angelegt, auch bei inhaltlicher Fundierung bestehender Objekte).

---

## 6. Neue Scientific Debt

Vollständig eingetragen in `00_project/SCIENTIFIC_DEBT.md`, Sektion "B-0012 — Predictably Irrational (SRC-0012)" (7 Einträge), inklusive einer neuen Kategorie "Autoren-Integritätsrisiko". Zusammenfassung:

| Objekt-ID | Kategorie | Priorität |
|---|---|---|
| ST-0241, ST-0242 (Ten-Commandments/Honor-Code) | Replikationsrisiko | **Hoch** — Verschuere et al. (2018) Registered Replication Report, 19 Labore, N=4.674, kein Effekt repliziert; Expression of Concern 2024 |
| SRC-0012 (Autor Dan Ariely, generell) | Autoren-Integritätsrisiko (neue Kategorie) | **Hoch** — 2021-Datenfälschungsvorwurf bei separater Studie ("The Signing Boosts Honesty", 2012 PNAS, 2021 zurückgezogen); differenzierte, werkspezifische Bewertung dokumentiert |
| A-0050, MEC-0023 (Zero-Preis-Effekt) | Externe Validierung ausstehend | Mittel — mind. eine externe Replikation (Vosgerau et al.), aber keine Multi-Labor-Replikation, kein B2B-Test |
| A-0052 (Preis-Placebo-Kausalität) | Externe Validierung ausstehend | Mittel — keine von Ariely unabhängige externe Replikation identifiziert |
| A-0053 (Optionsverlust-Angst) | Offene Forschungsfrage | Niedrig — CKM-Mindestschwelle für MEC-Anlage nicht erfüllt; Re-Prüfung bei B-0013 empfohlen |
| MEC-0002 (Erweiterung, Endowment-Effekt) | Widersprüchliche Evidenz (nicht aufgelöst) | Mittel — "mere ownership"-Debatte (Morewedge & Giblin 2015) offen |
| ST-0227 (Hot-Cold-Empathy-Gap) | Offene Forschungsfrage | Mittel — Stichprobe ausschließlich männliche Berkeley-Studierende (N=25), WEIRD-Bias |
| Durchgängig (alle B-0012-Objekte) | Kulturelle Generalisierung / Transferlücke | Hoch — B2C/US-Universitätsstudierenden-Bias durchgängig, direkter B2B-Vertriebstransfer in keinem Experiment getestet |

---

## 7. Neue Literaturquellen

Vollständig eingetragen in `05_research/LITERATURE_INDEX.md`, Abschnitt A (Entscheidungspsychologie & Behavioral Economics) und Abschnitt B (Sozialpsychologie), mit Verweis auf die Ariely-2021-Retraction als Kontext-/Bemerkungseintrag (nicht als eigene stützende Quelle, da zurückgezogen). Zusammenfassung:

| APA-Zitation | Verifikationsstatus | Unterstützt |
|---|---|---|
| Huber, J., Payne, J.W. & Puto, C. (1982). Adding Asymmetrically Dominated Alternatives: Violations of Regularity and the Similarity Hypothesis. *Journal of Consumer Research*, 9(1), 90–98. | Verifiziert (2026-07-02) | MEC-0009 (Erweiterung), P-0045, T-0043 |
| Kahneman, D., Knetsch, J.L. & Thaler, R.H. (1990). Experimental Tests of the Endowment Effect and the Coase Theorem. *Journal of Political Economy*, 98(6), 1325–1348. | Verifiziert (2026-07-02) — bereits als Grundlagenquelle etabliert | MEC-0002 (Erweiterung) |
| Carmon, Z. & Ariely, D. (2000). Focusing on the Forgone: How Value Can Appear So Different to Buyers and Sellers. *Journal of Consumer Research*, 27(3), 360–370. | Verifiziert (2026-07-02) | MEC-0002 (Erweiterung, Duke-Ticket-Studie) |
| Ariely, D., Loewenstein, G. & Prelec, D. (2003). "Coherent Arbitrariness": Stable Demand Curves Without Stable Preferences. *Quarterly Journal of Economics*, 118(1), 73–105. | Verifiziert (2026-07-02) | MEC-0021 (Erweiterung), P-0042 (Erweiterung) |
| Shampanier, K., Mazar, N. & Ariely, D. (2007). Zero as a Special Price: The True Value of Free Products. *Marketing Science*, 26(6), 742–757. | Verifiziert (2026-07-02) | MEC-0023 (neu), A-0050, P-0046 |
| Vosgerau, J. et al. Free Indulgences: Enhanced Zero-Price Effect for Hedonic Options (zitiert in Sekundärliteratur, ScienceDirect). | Websuchverifiziert (2026-07-02) über Sekundärquelle — vollständige Erstautorenangabe/Jahr nicht mit letzter Sicherheit bestätigt | MEC-0023 (unabhängige Replikationsstudie, hedonische Produkte) |
| McClure, S.M. et al. (2004). Neural Correlates of Behavioral Preference for Culturally Familiar Drinks. *Neuron*, 44(2), 379–387. | Verifiziert (2026-07-02) | MEC-0018 (Erweiterung, Coke-Pepsi-fMRT-Studie) |
| Gneezy, U. & Rustichini, A. (2000). A Fine is a Price. *Journal of Legal Studies*, 29(1), 1–17. | Verifiziert (2026-07-02) — Standardzitation des Tageskrippen-Bußgeld-Befunds | MEC-0005 (Erweiterung), A-0051, P-0047 |
| Waber, R.L., Shiv, B., Carmon, Z. & Ariely, D. (2008). Commercial Features of Placebo and Therapeutic Efficacy. *JAMA*, 299(9), 1016–1017. | Verifiziert (2026-07-02) | A-0008 (Erweiterung), A-0052 |
| Verschuere, B. et al. (2018). Registered Replication Report on Mazar, Amir, and Ariely (2008). *Advances in Methods and Practices in Psychological Science*, 1(3), 299–317. | Verifiziert (2026-07-02) — 19 Labore, N=4.674, Originaleffekt nicht repliziert | ST-0241, ST-0242 (Replikations-Warnhinweis, explizit NICHT als P/MEC-Grundlage) |

**Nicht als stützende Quelle, sondern als Kontext/Retraction dokumentiert:** Shu, K., Mazar, N., Gino, F., Ariely, D. & Bazerman, M.H. (2012). Signing at the Beginning Makes Ethics Salient and Decreases Dishonest Self-Reports in Comparison to Signing at the End. *PNAS*, 109(38), 15197–15200. — **2021 ZURÜCKGEZOGEN** wegen nachgewiesener Datenfälschung (Data-Colada-Untersuchung identifizierte Ariely als Ersteller der fabrizierten Datentabelle). Diese Publikation ist explizit KEINE Quelle für dieses Buch (2008/2009 publiziert, die betroffene Studie erschien erst 2012) und wird im Literaturindex nicht als unterstützende Referenz für ein Codex-Objekt geführt, sondern ausschließlich im Bemerkungsfeld als Kontext für die Autoren-Integritätsrisiko-Einordnung dokumentiert (siehe SCIENTIFIC_DEBT.md, Abschnitt 6).

**Nicht bibliografisch vollständig verifizierbar (offene Frage, nicht erfunden):** Clark, M.S., Mills, J. & Fiske, A.P. (Social Norms vs. Market Norms als getrennte Beziehungsdomänen) — im Ariely-Text erwähnt, vollständige Einzelzitation (Jahr, Journal) im Fließtext nicht angegeben und über WebSearch nicht mit ausreichender Sicherheit auffindbar. In der MEC-0005-Erweiterung als offene Frage markiert statt spekulativ zitiert.

---

## 8. Publikationsbias-Risiken

Struktur wie VAL-0012 Punkt 6, hier als eigenständiger Berichtsabschnitt mit drei klar getrennten Ebenen:

1. **Ariely-Datenfälschungsskandal 2021 (separates Werk, außerhalb dieses Buches):** Betrifft die 2012 in PNAS publizierte, 2021 zurückgezogene Studie "The Signing Boosts Honesty" (Shu, Mazar, Gino, Ariely, Bazerman) — NICHT Teil von SRC-0012 (Predictably Irrational, 2008/2009). Data-Colada-Untersuchung identifizierte Ariely als Ersteller der fabrizierten Datentabelle (Metadaten-Analyse einer 2011 versendeten Excel-Datei). Ariely bestreitet vorsätzliche Fälschung, räumt aber mangelnde Prüfung der Daten ein. Zusätzliche Kontroversen: 2021 Expression of Concern zu einer 2004 co-autorierten Studie (Heyman & Ariely, statistische Fehler); 2022 richtete Duke University verstärkte Aufsicht über Arielys Forschungszentrum ein. Sauber getrennt von den in diesem Buch beschriebenen Experimenten dokumentiert.
2. **Ten-Commandments-Replikationsfehlschlag (direkt DIESES Buch betreffend, Kap. 11):** Ein eigenständiger, über den ursprünglich erwarteten Scope hinausgehender, aber Priorität-2-relevanter Befund. Das im Buch selbst beschriebene Ten-Commandments-Experiment (Mazar, Amir & Ariely 2008) wurde durch Verschuere et al. (2018) NICHT repliziert; die Originalstudie erhielt 2024 zusätzlich ein Expression of Concern. Dies ist kategorial verschieden von Punkt 1 (separates Werk, keine Fälschungsvorwurf, sondern Nicht-Replikation + methodischer Vorbehalt) — explizit als eigener, prominent markierter Scientific-Debt-Eintrag geführt.
3. **Unabhängig replizierte/fundierte Kernbefunde:** Decoy-Effekt (Huber/Payne/Puto 1982, vor Ariely, unabhängige Gründungsquelle), Endowment-Effekt (Kahneman/Knetsch/Thaler 1990/1991, unabhängige Forschungsgruppe), Anchoring (Tversky/Kahneman 1974, unabhängige Gründungsquelle), Zero-Preis-Effekt (mind. eine externe Replikation, Vosgerau et al.) — diese sind überwiegend unabhängig von der Ariely-Integritätsfrage abgesichert und bilden das tragende Gerüst der in dieser Buchanalyse vorgenommenen MEC-Erweiterungen und der MEC-0023-Neuanlage.

**Sauberkeit der Trennung:** Kein Statement/Objekt in dieser Buchanalyse überträgt den 2021-Skandal oder den Ten-Commandments-Replikationsfehlschlag pauschal auf andere Ariely-Befunde — jede Erweiterung/Neuanlage prüft ihre jeweilige spezifische Evidenzbasis eigenständig (siehe Abschnitte 3/4 oben und VAL-0012 Punkt 6).

---

## 9. Neue Tier-1-Kandidaten (nur Dokumentation, keine Eintragung)

Gemäß Auftrag: Diese Quellen werden hier nur als mögliche Kandidaten für `00_project/ACADEMIC_RECOVERY_PLAN.md` dokumentiert — eine tatsächliche Eintragung dort ist außerhalb des Scopes dieser Buchanalyse.

- **Shampanier, Mazar & Ariely (2007) — Zero as a Special Price:** Starker Kandidat für Tier-1. Eine der meistzitierten Marketing-Science-Publikationen ihres Jahrgangs, mit klarer, prüfbarer kategorialer Kausalstruktur (Kontrollbedingungslogik 2→1 vs. 1→0 Cent) und mindestens einer unabhängigen Replikationsstudie (Vosgerau et al.). Würde MEC-0023 von E3 auf potenziell E4 heben, falls eine große Multi-Labor-Replikation (analog Schley & Weingarten 2023 für Anchoring) identifiziert werden kann.
- **Huber, Payne & Puto (1982) — Asymmetrische Dominanz:** Mittlerer bis starker Kandidat — Gründungsarbeit des Decoy-Effekts, unabhängig von Ariely, breit in der Marketing-/Konsumentenforschung rezipiert. Tier-1-Einstufung würde die Evidenzbasis von MEC-0009 zusätzlich zur bestehenden Cialdini-Fundierung stärken.
- **Kahneman, Knetsch & Thaler (1990/1991) — Endowment-Effekt:** Mittlerer Kandidat — bereits als Grundlagenquelle für MEC-0002 etabliert; eine Tier-1-Prüfung müsste klären, ob eine aktuelle Meta-Analyse zur Endowment-Effekt-Größe existiert (analog Brown et al. 2024 für Verlustaversion allgemein), was in diesem Sprint nicht durchgeführt wurde.

---

## Status

Abgeschlossen — 2026-07-02
