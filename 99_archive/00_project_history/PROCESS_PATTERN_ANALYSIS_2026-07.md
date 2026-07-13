# Process Pattern Analysis — Wiederkehrende Arbeitsmuster im Sales Codex

**Dokumentklasse:** Analyse / Reference
**Rolle:** Claude / Cowork, im Auftrag des Herausgebers — Analyse der Arbeitsmethodik, nicht der Inhalte
**Datum:** 2026-07-04
**Status:** Vorschlag zur Herausgeber-Prüfung — keine Skills implementiert, keine Repository-Änderungen
**Geltungsbereich dieses Dokuments:** Ausschließlich Prozesswissen (wie gearbeitet wird), nicht Fachwissen (was der Sales Codex inhaltlich aussagt)

---

## 1. Zweck und Methodik

Dieses Dokument analysiert die gesamte bisherige Entwicklung des Sales Codex — Framework, Repository-Aufbau, Research Program, Evidence System, Canonical Knowledge Model, Knowledge Atlas, Reviews, Releases und Architekturentscheidungen — mit dem Ziel, **wiederkehrende, standardisierbare Arbeitsmuster** zu identifizieren. Diese Muster sind Kandidaten für eine kleine Bibliothek wiederverwendbarer Workflows ("Skills"), die die Arbeitsmethodik des Projekts — nicht seine Inhalte — dauerhaft verbessern und auch für Sales Codex 2.0 oder gänzlich andere Wissensprojekte tragfähig wären.

**Ausdrücklich kein Gegenstand dieses Dokuments:** die inhaltliche Substanz des Sales Codex (Prinzipien, Mechanismen, Techniken etc.). Jeder vorgeschlagene Skill ist so formuliert, dass er ohne Bezug auf Vertriebswissen funktioniert.

**Ausgewertete Primärquellen** (vollständig gelesen, nicht aus Trainingswissen ergänzt):

- `00_project/SALES_CODEX_OPERATING_MANUAL.md`, `CLAUDE_BOOTSTRAP.md`, `PROJECT_BOOTSTRAP.md`, `task_rules.md`, `changelog.md`, `review_queue.md`, `OPEN_DECISIONS.md`, `CODEX_AUDIT_2026-07.md`
- `01_framework/05_knowledge_model/canonical_knowledge_model.md`, `01_framework/02_evidence_system/evidence_system.md`, `01_framework/04_principle_extraction/principle_extraction_standard.md`, `01_framework/07_agent_protocols/master_agent_protocol.md`
- `06_research_program/RESEARCH_LIFECYCLE.md`, `RESEARCH_GOVERNANCE.md`, `DECISION_POLICY.md`
- `08_knowledge_atlas/ATLAS_MANIFEST.md`, `08_knowledge_atlas/output/atlas_compiler_report.md`
- Repository-Struktur (vollständiger Verzeichnisbaum), Übersicht aller Dateien in `00_project/`, `01_framework/`, `06_research_program/`, `08_knowledge_atlas/`

**Nicht einzeln vollständig gelesen** (aus Changelog-Einträgen und Querverweisen rekonstruiert, nicht als Primärquelle zitiert): die vollständigen Volltexte von `ACADEMIC_RECOVERY_REPORT*.md`, `POST_MORTEM_*.md`, `REPOSITORY_CONSOLIDATION_REPORT_RC1.md`, `RC1_FREEZE_*.md`, `FINAL_RC1_AUDIT_VALIDATION_REPORT.md`. Wo diese Dokumente unten referenziert werden, stützt sich die Aussage auf die entsprechenden Changelog-Zusammenfassungen — als Unsicherheit hier explizit markiert (⚠).

---

## 2. Übersicht der identifizierten Muster

| # | Muster | Wiederholungen (Beleg) | Vorschlag |
|---|---|---|---|
| 1 | Session-Kontinuitätsprotokoll | Jede einzelne Session seit v1.1 | Skill, Tier 1 |
| 2 | Wissens-Extraktions-Pipeline-Orchestrator | 10 Buchanalysen (B-0001–B-0010) | Skill, Tier 1 |
| 3 | Konsistenz-Selbstreview (VAL-Report) | 10 VAL-Reports, ein Health Check | Skill, Tier 1 |
| 4 | Externe-Kritik-Verarbeitung | ≥6 Vorkommen (s. Abschnitt 3.4) | Skill, Tier 1 |
| 5 | Canonicalisierungs-Assistent | Bei jeder Objektanlage (>500 Objekte) | Skill, Tier 2 |
| 6 | Repository-Tiefenaudit | 2 Vorkommen (CODEX_AUDIT, Reifegradbericht) | Skill, Tier 2 |
| 7 | Governance-Register-Pflege | OPEN_DECISIONS.md, SCIENTIFIC_DEBT.md, laufend | Skill, Tier 2 |
| 8 | Postmortem-/Retrospektiven-Generator | ≥2 Vorkommen (B-0002, W-001 Health Check) | Skill, Tier 2 |
| 9 | Forschungsprogramm-Stufen-Orchestrator | 1 vollständiger Durchlauf (W-001), Framework fertig | Skill, Tier 3 |
| 10 | Repository-Konsolidierung | 2 Vorkommen (Sprint 1, Sprint 2) | Skill, Tier 3 |
| 11 | Release-Freeze-/Versionierungsprotokoll | 3 Vorkommen (v1.0-Infra-Freeze, v1.1, RC-1) | Skill, Tier 3 |
| 12 | Graph-/Referenz-Integritätsprüfung | 1 Vorkommen, bereits als Skript existent | Nicht als Skill, Tier 4 |
| 13 | Herausgeber-Entscheidung / Framework-Änderung | Durchgehend | Nicht als Skill, Tier 4 |

---

## 3. Detailbeschreibung je Muster

### 3.1 Session-Kontinuitätsprotokoll ("Stateless Handoff")

**Zweck:** Sicherstellen, dass jede neue Arbeitssitzung — unabhängig davon, welches KI-System oder welche Session sie ausführt — exakt auf dem tatsächlichen Repository-Zustand aufsetzt, nicht auf einer Erinnerung an den Chatverlauf.

**Welches Problem der Skill löst:** Chatverläufe enden, Sessions werden neu gestartet, verschiedene KI-Systeme wechseln sich ab. Ohne ein explizites Protokoll müsste jede Session entweder den gesamten Chatverlauf kennen (nicht garantiert) oder das gesamte Repository neu durchsuchen (ineffizient und fehleranfällig). Das Projekt hat dieses Problem bereits 2026-06-30 mit der "Stateless Agent Architecture" gelöst (`PROJECT_BOOTSTRAP.md`, `CURRENT_STATE.md`, `00_project/NEXT_ACTION.md`, `00_project/SESSION_LOG.md`) — aber als Dokumentenkonvention, nicht als aktiv erzwungenes Skill-Verhalten.

**Wann Claude ihn automatisch verwenden sollte:** Bei jedem Sitzungsbeginn in einem Projekt, das dieses Muster nutzt (Auslöser: Vorhandensein von `CURRENT_STATE.md`/`NEXT_ACTION.md` oder gleichwertigen Dateien im Root); am Ende jeder Sitzung, bevor eine Konversation als abgeschlossen gilt.

**Typische Ein-/Ausgaben:**
- Eingabe: aktuelles Repository (insbesondere `CURRENT_STATE.md`, `NEXT_ACTION.md`, `SESSION_LOG.md` oder Projekt-Äquivalente), keine Chat-Historie als Quelle.
- Ausgabe: aktualisierte Statusdateien (Task-Status, nächste freie IDs/Referenzen, ein Log-Eintrag mit Datum, was getan wurde, was sich geändert hat, exakt eine nächste Handlung).

