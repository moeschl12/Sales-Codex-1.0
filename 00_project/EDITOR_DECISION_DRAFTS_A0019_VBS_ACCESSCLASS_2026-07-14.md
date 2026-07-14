# Editor Decision Drafts — A-0019/Harrison, AR-011/Value-Based Selling, Zugriffsklasse Uni-Digitalisate

**Dokumentklasse:** Governance / Scientific Debt Reduction — Entscheidungsvorbereitung (keine Ausführung)
**Task-Type:** T11_SCIDEBT / T8-nah (Entscheidungsvorbereitung, keine eigene Herausgeberentscheidung)
**Auftrag:** Drei unabhängige Editorentscheidungen aus `00_project/ACADEMIC_RECOVERY_CONSOLIDATION_REPORT.md` (Teil 3: ED-AR-6, ED-AR-8, ED-AR-10) vertiefen und als Entscheidungsvorlagen aufbereiten — parallel zu einer separaten Bearbeitung durch Codex.
**Bearbeitet von:** Claude / Cowork
**Datum:** 2026-07-14
**Kein Commit, kein Push. Keine Wissensobjekte geändert. Keine neuen Objekte angelegt. MEC-0014 nicht angefasst.**

**Nachgelagerter Review- und Entscheidungsstatus (2026-07-14):** Codex hat die drei Vorlagen gegen den aktiven Bestand geprüft; Felix hat alle drei in korrigierter Fassung angenommen. Korrekturen gegenüber dem ursprünglichen Entwurf: Aus Harrison et al. wird keine Richtung oder Größenordnung eines möglichen CEB-Bias abgeleitet; die Access-Provenance-Stufen heißen „Zugangsweg 1/2/3“ statt „Klasse A/B/C“, um eine Verwechslung mit den Quellenklassen zu vermeiden. Umsetzung siehe A-0019, SRC-0024, `ACADEMIC_RECOVERY_PLAN.md`, `SCIENTIFIC_DEBT.md`, `ACADEMIC_RECOVERY_CONSOLIDATION_REPORT.md`, Codex Source Standard und Source Template.

---

## Hinweis zum Repository-Zustand während dieser Sitzung

Der Repository-Status (`git status`) zeigt zum Zeitpunkt dieser Bearbeitung parallele, unversionierte Änderungen an `MEC-0015`, `MEC-0016`, `MEC-0018`, `P-0002`, `SRC-0016`, `ST-0310`/`ST-0311`, `SRC-0023` u. a. — konsistent mit einer parallelen Bearbeitung durch Codex an anderen Editorentscheidungen aus demselben Konsolidierungsbericht (u. a. ED-AR-1 bis ED-AR-3). Diese Objekte wurden für die vorliegende Bearbeitung **nicht gelesen, nicht bewertet und nicht verändert** — sie liegen außerhalb des hier zugewiesenen Scopes (A-0019/SD-SYS-004, AR-011/VBS, Zugriffsklasse). Diese Beobachtung dient nur der Nachvollziehbarkeit, nicht der Bewertung von Codex' Arbeit.

---

## Entscheidung 1 — A-0019 / SD-SYS-004: Warnhinweis um Harrison et al. (2017) ergänzen?

### Kontext

A-0019 ("Kundenloyalität entsteht primär durch die Sales Experience") trägt seit dem External Audit Resolution Sprint (2026-07-03) einen sichtbaren Abschnitt "⚠ Hinweis: Publication Bias", der pauschal auf `SCIENTIFIC_DEBT.md`, SD-SYS-001 (Replikationsrisiko) und SD-SYS-004 (Publication Bias kommerzieller Studien) verweist — ohne konkrete Quellenangabe.

