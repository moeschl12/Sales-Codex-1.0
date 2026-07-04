# Book Catalog

## Zweck

Dieses Dokument ist die zentrale Steuerungsliste aller Bücher, die für den Sales Codex analysiert werden sollen.

Cowork nutzt diesen Katalog, um zu erkennen:

* welche Bücher existieren,
* welche Bücher priorisiert sind,
* welches Buch als Nächstes bearbeitet werden soll,
* welchen Bearbeitungsstatus jedes Buch besitzt.

---

## Synchronisations-Hinweis (2026-07-03, External Audit Resolution Sprint)

Dieser Katalog war seit seiner Anlage (vor Pilot 001) nicht mit dem tatsächlichen Repository-Fortschritt synchronisiert worden — ein vom externen Audit ("Wissenschaftliche Prüfung des Sales Codex") zutreffend identifizierter Befund. Bei der Prüfung zeigte sich ein tiefergehendes Problem als vom Audit selbst beschrieben: Die tatsächlich durchgeführten Buchanalysen (B-0001 bis B-0015, siehe `02_sources/`, `03_knowledge_base/`, `04_book_analysis/`) folgen einer eigenen, in der Praxis entstandenen Reihenfolge (Editor-Priorisierung + `research_agenda.md`-Empfehlungen, siehe `OPEN_DECISIONS.md` OD-004), die von der ursprünglich in diesem Katalog geplanten Reihenfolge und Buchauswahl an mehreren Stellen abweicht. Konkret:

- **Fünf tatsächlich abgeschlossene Bücher** (The JOLT Effect, Emotional Intelligence, Nudge, Priceless, Made to Stick — Made to Stick war ursprünglich unter einer anderen ID katalogisiert, s.u.) waren in der ursprünglichen Kandidatenliste dieses Katalogs gar nicht enthalten (For JOLT: gar nicht; für Emotional Intelligence, Nudge, Priceless: gar nicht; Made to Stick war unter B-0014 katalogisiert).
- **Sechs weitere tatsächlich abgeschlossene Bücher** (Getting to Yes, Pre-Suasion, To Sell Is Human, Thinking Fast and Slow, Predictably Irrational) waren zwar bereits als Kandidaten katalogisiert, jedoch unter anderen ID-Nummern als denen, unter denen sie tatsächlich verarbeitet wurden (z. B. "Thinking, Fast and Slow" ursprünglich als B-0015 geplant, tatsächlich verarbeitet als B-0010).
- Dadurch **kollidierten sieben noch offene Kandidaten-IDs** (die ursprünglichen B-0006, B-0008–B-0013) mit den tatsächlich vergebenen IDs bereits abgeschlossener, anderer Bücher.

**Vorgenommene Korrektur:** Die 15 tatsächlich abgeschlossenen Bücher sind unten unter ihrer realen, im gesamten Repository verwendeten ID (B-0001–B-0015) mit Status `DONE` eingetragen. Sechs Katalogeinträge, die dieselben Bücher unter einer anderen, nicht verwendeten ID doppelt führten, wurden entfernt (Inhalt jetzt korrekt unter der realen ID). Sieben noch offene, tatsächlich andere Kandidatenbücher, deren ursprüngliche ID mit einem jetzt tatsächlich vergebenen B-ID kollidierte, wurden auf neue, freie IDs (B-0041–B-0047) verschoben — Titel, Autor, Kategorie, Priorität und Notizen dieser sieben Einträge sind inhaltlich unverändert. Alle übrigen, nicht kollidierenden Kandidaten (B-0018–B-0027, B-0029–B-0040) sind unverändert. Diese Korrektur ist rein strukturell/nummerierungsbezogen — keine inhaltliche Neubewertung, keine neue Priorisierung, keine Streichung von Kandidaten.

---

## Status-Legende

| Status      | Bedeutung                              |
| ----------- | --------------------------------------- |
| IDEA        | mögliches Buch, noch nicht priorisiert |
| WAITING     | aufgenommen, aber noch nicht bereit    |
| READY       | darf als nächstes bearbeitet werden    |
| IN_PROGRESS | wird aktuell bearbeitet                |
| REVIEW      | wartet auf Review durch ChatGPT/Felix  |
| DONE        | abgeschlossen und freigegeben          |
| ARCHIVED    | vorerst nicht weiterverfolgt           |

---

## Priorität

| Priorität | Bedeutung                             |
| --------- | ------------------------------------- |
| P1        | Fundament / sehr hoher Erkenntniswert |
| P2        | wichtig                               |
| P3        | ergänzend                             |
| P4        | später / optional                     |

---

## Book Catalog

### Abgeschlossene Buchanalysen (B-0001–B-0015, alle Status DONE)

