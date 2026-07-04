# Canonicalization Report — B-0013 (Nudge: The Final Edition, Thaler & Sunstein 2008/2021)

## Zweck

Detaillierte Dokumentation aller Canonicalization-Entscheidungen der B-0013-Buchanalyse, gemäß Editor-Auftrag "Behavioral Science Expansion" — Priorität 1 (Kanonisierung vor Neuanlage). Ergänzt VAL-0013 und BOOK_REVIEW_REPORT_B0013.md um die geforderten strukturierten Einzelabschnitte. Format und Anspruchsniveau folgen CANONICALIZATION_REPORT_B0011.md und CANONICALIZATION_REPORT_B0012.md (Bücher 1 und 2 desselben Sprints).

**Formel (übernommen aus SPR-0001/canonicalization_report.md, identisch zu B-0011/B-0012):** Canonicalization Rate = Extensions / (Neue Objekte + Extensions) × 100, bezogen auf Mechanismen (MECs) — die Objektkategorie, die im CKM primär kanonisierbar ist.

---

## 1. Neue Statements

**Anzahl:** 18
**ID-Bereich:** ST-0249 bis ST-0266

Alle 18 Statements sind buchspezifische Einzelaussagen (per CKM-Definition nicht kanonisierbar/erweiterbar — Statements werden immer neu angelegt, auch wenn ihr Inhalt zur Fundierung bestehender A/MEC/P-Objekte verwendet wird). Zuordnung zu den Erweiterungen/Neuanlagen: ST-0249/ST-0250 → Grundbegriffe (Libertarian Paternalism, Choice Architecture, nicht selbst canonicalisiert); ST-0251/ST-0252/ST-0253/ST-0254 → MEC-0002-Erweiterung (Default-Effekt-Zerlegung); ST-0255/ST-0256 → MEC-0002-Erweiterung, Boundary Conditions (Autoren-Selbstkorrektur); ST-0257/ST-0258 → MEC-0024 (neu, Sludge); ST-0259 → MEC-0015-Erweiterung (Choice Overload, Schwedisches Rentensystem); ST-0260/ST-0261 → MEC-0006-Erweiterung (Social Proof/Asch/Normen); ST-0262/ST-0263 → MEC-0021-Erweiterung (Anchoring/Choice-Architecture-Anwendungen, Reaktanz); ST-0264/ST-0265 → Nicht-Anlage-Dokumentation (Kritik, Boost-Debatte); ST-0266 → MEC-0002-Erweiterung (Deductible Aversion als weitere Anwendung).

---

## 2. Neue Assumptions

**Anzahl:** 2
**IDs:** A-0054, A-0055

Jede neue Annahme trägt eine explizite Abgrenzungsbegründung:

- **A-0054** (Commitment-Verzögerung + Verlustvermeidung wirkt kombiniert stärker als jede Komponente einzeln): Postuliert eine super-additive Interaktion zwischen zeitlich verzögertem Commitment und Verlustvermeidungs-Framing, basierend auf der Save-More-Tomorrow-Logik (Thaler & Benartzi 2004). Abgrenzung zu MEC-0002 (reine Verlustaversion) und MEC-0001 (reine Commitment-Konsistenz) dokumentiert: A-0054 postuliert nicht einen dritten Mechanismus, sondern eine spezifische, empirisch plausible Interaktionshypothese zwischen zwei bestehenden Mechanismen — CKM-konform als A-Objekt (nicht MEC) geführt, da keine eigenständige kausale Struktur, sondern eine Kombinationswirkung behauptet wird. Evidenzstatus E2 (keine saubere 2×2-Kontrollbedingung zur Isolierung der Interaktion im Quelltext vorhanden).
- **A-0055** (Aktiv erhöhte Reibung wirkt trotz vorhandener Handlungsabsicht): Postuliert, dass künstlich hinzugefügte Reibung Verhalten blockiert, selbst wenn eine Handlungsabsicht bereits besteht — im Unterschied zur passiven Trägheit des Status-quo-Bias, die keine vorherige Absicht voraussetzt. Grundlage für MEC-0024 (Sludge). Abgrenzung zu MEC-0002 explizit dokumentiert (siehe Abschnitt 3 unten, MEC-0024-Rejection-Prüfung). Evidenzstatus E2–E3 (zwei konvergente Feldexperimente mit Kontrollbedingungslogik, aber keine Multi-Labor-Replikation).

