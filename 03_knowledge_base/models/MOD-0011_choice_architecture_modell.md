# MOD-0011 — Choice Architecture: Wahlarchitektur als eigenständiges Entscheidungsdesign-Framework

## Modell ID

MOD-0011

## Source ID

SRC-0013

## Name

Choice Architecture (Wahlarchitektur)

## Ursprung / Quelle

SRC-0013 — Nudge: The Final Edition, Richard H. Thaler & Cass R. Sunstein, Ausgabe 2021. Primär Kapitel 5 ("Choice Architecture"), Kapitel 6 ("But Wait, There's More" — Curation, Fun), Kapitel 7 ("Smart Disclosure"), Kapitel 8 ("#Sludge"), ergänzend Kapitel 1, 4, 9, 13, 14 (Anwendungsfälle).

## Zweck

Choice Architecture beschreibt, wie die STRUKTUR einer Entscheidungsumgebung (Reihenfolge, Voreinstellungen, Informationsdarstellung, Fehlertoleranz, Komplexitätsreduktion) das Wahlverhalten systematisch beeinflusst — unabhängig vom Inhalt der verfügbaren Optionen selbst. Das Modell liefert einen Werkzeugkasten zur bewussten, wohlfahrtsorientierten Gestaltung von Entscheidungsumgebungen (Formulare, Angebotsstrukturen, Vertragsprozesse, Produktpräsentationen).

## Annahmen

| A-ID | Name |
|---|---|
| A-0054 (neu) | Verzögertes Commitment + Verlustvermeidungs-Framing wirkt kombiniert stärker als Einzelintervention |
| A-0055 (neu) | Aktiv erhöhte Reibung verhindert Verhalten auch bei vorhandener Handlungsabsicht |
| A-0008 (bestehend, aus MOD-0002) | Wert-/Qualitäts-/Statuswahrnehmung ist relativ, nicht absolut — Grundlage für Mapping-/Rahmungsprinzipien |

## Enthaltene Prinzipien

| P-ID | Name |
|---|---|
| P-0048 | Default-Option-Wirkung |
| P-0049 | Verzögertes Commitment mit Verlustvermeidungs-Rahmung |
| P-0050 | Reibungsreduktion als Konversionshebel |

**Mindestschwellen-Prüfung (CKM Abschnitt 5):** MOD erfordert mindestens drei verknüpfte Prinzipien mit beschreibbarer kausallogischer Struktur. Erfüllt — drei eigenständige, jeweils die OR-Regel (≥2 MEC oder ≥2 A) erfüllende P-Objekte sind direkt aus SRC-0013 abgeleitet und bilden zusammen die drei zentralen Bausteine des Modells: Default-Gestaltung (P-0048), zeitliche Staffelung/Commitment-Design (P-0049), Reibungsmanagement (P-0050).

## Enthaltene Techniken

| T-ID | Name |
|---|---|
| T-0044 | Prompted Choice |
| T-0045 | Sludge-Audit im Kündigungs-/Vertragsverlängerungsprozess |
| T-0043 (aus MOD-0010-Kontext, querverwiesen) | Gut-Besser-Best-Decoy-Paketierung (Structure-Complex-Choices-Baustein) |

## Mechanismen

| MEC-ID | Name |
|---|---|
| MEC-0002 (erweitert) | Verlustaversion und Kosten des Status quo — Trägheits-/Referenzpunkt-Komponente |
| MEC-0008 (erweitert) | Autorität als automatischer Compliance-Auslöser — Default-als-Empfehlungssignal-Komponente |
| MEC-0006 (erweitert) | Soziale Bewährtheit als Korrektheitssignal — Norm-Kommunikations-Baustein |
| MEC-0015 (erweitert) | Kognitive Überlastung durch Feature-/Choice-Overload — Structure-Complex-Choices-Baustein |
| MEC-0021 (erweitert) | Anchoring-Mechanismus — Framing-/Reihenfolge-Baustein |
| MEC-0024 (neu) | Sludge — Reibungs-Baustein (Umkehrung) |

## Kausallogische Struktur

```
Entscheidungsumgebung hat zwangsläufig eine Struktur (keine "neutrale" Gestaltung möglich)
  → Choice Architect wählt bewusst oder unbewusst:
      (a) Default-Option (MEC-0002 + MEC-0008 → P-0048)
      (b) Reihenfolge/Framing/Anker (MEC-0021)
      (c) Informationsdarstellung/Mapping (Smart Disclosure, Kap. 7)
      (d) Komplexitätsgrad des Optionssets (MEC-0015 → Kuratierung, Kap. 6)
      (e) Prozessreibung — gesenkt (Nudge) oder erhöht (MEC-0024 Sludge)
      (f) Sozialer Normkontext (MEC-0006)
  → Diese sechs Gestaltungsdimensionen wirken gemeinsam auf das beobachtete Wahlverhalten
  → Wahlfreiheit bleibt bei allen sechs Dimensionen formal erhalten (Abgrenzung zu Zwang/Verboten) — Ausnahme: Sludge kann Wahlfreiheit faktisch (nicht formal) einschränken, wenn Reibung prohibitiv hoch wird
```

