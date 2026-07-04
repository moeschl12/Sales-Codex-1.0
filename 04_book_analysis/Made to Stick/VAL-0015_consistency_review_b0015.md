# VAL-0015 -- Konsistenzpruefung B-0015 (Made to Stick: Why Some Ideas Survive and Others Die)

## Pruefungs-ID

VAL-0015

## Buch

B-0015 -- Made to Stick: Why Some Ideas Survive and Others Die (Heath & Heath 2007)

## Datum

2026-07-02

## Pruefumfang

Alle Knowledge Objects aus B-0015:
- SRC-0015 (1 neue Quelle)
- ST-0287 bis ST-0309 (23 Statements)
- A-0057 bis A-0060 (4 neue Assumptions)
- MEC-0026, MEC-0027, MEC-0028, MEC-0029 (4 neue Mechanismen)
- MEC-0018 (1 Erweiterung, Querverweis auf MEC-0027)
- P-0052, P-0053 (2 neue Prinzipien)
- P-0036 (1 Erweiterung, Gap-Theorie-Querverweis)
- T-0047 (1 neue Technik)
- MOD-0012 (1 neues Modell, SUCCESS-Framework)

---

## Pruefpunkte

### 1. ID-Konsistenz

Alle neuen IDs im zugewiesenen Bereich per Verzeichnis-Listing verifiziert: ST-0287-ST-0309 (lueckenlos, 23 Objekte), A-0057-A-0060 (lueckenlos, 4 Objekte, naechste freie ID nach A-0056), MEC-0026-MEC-0029 (lueckenlos, 4 Objekte, naechste freie ID nach MEC-0025), P-0052-P-0053 (lueckenlos, 2 Objekte, naechste freie ID nach P-0051), T-0047 (naechste freie ID nach T-0046), MOD-0012 (naechste freie ID nach MOD-0011 -- diese ID war bereits seit B-0014/VAL-0014 explizit fuer B-0015 reserviert worden). Keine Doppelbelegungen, keine Luecken. EXTEND-Operationen auf MEC-0018 und P-0036 korrekt als Erweiterungsabschnitte (nicht als neue Dateien) durchgefuehrt und im jeweiligen Objekt mit Datum/Quelle gekennzeichnet.

**Ergebnis: PASS**

### 2. Quellenzuordnung

Alle neuen Objekte referenzieren SRC-0015 als Source ID. Externe Primaerquellen innerhalb des Buchs korrekt als Sekundaerzitate ausgewiesen und, soweit moeglich, per WebSearch verifiziert (Camerer/Loewenstein/Weber 1989, Hinds 1999, Loewenstein 1994, Kang et al. 2009, Ekman & Friesen 1975, Green & Brock 2000, Small/Loewenstein/Slovic 2004/2007, Maier et al. 2023 Replikationsstudie, Tversky & Shafir 1992). Newton (1990) und Bechky (1999) korrekt als Dissertationsquellen mit unvollstaendig verifizierbarem Publikationsstatus markiert (⚠), nicht spekulativ vervollstaendigt. Keine erfundenen bibliografischen Angaben identifiziert.

**Ergebnis: PASS**

### 3. Evidenzklassen-Vergabe

