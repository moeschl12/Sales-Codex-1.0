# Editorial Review Sprint — MEC-0018 Dependency Chain

**Dokumentklasse:** Archived (einmaliger Sprint-Report nach Abschluss)
**Rolle bei Erstellung:** Editor (Claude), redaktionelle Konsistenzprüfung — kein Forscher, keine neue Evidenzbewertung, keine Herausgeberentscheidung
**Datum:** 2026-07-05
**Grundlage:** `00_project/KNOWLEDGE_ATLAS_CONTENT_ANALYSIS_SPRINT_1_REPORT.md`, empfohlene Hauptaktion ("Editorial Review Priority — Sichtbarkeits-Prüfung der MEC-0018-Abhängigkeitskette")
**Scope:** Ausschließlich P-0035, P-0036, P-0041, MOD-0008 im Verhältnis zu MEC-0018. Keine neue Recherche, keine Evidenzbewertungsänderung, keine neuen Wissensobjekte, keine Framework-Änderungen. Reine Konsistenzprüfung — Formulierungsvorschläge sind Vorschläge, keine Direktänderung an den Wissensobjekten.

---

## 0. Vorgehen

Für jedes der vier Objekte wurde geprüft, welche Kernaussage bei Wegfall von MEC-0018 nicht mehr bestehen würde (materielle Abhängigkeit, nicht bloße Referenz), welche Evidenzebene(n) von MEC-0018 tatsächlich übernommen werden (robuster Spreading-Activation-Kern vs. unsicherer Bargh/Dijksterhuis-Priming-Teil, siehe MEC-0018 Abschnitt „Evidenzlevel"), ob dies im Objekt bereits sichtbar ist, und ob ein bestehendes editorisches Muster (der repositoryweite „⚠ Hinweis"-Mechanismus, z. B. `## ⚠ Hinweis: Publication Bias (Kommerzielle Quelle)` in ST-0107, ST-0108, A-0019, MOD-0006 u. a.) anwendbar wäre. Kein Objekt wurde allein deshalb als risikobehaftet eingestuft, weil es MEC-0018 in seiner Objektliste nennt.

**Referenzmuster (bereits etabliert, hier nur zitiert, nicht verändert):**

```
## ⚠ Hinweis: Publication Bias (Kommerzielle Quelle)

Dieses Objekt beruht (mit) auf der proprietaeren CEB-Befragungsstudie [...].
Siehe `SCIENTIFIC_DEBT.md`, SD-SYS-001 [...] fuer die vollstaendige Einordnung.
**[Ergaenzt DATUM, SPRINTNAME]**
```

MEC-0018 selbst nutzt bereits eine inhaltlich gleichwertige, aber inline (nicht als eigene Überschrift) formulierte Variante für die Kategorie „Replikationsrisiko" im Abschnitt „Vertriebsrelevanz".

---

## 1. P-0035 — Rahmen zuerst: Den psychologischen Kontext vor der Botschaft etablieren

**Abhängigkeit (Frage 1):** Vollständig und unmittelbar. Die Kernformulierung ("stelle sicher, dass der psychologische Rahmen ... zur Botschaft passt") ist die direkte praktische Übersetzung des MEC-0018-Wirkungspfads (Opener → Assoziations-Aktivierung → Privileged Moment). Ohne MEC-0018 hätte P-0035 keine mechanistische Grundlage — es gibt keine zweite, unabhängige Quelle für diese Aussage im Objekt.

**Evidenzübernahme (Frage 2):** Beide Ebenen, explizit unterschieden — bereits im Objekt selbst. Die Evidenzklassifikation zitiert wörtlich die MEC-0018-Differenzierung: E4 für Spreading Activation, E2 für die Bargh/Dijksterhuis-Priming-Studien mit Replikationsvorbehalt, E2 für die Sales-Anwendung, Gesamteinstufung E3.

**Bestehende Transparenz (Frage 3):** Hoch, aber nur im Fließtext der Evidenzklassifikation, nicht als eigenständige, scannbare Überschrift. Ein Leser, der die Evidenzklassifikations-Zeile vollständig liest, erkennt die Differenzierung korrekt. Ein Leser, der nur Formulierung/Begründung überfliegt (die beiden Abschnitte vor der Evidenzklassifikation), stößt nicht auf einen Hinweis.

**Risiko:** Real, aber bereits korrekt benannt — kein neues Risiko, nur eine Sichtbarkeitsfrage.