**Standardisierter Workflow:**
1. Session-Start: Pflichtlektüre in fester Reihenfolge (Bootstrap-Dokument → Zustandsdokument → nächste Aktion → nur die tatsächlich betroffenen Arbeitsdateien).
2. Arbeit ausführen.
3. Session-Ende: Zustandsdokument aktualisieren, nächste Aktion auf genau einen konkreten Schritt setzen, Log-Eintrag ergänzen.
4. Keine Session gilt als abgeschlossen, ohne dass Schritt 3 durchgeführt wurde.

**Qualitätskriterien:** Nächste Aktion ist immer genau eine, nie eine Liste (`00_project/NEXT_ACTION.md`-Konvention); Log-Einträge sind chronologisch und nennen konkret geänderte Dateien; das Zustandsdokument widerspricht nie dem tatsächlichen Dateisystem-Zustand (Stichprobe: nächste freie ID stimmt mit tatsächlich höchster vergebener ID überein).

**Typische Fehlerquellen:** Vergessenes Update am Sitzungsende (häufigster Fehler in stateless Architekturen allgemein); Zustandsdokument beschreibt einen Zwischenstand, der nie erreicht wurde (Über-Optimismus); mehrere "nächste Aktionen" statt einer, was Priorisierung an nachfolgende Sessions delegiert statt sie zu treffen.

**Abbruchbedingungen:** Zustandsdokument und tatsächlicher Repository-Zustand widersprechen sich eklatant (z. B. genannte Datei existiert nicht) → Diskrepanz dem Nutzer melden statt stillschweigend zu überschreiben.

**Nicht-Ziele:** Der Skill ersetzt kein Versionskontrollsystem (Git bleibt die Historie); er ersetzt keine inhaltliche Entscheidungsfindung; er erzwingt keine bestimmte Aufgabenpriorisierung, sondern nur die *Dokumentation* der gewählten Priorität.

**Erwarteter langfristiger Nutzen:** Größter Hebel des gesamten Projekts, weil er jede andere Arbeit erst zuverlässig fortsetzbar macht. Vollständig domänenunabhängig — identisch anwendbar in Sales Codex 2.0, einem Software-Repository oder einem völlig anderen Wissensprojekt.

---

### 3.2 Wissens-Extraktions-Pipeline-Orchestrator ("Book Mode" / Task-Generierung)

**Zweck:** Aus einer Primärquelle deterministisch und vollständig eine feste Sequenz von Verarbeitungsschritten ableiten, vorschlagen und (nach Freigabe) ohne Zwischenstopps ausführen.

**Welches Problem der Skill löst:** Ohne einen solchen Orchestrator müsste der Herausgeber für jede neue Quelle jeden einzelnen Arbeitsschritt manuell beauftragen. `00_project/task_rules.md` beschreibt genau dieses Problem und löst es projektspezifisch: Status im Katalog auf "bereit" setzen genügt, der Rest wird deterministisch abgeleitet (Abschnitt 4–5). Das allgemeine Muster dahinter — *fester Objekt-Pipeline mit Statuslogik, Vorschlag-vor-Ausführung, definierten Abbruchbedingungen* — ist unabhängig vom Sales Codex.

**Wann Claude ihn automatisch verwenden sollte:** Wenn ein Projekt eine definierte, mehrstufige Verarbeitungssequenz für wiederkehrende Eingabeeinheiten hat (hier: Bücher/Quellen) und ein Katalog/Statusfeld anzeigt, welche Einheit als nächstes bearbeitet werden soll.

**Typische Ein-/Ausgaben:**
- Eingabe: Katalogdatei mit Statuswerten, aktueller Repository-Zustand (welche Verarbeitungsstufen bereits vorliegen), Templates je Stufe.
- Ausgabe: eine Vorschlagsdatei mit vollständiger, abhängigkeitsgeordneter Aufgabenliste (nie direkte Ausführung ohne Freigabe); nach Freigabe: die tatsächlichen Objekte/Dateien jeder Stufe plus Abschlussbericht.

**Standardisierter Workflow (generisch, abgeleitet aus `task_rules.md` Abschnitt 5, 8, 10):**
1. Aktivierungsregel: genau eine Eingabeeinheit mit "bereit"-Status wählen (bei mehreren: definierte Tie-Breaker-Regel, hier niedrigste ID).
2. Repository-Zustand gegen jede Pipeline-Stufe prüfen (vorhanden/fehlt/unvollständig).
3. Deterministische Ableitungsmatrix anwenden: erste fehlende/unvollständige Stufe bestimmt den nächsten Task; spätere Stufen werden nicht vorgeschlagen, bevor Abhängigkeiten erfüllt sind.
4. Vorschlagsdatei erzeugen (Kontext, Zustand, Aufgabenliste, Abbruchbedingungen) — keine Ausführung.
5. Nach expliziter Freigabe: vollständige Sequenz ohne Zwischenfreigaben durchlaufen ("Modus ohne Pausen"), außer bei definierten Stopp-Bedingungen.
6. Abschluss: Standardausgabe (erzeugte Objekte, Kernerkenntnisse, offene Fragen, Empfehlung für nächsten Schritt) plus Session-Kontinuitätsprotokoll (3.1).

**Qualitätskriterien:** Jede Stufe referenziert das für sie vorgesehene Template; kein Task wird vorgeschlagen, dessen Abhängigkeit nicht erfüllt ist; die Vorschlagsdatei enthält keine inhaltlichen Urteile, keine Framework-Änderungsvorschläge.

**Typische Fehlerquellen:** Stille Annahme von Vollständigkeit einer Stufe ohne tatsächliche Prüfung (z. B. Kapitelstruktur-Tabelle existiert, ist aber nicht vollständig ausgefüllt — `task_rules.md` Abschnitt 5.4 adressiert dies explizit); mehrere gleichzeitige, konkurrierende Vorschläge (Abschnitt 8.5 verbietet dies ausdrücklich); Aktivierung trotz bereits laufender Bearbeitung.

**Abbruchbedingungen:** Kein Eingabeobjekt im aktivierenden Status vorhanden; nicht freigegebener Vorschlag existiert bereits; erforderliche Rohdaten (hier: Primärtext) nicht zugänglich; ein abgeleiteter Task würde eine Framework-Änderung voraussetzen.

**Nicht-Ziele:** Trifft keine Evidenz- oder Qualitätsurteile über den Inhalt; erzeugt keine neuen Template-Kategorien; führt keine Versionskontroll-Operationen aus; ersetzt keine Herausgeber-Freigabe.

**Erwarteter langfristiger Nutzen:** Macht den arbeitsintensivsten, am häufigsten wiederholten Prozess des Projekts (zehnmal identisch durchlaufen) reproduzierbar und prüfbar. In Sales Codex 2.0 oder einem Nachfolgeprojekt unmittelbar wiederverwendbar für jede Domäne mit definierter Mehrstufen-Pipeline (nicht nur Bücher).

---

### 3.3 Konsistenz-Selbstreview (VAL-Report-Generator)

**Zweck:** Nach Abschluss einer Arbeitseinheit eine strukturierte technische Selbstprüfung durchführen, die Fehler vor der Herausgeber-Freigabe abfängt.

**Welches Problem der Skill löst:** Fehler wie fehlende Felder, falsche ID-Referenzen oder inkonsistente Terminologie häufen sich unbemerkt an, wenn kein fester Prüfschritt existiert. Das Operating Manual (Schritt 8, Abschnitt 6 "Stufe 1 — Technischer Review") und die Research-Program-Templates (`MASTER_REVIEW_TEMPLATE.md`, `HEALTH_CHECK_TEMPLATE.md`) definieren dieses Muster bereits zweimal unabhängig — einmal für Buchanalysen (VAL), einmal für Forschungsprojekte (Health Check, Abschnitt 12 in `RESEARCH_LIFECYCLE.md`).

