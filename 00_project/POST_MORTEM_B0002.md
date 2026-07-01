# Post-Mortem — Sales Codex B-0002 Influence

Erstellt: 2026-06-30  
Bearbeiter: Cowork / Claude  
Status: Entwurf — wartet auf Herausgeber-Freigabe

## Vorbemerkung

Dieser Bericht bewertet den Prozess, nicht die Inhalte. Grundlage: der vollständige Gesprächsverlauf dieser und der vorangehenden Session, der Repository-Stand sowie BOOK_REVIEW_REPORT_B0002.md. Alle Empfehlungen stehen unter Freigabevorbehalt.

---

## Phase 1 — Source (TASK-0001)

**Was hat gut funktioniert:**
SRC-0002 wurde sauber angelegt. Das Source-Template liefert alle relevanten Felder. Die Verknüpfung zur PDF-Primärquelle war explizit.

**Probleme:**
Die initiale Anlage enthielt "Ausgabe 2021" (falsch) — die Korrektur auf "Ausgabe 2007" musste nachträglich in mehreren Dateien durchgeführt werden (SRC-0002, analysis.md). Ursache: Die Ausgabe wurde zu Beginn nicht direkt aus dem PDF-Cover verifiziert, sondern aus dem Gedächtnis angenommen. Der Fehler verbreitete sich, weil die Source-ID-Datei als Referenz für alle anderen Dateien dient.

**Fehlende Regeln:**
Es gibt keine explizite Pflicht, die Ausgabe beim Source-Anlegen direkt aus dem Primärtext zu verifizieren (PDF-Titelseite oder Impressum). Eine solche Pflichtprüfung hätte den Fehler verhindert.

**Überflüssige Arbeiten:**
Keine in dieser Phase.

**Automatisierungspotenzial:**
Ein Source-Checklist-Schritt ("Ausgabe aus Impressum verifiziert: ja/nein") direkt im SRC-Template würde Ausgabenfehler verhindern.

**Dokumente verwendet:** source_template.md, SRC-0002.  
**Dokumente praktisch nicht verwendet:** book_catalog.md (nur für Statusangaben, nicht für die eigentliche Arbeit).

---

## Phase 2 — Book Analysis (TASK-0002)

**Was hat gut funktioniert:**
analysis.md als zentrales Koordinationsdokument hat sich bewährt. Die Kapitelstruktur aus dem PDF-Inhaltsverzeichnis wurde korrekt erfasst.

**Probleme:**
Die Kapitelzeilen in der Kapitelstruktur-Tabelle blieben auf "ausstehend" stehen, auch nachdem alle Kapitel bearbeitet waren. Die Tabelle wurde nie auf "analysiert" aktualisiert. Dies ist ein Pflegefehler: analysis.md dient als Koordinationsdokument, aber es gibt keine Pflicht, den Kapitelstatus nach Abschluss jedes Kapitels zu aktualisieren.

**Fehlende Regeln:**
Nach Abschluss von TASK-0003 (Statements) sollte die Kapitelstatustabelle in analysis.md als Pflichtschritt aktualisiert werden.

**Überflüssige Arbeiten:**
Die Kapitelstruktur-Tabelle wurde initial sehr detailliert angelegt (Startseiten), aber die Startseiten-Information wurde danach nie wieder verwendet.

**Automatisierungspotenzial:**
Kapitelstatus-Aktualisierung als expliziter Sub-Schritt am Ende von TASK-0003.

---

## Phase 3 — Statements (TASK-0003)

**Was hat gut funktioniert:**
Die PDF-Extraktion via pdfplumber funktionierte gut. 26 Statements aus 9 Einheiten sind eine solide Grundlage. Die Entscheidung, ausschließlich aus dem Primärtext zu extrahieren (keine Trainingswissen-Paraphrasen), wurde konsequent eingehalten.

**Probleme:**

- Kapitel 2 produzierte 82,2 KB Rohtext — zu viel für direkte Verarbeitung. Lösung war manuelle Auswahl von Schlüsselseiten. Eine strukturiertere Extraktion (z.B. max. N Seiten pro Kapitel) würde das zuverlässiger machen.
- Die ST-Objektzahl (26) ist für ein 200-seitiges Buch knapp. Es entstand die Frage, ob wichtige Belege fehlen — ohne dass eine systematische Vollständigkeitsprüfung möglich war.
- Context Window: Die Session endete mitten in TASK-0003. Die Übergabe an die nächste Session über einen Kontextzusammenfassung funktionierte, war aber aufwändig und fehleranfällig (der Zusammenfassungstext enthielt keine ST-Dateiinhalte, nur Beschreibungen).

**Fehlende Regeln:**