**Empfehlung:** **B (kleine redaktionelle Ergänzung sinnvoll)** — keine neue Bewertung, sondern eine zusätzliche, kurze `## ⚠`-Überschrift, die den bereits vorhandenen Inhalt der Evidenzklassifikation an die im Repository etablierte, besser scannbare Stelle hebt (siehe Formulierungsvorschlag, Abschnitt 5).

---

## 2. P-0036 — Aufmerksamkeit strategisch lenken

**Abhängigkeit (Frage 1):** Gering, trotz Nennung von MEC-0018 in „Verknüpfte Objekte". Die Kernaussage ("Fokussiertes erscheint wichtiger und kausaler") stützt sich im Objekt selbst auf ST-0176 (Attention-Importance-Heuristik) und ST-0177 (Focal-Causal-Effekt) — beide E4, beide explizit auf Agenda-Setting-Forschung (Politik-/Medienpsychologie) bzw. Lassiter et al. Videoverhör-Studien gestützt, **nicht** auf die Bargh/Dijksterhuis-Priming-Literatur, die MEC-0018s Risiko trägt. Auch wenn MEC-0018 (bzw. dessen "Attention-Importance-Heuristik"-Schritt) vollständig entfiele, bliebe P-0036s Kernaussage durch ST-0176/ST-0177 unverändert bestehen. MEC-0018 liefert hier den zeitlichen Rahmen ("wann wird diese Heuristik genutzt"), nicht die Evidenzbasis des Effekts selbst.

**Evidenzübernahme (Frage 2):** Ausschließlich der robuste Layer. Es gibt keine Übernahme des unsicheren Bargh/Dijksterhuis-Priming-Teils.

**Bestehende Transparenz (Frage 3):** Ausreichend — die Evidenzklassifikation (E4, peer-reviewed) ist korrekt und referenziert keine Priming-Studien mit Replikationsvorbehalt.

**Risiko:** Keine materielle Abhängigkeit vom unsicheren Teil von MEC-0018 identifiziert.

**Empfehlung:** **A (keine Änderung notwendig).** Ein Warnhinweis wäre hier sachlich falsch platziert — er würde eine Unsicherheit suggerieren, die die tatsächliche Evidenzbasis von P-0036 (Agenda-Setting/Attribution, nicht Bargh/Dijksterhuis-Priming) nicht hat. Genau die im Auftrag benannte Falle ("Warnhinweis allein wegen Referenz auf MEC-0018") würde hier zuschlagen, wenn nicht differenziert geprüft würde.

---

## 3. P-0041 — System-1-kompatible Darstellung

**Abhängigkeit (Frage 1):** Gering. Die Kernaussage (Kaufentscheidungen sind primär System-1-getrieben, Kommunikation sollte entsprechend gestaltet sein) stützt sich im Objekt auf ST-0194, ST-0196, ST-0197 und A-0047 — alle aus SRC-0010 (Kahneman, *Thinking, Fast and Slow*) und auf MEC-0012 (Dual-Process), nicht auf MEC-0018. MEC-0018 erscheint in „Verknüpfte Objekte" nur mit dem Zusatz "zeitliche Dimension von S1-Vorbereitung" — ein sekundärer, ergänzender Bezug, kein tragender. Ohne MEC-0018 bliebe die gesamte Kernaussage von P-0041 (System-1-Dominanz, Cognitive Ease, WYSIATI, Dual-Coding) unverändert bestehen, da sie ausschließlich aus dem Kahneman-Strang abgeleitet ist.

**Evidenzübernahme (Frage 2):** Keine Übernahme der unsicheren Ebene. Die zugrundeliegenden Statements (System 1/2, Cognitive Ease, WYSIATI) sind Teil des sehr gut replizierten Kahneman-Dual-Process-Kernbestands (E4/E5) und explizit nicht Teil der in `SCIENTIFIC_DEBT.md` B-0010 dokumentierten Bargh/Dijksterhuis-Priming-Kontroverse (die betrifft spezifisch Kap. 4 der Priming-Forschung, nicht die Dual-Process-Architektur selbst).

**Bestehende Transparenz (Frage 3):** Ausreichend — Evidenzklassifikation E4 ist korrekt und unabhängig von MEC-0018 begründet.

**Risiko:** Keine materielle Abhängigkeit vom unsicheren Teil von MEC-0018.

**Empfehlung:** **A (keine Änderung notwendig).** Aus denselben Gründen wie bei P-0036: Die Verlinkung zu MEC-0018 ist real, aber nicht evidenztragend. Ein Warnhinweis würde die falsche Aussage treffen (dass P-0041s Kernthese von der unsicheren Priming-Forschung abhinge, was nicht der Fall ist).

