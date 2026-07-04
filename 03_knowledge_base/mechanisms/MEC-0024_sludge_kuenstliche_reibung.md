# MEC-0024 — Sludge: Künstlich erhöhte Transaktionsreibung als Verhaltensblockade

## Mechanism ID

MEC-0024

## Source ID

SRC-0013

## Name

Sludge: Künstlich erhöhte Transaktionsreibung als Verhaltensblockade

## Definition

Wenn einem Entscheidungsprozess gezielt oder als Nebenprodukt administrativer Gestaltung zusätzliche Reibung (Formularaufwand, Wartezeit, eingeschränkte Kanäle, Wiederholungsschritte) hinzugefügt wird, sinkt die Wahrscheinlichkeit, dass Personen eine für sie selbst vorteilhafte Handlung abschließen — auch wenn eine klare, bewusste Handlungsabsicht bereits vorhanden ist. Sludge ist die strukturelle Umkehrung eines Nudge: Wo ein Nudge Reibung SENKT, um erwünschtes Verhalten zu erleichtern, ERHÖHT Sludge Reibung, um Verhalten zu erschweren oder zu verhindern.

## Mechanismus-Typ

Ökonomisch / Organisatorisch

## Erklärung

Sludge wirkt über einen kausal von Status-quo-Bias (MEC-0002) unterscheidbaren Pfad:

**Stimulus (X):** Gezielt oder als Nebenprodukt hinzugefügte Transaktionskosten (zusätzliche Formularschritte, eingeschränkte Kündigungskanäle, Wartezeiten, Wiederholungspflichten) — NICHT das bloße Fehlen eines Anstoßes.

**Prozess (Y):** Auch bei vorhandener, expliziter Handlungsabsicht führt jeder zusätzliche Reibungsschritt zu einem kumulierten Abbruchrisiko — die Person hat die ursprüngliche Trägheit bereits überwunden (im Unterschied zu MEC-0002, wo die Trägheit selbst nie überwunden wird), wird aber durch neu hinzugefügten Widerstand erneut blockiert oder verlangsamt.

**Reaktion (Z):** Nichtabschluss oder Verzögerung einer bereits beabsichtigten, für die Person vorteilhaften Handlung — unabhängig vom Ausgangsgrad der Motivation.

**Entscheidender Unterschied zu MEC-0002 (Status-quo-Bias/Verlustaversion):** Status-quo-Bias wirkt bereits OHNE künstliche Zusatzhürden — reine Passivität/Trägheit genügt, damit die Default-Option gewählt wird. Sludge fügt AKTIV neue Hürden hinzu, die eine bereits vorhandene, bewusste Handlungsabsicht blockieren. Der entscheidende empirische Beleg für diese kausale Trennung (Kap. 8, Rebate-Redemption-Studie, "Everyone Believes in Redemption"): Aufklärung über niedrige Basisraten und Erinnerungen (Interventionen gegen mangelnde Motivation/Wissen) zeigten KEINEN Effekt auf die tatsächliche Einlösequote; NUR die Reduktion der tatsächlichen Formularreibung (Wegfall der Unterschriftspflicht) erhöhte die Einlösequote von 30% auf 54%. Wäre der Effekt vollständig durch mangelnde Motivation (Trägheit) erklärbar, hätte die Aufklärungsintervention ebenfalls wirken müssen.

**Zweiter unabhängiger Beleg:** Dynarski et al. (Feldexperiment, Kap. 8) — Wegfall der Finanzhilfe-Antragsformulare (bei identischer finanzieller Förderung) erhöhte die Bewerbungsquote leistungsstarker Schüler aus einkommensschwachen Familien an der University of Michigan von 26% auf 68%. Die Motivation (Wunsch auf College zu gehen, Wissen über Förderfähigkeit) war in beiden Gruppen konstant — nur die Reibung (Formularpflicht) variierte.

## Verknüpfte Prinzipien

- P-0050 — Reibungsreduktion als Konversionshebel (neu, siehe Prinzipien-Abschnitt)

## Verknüpfte Techniken

- T-0045 — Sludge-Audit im Kündigungs-/Vertragsverlängerungsprozess (neu)

## Wissenschaftliche Grundlage

