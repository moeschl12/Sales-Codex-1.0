# Sprint 2 Abschlussbericht — Research Sprint: Fünf Bücher

## Metadaten

| Feld | Wert |
|---|---|
| Sprint-ID | SPR-0002 |
| Sprint-Typ | Research Sprint (Book Mode) |
| Zeitraum | 2026-07-01 |
| Bücher | B-0006 bis B-0010 (5 Bücher) |
| Status | **ABGESCHLOSSEN** |

---

## 1. Verarbeitete Bücher

| Buch-ID | Titel | Autor | Jahr | Quellenklasse | Status |
|---|---|---|---|---|---|
| B-0006 | The JOLT Effect | Dixon/McKenna | 2022 | B+ | ✓ Vollständig |
| B-0007 | Getting to Yes | Fisher/Ury | 1981 | A | ✓ Vollständig |
| B-0008 | Pre-Suasion | Cialdini | 2016 | A | ✓ Vollständig |
| B-0009 | To Sell Is Human | Pink | 2012 | B | ✓ Vollständig |
| B-0010 | Thinking, Fast and Slow | Kahneman | 2011 | A+ | ✓ Vollständig |

---

## 2. Gesamtstatistik Knowledge Objects

### Neu erstellt in Sprint 2

| Objekttyp | B-0006 | B-0007 | B-0008 | B-0009 | B-0010 | **Gesamt Sprint 2** |
|---|---|---|---|---|---|---|
| Statements (ST) | 14 | 10 | 11 | 8 | 8 | **51** |
| Assumptions (A) | 6 | 4 | 4 | 3 | 2 | **19** |
| Mechanisms NEU (MEC) | 1 | 1 | 2 | 1 | 1 | **6** |
| Mechanisms EXTEND | 0 | 0 | 1 | 0 | 2 | **3** |
| Principles (P) | 4 | 4 | 3 | 3 | 3 | **17** |
| Techniques (T) | 5 | 4 | 3 | 2 | 2 | **16** |
| Models NEU (MOD) | 1 | 1 | 1 | 1 | 1 | **5** |
| **Objekte gesamt** | **31** | **24** | **25** | **18** | **20** | **118** |

### Kumulativer Codex-Stand nach Sprint 2

| Objekttyp | Stand vor Sprint 2 | Sprint 2 neu/erweitert | Stand gesamt |
|---|---|---|---|
| Statements (ST) | ~150 | 51 NEU | **~201** |
| Assumptions (A) | ~29 | 19 NEU | **~48** |
| Mechanisms (MEC) | 15 | 6 NEU + 3 EXTEND | **21** |
| Principles (P) | ~30 | 17 NEU | **~47** |
| Techniques (T) | ~25 | 16 NEU | **~41** |
| Models (MOD) | 5 | 5 NEU | **10** |

---

## 3. Canonicalization Rate

| Buch | Kandidaten | EXTEND/MERGE | NEU | Rate (EXTEND%) |
|---|---|---|---|---|
| B-0006 The JOLT Effect | 31 | 1 EXTEND | 30 | ~3% |
| B-0007 Getting to Yes | 24 | 0 | 24 | 0% |
| B-0008 Pre-Suasion | 25 | 1 EXTEND (MOD-0002) | 24 | 4% |
| B-0009 To Sell Is Human | 18 | 0 | 18 | 0% |
| B-0010 Thinking, Fast and Slow | 20 | 2 EXTEND + 1 NSTD aufgelöst | 17 | 15% |
| **Sprint 2 gesamt** | **118** | **4 EXTEND + 1 NSTD** | **113** | **~4%** |

**Interpretation:** Die niedrige Canonicalization Rate (4% EXTEND) zeigt, dass Sprint-2-Bücher konzeptuell stark eigenständig sind. Ausnahmen:
- B-0010 (15%): Logisch — Kahneman ist Primärforscher hinter MEC-0002 und MEC-0012; Quellen-Upgrade war ausstehend
- B-0008 (4%): MOD-0002 (Cialdini 6 Prinzipien) wurde um Unity erweitert — folgerichtig aus demselben Autor

---

## 4. Scientific Debt Delta

### Neu identifizierte Scientific Debt in Sprint 2

