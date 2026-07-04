# VAL-0012 — Konsistenzprüfung B-0012 (Predictably Irrational)

## Prüfungs-ID

VAL-0012

## Buch

B-0012 — Predictably Irrational: The Hidden Forces That Shape Our Decisions (Ariely 2008/2009, Revised and Expanded Edition)

## Datum

2026-07-02

## Prüfumfang

Alle Knowledge Objects aus B-0012:
- SRC-0012 (1 neue Quelle)
- ST-0218 bis ST-0248 (31 Statements)
- A-0050 bis A-0053 (4 neue Assumptions)
- A-0008 (1 Erweiterung)
- MEC-0023 (1 neuer Mechanismus)
- MEC-0009, MEC-0021, MEC-0002, MEC-0005, MEC-0018 (5 Erweiterungen)
- P-0045, P-0046, P-0047 (3 neue Prinzipien)
- P-0042 (1 Erweiterung)
- T-0043 (1 neue Technik)
- MOD-0010 (1 Erweiterung, keine MOD-0011-Neuanlage — geprüft und begründet abgelehnt)

---

## Prüfpunkte

### 1. ID-Konsistenz

Alle neuen IDs im zugewiesenen Bereich: ST-0218–ST-0248 (lückenlos, 31 Objekte, verifiziert per Verzeichnis-Listing), A-0050–A-0053 (4 Objekte, nächste freie IDs nach A-0049), MEC-0023 (nächste freie ID nach MEC-0022), P-0045–P-0047 (nächste freie IDs nach P-0044), T-0043 (nächste freie ID nach T-0042). Keine Doppelbelegungen, keine Lücken. EXTEND-Operationen auf MEC-0009, MEC-0021, MEC-0002, MEC-0005, MEC-0018, A-0008, P-0042, MOD-0010 korrekt als Erweiterungsabschnitte (nicht als neue Dateien) durchgeführt.

**Ergebnis: PASS**

### 2. Quellenzuordnung

Alle neuen Objekte referenzieren SRC-0012 als Source ID (bzw. Quelle-Feld bei älteren Template-Varianten). Externe Primärquellen innerhalb des Buchs korrekt als Sekundärzitate ausgewiesen (Huber/Payne/Puto 1982, Kahneman/Knetsch/Thaler 1990/1991, McClure et al. 2004, Gneezy & Rustichini 2000, Tversky/Kahneman Stift-Anzug-Studie). Alle über WebSearch verifizierten Quellenangaben sind explizit als "websuchverifiziert" mit Datum (2026-07-02) markiert. Nicht auffindbare oder unsichere bibliografische Details sind als offene Frage dokumentiert statt erfunden (z. B. Clark/Mills/Fiske-Vollzitation in MEC-0005-Erweiterung).

**Ergebnis: PASS**

### 3. Evidenzklassen-Vergabe

| Objekt | Vergabe | Angemessenheit |
|---|---|---|
| ST-0219 (Decoy Economist-Experiment) | — (Statement, keine E-Klasse im Template) | Korrekt gemäß Statement-Template |
| MEC-0023 (Zero-Preis-Effekt, neu) | E3 | Korrekt: Primärstudie gut etabliert und zitiert, mind. eine unabhängige Replikations-/Erweiterungsstudie (Vosgerau et al.), aber keine große Multi-Labor-Replikation bekannt, kein B2B-Test |
| ST-0241/ST-0242 (Ten-Commandments/Honor-Code) | geprüft mit ⚠⚠ | Korrekt mit doppeltem Warnhinweis (gescheiterte Großreplikation Verschuere et al. 2018 UND Expression of Concern 2024) — explizit NICHT als P/MEC-Grundlage verwendet |
| A-0050 (Zero-Preis kategorial) | E3 | Korrekt begründet: Primärstudie + eine Replikation, kein B2B-Test |
| A-0052 (Preis wirkt kausal auf Erfahrung) | E3 | Korrekt: zwei Paradigmen derselben Forschungsgruppe, keine externe Replikation dieser spezifischen Studien identifiziert |
| A-0053 (Optionsverlust-Angst) | E2 | Korrekt konservativ eingestuft: einzelne, aber methodisch robuste Studie ohne externe Replikation |
| MEC-0009/MEC-0021/MEC-0002/MEC-0005/MEC-0018 (Erweiterungen) | kein E-Level-Wechsel | Korrekt: alle Erweiterungen vertiefen bestehende Evidenzbasis, ohne die Kategorie zu verändern (explizit in jeder Erweiterung vermerkt) |

