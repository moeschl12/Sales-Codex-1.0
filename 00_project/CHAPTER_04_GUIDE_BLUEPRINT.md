# Kapitel-4-Blueprint: Entscheidungshürden reduzieren

**Dokumentklasse:** Redaktionelle Kapitel-Vorlage (Blueprint), keine T12-Publikationsarbeit im engeren Framework-Sinn — siehe Abschnitt 8.
**Auftrag:** Redaktionelle Vorbereitung von Leitfaden-Kapitel 4 (Felix, 2026-07-15).
**Charakter:** Vorlage/Struktur für einen späteren Schreibsprint. Kein finaler Kapiteltext, keine neuen Wissensobjekte, keine Änderungen an bestehenden Objekten, keine Evidenzlevel-Änderungen, keine externe Recherche. Kein Commit, kein Push.
**Leserfrage laut Auftrag:** Was hilft, wenn ein Käufer nicht Nein sagt, aber nicht entscheiden kann?

**Gelesene Grundlage (tatsächliche Pfade):**
- Pflichtstart: `PROJECT_BOOTSTRAP.md`, `SESSION_BRIEF.md`, `00_project/NEXT_ACTION.md`, `TASK_TYPES.md`
- `00_project/CODEX_GUIDE_STRUCTURE.md`, `00_project/CODEX_MERGE_READINESS_OVERVIEW.md` (vollständig), `00_project/ACADEMIC_RECOVERY_CONSOLIDATION_REPORT.md` (Abschnitte AR-013/ED-AR-2, gezielt), `00_project/SCIENTIFIC_DEBT.md` (Abschnitt B-0006 vollständig gelesen; restliche Datei — 542 Zeilen — per `rg` auf die hier relevanten Objekt-IDs geprüft, nicht zeilenweise vollständig gelesen; Fundstellen: Zeile 97 T-0022/MEC-0015, Zeile 101–109 B-0006, Zeile 252–256 SD-SYS-003)
- Formatreferenz (Präzedenz): `00_project/CHAPTER_03_GUIDE_BLUEPRINT.md`, `00_project/CHAPTER_06_GUIDE_BLUEPRINT.md`
- Tragende Objekte (vollständig gelesen): `03_knowledge_base/mechanisms/MEC-0015_kognitive_ueberlastung_durch_feature_overload.md`, `03_knowledge_base/mechanisms/MEC-0016_fomu_entscheidungsangst_durch_fehlerrisiko.md`, `03_knowledge_base/principles/P-S1-004_informationssparsamkeit_als_wirkungsverstaerker.md`, `03_knowledge_base/techniques/T-0022_gap_demo_methode.md`, `03_knowledge_base/statements/ST-0305_decision_paralysis_tversky_shafir.md`, `03_knowledge_base/statements/ST-0310_konfliktbedingte_optionssuche_tversky_shafir.md`
- Alle Dateinamen entsprachen den im Auftrag genannten IDs; keine Abweichung, kein `rg`-Fallback nötig.

**Datum:** 2026-07-15

---

## 1. Kapitelrolle im Gesamtleitfaden

Laut `CODEX_GUIDE_STRUCTURE.md` ist Kapitel 4 das vierte von sieben Kapiteln im Kaufprozess-Bogen, mit der Leitfadenreife **A mit B-Elementen** und an vierter Stelle der Schreibreihenfolge (nach Kapitel 6, 3, 1).

**Wofür Kapitel 4 zuständig ist:**

Das Kapitel beantwortet, warum ein Käufer, der grundsätzlich interessiert ist und nicht ablehnt, trotzdem nicht zu einer Entscheidung kommt — und was strukturell dagegen hilft. Es unterscheidet dabei explizit mehrere, kausal unterschiedliche Hürden (siehe Abschnitt 4) statt sie als eine einzige "Unentschlossenheit" zu behandeln: Informationsüberlastung/Feature Overload, Konflikt zwischen vergleichbar attraktiven Optionen, Unsicherheit/Risiko, tatsächlicher (nicht überflüssiger) Informationsbedarf und, nur soweit durch die tragenden Objekte gedeckt, Status-quo-/Aufschublogik.

**Wofür Kapitel 4 nicht zuständig ist:**