---

## 4. MOD-0008 — Pre-Suasion-Modell: Zeitliche Struktur der Überzeugung

**Abhängigkeit (Frage 1):** Teilweise, aber strukturell zentral für zwei von vier Phasen. Das Modell hat vier Phasen: Phase 1 (Opener) und Phase 2 (Privileged Moment) SIND MEC-0018 — sie würden ohne MEC-0018 vollständig entfallen, nicht nur abgeschwächt werden. Phase 3 (Kernbotschaft) stützt sich auf MOD-0002 (Cialdini 6+1-Prinzipien, separat evidenziert). Phase 4 (Commitment-Lock) stützt sich auf MEC-0006 (Konsistenz/Commitment, separat evidenziert, E4). Das Modell als Ganzes (die Idee einer zeitlichen Sequenz-Struktur der Überzeugung) würde ohne MEC-0018 auf zwei von vier Phasen verlieren — es bliebe kein vollständiges Sequenzmodell mehr, auch wenn Phase 3/4 für sich genommen bestehen blieben.

**Evidenzübernahme (Frage 2):** Beide Ebenen, bereits explizit unterschieden im Objekt selbst — die Evidenzlevel-Sektion von MOD-0008 zitiert wortgleich dieselbe Differenzierung wie P-0035 (Spreading Activation E4, Bargh/Dijksterhuis-Priming E2 mit Replikationsvorbehalt, Verweis auf `SCIENTIFIC_DEBT.md` B-0010 Priorität Hoch, Gesamtmodell E3).

**Bestehende Transparenz (Frage 3):** Wie bei P-0035 — inhaltlich korrekt und vollständig, aber nur im Fließtext der Evidenzlevel-Sektion, nicht in einer eigenen scannbaren Überschrift. Zusätzlich fehlt im Modell-Schema selbst (der ASCII-Grafik und der Phasenbeschreibung) jeder Hinweis darauf, dass Phase 1/2 einerseits und Phase 3/4 andererseits unterschiedliche Evidenzrisiken tragen — ein Leser, der nur das Schema und die Phasenbeschreibung liest (nicht bis zur Evidenzlevel-Sektion vorstößt), sieht vier gleichwertig dargestellte Phasen ohne Risikodifferenzierung.

**Risiko:** Real und am stärksten unter den vier geprüften Objekten, weil hier zusätzlich zur reinen Evidenzklassifikation auch die visuelle Modell-Darstellung (Schema) alle vier Phasen ununterschieden gleich behandelt.

**Empfehlung:** **B (kleine redaktionelle Ergänzung sinnvoll)** — analog zu P-0035, plus optional ein kurzer Klammerzusatz direkt in der Phasenbeschreibung (Phase 1/2), der auf die Evidenzlevel-Sektion verweist, ohne das Schema selbst zu verändern.

---

## 5. Formulierungsvorschläge (nur für P-0035 und MOD-0008)

Beide Vorschläge verwenden ausschließlich das bereits im Repository etablierte `## ⚠ Hinweis`-Muster (siehe Abschnitt 0) und fügen keine neue Bewertung, keine neue Kategorie und keine neue Formatierungskonvention hinzu. Platzierung: unmittelbar vor `## Status`, wie beim bestehenden Publication-Bias-Muster.

### Vorschlag für P-0035 (neue Sektion, vor „## Status" einzufügen)

```markdown
## ⚠ Hinweis: Replikationsrisiko (geerbt von MEC-0018)

Dieses Prinzip ist die direkte praktische Ableitung von MEC-0018 (Pre-Suasion) und
besteht ohne diesen Mechanismus nicht eigenständig. Ein Teil der zugrundeliegenden
Priming-Forschung (Bargh-/Dijksterhuis-Stil) trägt ein dokumentiertes
Replikationsrisiko (`SCIENTIFIC_DEBT.md`, Sektion B-0010, Priorität Hoch); die
Basis-Assoziationsaktivierung (Spreading Activation, Collins & Loftus 1975) gilt
dagegen als robust repliziert. Vollständige Differenzierung: MEC-0018, Abschnitt
„Evidenzlevel". Keine neue Bewertung — dieser Hinweis macht die bereits in der
Evidenzklassifikation oben stehende Einordnung zusätzlich sichtbar.
**[Vorschlag, Editorial Review Sprint MEC-0018, 2026-07-05 — durch Herausgeber zu bestätigen]**
```

