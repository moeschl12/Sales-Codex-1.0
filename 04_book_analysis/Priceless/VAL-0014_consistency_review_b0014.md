# VAL-0014 -- Konsistenzpruefung B-0014 (Priceless: The Myth of Fair Value)

## Pruefungs-ID

VAL-0014

## Buch

B-0014 -- Priceless: The Myth of Fair Value (and How to Take Advantage of It) (Poundstone 2010)

## Datum

2026-07-02

## Pruefumfang

Alle Knowledge Objects aus B-0014:
- SRC-0014 (1 neue Quelle)
- ST-0267 bis ST-0286 (20 Statements)
- A-0056 (1 neue Assumption)
- A-0048 (1 Erweiterung)
- MEC-0025 (1 neuer Mechanismus)
- MEC-0021, MEC-0009 (2 Erweiterungen)
- P-0051 (1 neues Prinzip)
- P-0042, P-0014 (2 Erweiterungen)
- T-0046 (1 neue Technik)
- MOD-0010 (1 Erweiterung, neue Kategorie 6)

---

## Pruefpunkte

### 1. ID-Konsistenz

Alle neuen IDs im zugewiesenen Bereich verifiziert per Verzeichnis-Listing: ST-0267-ST-0286 (lueckenlos, 20 Objekte), A-0056 (naechste freie ID nach A-0055), MEC-0025 (naechste freie ID nach MEC-0024), P-0051 (naechste freie ID nach P-0050), T-0046 (naechste freie ID nach T-0045), keine neue MOD-ID vergeben (MOD-0010 erweitert statt MOD-0012 neu angelegt, siehe Punkt 4). Keine Doppelbelegungen, keine Luecken. EXTEND-Operationen auf MEC-0021, MEC-0009, A-0048, P-0042, P-0014, MOD-0010 korrekt als Erweiterungsabschnitte (nicht als neue Dateien) durchgefuehrt. Ausgangs-ID-Bereich (ST-0267, A-0056, MEC-0025, P-0051, T-0046, MOD-0012, SRC-0014, VAL-0014) stimmte mit unabhaengiger Bash-Verifikation zu Sprintbeginn ueberein; MOD-0012 wurde bewusst NICHT vergeben (siehe Punkt 4), daher bleibt diese ID fuer den naechsten Buchschritt (B-0015) offen.

**Ergebnis: PASS**

### 2. Quellenzuordnung

