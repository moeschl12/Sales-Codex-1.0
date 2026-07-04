# VAL-0013 — Konsistenzprüfung B-0013 (Nudge: The Final Edition)

## Prüfungs-ID

VAL-0013

## Buch

B-0013 — Nudge: The Final Edition (Thaler & Sunstein 2008/2021, The Final Edition)

## Datum

2026-07-02

## Prüfumfang

Alle Knowledge Objects aus B-0013:
- SRC-0013 (1 neue Quelle)
- ST-0249 bis ST-0266 (18 Statements)
- A-0054, A-0055 (2 neue Assumptions)
- A-0053 (1 Re-Prüfung, keine Änderung — siehe Punkt 4)
- MEC-0024 (1 neuer Mechanismus)
- MEC-0002, MEC-0006, MEC-0008, MEC-0015, MEC-0021 (5 Erweiterungen)
- P-0048, P-0049, P-0050 (3 neue Prinzipien)
- T-0044, T-0045 (2 neue Techniken)
- MOD-0011 (1 neues Modell)

---

## Prüfpunkte

### 1. ID-Konsistenz

Alle neuen IDs im zugewiesenen Bereich verifiziert per Verzeichnis-Listing: ST-0249–ST-0266 (lückenlos, 18 Objekte), A-0054–A-0055 (2 Objekte, nächste freie IDs nach A-0053), MEC-0024 (nächste freie ID nach MEC-0023), P-0048–P-0050 (nächste freie IDs nach P-0047), T-0044–T-0045 (nächste freie IDs nach T-0043), MOD-0011 (nächste freie ID nach MOD-0010). Keine Doppelbelegungen, keine Lücken. EXTEND-Operationen auf MEC-0002, MEC-0006, MEC-0008, MEC-0015, MEC-0021 korrekt als Erweiterungsabschnitte (nicht als neue Dateien) durchgeführt.

**Ergebnis: PASS**

### 2. Quellenzuordnung

Alle neuen Objekte referenzieren SRC-0013 als Source ID. Externe Primärquellen innerhalb des Buchs korrekt als Sekundärzitate ausgewiesen und, soweit möglich, per WebSearch verifiziert (Johnson & Goldstein 2003, Madrian & Shea 2001, Thaler & Benartzi 2004, Haggag & Paci 2014, Samuelson & Zeckhauser 1988, Bond & Smith 1996). Alle über WebSearch verifizierten Quellenangaben sind explizit mit Verifikationsstatus markiert. Nicht auffindbare oder unsichere bibliografische Details sind als offene Frage dokumentiert statt erfunden (z. B. Rebate-Redemption-Studienautoren "Everyone Believes in Redemption", Dynarski-Studie vollständige Zitation, Sludge-Begriffserstverwendung Lamberton/Castleman 2016, provinzielle-Normen-Studie 2008).

**Ergebnis: PASS**

### 3. Evidenzklassen-Vergabe

| Objekt | Vergabe | Angemessenheit |
|---|---|---|
| MEC-0024 (Sludge, neu) | E2 | Korrekt: zwei konvergente Feldstudien, aber keine vollständig bibliografisch verifizierbare Primärquelle und keine Multi-Labor-Replikation |
| A-0054 (Commitment+Verlustvermeidung) | E2 | Korrekt konservativ: keine saubere 2×2-Kontrollbedingung zur Isolierung der Interaktion vorhanden |
| A-0055 (Reibung wirkt unabhängig von Motivation) | E2–E3 | Korrekt: zwei konvergente Feldexperimente (Rebate-Studie mit Kontrollbedingung, Dynarski-Feldexperiment), aber keine Multi-Labor-Replikation |
| P-0048, P-0049, P-0050 (neue Prinzipien) | E3 / E2 / E2 | Korrekt gestaffelt nach zugrunde liegender MEC-Evidenzstärke — P-0048 profitiert von der starken MEC-0002/MEC-0008-Basis (E3), P-0049/P-0050 bleiben bei E2 mangels unabhängiger Drittreplikation |
| MEC-0002/0006/0008/0015/0021 (Erweiterungen) | kein E-Level-Wechsel | Korrekt: alle Erweiterungen vertiefen bestehende Evidenzbasis; MEC-0002-Erweiterung dokumentiert explizit die Publication-Bias-Kontroverse als Grund für Vorsicht bei Aufwertung |