**Ergebnis: PASS** — alle unsicheren/umstrittenen Befunde tragen ⚠-Markierung statt unkritischer Übernahme; der schwerwiegendste Befund (Ten-Commandments-Replikationsfehlschlag) ist besonders prominent (⚠⚠) markiert und konsequent von jeglicher P/MEC-Verwendung ausgeschlossen.

### 4. Kanonisierungs-Konsistenz

EXTEND-Entscheidungen geprüft:
- MEC-0009 EXTEND (Decoy-Effekt): Korrekt — Kausalpfad identisch (X=Vergleichsreiz, Y=Kontrastwahrnehmung, Z=veränderte Bewertung), Huber/Payne/Puto 1982 als unabhängige, von Ariely getrennte Gründungsquelle bestätigt Konvergenz. Kein E-Level-Wechsel.
- MEC-0021 EXTEND (Arbitrary Coherence): Korrekt — identischer S1/S2-Kausalpfad, Ariely liefert zeitliche/kategoriale Vertiefung (Dauerhaftigkeit über Produktkategorien). Bereits vorher als "kanonisches Experiment" sekundär zitiert, jetzt mit Primärquelle (Ariely/Loewenstein/Prelec 2003, QJE) vertieft. Kein E-Level-Wechsel (E5 Gesamtphänomen bleibt).
- MEC-0002 EXTEND (Endowment-Effekt): Korrekt — KKT (1990/1991) selbst führen Endowment-Effekt auf Verlustaversion zurück, Ariely folgt dieser Interpretation; Duke-Ticket-Experiment als methodisch starke (Zufallszuteilung) neue Evidenzquelle. Offene "mere ownership"-Debatte transparent als Grenze dokumentiert, NICHT aufgelöst (korrekt gemäß Auftrag "Widersprüche werden dokumentiert, nicht aufgelöst").
- MEC-0005 EXTEND (Social-vs-Market-Norms-Grenzbedingung): Korrekt — kein neuer Kausalpfad, sondern wichtige, bislang fehlende Randbedingung (Reziprozität kollabiert bei Marktrahmung) plus Irreversibilitäts-Befund (Gneezy/Rustichini extern).
- MEC-0018 EXTEND (Erwartung/fMRT-Vertiefung): Korrekt — identischer Opener→Voraktivierung→veränderte-Verarbeitung-Pfad, jetzt mit externer, unabhängiger neurowissenschaftlicher Evidenz (McClure et al. 2004) gestärkt.
- A-0008 EXTEND (Preis-Placebo): Korrekt — vertieft die bestehende "Preis als Qualitätssignal"-These um kausale, teils objektiv gemessene Evidenz (JAMA-Publikation).
- P-0042 EXTEND (Ankerkontrolle/Arbitrary Coherence): Korrekt — zeitliche Vertiefung eines bestehenden Prinzips, kein neues Prinzip nötig.
- MOD-0010 EXTEND: Korrekt — sechs neue Bias-Einträge fügen sich in bestehende Kategorien 1/2 ein bzw. bilden eine fünfte, thematisch kohärente Kategorie ("Besitz- und Optionsverzerrungen"); keine MOD-0011-Neuanlage, da dies eine reine Container-Dopplung wäre (CKM §6 "zu allgemein"-Warnung korrekt angewendet).