**A-0053-Re-Prüfung (kein neues Objekt, keine Änderung):** Wie in SCIENTIFIC_DEBT.md (B-0012-Sektion) und BOOK_REVIEW_REPORT_B0012.md explizit empfohlen, wurde geprüft, ob B-0013 einen zweiten unabhängigen Beleg für das "Keeping-Doors-Open"/Optionsverlust-Angst-Phänomen liefert. Ergebnis: Nudge behandelt Choice Overload (Schwedisches Rentenfondssystem, MEC-0015-Erweiterung) und Status-quo-Bias (MEC-0002-Erweiterung), aber kein direktes Äquivalent zum spezifischen Ariely-Befund (Angst vor Verlust des Zugriffsrechts auf eine wertlose, ungenutzte Option). Die CKM-Mindestschwelle (≥2 unabhängige Auftreten als erklärende Kraft) bleibt unerfüllt. A-0053 bleibt unverändert mit Kandidatenstatus — dokumentiert als "geprüft, nicht aufgelöst" statt stillschweigend übergangen.

---

## 3. Neue Mechanismen

**Anzahl:** 1
**ID:** MEC-0024 — "Sludge: Künstlich erhöhte Transaktionsreibung als Verhaltensblockade"

### Canonicalization-Rejection-Begründung (vollständig, aus MEC-0024-Datei zusammengefasst)

Geprüfter bestehender Kandidat: **MEC-0002 (Verlustaversion und Kosten des Status quo)**.

**CKM-Schritt 1 (Suche):** MEC-0002 ist der naheliegendste Kandidat, da Sludge (zusätzliche Reibung, die eine Handlung erschwert) oberflächlich wie eine Spielart der Status-quo-Bias-Trägheit wirken könnte — in beiden Fällen "bleibt am Ende weniger passiert als ohne die Hürde".

**CKM-Schritt 2 (Identitätsprüfung nach kausaler Struktur):**

| Merkmal | MEC-0002 (Status-quo-Bias/Trägheit) | MEC-0024 (Sludge) |
|---|---|---|
| Ausgangszustand | Keine Handlungsabsicht erforderlich — Trägheit wirkt bereits ohne aktiven Widerstand | Handlungsabsicht bereits VORHANDEN (z. B. Kunde will kündigen, Rabatt einlösen, Formular abschicken) |
| Stimulus (X) | Abwesenheit eines Anstoßes / Vorhandensein eines passiven Defaults | Aktiv hinzugefügte, künstliche Reibung (zusätzliche Formularschritte, versteckte Kündigungswege, Wartezeiten) |
| Prozess (Y) | Aufwandsvermeidung + Verlustaversion relativ zum Status quo | Überwindung der Reibung erfordert mehr Aufwand/Ausdauer als die vorhandene Motivation hergibt — Motivation wird durch Prozesshürden "aufgebraucht" |
| Reaktion (Z) | Verbleib beim Status quo trotz theoretisch vorhandener besserer Alternative | Abbruch einer bereits begonnenen, gewollten Handlung |
| Kernevidenz | Madrian & Shea 2001, Samuelson & Zeckhauser 1988 | Rebate-Redemption-Studie, Dynarski-Studie |

**Entscheidender Beleg für die kausale Nicht-Identität:** Die Kontrollbedingungs-Logik der Rebate-Redemption-Studie ist zentral. Aufklärungs- und Erinnerungsinterventionen (die die HandlungsABSICHT stärken sollten) hatten NULL Effekt auf die tatsächliche Rückerstattungsquote — nur die direkte Reduktion der Prozessreibung selbst (weniger Formularschritte, kürzere Fristen-Anforderungen) erhöhte die Rate von 30% auf 54%. Wäre der Effekt vollständig durch Status-quo-Trägheit (MEC-0002) erklärbar, müsste eine Stärkung der Handlungsabsicht (Aufklärung/Erinnerung) ebenfalls wirksam sein, da Trägheit graduell mit der Motivationsstärke variiert. Die beobachtete Nullwirkung von Aufklärung bei gleichzeitig starker Wirkung der reinen Reibungsreduktion zeigt, dass ein von der Motivationsstärke UNABHÄNGIGER Blockademechanismus vorliegt — genau die per CKM geforderte "Kontrollbedingung, die eine Erklärung durch den bestehenden Mechanismus ausschließt".