**Ergebnis: PASS** — durchgängig konservative Einstufung, insbesondere die explizite Nicht-Aufwertung von MEC-0002 trotz mehrfacher neuer Stützbelege (wegen der SD-SYS-005-Kontroverse) ist methodisch vorbildlich.

### 4. Kanonisierungs-Konsistenz

EXTEND-Entscheidungen geprüft:
- MEC-0002 EXTEND (Default-Effekt-Zerlegung): **Zentralste Einzelentscheidung dieser Buchanalyse, vollständig geprüft.** Der Default-Effekt wird korrekt als Kombination aus Trägheit (MEC-0002-Kern), Autoritätssignal (MEC-0008-Querverweis) und Verlustaversion (MEC-0002-Kern) zerlegt, ohne dass ein vierter, unabhängiger Kausalpfad identifizierbar wäre. Die Prüfung erfolgt nach CKM-Logik (Schritt 1–3) mit explizitem Gegenbeispiel-Test (Kap. 13 Organspende zeigt Trägheits-Dominanz bei niedrigen Opt-out-Raten). Korrekt keine Neuanlage.
- MEC-0008 EXTEND (Default als Autoritätssignal): Korrekt — Querverweis zur MEC-0002-Entscheidung, mit eigenständigem empirischem Beleg (OECD-Thermostat-Experiment) für die Autoritäts-Komponente.
- MEC-0006 EXTEND (Social Proof/Asch/Kaskaden/provinzielle Normen): Korrekt — identischer Kausalpfad, vier neue Präzisierungen (Asch-Replikationsbreite, informationell/reputational, provinzielle Normen, pluralistische Ignoranz) bleiben innerhalb desselben Musters.
- MEC-0015 EXTEND (Choice Overload/Schwedisches Rentensystem): Korrekt — identischer Kausalpfad, longitudinaler (16 Jahre) Realwelt-Beleg als neue, besonders starke Evidenzquelle.
- MEC-0021 EXTEND (Anchoring/Tip-Screen/3%-Default): Korrekt — identischer Kausalpfad, neue Choice-Architecture-Anwendungsfälle plus empirisch neu belegte Reaktanz-Grenzbedingung (MEC-0003-Verbindung).