NEU-Entscheidungen geprüft:
- MEC-0023 (Zero-Preis-Effekt): Vollständige Canonicalization-Rejection-Prüfung gegen MEC-0009 UND MEC-0002 durchgeführt und dokumentiert (Stimulus/Prozess/Reaktion-Vergleichstabelle mit beiden Kandidaten). Kernunterschied: Weder Kontrast (graduell-proportional) noch Verlustaversion (kontinuierlich) erklären die SPRUNGHAFTE, kategoriale Sonderverarbeitung exakt am Nullpunkt — durch Kontrollbedingungen (2→1 Cent vs. 1→0 Cent bei identischer absoluter Differenz) explizit von beiden bestehenden Mechanismen abgegrenzt. Alle 4 Bedingungen für MEC-Neuanlage erfüllt. **NEU gerechtfertigt.**
- A-0050, A-0052, A-0053 (neue Annahmen): Jeweils explizite Abgrenzung zu bestehenden Annahmen (A-0008) bzw. Dokumentation als eigenständige Falsifizierungsbedingung. **NEU gerechtfertigt**, mit A-0052 als Grenzfall explizit diskutiert (enge Verwandtschaft zu A-0008-Erweiterung, aber unterschiedlicher Evidenztyp — beide Wege dokumentiert für Transparenz).
- A-0051 (Marktnormen verdrängen Sozialnormen irreversibel): Abgrenzung zu MEC-0005 selbst dokumentiert (A-0051 ist eine zusätzliche, empirisch eigenständige PERSISTENZ-Eigenschaft, nicht nur Restatement des MEC-0005-Grenzbedingungs-Befunds). **NEU gerechtfertigt.**
- P-0045, P-0046, P-0047 (neue Prinzipien): Alle drei erfüllen die OR-Regel (≥2 MEC ODER ≥2 A ODER Kombination) — P-0045 (MEC-0009 + A-0008), P-0046 (MEC-0023 + A-0050, mit Transparenzhinweis auf enge Quellenverwandtschaft), P-0047 (MEC-0005 + A-0051). Alle drei tragen explizite Vier-Pflichtfragen-Struktur (Was/Warum/Wann/Wann nicht) und Ethisches-Risiko-Einstufung. **NEU gerechtfertigt.**
- T-0043 (Gut-Besser-Best-Decoy-Paketierung): Erfüllt Technik-Kriterien (konkrete, wiederholbare Handlung: Angebotsstruktur mit Decoy-Stufe), klar von P-0045 (Prinzip-Ebene) unterscheidbar, mit explizitem Ethisches-Risiko-Feld (mittel) und Fehlanwendungs-Abschnitt. **NEU gerechtfertigt.**
- "Keeping Doors Open" als MEC: Geprüft und VERWORFEN (Mindestschwelle CKM §5: ≥2 unabhängige Auftreten nicht erfüllt) — als A-0053 mit Kandidatenstatus für spätere Prüfung (B-0013 Nudge) dokumentiert. Korrekt.
- "Hot-Cold-Empathy-Gap" als MEC: Geprüft und VERWORFEN (gleicher Grund: Mindestschwelle nicht erfüllt, nur ST-0227 ohne MEC-Anlage) — korrekt als Statement mit Kandidatenvermerk dokumentiert.
- Ehrlichkeits-Priming (Ten-Commandments) als MEC/P: Geprüft und VERWORFEN — explizit wegen gescheiterter Großreplikation (Verschuere et al. 2018) und Expression of Concern (2024), NICHT wegen fehlender Mindestschwelle. Dies ist die wichtigste Nicht-Anlage-Entscheidung dieser Buchanalyse und wird in Punkt 6 vertieft geprüft.
- "Behavioral-Economics-Definitionsmodell" als MOD: Geprüft und VERWORFEN (reine disziplinäre Selbstverortung, keine Kausalstruktur, CKM §6). Korrekt in analysis.md dokumentiert.

**Ergebnis: PASS**

### 5. Nicht-Anlage-Dokumentation (CKM §9)

Geprüft: Alle vier verworfenen Kandidaten (Keeping-Doors-Open-MEC, Hot-Cold-Empathy-Gap-MEC, Ehrlichkeits-Priming-MEC/P, Behavioral-Economics-MOD) sind mit expliziter Begründung in analysis.md dokumentiert, nicht stillschweigend fallengelassen. Besonders hervorzuheben: Die Ehrlichkeits-Priming-Nicht-Anlage ist zusätzlich zur analysis.md-Dokumentation auch direkt im betroffenen Statement (ST-0241, ST-0242) mit doppeltem Warnhinweis versehen — Dokumentation ist damit redundant an zwei Stellen verankert, was das Risiko einer versehentlichen späteren Wiederverwendung als Prinzipiengrundlage minimiert.