**Wann Claude ihn automatisch verwenden sollte:** Direkt nach Abschluss jeder in sich geschlossenen Arbeitseinheit (Buchanalyse, Forschungsprojekt, Sprint), bevor ein Abschlussbericht oder eine Freigabe-Anfrage formuliert wird.

**Typische Ein-/Ausgaben:**
- Eingabe: alle in dieser Arbeitseinheit erzeugten/geänderten Objekte, die dazugehörigen Templates, referenzierte IDs.
- Ausgabe: ein Prüfbericht mit fester Struktur (behobene Befunde / offene Befunde / keine Befunde), niemals eine stillschweigende Korrektur ohne Protokolleintrag.

**Standardisierter Workflow (abgeleitet aus Operating Manual Abschnitt 6 und 9.4, `RESEARCH_LIFECYCLE.md` Abschnitt 12.3):**
1. Feste Prüfkriterien-Liste anwenden (z. B.: existieren alle referenzierten IDs als Dateien; sind Pflichtfelder vollständig; ist Terminologie/Formatierung templatekonform; sind Unsicherheiten markiert; stimmen abhängige Felder zwischen verknüpften Objekten überein).
2. Jeden Prüfpunkt einzeln als erfüllt / nicht erfüllt / nicht anwendbar bewerten — keine Pauschalaussage "alles in Ordnung".
3. Befunde nach Schweregrad in "behoben" (in dieser Sitzung korrigiert) und "offen" (dokumentiert, nicht korrigiert) trennen.
4. Bericht nach festem Template ablegen, niemals im Chat "verloren gehen" lassen.

**Qualitätskriterien:** Jeder Prüfpunkt ist einzeln begründet, nicht pauschal (dieselbe Anforderung wie in `RESEARCH_LIFECYCLE.md`, Stufe 4, an die Peer Review gestellt); ein negativer Befund wird nicht deshalb vermieden, weil die vorausgehende Arbeit bereits umfangreich war.

**Typische Fehlerquellen:** Der reale Befund aus `CODEX_AUDIT_2026-07.md` (Abschnitt 3, "Neubefund dieses Audits") zeigt die konkrete Fehlerklasse: frühere Reviews konzentrierten sich auf eine Objektebene (Mechanismen) und prüften nachgelagerte Ebenen (Prinzipien, Techniken) nicht mit derselben Sorgfalt mit — Selbstreviews neigen dazu, dort gründlich zu sein, wo zuletzt gearbeitet wurde, und oberflächlich dort, wo nur mitgeführt wird.

**Abbruchbedingungen:** Eine referenzierte ID existiert nicht und lässt sich nicht klären → Arbeitseinheit gilt als nicht abschlussbereit, kein Bericht mit Gesamturteil "bestanden".

**Nicht-Ziele:** Ersetzt keine externe/wissenschaftliche Validierung (das ist eine andere Prüfstufe); trifft keine Evidenzklassen-Entscheidungen aus eigener Autorität, wenn dafür laut Governance eine höhere Freigabestufe nötig ist.

**Erwarteter langfristiger Nutzen:** Reduziert die Rate unentdeckter Inkonsistenzen, die sonst erst bei einem seltenen Tiefenaudit (3.6) auffallen — verschiebt Fehlerentdeckung von "einmal pro Quartal, teuer" zu "nach jeder Einheit, günstig".

---

### 3.4 Externe-Kritik-Verarbeitung (Review-Decision-Processing)

**Zweck:** Eine Liste externer Kritikpunkte (Gutachten, Audit, Peer Review) systematisch, punktweise und nachvollziehbar in Annahme-/Teilannahme-/Ablehnungsentscheidungen überführen — ohne unbequeme Punkte stillschweigend zu übergehen und ohne unkritisch jede Kritik zu übernehmen.

**Welches Problem der Skill löst:** Externe Kritik wird häufig entweder komplett übernommen (Verlust eigener Standards) oder komplett ignoriert (Verlust an Selbstkorrektur). Dieses Projekt hat das Muster mindestens sechsmal unabhängig wiederholt: `99_archive/00_project_history/peer_review/decisions/PEER_REVIEW_DECISION_REPORT_SPRINT_001.md`, `PEER_REVIEW_DECISION_REPORT_SPRINT_002.md`, `BEHAVIORAL_SCIENCE_REVIEW_DECISION_REPORT_2026-07.md`, `OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`, ⚠ `FINAL_RC1_AUDIT_VALIDATION_REPORT.md` (19 Einzelkritikpunkte dreier Gutachten, laut Changelog-Eintrag 2026-07-04 — Volltext nicht gelesen), und implizit in `DECISION_POLICY.md` als formales Regelwerk für genau diesen Vorgang.

**Wann Claude ihn automatisch verwenden sollte:** Immer, wenn ein externes Dokument (Gutachten, Audit, Reviewer-Kommentar) eine Liste von Empfehlungen oder Kritikpunkten enthält, die gegen den tatsächlichen Projektzustand bewertet werden sollen.

**Typische Ein-/Ausgaben:**
- Eingabe: das externe Dokument (Kritikliste), der tatsächliche aktuelle Projektzustand (nicht die Erinnerung daran).
- Ausgabe: ein Entscheidungsbericht mit einer Zeile pro Kritikpunkt: Bewertung (Übernehmen / Teilweise übernehmen / Ablehnen / bereits erfüllt / nicht reproduzierbar), Begründung mit Bezug auf konkrete Repository-Stellen, betroffene Dateien, ggf. durchgeführte Korrektur.

**Standardisierter Workflow (abgeleitet aus `DECISION_POLICY.md` Abschnitt 2–4 und den o. g. Decision Reports):**
1. Jeden Kritikpunkt einzeln extrahieren (keine Sammelbewertung).
2. Für jeden Punkt den *tatsächlichen* Zustand prüfen, bevor bewertet wird — die Behauptung "Feld X fehlt" muss am echten Objekt verifiziert werden, nicht angenommen werden (siehe `CODEX_CONSISTENCY_CORRECTION_REPORT_2026-07.md`-Eintrag im Changelog: "Audit-Falschbefund richtiggestellt").
3. Bewertung in eine der festen Kategorien einordnen; "bereits erfüllt, Reviewer-Behauptung trifft nicht zu" ist ein zulässiges, eigenständig zu dokumentierendes Ergebnis (kein automatisches "Übernehmen").
4. Bei "Teilweise übernehmen": exakt benennen, welcher Teil warum übernommen wird und welcher nicht.
5. Kritikpunkte, die eine Framework-Änderung voraussetzen würden, werden nicht im selben Schritt entschieden, sondern als eigene Herausgeber-Entscheidung ausgelagert (siehe `DECISION_POLICY.md` Abschnitt 6, `review_queue.md`-Eintrag ED-008 "Ablehnen … Framework-Änderung außerhalb des Sprintumfangs").
6. Widersprüche zwischen zwei externen Gutachten werden dokumentiert, nicht durch Mittelwertbildung aufgelöst.

**Qualitätskriterien:** Jede Bewertung nennt eine konkrete Repository-Referenz, nicht nur eine Meinung; die Anzahl bewerteter Punkte entspricht exakt der Anzahl eingegangener Kritikpunkte (keine stille Auslassung); eine Ablehnung ist genauso ausführlich begründet wie eine Annahme.