| Objekt | Vergabe | Angemessenheit |
|---|---|---|
| MEC-0026 (Curse of Knowledge, neu) | E3 | Korrekt: vier konvergente Studiendesigns (Camerer/Loewenstein/Weber, Newton, Hinds, Bechky), aber keine Metaanalyse und zwei Quellen mit ⚠ unvollstaendig verifizierbarem Status -- konservativ nicht auf E4 gehoben |
| MEC-0027 (Gap-Theorie, neu) | E3 | Korrekt: Loewenstein 1994 (theoretische Synthese) und Kang et al. 2009 (Einzelstudie mit fMRT) -- Einzelstudien-Konvergenz, keine Metaanalyse, keine Ueberhoehung |
| MEC-0028 (Konkretheits-Encoding, neu) | E3 | Korrekt: Rubin/Paivio-Tradition und Stanford-Speakers-Experiment als Kernbelege; Identifiable-Victim-Anwendungsfall EXPLIZIT mit Replikationsvorbehalt (Maier et al. 2023) versehen, nicht in die Haupt-Evidenzbewertung eingerechnet |
| MEC-0029 (Narrative Transportation, neu) | E3 | Korrekt: Green & Brock 2000 als Gruendungsstudie, Klein (Flugsimulator-Funktion) als zweite unabhaengige Anwendung; UCLA-Studie mit ⚠ Zitationsluecke korrekt gekennzeichnet, nicht ueberbewertet |
| P-0052 (Glaubwuerdigkeit durch testbare Nachweise) | E3 | Korrekt: Basis MEC-Cluster Autoritaet (bestehend) + neue interne Glaubwuerdigkeits-Statements (Sinatra-Test, Wendy's), kein Evidenz-Upgrade ueber die Basis der Einzelbelege hinaus |
| P-0053 (Konkretheit gegen Curse of Knowledge) | E3 | Korrekt: direkte Ableitung aus MEC-0026 + MEC-0028 (OR-Regel erfuellt durch Kombination zweier MECs) |
| MOD-0012 (SUCCESS-Framework, neu) | E3 | Korrekt: Einzelkomponenten E3, Gesamtmodell als Integrationsrahmen nicht separat getestet -- analog zur etablierten Praxis bei MOD-0002/0010/0011, kein unbegruendetes Evidenz-Upgrade fuer das Container-Modell selbst |
| MEC-0018, P-0036 (Erweiterungen) | Kein E-Level-Wechsel | Korrekt: beide Erweiterungen fuegen einen komplementaeren, aber empirisch eigenstaendig gestuetzten Mechanismus als Querverweis hinzu, ohne die bestehende Kernevidenz zu veraendern |

**Ergebnis: PASS**

### 4. Kanonisierungs-Konsistenz

EXTEND-Entscheidungen geprueft:
- MEC-0018 EXTEND (Querverweis auf MEC-0027, Gap-Theorie als komplementaerer Aufmerksamkeitsmechanismus): Korrekt -- vollstaendige Abgrenzung nach Zeitprofil (kurzes Privileged-Moment-Fenster vor der Botschaft vs. anhaltende Spannung waehrend der Botschaft) dokumentiert, keine Vermischung der Kausalstrukturen.
- P-0036 EXTEND (Gap-Theorie-Ergaenzung): Korrekt -- explizite Abgrenzung zwischen Focal-Importance-Heuristik (Salienz) und Spannungsreduktions-Motivation (Wissensluecke) dokumentiert, inklusive praktischer Kombinationshinweis ohne Prinzipien-Verschmelzung.

NEU-Entscheidungen geprueft:
- MEC-0026 (Curse of Knowledge): Vollstaendige Canonicalization-Rejection-Pruefung gegen MEC-0020 (Perspektivuebernahme-Asymmetrie durch Macht), MEC-0018 und MEC-0012 durchgefuehrt und dokumentiert. Kernunterschied zu MEC-0020: struktureller (Wissen) statt motivationaler (Macht) Mechanismus, durch Newtons Befund (Motivation beseitigt den Effekt NICHT) empirisch gestuetzt. Alle vier CKM-Bedingungen erfuellt. **NEU gerechtfertigt.**
- MEC-0027 (Gap-Theorie der Neugier): Vollstaendige Abgrenzung zu MEC-0018 (Pre-Suasion) dokumentiert -- unterschiedlicher Stimulus (Wissensluecke vs. Opener-Reiz), unterschiedliches Zeitprofil (anhaltend vs. kurzes Fenster), unterschiedliche Moduationsbeziehung (invers-U-foermige Vorwissensabhaengigkeit ohne Entsprechung in MEC-0018). **NEU gerechtfertigt.**
- MEC-0028 (Konkretheits-Encoding): Abgrenzung zu MEC-0012 (Dual-Process) und MEC-0015 (Feature Overload) dokumentiert -- orthogonale Dimensionen (Kodierungspfad-Anzahl vs. Verarbeitungsmodus bzw. Options-Anzahl). Chunking (Miller 1956) und Identifiable Victim Effect korrekt als eingebettete Anwendungsfaelle statt eigener MECs eingeordnet. **NEU gerechtfertigt.**
- MEC-0029 (Narrative Transportation): Abgrenzung zu MEC-0018 (Pre-Suasion) und MEC-0007 (Liking-Transfer) dokumentiert -- Immersions-/Gegenargumentations-Verdraengungsmechanik ist weder identisch mit assoziativem Priming noch mit affektivem Sympathie-Transfer. **NEU gerechtfertigt.**
- P-0052 (Glaubwuerdigkeit durch testbare Nachweise) und T-0047 (Testable-Credentials-Technik): Erfuellen OR-Regel durch Kombination bestehender Autoritaets-MECs mit neuen Statements (Sinatra-Test, Wendy's-Beispiel); klare Abgrenzung von externer Autoritaetszuschreibung (Cialdini-Cluster) zu interner/textimmanenter Glaubwuerdigkeit dokumentiert. **NEU gerechtfertigt.**
- P-0053 (Konkretheit gegen Curse of Knowledge): Erfuellt OR-Regel durch Kombination MEC-0026 + MEC-0028. **NEU gerechtfertigt.**
- MOD-0012 (SUCCESS-Framework): Vollstaendige Pruefung gegen MOD-0008 (Pre-Suasion-Modell, zeitliche Sequenz) und MOD-0009 (Pink ABC-Modell, Sender-Dispositionen) dokumentiert -- MOD-0012 beschreibt Botschafts-Eigenschaften (Was), kategorial verschieden von Wann (MOD-0008) und Wer (MOD-0009). Mindestschwelle (≥3 verknuepfte Prinzipien) erfuellt. **NEU gerechtfertigt.**
- SUCCESS als MEC statt MOD: Geprueft und VERWORFEN -- Container-/Checklisten-Struktur, keine einzelne Stimulus-Prozess-Reaktion-Kette, wuerde CKM §6 verletzen. Korrekt als MOD klassifiziert.
- Chunking als eigener MEC: Geprueft und VERWORFEN -- Unterfall von MEC-0028, keine eigenstaendige Kausalstruktur.
- Identifiable Victim Effect als eigener MEC: Geprueft und VERWORFEN -- Spezialfall von MEC-0028 auf emotional-motivationaler Ebene, zusaetzlich durch gescheiterte Replikation (Maier et al. 2023) geschwaecht.
- Maslow-Beduerfnishierarchie-Reinterpretation als eigener MEC: Geprueft und VERWORFEN -- Attributionsfehler, keine eigenstaendige vertrieblich steuerbare Kausalkette; als Statement mit Verweis auf MOD-0012 dokumentiert.
- ELM (Petty & Cacioppo) als eigener MEC: Geprueft und VERWORFEN -- nicht direkt im Buch zitiert, waere Dopplung von MEC-0012 (Dual-Process).

**Ergebnis: PASS**

### 5. Nicht-Anlage-Dokumentation (CKM Sec. 9)

Geprueft: Alle fuenf verworfenen Kandidaten (ELM als MEC, Chunking als MEC, Identifiable Victim Effect als MEC, SUCCESS als MEC statt MOD, Maslow-Reinterpretation als MEC) sind mit expliziter Begruendung in analysis.md ("Verworfene Kandidaten") UND, soweit zutreffend, im jeweiligen "parent"-Objekt (MEC-0028, MOD-0012) dokumentiert.

**Ergebnis: PASS**

### 6. Replikations-/Publikationsbias-Dokumentation (Sprint-Prioritaet 2)

- **Rokia-Identifiable-Victim-Effect (Small/Loewenstein/Slovic):** Zentrale Kernevidenz fuer die EMOTIONAL-Komponente des Buches. Eine 2023 praeregistrierte Replikationsstudie (Maier et al., Collabra: Psychology, websuchverifiziert 2026-07-02) fand KEINE Stuetzung fuer den Effekt in der replizierten Form -- prominent als ⚠⚠-Warnhinweis in ST-0301 sowie in MEC-0028 (Grenzen) und analysis.md dokumentiert. Dies ist der wichtigste Einzelbefund der Priori­taet-2-Recherche dieser Buchanalyse.
- **Newton (1990) "Tappers and Listeners":** Als unveroeffentlichte oder nur teilweise verifizierbare Dissertationsquelle markiert (⚠), exakte Stichprobengroesse/Publikationsstatus nicht abschliessend verifizierbar -- als Scientific Debt dokumentiert statt spekulativ vervollstaendigt.
- **Bechky (1999):** Unveroeffentlichte Dissertation, nicht unabhaengig verifizierbar -- entsprechend konservativ (⚠) markiert.
- **Curse of Knowledge (Camerer/Loewenstein/Weber 1989):** Keine dem Codex bekannte Metaanalyse identifiziert (WebSearch durchgefuehrt, ergebnislos) -- E3 statt E4/E5, konservativ eingestuft.
- **Gap-Theorie (Loewenstein 1994, Kang et al. 2009):** Keine Metaanalyse identifiziert -- E3, Einzelstudien-Konvergenz statt systematischer Review.
- **B2B-Transfer-Luecke:** Durchgaengig in jedem neuen Objekt als Grenze markiert -- kein Experiment im Buch testet direkten B2B-Vertriebstransfer.
- **Autoren-Selbsteinschraenkung (Accuracy vs. Accessibility):** Das Buch benennt selbst einen Zielkonflikt zwischen Simplizitaet und fachlicher Praezision (Elektronenmodell-Beispiel) -- als im Quelltext selbst dokumentierte Grenze in analysis.md uebernommen, nicht verschwiegen.

**Ergebnis: PASS**

### 7. Grenzen-Dokumentation

Alle neuen Objekte enthalten einen expliziten Grenzen-Abschnitt (MEC-0026 bis MEC-0029, MOD-0012). Durchgaengige Transferluecke (B2B-Vertrieb nicht getestet) konsistent markiert. Survivorship-Bias-Risiko der zahlreichen Anekdoten/Fallstudien (Nordstrom, Southwest, Sony, Jared/Subway) explizit in SRC-0015 (Quellenklasse-Begruendung) und analysis.md (Grenzen der Quelle) benannt, nicht unkritisch uebernommen.

**Ergebnis: PASS**

### 8. Ethisches Risiko

Keine ethisch riskanten Techniken oder Manipulationsmuster in B-0015 identifiziert, die eine gesonderte Kennzeichnung erfordert haetten (im Unterschied zu B-0012/B-0014, wo Diskriminierungs-/Hormonforschungsbefunde markiert werden mussten). Die "Kidney Heist"-Urban-Legend und weitere Legenden sind im Buch selbst korrekt als Fiktion markiert und wurden im Codex entsprechend NICHT als Tatsachenbehauptungen uebernommen.

**Ergebnis: PASS**

### 9. Beobachtung/Interpretation-Trennung

Alle Statements (ST-0287 bis ST-0309) trennen Originalaussage/Paraphrase (Beobachtung) von "Moegliche Annahmen"/"Moegliche Prinzipien" (Interpretation). Keine Vermischung identifiziert.

**Ergebnis: PASS**

### 10. Freitext-Mechanismenreferenzen

Alle Verweise auf Mechanismen in ST-, A-, P-, T- und MOD-Objekten erfolgen per ID (MEC-00XX), keine Freitext-Referenzen ohne ID-Anker identifiziert.

**Ergebnis: PASS**

---

## Gesamtergebnis

**STATUS: BESTANDEN** -- alle 10 Pruefpunkte PASS. Keine Blocker.

## Nicht blockierende Restpunkte

1. **Newton (1990) und Bechky (1999) bibliografisch nicht vollstaendig verifizierbar** -- als Scientific Debt dokumentiert (siehe SCIENTIFIC_DEBT.md, Sektion B-0015).
2. **Rokia-Identifiable-Victim-Effect-Replikationsversagen** -- prominent dokumentiert, aber nicht abschliessend aufgeloest, ob der urspruengliche Effekt unter anderen Bedingungen doch repliziert werden koennte.
3. **MOD-0012-Gesamtmodell nicht separat als Integrationsrahmen getestet** -- konsistent mit der bereits etablierten Praxis bei MOD-0002/0010/0011, als Grenzen-Eintrag dokumentiert.
4. **Konfliktfall zwischen SUCCESS-Komponenten nicht quantifiziert** -- keine Prioritaetsregel, falls zwei Komponenten (z. B. Simplizitaet vs. Konkretheit) in seltenen Faellen um begrenzten Botschaftsraum konkurrieren.

## Status

Abgeschlossen -- 2026-07-02