**Ergebnis: PASS**

### 6. Replikations-/Publikationsbias-Dokumentation — vertiefte Prüfung (Sprint-Priorität 2)

Dies ist der wissenschaftlich anspruchsvollste Prüfpunkt dieser Buchanalyse, da der Auftrag explizit eine differenzierte, nicht pauschalisierende Behandlung der Ariely-Integritätsfrage verlangt.

- **Ariely-Datenfälschungsskandal 2021 (separates Werk, außerhalb dieses Buches):** Korrekt recherchiert und dokumentiert — betrifft die 2012 in PNAS publizierte, 2021 zurückgezogene Studie "The Signing Boosts Honesty" (Shu, Mazar, Gino, Ariely, Bazerman), NICHT Teil von SRC-0012 (Predictably Irrational, 2008/2009). Data-Colada-Untersuchung identifizierte Ariely als Ersteller der fabrizierten Datentabelle. Sauber getrennt von den in DIESEM Buch beschriebenen Experimenten dokumentiert (siehe SCIENTIFIC_DEBT.md).
- **Zusätzlich identifiziert (über den ursprünglich erwarteten Scope hinaus, aber Priorität-2-relevant):** Ein direkt DIESES Buch betreffender Befund — das im Buch selbst (Kap. 11) beschriebene Ten-Commandments-Experiment (Mazar, Amir & Ariely 2008) wurde durch eine unabhängige Registered Replication Report (Verschuere et al. 2018, 19 Labore, N=4.674) NICHT repliziert, und die Originalstudie erhielt 2024 ein Expression of Concern. Dies ist ein wichtiger, eigenständiger Befund, der über die reine "2021-Skandal"-Frage hinausgeht und spezifisch DIESES Buch betrifft. Korrekt als eigenständiger, prominent markierter Scientific-Debt-Eintrag dokumentiert (ST-0241/242, NICHT als P/MEC-Grundlage verwendet).
- **Unabhängig replizierte/fundierte Kernbefunde (Anchoring, Decoy-Effekt, Zero-Preis-Effekt, Endowment-Effekt):** Korrekt als überwiegend unabhängig von der Ariely-Integritätsfrage abgesichert dokumentiert — Decoy-Effekt basiert auf Huber/Payne/Puto (1982, vor Ariely), Endowment-Effekt auf Kahneman/Knetsch/Thaler (1990/1991, unabhängige Forschungsgruppe), Zero-Preis-Effekt hat mindestens eine externe Replikationsstudie (Vosgerau et al.).
- **Sauberkeit der Trennung:** Kein Statement/Objekt in dieser Buchanalyse überträgt den 2021-Skandal oder den Ten-Commandments-Replikationsfehlschlag pauschal auf andere Ariely-Befunde — jede Erweiterung/Neuanlage prüft ihre jeweilige spezifische Evidenzbasis eigenständig (siehe Punkt 3/4).

**Ergebnis: PASS** — die differenzierte Behandlung der Ariely-Integritätsfrage erfüllt die Auftragsanforderung vollständig; die zusätzlich identifizierte Ten-Commandments-Replikationsproblematik ist ein wichtiger, korrekt dokumentierter Mehrwert dieser Prüfung.

### 7. Grenzen-Dokumentation

Alle neuen/erweiterten Objekte enthalten Grenzen-Abschnitte bzw. entsprechende Einschränkungen. B2B-Transfer-Lücke wird durchgängig als offene Frage markiert (kein Objekt behauptet direkten, getesteten B2B-Vertriebstransfer für die B-0012-spezifischen Ergänzungen — alle Kernexperimente sind B2C/Konsumentenkontext, wie in SRC-0012 explizit als Grenze der Quelle dokumentiert).

**Ergebnis: PASS**