- Kein Mindestzahl-Kriterium für ST-Objekte pro Kapitel (verhindert zu dünne Extraktion).
- Kein Maximalzahl-Kriterium (verhindert Überextraktion).
- Keine Pflicht-Kontrollfrage: "Sind die sechs Hauptprinzipien vollständig belegt?" nach TASK-0003.

**Überflüssige Arbeiten:**
Der Aufwand, nach einem Context-Window-Break den Zustand zu rekonstruieren, war hoch. Die Stateless Architecture (CURRENT_STATE.md, NEXT_ACTION.md) hätte das stark vereinfacht — sie existierte zu diesem Zeitpunkt noch nicht.

**Automatisierungspotenzial:**
Ein ID-Counter-Skript ("nächste freie ST-ID") würde Zählfehler vermeiden.

**Dokumente verwendet:** pdfplumber (Python), statement_template.md.  
**Dokumente praktisch nicht verwendet:** extraction_standards.md (soweit erkennbar — nicht explizit referenziert).

---

## Phase 4 — Annahmen (TASK-0004)

**Was hat gut funktioniert:**
Die n:m-Clustering-Methodik (explizit vom Herausgeber eingeführt) war der wichtigste methodische Fortschritt gegenüber Pilot-001. 8 Annahmen aus 26 Statements sind sinnvoll verdichtet. Die thematischen Cluster (kognitive Grenzen, Einzelmerkmal-Trigger, evolutionäre Verankerung, relative Wertwahrnehmung, Commitment-Selbstbild, soziale Signalübertragung, Compliance-Redirect, Verfügbarkeitsrestriktion) decken das Buch gut ab.

**Probleme:**

- Es gab keine explizite Qualitätsprüfung nach TASK-0004: "Decken die Annahmen wirklich alle Hauptmechanismen ab?" Eine Überprüfungsmatrix (ST → A-Cluster) wurde nicht formal angelegt, obwohl sie implizit im Clustering steckte.
- Die Annahmen-Objekte haben keine eigene Evidenzklasse, weil sie abgeleitet sind — das ist korrekt, aber für spätere Leser nicht sofort klar.

**Fehlende Regeln:**

- Eine Vollständigkeitsprüfung ("Sind alle Hauptthesen des Buches in mindestens einer Annahme abgedeckt?") fehlt als expliziter Schritt.
- Keine Konvention für die Reihenfolge der Annahmen-IDs (aktuell: chronologisch nach Erstellungsreihenfolge, nicht nach Thema).

**Überflüssige Arbeiten:**
Keine in dieser Phase.

**Automatisierungspotenzial:**
Eine Cluster-Matrix (ST-ID → A-ID-Mapping) als Teil des A-Objekts oder als separates Dokument würde die Nachvollziehbarkeit erhöhen.

---

## Phase 5 — Mechanismen (TASK-0005)

**Was hat gut funktioniert:**
Die Canonicalization-Entscheidung (EXTEND vs. NEW) war der produktivste Arbeitsschritt. Drei bestehende MECs (MEC-0001, MEC-0003, MEC-0004) zu erweitern statt Duplikate anzulegen — und diese Entscheidung explizit zu dokumentieren — ist ein echter Qualitätsgewinn. Das Canonical Knowledge Model hat hier konkret gearbeitet.

**Probleme:**

- Edit-without-Read-Fehler bei MEC-0001: Beim Versuch, MEC-0001 zu erweitern, wurde vergessen, die Datei zuerst zu lesen. Fehlermeldung: "File has not been read yet." Dieses Problem trat mehrfach auf.
- Die Abgrenzung MEC-0001 (Bem Self-Perception) vs. MEC-0004 (Festinger Dissonance) war konzeptuell anspruchsvoll — die Grenzlinie ist korrekt, aber die Dokumentation erforderte mehrere Überarbeitungen.
- Die Scarcity-as-value-heuristic wurde bewusst NICHT als eigener MEC angelegt (nur als A-Objekt) — diese Entscheidung ist richtig, aber sie wurde nicht formal dokumentiert. Sie versteckt sich implizit in den Canonicalisierungsabschnitten.

**Fehlende Regeln:**

- Eine explizite "Nicht-Anlage-Entscheidung"-Dokumentation fehlt: Wenn ein Kandidat BEWUSST nicht als MEC angelegt wird, sollte das genauso explizit dokumentiert sein wie eine EXTEND- oder NEW-Entscheidung.
- Das Read-before-Edit-Muster sollte als explizite Arbeitsregel in agent_protocols aufgenommen werden.

**Überflüssige Arbeiten:**
Die Scarcity-as-value-heuristic wurde in Annahmen und Diskussionen mehrfach thematisiert, bevor die Nicht-Anlage-Entscheidung final war.

**Automatisierungspotenzial:**
Ein Canonicalization-Checklisten-Template ("Haben wir geprüft: identische Kausalstruktur? Identischer Kontext? Merge, Extend oder New?") würde die Entscheidungsdokumentation vereinheitlichen.