## Bester Kontext

Formular-, Angebots-, Vertrags- und Interface-Gestaltung mit wiederkehrenden, standardisierbaren Entscheidungspunkten (Vertragsverlängerung, Onboarding, Produktkonfiguration, Rabatt-/Bonusprogramme). Besonders wirksam bei komplexen, seltenen oder informationsarmen Entscheidungssituationen (siehe P-0048-Kontextlabel).

## Grenzen

- Fast alle empirischen Belege stammen aus Public-Policy-/Konsumenten-/Arbeitgeber-Benefits-Kontexten — direkter B2B-Vertriebstransfer in keinem der zugrunde liegenden Experimente getestet.
- Publication-Bias-Kontroverse (Mertens 2021 vs. Maier/Szaszi 2022, SD-SYS-005) betrifft die Wirksamkeit von Choice-Architecture-Interventionen insgesamt — mahnt zu Vorsicht bei pauschaler Wirksamkeitsannahme.
- Grenzfall Sludge-Baustein: Die ethische Doppelnutzbarkeit (Reibungsreduktion vs. -erhöhung) macht diesen Baustein des Modells besonders sorgfältig anwendungsbedürftig (siehe T-0045 Ethisches-Risiko-Feld).
- Keine Quantifizierung, welcher der sechs Bausteine bei Konflikt zwischen ihnen (z. B. Default vs. starke soziale Norm in Gegenrichtung) dominiert.

## Konkurrierende Modelle

Keine direkt konkurrierenden Modelle — MOD-0011 ist komplementär zu MOD-0002 (Cialdini Sechs-Prinzipien-Modell) und MOD-0010 (Kahneman Kognitive Bias-Landkarte), siehe Quervergleich unten.

## Canonicalisierungsentscheidung

Wurde geprüft, ob ein bestehendes MOD-Objekt dieses Modell bereits abdeckt?

| Geprüftes Objekt | Ergebnis | Begründung |
|---|---|---|
| MOD-0002 (Cialdini Sechs-Prinzipien-Modell) | Nicht abdeckend — Erweiterung abgelehnt | MOD-0002 beschreibt sechs psychologische COMPLIANCE-TRIGGER (Reziprozität, Commitment, Social Proof, Liking, Autorität, Knappheit) — ein Bias-/Trigger-Katalog, der ERKLÄRT, warum Menschen auf bestimmte Reize automatisch reagieren. MOD-0011 beschreibt dagegen ein DESIGN-FRAMEWORK — wie eine EntscheidungsUMGEBUNG (nicht ein einzelner Trigger-Reiz) strukturiert wird. Die Domänen überschneiden sich (Default-Signale nutzen z. B. MEC-0008, das auch in MOD-0002 verankert ist), aber MOD-0011 organisiert diese Bausteine nach GestaltungsFUNKTION (Default, Framing, Struktur, Reibung) statt nach psychologischem Trigger-Typ. Eine Eingliederung in MOD-0002 würde dessen Kohärenz als Compliance-Trigger-Katalog verwässern (CKM §6, "zu allgemein"-Warnung) und die eigenständige Designperspektive (Reihenfolge, Formulargestaltung, Prozessarchitektur) verlieren, die in MOD-0002 nicht abgebildet ist. |
| MOD-0010 (Kahneman Kognitive Bias-Landkarte) | Nicht abdeckend — Erweiterung abgelehnt | MOD-0010 ist eine DESKRIPTIVE Landkarte kognitiver Verzerrungen (Urteilsbildung, numerische Schätzung, Risikobeurteilung, Selbstüberschätzung) — sie beschreibt, WARUM Menschen verzerrt urteilen. MOD-0011 ist PRÄSKRIPTIV/GESTALTEND — es beschreibt, WIE eine Entscheidungsumgebung als Reaktion auf diese Verzerrungen gezielt gebaut wird. Der kategoriale Unterschied entspricht der Unterscheidung zwischen Diagnose (MOD-0010) und Intervention/Design (MOD-0011). Eine Eingliederung würde die klare, bereits etablierte Bias-Katalog-Struktur von MOD-0010 durch eine strukturell andersartige Design-Methodik verwässern. |

**Entscheidung:** Neu anlegen (MOD-0011). Mindestschwelle erfüllt (≥3 verknüpfte Prinzipien, siehe oben). Kategoriale Eigenständigkeit gegenüber beiden geprüften Kandidaten hinreichend begründet.