**Typische Fehlerquellen:** Kritikpunkte werden thematisch gebündelt und pauschal beantwortet, wodurch einzelne berechtigte Punkte in einer pauschalen Ablehnung untergehen; eine externe Behauptung wird ungeprüft als wahr übernommen (das Gegenteil ist im Projekt mehrfach vorgekommen — Behauptungen, ein Feld fehle, waren falsch); Scope-Kriechen: eine Kritik am Inhalt wird nebenbei durch eine Framework-Änderung "miterledigt", obwohl dafür keine Freigabe vorliegt.

**Abbruchbedingungen:** Ein Kritikpunkt kann ohne Zugriff auf die vom Reviewer genannte Primärquelle nicht geprüft werden → als "nicht verifizierbar" kennzeichnen, nicht raten.

**Nicht-Ziele:** Ersetzt nicht die eigentliche fachliche Prüfung des Kritikpunkts (das leistet z. B. die wissenschaftliche Validierungsrolle); ist kein Mechanismus, um Kritik automatisch zu entkräften — im Zweifel ist Zurückstellen/Dokumentieren das korrekte Ergebnis, nicht Ablehnen.

**Erwarteter langfristiger Nutzen:** Erhält die Fähigkeit des Projekts, externes Feedback (menschlich oder durch andere KI-Systeme) aufzunehmen, ohne entweder beliebig nachgiebig oder beliebig defensiv zu werden — eine Kerneigenschaft, die laut Audit ausdrücklich als Stärke hervorgehoben wird ("Kultur der Selbstkorrektur … tatsächlich zu Herabstufungen … geführt").

---

### 3.5 Canonicalisierungs-Assistent (New / Extend / Merge / Reject)

**Zweck:** Bei jedem neuen Wissenskandidaten dieselbe strukturierte Entscheidungslogik anwenden, um zu bestimmen, ob ein neues Objekt angelegt, ein bestehendes erweitert, zwei Objekte zusammengeführt oder der Kandidat verworfen werden soll.

**Welches Problem der Skill löst:** Ohne feste Identitätskriterien entstehen entweder Duplikate (dasselbe Konzept mehrfach unter verschiedenen Namen) oder fälschliche Zusammenlegungen (unterschiedliche Kausalstrukturen werden vermischt). `canonical_knowledge_model.md` löst dies mit einer expliziten Entscheidungslogik (Abschnitt 4) und dokumentierten Grenzfällen (Abschnitt 9, "Nicht-Anlage-Dokumentation"). Das Muster ist rein strukturell: *Identität wird durch Kausalstruktur + Kontext bestimmt, nicht durch thematische Ähnlichkeit oder Stichworte* — das gilt für jede Art von Wissensbasis, nicht nur für Vertriebsmechanismen.

**Wann Claude ihn automatisch verwenden sollte:** Vor jeder Neuanlage eines Objekts in einer strukturierten Wissensbasis mit definierten Objekttypen und Identitätskriterien.

**Typische Ein-/Ausgaben:**
- Eingabe: der neue Kandidat (Aussage/Mechanismus/Prinzip/etc.), die vollständige Liste bestehender Objekte desselben Typs.
- Ausgabe: eine von vier Entscheidungen (Neu / Erweitern / Zusammenführungskandidat / Verwerfen) mit expliziter Begründung nach dem Vergleichskriterium des jeweiligen Objekttyps; bei "Zusammenführen" kein eigenmächtiger Vollzug, sondern ein Eintrag in einem Kandidatenregister.

**Standardisierter Workflow (abgeleitet aus `canonical_knowledge_model.md` Abschnitt 4):**
1. Alle bestehenden Objekte desselben Typs nach identischer *Struktur* durchsuchen (nicht nach Stichworten).
2. Prüffrage 1: Ist die kausale/strukturelle Grundlage identisch? Wenn nein → neu anlegen.
3. Prüffrage 2 (nur wenn ja): Ist der Kontext identisch? Wenn ja → Erweitern ist verpflichtend, Neuanlage ist verboten. Wenn nein → neu anlegen als Kontextspezialisierung, mit gegenseitigem Verweis.
4. Vor jeder Neuanlage: Mindestschwelle des Objekttyps prüfen (z. B. "mindestens zwei unabhängige Auftreten" für einen Mechanismus-Typ).
5. Wird ein Kandidat bewusst nicht angelegt, ist diese Entscheidung genauso pflichtig zu dokumentieren wie eine Neuanlage (Ort, Grund, Zuordnung zum abdeckenden Objekt).
6. Zusammenführungen sind nie ein eigenständiger Vollzug — sie werden vorgeschlagen und in ein Wartemodul (z. B. `review_queue.md`) eingetragen, bis eine übergeordnete Instanz entscheidet.

**Qualitätskriterien:** Jede Neu-/Erweiterungs-/Verwerfungsentscheidung nennt das konkrete Vergleichskriterium (nicht nur "ähnlich genug"); jede Ablehnung wird an genau einem bestehenden Objekt festgemacht.

**Typische Fehlerquellen:** Verwechslung von thematischer Nähe mit struktureller Identität (explizit als Kernfehler in Abschnitt 2 des CKM benannt); zu spät erkannte Duplikate, weil die Suche in Schritt 1 nach Stichworten statt nach Struktur erfolgte; eigenmächtige Zusammenführung ohne Freigabe der übergeordneten Entscheidungsinstanz.

**Abbruchbedingungen:** Zwei gleichermaßen vertretbare Klassifikationen ohne klare Präferenz → im Zweifel getrennt halten und als offene Frage dokumentieren, nicht raten.

**Nicht-Ziele:** Trifft keine abschließende Zusammenführungsentscheidung selbst; führt keine neuen Objekttypen ein; bewertet nicht die inhaltliche Richtigkeit des Kandidaten, nur seine strukturelle Einordnung.

**Erwarteter langfristiger Nutzen:** Verhindert Wildwuchs in einer wachsenden Wissensbasis unabhängig vom Fachgebiet; die real gemessene "Canonicalization Rate" (z. B. 37,5 %, 50 %, 67 % je nach thematischer Nähe, siehe `CODEX_AUDIT_2026-07.md` Kapitel 3) zeigt, dass dieses Muster bereits messbar Wirkung entfaltet und sich als KPI weiterverfolgen lässt.

---

### 3.6 Repository-Tiefenaudit (periodischer, benoteter Gesamtaudit)

**Zweck:** In größeren Abständen (nicht nach jeder Arbeitseinheit) eine vollständige, rein lesende Prüfung des gesamten Repositorys durchführen, die über die routinemäßige Selbstprüfung (3.3) hinausgeht: Statistiken, Redundanzanalyse, Evidenzverteilung, priorisierte Risiken, eine Gesamtnote.

**Welches Problem der Skill löst:** Einzelne Selbstreviews (3.3) prüfen jeweils nur die zuletzt bearbeitete Einheit und neigen dazu, ältere, nicht mehr im Fokus stehende Teile des Repositorys zu übersehen (siehe der Neubefund in `CODEX_AUDIT_2026-07.md`: Evidenzlevel-Desynchronisation zwischen MEC- und T-Ebene, drei frühere Prüfzyklen lang unentdeckt). Ein periodischer Tiefenaudit ist ein bewusst breiterer, selteneren Kontrollmechanismus.

**Wann Claude ihn automatisch verwenden sollte:** Vor größeren Meilensteinen (Versionsfreeze, Release), oder wenn der Herausgeber explizit einen Gesamtzustandsbericht anfordert, oder in einer festgelegten Kadenz (Kadenz selbst ist eine offene Governance-Frage im Projekt, vgl. OD-010, "Validierungs-Governance").