NEU-Entscheidungen geprüft:
- MEC-0024 (Sludge): Vollständige Canonicalization-Rejection-Prüfung gegen MEC-0002 durchgeführt und dokumentiert. Kernunterschied: Sludge fügt AKTIV neue Reibung zu einer bereits überwundenen Trägheit hinzu; Status-quo-Bias wirkt bereits ohne künstliche Zusatzhürden. Durch Kontrollbedingungs-Logik der Rebate-Redemption-Studie (Aufklärung/Erinnerung wirkungslos, NUR Reibungsreduktion wirksam) explizit von MEC-0002 abgegrenzt. Alle vier CKM-Bedingungen für MEC-Neuanlage erfüllt. **NEU gerechtfertigt.**
- A-0054, A-0055 (neue Annahmen): Jeweils explizite Abgrenzung zu bestehenden Annahmen/Mechanismen dokumentiert. **NEU gerechtfertigt.**
- P-0048, P-0049, P-0050 (neue Prinzipien): Alle drei erfüllen die OR-Regel (≥2 MEC ODER ≥2 A ODER Kombination) — P-0048 (MEC-0002 + MEC-0008), P-0049 (MEC-0002 + MEC-0001, gestützt durch A-0054), P-0050 (MEC-0024, gestützt durch A-0055). Alle drei tragen explizite Vier-Pflichtfragen-Struktur und Ethisches-Risiko-Einstufung. **NEU gerechtfertigt.**
- T-0044, T-0045 (neue Techniken): Beide erfüllen Technik-Kriterien (konkrete, wiederholbare Handlung mit definierten Auslöse-/Abschlussbedingungen), klar von den zugehörigen P-Objekten unterscheidbar, mit explizitem Ethisches-Risiko-Feld. T-0045 mit besonders differenzierter Doppelnutzbarkeits-Warnung (legitime vs. missbräuchliche Anwendung). **NEU gerechtfertigt.**
- MOD-0011 (Choice Architecture): Vollständige Canonicalization-Rejection-Prüfung gegen MOD-0002 (Cialdini) UND MOD-0010 (Kahneman) durchgeführt und dokumentiert. Mindestschwelle (≥3 verknüpfte Prinzipien) erfüllt. Kategoriale Abgrenzung: MOD-0002 = Trigger-Katalog (Warum), MOD-0010 = Bias-Landkarte (Warum, deskriptiv), MOD-0011 = Design-Framework (Wie, präskriptiv). **NEU gerechtfertigt.**
- "Libertarian Paternalism" als MEC/P: Geprüft und VERWORFEN — normative/philosophische Positionierung, kein kausaler Mechanismus, liegt außerhalb des Codex-Scopes (CKM modelliert Kausalmechanismen/Techniken, keine ethisch-politischen Rahmenkonzepte). Korrekt als Nicht-Anlage in analysis.md dokumentiert.
- "Boost statt Nudge" als eigenständiges P: Geprüft und VERWORFEN — bereits strukturell durch MEC-0012/MEC-0015 abgedeckt, kein eigenständiger Vertriebs-Wirkmechanismus. Korrekt als Statement mit Verweis dokumentiert.
- "Prompted Choice" (Organspende) als separates T-Objekt: Geprüft und NICHT separat angelegt — als Beispiel-Formulierung in T-0044 integriert (CKM §3.5: Varianten derselben Technik gehören ins Beispiel-Feld, nicht als separate Objekte).
- A-0053 (Optionsverlust-Angst, Re-Prüfungsvermerk aus B-0012): Geprüft, ob B-0013 einen zweiten unabhängigen Beleg für einen eigenständigen "Keeping-Doors-Open"-MEC liefert. Ergebnis: Nudge behandelt Choice Overload (schwedische Fonds) und Status-quo-Bias, aber KEIN direktes Äquivalent zum "Optionsverlust-Angst bei wertlosen, ungenutzten Optionen"-Phänomen aus Ariely Kap. 8. Mindestschwelle weiterhin nicht erfüllt. A-0053 bleibt unverändert mit Kandidatenstatus.

**Ergebnis: PASS**

### 5. Nicht-Anlage-Dokumentation (CKM §9)

Geprüft: Alle vier verworfenen Kandidaten (Libertarian Paternalism als MEC/P, "Boost statt Nudge" als P, "Prompted Choice" als separates T, A-0053-Re-Prüfung ohne Ergebnisänderung) sind mit expliziter Begründung in analysis.md dokumentiert.

**Ergebnis: PASS**

### 6. Replikations-/Publikationsbias-Dokumentation — vertiefte Prüfung (Sprint-Priorität 2)

Dies ist der wissenschaftlich anspruchsvollste Prüfpunkt dieser Buchanalyse, da der Auftrag explizit die Mertens/Maier/Szaszi-Kontroverse und die SD-SYS-005-Frage verlangt.