**CKM-Schritt 3 (Qualitätsprüfung, alle vier Bedingungen erfüllt):**
1. Nicht bereits durch MEC-0002 abgedeckt — siehe Kontrollbedingungs-Analyse oben.
2. Eigenständiger erklärender Beitrag: Ja — erklärt einen empirisch beobachtbaren Bruch zwischen Absicht und Verhalten, den reine Trägheitslogik nicht erklären kann.
3. Mindestschwelle (≥2 unabhängige Auftreten als erklärende Kraft): Erfüllt — Rebate-Redemption-Studie und Dynarski-Studie (Formularentfernung erhöhte Abschlussquote von 26% auf 68%) sind zwei unabhängige, konvergente Feldbelege.
4. Keine bloße Umbenennung: Erfüllt — beschreibt eine andere Wirkrichtung (AKTIV erschwerend gegen vorhandene Absicht) als MEC-0002 (PASSIV trägheitserhaltend ohne vorherige Absicht).

**Ergebnis:** Alle vier Bedingungen erfüllt → Neuanlage gerechtfertigt. Evidenzlevel E2 (zwei konvergente Feldstudien, aber unvollständige bibliografische Primärquellenangaben und keine Multi-Labor-Replikation — konservativ eingestuft, kein E3).

**Keine weiteren neuen Mechanismen wurden angelegt.** Alle übrigen geprüften Kandidaten (Default-Effekt, Anchoring-in-Choice-Architecture, Social-Proof-Präzisierungen, Choice-Overload-Vertiefung) wurden als Erweiterungen bestehender MECs eingeordnet (siehe Abschnitt 4).

---

## 4. Erweiterte Objekte

**Anzahl:** 5 (alle MEC)

| Objekt | Art der Erweiterung |
|---|---|
| **MEC-0002 (Verlustaversion und Kosten des Status quo)** | **Zentralste Einzelentscheidung dieser Buchanalyse.** Der Default-Effekt wird als Kombination aus drei Komponenten zerlegt: (1) Trägheit/Aufwandsvermeidung — Kern von MEC-0002 selbst; (2) implizites Autoritätssignal — Querverweis zu MEC-0008; (3) Verlustaversion relativ zum Status-quo-Referenzpunkt — Kern von MEC-0002 selbst. Kein vierter, unabhängiger Kausalpfad im Quelltext identifizierbar. Neue Primärquellen: Madrian & Shea (2001, 401(k)-Automatic-Enrollment), Johnson & Goldstein (2003, Organspende-Default), Thaler & Benartzi (2004, Save More Tomorrow). Kritischer neuer Grenzen-Abschnitt: Boundary Conditions (harte vs. weiche Presumed-Consent-Unterscheidung, Spanien-Fehlklassifikation — Autoren-Selbstkorrektur in Kap. 13), Publikationsbias-Kontroverse (Mertens/Maier/Szaszi, Querverweis SD-SYS-005), B2B-Transfer-Lücke. Zusätzliche Anwendungsbeispiele: Deductible Aversion ("Choose to Lose"). Kein E-Level-Wechsel (bewusst nicht auf E4 gehoben, trotz mehrfacher neuer Stützbelege, wegen der offenen Publikationsbias-Kontroverse). |
| MEC-0008 (Autorität und automatische Befolgung) | Querverweis-Erweiterung aus der MEC-0002-Entscheidung: Default-Optionen wirken zusätzlich als implizites Autoritätssignal ("die Institution empfiehlt diese Option"). Eigenständiger empirischer Beleg: OECD-Thermostat-Experiment (1°C-Default vs. 2°C-Default), das zeigt, dass die Autoritätssignal-Komponente kollabiert, wenn der Default als unplausibel wahrgenommen wird. Kein E-Level-Wechsel. |
| MEC-0006 (Social Proof/Korrektheitssignal) | Vertiefung um Asch-Konformitätsforschung (1956-Monographie, zusätzlich Bond & Smith 1996 Meta-Analyse über 130+ Studien/17 Länder), Unterscheidung informationeller vs. reputationaler Kaskaden, provinzielle/deskriptive Normen (Hotel-Handtuch-Studie), pluralistische Ignoranz (Saudi-Arabien-Beispiel aus dem Buch). Kein E-Level-Wechsel. |
| MEC-0015 (Kognitive Überlastung durch Feature-/Choice-Overload) | Neuer, besonders starker longitudinaler Realwelt-Beleg: schwedisches Prämien-Rentenfondssystem (456 auf über 900 Fonds über 16 Jahre), das trotz aktiver staatlicher Förderung von Eigenverantwortung persistente Wahlüberlastung zeigt (inkl. Betrugsskandal mit nur 1,4% aktivem Anbieterwechsel). Kein E-Level-Wechsel. |
| MEC-0021 (Anchoring-Mechanismus) | Neue Choice-Architecture-Anwendungsfälle (3%-Default als Anker im Save-More-Tomorrow-Programm) sowie eine neue, empirisch belegte Reaktanz-Grenzbedingung (Haggag & Paci 2014, Tip-Screen-Experiment: unplausibel hohe Default-Anker erzeugen Reaktanz statt Zustimmung). Kein E-Level-Wechsel. |