**Typische Ein-/Ausgaben:**
- Eingabe: das gesamte Repository (alle Objekttypen, alle Governance-Dokumente), keine Beschränkung auf eine Arbeitseinheit.
- Ausgabe: ein strukturierter Bericht mit Statistikteil, Stärken, Risiken (priorisiert), konkreten Handlungsempfehlungen in Reihenfolge, einer nachvollziehbar begründeten Gesamtnote.

**Standardisierter Workflow (abgeleitet aus `CODEX_AUDIT_2026-07.md`, komplette Struktur):**
1. Repository-Statistiken vollständig und nachprüfbar erheben (nicht aus einem Zwischenbericht übernehmen, sondern gegen das Dateisystem zählen).
2. Objektübergreifende Konsistenzprüfung: stichprobenartig auch die Ebenen prüfen, die zuletzt *nicht* im Zentrum standen (explizite Gegenmaßnahme gegen den in 3.3 beschriebenen Fehler).
3. Stärken und Risiken getrennt und konkret benennen — keine pauschale Gesamtbewertung ohne Beleg.
4. Handlungsempfehlungen priorisieren (nicht nur auflisten).
5. Gesamtnote nur mit expliziter, nachvollziehbarer Begründung vergeben, unter Bezug auf frühere Bewertungen (Verbesserung/Verschlechterung sichtbar machen).

**Qualitätskriterien:** Jede Statistik ist gegen die tatsächliche Dateibasis geprüft, nicht aus einem älteren Bericht übernommen; ein Neubefund (etwas, das frühere Prüfungen übersehen haben) wird explizit als solcher gekennzeichnet, nicht in die allgemeine Liste eingemischt.

**Typische Fehlerquellen:** Wiederholung der immer gleichen Prüfschwerpunkte (Bestätigungsschleife statt echter Neuprüfung); Verwechslung von "gut dokumentierter Unsicherheit" mit "kein Problem" (ein Risiko bleibt ein Risiko, auch wenn es transparent dokumentiert ist); Owner-Bias, wenn derselbe Akteur prüft, der zuvor gearbeitet hat (das Projekt begegnet diesem Risiko im Research Program durch die harte Rollentrennung Master Review/Peer Review — ein Hinweis, dass auch ein Tiefenaudit von einer unabhängigen Instanz vorteilhaft ist).

**Abbruchbedingungen:** Zugriff auf Teile des Repositorys fehlt → Audit als partiell kennzeichnen, keine Gesamtnote auf unvollständiger Basis vergeben.

**Nicht-Ziele:** Kein Ersatz für externe wissenschaftliche Begutachtung; keine Entscheidungsbefugnis über die aufgedeckten Risiken (das bleibt Herausgeber-Sache, ggf. über 3.4 verarbeitet).

**Erwarteter langfristiger Nutzen:** Fängt genau die Fehlerklasse ab, die häufige, aber enge Selbstreviews systematisch übersehen — komplementär, nicht redundant zu 3.3.

---

### 3.7 Governance-Register-Pflege (Open Decisions / Scientific Debt)

**Zweck:** Offene Entscheidungen und bekannte Wissenslücken als lebende, versionierte Register führen — nicht als einmalige Liste, sondern mit periodischer, ehrlicher Statusprüfung jedes einzelnen Eintrags.

**Welches Problem der Skill löst:** Offene Fragen und bekannte Schwächen werden in vielen Projekten entweder vergessen (nie wieder geprüft) oder unter Termindruck stillschweigend als erledigt behandelt. `OPEN_DECISIONS.md` und `SCIENTIFIC_DEBT.md` lösen dies durch ein festes Format: jeder Eintrag hat einen Status, und ein "Resolution Sprint" prüft jeden Eintrag einzeln, ohne automatische Sammel-Schließung (`OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`: von acht Entscheidungen wurden vier auf DONE gesetzt, eine ersetzt, drei blieben nach expliziter Einzelprüfung OFFEN).

**Wann Claude ihn automatisch verwenden sollte:** Immer, wenn eine Entscheidung getroffen werden müsste, aber (a) außerhalb der aktuellen Befugnis liegt, (b) auf eine externe Ressource wartet oder (c) bewusst vertagt wird; periodisch, um das gesamte Register gegen den aktuellen Zustand zu prüfen.

**Typische Ein-/Ausgaben:**
- Eingabe: das bestehende Register, der aktuelle Projektzustand.
- Ausgabe: pro Eintrag entweder unverändert OFFEN (mit Begründung, warum keine implizite Beantwortung vorliegt), DONE (mit Beleg), ERSETZT (mit Verweis auf Nachfolgeeintrag) oder neuer Eintrag.

**Standardisierter Workflow (abgeleitet aus `OPEN_DECISIONS.md`, Governance-Hinweis, und `OPEN_DECISION_RESOLUTION_REPORT_2026-07.md`):**
1. Ursprünglichen Text jedes Eintrags unverändert erhalten (nicht rückwirkend glätten).
2. Für jeden Eintrag einzeln prüfen, ob seit dem letzten Stand eine Entwicklung eingetreten ist, die ihn implizit beantwortet — nicht raten, sondern konkret belegen.
3. Kategorien sind fest: DONE / OFFEN (bestätigt) / ERSETZT / ANGENOMMEN (Entscheidung liegt vor, Umsetzung ggf. noch aus). Ein Eintrag ohne neue Entwicklung bleibt OFFEN — kein automatisches Schließen mangels Fortschritt.
4. Jede Auflösung wird als eigener, datierter Abschnitt am bestehenden Eintrag ergänzt, nicht als Ersetzung des Originaltexts.
5. Neue Erkenntnisse, die keine bestehende Entscheidung betreffen, werden als neuer, fortlaufend nummerierter Eintrag ergänzt.

**Qualitätskriterien:** Kein Eintrag verschwindet stillschweigend; jede Status-Änderung hat einen Beleg (Datei, Datum, Ereignis); ein Eintrag, der aus zwei separaten, aber verwandten Sorgen entsteht (vgl. OD-006/ARS-0001, "Meme-Risiko" und "Begriffsinflation"), wird als Zusammenhang dokumentiert statt dupliziert.

**Typische Fehlerquellen:** Implizite Schließung ("wurde seither nicht mehr erwähnt, also wohl erledigt") ohne Beleg; Vermischung von "technisch umgesetzt" und "inhaltlich abgeschlossen" (das Projekt trennt dies explizit, z. B. OD-006/OD-007: Entscheidung liegt vor, Umsetzung ist bewusst auf einen Folgesprint verschoben und bleibt bis dahin ausdrücklich unvollständig).

**Abbruchbedingungen:** Zwei Register (hier: `OPEN_DECISIONS.md`, `SCIENTIFIC_DEBT.md`, `review_queue.md`) drohen sich inhaltlich zu überschneiden, ohne dass ihre Abgrenzung definiert ist → als eigene Klärungsfrage eskalieren, nicht handeln, als wären es dieselbe Kategorie (im Projekt selbst als OD-011 dokumentiert).

**Nicht-Ziele:** Trifft keine Entscheidungen selbst — reine Statuspflege und Aufbereitung für die entscheidende Instanz; ersetzt keine Priorisierung durch den Herausgeber.

**Erwarteter langfristiger Nutzen:** Verhindert das in vielen Wissensprojekten typische Verschwinden unbequemer offener Punkte; macht den tatsächlichen Reifegrad eines Projekts an einer Stelle ablesbar, statt über Dutzende Dokumente verstreut.

---

### 3.8 Postmortem-/Retrospektiven-Generator