| ID     | Titel                                   | Autor                              | Kategorie                        | Priorität | Status | Rolle im Sales Codex                              | Notizen                               |
| ------ | --------------------------------------- | ----------------------------------- | --------------------------------- | --------- | ------ | -------------------------------------------------- | -------------------------------------- |
| B-0001 | SPIN Selling                            | Neil Rackham                        | Vertrieb / Fragetechnik          | P1        | DONE   | Pilotprojekt und Referenzanalyse                  | Buchanalyse abgeschlossen; SRC-0001; Pilot 001 |
| B-0002 | Influence: The Psychology of Persuasion | Robert B. Cialdini                  | Psychologie / Einfluss           | P1        | DONE   | Psychologische Mechanismen und Einflussprinzipien | Buchanalyse abgeschlossen; SRC-0002 |
| B-0003 | Never Split the Difference              | Chris Voss (mit Tahl Raz)            | Verhandlung / Kommunikation      | P1        | DONE   | Verhandlungspsychologie, Labeling, Mirroring      | Buchanalyse abgeschlossen; SRC-0003 |
| B-0004 | The Challenger Sale                     | Matthew Dixon & Brent Adamson        | B2B Vertrieb                     | P1        | DONE   | alternatives Modell zu SPIN                       | Buchanalyse abgeschlossen; SRC-0004; proprietäre CEB-Studie, siehe SCIENTIFIC_DEBT.md SD-SYS-001 |
| B-0005 | Gap Selling                             | Keenan (Jim Keenan)                  | Problemorientierter Vertrieb     | P1        | DONE   | Problem-Gap-Logik, Status quo, Kaufmotivation     | Buchanalyse abgeschlossen; SRC-0005; Teilfassung (fehlende Kapitel), siehe SCIENTIFIC_DEBT.md SD-SYS-002 |
| B-0006 | The JOLT Effect                         | Matthew Dixon & Ted McKenna           | B2B Vertrieb / Indecision        | P1        | DONE   | Kundenunentschlossenheit, FOMU                    | Buchanalyse abgeschlossen; SRC-0006; proprietäre Tethr-Studie, siehe SCIENTIFIC_DEBT.md SD-SYS-004; ursprünglich war dieser ID-Slot für "How to Win Friends and Influence People" (Carnegie) vorgesehen — siehe B-0041 |
| B-0007 | Getting to Yes                          | Roger Fisher & William Ury (mit Bruce Patton) | Verhandlung             | P1        | DONE   | Harvard-Konzept, Interessen statt Positionen      | Buchanalyse abgeschlossen; SRC-0007; ursprünglich als B-0028 katalogisiert |
| B-0008 | Pre-Suasion                             | Robert B. Cialdini                  | Einfluss / Kontext                | P2        | DONE   | Vorprägung und Aufmerksamkeitssteuerung           | Buchanalyse abgeschlossen; SRC-0008; ursprünglich als B-0017 katalogisiert |
| B-0009 | To Sell Is Human                        | Daniel H. Pink                      | Verkaufspsychologie               | P2        | DONE   | moderne Sicht auf Überzeugung                     | Buchanalyse abgeschlossen; SRC-0009 |
| B-0010 | Thinking, Fast and Slow                 | Daniel Kahneman                      | Entscheidungspsychologie          | P1        | DONE   | System 1/2, Biases, Prospect Theory               | Buchanalyse abgeschlossen; SRC-0010; ursprünglich als B-0015 katalogisiert |
| B-0011 | Emotional Intelligence                  | Daniel Goleman                       | Psychologie / Emotionsregulation  | P2        | DONE   | Amygdala-Regulation, emotionale Kompetenz         | Buchanalyse abgeschlossen; SRC-0011; im ursprünglichen Katalog nicht enthalten (Behavioral Science Expansion Sprint) |
| B-0012 | Predictably Irrational                  | Dan Ariely                          | Verhaltensökonomie                | P2        | DONE   | irrationale Entscheidungen                        | Buchanalyse abgeschlossen; SRC-0012; ursprünglich als B-0016 katalogisiert |
| B-0013 | Nudge: The Final Edition                | Richard H. Thaler & Cass R. Sunstein  | Verhaltensökonomie / Choice Architecture | P2  | DONE   | Defaults, Choice Architecture                     | Buchanalyse abgeschlossen; SRC-0013; im ursprünglichen Katalog nicht enthalten (Behavioral Science Expansion Sprint) |
| B-0014 | Priceless: The Myth of Fair Value       | William Poundstone                   | Verhaltensökonomie / Preispsychologie | P2    | DONE   | Ankerpreise, Fairness, Verhandlung                | Buchanalyse abgeschlossen; SRC-0014; im ursprünglichen Katalog nicht enthalten (Behavioral Science Expansion Sprint) |
| B-0015 | Made to Stick                           | Chip Heath & Dan Heath                | Kommunikation / Ideenpsychologie  | P2        | DONE   | Merkfähigkeit, Botschaftsdesign                   | Buchanalyse abgeschlossen; SRC-0015; ursprünglich als B-0014 katalogisiert |