**⚠ Repository-Anomalie (nicht durch B-0013 verursacht):** MEC-0002, MEC-0006, MEC-0008 und MEC-0021 enthielten vor dieser Buchanalyse bereits abgeschnittene, unvollständige Erweiterungsabschnitte aus früheren Sprints (Satzfragmente). Dies wurde bei Bearbeitung entdeckt, ist in jeder betroffenen Datei mit ⚠-Vermerk dokumentiert und zur Bereinigung an eine höhere Sprint-Ebene weitergereicht — analog zur SRC-0010-Anomalie-Dokumentation in B-0011.

---

## 5. Canonicalization Rate

**Berechnungsbasis (MEC-spezifisch, wie in SPR-0001/B-0011/B-0012 definiert):**

- Neue MECs: 1 (MEC-0024)
- Erweiterte MECs: 5 (MEC-0002, MEC-0006, MEC-0008, MEC-0015, MEC-0021)
- **Canonicalization Rate B-0013 = 5 / (1 + 5) × 100 = 83,3%**

**Vergleich mit vorherigen Büchern des Sprints:**

| Buch | Canonicalization Rate (MEC-basiert) | Neue MECs | Erweiterte MECs |
|---|---|---|---|
| B-0011 (Emotional Intelligence, Goleman) | 75,0% | 1 | 3 |
| B-0012 (Predictably Irrational, Ariely) | 83,3% | 1 | 5 |
| **B-0013 (Nudge, Thaler & Sunstein)** | **83,3%** | **1** | **5** |

B-0013 erreicht denselben hohen Vertiefungsgrad wie B-0012 und bestätigt damit den positiven Trend des Sprints: von den drei bisher bearbeiteten Büchern zeigen zwei den bislang höchsten MEC-Canonicalization-Wert des gesamten Sprints "Behavioral Science Expansion" (83,3%), deutlich über dem Sprint-1-Zielwert (≥60%) und über dem Sprint-1-Höchstwert (B-0005: 67%). Dies ist inhaltlich plausibel und nicht zufällig: Thaler ist Mitautor sowohl der Verlustaversions-/Endowment-Grundlagenforschung (bereits als MEC-0002 im Codex verankert) als auch des Nudge-Konzepts selbst — die thematische Nähe zu bereits canonicalisierten Mechanismen war strukturell von vornherein hoch. Die einzige tatsächliche Neuanlage (MEC-0024, Sludge) ist durch eine besonders sorgfältig dokumentierte, kontrollbedingungsbasierte Canonicalization-Rejection-Prüfung gegen MEC-0002 gerechtfertigt — dieselbe methodische Rigorosität wie bei MEC-0023 in B-0012.