**Zweck:** Nach Abschluss einer bedeutenden Arbeitseinheit (nicht jeder einzelnen, sondern struktureller Meilensteine) eine strukturierte Rückschau erzeugen, die den Ablauf selbst bewertet — nicht nur das Ergebnis.

**Welches Problem der Skill löst:** Ohne strukturierte Retrospektive wiederholen sich vermeidbare Prozessfehler. `POST_MORTEM_B0002.md` (⚠ Volltext nicht gelesen, aus Changelog- und OD-001/OD-002-Kontext rekonstruiert: 12 Workflow-Phasen, Architekturreview, priorisierte Empfehlungen A/B/C) führte direkt zur Einführung des Book Mode und der Stateless Agent Architecture (OD-002, OD-003) — ein Beleg, dass das Muster tatsächlich Prozessänderungen ausgelöst hat, nicht nur dokumentiert wurde.

**Wann Claude ihn automatisch verwenden sollte:** Nach Abschluss eines strukturell neuen oder besonders folgenreichen Arbeitsablaufs (erster Durchlauf eines neuen Modus, Abschluss eines Forschungsprojekts, größere Sprintserie) — nicht nach jeder Routineeinheit.

**Typische Ein-/Ausgaben:**
- Eingabe: der vollständige Ablauf der abgeschlossenen Einheit (Sitzungslogs, erzeugte Dokumente, aufgetretene Abweichungen).
- Ausgabe: ein Bericht mit Ablaufbewertung, Architektur-/Methodikbewertung, priorisierten Empfehlungen (mind. zwei Prioritätsstufen), die in offene Entscheidungen überführt werden (nicht direkt umgesetzt).

**Standardisierter Workflow (abgeleitet aus Struktur und Wirkung von `POST_MORTEM_B0002.md` sowie dem projektspezifischen Health Check in `RESEARCH_LIFECYCLE.md` Abschnitt 12):**
1. Ablauf phasenweise rekonstruieren (nicht nur Endergebnis betrachten).
2. Architektur-/Methodikentscheidungen einzeln bewerten: hat die Regel/das Template in der Praxis funktioniert?
3. Empfehlungen priorisieren (mind. "sollte in den Standardprozess übernommen werden" vs. "Idee für später").
4. Empfehlungen nicht selbst umsetzen — als offene Entscheidungen an die zuständige Freigabeinstanz übergeben (siehe Übergang Postmortem → OD-001/OD-002/OD-003).

**Qualitätskriterien:** Empfehlungen sind konkret und einzeln umsetzbar, nicht allgemeine Stimmungsbilder; jede Empfehlung benennt, welches konkrete Dokument sie beträfe, falls umgesetzt.

**Typische Fehlerquellen:** Retrospektive wird zur reinen Erfolgsbestätigung ohne kritische Distanz; Empfehlungen bleiben vage ("mehr Sorgfalt") statt konkret (welches Template, welches Feld); Vermischung von einmaligen Sonderfällen mit strukturellen Mustern.

**Abbruchbedingungen:** Keine — ein Postmortem sollte grundsätzlich durchführbar sein, solange der Ablauf dokumentiert ist; fehlt die Dokumentation des Ablaufs selbst, ist das der eigentliche Befund.

**Nicht-Ziele:** Setzt keine Prozessänderung eigenmächtig in Kraft; ist kein Ersatz für die Konsistenzprüfung der Inhalte (3.3).

**Erwarteter langfristiger Nutzen:** Der nachweisbare Effekt im Projekt selbst (Postmortem → drei umgesetzte Open Decisions → Framework v1.1) zeigt, dass dieses Muster tatsächlich Methodik verbessert, nicht nur dokumentiert.

---

### 3.9 Forschungsprogramm-Stufen-Orchestrator (Research Lifecycle Gate)

**Zweck:** Für Fragen, die der Standardprozess (3.2) nicht lösen kann (insbesondere Widersprüche zwischen bereits verarbeiteten Einheiten), einen separaten, mehrstufigen Prozess mit klaren Rollentrennungen und Übergabekriterien je Stufe orchestrieren.

**Welches Problem der Skill löst:** Manche Fragen sind zu groß oder zu grundsätzlich für den Routineprozess und brauchen eine eigene, langsamere, mehrfach gegengeprüfte Bearbeitung. `RESEARCH_LIFECYCLE.md` definiert genau das: neun Stufen (Research Question → Initial Hypothesis → Master Review → Peer Review → Theory Landscape → Decision Brief → Editor Decision → Repository Integration → Health Check), mit einer harten Rollentrennungsregel (Peer Reviewer ≠ Master Reviewer, `RESEARCH_GOVERNANCE.md` Abschnitt 4.4).

**Wann Claude ihn automatisch verwenden sollte:** Wenn eine Frage nicht durch einfaches Nachschlagen oder Erweitern eines bestehenden Objekts lösbar ist, sondern eine eigenständige, gegen konkurrierende Hypothesen abzuwägende Untersuchung erfordert — insbesondere bei dokumentierten Widersprüchen zwischen bestehenden Wissensobjekten.

**Typische Ein-/Ausgaben:**
- Eingabe: eine benannte, aus einem konkreten Repository-Anlass abgeleitete Forschungsfrage.
- Ausgabe: eine Kette von neun Stufendokumenten, endend in einer verbindlichen Freigabeentscheidung und (bei Annahme) integrierten Wissensobjekten plus Abschluss-Health-Check.

**Standardisierter Workflow:** siehe vollständige Stufenbeschreibung in `RESEARCH_LIFECYCLE.md`, Abschnitte 3–12 (Research Question, Initial Hypothesis, Master Review, Peer Review, Theory Landscape, Decision Brief, Editor Decision, Repository Integration, Health Check) — hier nicht wiederholt, um keine Redundanz zum bestehenden Dokument zu erzeugen.

**Qualitätskriterien:** Übergabekriterien jeder Stufe sind laut Lifecycle-Dokument bereits explizit definiert; ein Widerspruch zwischen zwei Stufen ist kein Abbruchgrund, sondern wird unverändert an die nächste Stufe weitergereicht (Grundprinzip, nicht Ausnahme).

**Typische Fehlerquellen:** Stufen überspringen unter Zeitdruck; Rollentrennung (Master vs. Peer Reviewer) faktisch aufweichen, weil dieselbe Session beide Rollen übernimmt; Theory-Landscape-Stufe vor statt nach den Reviews ansetzen, ohne die im Projekt selbst dokumentierte bewusste Abgrenzung zu kennen (Abschnitt 7 des Lifecycle-Dokuments).

**Abbruchbedingungen:** Siehe `RESEARCH_GOVERNANCE.md` Abschnitt 7 (u. a. unzugängliche Primärquelle, ethischer Grenzfall, unauflösbarer Canonicalisierungskonflikt bei der Integration).

**Nicht-Ziele:** Ersetzt nicht den Standardprozess (3.2) für gewöhnliche Quellenverarbeitung; führt keine neuen Objekttypen ein.

**Erwarteter langfristiger Nutzen:** Hoch, aber schmal — nur ein vollständiger Durchlauf (W-001) liegt bisher vor. Das Muster ist ausgereift dokumentiert, aber noch nicht durch Wiederholung geprüft (Tier-Einordnung berücksichtigt dies, siehe Abschnitt 4).

---

### 3.10 Repository-Konsolidierung (strukturelles Housekeeping)

**Zweck:** In eigenen, klar abgegrenzten Sprints strukturelle Unordnung (verwaiste Ordner, falsch abgelegte Dateien, doppelte Nummernbelegung, tote Verweise) beheben — ausdrücklich getrennt von inhaltlicher Arbeit.