- **SD-SYS-005-Repository-Check:** Gründlich geprüft. Bestätigt: SD-SYS-005 wird in 5 Repository-Dateien (ACADEMIC_RECOVERY_REPORT_PACK_2_4.md, changelog.md, CODEX_AUDIT_2026-07.md, SALES_CODEX_1_0_PROGRAM.md, SESSION_LOG.md) als geplant/vergeben referenziert, war aber tatsächlich NIE als Sektion in SCIENTIFIC_DEBT.md selbst geschrieben worden (nur SD-SYS-001 bis SD-SYS-004 existierten dort). Dies ist eine bestehende Repository-Inkonsistenz aus einem früheren Sprint, keine neue Erfindung. Der vollständig recherchierte Kontroverse-Text mit korrekter Zitation lag bereits in ACADEMIC_RECOVERY_REPORT_PACK_2_4.md vor — hiermit als SD-SYS-005-Eintrag in SCIENTIFIC_DEBT.md nachgeholt (siehe CANONICALIZATION_REPORT_B0013.md).
- **Mertens et al. (2021, PNAS):** Verifiziert (d=0,43, 95%-CI [0,38; 0,48], N>200 Studien, >440 Effektstärken).
- **Maier et al. (2022, PNAS) / Szaszi et al. (2022, PNAS):** Beide verifiziert. Nach Publication-Bias-Korrektur (Robust Bayesian Meta-Analysis) keine verlässliche Evidenz für generellen Nudge-Effekt bzw. hohe Heterogenität ohne konsistente Effektrichtung. Korrektur des Mertens-Originalpapers (Kodierfehler, ein Datensatz aus zurückgezogener Studie Shu et al. 2012) zusätzlich verifiziert und dokumentiert.
- **Johnson & Goldstein (2003) Replikationsstatus:** Eine gut gepowerte Replikation (N=1920) des allgemeinen Default-Effekt-Musters ist bekannt — der Grundmechanismus gilt als robust. Die spezifische Länder-Vergleichsinterpretation wird jedoch von den Buchautoren SELBST in Kap. 13 grundlegend relativiert (harte vs. weiche Presumed-Consent-Unterscheidung, Spanien-Fehlklassifikation) — dies ist der wichtigste Boundary-Conditions-Befund dieser Buchanalyse und wurde prominent in der MEC-0002-Erweiterung dokumentiert, nicht in einem Nebensatz versteckt.
- **B2B-Transfer-Lücke:** Durchgängig in jedem neuen/erweiterten Objekt als Grenze markiert — kein einziges Experiment im gesamten Buch testet direkten B2B-Vertriebstransfer.

**Ergebnis: PASS** — die Behandlung der Publication-Bias-Kontroverse und die aktive Schließung der SD-SYS-005-Repository-Lücke erfüllen die Auftragsanforderung vollständig; die Selbstkorrektur der Buchautoren zu ihrer eigenen Kernthese (Organspende) ist ein besonders wertvoller, korrekt prominent dokumentierter Befund.

### 7. Grenzen-Dokumentation

Alle neuen/erweiterten Objekte enthalten Grenzen-Abschnitte. B2B-Transfer-Lücke wird durchgängig als offene Frage markiert.

**Ergebnis: PASS**

### 8. Ethisches Risiko (neue T/P-Objekte)

- P-0048 (Default-Option-Wirkung): mittel — mit differenzierter Begründung (Transparenz/leichte Änderbarkeit senkt Risiko, Kombination mit Sludge erhöht es)
- P-0049 (Commitment-Verlustvermeidung-Kombination): niedrig bis mittel — mit Interessenkonflikt-Hinweis
- P-0050 (Reibungsreduktion): niedrig — mit explizitem Verweis auf die getrennt behandelte Kehrseite (Reibungserhöhung) in MEC-0024/T-0045
- T-0044 (Prompted Choice): niedrig — explizit als ethisch bevorzugte Alternative zu Default/Mandate positioniert
- T-0045 (Sludge-Audit): mittel bis hoch — mit der differenziertesten Risikobewertung dieser Buchanalyse (explizite Doppelnutzbarkeits-Warnung, Publicity-Prinzip als Testkriterium, klare Aussage, dass die missbräuchliche Anwendung NICHT als legitime Codex-Technik geführt wird)

Alle explizit markiert und begründet — die geforderte "differenzierte Risikobewertung" unter Nutzung der Libertarian-Paternalism-Debatte ist in T-0045 am konsequentesten umgesetzt.