### Vorschlag für MOD-0008 (neue Sektion, vor „## Status" einzufügen)

```markdown
## ⚠ Hinweis: Replikationsrisiko (Phase 1–2, geerbt von MEC-0018)

Phase 1 (Opener) und Phase 2 (Privileged Moment) dieses Modells sind identisch mit
MEC-0018 und teilen dessen dokumentiertes Replikationsrisiko: Ein Teil der
zugrundeliegenden Priming-Forschung (Bargh-/Dijksterhuis-Stil) gilt als in der
Replikationskrise nicht bestätigt (`SCIENTIFIC_DEBT.md`, Sektion B-0010, Priorität
Hoch), während die Basis-Assoziationsaktivierung (Spreading Activation) robust
repliziert ist. Phase 3 (MOD-0002) und Phase 4 (MEC-0006) sind davon unabhängig
und tragen dieses Risiko nicht. Vollständige Differenzierung: MEC-0018, Abschnitt
„Evidenzlevel". Keine neue Bewertung.
**[Vorschlag, Editorial Review Sprint MEC-0018, 2026-07-05 — durch Herausgeber zu bestätigen]**
```

Beide Vorschläge wurden **nicht** in die Objektdateien eingetragen — dieser Sprint ist diagnostisch, keine Umsetzung. Die Übernahme ist eine editorische Entscheidung des Herausgebers.

---

## 6. Zusammenfassung

| Objekt | Materielle Abhängigkeit von MEC-0018 | Übernommene Evidenzebene | Bereits ausreichend sichtbar? | Empfehlung |
|---|---|---|---|---|
| P-0035 | Vollständig | Beide (robust + unsicher), bereits im Objekt differenziert | Inhaltlich ja, aber nur im Fließtext, nicht als eigene Überschrift | **B** |
| P-0036 | Gering (eigene, unabhängige Evidenzbasis: Agenda-Setting/Attribution) | Nur robuster Layer | Ja | **A** |
| P-0041 | Gering (eigene, unabhängige Evidenzbasis: Kahneman Dual-Process) | Nur robuster Layer | Ja | **A** |
| MOD-0008 | Teilweise (2 von 4 Phasen vollständig, 2 von 4 Phasen unabhängig) | Beide, bereits im Objekt differenziert, aber im Modell-Schema nicht sichtbar | Nur in der Evidenzlevel-Sektion, nicht im Schema selbst | **B** |

**Gesamtergebnis: Empfehlung B, aber eng begrenzt** — nur 2 von 4 geprüften Objekten (P-0035, MOD-0008) benötigen eine Ergänzung, und diese Ergänzung ist ausschließlich eine Sichtbarkeits-/Formatierungsmaßnahme (bereits vorhandener Inhalt wird in das etablierte `⚠`-Muster gehoben), keine neue inhaltliche Bewertung. P-0036 und P-0041 benötigen ausdrücklich **keine** Änderung — beide referenzieren MEC-0018, tragen aber nachweislich nicht dessen Evidenzrisiko, weil ihre Kernaussagen auf eigenständigen, robusten Literatursträngen beruhen. Dies bestätigt die im Sprintauftrag geforderte Vorsicht: bloße Referenz auf MEC-0018 rechtfertigt keinen automatischen Warnhinweis.

---

## 7. Empfohlene nächste Hauptaktion

**Genau eine:** Der Herausgeber prüft die beiden in Abschnitt 5 vorgeschlagenen `## ⚠ Hinweis`-Ergänzungen für P-0035 und MOD-0008 und entscheidet über deren Übernahme (unverändert, angepasst oder abgelehnt). Bei Freigabe ist die Umsetzung ein reiner T3-Wartungsschritt (punktuelle Ergänzung einer bereits im Repository etablierten Formatierungskonvention, keine neue Recherche, keine E-Level-Änderung) und kann in einem eigenen, sehr kurzen Folgeauftrag ausgeführt werden. Keine weitere Analyse ist für diese Abhängigkeitskette erforderlich.

---

*Dieser Report ist ein generierter Analyse-Output eines diagnostischen Editorial-Review-Sprints, kein Wissensobjekt und keine Framework-Datei. Er ändert keine Evidenzbewertung und trifft keine Herausgeberentscheidung — die vorgeschlagenen Formulierungen in Abschnitt 5 sind Vorschläge zur Bestätigung, keine vollzogenen Änderungen.*