**Codex-weite Rate (alle Objekttypen, informativ, nicht die primäre Kennzahl):** 5 Extensions / (27 Neue + 5 Extensions) × 100 = 15,6%. Niedriger als die MEC-spezifische Rate, methodisch erwartbar (Statements — hier 18 von 27 Neuanlagen — werden per CKM-Definition immer neu angelegt, auch bei inhaltlicher Fundierung bestehender Objekte).

---

## 6. Neue Scientific Debt

Vollständig eingetragen in `00_project/SCIENTIFIC_DEBT.md`:

1. **Neue Sektion "B-0013 — Nudge: The Final Edition (SRC-0013)"** (7 Einträge) mit buchspezifischen Debt-Punkten: MEC-0002-Publikationsbias-Vorbehalt, ST-0255/ST-0256-Autoren-Selbstkorrektur, MEC-0024-externe-Validierung-ausstehend, A-0054/A-0055-externe-Validierung-ausstehend, A-0053-Re-Prüfung-ohne-Änderung, unvollständige Sekundärzitate, durchgängige B2B-Transferlücke.

2. **Neue systemische Sektion "SD-SYS-005 — Publikationsbias-Kontroverse zur generellen Nudge-/Choice-Architecture-Wirksamkeit"** (nachgetragen, siehe Abschnitt 7 unten für Details zur Repository-Lücken-Schließung).

Zusammenfassung der wichtigsten neuen Einträge:

| Objekt-ID | Kategorie | Priorität |
|---|---|---|
| MEC-0002 (Erweiterung), MOD-0011, P-0048 | Widersprüchliche Evidenz (SD-SYS-005) | **Hoch** — Mertens et al. 2021 (d=0,43) vs. Maier et al. 2022 / Szaszi et al. 2022 (keine verlässliche Evidenz nach Publication-Bias-Korrektur) |
| ST-0255, ST-0256 | Widersprüchliche Evidenz (Autoren-Selbstkorrektur) | Mittel — Thaler/Sunstein relativieren die Organspende-Default-These selbst (Spanien-Fehlklassifikation) |
| MEC-0024 (Sludge) | Externe Validierung ausstehend | Mittel — zwei konvergente Feldstudien, keine Multi-Labor-Replikation, unvollständige Primärquellenangaben |
| A-0054, A-0055 | Externe Validierung ausstehend | Mittel — keine saubere Kontrollbedingung bzw. Multi-Labor-Replikation |
| A-0053 (Re-Prüfung) | Offene Forschungsfrage | Niedrig — CKM-Mindestschwelle weiterhin nicht erfüllt |
| Mehrere Sekundärzitate | Unbelegte Annahme | Niedrig — Rebate-Redemption-Studie, Dynarski-Studie, provinzielle-Normen-Studie ohne vollständige bibliografische Angabe |
| Durchgängig (alle B-0013-Objekte) | Kulturelle Generalisierung / Transferlücke | Hoch — Public-Policy-/Altersvorsorge-Kontext, kein direkter B2B-Vertriebstest |

---

## 7. SD-SYS-005 — Repository-Lücken-Schließung (gesonderte Dokumentation)

Wie im Auftrag explizit gefordert, wurde die Existenz von SD-SYS-005 in `00_project/SCIENTIFIC_DEBT.md` gründlich selbst verifiziert, statt sich auf den ersten Grep-Befund des Auftraggebers zu verlassen.