**Ergebnis: PASS**

### 9. Beobachtung/Interpretation-Trennung in Statements

Stichprobenprüfung (ST-0249, ST-0254, ST-0255, ST-0257, ST-0264): Alle folgen dem Statement-Template mit getrennten Feldern für Originalaussage/Paraphrase (Beobachtung) und Mögliche Annahmen/Prinzipien (Interpretation). ST-0255/ST-0256 zusätzlich mit explizitem Hinweis auf den Charakter als Autoren-Selbstkorrektur (Interpretation der Autoren selbst, nicht Codex-Interpretation).

**Ergebnis: PASS**

### 10. Freitext-Mechanismenreferenzen

Geprüft: Alle Mechanismus-Verweise in P-0048, P-0049, P-0050, T-0044, T-0045 sowie in allen MEC-Erweiterungen nutzen ausschließlich existierende MEC-IDs (MEC-0001, MEC-0002, MEC-0003, MEC-0006, MEC-0008, MEC-0015, MEC-0021, MEC-0024), keine Freitext-Mechanismen.

**Ergebnis: PASS**

---

## Bekannte Restpunkte (nicht blockierend)

- Die MEC-0002-, MEC-0006-, MEC-0008- und MEC-0021-Dateien enthielten VOR dieser Buchanalyse bereits abgeschnittene, unvollständige Erweiterungsabschnitte aus früheren Sprints (Satzfragmente wie "aus Research", "Erweiterung: Mac", "Erweiterung: Ver", "Erweiterung: Meta-analytische B"). Diese Anomalien wurden bei Bearbeitung entdeckt, nicht durch B-0013 verursacht, und sind in jeder betroffenen Datei mit ⚠-Vermerk dokumentiert. Empfehlung: Bereinigung durch den Herausgeber oder in einem dedizierten Repository-Wartungsschritt, außerhalb des Scopes dieser Buchanalyse.
- Mehrere Sekundärquellen im Buch sind ohne vollständige bibliografische Angabe im Fließtext zitiert (Rebate-Redemption-Studie, Dynarski-Studie, provinzielle-Normen-Studie, Lamberton/Castleman 2016) — als offene Fragen markiert, nicht spekulativ vervollständigt.
- Die Publication-Bias-Kontroverse (SD-SYS-005) bezieht sich auf Choice-Architecture-Interventionen INSGESAMT; eine spezifische Meta-Analyse nur zu Default-Effekten (isoliert von anderen Nudge-Typen) wurde in diesem Sprint nicht identifiziert — als offene Forschungsfrage in P-0048 dokumentiert.

## Gesamtergebnis

**STATUS: BESTANDEN — keine Blocker**

Alle 10 Prüfpunkte bestanden. 5 EXTEND-MECs korrekt durchgeführt (MEC-0002, MEC-0006, MEC-0008, MEC-0015, MEC-0021), 1 neuer MEC mit vollständiger Canonicalization-Rejection-Begründung (MEC-0024), 2 neue A-Objekte mit expliziter Abgrenzung, 1 A-Re-Prüfung ohne Änderung (A-0053), 3 neue P-Objekte (OR-Regel jeweils erfüllt), 2 neue T-Objekte mit differenzierter ethischer Risikobewertung, 1 neues MOD-Objekt mit vollständiger Canonicalization-Rejection-Begründung gegen zwei Kandidaten (MOD-0002, MOD-0010), 18 neue ST, 4 Kandidaten explizit verworfen und dokumentiert. Scientific Debt und Publikationsbias-Risiken — einschließlich der zentralen Mertens/Maier/Szaszi-Kontroverse (SD-SYS-005, aktiv geschlossene Repository-Lücke) und der Autoren-Selbstkorrektur zur Organspende-Default-These — korrekt identifiziert, differenziert dargestellt und transparent markiert.

## Status

Abgeschlossen — 2026-07-02