---

## Phase 6 — Prinzipien (TASK-0006)

**Was hat gut funktioniert:**
Die explizite Abgrenzungspflicht (vom Herausgeber eingeführt) war der entscheidende Qualitätsimpuls. Jedes P-Objekt enthält einen "Abgrenzung vom Mechanismus"-Abschnitt. Das erzwang tieferes Analysieren und verhinderte oberflächliche Reformulierungen. Die Quervergleiche gegen P-0001–P-0007 wurden systematisch durchgeführt und dokumentiert.

**Probleme:**

- Fünf P-Objekte referenzieren nur einen Hauptmechanismus (P-0009, P-0011, P-0012, P-0013, P-0015). Das ist korrekt, weil sie je zwei A-Objekte referenzieren, aber die Regel lautet "mehrere Mechanismen ODER Annahmen" — die OR-Interpretation musste implizit angewendet werden, ohne dass sie in task_rules.md explizit so formuliert ist.
- P-0008 (Meta-Prinzip) ist konzeptuell der stärkste Beitrag, aber zugleich das schwächste P-Objekt bezüglich direkter Evidenz. Das Meta-Prinzip ist stärker ein Rahmenkonzept als ein empirisch belegtes Prinzip — es hätte möglicherweise als MOD-Kapitel besser gepasst. Diese Grenzfrage blieb offen.

**Fehlende Regeln:**

- Die OR-Formulierung ("aus mehreren Mechanismen ODER Annahmen") sollte in task_rules.md explizit stehen.
- Es fehlt ein Kriterium, wann ein Konzept als P-Objekt vs. als MOD-Abschnitt klassifiziert werden sollte. P-0008 illustriert diese Grenzfrage.

**Überflüssige Arbeiten:**
Die Quervergleiche gegen P-0001–P-0007 waren für die meisten P-Objekte schnell abgehandelt (keine Überschneidung), aber für P-0010 (Commitment-Sequenzierung) vs. P-0007 (Verpflichtungssicherung) war die Abgrenzung aufwändig und korrekt.

**Automatisierungspotenzial:**
Ein Template-Pflichtfeld "Quervergleich mit bestehenden P-Objekten: [IDs geprüft, Ergebnis]" würde sicherstellen, dass die Quervergleiche immer durchgeführt und dokumentiert werden.

---

## Phase 7 — Techniken (TASK-0007)

**Was hat gut funktioniert:**
7 Techniken für 6 Cialdini-Prinzipien ist eine angemessene Dichte. Die Zuordnung zu Gesprächszuständen (Pre-Contact, Attention, Solution_Evaluation, Decision) gibt den T-Objekten eine Verwendungskontext-Verankerung.

**Probleme:**

- Rapport/Liking hat kein eigenes T-Objekt — Ähnlichkeits-Signalisierung und Rapport-Aufbau wurden als "Kompetenz" eingestuft, nicht als Technik. Das ist vertretbar, aber die Grenze zwischen Technik und Kompetenz ist im Framework nicht explizit definiert.
- Die ethischen Risiko-Bewertungen für T-0010 (Credential-Positionierung) und T-0011 (Knappheitssignale) sind "hoch" — was den Eindruck erweckt, dass der Sales Codex primär hochriskante Techniken enthält. Das liegt daran, dass Cialdini-Techniken grundsätzlich manipulationsanfälliger sind als SPIN-Fragetypen.
- T-0006 (Rejection-then-Retreat) und T-0007 (Foot-in-the-Door) haben beide Evidenzlevel E3, aber die Evidenz ist unterschiedlich geartet (Labor vs. Feld). Diese Differenzierung geht im E-Level verloren.

**Fehlende Regeln:**

- Eine Definition der Grenze zwischen Technik (T-Objekt) und Kompetenz (Verknüpfte Kompetenz) fehlt im Framework.
- Kein Kriterium, wie viele T-Objekte pro Quelle "ausreichend" sind.

---

## Phase 8 — Modelle (TASK-0008)

**Was hat gut funktioniert:**
MOD-0002 bietet den konzeptuellen Rahmen, der alle Cialdini-Objekte verbindet. Die Vergleichstabelle mit MOD-0001 (SPIN Selling) ist ein echter Mehrwert. Die Kahneman-Quervergleich-Notiz ist korrekt platziert (offen, nicht erfunden).

**Probleme:**

- Ein Modell-Template existiert möglicherweise nicht oder wurde nicht referenziert. MOD-0002 orientiert sich am Format von MOD-0001, nicht an einem expliziten Template. Inkonsistenz-Risiko bei zukünftigen Modellen.
- Die Frage "Wann ist ein Modell ein MOD-Objekt vs. ein ergänzter MOD-Abschnitt?" ist nicht geregelt.

