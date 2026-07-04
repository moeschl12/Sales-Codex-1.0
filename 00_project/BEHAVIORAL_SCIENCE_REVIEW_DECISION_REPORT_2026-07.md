# Behavioral Science Review Sprint — Editor Decision Report

**Dokumentklasse:** Governance / Editor Decision
**Datum:** 2026-07-02
**Auslöser:** Unabhängiges wissenschaftliches Gutachten zum Behavioral Science Expansion Sprint (SPR-0003), Datei `Wissenschaftliche Begutachtung des Behavioral Science Sprints.md` (extern zugeliefert, kein Repository-Artefakt).
**Geprüfte Eingabedokumente:** `04_synthesis/SPR-0003_Behavioral_Science_Synthesis/SPR-0003_BEHAVIORAL_SCIENCE_SYNTHESIS.md`, das externe Gutachten, sowie zur Verifikation jeder einzelnen Reviewer-Aussage der tatsächliche Repository-Zustand (MEC-0025, MOD-0011, MOD-0012, `SCIENTIFIC_DEBT.md`, `LITERATURE_INDEX.md`, `canonical_knowledge_model.md`, `codex_knowledge_model.md`).
**Rolle dieses Dokuments:** Verbindliche Editor Decision. Das Gutachten stellt ausschließlich die Position des externen Reviewers dar; bei Widersprüchen zwischen Gutachten und dieser Decision gilt diese Decision. Dieses Dokument selbst verändert **keine** Repository-Datei — es dokumentiert ausschließlich die Entscheidung. Umsetzung erfolgt erst nach Fertigstellung dieses Reports (Aufgabe 2).
**Methodischer Hinweis:** Jede Reviewer-Aussage wurde gegen den tatsächlichen, aktuellen Repository-Zustand geprüft (nicht gegen die Erinnerung/Annahme, was im Repository stehen müsste). An drei Stellen (ED-002, ED-007) weicht der reale Zustand vom Gutachten ab — dies wird unten explizit dokumentiert, nicht geglättet (Repository-Grundregel: „Dokumentiere Widersprüche statt sie zu glätten").

---

## Zusammenfassung

| ED | Gegenstand | Editor Decision |
|---|---|---|
| ED-001 | MEC-0025 Umbenennung | Übernehmen |
| ED-002 | B-0011 Scientific Debt erweitern | Übernehmen (teilweise bereits erfüllt — siehe Abweichungshinweis) |
| ED-003 | MOD-0011 Klassifikation | Teilweise übernehmen |
| ED-004 | MOD-0012 Klassifikation | Teilweise übernehmen |
| ED-005 | Boundary Conditions Individual→Organisation | Übernehmen |
| ED-006 | Ariely Scientific Debt Status | Teilweise übernehmen |
| ED-007 | Literature Index bereinigen | Übernehmen (bereits weitgehend erfüllt — siehe Abweichungshinweis) |
| ED-008 | Neue Kategorien PRX/TAX | Ablehnen |

---

## ED-001 — MEC-0025 Umbenennung

### Reviewer Position

Die Benennung „Fairness-Verzicht" für MEC-0025 sei wissenschaftlich falsch und irreführend: Der Bestrafende verzichte nicht auf Fairness, sondern fordere sie aktiv ein und zahle dafür einen persönlichen Preis. Das etablierte akademische Konstrukt heiße „altruistische Bestrafung" (altruistic punishment) bzw. „costly punishment". Die Beibehaltung beschädige die wissenschaftliche Glaubwürdigkeit des Codex.

### Wissenschaftliche Bewertung

Zutreffend. Die Fachliteratur zum Ultimatum-Spiel (Fehr & Gächter 2002 u. a.) verwendet durchgängig „altruistic punishment" / „costly punishment" für exakt dieses Verhalten: Der Ablehnende verzichtet nicht auf Fairness, sondern sanktioniert deren Verletzung unter Inkaufnahme eigener Kosten. Der Codex-eigene Mechanismus-Text (MEC-0025) beschreibt den Kausalpfad bereits korrekt („aktive kostenpflichtige Bestrafung eines als unfair wahrgenommenen Angebots") — der Widerspruch liegt ausschließlich im **Namen**, nicht im beschriebenen Mechanismus selbst. Die inhaltliche Definition, Mechanismus-Kette und Evidenzbasis (Güth et al. 1982; Sanfey et al. 2003; Oosterbeek/Sloof/van de Kuilen 2004) sind fachlich korrekt und bleiben unverändert gültig.

### Repository-Kompatibilität

Vollständig kompatibel. Reine Namens-/Titeländerung an einem bestehenden Objekt — keine neue Objekt-ID, keine neue Canonicalisierung, keine Framework-Änderung. Deckt sich mit CKM Abschnitt 4.1 (Erweiterung eines bestehenden Objekts: „eine neue Quelle... liefert eine neue Anwendungsbedingung" — hier: präzisiert die bereits vorhandene Definition terminologisch, ohne die kausale Struktur zu verändern).

**Boundary-Conditions-Prüfung (Zusatzauftrag):** Henrich et al. (2001, 2004) sind bereits vollständig in MEC-0025 dokumentiert — im Abschnitt „Wissenschaftliche Grundlage" (Literaturangabe), im Abschnitt „Grenzen" (erster Punkt: „Kulturell moduliert... Henrich et al.") und in den „Offenen Fragen". Ebenso in `SCIENTIFIC_DEBT.md` (B-0014-Sektion, Zeile „MEC-0025, P-0051 | Kulturelle Generalisierung | Henrich et al. (2001, 2004)...", Priorität **Hoch**) und in `LITERATURE_INDEX.md` (Sektion A, verifizierter Eintrag). Kein zusätzlicher Bedarf.

### Editor Decision

**ÜBERNEHMEN.**

### Begründung

Die Umbenennung korrigiert einen nominalen Fehler, ohne die kausale Struktur, die Evidenzbasis oder die Objekt-Identität zu verändern. Sie ist eine reine Präzisierung im Sinne von CKM 4.1, keine Neuanlage (CKM 4.2) und keine Zusammenführung (CKM 4.3). Die vom Herausgeber verlangte Prüfung der Henrich-Boundary-Conditions ergibt: bereits ausreichend dokumentiert, keine Ergänzung nötig.

### Betroffene Dateien

Innerhalb der erlaubten Dateikategorien (Aufgabe 2):

- `03_knowledge_base/mechanisms/MEC-0025_fairness_verzicht_ultimatum.md` (Titel, Name-Feld, Definitionstext, Mechanismus-Kette — Umbenennung in „Altruistische Bestrafung / Altruistic Punishment"; Dateiname/-pfad bleibt unverändert, da eine Pfadänderung eine Repository-Strukturänderung wäre, die außerhalb des Sprintauftrags liegt)
- `03_knowledge_base/models/MOD-0010_kahneman_kognitive_bias_karte.md` (referenziert MEC-0025 als „Fairness-Verzicht" in Kategorie 6 und im Vergleichstext — betroffene MOD-Datei, Umbenennung im Fließtext)
- `00_project/SCIENTIFIC_DEBT.md` (referenziert „Fairness-Verzicht" indirekt über MEC-0025-Kontext — Terminologie-Angleichung, keine inhaltliche Änderung)
- `00_project/changelog.md` (Eintrag zur Umbenennung)

**Außerhalb der erlaubten Dateikategorien für diesen Sprint (nicht Teil von Aufgabe 2 — siehe Folgeaufgaben):** `P-0051_fairness_schwelle_beachten.md`, `A-0056_fairness_normverletzung_motiviert_kostenpflichtige_bestrafung.md`, `ST-0275/0276/0277/0280/0285`, sowie die historischen B-0014-Sprintartefakte (`CANONICALIZATION_REPORT_B0014.md`, `BOOK_REVIEW_REPORT_B0014.md`, `VAL-0014_consistency_review_b0014.md`, `analysis.md`) referenzieren „Fairness-Verzicht" ebenfalls. Diese Dateitypen (P/A/ST, historische Sprintberichte) stehen nicht auf der für diesen Sprint freigegebenen Änderungsliste.

### Umsetzungsumfang

Klein — Textänderung an zwei bis drei Stellen in MEC-0025 (Titelzeile, Name-Feld, ggf. kurzer Klarstellungssatz zum Kausalpfad in der Definition), ein Fließtext-Update in MOD-0010, ein Terminologie-Hinweis in SCIENTIFIC_DEBT.md, ein Changelog-Eintrag.

### Folgeaufgaben

Terminologie-Nachziehung in P-0051, A-0056, den fünf betroffenen ST-Objekten und den historischen B-0014-Sprintartefakten ist als redaktioneller Nacharbeitspunkt zu dokumentieren (nicht Teil dieses Sprints, da diese Dateitypen nicht auf der Freigabeliste stehen). Empfehlung: eigener kleiner Folgesprint „Terminologie-Konsistenz MEC-0025" oder Erledigung im Rahmen des nächsten Consistency-Correction-Sprints.

---

## ED-002 — B-0011 (Emotional Intelligence) Scientific Debt erweitern

### Reviewer Position

Die wissenschaftlichen Kontroversen zu B-0011 fehlten im Codex: (a) Konstruktvalidität von Emotional Intelligence im Vergleich zu etablierten Persönlichkeitsmodellen (Big Five), (b) das gescheiterte Marshmallow-Replikationsexperiment (Watts, Duncan & Quan 2018), (c) die Ekman-Universalitätskontroverse gegenüber Barretts „Theory of Constructed Emotion". Das Sündenregister müsse entsprechend erweitert werden.

### Wissenschaftliche Bewertung

**Teilweise unzutreffend gegenüber dem aktuellen Repository-Zustand — dokumentierter Widerspruch, nicht geglättet:**

Bei Prüfung von `SCIENTIFIC_DEBT.md`, Sektion „B-0011 — Emotional Intelligence" (Zeilen 147–158), zeigt sich:

- **Marshmallow-Replikationsversagen:** Bereits vollständig dokumentiert als ST-0213, Kategorie „Replikationsrisiko", Priorität **Hoch**, mit korrektem Verweis auf Watts, Duncan & Quan (2018). Die Reviewer-Behauptung „wird im aktuellen Sündenregister komplett verschwiegen" trifft auf den aktuellen Repository-Zustand **nicht zu**.
- **Ekman/Barrett-Kontroverse:** Bereits vollständig dokumentiert als ST-0214, Kategorie „Widersprüchliche Evidenz", Priorität Mittel, mit korrektem Verweis auf Barretts „Theory of Constructed Emotion". Auch hier trifft die Reviewer-Behauptung eines fehlenden Eintrags **nicht zu**.
- **Konstruktvalidität EI vs. Big Five:** Hier hat der Reviewer recht — eine gezielte Repository-Suche (Volltextsuche über alle Dateien nach „Harms", „Credé", „Landy", „Locke", „Konstruktvalidität", „Big Five" im EI-Kontext) ergibt **keinen** Treffer. Dieser spezifische Scientific-Debt-Eintrag fehlt tatsächlich.

**Einordnung:** Zwei der drei vom Reviewer benannten Lücken existieren im aktuellen Repository-Stand nicht (mutmaßlich war der Gutachtenstand älter als der finale `SCIENTIFIC_DEBT.md`-Stand vom 2026-07-02, oder das Gutachten wertete nur die B-0011-Buchanalyse-Rohdaten statt der bereits fertig integrierten Sündenregister-Datei aus). Die dritte Lücke (Konstruktvalidität) ist real und relevant — die kritisierte „unkritische Übernahme" des Goleman-Konstrukts ist an dieser einen Stelle tatsächlich noch nicht durch einen eigenen Scientific-Debt-Eintrag abgesichert.

### Repository-Kompatibilität

Vollständig kompatibel mit dem bestehenden Scientific-Debt-Format (Tabellenzeile nach etabliertem Muster: Objekt-ID | Kategorie | Beschreibung | Priorität). MEC-0022 (Emotionale Ansteckung) selbst stützt sich bereits primär auf Hatfield/Cacioppo/Rapson, nicht auf Goleman — der neue Debt-Eintrag betrifft die Goleman-EQ-Rezeption in SRC-0011 allgemein, nicht MEC-0022 spezifisch.

### Editor Decision

**ÜBERNEHMEN** — mit der Präzisierung, dass nur der tatsächlich fehlende Teil (Konstruktvalidität) ergänzt wird; die beiden bereits vorhandenen Einträge (Marshmallow, Ekman/Barrett) bleiben unverändert bestehen.

### Begründung

Ein Scientific-Debt-Eintrag darf nicht doppelt angelegt werden (Repository-Grundregel gegen Redundanz, analog CKM-Objektidentitätsprinzip). Da zwei der drei Punkte bereits vollständig und korrekt dokumentiert sind, würde eine pauschale „Erweiterung um alle drei Punkte" zu Dubletten führen. Die Nicht-Übernahme unveränderter Punkte ist selbst eine Form von „Widersprüche dokumentieren statt glätten" — der Bericht hält fest, dass das Gutachten hier nicht mit dem aktuellen Stand übereinstimmt, statt dies stillschweigend zu übergehen. Emotionale Ansteckung (MEC-0022) wird ausdrücklich nicht entfernt oder inhaltlich verändert; Goleman bleibt in SRC-0011 als historische Sekundärquelle erhalten (keine Änderung an SRC-0011 vorgesehen oder nötig).

### Betroffene Dateien

- `00_project/SCIENTIFIC_DEBT.md` (neue Tabellenzeile in Sektion B-0011: Konstruktvalidität EI vs. Big Five, Kategorie „Unbelegte Annahme" bzw. „Offene Forschungsfrage", Priorität Hoch)
- `00_project/changelog.md` (Eintrag)

### Umsetzungsumfang

Klein — eine neue Tabellenzeile in `SCIENTIFIC_DEBT.md`, referenziert auf die vom Reviewer genannten Standardarbeiten (Harms & Credé 2010; Landy 2005; Locke 2005) mit dem Hinweis, dass diese Referenzen bislang nicht websuchverifiziert wurden (Repository-Regel: keine Quellen erfinden — die drei Zitate stammen aus dem Gutachten, nicht aus eigener Verifikation, und werden entsprechend als **nicht verifiziert** gekennzeichnet, nicht als geprüfte Primärquelle).

### Folgeaufgaben

Websuch-Verifikation von Harms & Credé (2010), Landy (2005) und Locke (2005) vor einer eventuellen Aufnahme in `LITERATURE_INDEX.md` als verifizierte Quelle. Bis dahin bleibt der Scientific-Debt-Eintrag mit Quellenvorbehalt.

---

## ED-003 — MOD-0011 (Choice Architecture) Klassifikation

### Reviewer Position

Choice Architecture erfülle nicht die wissenschaftstheoretischen Kriterien eines „Modells" (formales System mit prüfbaren kausalen Prädiktionen). Es sei eine Sammlung bestehender Mechanismen plus ein präskriptives Design-Framework, nie als Gesamtkonstrukt empirisch getestet, zusätzlich durch die SD-SYS-005-Publikationsbias-Kontroverse belastet. Empfehlung: Re-Klassifizierung als eigene Kategorie „PRX" (präskriptives Design-Framework).

### Wissenschaftliche Bewertung

Die epistemologische Beobachtung des Reviewers ist in der Sache korrekt: MOD-0011 ist kein empirisch getestetes Kausalmodell im strengen Sinne (prüfbare quantitative Prädiktionen). Das ist jedoch **kein Widerspruch zur bestehenden Codex-Definition** von „Modell" — dort gilt ein anderer, bereits im Repository seit Pilot 001 etablierter Maßstab.

### Repository-Kompatibilität

Geprüft gegen `01_framework/05_knowledge_model/canonical_knowledge_model.md` (das laut `codex_knowledge_model.md`-Kopfhinweis „maßgebliche, aktuell gültige" Wissensmodell-Dokument, siehe dortiger Consistency-Correction-Hinweis von 2026-07): Abschnitt 5 definiert die Mindestschwelle für „Modell (MOD)" als **„Mindestens drei verknüpfte Prinzipien. Kausallogische Struktur beschreibbar."** — nicht als „empirisch getesteter Prädiktionsapparat". MOD-0011 selbst dokumentiert unter „Mindestschwellen-Prüfung (CKM Abschnitt 5)" bereits explizit die Erfüllung dieser Schwelle (drei P-Objekte: P-0048, P-0049, P-0050) sowie unter „Kausallogische Struktur" ein beschreibbares Ablaufschema. Nach der **aktuell gültigen** Codex-eigenen MOD-Definition ist die Einordnung als MOD damit bereits zulässig — die vom Reviewer geforderte strengere, wissenschaftstheoretische Modell-Definition ist nicht die im Repository verankerte.

Eine neue Kategorie „PRX" existiert im Wissensmodell nicht (weder in `canonical_knowledge_model.md` noch in `codex_knowledge_model.md`) und würde CKM Abschnitt 10 verletzen („Die Einführung neuer Objekttypen [ist eine] Herausgeber-Entscheidung" — nicht redaktionell im Rahmen dieses Sprints zulässig).

### Editor Decision

**TEILWEISE ÜBERNEHMEN.**

### Begründung

Wie im Auftrag vorgegeben: keine sofortige Umklassifizierung, zuerst Prüfung der bestehenden MOD-Definition. Ergebnis der Prüfung: **Ja**, die bestehende MOD-Definition erlaubt die aktuelle Einordnung bereits (Mindestschwelle erfüllt, kausallogische Struktur vorhanden — beides bereits in MOD-0011 selbst dokumentiert). Konsequenz laut Auftrag: **Klassifikationshinweis ergänzen**, keine Frameworkänderung, keine neue Kategorie. Der Klassifikationshinweis macht die vom Reviewer zu Recht benannte Einschränkung explizit sichtbar, statt sie zu verschweigen: MOD-0011 ist ein Modell im Sinne der Codex-eigenen, strukturellen MOD-Definition (Bündelung verknüpfter Prinzipien mit beschreibbarer Kausallogik), nicht im Sinne eines formal-empirischen, prädiktiv getesteten Wissenschaftsmodells. Diese Unterscheidung war zuvor implizit (in „Grenzen" und „Evidenzlevel" bereits angedeutet: „Das GESAMTMODELL... ist nicht direkt getestet"), wird nun aber als eigener, benannter Klassifikationshinweis geführt.

### Repository-Kompatibilität (Zusatz)

Vollständig kompatibel — reine Ergänzung eines erklärenden Abschnitts in einer bestehenden MOD-Datei, keine Strukturänderung.

### Betroffene Dateien

- `03_knowledge_base/models/MOD-0011_choice_architecture_modell.md` (neuer Abschnitt „Klassifikationshinweis" oder Ergänzung im bestehenden „Evidenzlevel"-Abschnitt)
- `00_project/changelog.md`

### Umsetzungsumfang

Klein — ein neuer, kurzer Abschnitt in MOD-0011, kein Eingriff in Annahmen, Prinzipien, Techniken oder Mechanismen-Verknüpfungen des Modells.

### Folgeaufgaben

Reviewer-Empfehlung 7 aus SPR-0003 selbst („MOD-0011 und MOD-0012... vor Version 1.0 in einem künftigen Peer-Review-Sprint auf internen Konsistenzbedarf prüfen") bleibt unverändert gültig und wird durch diesen Klassifikationshinweis nicht ersetzt, sondern bestätigt.

---

## ED-004 — MOD-0012 (SUCCESS-Framework) Klassifikation

### Reviewer Position

Analog zu ED-003: SUCCESS sei kein Modell, sondern eine didaktisch-heuristische Taxonomie von Botschaftseigenschaften ohne nachgewiesene interaktive/multiplikative Kausalität zwischen den sechs Komponenten. Empfehlung: Re-Klassifizierung als „TAX" (heuristische Kommunikations-Taxonomie).

### Wissenschaftliche Bewertung

Identische Struktur wie ED-003. Die Beobachtung ist in der Sache korrekt (kein getesteter Interaktionseffekt zwischen den sechs SUCCESS-Komponenten), betrifft aber wiederum die strenge wissenschaftstheoretische Modell-Definition, nicht die Codex-eigene.

### Repository-Kompatibilität

Wie bei MOD-0011: `canonical_knowledge_model.md` Abschnitt 5 verlangt „mindestens drei verknüpfte Prinzipien, kausallogische Struktur beschreibbar". MOD-0012 dokumentiert unter „Mindestschwellen-Prüfung" die Erfüllung (P-0052, P-0053, erweitertes P-0036) sowie eine beschreibbare Kausallogik-Struktur. Die Mindestschwelle ist nach aktuell gültiger Definition erfüllt. Eine neue Kategorie „TAX" existiert nicht im Wissensmodell und würde CKM Abschnitt 10 verletzen.

### Editor Decision

**TEILWEISE ÜBERNEHMEN.**

### Begründung

Analog zu ED-003. Bestehende MOD-Definition erlaubt die aktuelle Einordnung bereits → Klassifikationshinweis ergänzen statt Umklassifizierung. MOD-0012 selbst dokumentiert die Einschränkung teilweise bereits („Grenzen": „Kein empirischer Test des SUCCESS-Frameworks als GESAMTMODELL... identifiziert"), der neue Klassifikationshinweis macht dies zusätzlich explizit als benannte Kategorie-Einordnung sichtbar, konsistent mit dem gleichlautenden Hinweis in MOD-0011.

### Betroffene Dateien

- `03_knowledge_base/models/MOD-0012_success_framework.md` (neuer Abschnitt „Klassifikationshinweis")
- `00_project/changelog.md`

### Umsetzungsumfang

Klein, identisch zu ED-003.

### Folgeaufgaben

Keine über ED-003 hinausgehenden. Beide Klassifikationshinweise sollten sprachlich konsistent gehalten werden (gleicher Textbaustein zur MOD-Definition, angepasst an die jeweilige Modellspezifik).

---

## ED-005 — Boundary Conditions: Transfer Individual → Organisation

### Reviewer Position

Der „fundamentale Ebenenfehler" (Level Error): Fast die gesamte experimentelle Basis der fünf Bücher beruht auf individueller Ebene (Studierende, Endverbraucher), während B2B-Enterprise-Kaufprozesse ein organisationales Gruppenphänomen (Buying Center) sind. Die unkritische Übertragung von Mechanismen wie emotionaler Ansteckung (MEC-0022), Anchoring (MEC-0021) oder Defaults (MEC-0002-Erweiterung) auf ein professionelles Einkaufsgremium — ohne Berücksichtigung von Ausschreibungsrichtlinien, Budgetfreigabegrenzen, Revisionspflichten, mikropolitischen Koalitionen — sei methodisch unsauber.

### Wissenschaftliche Bewertung

Zutreffend und bereits an mehreren Stellen im Repository in schwächerer, generischer Form vorhanden (durchgängige „B2B-Transfer nicht getestet"-Vermerke in praktisch jedem Sprint-Objekt). Der Reviewer benennt jedoch einen spezifischeren Punkt, der bisher **nicht** explizit dokumentiert ist: nicht nur, dass B2B-Wirksamkeit ungetestet ist, sondern dass **strukturelle Merkmale organisationaler Kaufprozesse** (formale Prozesse, Mehrpersonen-Gremien, Genehmigungsstufen) die Mechanismenwirkung plausibel **dämpfen** — ein qualitativ anderer, spezifischerer Hinweis als die bereits vorhandene generische Transferlücken-Dokumentation.

### Repository-Kompatibilität

Kompatibel mit dem bestehenden „Grenzen"-Abschnittsformat der MEC-Dateien. Erfordert keine neue Kategorie in `SCIENTIFIC_DEBT.md` (die Kategorie „Offene Forschungsfrage" bzw. „Kulturelle Generalisierung" — hier eher „Kontextgeneralisierung" — deckt dies ab, auch wenn keine dieser Kategorien exakt passt; es wird die bestehende Kategorie „Offene Forschungsfrage" verwendet, um keine neue Kategorie einzuführen).

### Editor Decision

**ÜBERNEHMEN** — mit enger Auslegung des Anwendungsbereichs auf die vom Reviewer selbst namentlich benannten Sprint-Objekte, um eine repositoryweite Massenänderung zu vermeiden.

### Begründung

Der Auftrag ist eindeutig: „ausschließlich an den betroffenen Sprint-Objekten", „keine repositoryweite Massenänderung". Der Reviewer selbst benennt in seiner Änderungsempfehlung 4 explizit nur drei Mechanismen namentlich: „Defaults, Anchoring und emotionaler Ansteckung" — das sind MEC-0002 (Default-Erweiterung), MEC-0021 (Anchoring) und MEC-0022 (Emotional Contagion). Diese enge Auslegung entspricht sowohl dem Wortlaut der Reviewer-Empfehlung als auch der Editor-Vorgabe „ausschließlich an den betroffenen Sprint-Objekten". Eine Ausweitung auf alle 16 im Sprint erweiterten oder 8 neu angelegten Mechanismen würde die Vorgabe „keine repositoryweite Massenänderung" verletzen.

### Betroffene Dateien

- `03_knowledge_base/mechanisms/MEC-0002_loss_aversion_and_status_quo_cost.md` (Ergänzung im bestehenden Boundary-Conditions-Abschnitt „B2B-Transfer-Lücke" um die spezifische organisationale Dämpfungshypothese)
- `03_knowledge_base/mechanisms/MEC-0021_anchoring_mechanismus.md` (neuer, kurzer Grenzen-Zusatz)
- `03_knowledge_base/mechanisms/MEC-0022_emotional_contagion_durch_facial_feedback.md` (Ergänzung im bestehenden „Grenzen"-Abschnitt)
- `00_project/changelog.md`

### Umsetzungsumfang

Klein bis mittel — je ein kurzer, klar als „Boundary Condition (Editor Decision ED-005, Behavioral Science Review Sprint)" gekennzeichneter Zusatzabsatz in drei bestehenden MEC-Dateien. Kein neues Objekt, keine E-Level-Änderung (die Dämpfungshypothese selbst ist nicht empirisch getestet, sondern eine plausible, aber unbelegte Randbedingung — wird entsprechend als „Offene Forschungsfrage", nicht als gesicherter Befund, formuliert).

### Folgeaufgaben

Analoge Ergänzung für die übrigen Sprint-Objekte (MEC-0023 bis MEC-0029, MOD-0011, MOD-0012) ist ein sinnvoller Kandidat für einen künftigen, eigenständigen „Boundary Conditions Sprint" — explizit nicht Teil dieses Sprints. Die in SPR-0003 Abschnitt 9, Punkt 3 bereits vom Sprint selbst vorgeschlagene „sprintübergreifende Übersicht bekannter Replikationsversagen" könnte um eine parallele Übersicht „bekannte Boundary Conditions Individual→Organisation" ergänzt werden.

---

## ED-006 — Ariely Scientific Debt Status

### Reviewer Position

Durch die erfolgreiche bibliografische Entkopplung von Ariely (Decoy-Effekt über Huber/Payne/Puto 1982, Endowment-Effekt über KKT 1990) könnten die bestehenden Scientific-Debt-Einträge zu MEC-0002 und MEC-0009 bezüglich Arielys Person „mit sofortiger Wirkung als erfolgreich geschlossen deklariert werden".

### Wissenschaftliche Bewertung

Teilweise zutreffend, aber zu weitgehend formuliert. Prüfung von `SCIENTIFIC_DEBT.md`, Sektion B-0012 (Zeile 167): Der bestehende Eintrag „Autoren-Integritätsrisiko" bezieht sich nicht ausschließlich auf MEC-0002/MEC-0009, sondern pauschal auf „SRC-0012 (Autor Dan Ariely, generell)" und dokumentiert bereits selbst eine differenzierte Bewertung — der Eintrag stellt bereits fest, dass Decoy-, Anchoring-, Zero-Preis- und Endowment-Effekt „NICHT direkt" von der Integritätsfrage betroffen sind, während die Ehrlichkeits-/Dishonesty-Forschungslinie (Kap. 11/12, ST-0241/242) explizit **weiterhin** betroffen bleibt und bewusst nicht in ein P/MEC-Objekt überführt wurde. Ein vollständiges „Schließen" des Eintrags würde diese zweite, nach wie vor bestehende Einschränkung unsichtbar machen. Zusätzlich bleibt das allgemeine Faktum eines dokumentierten Integritätsvorfalls bei diesem Autor (unabhängig von den entkoppelten Einzelmechanismen) ein dauerhaft dokumentationswürdiger Kontext, kein binär „erledigtes" Risiko.

### Repository-Kompatibilität

Kompatibel mit dem bestehenden Scientific-Debt-Format. Das im Auftrag vorgeschlagene Statuslabel „partially mitigated" existiert nicht als vordefinierter Wert in der Kategorienliste (Abschnitt „Kategorien" von `SCIENTIFIC_DEBT.md` enthält keine Status-Spalte, nur Kategorie/Beschreibung/Priorität) — es lässt sich jedoch unmittelbar in den bestehenden Beschreibungstext integrieren, ohne die Tabellenstruktur zu ändern.

### Editor Decision

**TEILWEISE ÜBERNEHMEN.**

### Begründung

Wie im Auftrag vorgegeben: nicht schließen. Stattdessen Prüfung, welche Risiken tatsächlich entschärft wurden: Die vier zentral genutzten Kernexperimente (Decoy, Anchoring/SSN, Zero-Preis, Endowment) sind — wie im bestehenden Eintrag bereits dokumentiert — durch unabhängige Gründungsquellen abgesichert und dadurch tatsächlich entschärft. Die Ehrlichkeits-Forschungslinie (Kap. 11/12) bleibt hingegen unverändert und explizit unberührt von dieser Entschärfung; dort wurde ohnehin nie ein P/MEC-Objekt angelegt (Nicht-Anlage-Dokumentation bereits vorhanden). Status wird auf „partially mitigated" präzisiert, mit expliziter Trennung: entschärft für die vier Kernmechanismen, unverändert offen für die generelle Autoren-Integritätsrisiko-Kategorie als solche.

### Betroffene Dateien

- `00_project/SCIENTIFIC_DEBT.md` (Sektion B-0012, bestehende Zeile „Autoren-Integritätsrisiko" — Statuspräzisierung im Beschreibungstext, keine neue Zeile)
- `00_project/changelog.md`

### Umsetzungsumfang

Klein — Textpräzisierung einer bestehenden Zeile, keine Strukturänderung, keine neue Kategorie.

### Folgeaufgaben

Keine unmittelbaren. Sollte bei einer künftigen B-0012-Nachprüfung (z. B. falls neue Ariely-bezogene Kontroversen bekannt werden) erneut evaluiert werden.

---

## ED-007 — Literature Index bereinigen

### Reviewer Position

Bibliographische Unschärfen: ein „unvollständiger und fragmentierter Literatureintrag zu Carmon & Ariely (2000)" sowie mehrere als „unverifiziert" geführte Quellen (zwei unveröffentlichte Stanford-Dissertationen: Newton 1990, Bechky 1999; eine unvollständige UCLA-Studie).

### Wissenschaftliche Bewertung

**Teilweise unzutreffend gegenüber dem aktuellen Repository-Zustand — dokumentierter Widerspruch, nicht geglättet:**

- **Carmon & Ariely (2000):** Prüfung von `LITERATURE_INDEX.md`, Sektion A, sowie der zugehörigen `ST-0229_endowment_effekt_duke_basketball_tickets.md`: Der Eintrag ist vollständig (vollständige APA-Zitation, Evidenztyp, Kernaussage, MEC-Zuordnung, Evidenzlevel E3, Verifikationsvermerk „Verifiziert 2026-07-02"). Ein fragmentierter oder unvollständiger Zustand konnte **nicht** bestätigt werden. Die Reviewer-Behauptung trifft auf den aktuellen Stand nicht zu.
- **Newton (1990) und Bechky (1999):** Bereits korrekt und explizit als nicht vollständig verifizierbar gekennzeichnet (`LITERATURE_INDEX.md` Sektion E, Bemerkungsspalte: „Nicht vollständig verifiziert" / „Nicht unabhängig verifiziert", zusätzlich in `SCIENTIFIC_DEBT.md` B-0015-Sektion als „Verifikationslücke" dokumentiert). Zusätzlich gibt es bereits eine zusammenfassende Sammelzeile am Dateiende („Nicht bibliografisch vollständig verifizierbar (offene Fragen, nicht erfunden): Newton (1990) und Bechky (1999)..."). Dieser Punkt ist bereits vollständig erfüllt.
- **UCLA-Studie (ST-0306):** Ebenfalls bereits in derselben Sammelzeile als „ohne vollständige Autorenangabe... exakte Autorenschaft nicht abschließend identifizierbar" dokumentiert. Bereits erfüllt.

**Einordnung:** Wie bei ED-002 scheint das Gutachten einen älteren oder unvollständigen Repository-Stand bewertet zu haben, oder die Prüfung erfolgte nicht gegen die tatsächliche `LITERATURE_INDEX.md`-Datei. Alle drei vom Reviewer benannten Einzelpunkte sind im aktuellen Stand (Version 1.2, Stand 2026-07-02) bereits korrekt als unresolved/unverifiziert gekennzeichnet.

### Repository-Kompatibilität

Vollständig kompatibel — der bestehende Verifikationsstatus-Mechanismus („verifiziert" / „codex-bestätigt" / „nicht verifiziert") deckt genau diesen Anwendungsfall bereits ab und wird korrekt angewendet.

### Editor Decision

**ÜBERNEHMEN** — im Sinne einer Bestätigungsprüfung ohne inhaltliche Änderung, da der geforderte Zielzustand bereits erreicht ist.

### Begründung

Der Auftrag lautet „Literature Index bereinigen. Nicht verifizierte Quellen bleiben als unresolved gekennzeichnet. Keine Quellen erfinden." Die Prüfung ergibt: Der Zielzustand ist bereits erreicht. Eine „Übernahme" bedeutet hier nicht neue Textänderungen, sondern die explizite Bestätigung und Dokumentation, dass die drei vom Reviewer benannten Punkte bereits repository-konform behandelt sind — inklusive der expliziten Klarstellung, dass die Carmon-&-Ariely-Kritik nicht nachvollzogen werden konnte. Eine spekulative „Reparatur" eines nicht bestehenden Problems würde gegen die Grundregel verstoßen, keine Fakten zu erfinden.

### Betroffene Dateien

- `05_research/LITERATURE_INDEX.md` (keine inhaltliche Änderung nötig; optional ein kurzer Prüfvermerk am Dateiende, dass die Reviewer-Punkte gegen den 2026-07-02-Stand verifiziert wurden)
- `00_project/changelog.md` (Eintrag: Prüfung durchgeführt, keine Korrektur nötig, Abweichung zum Gutachten dokumentiert)

### Umsetzungsumfang

Minimal — keine inhaltliche Korrektur, nur ein Prüfvermerk und Changelog-Eintrag.

### Folgeaufgaben

Keine.

---

## ED-008 — Neue Kategorien PRX / TAX

### Reviewer Position

MOD-0011 und MOD-0012 sollten aus der Kategorie „MOD" entfernt und als neue Objektkategorien „PRX" (präskriptives Design-Framework) bzw. „TAX" (heuristische Kommunikations-Taxonomie) neu angelegt werden.

### Wissenschaftliche Bewertung

Die zugrunde liegende epistemologische Beobachtung ist nachvollziehbar (siehe ED-003/ED-004) — die konkrete Lösung (neue Objektkategorien) ist jedoch eine Framework-Entscheidung von erheblicher Tragweite, keine Buchanalyse- oder Sprintebenen-Entscheidung.

### Repository-Kompatibilität

Nicht kompatibel mit dem Sprintauftrag. CKM Abschnitt 10 weist die „Einführung neuer Objekttypen" explizit als „Herausgeber-Entscheidung" außerhalb der redaktionellen Vergleichs- und Entscheidungslogik aus. Der Auftrag für diesen Sprint schließt „neue Kategorien" und „neue Objektarten" explizit unter „Nicht zulässig" aus.

### Editor Decision

**ABLEHNEN.**

### Begründung

Framework-Änderung. Außerhalb des Sprintumfangs. Eine Einführung neuer Objektkategorien hätte Auswirkungen auf das gesamte Wissensmodell (Vergleichslogik, Mindestschwellen, Evidenzklassen-Zuordnung, Beziehungstypen) und alle 12 bestehenden MOD-Objekte, nicht nur auf MOD-0011/MOD-0012 — eine Tragweite, die eine bewusste, eigenständige Herausgeber-Entscheidung mit eigenem Sprint erfordert, keine Nebenentscheidung innerhalb eines Review-Umsetzungssprints. Die inhaltliche Sorge des Reviewers wird stattdessen über die Klassifikationshinweise in ED-003/ED-004 adressiert, ohne das Framework zu ändern.

### Betroffene Dateien

Keine (Ablehnung ohne Umsetzung).

### Umsetzungsumfang

Keiner.

### Folgeaufgaben

Falls der Herausgeber die PRX/TAX-Unterscheidung grundsätzlich für sinnvoll hält, sollte dies als neue Open Decision in `OPEN_DECISIONS.md` erfasst werden (außerhalb dieses Sprints, da „Open Decisions ändern" explizit als nicht zulässig markiert ist). Dieser Report empfiehlt diesen Schritt, entscheidet ihn aber nicht.

---

## Übersicht: Umsetzungsplan für Aufgabe 2

| ED | Zu ändernde Dateien | Umfang |
|---|---|---|
| ED-001 | MEC-0025, MOD-0010, SCIENTIFIC_DEBT.md, changelog.md | Klein |
| ED-002 | SCIENTIFIC_DEBT.md, changelog.md | Klein |
| ED-003 | MOD-0011, changelog.md | Klein |
| ED-004 | MOD-0012, changelog.md | Klein |
| ED-005 | MEC-0002, MEC-0021, MEC-0022, changelog.md | Klein–Mittel |
| ED-006 | SCIENTIFIC_DEBT.md, changelog.md | Klein |
| ED-007 | LITERATURE_INDEX.md (optional Prüfvermerk), changelog.md | Minimal |
| ED-008 | Keine | — |

Zusätzlich nach Abschluss aller Einzeländerungen: `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md` (Governance-Nachführung, wie in allen bisherigen Sprints üblich).

---

*Bericht erstellt: 2026-07-02. Ausschließlich Editor-Entscheidungsdokumentation — keine Repository-Datei außer dieser wurde in diesem Schritt verändert (Aufgabe 1). Umsetzung folgt in Aufgabe 2.*