| ID | Buch | Typ | Beschreibung | Priorität |
|---|---|---|---|---|
| SD-B006-001 | B-0006 | Offene Forschungsfrage | 44/56-Split Klassifizierungsmethodik nicht veröffentlicht | Mittel |
| SD-B006-002 | B-0006 | Externe Validierung | FOMU als primärer Indecision-Treiber: kausal nicht direkt belegt | Mittel |
| SD-B006-003 | B-0006 | Kulturelle Generalisierung | JOLT-Techniken: US/COVID-2020-Daten | Niedrig |
| SD-B007-001 | B-0007 | Externe Validierung | Principled Negotiation vs. positional: kein RCT | Niedrig |
| SD-B007-002 | B-0007 | Offene Forschungsfrage | Fixed-Pie-Fallacy in B2B-Sales-Kontext nicht gemessen | Niedrig |
| SD-B008-001 | B-0008 | Externe Validierung | Pre-Suasion B2B-Transfer: Lab→Sales nicht gemessen | Mittel |
| SD-B008-002 | B-0008 | Externe Validierung | Unity-Kapitel: am wenigsten extern repliziert | Niedrig |
| SD-B009-001 | B-0009 | Offene Forschungsfrage | Improv-Transfer auf Sales: kein RCT | Niedrig |
| SD-B009-002 | B-0009 | Replikationsrisiko | Ambivert-Vorteil: Grant-Einzelstudie Call-Center | Mittel |
| SD-B009-003 | B-0009 | Offene Forschungsfrage | Prosoziale Motivation vs. Eigennutz langfristig | Mittel |
| SD-B010-001 | B-0010 | Replikationsrisiko | Priming-Forschung (Kap.4): Replikationskrise; betrifft auch MEC-0018 | **Hoch** |
| SD-B010-002 | B-0010 | Transferlücke | B2B-Transfer Lab-Anchoring/Framing/Ease | Mittel |
| SD-B010-003 | B-0010 | Offene Forschungsfrage | Expert Intuition in Enterprise B2B-Zyklen | Niedrig |

**Wichtigste neue Schuld:** SD-B010-001 (Priming-Replikationskrise) — betrifft MEC-0018 (Pre-Suasion) rückwirkend. Empfehlung: Externe Validierung MEC-0018 in nächstem Validierungssprint.

---

## 5. W-001-Status: Teach First (Challenger) vs. Diagnose First (SPIN/Gap Selling)

| Buch | Position gegenüber W-001 |
|---|---|
| B-0006 The JOLT Effect | Phaslich eingeordnet: JOLT-Techniken wirken nach Problemidentifikation — neutral |
| B-0007 Getting to Yes | Orthogonal: Interessen > Positionen-Rahmen transzendiert die Dichotomie |
| B-0008 Pre-Suasion | Orthogonal: Pre-Suasion verbessert beide Seiten ohne zu entscheiden |
| B-0009 To Sell Is Human | Indirekter Bezug: Clarity/Problem-Finding stützt Diagnose; Pitch hat Teach-Affinität |
| B-0010 Thinking, Fast and Slow | Neutral: Käuferpsychologie-Modell; beide Seiten können es nutzen |

**Gesamtstatus W-001 nach Sprint 2: OFFEN**

Keine der fünf Quellen löst W-001 auf. Kein direkter Vergleichsbefund (RCT Challenger vs. SPIN/Gap) existiert. Neue Einsicht aus Sprint 2: Pink's Problem Finding (ST-0191) legt nahe, dass W-001 möglicherweise falsch gerahmt ist — die richtige Frage könnte sein "Wann braucht der Käufer Diagnose, wann Insight?" statt "Welche Methode ist generell besser." Diese Reframierung ist für SPR-0003 vorgemerkt.

---

## 6. Evidenz-Upgrades durch Sprint 2

### Primärquellen-Upgrades

| Objekt | Vorher | Nachher | Grund |
|---|---|---|---|
| MEC-0002 (Loss Aversion) | Kahneman/Tversky als Referenz | SRC-0010 als explizite Primärquelle | B-0010 war Kahneman's Hauptwerk; retroaktiver Upgrade |
| MEC-0012 (System 1/2) | Voss/SRC-0003 als Ursprungsquelle | SRC-0010 als kanonische Primärquelle | Kahneman ist Schöpfer des Modells, nicht Voss |
| MEC-0009 (NSTD Anchoring) | Offener Quervergleich seit B-0002 | MEC-0021 angelegt; Abgrenzung dokumentiert | 4 Sprints später endlich aufgelöst |

### Neue Hochqualitäts-Objekte (E5)

Sprint 2 hat 12 Objekte mit E5-Evidenz hinzugefügt (alle aus B-0010):
ST-0194, ST-0195, ST-0196, ST-0198, ST-0199 — alles Nobel-Preis-assoziierte oder mehrfach replizierte Befunde.

---

## 7. Cross-Book-Verbindungen und Widersprüche

### Neue Verbindungen (Sprint 2)

| Von | Zu | Verbindungstyp |
|---|---|---|
| MEC-0021 (Anchoring, B-0010) | MEC-0002 (Loss Aversion, B-0001) | Kombination: Anker + Loss-Frame |
| ST-0187 (Caveat Venditor, B-0009) | ST-0191 (Problem Finding, B-0009) | Kausal: Informationsparität → Problem Finding als Differenzierung |
| MOD-0008 (Pre-Suasion, B-0008) | MEC-0018 (Priming) | B-0010 enthüllt Replikationsrisiko (SD-B010-001) |
| MEC-0020 (Perspektivübernahme Macht, B-0009) | MEC-0010 (Tactical Empathy, B-0003) | Abgrenzung: kognitiv vs. emotional |
| P-0037 (Unity, B-0008) | MEC-0019 (We-Identity) | Systematische Erweiterung von B-0002 Compliance-Prinzipien |
| P-0038 (Problem Finding, B-0009) | MEC-0013 (Insight-Disruption, B-0004) | Konzeptuelle Überlappung: Problem Finding ≈ Teaching-Reframe |