**Fehlende Regeln:**

- Ein model_template.md fehlt (oder war nicht auffindbar). MOD-0001 wurde als De-facto-Template verwendet.

---

## Phase 9 — Canonicalisierung

**Gesamtbewertung:**
Das Canonical Knowledge Model hat im Influence-Durchlauf seinen Zweck erfüllt. Drei Erweiterungs-Entscheidungen wurden korrekt getroffen und dokumentiert. Fünf neue MECs wurden angelegt. Kein offensichtliches Duplikat wurde erzeugt.

**Was hat gut funktioniert:**

- Die Entscheidungslogik (identische Kausalstruktur = erweitern; andere Struktur = neu) war in der Praxis ausreichend klar.
- Die explizite Canonicalisierungs-Dokumentation in jedem MEC-Objekt macht die Entscheidungen nachvollziehbar und revidierbar.
- Die Abgrenzung MEC-0001 (Bem) vs. MEC-0004 (Festinger) verhinderte eine falsche Zusammenführung.

**Probleme:**

- Die "Nicht-Anlage"-Entscheidung (Scarcity-as-value-heuristic wird NICHT als MEC angelegt) ist nicht formal dokumentiert.
- Die Grenzfrage bei P-0008 (Prinzip oder Modell?) wurde nicht durch CKM-Regeln entschieden, sondern pragmatisch.
- Das CKM gilt explizit für MECs. Ob dieselbe Logik auf P-Objekte und T-Objekte angewendet werden soll, ist nicht klar geregelt.

**Wo war es unklar:**
Die Grenze zwischen "identischer Kausalstruktur, unterschiedlicher Kontext" (erweitern) und "grundlegend anderer Kausalstruktur" (neu anlegen) ist in einigen Grenzfällen unklar. Beispiel: Ist MEC-0009 (Perzeptueller Kontrast) grundlegend anders als MEC-0002 (Verlustaversion/Status-quo-Kosten)? Beide betreffen relative Wertwahrnehmung. Diese Entscheidung wurde im Rahmen von TASK-0005 getroffen, aber die Begründung "grundlegend andere Kausalstruktur" wäre bei einem anderen Analysten möglicherweise anders ausgefallen.

**Fehlende Regeln:**

- "Nicht-Anlage"-Entscheidungen müssen dokumentiert werden, nicht nur EXTEND/NEW.
- CKM-Anwendung auf P-Objekte und T-Objekte explizit regeln.

---

## Phase 10 — Validierung (TASK-0009)

**Was hat gut funktioniert:**
VAL-0002 war schnell durchführbar, weil die Prüfungen mechanisch sind (Datei vorhanden? Source-ID vorhanden? Multi-Quellen-Anforderung erfüllt?). Der Bash-Script-Ansatz (Dateianzahl prüfen, grep auf MEC-IDs und A-IDs) ermöglichte objektive Prüfungen.

**Probleme:**

- VAL-0002 liegt in `00_project/` statt in einer quellenspezifischen Struktur. VAL-0001 liegt auch dort — aber eigentlich handelt es sich um quellspezifische Validierungen. Konsistenter wäre `04_book_analysis/Influence/VAL-0002.md`.
- Eine externe Validierung (Gemini für Replikationsstatus, Perplexity für B2B-Belege) fehlt als Pflichtschritt. Das ist bekannt und als "ausstehend" dokumentiert.
- Die VAL-Phase ist der Schritt, bei dem die Kapitelstatustabelle in analysis.md hätte geprüft und korrigiert werden sollen — wurde nicht explizit als VAL-Prüfpunkt definiert.

**Fehlende Regeln:**

- VAL-Objekte sollten entweder konsequent in `00_project/` (als projektweite Reviews) oder in `04_book_analysis/[Buch]/` (als quellspezifische Reviews) liegen. Entscheidung fehlt.
- Ein "Externe Validierung ausstehend"-Flag direkt im VAL-Objekt würde spätere Nachverfolgung erleichtern.
- Kapitelstatus-Korrektheit als expliziter VAL-Prüfpunkt aufnehmen.

---

## Phase 11 — Repository Health Check

**Was hat gut funktioniert:**
Der Bash-basierte Schnellcheck (Dateianzahl, ID-Konsistenz, Source-ID-Präsenz) funktionierte gut und war in wenigen Minuten durchführbar.

**Probleme:**

- Der Repository Health Check ist kein formaler Schritt im aktuellen Workflow. Er wurde ad hoc im Rahmen von VAL-0002 durchgeführt. Es gibt kein explizites Health-Check-Protokoll.
- Einige strukturelle Inkonsistenzen wurden gefunden (CLAUDE_BOOTSTRAP.md vs. PROJECT_BOOTSTRAP.md, Kapitelstatus "ausstehend"), aber nicht als eigener Schritt adressiert.