- Lamberton, C. & Castleman, B. (2016) — erste Verwendung des Begriffs "Sludge" (Sekundärzitat aus SRC-0013, vollständige akademische Erstquelle nicht unabhängig verifiziert — als offene Frage markiert)
- Thaler, R.H. & Sunstein, C.R. (2021). Nudge: The Final Edition, Kapitel 8 "#Sludge"
- Sunstein, C.R. (2019/2021) — eigenständige Monographie zu Sludge, im Buch erwähnt, nicht separat verifiziert (Titel im Buchtext bewusst als Rätsel formuliert: "Take a guess at its title?")
- Feldstudie "Everyone Believes in Redemption" (Autoren im Fließtext nicht vollständig benannt — offene Frage)
- Dynarski, S. et al. — Feldexperiment University of Michigan Financial-Aid-Guarantee (im Fließtext ohne vollständige Zitation — offene Frage, WebSearch-Recherche zu vollständiger Zitation nicht abschließend erfolgreich in diesem Sprint)

## Evidenzlevel

E2 — Zwei konvergente, aber nicht identische Feldexperimente (Rebate-Redemption mit expliziter Kontrollbedingung; Dynarski College-Bewerbung als Realwelt-RCT) belegen den Mechanismus unabhängig voneinander. Kein E3, da (a) keine der beiden Studien vollständig bibliografisch verifizierbar war (fehlende Erstautorenangaben im Fließtext) und (b) keine Multi-Labor-Replikation oder Meta-Analyse spezifisch zu Sludge als eigenständigem Konstrukt bekannt ist. B2B-Vertriebstransfer ungetestet.

## Vertriebsrelevanz

Hoch — direkt anwendbar auf Checkout-/Vertragsabschluss-, Onboarding- und insbesondere Kündigungs-/Verlängerungsprozesse. Zentrale Implikation: Umsatzverlust durch Reibung ist von Umsatzverlust durch mangelnde Kundenmotivation kausal zu unterscheiden — ein Reibungsproblem lässt sich nicht durch mehr Überzeugungsarbeit lösen, sondern nur durch Prozessvereinfachung.

## Grenzen

- Die Abgrenzung zu MEC-0002 ist bei GERINGER Handlungsabsicht unscharf: Ist eine Person, die bei geringer, aber vorhandener Absicht durch eine kleine Zusatzhürde abgehalten wird, ein Sludge-Fall oder ein Status-quo-Bias-Fall? Das Buch selbst löst diese Grenzlinie nicht abschließend auf (kontinuierliches Spektrum statt scharfer Trennung plausibel).
- ⚠ Ethisches Risiko: Sludge ist per Definition asymmetrisch zwischen legitimer Prozessintegrität (z. B. Betrugsprävention) und absichtlicher Kundenbindungs-Manipulation (z. B. Kündigungserschwerung) — das Buch selbst warnt vor "dark patterns" als Sludge-Unterform. Jedes T-Objekt, das MEC-0024 nutzt, muss diese Doppelnutzbarkeit (Sludge-Reduktion als Kundenvorteil vs. Sludge-Erhöhung als Retention-Taktik) explizit im Ethisches-Risiko-Feld markieren.
- Keine Quantifizierung einer "Sludge-Schwelle" bekannt, ab der eine bestimmte Anzahl/Art von Reibungsschritten Handlungsabsicht sicher bricht.
- B2B-Transfer-Lücke: Kein Experiment im Buch testet Sludge-Effekte in mehrstufigen B2B-Buying-Center-Prozessen, wo ein Teil der Reibung (Compliance, Freigabeprozesse) strukturell notwendig statt künstlich hinzugefügt ist.

## Offene Fragen

- Vollständige akademische Erstquelle des Sludge-Begriffs (Lamberton & Castleman 2016) nicht unabhängig verifiziert.
- Vollständige Zitation der Rebate-Redemption-Studie ("Everyone Believes in Redemption") und der Dynarski-College-Bewerbungsstudie nicht abschließend WebSearch-verifiziert — als offene Frage dokumentiert statt spekulativ zitiert.
- Wie verhält sich die notwendige (legitime) vs. künstliche (schädliche) Reibung in regulierten B2B-Vertriebsprozessen (z. B. Compliance-Prüfungen)?

## Status

Entwurf
