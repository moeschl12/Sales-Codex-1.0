# Open Decision Resolution Report — 2026-07

**Sprint-Typ:** Governance-Sprint (ausschließlich redaktionell — keine neue Recherche, keine neuen Wissensobjekte, keine Framework-Änderungen, keine Academic Recovery)
**Auslöser:** Herausgeberauftrag „OPEN DECISIONS RESOLUTION SPRINT" nach Abschluss von: 10 Buchanalysen, Sprint-1- und Sprint-2-Synthese, Peer Review Sprint 1 + 2, Academic Recovery Phase 1 + 2, Gemini Scientific Review, Claude Response Review, vollständigem Codex Audit, Consistency Correction Sprint.
**Bearbeitete Datei:** `00_project/OPEN_DECISIONS.md` (Primärartefakt) sowie Governance-Dateien `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`, `00_project/changelog.md`.
**Rolle:** Ausschließlich Herausgeber-Redaktion. Keine eigene Erinnerung als Autorität — jede Bewertung stützt sich auf im Repository dokumentierte Belege (Session Log, Changelog, Wissensobjekte, Berichte).

---

## 1. Zusammenfassung

Alle acht bestehenden Open Decisions (OD-001 bis OD-008) wurden einzeln gegen den aktuellen Repository-Zustand geprüft. Vier Entscheidungen (OD-001 bis OD-004) waren objektiv bereits umgesetzt und wurden auf **DONE** gesetzt. Eine Entscheidung (OD-005) wurde als **ERSETZT** markiert — ihre wörtliche Fragestellung (Gemini als Instrument) wurde nie umgesetzt, ihre inhaltliche Absicht (externe Validierung) aber über andere, bereits laufende Instrumente weitgehend erfüllt; sie wird durch die grundsätzlichere OD-010 (Validierungs-Governance) abgelöst. Drei Entscheidungen (OD-006, OD-007, OD-008) bleiben **OFFEN** — bei OD-006 und OD-007 ausdrücklich weisungsgemäß ohne automatischen Schluss, bei OD-008 mangels neuer Entwicklung seit Eintragung. Drei neue, langfristige Architektur-Entscheidungen wurden identifiziert und angelegt (OD-009, OD-010, OD-011) — keine davon ist eine Forschungsaufgabe; alle drei sind Governance-/Versionierungsfragen, deren Grundlagen bereits im Repository vorliegen.