### Offene Kandidaten (unverändert, keine Kollision mit abgeschlossenen IDs)

| ID     | Titel                                   | Autor                              | Kategorie                        | Priorität | Status  | Rolle im Sales Codex                              | Notizen                               |
| ------ | --------------------------------------- | ----------------------------------- | --------------------------------- | --------- | ------- | -------------------------------------------------- | -------------------------------------- |
| B-0018 | The Challenger Customer                 | Brent Adamson et al.                 | B2B Buying Committees             | P2        | WAITING | Buying Center, Konsensbildung                     | Ergänzung Challenger                  |
| B-0019 | Strategic Selling                       | Miller Heiman                        | B2B / komplexe Accounts           | P2        | WAITING | Stakeholder, Buying Process                       | Modellvergleich                       |
| B-0020 | Conceptual Selling                      | Miller Heiman                        | Consultative Selling              | P2        | WAITING | Kundenkonzept statt Produkt                       | Vergleich zu SPIN                     |
| B-0021 | Solution Selling                        | Michael Bosworth                     | Lösungsvertrieb                   | P2        | WAITING | Problem-Lösung-Logik                              | historisch wichtig                    |
| B-0022 | The New Strategic Selling               | Miller Heiman                        | B2B Strategie                     | P2        | WAITING | Account-Strategie                                 | später                                |
| B-0023 | SNAP Selling                            | Jill Konrath                         | Komplexer Vertrieb                | P2        | WAITING | überlastete Käufer                                | moderner Kontext                      |
| B-0024 | Let's Get Real or Let's Not Play        | Mahan Khalsa / Randy Illig            | Consultative Selling              | P2        | WAITING | Ehrlichkeit, Diagnose, Beratung                   | ethisch relevant                      |
| B-0025 | Secrets of Closing the Sale             | Zig Ziglar                           | Closing                           | P3        | WAITING | klassische Abschlusstechniken                     | kritisch prüfen                       |
| B-0026 | The Little Red Book of Selling          | Jeffrey Gitomer                      | Verkauf / Haltung                 | P3        | WAITING | klassische Praxistipps                            | kritisch einordnen                    |
| B-0027 | Sell or Be Sold                         | Grant Cardone                        | Verkauf / Mindset                 | P4        | WAITING | High-pressure Sales                               | ethisch kritisch prüfen               |
| B-0029 | Bargaining for Advantage                | G. Richard Shell                     | Verhandlung                       | P2        | WAITING | Verhandlungstypen, Strategie                      | Ergänzung                             |
| B-0030 | The Trusted Advisor                     | David H. Maister et al.               | Vertrauen / Beratung              | P1        | WAITING | Vertrauensaufbau in Beratung                      | sehr relevant für High-Ticket         |
| B-0031 | Trusted Advisor Fieldbook                | Charles H. Green / Andrea P. Howe     | Vertrauen / Beratung              | P2        | WAITING | Anwendung Trusted Advisor                         | Ergänzung                             |
| B-0032 | Start with Why                          | Simon Sinek                          | Motivation / Kommunikation        | P3        | WAITING | Sinn und Identität                                | kritisch prüfen                       |
| B-0033 | Atomic Habits                           | James Clear                          | Verhalten / Gewohnheiten          | P3        | WAITING | Verkäuferdisziplin, Lernsysteme                   | ergänzend                             |
| B-0034 | The E-Myth Revisited                    | Michael E. Gerber                    | Unternehmertum / Systeme          | P2        | WAITING | Systematisierung von Arbeit                       | relevant für Selbstständigkeit        |
| B-0035 | Profit First                            | Mike Michalowicz                     | Finanzen / Unternehmertum         | P3        | WAITING | finanzielle Steuerung                             | ergänzend                             |
| B-0036 | Blue Ocean Strategy                     | W. Chan Kim / Renée Mauborgne         | Strategie                         | P3        | WAITING | Differenzierung, Märkte                           | später                                |
| B-0037 | Crossing the Chasm                      | Geoffrey A. Moore                    | B2B / Technologievertrieb         | P3        | WAITING | Adoption, Zielgruppenlogik                        | relevant für Tech Sales               |
| B-0038 | Good Strategy Bad Strategy              | Richard Rumelt                       | Strategie                         | P3        | WAITING | strategisches Denken                              | ergänzend                             |
| B-0039 | The Mom Test                            | Rob Fitzpatrick                      | Kundeninterviews                  | P2        | WAITING | bessere Fragen, Bias-Vermeidung                   | stark relevant für Discovery          |
| B-0040 | Objections                              | Jeb Blount                           | Einwandbehandlung                 | P2        | WAITING | Einwände, Reframing, Follow-up                    | praxisnah                             |