Alle neuen Objekte referenzieren SRC-0014 als Source ID. Externe Primaerquellen innerhalb des Buchs korrekt als Sekundaerzitate ausgewiesen und, soweit moeglich, per WebSearch verifiziert (Northcraft & Neale 1987, Oosterbeek/Sloof/van de Kuilen 2004, Sanfey et al. 2003, Guth/Schmittberger/Schwarze 1982, Kahneman/Knetsch/Thaler 1986, Mussweiler/Strack/Pfeiffer 2000, Chapman & Bornstein 1996, Shafir/Diamond/Tversky 1997, Stevens 1957, Henrich et al. 2001/2004, Oechssler/Roider/Schmitz 2008/2009). Alle ueber WebSearch verifizierten Quellenangaben sind explizit mit Verifikationsstatus markiert. Nicht auffindbare oder unsichere bibliografische Details sind als offene Frage dokumentiert statt erfunden (z. B. exakte "Barr Scale"-Validierung, exakte Replikationszahl fuer Stevens' Machtgesetz-Kritik).

**Ergebnis: PASS**

### 3. Evidenzklassen-Vergabe

| Objekt | Vergabe | Angemessenheit |
|---|---|---|
| MEC-0025 (Fairness-Verzicht, neu) | E4 | Korrekt: Ultimatum-Spiel-Grundphaenomen durch Metaanalyse (37 Studien) gestuetzt; spezifische neuronale Fundierung (Sanfey et al.) separat als E3 ausgewiesen |
| A-0056 (Fairness-Normverletzung motiviert Bestrafung) | E4 (Grundphaenomen) / E3 (neuronale Stuetzung) | Korrekt gestaffelt, keine Vermischung der Evidenzstufen |
| P-0051 (Fairness-Schwelle beachten) | E4 | Korrekt: Basis MEC-0025 (E4), B2B-Transfer explizit als Codex-eigene Extrapolation gekennzeichnet, kein Evidenz-Upgrade fuer die Transfer-Annahme |
| MEC-0021, MEC-0009 (Erweiterungen) | kein E-Level-Wechsel | Korrekt: beide Erweiterungen vertiefen/fundieren die bestehende Evidenzbasis (Primaerquellen-Rekonstruktion bzw. psychophysikalische Fundierung), ohne dass neue Feldbelege eine Aufwertung rechtfertigen wuerden |
| A-0048, P-0042 (Erweiterungen) | Teilweiser E-Level-Anstieg (Ritov-Komponente) | Korrekt begruendet: Ritov 1996 schliesst eine zuvor explizit als "normativ, nicht empirisch gemessen" dokumentierte Luecke mit einem kontrollierten Experiment (E3) -- Anstieg nur fuer die Erstangebots-Teilkomponente, nicht fuer das Gesamtprinzip |
| T-0046 (Consider-the-Opposite) | E3 | Korrekt: zwei unabhaengige Anwendungskontexte (Kfz-Mechaniker-Studie, Wuerzburg-Prognoseaufgabe), aber keine grosse Multi-Labor-Replikation bekannt |

**Ergebnis: PASS**

### 4. Kanonisierungs-Konsistenz

EXTEND-Entscheidungen geprueft:
- MEC-0021 EXTEND (Primaerquellen-Vertiefung, Robustheitsnachweise, Preference Reversal, Money Illusion): Korrekt -- identischer Kausalpfad (S1-Priming + S2-Adjustment) fuer alle neuen Belege bestaetigt; Preference Reversal und Money Illusion explizit gepruefte und VERWORFENE Kandidaten fuer eigene MECs, stattdessen hier eingeordnet (Money Illusion zusaetzlich durch explizite Selbsteinordnung der Originalautoren als "a form of anchoring" gestuetzt).
- MEC-0009 EXTEND (Psychophysikalische Grundlagen): Korrekt -- reine wissenschaftliche Fundierung des bereits bestehenden Kausalpfads (Weber/Fechner/Stevens), keine neue Kausalstruktur. Wichtige Klaerung der zuvor offenen Frage zur Helson/Tversky-Kahneman-Begriffsverwandtschaft vollstaendig dokumentiert und im Bestand als beantwortet markiert.
- A-0048 EXTEND (Ritov-Erstangebotsvorteil): Korrekt -- schliesst die im Bestand selbst dokumentierte Evidenzluecke empirisch, ohne die Kernannahme zu veraendern.
- P-0042 EXTEND (Ritov, Chapman & Bornstein): Korrekt -- direkte empirische Stuetzung von Umsetzungsrichtlinie 2 (extreme Eroeffnung), inklusive Widerlegung der "Boomerang-Effekt"-Gegenhypothese.
- P-0014 EXTEND (Offene-Frage-Schliessung): Korrekt -- keine inhaltliche Erweiterung noetig, nur Verweis auf die in MEC-0009 dokumentierte Klaerung.
- MOD-0010 EXTEND (Kategorie 2 vertieft, neue Kategorie 6): Korrekt -- vollstaendige Begruendung, warum eine neue Kategorie (nicht Einordnung in Kategorien 1-5) erforderlich ist (sozial-normative vs. individuell-kognitive Prozesse), mit expliziter Abgrenzung zur bereits bestehenden Kategorie 5.

NEU-Entscheidungen geprueft:
- MEC-0025 (Fairness-Verzicht): Vollstaendige Canonicalization-Rejection-Pruefung gegen MEC-0002 und MEC-0009 durchgefuehrt und dokumentiert (in MEC-0025 selbst UND in analysis.md). Kernunterschied zu MEC-0002: Ablehnung eines strikt positiven Gewinns ist keine Verlustvermeidung, sondern aktive Gewinnaufopferung -- durch die Grundstruktur des Ultimatum-Spiels selbst beweisbar. Kernunterschied zu MEC-0009: erfordert intentionalen sozialen Akteur und aktive Sanktionsmotivation, kein rein perzeptuelles Phaenomen -- durch qualitativ unterschiedliche neuronale Korrelate (Insula-Aktivierung) gestuetzt. Alle vier CKM-Bedingungen fuer MEC-Neuanlage erfuellt und einzeln durchdekliniert. **NEU gerechtfertigt.**
- A-0056 (neue Annahme): Explizite Abgrenzung zu MEC-0002 (Verlustaversion) dokumentiert, direkte Anbindung an MEC-0025. **NEU gerechtfertigt.**
- P-0051 (neues Prinzip): Erfuellt die OR-Regel (A6, task_rules.md Sec. 10.4) durch Kombination MEC-0025 + A-0056 (+ Querverweis MEC-0002 zur Abgrenzung/Interaktion). Vollstaendiger Quervergleich mit P-0042 und P-0014 dokumentiert, inklusive explizit benanntem Spannungsverhaeltnis zu P-0042 (extremes Anchoring kann selbst als Fairness-Verstoss wahrgenommen werden). **NEU gerechtfertigt.**
- T-0046 (neue Technik): Erfuellt Technik-Kriterien (konkrete, wiederholbare Handlung -- aktive Gegenargument-Suche vor eigener Zahlennennung -- mit definierten Ausloese-/Abschlussbedingungen), klar von P-0042 unterscheidbar (Kehrseite: Selbstschutz statt Fremdbeeinflussung), mit explizitem Ethisches-Risiko-Feld (Risiko: keines). **NEU gerechtfertigt.**
- Kein neues MOD-Objekt (MOD-0012 NICHT vergeben): Gepruefte Alternative war eine eigene "Preispsychologie/Fairness-Verhandlungs-Modell"-Neuanlage. Entscheidung: Erweiterung von MOD-0010 um Kategorie 6 ist CKM-konform (keine Container-Dopplung, thematische Kohaerenz mit dem "kognitive Bias-Landkarte"-Rahmen bleibt gewahrt, da Fairness-Verzicht ein Kahneman/Sanfey-nahes verhaltenswissenschaftliches Phaenomen ist). Explizite Begruendung in MOD-0010 selbst dokumentiert. **Korrekt keine Neuanlage.**
- Preference Reversal als eigener MEC: Geprueft und VERWORFEN -- identischer Kausalpfad wie MEC-0021 Pfad 1 (Bewertungsmodus wirkt als Anker/Kompatibilitaetsfilter), kein eigenstaendiger Mechanismus. Korrekt als MEC-0021-Erweiterung dokumentiert.
- Money Illusion als eigener MEC: Geprueft und VERWORFEN -- von den Originalautoren selbst explizit als "a form of anchoring" bezeichnet; Unterfall von MEC-0021 Pfad 2. Korrekt als MEC-0021-Erweiterung dokumentiert.
- Testosteron/Oxytocin-Hormonforschung als MEC oder T: Geprueft und VERWORFEN -- methodisch schwach (kleine Stichproben), ausserhalb legitimer Verkaeufer-Einflussnahme, zusaetzlich durch die im Buch selbst dokumentierte "Liquid Trust"-Produktkritik als Missbrauchsrisiko belegt. Nur als Statement (ST-0284) mit explizitem Ethik-Warnhinweis dokumentiert, keine Ueberfuehrung in anwendbare Objekte.
- Gender-/Rassendiskriminierung beim Autoverkauf als Technik: Geprueft und VERWORFEN -- beschreibt ein Diskriminierungsphaenomen bei Verkaeufern, keine anwendbare oder ethisch vertretbare Vertriebstechnik; in vielen Rechtsordnungen illegal. Nur als Statement (ST-0283) mit explizitem Ethik-Warnhinweis dokumentiert.
- Zero-Preis-Konvergenz (Shampanier/Mazar/Ariely erneut zitiert): Geprueft -- Priceless zitiert dieselbe Studie wie bereits MEC-0023 (aus B-0012). Keine neue Evidenz, keine Erweiterung von MEC-0023 vorgenommen, nur als Konvergenz-Statement (ST-0282) dokumentiert, um Doppelzaehlung in der Evidenzbasis zu vermeiden.

**Ergebnis: PASS**

### 5. Nicht-Anlage-Dokumentation (CKM Sec. 9)

Geprueft: Alle sechs verworfenen Kandidaten (Preference Reversal als MEC, Money Illusion als MEC, Testosteron/Oxytocin als MEC/T, Gender-/Rassendiskriminierung als T, MOD-0012-Neuanlage, Zero-Preis-Konvergenz als MEC-0023-Erweiterung) sind mit expliziter Begruendung in analysis.md ("Verworfene Kandidaten") UND, soweit zutreffend, im jeweiligen "parent"-Objekt (MEC-0021, MEC-0023, MOD-0010) dokumentiert.

**Ergebnis: PASS**

### 6. Replikations-/Publikationsbias-Dokumentation (Sprint-Prioritaet 2)

- **Ultimatum-Spiel-Grundphaenomen:** Metaanalyse Oosterbeek/Sloof/van de Kuilen (2004, 37 Studien, 75 Ergebnisse) WebSearch-verifiziert -- eines der am robustesten replizierten Befunde der Verhaltensoekonomie, in MEC-0025 explizit als E4-Grundlage dokumentiert.
- **Sanfey et al. (2003) fMRI-Studie:** Als Einzelstudie (E3) korrekt NICHT auf E4/E5 hochgestuft, trotz haeufiger Nachfolgezitation -- konservative Einstufung dokumentiert.
- **Northcraft & Neale (1987):** WebSearch-verifizierte Korrelationswerte (r=0.41 Experten, r=0.48 Laien) aus Sekundaerzitationen ergaenzt, mit Hinweis auf den Sekundaerquellen-Charakter der exakten Korrelationswerte.
- **Stevens' Machtgesetz (1957):** WebSearch-verifizierte spaetere Methodenkritik (Magnitude-Estimation-Technik) explizit dokumentiert, relativiert die exakte Exponenten-Allgemeingueltigkeit, ohne den Grundbefund zu widerlegen -- Publication-Bias-Risiko als gering eingestuft, da die Kritik methodisch, nicht auf Nicht-Publikation negativer Ergebnisse basiert.
- **Kulturelle Generalisierbarkeit (Henrich et al.):** Explizit als Grenzbedingung in MEC-0025, A-0056, P-0051 dokumentiert -- das Grundphaenomen ist NICHT universell, sondern an Marktoekonomie-Einbindung gekoppelt. Dies ist die wichtigste Boundary-Conditions-Erkenntnis dieser Buchanalyse.
- **B2B-Transfer-Luecke:** Durchgaengig in jedem neuen/erweiterten Objekt als Grenze markiert -- kein Experiment im Buch testet direkten B2B-Vertriebstransfer; Ritov (1996) und die Ultimatum-Spiel-Forschung basieren auf Labor-/Studierendenstichproben.
- **Testosteron/Oxytocin-Forschung:** Kleine Stichproben (N=26 bzw. vergleichbar) explizit als methodische Schwaeche benannt, zusaetzlich mit dokumentiertem Missbrauchsbeispiel (Liquid Trust) -- angemessen konservative, warnende Behandlung statt unkritischer Uebernahme.

**Ergebnis: PASS**

### 7. Grenzen-Dokumentation

Alle neuen/erweiterten Objekte enthalten Grenzen-Abschnitte. Kulturelle Generalisierbarkeitsgrenze (MEC-0025) und B2B-Transfer-Luecke werden durchgaengig als offene Fragen markiert. Spannungsverhaeltnis zwischen P-0051 und P-0042 (Fairness-Schwelle vs. extremes Anchoring) ist als explizite Grenzbedingung in beiden Objekten kreuzreferenziert.

**Ergebnis: PASS**

### 8. Ethisches Risiko (neue T/P-Objekte)

- P-0051 (Fairness-Schwelle beachten): niedrig als Warnprinzip, mittel bis hoch bei bewusster Invertierung ("Sucker-Pricing") -- explizit als nicht empfohlen markiert, mit Verweis auf ST-0283 als Negativbeispiel
- T-0046 (Consider-the-Opposite): keines -- reine Selbstschutz-/Selbstregulationstechnik, uneingeschraenkt empfohlen
- ST-0283 (Diskriminierungsstudie) und ST-0284 (Hormonforschung): beide mit explizitem, eigenstaendigem Ethik-Warnhinweis im Statement selbst versehen, bewusst NICHT in Techniken oder Prinzipien ueberfuehrt

Alle explizit markiert und begruendet.

**Ergebnis: PASS**

### 9. Beobachtung/Interpretation-Trennung in Statements

Stichprobenpruefung (ST-0267, ST-0275, ST-0279, ST-0281, ST-0283, ST-0285): Alle folgen dem Statement-Template mit getrennten Feldern fuer Originalaussage/Paraphrase (Beobachtung) und Moegliche Annahmen/Prinzipien (Interpretation). ST-0281 (Money Illusion) zusaetzlich mit explizitem Hinweis, dass die "Anchoring-Form"-Einordnung eine Aussage der Originalautoren selbst ist, nicht Codex-Interpretation.

**Ergebnis: PASS**

### 10. Freitext-Mechanismenreferenzen

Geprueft: Alle Mechanismus-Verweise in P-0051, T-0046 sowie in allen MEC-/A-/P-Erweiterungen nutzen ausschliesslich existierende MEC-IDs (MEC-0002, MEC-0009, MEC-0021, MEC-0025), keine Freitext-Mechanismen.

**Ergebnis: PASS**

---

## Bekannte Restpunkte (nicht blockierend)

- MEC-0021 enthaelt weiterhin die bereits vor B-0013 dokumentierte Repository-Anomalie (abgeschnittener Abschnitt "Erweiterung: Meta-analytische B") -- unveraendert, ausserhalb des Scopes dieser Buchanalyse, bereits in VAL-0013 dokumentiert.
- Die exakte Validierungsmethodik der im Buch erwaehnten "Barr Scale" (informelle Experteneinschaetzung zur kulturellen Fairness-Norm-Staerke) bleibt unklar -- als offene Frage in ST-0285 und MEC-0025 dokumentiert, nicht spekulativ vervollstaendigt.
- Die Interaktion zwischen MEC-0025 (Fairness-Verzicht) und MEC-0002 (Verlustaversion) in Situationen, in denen beide gleichzeitig aktiviert werden koennten, ist theoretisch plausibel, aber nicht empirisch getrennt untersucht -- als offene Frage in MEC-0025 dokumentiert.
- Kein MOD-0012 in diesem Buchschritt vergeben -- die ID bleibt fuer B-0015 oder spaetere Buecher offen, sollte dort ein CKM-konformer Bedarf entstehen.

## Gesamtergebnis

**STATUS: BESTANDEN -- keine Blocker**

Alle 10 Pruefpunkte bestanden. 6 EXTEND-Operationen korrekt durchgefuehrt (MEC-0021, MEC-0009, A-0048, P-0042, P-0014, MOD-0010), 1 neuer MEC mit vollstaendiger Canonicalization-Rejection-Begruendung (MEC-0025), 1 neues A-Objekt mit expliziter Abgrenzung (A-0056), 1 neues P-Objekt (OR-Regel erfuellt: MEC-0025 + A-0056, P-0051), 1 neues T-Objekt mit vollstaendiger ethischer Risikobewertung (T-0046), 20 neue ST, 6 Kandidaten explizit verworfen und dokumentiert (davon 2 mit explizitem Ethik-Warnhinweis statt Ueberfuehrung in anwendbare Technik). Scientific Debt und Publikationsbias-Risiken -- einschliesslich der kulturellen Generalisierbarkeitsgrenze des Ultimatum-Spiel-Grundphaenomens und der durchgaengigen B2B-Transfer-Luecke -- korrekt identifiziert, differenziert dargestellt und transparent markiert.

## Status

Abgeschlossen -- 2026-07-02