**Welches Problem der Skill löst:** Strukturelle Unordnung sammelt sich in jedem wachsenden Repository an. `REPOSITORY_CONSOLIDATION_REPORT_RC1.md` / `_IMPLEMENTATION_REPORT_RC1.md` (⚠ Volltexte nicht gelesen, aus Changelog-Eintrag 2026-07-02 rekonstruiert) belegen ein Muster: acht einzeln freigegebene Editor Decisions (ED-001 bis ED-008), rein strukturell, mit anschließender repositoryweiter Cross-Referenz-Prüfung.

**Wann Claude ihn automatisch verwenden sollte:** Wenn im Rahmen anderer Arbeit strukturelle Unordnung auffällt (leere Ordner, doppelte Ablagen, falsch platzierte Dateien) — gesammelt in einem eigenen Sprint, nicht einzeln nebenbei "mal eben" behoben.

**Typische Ein-/Ausgaben:**
- Eingabe: der vollständige Verzeichnisbaum, bekannte strukturelle Auffälligkeiten (oft aus einem vorausgehenden Tiefenaudit, 3.6).
- Ausgabe: eine Liste einzeln benannter, einzeln freizugebender struktureller Änderungen (ED-Format), nach Freigabe ausgeführt, mit anschließendem Cross-Referenz-Check und Umsetzungsbericht.

**Standardisierter Workflow (abgeleitet aus dem Zwei-Phasen-Muster Sprint 1/Sprint 2):**
1. Auffälligkeiten sammeln, jede einzeln benennen (nicht pauschal "Repository aufräumen").
2. Für jede Auffälligkeit eine eigene, kurze Editor-Decision-Zeile formulieren (was, warum, Auswirkung).
3. Erst nach Sammelfreigabe durch die entscheidende Instanz ausführen.
4. Nach Ausführung: repositoryweite Prüfung, ob alte Pfadverweise auf die verschobenen/gelöschten Elemente noch existieren; historische, datierte Berichte bewusst unverändert lassen (sie beschreiben einen historischen Zustand, keinen aktuellen).
5. Umsetzungsbericht mit einer Zeile pro ED-Nummer.

**Qualitätskriterien:** Jede Änderung ist einzeln nachvollziehbar (keine Sammeloperation "diverses aufgeräumt"); nach der Operation ist die Cross-Referenz-Integrität geprüft, nicht nur angenommen.

**Typische Fehlerquellen:** Versehentliches Verändern historischer Berichte beim "Aufräumen" von Referenzen (das Projekt behandelt dies explizit als Fehler: alte Pfadverweise in datierten Sprintberichten bleiben bewusst unverändert); strukturelle und inhaltliche Änderungen in einem Sprint vermischen.

**Abbruchbedingungen:** Eine gefundene Unregelmäßigkeit liegt außerhalb des Sprintumfangs (Beispiel aus dem Projekt: ein vorbestehender Git-Indexfehler wurde erkannt, aber bewusst nicht behoben, sondern nur dokumentiert und dem Herausgeber gemeldet) → dokumentieren, nicht "mal eben mitbeheben".

**Nicht-Ziele:** Keine inhaltlichen Entscheidungen; keine Architekturentscheidungen "nebenbei"; kein Ersatz für den Tiefenaudit, der die Auffälligkeiten meist erst identifiziert.

**Erwarteter langfristiger Nutzen:** Hält die strukturelle Übersichtlichkeit auch bei starkem Wachstum aufrecht; das Muster ist bereits zweimal erprobt und funktioniert nachweislich (0 gefundene Inkonsistenzen im zweiten Durchlauf).

---

### 3.11 Release-Freeze- und Versionierungsprotokoll

**Zweck:** Einen erreichten Reifegrad formal einfrieren: Snapshot des Zustands, Freeze-Erklärung mit erlaubten/verbotenen Änderungen, Verifikation gegen das tatsächliche Dateisystem, klare Abgrenzung zwischen "eingefroren" und "veröffentlicht".

**Welches Problem der Skill löst:** Ohne einen formalen Freeze-Mechanismus verschwimmt der Unterschied zwischen "wir arbeiten noch daran" und "dieser Stand gilt". Das Projekt hat dieses Muster mindestens dreimal angewendet: v1.0-Infrastruktur-Freeze (2026-06-27), v1.1-Release (2026-06-30), RC-1-Freeze und anschließende Version-1.0-Veröffentlichung (2026-07-03/04) — mit wachsender Formalisierung (Freeze-Kennzahlen, Manifest-Snapshot, explizite Aussage "READY FOR AUDIT" statt "READY FOR RELEASE").

**Wann Claude ihn automatisch verwenden sollte:** Vor einem angekündigten Meilenstein/Release, wenn der Herausgeber einen Zustand als verbindlich referenzierbar markieren möchte.

**Typische Ein-/Ausgaben:**
- Eingabe: aktueller Gesamtzustand des Projekts (Objektzahlen, Governance-Status, bekannte Einschränkungen).
- Ausgabe: eine Freeze-Erklärung (was ist ab jetzt unveränderlich, was ist noch änderbar), ein Manifest/Snapshot, Release Notes, ein Verifikationsbericht (Kennzahlen gegen tatsächliches Dateisystem geprüft, nicht nur behauptet).

**Standardisierter Workflow (abgeleitet aus den drei Freeze-Vorkommen, insbesondere den Changelog-Einträgen 2026-07-03/04):**
1. Kennzahlen erheben und *unabhängig gegen das Dateisystem verifizieren* (nicht aus einem vorherigen Bericht kopieren).
2. Freeze-Erklärung: explizit benennen, was ab sofort nicht mehr verändert werden darf, und was (z. B. Backlog für die Folgeversion) weiterhin änderbar bleibt.
3. Klare Sprachtrennung zwischen Zwischenzuständen einhalten (z. B. "bereit für den Audit" ist nicht dasselbe wie "bereit für die Veröffentlichung" — beide Zustände werden im Projekt bewusst unterschieden, nicht vermischt).
4. Erst nach einer separaten, expliziten Freigabeinstanz erfolgt der Übergang von "eingefroren" zu "veröffentlicht".
5. Am Ende: Versionsfelder in allen Statusdokumenten konsistent aktualisieren (nicht nur an einer Stelle).

**Qualitätskriterien:** Jede genannte Kennzahl ist nachprüfbar, nicht nur behauptet; die Freeze-Erklärung wird nicht mit der Veröffentlichungserklärung verwechselt oder vorschnell gleichgesetzt.

**Typische Fehlerquellen:** Voreiliges Gleichsetzen von "eingefroren" mit "veröffentlicht" (das Projekt vermeidet dies explizit — RC1_FREEZE_REPORT.md spricht bewusst nur von "READY FOR FINAL RC-1 AUDIT", nicht "READY FOR RELEASE"); Kennzahlen aus einem älteren Bericht unkritisch übernehmen, statt neu zu verifizieren.

**Abbruchbedingungen:** Verifikation deckt eine Diskrepanz zwischen behauptetem und tatsächlichem Zustand auf → Freeze verzögern, Diskrepanz zuerst klären.

**Nicht-Ziele:** Kein Ersatz für den Tiefenaudit (3.6) oder die externe Begutachtung — ein Freeze bestätigt einen Zustand, er bewertet ihn nicht neu.

**Erwarteter langfristiger Nutzen:** Schafft verlässliche, zitierfähige Meilensteine — wichtig, sobald mehrere Akteure (menschlich oder KI) sich auf "den aktuellen Stand" beziehen müssen.

---

### 3.12 Graph-/Referenz-Integritätsprüfung — NICHT als Skill geeignet