### Offene Kandidaten (umnummeriert wegen ID-Kollision mit abgeschlossenen Büchern, Inhalt unverändert)

| ID     | Titel                                   | Autor                              | Kategorie                        | Priorität | Status  | Rolle im Sales Codex                              | Notizen                               |
| ------ | --------------------------------------- | ----------------------------------- | --------------------------------- | --------- | ------- | -------------------------------------------------- | -------------------------------------- |
| B-0041 | How to Win Friends and Influence People | Dale Carnegie                        | Kommunikation / Beziehung         | P1        | WAITING | Vertrauen, Beziehung, Sympathie                   | wichtig für Verkäuferverhalten; ursprünglich als B-0006 katalogisiert, umnummeriert wegen Kollision mit The JOLT Effect |
| B-0042 | Fanatical Prospecting                   | Jeb Blount                           | Akquise                           | P2        | WAITING | Prospecting, Disziplin, Pipeline                  | Prozess-/Aktivitätslogik; ursprünglich als B-0008 katalogisiert, umnummeriert wegen Kollision mit Pre-Suasion |
| B-0043 | New Sales. Simplified.                  | Mike Weinberg                        | Akquise / B2B                     | P2        | WAITING | strukturierte Neukundengewinnung                  | praxisnah; ursprünglich als B-0009 katalogisiert, umnummeriert wegen Kollision mit To Sell Is Human |
| B-0044 | The Psychology of Selling               | Brian Tracy                          | Verkauf / Mindset                 | P3        | WAITING | klassische Verkaufspsychologie                    | kritisch prüfen; ursprünglich als B-0010 katalogisiert, umnummeriert wegen Kollision mit Thinking, Fast and Slow |
| B-0045 | Exactly What to Say                     | Phil M. Jones                        | Sprache / Formulierungen          | P2        | WAITING | Mikroformulierungen und Gesprächsführung          | Technikbibliothek; ursprünglich als B-0011 katalogisiert, umnummeriert wegen Kollision mit Emotional Intelligence |
| B-0046 | Sell with a Story                       | Paul Smith                           | Storytelling                      | P2        | WAITING | Storytelling im Verkauf                           | relevant für Präsentation; ursprünglich als B-0012 katalogisiert, umnummeriert wegen Kollision mit Predictably Irrational |
| B-0047 | Building a StoryBrand                   | Donald Miller                        | Marketing / Storytelling          | P2        | WAITING | Positionierung und Narrative                      | Übergang Marketing-Vertrieb; ursprünglich als B-0013 katalogisiert, umnummeriert wegen Kollision mit Nudge |

---

## Arbeitsregel für Cowork

Cowork bearbeitet immer das erste Buch mit Status `READY`, sofern keine ausdrückliche Herausgeberanweisung etwas anderes vorgibt.

Nach Beginn setzt Cowork den Status auf `IN_PROGRESS`.

Nach Abschluss setzt Cowork den Status auf `REVIEW`.

Nur der Herausgeber setzt ein Buch auf `DONE`.

**Hinweis (2026-07-03):** In der Praxis wurde diese Arbeitsregel seit B-0003 nicht mehr über diesen Katalog gesteuert — die tatsächliche Buchauswahl erfolgte stattdessen über Editor-Priorisierung in Kombination mit Empfehlungen aus `04_synthesis/SPR-0001_Sales_Core_Synthesis/research_agenda.md` und späteren Sprintaufträgen (siehe `OPEN_DECISIONS.md`, OD-004, Auflösung). Dieser Katalog ist damit faktisch kein Pflichtsteuerungsinstrument mehr für die Buchauswahl, auch wenn er als Kandidaten-Backlog weitergeführt wird. Eine formale Entscheidung, ob dieser Katalog künftig wieder als verbindliches Steuerungsinstrument reaktiviert oder offiziell auf reinen Backlog-Status herabgestuft wird, wurde nicht getroffen — dies wird im External Audit Resolution Report als Beobachtung, nicht als neue Open Decision, dokumentiert (siehe dortiger Abschnitt zu diesem Kritikpunkt).

---

## Nächster geplanter Schritt

**Veraltet — nicht mehr repräsentativ für den aktuellen Repository-Zustand.** Alle 15 tatsächlich abgeschlossenen Bücher (B-0001–B-0015) sind oben mit Status `DONE` erfasst. Es gibt aktuell kein Buch mit Status `READY` in diesem Katalog. Die tatsächliche nächste Priorität für weitere Buchanalysen ist nicht in diesem Dokument, sondern in `00_project/NEXT_ACTION.md` und `00_project/ACADEMIC_RECOVERY_PLAN.md` dokumentiert (Stand 2026-07-03: Fortsetzung Academic Recovery Plan Tier 1 hat Priorität vor neuen Buchanalysen).