**Fehlende Regeln:**
Ein formaler Repository Health Check als Teil von TASK-0009/VAL sollte standardisiert werden: ID-Lücken prüfen, verwaiste Referenzen prüfen, Dateigröße-Anomalien prüfen, Sprachpolitik-Stichprobe, Kapitelstatus-Vollständigkeit.

---

## Phase 12 — Abschlussbericht (TASK-0010)

**Was hat gut funktioniert:**
BOOK_REVIEW_REPORT_B0002.md ist das erste standardisierte Abschlussdokument für eine Buchanalyse. Es deckt alle wesentlichen Dimensionen ab: Objektmenge, Hauptthese, Codex-Beitrag, Evidenzlage, Grenzen, Folgeempfehlungen, Qualitätsstatus.

**Probleme:**

- Es gibt kein BOOK_REVIEW_REPORT-Template. Das Format wurde ad hoc aus dem Inhalt entwickelt und an PILOT_001_ABSCHLUSSBERICHT.md angelehnt. Ohne Template besteht Inkonsistenzrisiko für B-0003.
- Der Abschlussbericht liegt in `04_book_analysis/Influence/` — korrekt. Aber PILOT_001_ABSCHLUSSBERICHT liegt in `00_project/`. Inkonsistente Ablage.

**Fehlende Regeln:**

- BOOK_REVIEW_REPORT-Template in `01_framework/08_templates/` anlegen.
- Einheitlicher Ablageort: `04_book_analysis/[Buch]/` für quellspezifische Abschlussberichte.

---

## Architekturreview

**Ist die Repositorystruktur sinnvoll?**
Grundsätzlich ja. Die Trennung von `00_project/`, `01_framework/`, `02_sources/`, `03_knowledge_base/`, `04_book_analysis/` ist logisch und hat sich in der Praxis bewährt.

**Ordner, die sich als unnötig erwiesen haben:**

- `05_publications/` — nie verwendet
- `06_media/` — nie verwendet
- `07_scripts/` — einmalig für Python-Skript, aber kein dauerhafter Nutzen
- `99_archive/` — nie verwendet

Diese Ordner erzeugen keinen Schaden, aber sie erhöhen die kognitive Last beim Repository-Einlesen. PROJECT_BOOTSTRAP.md muss sie erwähnen, auch wenn sie leer sind.

**Templates, die nie verwendet wurden:**

- model_template.md (falls vorhanden — nicht explizit referenziert)
- principle_template.md wird zwar referenziert, aber in der Praxis weicht P-0007 deutlich vom Template ab — das Template scheint eher als Orientierung denn als strenge Vorlage genutzt zu werden.

**Dokumente mit überschneidender Verantwortung:**

- `CLAUDE_BOOTSTRAP.md` vs. `PROJECT_BOOTSTRAP.md`: Zwei Boot-Dokumente für KI-Sessions. CLAUDE_BOOTSTRAP.md ist jetzt veraltet.
- `00_project/SALES_CODEX_OPERATING_MANUAL.md` und `00_project/COWORK_EXECUTION_PROTOCOL.md`: Beide beschreiben operative Abläufe. Im Influence-Durchlauf wurden beide praktisch nie gelesen. Die tatsächliche Arbeitsgrundlage war task_rules.md + Herausgeber-Anweisungen im Chat.
- `00_project/roadmap.md` und `00_project/backlog.md`: Beide beschreiben geplante Arbeit. roadmap.md wurde nie referenziert; backlog.md war die operative Grundlage.
- `00_project/review_queue.md`: Nie verwendet.
- `00_project/decision_log.md`: Nie aktiv während Influence genutzt — Entscheidungen wurden direkt in den MEC-Objekten dokumentiert.

**Vereinfachungspotenzial:**

1. `05_publications/`, `06_media/`, `07_scripts/`, `99_archive/` könnten entfernt oder kollabiert werden.
2. `CLAUDE_BOOTSTRAP.md` kann durch `PROJECT_BOOTSTRAP.md` ersetzt werden.
3. `roadmap.md` und `review_queue.md` werden nicht verwendet und könnten archiviert werden.
4. Operating Manual und Execution Protocol könnten zu einem einzigen WORKFLOW.md zusammengefasst werden.

---

## Canonical Knowledge Model Review

**Hat das CKM Duplikate verhindert?**
Ja — direkt beobachtbar. Drei MECs wurden erweitert statt verdoppelt. Ohne CKM wären wahrscheinlich "Selbstbild-Update durch Commitment" (als neuer MEC neben MEC-0001) und "Knappheits-Reaktanz" (als neuer MEC neben MEC-0003) entstanden.