**Befund:** Bestätigt — SD-SYS-005 wurde in mindestens 5 Repository-Dateien als geplant/existierend referenziert (`ACADEMIC_RECOVERY_REPORT_PACK_2_4.md` Zeile 201 kündigt "Neue Sektion... Mertens-Kontroverse (SD-SYS-005)" an; `changelog.md`, `CODEX_AUDIT_2026-07.md`, `SALES_CODEX_1_0_PROGRAM.md` und `SESSION_LOG.md` referenzieren SD-SYS-005 als bestehenden Eintrag), aber `SCIENTIFIC_DEBT.md` selbst enthielt vor dieser Buchanalyse nur die Abschnitte SD-SYS-001 bis SD-SYS-003 als tatsächlich geschriebene `####`-Unterabschnitte (verifiziert per Volltext-Grep auf `SD-SYS-00\d`). Der vollständig recherchierte, für SD-SYS-005 vorgesehene Inhalt lag bereits ausformuliert in `ACADEMIC_RECOVERY_REPORT_PACK_2_4.md` Abschnitt 1.3 vor (inklusive vollständiger Zitation: Mertens, Herberz, Hahnel & Brosch 2021, PNAS, d=0,43, 95%-CI [0,38; 0,48]; Maier et al. 2022, PNAS; Kodierfehler-Korrektur mit Bezug zur zurückgezogenen Shu et al. 2012-Studie).

**Vorgehen:** Der bereits recherchierte Inhalt wurde NICHT neu erfunden oder verändert, sondern unverändert in einen neuen `#### SD-SYS-005`-Abschnitt in `SCIENTIFIC_DEBT.md` überführt (eingefügt nach SD-SYS-003, vor der Academic-Recovery-Sprint-Sektion) und um die eigenständige Re-Verifikation aus B-0013 (Maier et al. 2022 vollständige Zitation, plus Szaszi et al. 2022 als zusätzliche, im ursprünglichen Recovery-Report nur am Rande erwähnte zweite Reanalyse) ergänzt.

**Zusätzlich entdeckt:** SD-SYS-004 wird ebenfalls in mehreren Dateien außerhalb von `SCIENTIFIC_DEBT.md` referenziert (`ACADEMIC_RECOVERY_PLAN.md`, `CODEX_AUDIT_2026-07.md`, `SALES_CODEX_1_0_PROGRAM.md`, `SESSION_LOG.md`, `peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`) als "Publication Bias (kommerzielle Studien)"-Kategorie mit CEB/Challenger- und Tethr/JOLT-Einträgen — jedoch ohne einen eigenen `#### SD-SYS-004`-Überschriftenabschnitt in `SCIENTIFIC_DEBT.md` selbst (die zugehörigen Einträge scheinen stattdessen direkt in den B-0004/B-0006-Buchsektionen oder an anderer Stelle eingearbeitet worden zu sein, ohne die erwartete SD-SYS-004-Überschrift zu tragen). Dies ist eine weitere, von SD-SYS-005 unabhängige Repository-Inkonsistenz, die außerhalb des Scopes dieser B-0013-Buchanalyse liegt (kein B-0013-Objekt referenziert SD-SYS-004) — hiermit zur Kenntnis dokumentiert und an eine höhere Sprint-Ebene zur Bereinigung weitergegeben, nicht eigenständig repariert, um den Auftrags-Scope (nur SD-SYS-005 war explizit beauftragt) nicht zu überschreiten.

---

## 8. Neue Literaturquellen

Vollständig eingetragen in `05_research/LITERATURE_INDEX.md`, Abschnitt A (Entscheidungspsychologie & Behavioral Economics). Zusammenfassung:

| APA-Zitation | Verifikationsstatus | Unterstützt |
|---|---|---|
| Madrian, B.C. & Shea, D.F. (2001). The Power of Suggestion: Inertia in 401(k) Participation and Savings Behavior. *Quarterly Journal of Economics*, 116(4), 1149–1187. | Verifiziert (2026-07-02) | MEC-0002 (Erweiterung), P-0048, MOD-0011 |
| Johnson, E.J. & Goldstein, D. (2003). Do Defaults Save Lives? *Science*, 302(5649), 1338–1339. | Verifiziert (2026-07-02) | MEC-0002 (Erweiterung), P-0048, MOD-0011 |
| Thaler, R.H. & Benartzi, S. (2004). Save More Tomorrow™: Using Behavioral Economics to Increase Employee Saving. *Journal of Political Economy*, 112(S1), S164–S187. | Verifiziert (2026-07-02) | MEC-0002 (Erweiterung), MEC-0001, A-0054, P-0049 |
| Maier, M., Bartoš, F., Stanley, T.D., Shanks, D.R., Wagenmakers, E.-J. & Harris, A.J.L. (2022). No Evidence for Nudging after Adjusting for Publication Bias. *PNAS*, 119(31), e2200300119. | Verifiziert (2026-07-02) | SD-SYS-005, MEC-0002 (Kontext-Vorbehalt), MOD-0011 |
| Szaszi, B. et al. (2022). No Reason to Expect Large and Consistent Effects of Nudge Interventions. *PNAS*, 119(31), e2202261119. | Verifiziert (2026-07-02) | SD-SYS-005 (zweite konvergente Reanalyse) |
| Asch, S.E. (1956). Studies of Independence and Conformity. *Psychological Monographs*, 70(9), 1–70. | Verifiziert (2026-07-02) | MEC-0006 (Erweiterung) |
| Bond, R. & Smith, P.B. (1996). Culture and Conformity: A Meta-Analysis of Studies Using Asch's Line Judgment Task. *Psychological Bulletin*, 119(1), 111–137. | Verifiziert (2026-07-02) | MEC-0006 (Erweiterung, erste Meta-Analyse-Referenz) |
| Haggag, K. & Paci, G. (2014). Default Tips. *American Economic Journal: Applied Economics*, 6(3), 1–19. | Verifiziert (2026-07-02) | MEC-0021 (Erweiterung, Reaktanz-Grenzbedingung), MOD-0011 |
| Mertens, S., Herberz, M., Hahnel, U.J.J. & Brosch, T. (2021). The Effectiveness of Nudging. *PNAS*, 119(1). | Re-verifiziert (2026-07-02, bereits 2026-07-01 in Research Pack 2 verifiziert) | SD-SYS-005, MEC-0002 (Kontext-Vorbehalt), MOD-0011 |
| Thaler, R.H. & Sunstein, C.R. (2008/2021). Nudge / Nudge: The Final Edition. | Vollständig verarbeitet als SRC-0013 | Alle B-0013-Objekte |

**Nicht bibliografisch vollständig verifizierbar (offene Fragen, nicht erfunden):** Rebate-Redemption-Studie ("Everyone Believes in Redemption", im Buch ohne vollständige Autorenangabe zitiert), Dynarski-Studie (vollständige Zitation im Fließtext nicht angegeben), provinzielle-Normen-Studie (2008, Hotel-Handtuch-Kontext, ohne vollständige Autorenangabe im Buch). Alle drei in MEC-0024 bzw. MEC-0006/MEC-0021 als offene bibliografische Fragen markiert statt spekulativ vervollständigt.

---

## 9. Publikationsbias-Risiken

Struktur wie VAL-0013 Punkt 6, hier als eigenständiger Berichtsabschnitt mit drei klar getrennten Ebenen:

1. **Mertens/Maier/Szaszi-Kontroverse zur generellen Nudge-Wirksamkeit (SD-SYS-005, direkt DIESES Buch betreffend):** Mertens et al. (2021, PNAS) berichten einen Gesamteffekt von Choice-Architecture-Interventionen von d=0,43 über >200 Studien. Zwei unabhängige, 2022 in PNAS publizierte Reanalysen (Maier et al.; Szaszi et al.) finden nach Publication-Bias-Korrektur (Robust Bayesian Meta-Analysis) keine verlässliche Evidenz für einen generellen, konsistenten Effekt. Zusätzlich existiert eine publizierte Korrektur zum Mertens-Originalpapier wegen Kodierfehlern (ein Datensatz stammte aus der 2021 zurückgezogenen Studie Shu et al. 2012 — dieselbe Studie, die bereits als Kontext für die B-0012-Ariely-Integritätsfrage dokumentiert ist, hier jedoch als unabhängiges Datenqualitätsproblem der Mertens-Meta-Analyse relevant). Dies ist der wissenschaftlich bedeutsamste Befund dieser Buchanalyse und wurde bewusst NICHT verwendet, um MEC-0002 auf ein höheres Evidenzlevel zu heben, trotz mehrfacher neuer Stützbelege aus B-0013 selbst.
2. **Autoren-Selbstkorrektur zur Organspende-Default-These (direkt DIESES Buch betreffend, Kap. 13):** Thaler und Sunstein relativieren ihre eigene, in früheren Auflagen prominent vertretene These, dass Opt-out-Länder (Presumed Consent) durchgängig höhere effektive Organspenderaten zeigen als Opt-in-Länder. Die vielzitierte Spanien-als-Erfolgsbeispiel-Darstellung wird korrigiert: Spaniens hohe Raten werden primär auf Transplantationsinfrastruktur (nicht auf den rechtlichen Default) zurückgeführt; zusätzlich wird zwischen hartem und weichem Presumed Consent unterschieden. Dies ist kategorial verschieden von Punkt 1 (keine externe Kontroverse, sondern eine im Quelltext selbst dokumentierte, transparente Selbstkorrektur der Autoren) — als besonders wertvoller methodischer Befund prominent in der MEC-0002-Erweiterung dokumentiert.
3. **Unabhängig replizierte/fundierte Kernbefunde:** Der allgemeine Default-Effekt-Grundmechanismus (Madrian & Shea 2001, Johnson & Goldstein 2003 als Grundlagenstudien) gilt als robust repliziert und ist von der Mertens/Maier/Szaszi-Kontroverse (die sich auf Choice-Architecture-Interventionen INSGESAMT bezieht) nicht direkt in gleicher Schärfe betroffen. Save More Tomorrow (Thaler & Benartzi 2004) verfügt über einen longitudinalen Feldexperiment-Befund mit Follow-up über mehrere Jahre. Asch-Konformitätsforschung (1956, Bond & Smith 1996 Meta-Analyse über 17 Länder) ist eine der am breitesten replizierten Erkenntnisse der Sozialpsychologie überhaupt.

**Sauberkeit der Trennung:** Kein Statement/Objekt in dieser Buchanalyse überträgt die generelle Publikationsbias-Kontroverse pauschal auf die spezifischen Einzelbefunde zum Default-Effekt — jede Erweiterung prüft ihre jeweilige spezifische Evidenzbasis eigenständig, analog zur B-0012-Vorgehensweise bei der Ariely-Integritätsfrage.

---

## 10. Neue Tier-1-Kandidaten (nur Dokumentation, keine Eintragung)

Gemäß Auftrag: Diese Quellen werden hier nur als mögliche Kandidaten für `00_project/ACADEMIC_RECOVERY_PLAN.md` dokumentiert — eine tatsächliche Eintragung dort ist außerhalb des Scopes dieser Buchanalyse.

- **Madrian & Shea (2001) — The Power of Suggestion:** Starker Kandidat für Tier-1. Eine der meistzitierten Default-Effekt-Gründungsarbeiten in der Verhaltensökonomie, mit klarer Feldstudien-Evidenz (Unternehmensdaten, nicht Labor) und breiter Rezeption über die Behavioral-Economics-Literatur hinaus. Würde die Default-Erweiterung von MEC-0002 zusätzlich absichern.
- **Johnson & Goldstein (2003) — Do Defaults Save Lives?:** Mittlerer bis starker Kandidat — kurze, aber extrem einflussreiche Science-Publikation. Eine Tier-1-Prüfung müsste die Boundary-Conditions-Frage (Spanien-Fehlklassifikation) explizit mit aufnehmen, um keine unkritische Übernahme der ursprünglichen Länder-Interpretation zu riskieren.
- **Bond & Smith (1996) — Culture and Conformity Meta-Analysis:** Mittlerer Kandidat — stärkt die interkulturelle Generalisierbarkeit von MEC-0006 erheblich (17 Länder, 133 Studien) und wäre ein wertvoller Beitrag zur B2B-internationalen-Transferfrage, die in mehreren Scientific-Debt-Einträgen als offen markiert ist.
- **Maier et al. (2022) / Szaszi et al. (2022) — Publikationsbias-Reanalysen:** Bereits vollständig als SD-SYS-005 dokumentiert (siehe Abschnitt 7); eine Tier-1-Aufnahme wäre sinnvoll, falls der Codex künftig eine dedizierte Methodik-Sektion zu Meta-Analyse-Qualitätsprüfung einführt (aktuell nicht vorgesehen, außerhalb des Scopes dieser Buchanalyse).

---

## Status

Abgeschlossen — 2026-07-02