SD-SYS-004 selbst wurde durch AR-002 (2026-07-13) final kategorisiert: **Kategorie 3 — "plausibel, aber nicht sales-spezifisch nachgewiesen."** Zentrale Kalibrierungsquelle dieser Kategorisierung ist SRC-0024 (Harrison, Banks, Pollack, O'Boyle & Short, 2017, *Journal of Management* 43(2), 400–425): eine akademische Methodenstudie, die Publication Bias **im strategischen Management** (nicht Marketing/Vertrieb, nicht proprietäre Anbieterstudien) empirisch quantifiziert — Korrelations-Inflation im Mittel zwischen 0,00 und 0,19, themenabhängig, nicht universell. Nur das vollständige, verifizierte Abstract wurde gelesen (legitimer Green-Open-Access-Zugriff über das UR Scholarship Repository, PDF-Volltext technisch nicht extrahierbar — kein Zugriffsproblem, sondern Werkzeuglimitation). AR-002 selbst hat die Ergänzung von A-0019 um diesen Verweis bereits als **nicht ausgeführten Editorvorschlag** dokumentiert (außerhalb des damaligen Dateiscopes, der `03_knowledge_base/` nicht einschloss).

### Fachlicher Nutzen

- Der bestehende A-0019-Warnhinweis ist aktuell generisch ("Publication Bias, siehe SD-SYS-001/SD-SYS-004") — ein Leser des Objekts selbst erfährt nicht, dass es eine konkrete, akademisch quantifizierte Kalibrierungsquelle gibt, ohne zusätzlich `SCIENTIFIC_DEBT.md` vollständig zu durchsuchen.
- Ein konkreter Verweis auf eine bezifferte Größenordnung (0,00–0,19 Korrelations-Inflation) gibt dem Leser einen greifbaren Maßstab dafür, wie stark Publication Bias selbst in einem regulär referierten akademischen Feld wirken kann — nützlich als Kontext für die Einordnung der unbelegten, aber plausiblen CEB-Risiken.
- Erhöht die Traceability des Objekts, ohne neue Recherche zu erfordern (die Quelle ist bereits vollständig im Repository dokumentiert).

### Risiko der Überdehnung

- Harrison et al. (2017) untersucht eine **andere Disziplin** (strategisches Management, nicht Vertrieb/Marketing), einen **anderen Mechanismus** (selektive Publikation innerhalb des regulären akademischen Peer-Review-Prozesses, nicht Sponsoring-Bias bei proprietären, nicht-akademischen Anbieterstudien) und **nicht die CEB-Studie selbst**. AR-002 stuft die Übertragbarkeit ausdrücklich als "Plausibilitätsschlussfolgerung durch Analogie, kein direkter Beweis" ein.
- Eine unpräzise Formulierung in A-0019 könnte fälschlich den Eindruck erwecken, es gäbe jetzt einen direkten akademischen Beleg für Publication Bias bei CEB/Challenger — das wäre eine Verletzung der Repository-Grundregel "Erfinde niemals Quellen oder Fakten" bzw. eine unzulässige Verschärfung einer bereits als Analogie gekennzeichneten Aussage.
- Da nur das Abstract von SRC-0024 gelesen wurde (kein Volltext), darf die Ergänzung ausschließlich Abstract-Ebene-Aussagen wiedergeben — keine darüberhinausgehenden Details (z. B. zu Methodik oder betroffenen Einzelthemen) behaupten.

### Optionen

1. **A-0019 um einen präzise kalibrierten Zusatzsatz ergänzen**, der Harrison et al. (2017) explizit als Analogie-/Kalibrierungsquelle benennt, mit ausdrücklicher Klarstellung der Nicht-Übertragbarkeit auf CEB/Challenger selbst.
2. **Unverändert lassen** — der bestehende generische Warnhinweis mit Verweis auf `SCIENTIFIC_DEBT.md` ist bereits sachlich korrekt und ausreichend; eine Konkretisierung wäre eine Komfort-, keine Notwendigkeitsverbesserung.
3. **Nur `SCIENTIFIC_DEBT.md` präzisieren** (dort ist Harrison et al. bereits vollständig dokumentiert; keine A-0019-Änderung), falls Felix eine Änderung an Wissensobjekten grundsätzlich vermeiden möchte, auch bei geringem Risiko.

### Empfehlung

**Option 1**, mit strikt kalibrierter Formulierung — der fachliche Nutzen (konkrete, bezifferte Kalibrierungsquelle direkt im Objekt sichtbar) überwiegt das Überdehnungsrisiko, sofern die Formulierung die Analogie-Natur explizit macht statt sie zu glätten. Dies deckt sich mit dem bereits in AR-002 dokumentierten, aber nicht ausgeführten Vorschlag.

### Genauer Formulierungsvorschlag (nicht ausgeführt)

Ergänzung am Ende des bestehenden Abschnitts "⚠ Hinweis: Publication Bias (Kommerzielle Quelle)" in A-0019:

> **Kalibrierungsquelle (nicht sales-spezifisch):** Eine akademische Methodenstudie zu Publication Bias in der benachbarten Disziplin strategisches Management (Harrison, Banks, Pollack, O'Boyle & Short, 2017, *Journal of Management* 43(2), 400–425, SRC-0024) weist einen messbaren, aber themenabhängigen Effekt nach — Korrelations-Inflation im Mittel zwischen 0,00 und 0,19. **Dies ist eine Plausibilitätsanalogie, kein direkter Nachweis für die hier verwendete CEB-Studie:** Harrison et al. (2017) prüft weder Vertriebs-/Marketingforschung noch die CEB-Daten selbst und erlaubt keine Aussage über Richtung oder Größenordnung eines möglichen Bias in der CEB-Studie. Vollständige Herleitung: `00_project/AR-002_COMPLETION_REPORT.md`, `SCIENTIFIC_DEBT.md` (SD-SYS-004).

### Betroffene Dateien (bei Ausführung — nicht in dieser Sitzung geändert)

- `03_knowledge_base/assumptions/A-0019_kundenloyalitaet_entsteht_durch_sales_experience.md` (Ergänzung im bestehenden Warnhinweis-Abschnitt)
- Optional, nicht zwingend: `00_project/SCIENTIFIC_DEBT.md` (Cross-Reference-Vermerk "A-0019 verweist jetzt konkret auf SRC-0024") — SD-SYS-004 selbst ist bereits vollständig dokumentiert und muss inhaltlich nicht geändert werden.

---

## Entscheidung 2 — AR-011 / Value-Based Selling: dauerhaft oder vorläufig außerhalb Scope?

### Kontext

AR-011 (2026-07-14) hat Keränen, Totzek, Salonen & Kienzler (2023), *Advancing value-based selling research in B2B markets*, vollständig im Volltext verarbeitet und redaktionell entschieden: Value-Based Selling (VBS) bleibt "vorerst außerhalb des aktuellen Codex-Scopes". Diese Formulierung ist bereits so in `SCIENTIFIC_DEBT.md` und `ACADEMIC_RECOVERY_PLAN.md` verankert — es handelt sich aber um eine **redaktionelle**, nicht um eine von Felix ratifizierte **Herausgeberentscheidung**. Die Quelle selbst ist ein konzeptionelles Theorie-Integrations-Paper ohne eigene Empirie ("no data was used"), das acht geliehene Theorien auf VBS anwendet und 32 ungeprüfte Forschungsfragen ableitet.

### Scope-Argumente

**Für dauerhaften Ausschluss:**
- VBS ist in dieser Quelle strukturell eine B2B-**Preisstrategie**-Forschungsagenda (Wertquantifizierung, Pricing, Vertragsgestaltung, organisationale Adoption) — ein anderer Gegenstandsbereich als der aktuelle Codex-Scope (Vertrieb, Verkauf, Verhandlung, Kommunikation, **Käuferpsychologie**, siehe `PROJECT_BOOTSTRAP.md`).
- Alle acht in der Quelle verwendeten Theorien sind entweder (a) bereits im Codex über autoritativere Primärquellen in anderem Kontext vertreten (Agency Theory/MEC-0014, Mental Accounting/SRC-0014, Social Exchange/MEC-0030) oder (b) treten nur als ungeprüfte Forschungsvorschläge auf, nicht als etablierte Befunde.
- Keine eigene Empirie in der Quelle — nichts erfüllt die Statement-Extraktions-Schwelle des Codex.

**Für vorläufigen Ausschluss (Wiedervorlage möglich):**
- Der Quellentyp selbst ("Forschungsagenda") ist per Definition ein Vorläufer künftiger empirischer Arbeiten — ein dauerhafter Ausschluss würde implizit unterstellen, dass keine der 32 Forschungsfragen je Codex-relevant werden könnte, was angesichts von drei individuenbezogenen, käuferpsychologisch relevanten Theorien (Equity, Framing, Mental Accounting) nicht zwingend ist.
- Eine künftige Primärstudie, die eine dieser Forschungsfragen empirisch testet, wäre möglicherweise direkt an ein bestehendes Codex-Objekt anschlussfähig, ohne dass der Scope selbst erweitert werden müsste (reine Objekterweiterung statt neues Themenfeld).
- Die bereits im Repository verwendete Formulierung ("vorerst") impliziert schon Nicht-Permanenz — eine Verschärfung zu "dauerhaft" wäre eine stärkere, schwerer reversible Policy-Festlegung, ohne dass ein neuer Befund dies zwingend nahelegt.
- Die Kosten der Offenhaltung sind gering: Es entsteht kein aktiver Rechercheaufwand, nur ein dokumentierter Prüfstatus mit klar benannten Wiedervorlage-Triggern.

### Mögliche spätere Trigger für Wiederaufnahme

1. Eine der 32 Forschungsfragen aus Keränen et al. (2023) — insbesondere mit Equity-, Framing- oder Mental-Accounting-Bezug (individuenbezogene Ebene) — wird durch eine künftige Primärstudie empirisch getestet, deren Ergebnis direkt an ein bestehendes Codex-Objekt anschlussfähig ist.
2. Felix erweitert den Codex-Scope explizit in Richtung B2B-Preisstrategie/Pricing/Wertquantifizierung — eine eigenständige, von AR-011 unabhängige Grundsatzentscheidung.
3. Eine Folgestudie mit direktem Buying-Center-/Käuferpsychologie-Bezug verknüpft VBS empirisch mit bereits etablierten Codex-Mechanismen (z. B. MEC-0002 Verlustaversion, MEC-0014 Konsens, MEC-0030 Vertrauensbildung).

### Empfehlung

**Vorläufige Formulierung beibehalten** ("derzeit/vorerst außerhalb Scope"), **nicht** auf "dauerhaft ausgeschlossen" verschärfen — bei gleichzeitiger expliziter Benennung der drei oben genannten Trigger, damit "vorerst" nicht zu einer unbefristeten, unklaren Schwebe wird, sondern an konkrete, prüfbare Bedingungen geknüpft ist.

### Empfohlene Governance-Formulierung (nicht ausgeführt)

Ergänzung in `SCIENTIFIC_DEBT.md` (VBS-Zeile) und `ACADEMIC_RECOVERY_PLAN.md` (AR-011-Abschnitt), jeweils identisch:

> **Herausgeberentscheidung (offen, hier nur vorgeschlagen):** Value-Based Selling bleibt bis auf Weiteres außerhalb des Codex-Scopes — als "derzeit außerhalb Scope", nicht als "dauerhaft ausgeschlossen" zu verstehen. Eine Wiedervorlage ist angezeigt, sobald (a) eine der 32 in Keränen et al. (2023) vorgeschlagenen Forschungsfragen empirisch getestet und direkt an ein bestehendes Codex-Objekt anschlussfähig wird, oder (b) der Codex-Scope durch eine eigenständige Herausgeberentscheidung auf B2B-Preisstrategie/Pricing erweitert wird. Ohne einen dieser beiden Trigger ist keine automatische erneute Prüfung vorgesehen — VBS wird nicht routinemäßig in künftigen Academic-Recovery-Sprints erneut aufgegriffen.

### Betroffene Dateien (bei Ausführung — nicht in dieser Sitzung geändert)

- `00_project/SCIENTIFIC_DEBT.md` (VBS-Zeile, Ergänzung um Governance-Formulierung + Trigger)
- `00_project/ACADEMIC_RECOVERY_PLAN.md` (AR-011-Abschnitt, identischer Zusatz)
- `00_project/AR-011_COMPLETION_REPORT.md` bleibt unverändert (abgeschlossenes Sitzungsprotokoll wird nicht rückwirkend editiert)

---

## Entscheidung 3 — Zugriffsklasse "Universitäts-/Fakultätsseiten-Digitalisate": Governance-Regel

### Kontext

Seit AR-013 (2026-07-13, Präzedenzfall SRC-0016, Tversky & Shafir 1992, Zugriff über `bear.warrington.ufl.edu`) wurde eine Zugriffsklasse wiederholt verwendet, die weder offizieller Verlags-Open-Access noch Sci-Hub/Schattenbibliothek ist: legitim erreichbare, aber nicht offiziell als Open Access gekennzeichnete Digitalisate auf Universitäts-Kurs- oder Fakultätsseiten. AR-007 selbst hat dies als "dokumentierte Restunsicherheit" benannt und eine gesonderte Governance-Entscheidung angeregt, falls Felix die Klasse enger regeln möchte.

**Bestandsaufnahme der tatsächlich verwendeten Zugriffswege (AR-007, AR-008, AR-009, AR-010, AR-013):**

Bei genauer Prüfung zerfällt die in den AR-Berichten pauschal als "Zugriffsklasse Uni-/Fakultätsseiten" bezeichnete Kategorie in **drei fachlich unterschiedliche Unterklassen**, die im bisherigen Bestand unter demselben Namen geführt werden, aber ein unterschiedliches Legitimitäts- und Unsicherheitsprofil haben:

| Unterklasse | Beispiele aus dem Bestand | Charakteristik |
|---|---|---|
| **(a) Offizielle institutionelle Repositorien** | AR-009 (University of Ottawa `ruor.uottawa.ca`, Dissertation als "Author Accepted Manuscript"); AR-010 (Cranfield CERES `dspace.lib.cranfield.ac.uk`, Author Accepted Manuscript, CC BY-NC 4.0); AR-006 (SMU `ink.library.smu.edu.sg`); AR-011 (JYX Jyväskylä, offizielle publizierte Fassung, CC BY 4.0) | Von der Universitätsbibliothek selbst betriebene, formale Green-Open-Access-Repositorien mit Lizenzkennzeichnung und Autoren-Deposit-Nachweis. Etablierter, in der akademischen Praxis allgemein akzeptierter Standardweg. |
| **(b) Autoren-Selbstarchivierung auf eigener Homepage/Lab-Seite** | AR-004 (Sheth, `jagsheth.com`, mit explizitem öffentlichem Autoren-Kommentar zur Nachdruckerlaubnis); AR-008 (Weingarten et al., `socialactionlab.org`, autoren-/labgehostetes PDF) | Der Artikel-Autor selbst stellt sein eigenes Werk auf seiner Homepage bereit — ebenfalls etablierte, akzeptierte Praxis (Green-Open-Access via Self-Archiving), besonders eindeutig bei explizit bestätigter Autorisierung (Sheth-Fall). |
| **(c) Drittanbieter-Kurs-/Fakultätsseiten ohne erkennbaren Autoren- oder Institutionsbezug zum jeweiligen Werk** | AR-013 (bear.warrington.ufl.edu — Kurs-/Dozentenseite der University of Florida, nicht Autor Tversky/Shafir); AR-007 (UCI-Fakultätsseite für Tversky & Kahneman 1974, U-Puget-Sound-Kursseite für Kahneman & Tversky 1979, Stanford-Kursseite für Tversky & Kahneman 1981 — in keinem Fall ist die hostende Person Autor des Artikels); AR-008 (MIT-Kursseite für Bargh, Chen & Burrows 1996) | Eine Lehrperson stellt für den eigenen Seminar-/Kursgebrauch einen Scan/ein PDF eines **fremden** Artikels bereit. Weder offizielles institutionelles Repositorium noch Autoren-Selbstarchivierung. Öffentlich auffindbar und nicht durch technische Zugriffsschutz-Umgehung erreicht, aber ohne erkennbare explizite Verlags- oder Autorenautorisierung für genau diese Verbreitungsform. |

Bei allen drei Unterklassen gilt durchgehend: kein Sci-Hub, keine technische Zugriffsschutz-Umgehung, keine Nutzung erkennbar nicht-autorisierter Kopien (mehrfach dokumentiert abgelehnt, z. B. Papermill-Hosting/Google-Groups in AR-004, Kurs-Hosting-Spiegel in AR-006, Scribd/"Anna's Archive" in AR-014). Der Unterschied betrifft ausschließlich die **Herkunfts- und Autorisierungsklarheit** der jeweiligen Kopie, nicht die grundsätzliche Zulässigkeit des Zugriffswegs.

### Fachliche Einschätzung

- Unterklassen (a) und (b) entsprechen etablierter akademischer Praxis und sollten ohne Einschränkung zulässig bleiben.
- Unterklasse (c) ist der eigentliche Kern der von AR-007 aufgeworfenen Restunsicherheit: technisch frei zugänglich und nicht durch Umgehung erreicht, aber ohne erkennbare Autorisierung durch Verlag oder Autor für genau diese Verbreitungsform. Dies ist urheberrechtlich nicht eindeutig, auch wenn es sich klar von einer Zugriffsschutz-Umgehung unterscheidet — eine rein binäre Regel ("zulässig"/"nicht zulässig") würde diese Zwischenposition nicht sauber abbilden.
- Bereits etablierte Praxis im Bestand zeigt implizit eine Präferenzreihenfolge: Wenn sowohl ein institutionelles Repositorium/eine Autorenseite **als auch** eine Kurs-/Fakultätsseiten-Kopie desselben Werks identifiziert wurden, wurde die Kurs-Seiten-Kopie bewusst verworfen (AR-006: SMU-Repository statt `eclass.aueb.gr`-Kursspiegel). Diese Präferenz ist bisher nicht explizit als Regel formuliert, sondern nur einzelfallweise praktiziert.

### Optionen

1. **Uneingeschränkt zulässig** — alle drei Unterklassen werden weiterhin wie bisher gleichwertig behandelt, keine neue Regel.
2. **Differenzierte Regel** — (a) und (b) uneingeschränkt zulässig; (c) nur zulässig, wenn zusätzlich (i) kein legitimerer Weg (a)/(b) auffindbar ist UND (ii) das Ergebnis im SRC-Objekt mit einem expliziten, standardisierten Restunsicherheitsvermerk gekennzeichnet wird.
3. **Nicht zulässig** — Unterklasse (c) wird künftig ausgeschlossen; bei fehlendem Zugriff über (a)/(b)/offiziellen Verlagszugang gilt die Quelle als blockiert (analog AR-003/AR-005/AR-014).

### Empfehlung

**Option 2** — differenzierte Regel mit Präferenzreihenfolge (a) > (b) > (c) und verpflichtendem Restunsicherheitsvermerk für (c). Begründung: Die bisherige Praxis hat bereits mehrfach demonstriert, dass Recherchen ohne (c) teils komplett blockiert wären (AR-013-Präzedenzfall, AR-007 alle drei Quellen, AR-008 Bargh 1996) — ein vollständiger Ausschluss (Option 3) würde einen erheblichen Teil des bisher erzielten Academic-Recovery-Fortschritts faktisch rückgängig machen bzw. hätte ihn von vornherein verhindert. Ein uneingeschränktes Fortführen ohne Kennzeichnung (Option 1) lässt die von AR-007 selbst benannte Restunsicherheit unadressiert.

### Vorschlag für eine klare Regel (nicht ausgeführt)

> **Zugriffslegitimität für Quellenbeschaffung (Vorschlag):**
> 1. **Zugangsweg 1 — Offizielle institutionelle Repositorien** (Universitätsbibliotheks-Repositorien, DSpace/EPrints-Instanzen, formale Green-OA-Kennzeichnung): regulär zulässig; Textversion, Lizenz und Repository dokumentieren, soweit ausgewiesen.
> 2. **Zugangsweg 2 — Autoren-Selbstarchivierung** (Homepage/Lab-Seite des Artikel-Autors selbst): regulär zulässig; bei explizit bestätigter Autorisierung als "bestätigt" kennzeichnen, sonst die Autorenbereitstellung benennen, ohne eine weitergehende Lizenzbehauptung.
> 3. **Zugangsweg 3 — Drittanbieter-Kurs-/Fakultätsseiten ohne erkennbaren Autoren-/Institutionsbezug zum Werk**: nur zulässig, wenn (i) kein Zugangsweg 1 oder 2 sowie kein regulärer Verlagszugang auffindbar ist, UND (ii) im SRC-Objekt ein expliziter Restunsicherheitsvermerk aufgenommen wird (Formulierungsvorschlag: *"Zugangsweg 3 — Drittanbieter-Kurs-/Fakultätsseite ohne erkennbare Autoren- oder Verlagsautorisierung für diese Verbreitungsform. Kein Sci-Hub, keine Zugriffsschutz-Umgehung; öffentlich frei auffindbar. Die Autorisierung dieser spezifischen Kopie ist nicht verifizierbar."*).
> 4. **Präferenzreihenfolge:** Bei mehreren identifizierten Zugangswegen zum selben Werk ist regulärer Verlagszugang/Open Access vor Zugangsweg 1, vor Zugangsweg 2, vor Zugangsweg 3 zu bevorzugen.
> 5. Unverändert bleibt: kein Sci-Hub, keine Schattenbibliotheken, keine erkennbar nicht-autorisierten Drittkopien (z. B. Papermill-Hosting, Kurs-Spiegel-Duplikate ohne Primärstatus) — diese bleiben unter allen drei Klassen ausgeschlossen.

### Umsetzungsvorschläge bei Zustimmung (nicht ausgeführt, nur benannt)

1. Neuer Abschnitt "Zugriffslegitimität (Access Provenance)" in `01_framework/03_source_standard/codex_source_standard.md` — dies wäre eine **Framework-Änderung** und erfordert nach `TASK_TYPES.md` (T2) eine gesonderte, explizite Freigabe durch Felix, keine Ausführung im Rahmen dieser T11-nahen Entscheidungsvorbereitung.
2. Neues Feld "Zugangsweg / Access Provenance" im Quellentemplate `01_framework/08_templates/source_template.md` für künftige SRC-Objekte.
3. **Gesonderter Folgeauftrag (nicht Teil dieses Vorschlags):** rückwirkende Kennzeichnung bereits bestehender Klasse-C-Fälle im Bestand (mindestens SRC-0016 [AR-013], SRC-0029/SRC-0030/SRC-0031 [AR-007], SRC-0032 [AR-008, Bargh 1996]) — dies wäre eine Änderung an bestehenden Quellenakten und liegt außerhalb des für die vorliegende Sitzung freigegebenen Scopes ("keine Wissensobjekte ändern").

### Betroffene Dateien (bei Ausführung — nicht in dieser Sitzung geändert)

- `01_framework/03_source_standard/codex_source_standard.md` (neuer Abschnitt — Framework-Änderung, erfordert T2-Freigabe)
- Optional: `01_framework/08_templates/source_template.md` (neues Feld)
- Optional, gesonderter Folgeauftrag: `02_sources/studies/SRC-0016_choice_under_conflict_tversky_shafir.md`, `SRC-0029_...`, `SRC-0030_...`, `SRC-0031_...`, `SRC-0032_...` (Access Provenance bei späterer Revision nachtragen)

---

## Abschlussbericht

**Kernergebnis:** Drei Entscheidungsvorlagen wurden anhand des tatsächlichen Repository-Bestands ausgearbeitet — keine davon wurde ausgeführt.

1. **A-0019/Harrison et al. (2017):** Ergänzung empfohlen (Option 1), mit einer präzise kalibrierten Formulierung, die die Analogie-Natur der Quelle explizit macht, um Überdehnung zu vermeiden. Konkreter Formulierungsvorschlag liegt vor.
2. **AR-011/Value-Based Selling:** Vorläufige Formulierung ("derzeit außerhalb Scope") wird empfohlen, nicht "dauerhaft" — mit drei explizit benannten Wiedervorlage-Triggern, um "vorerst" nicht zu einer unbefristeten Schwebe werden zu lassen.
3. **Zugriffsklasse Uni-/Fakultätsseiten-Digitalisate:** Die pauschale Bezeichnung zerfällt bei genauer Prüfung in drei Unterklassen mit unterschiedlichem Legitimitätsprofil (institutionelle Repositorien / Autoren-Selbstarchivierung / Drittanbieter-Kursseiten). Eine differenzierte Regel mit Präferenzreihenfolge und verpflichtendem Restunsicherheitsvermerk für die dritte Klasse wird empfohlen — vollständiger Ausschluss würde einen erheblichen Teil des bisherigen Academic-Recovery-Fortschritts (u. a. AR-007, AR-008, AR-013) rückwirkend infrage stellen.

**Betroffene Dateien in dieser Sitzung (nur diese eine neue Datei):**
- `00_project/EDITOR_DECISION_DRAFTS_A0019_VBS_ACCESSCLASS_2026-07-14.md` (diese Datei, neu)

**Nicht geänderte Bereiche:** `03_knowledge_base/` (keine Wissensobjekte geändert, insbesondere nicht A-0019, MEC-0014 wurde nicht angefasst), `02_sources/` (keine Quellenakten geändert), `01_framework/` (keine Framework-/Template-Änderungen ausgeführt — nur als Umsetzungsvorschlag benannt), `00_project/SCIENTIFIC_DEBT.md`, `00_project/ACADEMIC_RECOVERY_PLAN.md`, `00_project/AR-011_COMPLETION_REPORT.md` (alle unverändert — Formulierungsvorschläge liegen nur in dieser Datei vor).

**Ursprünglicher Entwurfsstatus:** Kein Commit, kein Push durch Claude. Nachgelagerte Prüfung, Herausgeberentscheidung und Umsetzung erfolgten durch Codex/Felix am 2026-07-14.

---

*Erstellt: 2026-07-14 | Entscheidungsvorbereitung (parallel zu Codex) | KI-Redaktion Sales Codex (Claude/Cowork)*