**Warum kein Skill:** Dieses Muster (Knoten/Kanten aus expliziten ID-Referenzen extrahieren, Reference Orphans und unaufgelöste Referenzen finden, siehe `08_knowledge_atlas/scripts/compile_atlas.py` und den zugehörigen Report) ist bereits als deterministisches, mechanisches Skript gelöst — nicht als eine Aufgabe, die agentisches Urteilsvermögen braucht. Ein Skill mit LLM-Beteiligung wäre hier langsamer, teurer und weniger zuverlässig als ein einfaches Skript, das bei jedem Lauf exakt reproduzierbare Ergebnisse liefert (der Report selbst benennt dies: "reiner Struktur-Export … keine Analyseplattform"). Der Bericht dokumentiert zudem explizit die Grenzen eines reinen Textmuster-Scans (Bereichsangaben, Sonderformate) — Grenzen, die durch besseres Skript-Engineering behoben werden, nicht durch ein LLM "mit Ermessen".

**Empfehlung statt Skill:** Das bestehende Skript pflegen und bei Bedarf ausführen; ein Claude-Skill sollte höchstens den *Aufruf* dieses Skripts plus die *Interpretation* des Ergebnisberichts (z. B. "ist ein gefundener Orphan handlungsrelevant?") übernehmen — das wäre dann aber wieder Teil des Tiefenaudits (3.6), kein eigenständiges Muster.

---

### 3.13 Herausgeber-Entscheidung / Framework-Änderung — NICHT als Skill geeignet

**Warum kein Skill:** Jede der recherchierten Governance-Dokumente (`SALES_CODEX_OPERATING_MANUAL.md` Abschnitt 8, `DECISION_POLICY.md`, `task_rules.md` Abschnitt 9) markiert diesen Schritt ausdrücklich als exklusive menschliche Entscheidungsbefugnis, nicht delegierbar: "Keine Framework-Änderungen — Ordnerstruktur, Templates und Methodik werden nicht eigenständig modifiziert." Ein Skill, der diesen Schritt automatisiert, würde der zentralen Rollentrennung des gesamten Projekts widersprechen (Herausgeber = Entscheider, KI = Produzent/Redakteur). Das gilt vermutlich für jedes Wissensprojekt mit vergleichbarer Governance-Struktur, nicht nur für den Sales Codex.

**Was stattdessen sinnvoll ist:** Die *Vorbereitung* einer Herausgeber-Entscheidung (Optionen strukturieren, Für/Wider aufbereiten, wie in den vorliegenden OD-Einträgen bereits praktiziert) ist Teil von 3.7 (Governance-Register-Pflege) und dort bereits abgedeckt — die Entscheidung selbst bleibt außerhalb des Skill-Anspruchs.

---

## 4. Priorisierung nach strategischem Wert

### 1 — Sofort implementieren

| Skill | Kurzbegründung |
|---|---|
| 3.1 Session-Kontinuitätsprotokoll | Höchster Hebel, geringste Komplexität, in jeder Session wirksam, bereits vollständig als Konvention etabliert — muss nur noch als aktiv erzwungenes Verhalten formalisiert werden. |
| 3.2 Wissens-Extraktions-Pipeline-Orchestrator | Zehnfach erprobt, deterministisch spezifiziert (`task_rules.md`), größter Zeitgewinn im laufenden Betrieb. |
| 3.3 Konsistenz-Selbstreview | Direkt nach jeder Arbeitseinheit einsetzbar, verhindert die im Audit real belegte Fehlerklasse (Ebenen-Desynchronisation), klar abgegrenzter Prüfrahmen. |
| 3.4 Externe-Kritik-Verarbeitung | Sechsfach wiederholtes, ausgereiftes Muster mit fertigem Regelwerk (`DECISION_POLICY.md`); besonders wertvoll für die Zusammenarbeit mit externen/anderen KI-Systemen. |

### 2 — Mittelfristig sinnvoll

| Skill | Kurzbegründung |
|---|---|
| 3.5 Canonicalisierungs-Assistent | Sehr hoher Wert, aber die Entscheidungslogik ist komplex genug (typspezifische Kriterien), dass ein sorgfältiger, iterativer Skill-Entwurf sinnvoller ist als ein sofortiger Wurf. |
| 3.6 Repository-Tiefenaudit | Wertvoll, aber selten genutzt (bisher zwei echte Vorkommen) — Kadenz und Auslöser sind noch nicht abschließend geklärt (vgl. OD-010). |
| 3.7 Governance-Register-Pflege | Wichtig für Langlebigkeit, aber von der noch offenen Grundsatzfrage abhängig, wie sich die drei parallelen Register zueinander verhalten sollen (OD-011) — Skill-Design sollte diese Klärung abwarten. |
| 3.8 Postmortem-Generator | Nachweislich wirksam, aber naturgemäß selten (nur nach größeren Meilensteinen) — geringerer Automatisierungsdruck als bei täglich genutzten Mustern. |

### 3 — Optional

| Skill | Kurzbegründung |
|---|---|
| 3.9 Forschungsprogramm-Stufen-Orchestrator | Ausgereift dokumentiert, aber erst einmal vollständig durchlaufen — ein Skill auf Basis einer einzigen Iteration wäre verfrüht formalisiert. |
| 3.10 Repository-Konsolidierung | Selten (zwei Vorkommen), von Natur aus risikobehaftet (Datei verschieben/löschen) — manuelle Sorgfalt unter Aufsicht ist hier vermutlich dauerhaft angemessener als Automatisierung. |
| 3.11 Release-Freeze-Protokoll | Wertvoll, aber sehr selten (drei Vorkommen über die gesamte Projektlaufzeit) — Formalisierung lohnt sich erst, wenn absehbar ist, dass Sales Codex 2.0 denselben Rhythmus wiederholt. |

### 4 — Nicht als Skill geeignet

| Muster | Kurzbegründung |
|---|---|
| 3.12 Graph-/Referenz-Integritätsprüfung | Bereits korrekt als deterministisches Skript gelöst — ein Skill würde hier Zuverlässigkeit gegen Flexibilität eintauschen, ohne Gegenwert. |
| 3.13 Herausgeber-Entscheidung / Framework-Änderung | Strukturell nicht delegierbar; jede Automatisierung würde der Kernrollentrennung des Projekts widersprechen. |

---

## 5. Offene Fragen an den Herausgeber

- Soll die Priorisierung in Abschnitt 4 als verbindliche Reihenfolge für die tatsächliche Skill-Entwicklung gelten, oder nur als Diskussionsgrundlage?
- Für 3.6 und 3.7 hängt der sinnvolle Skill-Zuschnitt von noch offenen Governance-Fragen ab (insbesondere OD-010 "Validierungs-Governance" und OD-011 "Literature-Governance"). Sollen diese zuerst entschieden werden, bevor ein Skill-Entwurf für 3.6/3.7 beginnt?
- Dieses Dokument wurde als neue Analyse-Datei in `00_project/` abgelegt (Konvention wie bei `CODEX_AUDIT_2026-07.md`, `POST_MORTEM_*.md`). Ist diese Ablage im Sinne des Herausgebers, oder soll eine Analyse dieser Art künftig an anderer Stelle geführt werden (z. B. ein neuer Bereich außerhalb der Kern-Repository-Struktur, analog zu `08_knowledge_atlas/` als eigenständigem Subsystem)?

---

*Dieses Dokument ist eine Analyse, keine Framework-Änderung. Es legt keine Skills fest, ändert keine Templates, keine Ordnerstruktur und keine Methodik. Alle Aussagen sind mit Repository-Referenzen belegt; wo Volltexte nicht gelesen wurden, ist dies durch ⚠ gekennzeichnet. Erstellt: 2026-07-04.*