- Keine Bedarfsentwicklung oder Problemdiagnose selbst (Kapitel 1) — Kapitel 4 setzt voraus, dass ein Problem bereits entwickelt ist, und behandelt ausschließlich die Hürde danach, vor der finalen Entscheidung.
- Keine Reframing-/Insight-Logik oder Statusquo-Überwindung (Kapitel 2) — Kapitel 4 beginnt erst, nachdem der Status quo bereits infrage gestellt wurde, und behandelt nur, warum danach trotzdem nicht entschieden wird.
- Keine Verständlichkeits-/Vertrauensarbeit auf Ebene einer einzelnen Aussage oder Präsentation (Kapitel 3) — Kapitel 3 behandelt kognitive Entlastung auf Formulierungsebene; Kapitel 4 behandelt sie auf Ebene der Options- und Informationsmenge im gesamten Entscheidungsprozess.
- Keine interne Vertretbarkeit, Champion- oder Buying-Center-Arbeit (Kapitel 5) — auch wenn ein diffuser Entscheiderkreis eine der Ursachen für "Nicht-Entscheiden-Können" sein kann, behandelt Kapitel 4 nur die individuelle Entscheidungslogik, nicht die organisationale Konsensbildung.
- Keine Preis-, Anker- oder Verhandlungsfairness-Fragen (Kapitel 6) — auch wenn Risikoabbau/Empfehlung preisnahe Formulierungen berühren kann, ist die Verhandlungslogik selbst eigenständig in Kapitel 6 verortet.
- Kein geschlossenes JOLT-Gesamtsystem und keine Buying-Center-Konsenstheorie als Erklärung für Aufschub (siehe Leitplanken/Abschnitt 6).

---

## 2. Tragende Objekte