**Hat es Entscheidungen erleichtert?**
Teilweise. Die Entscheidungslogik (Kausalstruktur identisch? Kontext identisch?) ist hilfreich, aber nicht immer eindeutig genug. Grenzfälle erforderten Urteilsvermögen, das durch das CKM allein nicht vollständig strukturiert war.

**Wo war es unklar:**

- "Grundlegend andere Kausalstruktur" ist interpretierbar. MEC-0009 (Kontrast) und MEC-0002 (Verlustaversion) überlappen in der Wertwahrnehmungslogik — die Abgrenzung wurde pragmatisch getroffen.
- Die Anwendung des CKM auf P-Objekte und T-Objekte ist im CKM-Text nicht explizit geregelt, wurde aber implizit angewendet.
- "Nicht-Anlage"-Entscheidungen sind nicht Teil des CKM-Rahmens.

**Welche Regeln sollten ergänzt werden:**

1. "Nicht-Anlage"-Dokumentation: Explizite Regel, dass bewusst verworfene Kandidaten dokumentiert werden müssen.
2. Anwendungsbereich: CKM gilt für ST, A, MEC, P, T, MOD — oder nur für MEC? Explizit regeln.
3. Granularitätsschwelle: Ab welchem Ähnlichkeitsgrad ist eine Zusammenführung zu prüfen? Aktuell implizit.

---

## Arbeitsablauf-Review: Task-basiert vs. Book Mode

**Was hat im task-basierten Workflow gut funktioniert:**

- Klare Granularität: Jeder Task hat eine definierte Eingabe und Ausgabe.
- Gute Nachvollziehbarkeit im backlog.md.
- Herausgeber-Freigaben haben methodische Verbesserungen eingebracht (n:m-Clustering, Abgrenzungspflicht).

**Was hat nicht gut funktioniert:**

- Zu viele Zwischenfreigaben: TASK-0003, 0004, 0005 hatten je eigene Freigaberunden. Das hat Token und Zeit gekostet, ohne dass die Qualität der Einzelergebnisse davon abhing.
- Die Freigaben für TASK-0003 bis TASK-0005 haben zwar methodische Regeln mitgebracht, aber diese Regeln hätten ebenso gut vor TASK-0003 als globale Regeln kommuniziert werden können.
- Der task-basierte Workflow hat keine Abbruchbedingungen explizit definiert — was dazu führte, dass die KI bei jeder normalen Unsicherheit pausierte.

**Book Mode — Was übernommen werden sollte:**

- Keine Zwischenfreigaben innerhalb einer Buchanalyse (außer expliziten Abbruchbedingungen).
- NEXT_ACTION.md als single point of entry für den nächsten Schritt.
- BOOK_REVIEW als definierter Endstatus.
- Vollständiger Workflow in einer Session oder nachvollziehbar übertragbar via CURRENT_STATE.md.

**Was nicht übernommen werden sollte:**

- Das Konzept "Task-Freigabe" komplett abschaffen: Es ist sinnvoll, die erste Freigabe zu haben (Task-Proposal) und eine letzte (Post-Mortem/Review). Die mittleren Freigaben können entfallen, wenn die methodischen Regeln vorab etabliert sind.
- Ein vollständig sequenzieller Workflow ohne jede Rückkopplungsmöglichkeit wäre zu starr.

**Risiken:**
Ohne Zwischenfreigaben besteht das Risiko, dass methodische Fehler (z.B. falsche Canonicalisierung) erst beim Post-Mortem entdeckt werden — dann sind viele abhängige Objekte betroffen. Mitigation: Explizitere Abbruchbedingungen + VAL-Schritt vor BOOK_REVIEW als Qualitätsfilter.

---

## Stateless Architecture Review

**Hat sie funktioniert?**
Ja — in dem Maße, in dem sie eingeführt wurde. Die Architektur-Dateien waren am Ende der Session alle korrekt befüllt. Für die nächste Session ist das Einlesen von PROJECT_BOOTSTRAP.md + CURRENT_STATE.md + NEXT_ACTION.md ausreichend, um die Arbeit fortzusetzen.

**Welche Dateien wurden tatsächlich benötigt:**

- CURRENT_STATE.md (nach Update) — zentral für Zustandsübertragung.
- 00_project/NEXT_ACTION.md — klare Handlungsanweisung.
- 04_book_analysis/Influence/analysis.md — Koordinationsdokument für alle Influence-Arbeit.
- 00_project/backlog.md — Statusverfolgung.
- Die direkt bearbeiteten Templates und Objekte.

**Welche Dateien wurden nie gelesen:**

- SALES_CODEX_OPERATING_MANUAL.md
- COWORK_EXECUTION_PROTOCOL.md
- roadmap.md
- review_queue.md
- VISION.md
- INDEX.md
- SETUP.md
- CONTRIBUTING.md
- agent_protocols/ (bis auf initialen Überblick)