## Quervergleich mit bestehenden MOD-Objekten

| MOD-ID | Vergleich | Abgrenzung |
|---|---|---|
| MOD-0002 (Cialdini) | Beide behandeln automatische/heuristische Reaktionen auf Gestaltungsreize | MOD-0002 = Trigger-Katalog (WARUM einzelne Reize wirken); MOD-0011 = Design-Framework (WIE eine gesamte Entscheidungsumgebung strukturiert wird). MEC-0006 und MEC-0008 sind in beiden Modellen verankert, aber aus unterschiedlicher Perspektive (Trigger-Mechanismus vs. Gestaltungsbaustein). |
| MOD-0010 (Kahneman) | Beide bauen auf denselben kognitionspsychologischen Grundlagen auf (S1/S2, Anchoring, Verlustaversion) | MOD-0010 = deskriptive Bias-Landkarte; MOD-0011 = präskriptives Interventionsdesign. MEC-0021 (Anchoring) ist in beiden verankert, aus Diagnose- (MOD-0010) vs. Gestaltungs-Perspektive (MOD-0011). |

## Evidenzlevel

E3 (Sales-Integration) — Die zugrunde liegenden Einzelmechanismen sind unterschiedlich stark belegt (MEC-0021 E5, MEC-0002 E4, MEC-0024 E2). Das GESAMTMODELL als Integrationsrahmen selbst ist nicht direkt getestet (kein Experiment testet "Choice Architecture als Ganzes"), sondern eine Codex-eigene Systematisierung der im Quellenmaterial beschriebenen Einzelbausteine — analog zur bereits etablierten Praxis bei MOD-0002 und MOD-0010.

## Klassifikationshinweis (Editor Decision ED-003, Behavioral Science Review Sprint, 2026-07-02)

Ein externes wissenschaftliches Gutachten zum Behavioral Science Expansion Sprint (SPR-0003) kritisierte die Einordnung von MOD-0011 als "Modell", da Choice Architecture kein formales System mit empirisch prüfbaren, quantitativen kausalen Prädiktionen sei, sondern ein präskriptives Design-Framework/eine Sammlung bestehender Mechanismen. Diese Beobachtung ist in der Sache zutreffend, betrifft jedoch eine strengere, wissenschaftstheoretische Modell-Definition, die nicht die im Repository aktuell gültige ist.

Die maßgebliche Codex-eigene Definition (`01_framework/05_knowledge_model/canonical_knowledge_model.md`, Abschnitt 5) verlangt für ein MOD-Objekt ausschließlich: „Mindestens drei verknüpfte Prinzipien. Kausallogische Struktur beschreibbar." MOD-0011 erfüllt diese Schwelle nachweisbar (drei Prinzipien: P-0048, P-0049, P-0050; beschreibbare Kausallogik-Struktur, siehe oben) und ist nach dieser Definition korrekt als MOD klassifiziert.

**Diese Einordnung bedeutet ausdrücklich nicht**, dass MOD-0011 ein formal-empirisches, prädiktiv getestetes Wissenschaftsmodell im strengen Sinne ist — das GESAMTMODELL selbst wurde nie als integriertes Konstrukt empirisch getestet (siehe „Evidenzlevel" und „Grenzen" oben, sowie die SD-SYS-005-Publikationsbias-Kontroverse in `SCIENTIFIC_DEBT.md`). MOD-0011 ist ein Modell im Sinne der Codex-eigenen, strukturellen Definition (Bündelung verknüpfter, kausallogisch beschreibbarer Prinzipien) — nicht im Sinne eines formalen, prädiktiv validierten wissenschaftlichen Kausalmodells. Eine Umklassifizierung in eine neue Objektkategorie (z. B. "präskriptives Design-Framework") wurde geprüft und abgelehnt (ED-008) — dies wäre eine Framework-Änderung außerhalb des Sprintumfangs. Details: `00_project/BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md`, ED-003.

## Codex-Interpretation

MOD-0011 schließt eine bislang im Sales Codex fehlende Ebene: Die bisherigen Modelle (SPIN, Cialdini, Voss/BCSM, Challenger, Gap Selling, JOLT, Principled Negotiation, Pre-Suasion, Pink ABC, Kahneman Bias-Landkarte) fokussieren überwiegend auf GESPRÄCHSFÜHRUNG und VERHANDLUNG. MOD-0011 ergänzt die STRUKTURELLE Gestaltungsebene (Formulare, Angebote, Vertragsprozesse, Produktkonfiguratoren) — relevant für Sales Operations, Angebotsmanagement und Customer-Success-Prozessgestaltung, nicht nur für das Einzelgespräch.

## Status

Entwurf — erstellt 2026-07-02 (SRC-0013)