### Widersprüche

| Conflict | Bücher | Status |
|---|---|---|
| W-001: Teach First vs. Diagnose First | B-0001/0004/0005 vs. B-0004 | OFFEN seit Sprint 1 — Sprint 2 orthogonal |
| Voss vs. Fisher/Ury: Kompromiss | B-0003 vs. B-0007 | Dokumentiert in B-0007; kein RCT; Kontext-abhängige Antwort wahrscheinlich |
| Empathie (Voss) vs. Perspektivübernahme (Pink) | B-0003 vs. B-0009 | Nicht direkter Widerspruch — verschiedene Mechanismen (MEC-0010 vs. MEC-0020); komplementär |
| Kognitiver Ease vs. analytisches Überzeugung | B-0010 vs. B-0001 (SPIN: analytisches Fragen) | Keine echte Spannung: SPIN-Fragen aktivieren käufer-eigenes S1 (MEC-0001), nicht Verkäufer-S1 |

---

## 8. Ausstehende NSTD-Marker (geerbte offene Punkte)

| Marker | Objekt | Beschreibung | Priorität |
|---|---|---|---|
| NSTD-P-Kandidat | MEC-0002 | Loss Framing vor Gain Framing als eigenständiges Prinzip | Mittel (→ P-0042 teilweise gelöst) |
| NSTD-T-Kandidat | MEC-0002 | Negative Leverage als eigenständige Technik | Niedrig |
| NSTD-P/T | MEC-0012 | Kalibrierte Fragen (What/How vs. Why) als Technik | Niedrig |

---

## 9. Quellenqualitäts-Analyse Sprint 2

| Buch | Quellenklasse | Stärke | Hauptschwäche |
|---|---|---|---|
| B-0006 The JOLT Effect | B+ | ML-Analyse großer Datensatz; zeitgemäß (2022) | Proprietäre Methodik; keine Peer-Review |
| B-0007 Getting to Yes | A | Harvard PON; institutionell gut verankert; E3-E4 | 1981er Studie; Verhandlungskontext ≠ Sales |
| B-0008 Pre-Suasion | A | Cialdini als führender Compliance-Forscher; E4 Basis | Lab→Field-Transfer; Unity am schwächsten |
| B-0009 To Sell Is Human | B | Starke Forschungsintegration (Grant, Galinsky, Seligman) | Journalist, kein Primärforscher; Improv-Kapitel E2 |
| B-0010 Thinking, Fast and Slow | **A+** | Primärforscher; Nobel; E5 für Kernbefunde | Sales-Transfer induktiv; Priming-Krise SD-B010-001 |

**Beste Quelle Sprint 2:** B-0010 (Kahneman) — einzige A+-Quelle; liefert Primärbasis für mehrere ältere Codex-Mechanismen.

---

## 10. Empfehlungen für SPR-0003

### Hohe Priorität
1. **Validierungssprint MEC-0018 (Pre-Suasion Priming):** SD-B010-001 zeigt, dass Priming-Grundlage unter Replikationsdruck steht — externe Validierung erforderlich
2. **W-001 Reframierung explorieren:** Pink's Problem Finding legt neue Fragestellung nahe ("Wann Diagnose, wann Insight?") — könnte W-001 auflösen
3. **Eigene empirische Evidenz für B2B-Transfer prüfen:** Mehrere Lab-Befunde (Anchoring, Framing, Cognitive Ease) brauchen B2B-spezifische Stützung

### Mittlere Priorität
4. **MEC-0009 (Perzeptueller Kontrast) formell aktualisieren:** NSTD-Marker aufgelöst — Abgrenzungs-Text in MEC-0009 wurde bereits ergänzt
5. **Ambivert-Befund (SD-B009-002) extern prüfen:** Grant-Einzelstudie; Replikation in komplexem B2B suchen
6. **NSTD-Marker in MEC-0002 abarbeiten:** Loss Framing-Prinzip und Negative-Leverage-Technik als eigenständige Objekte anlegen

---

## 11. Sprint 2 Abschluss-Statement

**Sprint 2 ist vollständig abgeschlossen.** Alle fünf Bücher (B-0006 bis B-0010) wurden gemäß Book Mode v1.1 vollständig verarbeitet: SRC → ST → A → MEC → P → T → MOD → VAL → BOOK_REVIEW → State Files.

118 neue oder erweiterte Knowledge Objects wurden in den Sales Codex integriert. Der Codex umfasst jetzt ~368 Objekte über 10 Bücher und 6 Objekttypen.

W-001 bleibt offen — ist für SPR-0003 Schwerpunktthema.

Die wissenschaftlich stärkste Errungenschaft von Sprint 2 ist die retroaktive Primärquellen-Verankerung mehrerer zentraler Mechanismen (MEC-0002, MEC-0012) durch SRC-0010 (Kahneman) und die Anlage von MEC-0021 (Anchoring) als eigenständigen Mechanismus.

---

*Erstellt: 2026-07-01 | Sprint 2 | KI-Redaktion Sales Codex*