**Welche Dateien sollten Pflicht sein (beim Session-Start):**

1. `PROJECT_BOOTSTRAP.md`
2. `CURRENT_STATE.md`
3. `00_project/NEXT_ACTION.md`
4. Die direkt betroffenen Arbeitsdateien.

**Was noch fehlt:**
Ein SESSION_START-Protokoll ("Lies diese 3 Dateien, dann die betroffenen Arbeitsdateien, dann beginne") existiert jetzt implizit in PROJECT_BOOTSTRAP.md. Es wäre sinnvoll, dies als explizite erste Zeile im NEXT_ACTION.md zu führen.

---

## Priorisierte Empfehlungen

### Priorität A — Unbedingt in v1.1 übernehmen

**A1 — Book Mode offiziell einführen**
- Begründung: Der Influence-Durchlauf hat bewiesen, dass ein vollständiger Workflow ohne Zwischenfreigaben funktioniert. Die Qualität war höher als bei Pilot-001.
- Nutzen: 40–60% weniger Interaktionsaufwand pro Buch; reproduzierbarerer Workflow.
- Aufwand: Gering — Regel in OPERATING_MANUAL und task_rules.md dokumentieren.
- Betroffene Dateien: SALES_CODEX_OPERATING_MANUAL.md, task_rules.md, COWORK_EXECUTION_PROTOCOL.md.

**A2 — BOOK_REVIEW_REPORT-Template anlegen**
- Begründung: Ohne Template wird das nächste Abschlussdokument inkonsistent sein.
- Nutzen: Standardisierte Ausgabe; leichter vergleichbar über Bücher hinweg.
- Aufwand: Gering — Template aus BOOK_REVIEW_REPORT_B0002.md ableiten.
- Betroffene Dateien: `01_framework/08_templates/book_review_template.md` (neu).

**A3 — "Nicht-Anlage"-Dokumentation als CKM-Pflicht einführen**
- Begründung: Bewusst verworfene MEC-Kandidaten (z.B. Scarcity-as-value-heuristic) sind aktuell nicht formal dokumentiert. Spätere Sessions könnten sie erneut als Kandidaten vorschlagen.
- Nutzen: Verhindert, dass dieselben Entscheidungen mehrfach getroffen werden.
- Aufwand: Gering — Regel im CKM-Dokument ergänzen; optional: "Rejected Candidates"-Abschnitt in analysis.md.
- Betroffene Dateien: CKM-Dokument, analysis.md-Template.

**A4 — CURRENT_STATE.md + NEXT_ACTION.md + SESSION_LOG.md als Pflicht-Abschluss jeder Session**
- Begründung: Die Stateless Architecture funktioniert nur, wenn diese Dateien am Ende jeder Session zuverlässig aktualisiert werden.
- Nutzen: Zuverlässige Übergabe zwischen Sessions; keine Rekonstruktionsarbeit nach Context-Window-Breaks.
- Aufwand: Sehr gering — als letzter Schritt im Book Mode verankern.
- Betroffene Dateien: task_rules.md, NEXT_ACTION.md.

**A5 — Ausgabe-Verifikationspflicht beim Source-Anlegen**
- Begründung: Der Ausgabenfehler (2021 statt 2007) verbreitete sich in mehrere Dateien.
- Nutzen: Verhindert Kaskadenfehler.
- Aufwand: Sehr gering — Pflichtfeld "Ausgabe aus Impressum verifiziert: [Seite X]" in source_template.md ergänzen.
- Betroffene Dateien: `01_framework/08_templates/source_template.md`.

**A6 — OR-Formulierung in der Prinzipien-Regel explizit machen**
- Begründung: "aus mehreren Mechanismen ODER Annahmen" muss explizit in task_rules.md stehen. Aktuell interpretierbar.
- Nutzen: Verhindert falsche Ablehnung valider Prinzipien.
- Aufwand: Minimal — eine Zeile in task_rules.md.
- Betroffene Dateien: `00_project/task_rules.md`.

---

### Priorität B — Sinnvolle Verbesserungen

**B1 — Ablage von VAL-Objekten konsolidieren**
- Begründung: VAL-0001 und VAL-0002 liegen in `00_project/`, aber logisch gehören sie zu den jeweiligen Buchanalysen.
- Empfehlung: VAL-Objekte in `04_book_analysis/[Buch]/` ablegen ab VAL-0003; VAL-0001/0002 als historische Ausnahme belassen.
- Aufwand: Gering.

**B2 — Kapitelstatus-Aktualisierung als Pflichtschritt in TASK-0003**
- Begründung: Kapitelzeilen blieben auf "ausstehend" stehen, auch nach Abschluss.
- Empfehlung: Sub-Schritt am Ende von TASK-0003: "analysis.md Kapitelzeilen auf 'analysiert' setzen."
- Aufwand: Minimal.

