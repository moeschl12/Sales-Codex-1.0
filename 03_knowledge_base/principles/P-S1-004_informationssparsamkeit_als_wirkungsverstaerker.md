---
id: P-S1-004
typ: Prinzip
sprint: S1-SYNTHESIS
status: aktiv
erstellt: 2026-07-01
quellen: [B-0001, B-0002, B-0004, B-0005]
qk: QK-4
e_level: E5 (Miller's Law) + E2 (Methodologische Konvergenz)
verknüpfte_objekte:
  mechanismen: [MEC-0015]
  prinzipien: [P-0005, P-0008]
  techniken: [T-0019, T-0022]
widersprueche: []
---

# P-S1-004 — Informationssparsamkeit als Wirkungsverstärker

## Formulierung

Weniger Information zur richtigen Zeit wirkt stärker als mehr Information zur falschen Zeit. Jede effektive Verkaufsmethodik des Sprint 1 begrenzt aktiv die Informationsmenge pro Interaktion, um kognitive Überlastung zu vermeiden und Relevanz zu maximieren. Kognitive Beschränkung ist kein Hygieneanspruch — sie ist ein Wirkungsprinzip.

## Begründung

| Buch | Regel | Kontext | Objekt |
|---|---|---|---|
| SPIN Selling (B-0001, 1988) | Benefit erst nach explizitem Need — nie als Feature-Liste | Lösungspräsentation | P-0005 |
| Influence (B-0002, 1984) | Compliance-Trigger wirken durch Fokus auf einen Hebel, nicht viele | Persuasionsdesign | P-0008 |
| Challenger Sale (B-0004, 2011) | 6-Step-Struktur des Commercial Teaching Pitch | Pitch-Architektur | T-0019 |
| Gap Selling (B-0005, 2018) | Max. 6 Features in der Demo (Miller's Law explizit) | Demo-Design | T-0022, MEC-0015 |

**Warum erst durch Sprint sichtbar:** Jedes Buch hat eine eigene Version des Prinzips, aber kein Buch formuliert es als Verkaufs-Universalprinzip. SPIN nennt es als Technik-Regel (Benefit nur nach Need). Cialdini beschreibt Trigger-Fokussierung als Compliance-Design. Keenan zitiert Miller's Law für Demo-Design. Challenger strukturiert den Pitch auf sechs klare Schritte. Erst die Kombination zeigt: Alle vier Methodologien konvergieren auf Informationsreduktion als Wirkungsprinzip — unabhängig voneinander.

## Handlungsrelevanz

**Positive Formulierung:** Weniger ist strukturell besser: Drei starke Argumente überzeugen mehr als zehn schwache. Sechs relevante Features demonstrieren überzeugender als vierzehn vollständige. Ein aktivierter Compliance-Trigger wirkt stärker als fünf gleichzeitige Trigger.

**Negative Formulierung:** Feature-Vollständigkeit, mehrseitige Argumentationslisten und "lückenlose" Präsentationen signalisieren Unsicherheit und überflasten die kognitive Kapazität des Käufers — was zu Entscheidungsaufschub führt.

**Phasenübergreifende Anwendung:**
- Präsentation: Benefit nur nach explizitem Need (P-0005); max. 6 Features in Demo (T-0022)
- Pitch-Design: Einen Compliance-Trigger pro Situation auswählen, nicht stapeln (P-0008)
- Pitch-Architektur: 6-Step-Challenger-Pitch als Informations-Sequenz-Design (T-0019)
- Outreach: Problem-fokussierte Botschaft (ST-0148) statt Produkt-Feature-Liste

## Mechanistische Grundlage

**MEC-0015 (Kognitive Überlastung durch Feature-Overload):** Wenn die präsentierte Informationsmenge die kognitive Kapazität des Käufers überschreitet (Miller's Law: 7±2 Chunks), sinkt die Verarbeitungstiefe — Käufer sortieren nicht, sie brechen ab.

**Ergänzend:** System-1/2-Dual-Process-Theorie (MEC-0012): Kognitive Überlastung verschiebt die Entscheidung von System 2 (rational) zu System 1 (heuristisch) — was zu Statusquo-Präferenz und Entscheidungsaufschub führt (MEC-0002).

## OR-Basis

Referenziert MEC-0015 (Miller's Law, E5) als wissenschaftlichen Anker. P-0005 und P-0008 als buchspezifische Vorläuferformulierungen. QK-4 (vier Bücher, vier Kontexte).

## Abgrenzung

**Abgrenzung zu P-0005 (Benefit-Fokus):** P-0005 beschreibt buchspezifisch für SPIN, wann ein Benefit präsentiert werden soll (nach explizitem Need). P-S1-004 ist das übergreifende Prinzip hinter P-0005, T-0022, P-0008 und T-0019.

**Abgrenzung zu MEC-0015 (Kognitive Überlastung):** MEC-0015 ist der psychologische Mechanismus. P-S1-004 ist das daraus abgeleitete Handlungsprinzip für Verkäufer.

## Kontextgrenzen

- Technische Anforderungs-Reviews (RFP-Antworten, Ausschreibungen): Vollständigkeit ist Anforderung; Informationssparsamkeit gilt für ergänzende Präsentationen, nicht für Pflichtteil
- Discovery-Phase: Nicht auf Käufer-Seite anwenden — Käufer sollen ausführlich sprechen; Sparsamkeit gilt für Verkäufer-Output
- Sehr informierte Käufer (z.B. technische Experten): Kognitive Kapazität für das Thema ist höher; Miller-Grenze gilt für Working Memory, nicht für Expertise-Wissen

## Evidenzlücken

- Die "max. 6 Features"-Regel (Keenan) ist eine praktische Extrapolation von Miller's Law auf Demo-Kontexte — kein Verkaufsexperiment repliziert diese Zahl direkt
- Miller's Law (1956) wurde inzwischen auf 4±1 Chunks revidiert (Cowan, 2001) — der genaue Grenzwert für Verkaufspräsentationen ist unklar
- Die Wirkung von "mehr Informationen = weniger Überzeugungswirkung" ist in B2B-Langzyklus-Kontexten nicht systematisch gemessen

## Evidenzklassifikation

*(Abschnitt ergänzt 2026-07, Consistency Correction Sprint — siehe `CODEX_AUDIT_2026-07.md` Kapitel 3/11 und `CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md`.)*

E5 (Miller's Law) + E2 (methodologische Konvergenz, QK-4) — identisch mit dem `e_level`-Feld im YAML-Frontmatter dieses Objekts. Diese Ergänzung ist eine reine Sichtbarkeits-/Formatharmonisierung: Der Audit CODEX_AUDIT_2026-07.md hatte dieses Objekt fälschlich als „Evidenzfeld fehlt" gelistet, weil die Prüfung nur nach Markdown-Überschriften (`## Evidenz...`) gesucht und das bereits vorhandene YAML-Frontmatter-Feld `e_level` nicht erfasst hatte. Das Frontmatter-Feld war die ganze Zeit korrekt vorhanden — dies wird hier als Korrektur zum Audit-Befund festgehalten, keine neue Bewertung.