### 8. Ethisches Risiko (neue T/P-Objekte)

- P-0045 (Decoy-Positionierung): mittel — mit differenzierter Begründung (keine Falschaussage, aber Lenkungsrisiko unabhängig von tatsächlicher Kundeneignung)
- P-0046 (Zero-Preis-Instrument): mittel bis hoch — mit expliziter Unterscheidung legitimer (echte Testphasen) vs. manipulativer (verdeckte Nachteile) Anwendung
- P-0047 (Rahmungskontrolle): niedrig — mit Graubereich-Hinweis (Preistransparenz-Pflichten)
- T-0043 (Gut-Besser-Best-Decoy): mittel — mit Bedarfsanalyse-Empfehlung als Risikominderung

Alle explizit markiert und begründet, keine Unterbewertung des Manipulationspotenzials erkennbar.

**Ergebnis: PASS**

### 9. Beobachtung/Interpretation-Trennung in Statements

Stichprobenprüfung (ST-0219, ST-0225, ST-0229, ST-0241, ST-0246): Alle folgen dem Statement-Template mit getrennten Feldern für Originalaussage/Paraphrase (Beobachtung) und Mögliche Annahmen/Prinzipien (Interpretation). ST-0241/242 zusätzlich mit gesondertem, hervorgehobenem Kontext-Feld für den Replikationsvorbehalt.

**Ergebnis: PASS**

### 10. Freitext-Mechanismenreferenzen

Geprüft: Alle Mechanismus-Verweise in P-0045, P-0046, P-0047, T-0043 sowie in allen MEC-Erweiterungen nutzen ausschließlich existierende MEC-IDs (MEC-0002, MEC-0005, MEC-0009, MEC-0018, MEC-0021, MEC-0023), keine Freitext-Mechanismen.

**Ergebnis: PASS**

---

## Bekannte Restpunkte (nicht blockierend)

- A-0052 und die A-0008-Erweiterung überschneiden sich inhaltlich eng (beide basieren auf denselben zwei Ariely-Preis-Placebo-Studien) — dies ist transparent in beiden Objekten dokumentiert (siehe A-0008-Erweiterungsabschnitt, expliziter Verweis auf A-0052-Abgrenzungsbegründung), stellt aber eine methodische Grauzone dar, die der Herausgeber ggf. bei einer künftigen Konsolidierungsrunde prüfen sollte (Zusammenführungs-Kandidat gemäß CKM §4.3 — hier bewusst NICHT eigenständig durchgeführt, da Zusammenführung laut CKM eine Herausgeber-Entscheidung ist).
- Einige Sekundärquellen im Buch (Clark/Mills/Fiske zu Social/Market Norms, Dimberg-analoge Fußnoten) sind ohne vollständige bibliographische Angabe im Fließtext zitiert — als offene Fragen markiert, nicht spekulativ vervollständigt.

## Gesamtergebnis

**STATUS: BESTANDEN — keine Blocker**

Alle 10 Prüfpunkte bestanden. 5 EXTEND-MECs korrekt durchgeführt (MEC-0009, MEC-0021, MEC-0002, MEC-0005, MEC-0018), 1 neuer MEC mit vollständiger Canonicalization-Rejection-Begründung (MEC-0023), 4 neue A-Objekte mit expliziter Abgrenzung, 1 A-Erweiterung (A-0008), 3 neue P-Objekte (OR-Regel jeweils erfüllt), 1 P-Erweiterung (P-0042), 1 neue T, 1 MOD-Erweiterung (keine MOD-0011-Neuanlage, geprüft und begründet abgelehnt), 31 neue ST, 4 Kandidaten explizit verworfen und dokumentiert (Nicht-Anlage-Dokumentation). Scientific Debt und Publikationsbias-Risiken — einschließlich der komplexen, differenziert zu behandelnden Ariely-Integritätsfrage sowie eines zusätzlich identifizierten, direkt buchrelevanten Replikationsfehlschlags (Ten Commandments) — korrekt identifiziert, sauber getrennt und transparent markiert.

## Status

Abgeschlossen — 2026-07-02
