# T-0043 — Gut-Besser-Best-Paketierung mit gezieltem Decoy

## Technique ID

T-0043

## Source ID

SRC-0012

## Name

Gut-Besser-Best-Paketierung mit gezieltem Decoy (Drei-Optionen-Angebotsstruktur)

## Definition

Bei der Präsentation eines Angebots mit mehreren Ausstattungs-/Preisstufen wird eine mittlere oder niedrigere Stufe bewusst so gestaltet, dass sie einer der Hauptstufen klar unterlegen, aber gut vergleichbar ist ("Decoy") — mit dem Ziel, die Wahl zur eigentlich beabsichtigten Zielstufe zu lenken. Konkrete Umsetzung: Drei Angebotsstufen werden präsentiert, wobei die niedrigste Stufe (oder eine mittlere Stufe) bei minimalem Preisunterschied zur Zielstufe deutlich weniger Leistung bietet, sodass der Preisaufschlag zur Zielstufe im Vergleich trivial erscheint.

## Zweck

Lenkung der Kaufentscheidung zu einer vom Verkäufer/Anbieter bevorzugten (meist margenstärkeren) Angebotsstufe, ohne explizite Empfehlung aussprechen zu müssen — die Struktur des Angebots selbst erzeugt die Präferenz.

## Angewendetes Prinzip

P-0045 — Decoy-Positionierung zur gezielten Lenkung von Angebotswahl

## Genutzter Mechanismus

MEC-0009 — Perzeptueller Kontrast (erweitert um Decoy-Effekt/Asymmetrische Dominanz)

## Gesprächszustand

Solution_Frame / Solution_Evaluation

## Beispiel-Formulierung

**Situation: Software-Lizenzangebot mit drei Stufen**

> "Basic-Paket: 5 Nutzerlizenzen, Standard-Support, €2.000/Jahr.
> Standard-Paket: 5 Nutzerlizenzen, Priority-Support, erweiterte Reports, €3.200/Jahr.
> Premium-Paket: 5 Nutzerlizenzen, Priority-Support, erweiterte Reports, API-Zugang, dedizierter Account Manager, €3.400/Jahr."

Hier ist das Standard-Paket der Decoy: Für nur €200 mehr als Standard erhält der Kunde beim Premium-Paket deutlich mehr Leistung (API-Zugang, Account Manager) — der Preisaufschlag zum Premium-Paket erscheint gegen den Leistungssprung trivial, während der Sprung von Basic zu Standard weniger klar vorteilhaft wirkt. Die Zielstufe (Premium) profitiert vom Kontrast zur knapp darunterliegenden, unterlegenen Standard-Stufe.

## Risiken

- Wird die Konstruktion als bewusste Manipulation durchschaut (z. B. durch preisvergleichende Kunden oder Wiederholungskäufer), kann Vertrauen beschädigt werden (Reaktanz, MEC-0003)
- Die Zielstufe ist nicht zwangsläufig die für den individuellen Kundenbedarf beste Wahl — Risiko der Fehlberatung, wenn die Struktur unabhängig vom tatsächlichen Bedarf standardisiert eingesetzt wird

## Typische Fehlanwendung

1. **Decoy zu offensichtlich unattraktiv:** Wird die "schlechtere" Stufe absurd unvorteilhaft gestaltet, erkennen Kunden die Konstruktion und reagieren mit Misstrauen
2. **Fehlende Bedarfsanalyse vor Präsentation:** Die Decoy-Struktur wird eingesetzt, ohne vorher zu klären, ob die Zielstufe tatsächlich zum Kundenbedarf passt — führt zu Falschverkauf und späterer Unzufriedenheit/Kündigung
3. **Zu viele Stufen (>3-4):** Die Wirkung eines einzelnen Decoys ist bei komplexeren Optionssets weniger gut erforscht und kann durch Choice Overload (MEC-0015) konterkariert werden

## Ethisches Risiko

mittel — Die Technik lenkt Kaufentscheidungen strukturell, ohne explizite Falschaussagen zu treffen (alle Informationen bleiben korrekt und sichtbar). Das Risiko liegt in der potenziellen Diskrepanz zwischen gelenkter und tatsächlich bedarfsgerechter Wahl. Empfehlung: Nur nach vorheriger Bedarfsklärung einsetzen, und nur wenn die Zielstufe für die relevante Zielgruppenmehrheit tatsächlich sinnvoll ist — nicht als Ersatz für individuelle Beratung.

## Evidenzlevel

E3 — Die zugrunde liegende Decoy-Effekt-Forschung ist gut etabliert (Huber/Payne/Puto 1982, Ariely-Replikationen); die spezifische Anwendung auf B2B-Software-/Dienstleistungs-Paketpreisgestaltung ist jedoch Codex-eigene Extrapolation, nicht direkt in den Quellen getestet.

## Verknüpfte Kompetenzen

Angebots- und Preisarchitektur-Gestaltung, bedarfsorientierte Beratungsethik

## Status

Entwurf — erstellt 2026-07-02 (SRC-0012)