**B3 — Redundante Dokumente archivieren**
- CLAUDE_BOOTSTRAP.md → archivieren (ersetzt durch PROJECT_BOOTSTRAP.md).
- roadmap.md → archivieren (nie verwendet).
- review_queue.md → archivieren (nie verwendet).
- decision_log.md → überprüfen ob noch nötig (Entscheidungen leben jetzt in den Objekten und OPEN_DECISIONS.md).
- Aufwand: Gering.

**B4 — Abbruchbedingungen im NEXT_ACTION.md mitführen**
- Begründung: Der erste Blick in NEXT_ACTION.md soll nicht nur die nächste Aktion zeigen, sondern auch die Abbruchbedingungen. Aktuell stehen sie in PROJECT_BOOTSTRAP.md — zwei Klicks entfernt.
- Aufwand: Minimal.

**B5 — T/P-Grenze (Technik vs. Kompetenz) definieren**
- Begründung: Rapport/Ähnlichkeits-Signalisierung wurde als Kompetenz, nicht als Technik klassifiziert — ohne explizite Regel.
- Aufwand: Gering — eine Definition in technique_template.md oder task_rules.md.

**B6 — model_template.md anlegen oder verlinken**
- Begründung: MOD-0002 wurde ohne explizites Template erstellt.
- Aufwand: Gering — MOD-0001 als Basis verwenden.

---

### Priorität C — Ideen für später

**C1 — Cluster-Matrix als A-Objekt-Begleitung**
Ein formales ST→A-Mapping-Dokument pro Buch würde die n:m-Clustering-Entscheidungen dokumentieren und auditierbar machen.
Aufwand: Mittel; Nutzen eher für externe Nachvollziehbarkeit.

**C2 — ID-Counter-Skript**
Ein einfaches Bash-Skript, das die nächste freie ID pro Objekttyp ausgibt, würde Zählfehler eliminieren.
Aufwand: Gering (technisch); Einbettung in Workflow nötig.

**C3 — Gemini-Validierung als eigener Task-Typ (VAL-extern)**
Die externe Validierung des Replikationsstatus von Studien ist aktuell ein "ausstehend"-Vermerk. Sie könnte als eigener Workflow-Schritt (TASK-0009b) nach VAL-intern eingeführt werden.
Aufwand: Mittel; erfordert Konvention, welche Studien validiert werden und wie.

**C4 — Vereinheitlichte Abschluss-Checkliste**
Eine kurze "BOOK_DONE_CHECKLIST.md" (alle Objekte angelegt? VAL durchgeführt? analysis.md vollständig? BOOK_REVIEW erstellt? CURRENT_STATE aktualisiert?) würde den Abschluss eines Buchs absichern.
Aufwand: Gering.

**C5 — Integration von SPIN Selling und Cialdini in einem übergeordneten Modell**
MOD-0003 als integriertes Compliance+Conversation-Modell — wann SPIN-Logik, wann Cialdini-Trigger.
Aufwand: Hoch; hoher konzeptueller Mehrwert.

---

## Gesamtfazit

Der Influence-Durchlauf war der erste produktive Beweis, dass das Sales Codex OS funktioniert. Der Workflow von SRC bis BOOK_REVIEW ist grundsätzlich tragfähig.

**Was den größten Qualitätssprung erzeugt hat:** Die n:m-Clustering-Regel für Annahmen und die Abgrenzungspflicht für Prinzipien. Beide wurden vom Herausgeber als methodische Regeln eingebracht — nicht durch das Framework. Das zeigt, dass das Framework noch zu wenig methodische Tiefe in diese beiden Schritte gibt.

**Was am meisten Zeit kostet:** Zwischenfreigaben und Context-Window-Brüche. Beide sind durch Stateless Architecture und Book Mode adressierbar.

**Was nie verwendet wurde:** Das Operating Manual, das Execution Protocol, die roadmap. Die tatsächliche Arbeit lief über task_rules.md + Herausgeber-Direktanweisungen im Chat + die direkt bearbeiteten Objektdateien.

**Was am wenigsten gesichert ist:** Die Grenze zwischen MEC-Erweiterung und MEC-Neuanlage in Grenzfällen, und die Nicht-Anlage-Entscheidung. Beide brauchen explizitere Regeln.

**Das wichtigste strukturelle Risiko:** Wenn Entscheidungen primär in Chatverläufen getroffen werden (statt in Repository-Dateien), gehen sie verloren. Die Stateless Architecture löst das — aber nur, wenn SESSION_LOG und CURRENT_STATE zuverlässig gepflegt werden.

---

*Dieser Bericht steht unter Freigabevorbehalt. Alle Empfehlungen werden erst nach expliziter Freigabe durch Felix umgesetzt.*