| Objekt | Typ | Funktion im Kapitel | Evidenz-/Transfergrenze |
|---|---|---|---|
| **MEC-0015** | Mechanismus | **Tragend, Kern.** Kognitive Überlastung durch Informations- und Optionsüberflut. Deckt in seiner aktuellen (erweiterten) Fassung vier Auslösepfade ab: (a) Feature-Overload in der Präsentation, (b) Choice-Overload bei Kaufoptionen, (c) irrelevante Unsicherheit über einen Weltzustand (Tversky & Shafir 1992, 3(5), gestützt durch ST-0305), (d) Attributkonflikt zwischen nicht-dominierten, vergleichbar attraktiven Optionen (Tversky & Shafir 1992, 3(6), gestützt durch ST-0310, ED-AR-2). Trägt damit drei der fünf Leser-Kategorien aus Abschnitt 4. | E5 (Miller's Law) für den Grundmechanismus, E4 (Paradox of Choice; beide Tversky/Shafir-Studien) für die Erweiterungspfade, E2 für die konkrete Sales-/Demo-Anwendung. Pfade (c) und (d) beruhen auf Einzelstudien ohne Multi-Labor-Replikation im Codex-Bestand. |
| **MEC-0016** | Mechanismus | **Tragend, mit expliziter Grenze.** FOMU/antizipatorische Reue als möglicher Treiber von Nicht-Entscheiden. AR-013 hat Tversky & Shafir (1992) gezielt als mögliche akademische Stütze für MEC-0016 geprüft und **explizit verneint** (anderer kausaler Mechanismus: Attributkonflikt statt antizipierte Reue) — MEC-0016 bleibt insofern auf seiner ursprünglichen Quellenbasis stehen. | E4 für den allgemeinen Kern (antizipatorische Reue, Omission Bias — peer-reviewed, gut repliziert), E2 für die B2B-Kaufanwendung (aus JOLT-ML-Analyse abgeleitet, nicht direkt gemessen). **Scientific Debt aktiv, nicht aufgelöst** (siehe Abschnitt 7). |
| **P-S1-004** | Prinzip | **Tragend, Kern.** Informationssparsamkeit als Wirkungsverstärker — trägt die Kategorie "zu viele Informationen" sowie die Abgrenzung zu "echtem Informationsbedarf" (Kontextgrenzen-Abschnitt des Objekts selbst nennt Discovery-Phase und technische Pflicht-Reviews als Bereiche, in denen das Prinzip *nicht* gilt). | E5 (Miller's Law) + E2 (methodologische Konvergenz aus vier Büchern, QK-4). Cross-Book-Konvergenz ersetzt keine unabhängige Studie — SD-SYS-003 (Zirkelschlussrisiko bei Meta-Prinzipien) betrifft dieses Objekt ausdrücklich (siehe Abschnitt 7). |
| **T-0022** | Technik | **Optionales Beispiel, nicht tragend.** Gap-Demo-Methode / 6-Feature-Regel — eine mögliche, aber aus dem Gap-Selling-Cluster stammende Umsetzung von P-S1-004/MEC-0015 im Demo-Kontext. `CODEX_GUIDE_STRUCTURE.md` führt T-0022 nicht als Kernobjekt von Kapitel 1; wegen der Quellenvollständigkeitslücke von Gap Selling soll die Technik im Kapiteltext nur erscheinen, wenn eine gekennzeichnete E2-Praxisillustration wirklich benötigt wird. | E2 (Practitioner-Empfehlung); Miller's Law selbst E5. Scientific-Debt-Eintrag (SCIENTIFIC_DEBT.md Zeile 97, Priorität Niedrig): der optimale Feature-Count für Sales-Demos ist empirisch nicht gemessen — die "6" ist eine Extrapolation, kein direkt getesteter Wert. |
| **ST-0305** | Statement (akademische Stütze, kein eigenständiges Kapitelobjekt) | **Kontext/Begründung**, nicht selbstständig zitierfähig — trägt indirekt über MEC-0015 Pfad (c). Liefert die wissenschaftliche Grundlage für "irrelevante Unsicherheit lähmt" (Hawaii-Reise-Experiment) und "eine zusätzliche gute Option erhöht Rückkehr zur Standardoption" (Vorlesung-vs.-Lernen-Experiment). | Zwei unabhängige, publizierte Einzelexperimente (Tversky & Shafir 1992, 3(5); Redelmeier & Shafir 1995) mit Studierendenstichproben; kein direkter B2B-Kauftest. Bereits vollständig in MEC-0015 integriert — im Kapiteltext nicht zusätzlich als eigenständige Quelle einführen. |
| **ST-0310** | Statement (akademische Stütze, kein eigenständiges Kapitelobjekt) | **Kontext/Begründung**, trägt indirekt über MEC-0015 Pfad (d). Liefert die wissenschaftliche Grundlage für "Konflikt zwischen nicht-dominierten Optionen erhöht Suche nach Zusatzoptionen". Wurde zusätzlich **explizit gegen MEC-0016 geprüft und liefert dort keine Stützung** — diese Abgrenzung ist für Kapitel 4 wichtig, um Konfliktpfad und FOMU nicht zu vermischen. | E4 (peer-reviewte Einzelstudie mit zwei Aufgabendomänen — Wetten, Wohnungen — innerhalb desselben Experiments; keine externe Multi-Labor-Replikation im Codex-Bestand). Eine frühere, überzogene Formulierung ("unabhängig von antizipierter Reue") wurde am 2026-07-13 bereits sprachlich korrigiert — dieser Korrekturstand ist maßgeblich. |

**Bewusst nicht als tragend aufgenommen (nur Kontext/Grenze, nicht einzeln als Objektdatei gelesen — Angaben aus `CODEX_MERGE_READINESS_OVERVIEW.md`, `SCIENTIFIC_DEBT.md` und den "Verknüpfte Techniken/Prinzipien"-Abschnitten von MEC-0015/MEC-0016 erschlossen):**

- **MOD-0006 (JOLT-Modell), T-0026–T-0030, ST-0151** — tragen laut Merge-Readiness-Übersicht die JOLT-Gesamtlogik und die vier JOLT-Techniken. Laut Auftrag ausdrücklich **nicht** als geschlossenes, bewiesenes System lehren; JOLT-Techniken dürfen nur als begrenzte Anwendungssprache erscheinen (siehe Abschnitt 6). Die 44/56-Split-Zahl (ST-0151/MOD-0006) ist laut `SCIENTIFIC_DEBT.md` B-0006 weiterhin unrepliziert (Priorität Mittel, "AR-013 geprüft, nicht aufgelöst").
- **P-0027, P-0028, P-0030 sowie T-0026, T-0027, T-0029** (aus MEC-0016 "Verknüpfte Prinzipien/Techniken") — nicht Teil des Auftragsscopes, nur als Hinweis, dass MEC-0016 im Codex an weitere JOLT-nahe Objekte anschließt, die hier nicht einzeln geprüft wurden.
- **MEC-0002 (Verlustaversion/Status-quo-Bias)** — trägt den eigentlichen Status-quo-Mechanismus und gehört zum Kern der Kapitel 1/2. Für Kapitel 4 nur am Rand relevant, weil MEC-0015s Erweiterungen (über ST-0305/ST-0310) eine "Rückkehr zur Default-Option" beschreiben, ohne dass MEC-0002 selbst zu den mandatierten Kapitel-4-Kernobjekten zählt (siehe Abschnitt 4, Kategorie 5).

---

## 3. Mögliche Kapitelstruktur

Vorschlag: sechs Unterabschnitte (Rahmung, drei Hürden-Abschnitte entlang der tragenden Objekte, ein FOMU-Abschnitt mit eingebauter Warnung, ein Abschluss zur Antwortlogik).

### 3.1 Warum ein interessierter Käufer trotzdem nicht entscheidet

- **Leserfrage:** Warum sagt ein Käufer nicht Nein, kauft aber auch nicht?
- **Kernbotschaft:** Nicht-Entscheiden ist keine automatische Ablehnung und keine einheitliche Ursache — verschiedene Hürden brauchen verschiedene Antworten.
- **Tragende Objekte:** MEC-0015, MEC-0016 (beide nur als Rahmenbegriffe eingeführt, noch nicht im Detail).
- **Zulässige Leser-Sprache:** "Ein Käufer, der nicht entscheidet, hat nicht automatisch 'Nein' gesagt — aber er braucht auch nicht automatisch mehr Überzeugungsarbeit."
- **Grenzen/Vorsicht:** Kein geschlossenes JOLT-Modell als Rahmen einführen; keine 44/56-Zahl nennen, auch nicht als Einstiegsstatistik.

### 3.2 Wenn zu viele Informationen oder Optionen die Entscheidung blockieren

- **Leserfrage:** Warum wirkt "noch mehr Auswahl" oder "noch mehr Information" manchmal wie das Gegenteil von Hilfe?
- **Kernbotschaft:** Das Arbeitsgedächtnis ist begrenzt; mehr Features oder Optionen, als der Käufer verarbeiten kann, erzeugen Verwirrung und Vermeidung statt eine bessere Entscheidung.
- **Tragende Objekte:** MEC-0015 (Pfade a/b: Feature-/Choice-Overload), P-S1-004.
- **Zulässige Leser-Sprache:** "Weniger, aber relevantere Information zur richtigen Zeit wirkt stärker als mehr Information." (Laut Merge-Readiness eine starke, robust gestützte Praxisregel.)
- **Grenzen/Vorsicht:** Die 6-Feature-Regel nicht als empirisch optimierten Wert darstellen (nicht direkt gemessen). T-0022 gehört nicht zum Kern von Kapitel 1 und sollte wegen der Gap-Selling-Quellenlücke im Kapitel 4 nur bei echtem didaktischem Bedarf, klar als E2-Praxisillustration, erscheinen.

### 3.3 Wenn zwei gute Optionen im Widerspruch stehen

- **Leserfrage:** Warum zögert ein Käufer, wenn er zwischen zwei fast gleich attraktiven Optionen wählen muss?
- **Kernbotschaft:** Ein schwer auflösbarer Konflikt zwischen nicht-dominierten Optionen erhöht die Suche nach Zusatzoptionen und die Rückkehr zur Standardoption — unabhängig von der reinen Optionsmenge.
- **Tragende Objekte:** MEC-0015 (Pfad d), ST-0310.
- **Zulässige Leser-Sprache:** "Wenn zwei Angebote jeweils eigene, echte Vorteile haben, wird die Wahl selbst zur Last — das ist keine Unentschlossenheit des Käufers als Charakterzug, sondern eine bekannte Reaktion auf einen echten Zielkonflikt."
- **Grenzen/Vorsicht:** Nicht mit FOMU (3.5) vermischen — AR-013 hat diese Trennung ausdrücklich geprüft und bestätigt. ST-0310 ist eine Einzelstudie ohne Multi-Labor-Replikation und ohne direkten B2B-Test.

### 3.4 Wenn Unsicherheit selbst lähmt, auch ohne viele Optionen

- **Leserfrage:** Warum zögert ein Käufer, wenn eigentlich nur noch eine Nebenfrage offen ist (Budget-Freigabe, Timing, wer noch zustimmen muss)?
- **Kernbotschaft:** Schon reine Unsicherheit über einen im Grunde irrelevanten Zustand kann eine Entscheidung aufschieben — selbst wenn der Käufer sich bei jedem möglichen Ausgang gleich entscheiden würde.
- **Tragende Objekte:** MEC-0015 (Pfad c), ST-0305.
- **Zulässige Leser-Sprache:** "Eine offene Nebenfrage kann eine Entscheidung genauso aufschieben wie ein echtes inhaltliches Bedenken."
- **Grenzen/Vorsicht:** ST-0305 beruht auf zwei Laborexperimenten mit Studierenden (Hawaii-Reise, Vorlesung-vs.-Lernen) — kein direkter B2B-Test. Nicht als Regel für jede Art Unsicherheit verallgemeinern; abzugrenzen von echtem, sachlich relevantem Informationsbedarf (Kategorie 1 in Abschnitt 4).

### 3.5 Wenn die Angst vor der falschen Entscheidung selbst zur Bremse wird

- **Leserfrage:** Was, wenn der Käufer inhaltlich überzeugt wirkt, aber trotzdem nicht unterschreibt?
- **Kernbotschaft:** Die Vorstellung, sich falsch zu entscheiden, kann Handeln blockieren, auch wenn Nicht-Handeln real riskanter wäre. Das ist ein möglicher Treiber unter mehreren — kein automatisch dominanter.
- **Tragende Objekte:** MEC-0016.
- **Zulässige Leser-Sprache:** "Manche Käufer zögern nicht aus Zweifel am Angebot, sondern aus Angst, selbst die falsche Wahl zu treffen."
- **Grenzen/Vorsicht — wichtiger, im Repository dokumentierter Widerspruch:** Das Objekt MEC-0016 selbst formuliert im Feld "Vertriebsrelevanz": *"Sehr hoch — erklärt den dominanten Mechanismus hinter 56 % der No-Decision-Verluste und begründet alle vier JOLT-Elemente als kohärente Gegenmaßnahmen."* Diese Formulierung steht im Widerspruch zur Auftragsleitplanke "FOMU nicht als immer dominierenden Haupttreiber darstellen" und zur SCIENTIFIC_DEBT.md-Einstufung (44/56-Split weiterhin unrepliziert, MEC-0016-Validierung "AR-013 geprüft, nicht aufgelöst"). Dieser Widerspruch wird hier dokumentiert, nicht geglättet, und darf im späteren Kapiteltext **nicht** durch Übernahme der "sehr hoch/dominant"-Formulierung aufgelöst werden. Eine Korrektur des MEC-0016-Objekttexts selbst liegt außerhalb dieses Auftrags (siehe Abschnitt 8).

### 3.6 Was einem Käufer wirklich weiterhilft — Orientierung statt Drängen

- **Leserfrage:** Was kann ein Verkäufer konkret tun, wenn ein Käufer "hängt"?
- **Kernbotschaft:** Je nach diagnostizierter Hürde helfen unterschiedliche Antworten: gezielte Reduktion, Vergleichshilfe, Risikoabbau oder echte zusätzliche Information — nie ein pauschales Vorgehen für alle Fälle.
- **Tragende Objekte:** P-S1-004; Querverweis auf die begrenzte, nicht als System zu lehrende JOLT-Sprache (Kontextobjekte aus Abschnitt 2). T-0022 kann allenfalls als gekennzeichnete E2-Illustration dienen.
- **Zulässige Leser-Sprache:** "Eine begründete Empfehlung kann Orientierung geben — sie ersetzt nicht die Entscheidung des Käufers."
- **Grenzen/Vorsicht:** Kein geschlossenes JOLT-Technikset als Gesamtlösung lehren. Eine Empfehlung darf nicht wie Bevormundung oder wie eine verdeckte Verknappung wirken (siehe Abschnitt 6).

---

## 4. Entscheidungshürden-Taxonomie für Leser

Die folgende Übersicht ist eine **redaktionelle Übersetzung bereits bestehender Codex-Objekte in Leser-Sprache** — kein neues Codex-Modell, keine neue Wissensbehauptung, kein neues Objekt. Sie darf im späteren Kapiteltext als didaktisches Ordnungsraster verwendet werden, sollte aber nicht als eigenständig benanntes "Framework" auftreten.

| Leser-Sprache | Redaktionelle Hürden-Kategorie (laut Auftrag) | Tragende Codex-Objekte | Abdeckungsgrad |
|---|---|---|---|
| "Ich habe noch nicht genug Informationen." | Tatsächlicher Informationsbedarf | Keines der Kapitel-4-Kernobjekte direkt — Grenzfall zu Kapitel 1 (Discovery/SPIN); P-S1-004 nennt die Discovery-Phase explizit als Bereich, in dem Informationssparsamkeit *nicht* gilt. | Schwach innerhalb Kapitel 4 — bewusst nur als Abgrenzungsfall nennen, nicht ausbauen. |
| "Ich habe zu viele Informationen/Optionen." | Informationsüberlastung / Feature Overload / Choice Overload | MEC-0015 (Pfade a/b), P-S1-004. | Stark — E5/E4-Kern, E2 für Sales-Transfer, robuste Konvergenz laut Merge-Readiness. |
| "Ich kann die Optionen nicht gut vergleichen." | Konflikt zwischen vergleichbar attraktiven, nicht-dominierten Optionen | MEC-0015 (Pfad d), ST-0310. | Mittel — E4-Einzelstudie, keine Multi-Labor-Replikation, kein direkter B2B-Test. |
| "Ich fürchte, die falsche Entscheidung zu treffen." | Unsicherheit/Risiko (antizipierte Reue) | MEC-0016 (Kernpfad); MEC-0015 Pfad c über ST-0305 für Unsicherheit über einen Weltzustand. | Gemischt — MEC-0016 E4 allgemein/E2 B2B, mit dokumentiertem Widerspruch im Objekt selbst (siehe 3.5); MEC-0015 Pfad c E4-Einzelstudien. |
| "Ich bleibe erstmal, wie es ist." | Status-quo-/Aufschublogik (nur soweit gedeckt) | Nur am Rand über die "Rückkehr zur Default-Option"-Befunde in den MEC-0015-Erweiterungen (ST-0305, ST-0310); der eigentliche Status-quo-Mechanismus liegt in MEC-0002, das nicht zu den mandatierten Kapitel-4-Kernobjekten zählt. | Schwach innerhalb Kapitel 4 — als Randnotiz/Verweis auf Kapitel 1/2 behandeln, nicht als eigener Kapitelabschnitt entwickeln. |

---

## 5. Aussagen in Leser-Sprache

Formulierungsbausteine für einen späteren Kapiteltext — Alltagssprache, keine zusammenhängende Kapitelprosa, keine überzogenen Claims.

**Gute Formulierungen (Kandidaten):**

1. "Ein Käufer, der nicht Nein sagt, aber auch nicht entscheidet, hat meist einen konkreten Grund — und der ist selten fehlendes Interesse."
2. "Mehr Optionen fühlen sich nach mehr Freiheit an, wirken auf die Entscheidung aber oft wie mehr Last."
3. "Weniger, aber passendere Information hilft mehr als eine vollständige Liste."
4. "Wenn zwei Angebote beide gute Gründe für sich haben, wird genau das zur Hürde — nicht Desinteresse."
5. "Manchmal reicht eine offene Nebenfrage, um eine Entscheidung aufzuschieben, selbst wenn die Antwort am Ende keinen Unterschied macht."
6. "Die Angst, sich falsch zu entscheiden, kann genauso bremsen wie ein echtes inhaltliches Bedenken."
7. "Eine klare, begründete Empfehlung kann Orientierung geben — sie ersetzt nicht die Entscheidung des Käufers."
8. "Reduziere unnötige Komplexität, aber verschweige keine Information, die der Käufer wirklich braucht."
9. "Wenn ein Käufer tatsächlich noch etwas wissen muss, ist die richtige Antwort mehr Information — nicht weniger."
10. "Nicht jede Zurückhaltung ist ein verstecktes Nein."

**Formulierungen, die vermieden werden sollten (Gegenbeispiele zur Kalibrierung):**

- "44 % aller verlorenen Deals scheitern an Unentschlossenheit." (unreplizierte, proprietäre Zahl — siehe Abschnitt 6)
- "Die Angst vor Fehlentscheidungen ist der Hauptgrund fürs Zögern." (unterstellt FOMU als Haupttreiber)
- "Reduziere die Optionen des Käufers, damit er schneller kauft." (Informationsentzug statt Informationsreduktion)
- "Mit dieser Technik überzeugst du jeden zögerlichen Käufer." (Universalitäts-/Garantie-Anspruch)

---

## 6. Claims, die bewusst vermieden werden sollten

- Die **44/56-JOLT-Kennzahl** nicht als Fakt oder Leitfadenclaim verwenden — proprietär, ML-Klassifizierung nicht offengelegt, keine externe Replikation (`SCIENTIFIC_DEBT.md`, B-0006).
- Kein **"JOLT beweist ..."** und keine Darstellung der vier JOLT-Techniken als geschlossen validiertes Gesamtsystem.
- Kein **"immer weniger Optionen/Information ist besser"** als Universalregel — Informationsreduktion gilt nicht bei tatsächlichem Informationsbedarf (Kategorie 1 in Abschnitt 4) und nicht in Pflichtkontexten wie RFP-Antworten (Kontextgrenze von P-S1-004).
- Kein **"FOMU ist der Haupttreiber"** der Unentschlossenheit — trotz der "sehr hoch/dominant"-Formulierung im MEC-0016-Objekt selbst (siehe 3.5, dokumentierter Widerspruch, nicht übernehmen).
- Keine **manipulative Informationsverknappung** ("Optionen verstecken, damit der Käufer schneller entscheidet").
- Keine Gleichsetzung von "Entscheidung erleichtern" mit "für den Käufer entscheiden" — eine Empfehlung darf Orientierung geben, nicht Entscheidungsfreiheit ersetzen.
- Keine unqualifizierte Übertragung der zugrundeliegenden Studierenden-Laborexperimente (Hawaii-Reise, Vorlesung-vs.-Film, Wetten/Wohnungen) auf B2B-Kaufsituationen als direkt getestete Regel.
- Kein Vermischen von MEC-0015 (Optionskomplexität) und MEC-0016 (antizipierte Reue) als denselben Mechanismus — AR-013 hat diese Trennung explizit geprüft und bestätigt.
- Keine Darstellung der 6-Feature-Regel als empirisch optimierte, direkt gemessene Zahl.
- Keine Formulierungen wie "immer", "garantiert", "bei jedem Käufer" — laut `CODEX_GUIDE_STRUCTURE.md` Abschnitt 4 repositoryweit unzulässig.

---

## 7. Evidenz- und Transfergrenzen

**Robust (E4/E5, allgemeiner Mechanismus):** Miller's Law (E5, Arbeitsgedächtnis-Kapazität) als Grundlage von MEC-0015 und P-S1-004. Paradox of Choice / Iyengar & Lepper (E4). Antizipatorische Reue und Omission Bias als allgemeiner Kern von MEC-0016 (E4, peer-reviewed, gut repliziert). Beide Tversky-&-Shafir-Studien (ST-0305, ST-0310) sind peer-reviewte Einzelstudien (E4) ohne bekannte Multi-Labor-Replikation im Codex-Bestand.

**Plausibler Transfer, nicht direkt getestet:** Die Anwendung von MEC-0015 auf Sales-Demo- und B2B-Kaufoptionskontexte (E2). Die B2B-Anwendung von MEC-0016 (E2, aus JOLT-ML-Analyse abgeleitet, nicht direkt gemessen). Die 6-Feature-Regel (T-0022) als Extrapolation von Miller's Law auf Demo-Situationen — kein Verkaufsexperiment repliziert diese Zahl direkt (`SCIENTIFIC_DEBT.md`, Zeile 97). Die Übertragung der ST-0305/ST-0310-Laborexperimente (Studierendenstichproben, Hawaii-Reise/Lern-Szenario/Wetten/Wohnungen) auf reale B2B-Kaufentscheidungen.

**Proprietär/praktikerbasiert:** Die 44/56-JOLT-Split-Zahl und die vier JOLT-Techniken als Gesamtsystem (SRC-0006, Tethr-ML, nicht offengelegte Klassifizierungsmethodik, US-COVID-Datenbasis 2020–2021). T-0022 stammt aus Gap Selling (B-0005), das laut `SCIENTIFIC_DEBT.md`/`CODEX_GUIDE_STRUCTURE.md` eine eigene Quellenvollständigkeitslücke hat (SD-SYS-002). Es ist weder Kernobjekt von Kapitel 1 noch tragender Teil von Kapitel 4.

**Bleibt Scientific Debt (aktiv, nicht aufgelöst):** ST-0151/MOD-0006 44/56-Split weiterhin unrepliziert (Priorität Mittel). MEC-0016/A-0031 externe Validierung ausstehend — AR-013 hat die Tversky-&-Shafir-Kandidatur geprüft und verneint, die Grundlücke bleibt offen (Priorität Mittel). SD-SYS-003 (Zirkelschlussrisiko bei Meta-Prinzipien wie P-S1-004: Konvergenz mehrerer Practitioner-Bücher ersetzt keine unabhängige Studie, kein Korrektiv-Mechanismus im Wissensmodell vorhanden). Die 6-Feature-Regel (T-0022/MEC-0015) bleibt eine niedrig priorisierte, aber offene Forschungsfrage.

**Einordnung von ST-0305 und ST-0310:** Beide sind Statement-Objekte, keine eigenständigen Prinzipien oder Mechanismen. Ihr Beitrag zum Kapitel läuft ausschließlich über die bereits erfolgte Integration in MEC-0015 (ST-0305 als Grundlage des Unsicherheitspfads, ST-0310 als Grundlage des Konfliktpfads, Editorentscheidung ED-AR-2 vom 2026-07-14 für ST-0310). Beide sollten im Kapiteltext daher nicht als eigenständig zitierte Primärquellen auftreten, sondern über die MEC-0015-Sprache eingeführt werden. ST-0310 trägt zusätzlich eine wichtige Abgrenzungsfunktion: Es wurde eigens gegen MEC-0016 geprüft und liefert dort **keine** Stützung — dies ist die objektseitige Grundlage für das Trennungsgebot zwischen 3.3 (Konfliktpfad) und 3.5 (FOMU) in Abschnitt 3.

---

## 8. Empfehlung für Codex

**Schreibreife:** Kapitel 4 ist laut `CODEX_GUIDE_STRUCTURE.md` als "A mit B-Elementen" eingestuft und für die vierte Position der Schreibreihenfolge vorgesehen. Diese Vorlage bestätigt diese Einschätzung differenziert: Der Informationsreduktions-Kern (MEC-0015 Pfade a/b, P-S1-004) ist A-Niveau — robust, wenig kontrovers, klar in Leser-Sprache übersetzbar. Der Unsicherheits- und Konfliktpfad (MEC-0015 Pfade c/d über ST-0305/ST-0310) ist B-Niveau — plausibel und akademisch verankert, aber auf Einzelstudien ohne B2B-Test gestützt. Der FOMU-Teil (MEC-0016) ist ebenfalls B, jedoch mit einer aktiven, ungelösten Spannung im Quellobjekt selbst (siehe unten).

**Stark genug für einen ersten Prototyp:** Die Unterabschnitte 3.1 (Rahmung), 3.2 (Informations-/Feature-Overload) und 3.6 (Empfehlungslogik als Orientierung statt Ersatz der Entscheidung) sind die solidesten Bausteine — hohe Konvergenz, geringes Kontroversrisiko, unmittelbar in Alltagssprache übersetzbar.

**Nur vorsichtig oder als Randnotiz:** 3.3 (Optionskonflikt) und 3.4 (irrelevante Unsicherheit) sollten mit explizitem Hinweis auf die zugrundeliegenden Einzelstudien und fehlenden B2B-Test geführt werden, nicht als gleich sichere Regeln wie 3.2. 3.5 (FOMU) sollte nur mit sichtbar mitgeführter Warnung erscheinen, nicht als tragende Erklärung für "die meisten" Fälle von Nicht-Entscheiden.

**Offene Entscheidungen, die Felix/Codex vor dem finalen Kapiteltext treffen müssen:**

1. **Widerspruch im MEC-0016-Objekt selbst** (Feld "Vertriebsrelevanz": "sehr hoch ... dominanter Mechanismus hinter 56 % ...") steht im Widerspruch zur Auftragsleitplanke und zur eigenen Scientific-Debt-Einstufung des Objekts. Eine Korrektur des Objekttexts liegt außerhalb dieses Blueprint-Auftrags (kein Ändern bestehender Objekte erlaubt) — die Entscheidung, ob/wie dieses Feld vor oder parallel zum Kapitel-4-Schreibsprint präzisiert wird, ist eine Reserved Decision für Felix.
2. **Publikations-Gate:** Wie in `CODEX_GUIDE_STRUCTURE.md` Abschnitt 6 festgehalten, trägt aktuell kein Wissensobjekt im Codex den Status "Validiert" — auch keines der hier tragenden sechs Objekte. Diese Vorlage bereitet nur die Struktur vor; die Wahl zwischen "Validation Gate zuerst" und "Prototyp-Gate wie V11-04" bleibt eine ausstehende, kapitelübergreifende Herausgeberentscheidung außerhalb dieses Auftrags.
3. **T-0022 als optionale Illustration:** Die Zielstruktur führt T-0022 nicht als Kernobjekt von Kapitel 1. Damit besteht keine Kapitel-Doppelnutzung, die vor dem Schreiben aufgelöst werden müsste. Wegen der Gap-Selling-Quellenlücke sollte es im Kapitel-4-Text nur erscheinen, wenn der Nutzen einer ausdrücklich als E2 markierten Demo-Illustration den zusätzlichen Ballast rechtfertigt.
4. **Kategorie "tatsächlicher Informationsbedarf" (Abschnitt 4) bleibt objektseitig dünn** — falls Felix diese Kategorie im Kapiteltext stärker ausbauen möchte, wäre ein gezielter Verweis auf Kapitel-1-Objekte (Discovery/SPIN) nötig; ein neues Kapitel-4-eigenes Objekt ist durch diesen Auftrag nicht gedeckt.

---

*Erstellt: 2026-07-15 | Redaktionelle Kapitel-Vorlage, keine Umsetzung | KI-Redaktion Sales Codex (Claude/Cowork) | Kein Commit, kein Push.*