**Bilanz:** 8 geprüft → 4 DONE, 1 ERSETZT, 3 OFFEN → 3 neue OD angelegt → 11 OD im Repository nach Bereinigung (4 geschlossen, 1 ersetzt = 5 „erledigt" im weiteren Sinne; 6 aktiv offen: OD-006, OD-007, OD-008, OD-009, OD-010, OD-011).

---

## 2. Welche Entscheidungen geschlossen wurden (DONE)

| OD | Frage (verkürzt) | Beleg für Abschluss |
|---|---|---|
| OD-001 | Post-Mortem nach Influence durchführen | `POST_MORTEM_B0002.md` erstellt 2026-06-30, 12 Phasen, vollständig |
| OD-002 | Book Mode offiziell einführen | v1.1-Release 2026-06-30: Operating Manual, COWORK_EXECUTION_PROTOCOL, task_rules.md aktualisiert; seither 7× angewendet (B-0003–B-0010) |
| OD-003 | Framework v1.1 einfrieren | v1.1 freigegeben 2026-06-30 (CURRENT_STATE.md); 5/6 Inhalte umgesetzt, 1 Restlücke dokumentiert (kein formales Health-Check-Protokoll) |
| OD-004 | Nächstes Buch nach Influence festlegen | B-0003 = Never Split the Difference gewählt und abgeschlossen 2026-06-30; Folgebücher über etabliertes Nachfolgeverfahren (Editor-Priorisierung + research_agenda.md) statt dieser OD ausgewählt |

Alle vier Abschlüsse erfüllen die Sprintvorgabe „OD-001 bis OD-005 dürfen geschlossen werden, wenn die Entscheidung objektiv bereits umgesetzt wurde" — jeder Abschluss stützt sich auf ein konkretes, im Repository auffindbares Artefakt (Datei, Changelog-Eintrag, Session-Log-Eintrag), nicht auf Erinnerung oder Vermutung.

OD-003 wurde bewusst nicht unter den Teppich gekehrt: Die Freeze-Entscheidung selbst wurde vollzogen (fünf von sechs geplanten Inhalten sind nachweisbar umgesetzt und seit acht Buchanalysen in Kraft), aber ein einzelner geplanter Inhalt — „Repository Health Check verpflichtend" — wurde laut `POST_MORTEM_B0002.md` Phase 11 nie formalisiert. Dies wird als Restlücke im OD-Eintrag dokumentiert (Prinzip: Widersprüche/Lücken dokumentieren statt glätten), begründet aber keine neue Open Decision, da es sich um einen operativen Nacharbeitspunkt (Prozessschritt-Formalisierung) und keine Architekturfrage handelt.

---

## 3. Welche offen bleiben

| OD | Status | Begründung |
|---|---|---|
| OD-006 | OFFEN — entscheidungsreif | Weisungsgemäß nicht automatisch schließbar. Analyse vollständig, keine neuen Entwicklungen seit 2026-07-01. Wartet auf Herausgeber-Entscheidung zu Format/Bewertungsskala eines Meme-Risiko-Feldes. |
| OD-007 | OFFEN — entscheidungsreif | Weisungsgemäß nicht automatisch schließbar. Vollständigste wissenschaftliche Analyse aller offenen Entscheidungen (3 Optionen ausgearbeitet), keine neuen Entwicklungen. Wartet auf Herausgeber-Wahl zwischen Einführung/optional/Beibehaltung Status quo. |
| OD-008 | OFFEN — weiterhin relevant | Keine implizite Beantwortung seit Eintragung (2026-07-01); `NEXT_ACTION.md` referenziert die Entscheidung unverändert. Editor-Empfehlung (Tier-1-Fortsetzung vorrangig) bleibt Empfehlung, keine Vorentscheidung. |
| OD-009 (neu) | OFFEN | Neu angelegt — Framework-RC1-Statusübergang. Grundlagen liegen vor (Reifegradbericht, Audit), formaler Übergangsmechanismus fehlt. |
| OD-010 (neu) | OFFEN | Neu angelegt — Nachfolger von OD-005. Validierungs-Policy über mehrere Instrumente hinweg fehlt. |
| OD-011 (neu) | OFFEN | Neu angelegt — Verhältnis von `LITERATURE_INDEX.md` zu `SCIENTIFIC_DEBT.md`/`review_queue.md` ungeklärt. |

Für OD-006 und OD-007 wurde explizit geprüft, ob spätere Entwicklungen sie implizit entschieden haben — das ist nicht der Fall. Beide sind seit ihrer Eintragung (2026-07-01) inhaltlich unverändert und warten ausschließlich auf eine explizite Herausgeber-Wahl zwischen bereits ausformulierten Optionen. Eine Umstrukturierung (z. B. Zusammenlegung von OD-006 mit der in seinem eigenen Text erwähnten Begriffsinflations-Frage) wurde erwogen, aber bewusst nicht eigenständig vorgenommen — das wäre eine inhaltliche Vorentscheidung, die laut Sprintvorgabe dem Herausgeber vorbehalten bleibt.

---

## 4. Welche ersetzt wurden

**OD-005 (Gemini-Validierung der Mechanismen) → ERSETZT durch OD-010 (Validierungs-Governance).**

Die ursprüngliche Frage war eng auf ein einzelnes Instrument (Gemini) und einen einzelnen Objektkreis (Cialdini-MECs) zugeschnitten. In der Praxis wurde seit Eintragung nie Gemini eingesetzt, wohl aber wurden dieselben und weitere Mechanismen (MEC-0005 bis MEC-0011) über Peer Review Sprint 1, Academic Recovery Sprint Phase 2 (Research Pack 3/4) und Sprint-3-Review substanziell extern geprüft — mit dokumentierten Ergebnissen (eine Herabstufung, mehrere Konvergenzbestätigungen). Die inhaltliche Absicht von OD-005 ist damit größtenteils erfüllt, aber uneinheitlich und ohne übergeordnete Policy. OD-010 stellt die daraus resultierende, grundsätzlichere Frage: welche Instrumente künftig für welche Evidenzlevel-Übergänge als hinreichend gelten. Dies ist die editoriell sauberere Fortführung, statt OD-005 entweder fälschlich als „done" (Gemini wurde nie benutzt) oder unverändert als „offen" (obwohl faktisch bereits viel Validierungsarbeit stattfand) zu belassen.

---

## 5. Begründung jeder Entscheidung

**OD-001 (DONE):** Direkter Beleg — `POST_MORTEM_B0002.md` existiert, ist vollständig (12 Phasen) und wurde in der Session vom 2026-06-30 als abgeschlossen protokolliert. Keine Interpretation nötig.

**OD-002 (DONE):** Direkter Beleg — alle drei in der OD selbst genannten Zieldokumente wurden nachweislich aktualisiert (changelog.md, 2026-06-30). Zusätzlich siebenfache Praxisbestätigung durch nachfolgende Buchanalysen.

**OD-003 (DONE, mit Restlücke):** Die Freeze-Entscheidung ist ein Vollzugsakt (Versionsnummer wurde erhöht und ist seit 2026-06-30 aktiv) — unabhängig davon, ob jeder einzelne geplante Unterpunkt vollständig umgesetzt wurde. Fünf von sechs Punkten sind belegt; der sechste wird transparent als offene Lücke geführt statt rückwirkend als erledigt dargestellt.

**OD-004 (DONE):** Die Frage war als Einzelentscheidung für B-0003 formuliert, nicht als dauerhafter Auswahlmechanismus. Sie wurde für B-0003 beantwortet; alle späteren Bücher folgten einem anderen, in S1-SYNTHESIS etablierten Verfahren. Das macht die ursprüngliche OD nicht nur erledigt, sondern gegenstandslos für alle Folgefragen.

**OD-005 (ERSETZT):** Siehe Abschnitt 4. Weder „DONE" (Instrument nie verwendet) noch unverändert „OFFEN" (Absicht faktisch erfüllt) trifft den Sachverhalt korrekt — ERSETZT durch eine allgemeinere Nachfolgefrage ist die genaueste Klassifikation.

**OD-006 (OFFEN):** Ausdrücklich von der Automatik ausgenommen. Es gibt keine neuen Fakten seit 2026-07-01, die eine andere Einschätzung rechtfertigen würden. Entscheidungsreif, aber nicht entschieden.

**OD-007 (OFFEN):** Ausdrücklich von der Automatik ausgenommen. Am gründlichsten vorbereitete offene Entscheidung im gesamten Repository (vollständige Für-/Gegen-Analyse, drei Optionen, Editor-Einschätzung ohne Vorentscheidung). Wartet ausschließlich auf Felix.

**OD-008 (OFFEN):** Keine der beiden Prüffragen („faktisch beantwortet?", „implizit entschieden?") trifft zu. Weder wurde ein ELM/Trust/PKM-Sprint gestartet, noch wurde Tier 1 des Academic Recovery Plan explizit durch eine Herausgeber-Entscheidung bestätigt (nur durchgehend als Editor-Empfehlung wiederholt).

**OD-009, OD-010, OD-011 (neu):** Alle drei erfüllen die Sprintvorgabe „langfristige Architekturentscheidungen, keine operativen Aufgaben". Keine ist eine neue Forschungsfrage — alle drei betreffen ausschließlich, wie das Repository künftig mit bereits vorhandenem Material und bereits etablierten Prozessen umgeht (Statusdefinition, Validierungs-Policy, Dokumentbeziehungen).

---

## 6. Governance-Reifegrad nach Bereinigung

Vor diesem Sprint enthielt `OPEN_DECISIONS.md` acht Einträge, von denen laut `CODEX_AUDIT_2026-07.md` (Kapitel „Open Decisions") **null als DONE markiert waren** — obwohl mindestens vier davon (OD-001 bis OD-004) bei genauer Prüfung objektiv bereits erledigt waren. Das war ein reines Pflegeproblem, kein inhaltliches: Governance-Dokumente wurden nach Abschluss der jeweiligen Arbeit nicht mehr zurück auf die offenen Entscheidungen gespiegelt.

Nach diesem Sprint gilt:

- **Pflegezustand:** von 0/8 auf 4/8 DONE + 1/8 ERSETZT korrigiert — kein Eintrag ist mehr fälschlich als offen gelistet, obwohl er erledigt ist.
- **Entscheidungsreife:** Die drei aktiven Kern-Entscheidungen (OD-006, OD-007, OD-008) sind alle vollständig ausgearbeitet und warten ausschließlich auf eine explizite Herausgeber-Wahl — keine davon erfordert weitere Recherche, bevor Felix entscheiden kann.
- **Neue Lücke sichtbar gemacht:** Die drei neuen OD (009–011) zeigen, dass der Codex nun an einem Punkt ist, an dem nicht mehr einzelne Wissensinhalte, sondern **Prozess- und Versionsgovernance** die limitierende Dimension ist — ein Reifezeichen (Inhaltsarbeit ist weit fortgeschritten: 10 Bücher, 2 Synthesen, 2 Peer Reviews, 2 Academic-Recovery-Phasen; die verbleibenden offenen Fragen sind strukturell/prozessual, nicht mehr primär inhaltlich).
- **Unverändert bestehende Lücke:** OD-003s Restlücke (Repository Health Check) zeigt, dass Governance-Pflege selbst noch nicht vollständig verlässlich ist — Prozessschritte werden geplant, aber nicht immer formalisiert nachgehalten.

**Gesamteinschätzung:** Governance-Reifegrad hat sich durch diesen Sprint von „inhaltlich erledigt, aber nicht nachgeführt" zu „aktuell, vollständig nachgeführt, mit klar benannten aktiven Entscheidungspunkten" verbessert. Dies ist ein reiner Dokumentationsgewinn — keine inhaltliche Aussage über den wissenschaftlichen Reifegrad des Codex selbst (dieser bleibt laut `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` und `CODEX_AUDIT_2026-07.md` bei B/B+, unverändert durch diesen Sprint, da hier ausdrücklich keine Academic Recovery und keine neue Bewertung stattfand).

---

## 7. Empfehlung für den nächsten Governance-Schritt

1. **Priorität 1 — Herausgeber-Entscheidungen einholen:** OD-006 und OD-007 sind vollständig entscheidungsreif und sollten vor jeder weiteren inhaltlichen Arbeit entschieden werden, da beide potenziell Framework-Änderungen nach sich ziehen, die spätere Buchanalysen/Sprints rückwirkend betreffen könnten (je später entschieden, desto größer der Nacharbeitsaufwand bei „Ja").
2. **Priorität 2 — OD-008 vs. Academic Recovery Plan Tier 1:** Eine explizite Priorisierungsentscheidung (nicht nur Editor-Empfehlung) würde die seit zwei Sprints wiederholte Unklarheit auflösen.
3. **Priorität 3 — OD-009/010/011 als Paket behandeln:** Alle drei sind Governance-Architektur-Fragen ohne inhaltliche Abhängigkeit voneinander, könnten aber in einer einzigen Sitzung mit Felix gemeinsam entschieden werden, da sie sich gegenseitig informieren (z. B. hängt eine sinnvolle RC1-Kriterienliste in OD-009 auch davon ab, wie OD-010 die Validierungs-Kadenz regelt).
4. **Danach:** Fortsetzung der zuletzt vor diesem Governance-Sprint gültigen inhaltlichen Priorität — `ACADEMIC_RECOVERY_PLAN.md` Tier 1 (AR-001, AR-002, AR-013) — unverändert, da dieser Sprint ausdrücklich keine inhaltliche Priorität verschoben hat.
5. **Operativ, nicht als OD:** Die in OD-003 dokumentierte Restlücke (Repository Health Check) sollte bei Gelegenheit eines künftigen Consistency-/Correction-Sprints nachgeholt werden — kein Herausgeber-Entscheid nötig, nur Umsetzung.

---

*Bericht erstellt: 2026-07-02. Ausschließlich Governance-Redaktion — keine neuen Wissensobjekte, keine neue Recherche, keine Framework-Änderungen, keine Academic Recovery.*
