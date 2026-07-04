# T-0045 — Sludge-Audit im Kündigungs-/Vertragsverlängerungsprozess

## Technique ID

T-0045

## Source ID

SRC-0013

## Name

Sludge-Audit im Kündigungs-/Vertragsverlängerungsprozess

## Definition

Systematischer Vergleich der Prozessschritte (Klickanzahl, Formularfelder, Wartezeiten, verfügbare Kanäle) zwischen Vertragsabschluss/Anmeldung einerseits und Kündigung/Widerruf andererseits, mit dem Ziel, unbeabsichtigte oder unangemessene Asymmetrien zu identifizieren und zu beseitigen. Konkrete Umsetzung: Für jeden Kundenprozess wird dokumentiert, wie viele Schritte/Kanäle für die Anmeldung nötig sind, und wie viele für die Kündigung — bei signifikanter Asymmetrie (z. B. Online-Anmeldung, aber Telefon-Kündigung während eingeschränkter Geschäftszeiten) wird eine Anpassung geprüft.

## Zweck

Vermeidung von Kundenvertrauensschäden durch erkennbare Retention-Sludge (siehe Ethisches Risiko) UND — bei GEZIELTER, transparenter Anwendung im Interesse des Kunden — Erhöhung der Konversionsrate bei bereits vorhandener Handlungsabsicht (z. B. Vertragsabschluss, Rabatteinlösung), indem unnötige, nicht der Programmintegrität dienende Reibung entfernt wird.

## Angewendetes Prinzip

P-0050 — Reibungsreduktion als Konversionshebel

## Genutzter Mechanismus

MEC-0024 — Sludge (Künstlich erhöhte Transaktionsreibung als Verhaltensblockade)

## Gesprächszustand

Decision / Solution_Evaluation

## Beispiel-Formulierung

**Audit-Fragenkatalog (aus SRC-0013 Kap. 8 abgeleitet, keine wörtliche Formulierung im Quellenmaterial, sondern Codex-eigene Operationalisierung):**

1. Wie viele Klicks/Schritte benötigt die Anmeldung/der Kaufabschluss? Wie viele die Kündigung/der Widerruf?
2. Sind für Anmeldung und Kündigung dieselben Kanäle verfügbar (online, Telefon, Post)?
3. Gibt es bei der Kündigung zusätzliche Pflichtangaben (Begründung, Wartezeit, Bestätigungsanrufe), die bei der Anmeldung nicht gefordert wurden?
4. Ist die Kündigungsmöglichkeit ebenso klar auffindbar/kommuniziert wie das Anmeldeangebot?

## Risiken

- Ein Sludge-Audit, der ausschließlich zur eigenen Absicherung (Compliance-Nachweis) durchgeführt wird, ohne tatsächliche Prozessänderung, ist wirkungslos ("Audit-Theater")
- Vollständige Symmetrie zwischen Anmeldung und Kündigung ist nicht immer angemessen (z. B. wenn Kündigung eine legitime Identitätsprüfung erfordert, die bei Anmeldung nicht nötig war) — pauschale Gleichsetzung kann zu neuen Problemen (Betrugsrisiko) führen

## Typische Fehlanwendung

1. **Audit ohne Umsetzungsmandat:** Sludge wird identifiziert, aber nicht abgebaut, weil interne Anreize (Retention-KPIs) der Prozessvereinfachung entgegenstehen — dieser Zielkonflikt wird im Quellenmaterial selbst offen benannt (Kap. 8: Kündigungssludge als "intentional retention policy").
2. **Verwechslung von legitimer Prozessintegrität mit Sludge:** Nicht jede Reibung ist Sludge — Identitätsprüfung bei sicherheitsrelevanten Änderungen kann legitim sein. Eine pauschale "je weniger Schritte, desto besser"-Logik ohne Abwägung der Schutzfunktion wäre eine Fehlanwendung.

## Ethisches Risiko

mittel bis hoch — ⚠ Diese Technik hat eine explizit doppelte Anwendungsmöglichkeit, die im Ethisches-Risiko-Feld transparent gemacht werden muss: (a) LEGITIME Anwendung: Reibung im Interesse des Kunden abbauen (Kündigung so leicht wie Anmeldung) — niedriges Risiko, Vertrauensgewinn. (b) MISSBRÄUCHLICHE Anwendung: Das Audit-Wissen wird genutzt, um GEZIELT Kündigungsreibung zu ERHÖHEN oder Anmeldereibung zu SENKEN, um Retention durch Sludge statt durch Werterhalt zu erzwingen — hohes Risiko, im Quellenmaterial selbst als "dark pattern" bezeichnet (Kap. 8, Kap. 15 Manipulationsdebatte). Der Sales Codex markiert diese Doppelnutzbarkeit ausdrücklich: Ein Sludge-Audit-T-Objekt darf im Codex-Kontext ausschließlich für die reibungsREDUZIERENDE (kundenorientierte) Anwendung empfohlen werden; die reibungsERHÖHENDE Anwendung wird hier explizit nicht als legitime Technik geführt, sondern als ethischer Risikofall dokumentiert (Publicity-Prinzip aus Kap. 15: Eine Praxis, die bei öffentlicher Offenlegung nicht verteidigt werden könnte, sollte nicht angewendet werden).

## Evidenzlevel

E2 — Gestützt durch zwei konvergente Feldbeispiele (Rebate-Redemption-Studie, Dynarski-Studie), aber keine direkte, kontrollierte Studie zu einem strukturierten "Sludge-Audit"-Prozess selbst — dies ist eine Codex-eigene Operationalisierung des im Quellenmaterial beschriebenen Grundprinzips, nicht eine im Buch selbst getestete Einzeltechnik.

## Verknüpfte Kompetenzen

Prozessdesign, Customer-Experience-Gestaltung, ethisch reflektierte Vertriebs-/Retentionsstrategie

## Status

Entwurf — erstellt 2026-07-02 (SRC-0013)
