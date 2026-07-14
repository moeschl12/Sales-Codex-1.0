# AR-009 Completion Report — Ohiomah, Benyoucef & Andreev (2020) Volltextauswertung

**Datum:** 2026-07-14
**Task-Typ:** T11_SCIDEBT (`TASK_TYPES.md`)
**Auftrag:** AR-009 aus `00_project/ACADEMIC_RECOVERY_PLAN.md` — Forschungsfrage: Welche empirisch gestützten Determinanten von B2B-Sales-Erfolg identifiziert Ohiomah et al. (2020), mit welchen Effektstärken/Moderatoren, und welche davon sind für bestehende Sales-Codex-Objekte oder Scientific-Debt-Lücken relevant?
**Ergebnis in einem Satz:** Die Meta-Analyse (139 Studien, 1980–2019) wurde legitim und größtenteils im Volltext gelesen (Einleitung, vollständige Methodik, vollständige Ergebnisse, überwiegender Teil der Diskussion; Tabellen/Fazit/Literaturverzeichnis technisch nicht extrahierbar); sie bestätigt Kundenvertrauen als stärkste B2B-Erfolgsdeterminante (r=0,48, relevant für MEC-0030), bestätigt weder CEB/Challenger (A-0019) noch schließt sie die dokumentierte Generalisierbarkeits-Lücke des Codex — sie schärft sie eher.

---

## 1. Zugriffslage zur Quelle

| Aspekt | Befund |
|---|---|
| Verlagsversion (ScienceDirect, DOI 10.1016/j.indmarman.2020.08.011) | Weiterhin paywalled (Abstract-Ebene), wie bereits in AR-002 dokumentiert. |
| Legitimer Volltextzugriff | **Ja** — University of Ottawa Institutional Repository ("Recherche uO", `ruor.uottawa.ca`), Ohiomahs PhD-Thesis-by-Articles *Lead to Win: Recipes for Inside Sales Success* (2020, DOI 10.20381/ruor-25714), öffentlich und legitim einsehbar. Kapitel 2 der Dissertation ist im Titelblatt explizit als "Author Accepted Manuscript" der Zieljournalpublikation ausgewiesen, mit identischer Zitatangabe (Industrial Marketing Management, 90, 435–452). Analog zum bereits akzeptierten Präzedenzfall AR-013/SRC-0016 (universitätsgehostetes Digitalisat). |
| Zugriffsmethode | Kein Sci-Hub, keine Zugriffsschutz-Umgehung. Ein Versuch, das PDF direkt über die Sandbox-Shell (curl) herunterzuladen, scheiterte an der Netzwerk-Allowlist der Sandbox selbst (nicht an einer Zugriffssperre der Quelle) — es wurde daraufhin nicht weiterversucht, dies zu umgehen. |

## 2. Ob Volltext vollständig gelesen wurde

**Nein — größtenteils, mit dokumentierter technischer Teilzugriffslücke.** Vollständig gelesen: Abstract, Abschnitt 2.1 (Introduction), Abschnitt 2.2 (What is Sales Success?), die vollständige Methodik 2.3.1–2.3.6 (Literatursuche, Coding, Tallying, Effektstärkenmetrik, bivariate Analyse, Moderatoranalyse-Design), die vollständige Ergebnisdarstellung 2.4.1–2.4.3 (Determinanten-Tallying, bivariate Analyse, Moderatoranalyse mit zahlreichen konkreten β-/r-Werten im Fließtext) sowie der überwiegende Teil der Diskussion 2.5.1–2.5.5 (alle vier Dimensionen: Salesperson, Organisation, Kunde, Umfeld) und der Beginn von 2.6/2.7 (Research Contributions, Opportunities for Future Research).

**Nicht gelesen:** das Ende von Abschnitt 2.7, Abschnitt 2.8 (Conclusion and Limitations), das vollständige Literaturverzeichnis des Kapitels, sowie der Inhalt der Tabellen 2.1–2.5 und Abbildung 2.1 (vollständige Liste aller kurzgelisteten/signifikanten Determinanten mit Einzelwerten, vollständige Moderator-Regressionstabelle, Rankingtabelle). Die Tabellen erschienen im abgerufenen Text durchgehend nur als Platzhalter ("Table X Appears here") — dies scheint eine Eigenschaft der PDF-Text-Extraktion selbst zu sein (Tabellen vermutlich als Grafik/Layout-Element eingebettet), nicht ein Effekt der Abruf-Obergrenze. Die Abruf-Obergrenze des verwendeten Fetch-Werkzeugs (ca. 113.000 Zeichen von insgesamt ca. 232 Dissertationsseiten) erklärt zusätzlich, warum der Text nach Abschnitt 2.7 abbricht. Dies ist eine dokumentierte technische Grenze, keine Zugriffsverweigerung durch Verlag oder Universität — der Auftrag verlangt in diesem Fall keinen Abbruch (kein Hard Block, keine "Quelle nicht zugänglich"), sondern Dokumentation der Unsicherheit und Fortsetzung mit dem, was tatsächlich geprüft werden konnte.

## 3. Exakte bibliografische Angaben

Ohiomah, A., Benyoucef, M. & Andreev, P. (2020). A Multidimensional Perspective of Business-to-Business Sales Success: A Meta-Analytic Review. *Industrial Marketing Management*, 90, 435–452. DOI: 10.1016/j.indmarman.2020.08.011. Im Volltext bestätigt (Kapitel-Titelblatt der Primärquelle), inkl. exaktem Titel, Autorenreihenfolge, Jahr, Journal, Band, Seiten und DOI — keine Abweichung von der im Recovery Plan geführten Angabe.

## 4. Methode und Datenbasis

Systematischer Review + Meta-Analyse. Literatursuche in ABI/Inform, Business Source Complete, Scopus, PsycARTICLES sowie gezielt in neun Kernjournalen (u. a. Journal of Marketing, JMR, JAMS, JBR, EJM, Industrial Marketing Management, JPSSM, Journal of Applied Psychology, AMJ), Zeitraum 1980–2019. Initial 1338 Studien, nach Relevanz-Screening (Titel/Abstract, Zwei-Gutachter-Verfahren mit Drittautor als Tie-Breaker) 594, nach Praxis-/Qualitätsscreening (nur B2B-Kontext, nur empirisch validiert, kein B2C/Retail, Ausschluss vorheriger Review-Papers als Primärdaten) 139 Studien für die Kodierung. Zweistufige Analyse: (1) informelles Vote-Counting zur Kurzlistung (Schwelle ≥3 validierte Beziehungen je Determinante), (2) Meta-Analyse der Pearson-Korrelationen mit Hunter-&-Schmidt-(2004)-Random-Effects-Modell (Software MIX 2.0), Fisher-r-zu-z-Transformation, Q-Statistik für Heterogenität. Datenbasis der bivariaten Analyse: 443 Korrelationen aus 140 Stichproben, ca. 29.000 Verkäufer und ca. 5.000 Manager/Supervisor. B2B-Abgrenzung: explizit über Studiendesign (B2B-Verkäufer/-Manager als Respondenten) statt Branchenklassifikation, mit explizitem Ausschluss von Retail-/B2C-Studien.

## 5. Wichtigste Determinanten und Effektstärken

- 35 kurzgelistete Determinanten, davon **31 signifikant** korreliert mit B2B-Vertriebserfolg (p<0,05), alle positiv außer Rollenambiguität (r=−0,23, einzige negative).
- **Nicht signifikant:** Geschlecht, Ausbildung, Rollenkonflikt, Wettbewerbereinfluss.
- **Stärkste Einzelkorrelationen:** Kundenvertrauen (r=0,48, insgesamt stärkste), Salesmanship-Fähigkeiten (r=0,44), interpersonelle Fähigkeiten (r=0,40), technische Fähigkeiten (r=0,40).
- Nach Cohen (1969): 21 Determinanten mit geringer (0,10<|r|<0,30), 9 mit mittlerer Effektstärke (0,30<|r|<0,50) — keine mit großer Effektstärke.
- Vier Dimensionen: Salesperson (am häufigsten untersucht; strukturiert über eine Kompetenz-Typologie nach Le Deist & Winterton 2005: kognitiv, funktional, sozial, Meta-Kompetenz), Organisation (u. a. Kontrollsysteme, Technologienutzung, Support, Training, Leadership, Supervisee-Trust), Kunde (Zufriedenheit, Vertrauen, Beziehungsqualität), Umfeld (Wettbewerb, Markt-/Technologiedynamik — am wenigsten untersucht).
- Vollständige Einzelwerte für alle 31 Determinanten liegen NICHT vor (Tabellen nicht extrahierbar) — nur die im Fließtext explizit benannten Werte wurden übernommen (siehe ST-0323/ST-0324).

## 6. Relevante Moderatoren / Kontextbedingungen

Sechs geprüfte Moderatoren: Selbst- vs. Managereinschätzung, subjektiv vs. objektiv, Einzel- vs. Mehrfach-Item-Messung, Güter- vs. Dienstleistungsvertrieb, Einzel- vs. Mehrfachbranche, Inside- vs. Outside-Sales, Publikation vor/nach 2010. Nur Determinanten mit mindestens 30:70-Gruppenverteilung wurden je Moderator ausgewertet (vier Determinanten insgesamt ausgeschlossen wegen zu geringer Varianz). Im Volltext vollständig mit Einzelwerten dokumentiert: alle sechs Moderatoren-Unterabschnitte (2.4.3). Detailliert extrahiert (ST-0326): Inside- vs. Outside-Sales — u. a. stärkere Korrelation von Beziehungsqualität (β=0,73), Organisationsunterstützung (β=0,83), Technologienutzung (β=0,53) bei Remote-Vertrieb; schwächere Korrelation von Adaptive Selling (β=−0,24), Capability Control (β=−0,61), Selbstwirksamkeit (β=−0,37) bei Remote-Vertrieb.

## 7. Betroffene bestehende Codex-Objekte

- **MEC-0030 (Vertrauensbildung aus wahrgenommener Vertrauenswürdigkeit):** direkt betroffen. Ohiomah et al. (2020) aktualisiert die dort dokumentierte Lücke ("seither keine aktualisierende Meta-Analyse identifiziert" seit Swan et al. 1999) mit einer neuen, größeren, B2B-spezifischen Bestätigung der Trust-Erfolgs-Korrelation. Neuer Abschnitt "AR-009-Ergänzung" ergänzt — **kein Evidenzlevel-Wechsel** (bleibt E2–E3 für den Sales-Transfer), da die Quelle die Outcome-Korrelation, nicht das ABI-Kausalmodell der Trust-Bildung selbst testet.
- **A-0019 / P-S1-003 / SD-SYS-001 (CEB-Kundenloyalität/Challenger):** indirekt betroffen, im Sinne einer Nicht-Bestätigung. Kein CEB-, Challenger- oder Tethr-Bezug im gelesenen Volltext. Konsistent mit dem bereits zu Verbeke, Dietz & Verwaal (2010/2011) dokumentierten Befund: andere Analyseebene, keine Bestätigung des 53%-Splits oder der Challenger-Taxonomie. SD-SYS-001 bleibt für A-0019 offen.
- **MEC-0013, MEC-0014:** geprüft, kein direkter inhaltlicher Bezug im gelesenen Text gefunden (keine Reframing-, Buying-Center- oder Principal-Agent-Diskussion in Kapitel 2) — keine Änderung vorgenommen.
- **Generalisierbarkeits-Schwäche (Reifegradbericht 1.5, C+):** Die Quelle bestätigt eher die Lücke, als sie zu schließen. Der Sales-Codex-Mechanismenbestand ist überwiegend aus käuferpsychologischer/verhandlungspsychologischer Literatur (Kahneman, Cialdini u. a.) abgeleitet; Ohiomah et al. decken eine strukturell andere Literatur ab (Verkäuferkompetenz-, Organisations- und Vertriebsmanagementforschung). Außer beim Kundenvertrauen (MEC-0030) besteht für die übrigen 30 signifikanten Determinanten (z. B. Adaptive Selling, Customer Orientation, Self-Efficacy, Organisationskontrollsysteme, Leadership, Supervisee-Trust) **kein** bestehendes Codex-MEC/P/T-Objekt. Dies ist ausdrücklich als offene, nicht aufgelöste Lücke dokumentiert — es wurde bewusst **keine** neue Taxonomie oder ein neues übergreifendes B2B-Erfolgsmodell angelegt (Auftragsvorgabe).

## 8. Neue Statements

Vier neue source-grounded Statements (`03_knowledge_base/statements/`), direkt aus dem gelesenen Primärtext:

- **ST-0323** — Meta-Analyse-Scope und Methodik (139 Studien, 1980–2019, zweistufiges Vote-Counting + Random-Effects-Meta-Analyse, 31 signifikante Determinanten in vier Dimensionen).
- **ST-0324** — Bivariate Effektstärken: 31/35 signifikant, Kundenvertrauen (r=0,48) stärkste, Rollenambiguität (r=−0,23) einzige negative, vier nicht-signifikante Determinanten, Cohen-Klassifikation (21 gering/9 mittel).
- **ST-0325** — Kundenvertrauen als stärkster Einzelprädiktor; explizite Analyseebenen-Abgrenzung zu MEC-0030 (Outcome-Korrelation vs. Trust-Bildungsmechanismus).
- **ST-0326** — Inside- vs. Outside-Sales-Moderatoreffekte mit konkreten β-Werten für acht Determinanten.

Keine neuen A-, P-, MOD- oder T-Objekte (Auftragsvorgabe: keine neue Taxonomie, Scope-Disziplin). Keine Änderung an A-0019 selbst (nur dokumentierte Nicht-Bestätigung in SCIENTIFIC_DEBT.md und diesem Bericht).

## 9. Offene Lücken / Editorentscheidungen

- **Vollständige Tabellenintegration** (alle 31 Determinanten mit Einzelwerten, vollständige Moderator-Regressionstabelle, Rankingtabelle Table 2.5) ist offen — abhängig von einem vollständigeren Volltextabruf (z. B. Direktzugriff auf das PDF ohne die hier aufgetretene technische Abruf-Obergrenze). Nicht Gegenstand einer Editorentscheidung, sondern eine technische Folgeaufgabe für eine künftige Sitzung.
- **Abschnitt 2.8 (Conclusion/Limitations) und Literaturverzeichnis** ungelesen — falls dort zusätzliche, hier nicht erfasste Limitationen oder Zitationen stehen, sind diese nicht in diesen Bericht eingeflossen.
- **MEC-0030-Evidenzlevel:** Keine Änderung vorgenommen. Ob die jetzt dokumentierte, aktualisierte Trust-Erfolgs-Korrelation (Ohiomah et al. 2020) Anlass für eine Editorentscheidung zur Anhebung des Sales-Transfer-Evidenzlevels (aktuell E2–E3) gibt, ist ausdrücklich **nicht** in dieser Session entschieden worden — eine mögliche Empfehlung, aber keine Umsetzung.
- **Generalisierbarkeits-Lücke (C+):** bleibt offen. Ob und wie die 30 nicht direkt Codex-gestützten Determinanten (Adaptive Selling, Customer Orientation etc.) künftig als eigenständige MEC-Kandidaten geprüft werden sollen, ist eine Herausgeberentscheidung außerhalb des AR-009-Scopes (keine neue Taxonomie in dieser Session).

## 10. Geänderte/neu angelegte Dateien

**Neu (5):** ST-0323, ST-0324, ST-0325, ST-0326 (`03_knowledge_base/statements/`); dieser Bericht (`00_project/AR-009_COMPLETION_REPORT.md`).

**Geändert (5):** `02_sources/studies/SRC-0022_ohiomah_et_al_2020_b2b_sales_success.md` (vollständig überarbeitet: Quellenklasse A formal vergeben, Bearbeitungsstatus "Analysiert", vollständiges Zugriffsprotokoll, zentrale Aussagen, Grenzen); `03_knowledge_base/mechanisms/MEC-0030_vertrauensbildung_aus_wahrgenommener_vertrauenswuerdigkeit.md` (neuer Abschnitt "AR-009-Ergänzung", kein E-Level-Wechsel); `05_research/LITERATURE_INDEX.md` (Sektion H, Ohiomah-Zeile aktualisiert); `00_project/SCIENTIFIC_DEBT.md` (Status-Update-Absatz zur SD-SYS-001/Generalisierbarkeits-Zeile ergänzt, Originalzeile nicht gelöscht); `00_project/ACADEMIC_RECOVERY_PLAN.md` (AR-009-Status-Update).

**Nicht geändert (auftragsgemäß):** Evidenzlevel von MEC-0030, A-0019 selbst, Completed-W-Dateien, Templates/Framework, andere MECs/Prinzipien/Techniken, keine neue Taxonomie. Kein Commit, kein Push.

## 11. Durchgeführte Prüfungen

1. **Pflichtstart:** `PROJECT_BOOTSTRAP.md`, `SESSION_BRIEF.md`, `00_project/NEXT_ACTION.md` vollständig gelesen; `TASK_TYPES.md` gezielt nach dem passenden Task-Typ durchsucht (T11_SCIDEBT identifiziert und dessen Routing-Vorgaben befolgt).
2. **AR-009-Abschnitt** in `ACADEMIC_RECOVERY_PLAN.md` gezielt gelesen (kein rekursiver Scan).
3. **Duplikatsprüfung vor Recherche:** Repository-weite gezielte Suche nach "Ohiomah" bestätigte, dass SRC-0022 bereits existiert (Abstract-Ebene aus AR-002/ARS-0001) sowie Referenzen in `LITERATURE_INDEX.md`, `SCIENTIFIC_DEBT.md`, `ACADEMIC_RECOVERY_PLAN.md` und weiteren Berichten. Keine ST-, A-, MEC-, P-, MOD- oder T-Objekte zu dieser Quelle vorgefunden — keine Duplikate angelegt, bestehendes SRC-0022 erweitert statt neu angelegt.
4. **Legitimer Zugriffsweg recherchiert und dokumentiert** (siehe Punkt 1) — externe Websuche zur Quellenverifikation gemäß T11-Routing, kein Rückgriff auf interne Volltextsuche als Ersatz für Recherche.
5. **Primärtextlektüre so vollständig wie technisch möglich**, mit expliziter Dokumentation der verbleibenden Lücke (Tabellen, Fazit, Literaturverzeichnis) statt stillschweigender Glättung — Abstract-only wurde nicht als ausreichend behandelt (Auftragsvorgabe eingehalten).
6. **Differenzierungsprüfung gemäß Auftrag ("Besonders sauber unterscheiden"):** B2B-Sales-Erfolg allgemein vs. individuelle Verkäuferperformance vs. organisationale Sales-Performance vs. Käuferpsychologie vs. Sales-Process-/Relationship-Determinanten wurde bei der Zuordnung zu den vier Dimensionen (Salesperson/Organisation/Kunde/Umfeld) beachtet; empirische Effektstärke (r/β-Werte) wurde durchgängig von rein theoretischer Relevanz unterschieden (z. B. explizite QK-Ratings und Evidenzklassen in allen vier Statements); direkte Codex-Stützung (MEC-0030) wurde von reiner Kontext-/Generalitätsstützung (die übrigen 30 Determinanten) klar getrennt (Punkt 7 oben).
7. **Explizite Prüfung des CEB-/Challenger-Verbots:** Der gesamte gelesene Volltext wurde auf Erwähnungen von CEB, Challenger, Tethr oder vergleichbaren proprietären Verkäufer-Typologien geprüft — keine gefunden. A-0019 wurde entsprechend NICHT als repliziert dargestellt (Auftragsvorgabe strikt eingehalten).
8. **Zitatverifikation:** Alle in den Statements und diesem Bericht verwendeten Zahlen (r-Werte, β-Werte, p-Werte, Stichprobengrößen) direkt aus dem gelesenen Volltext übernommen, keine aus Gedächtnis oder Sekundärquelle ergänzt.
9. **Scope-/Regel-Check am Ende:** keine Evidenzlevel-Änderung, keine neue Taxonomie, keine vollständige Übernahme aller 139 Einzelstudien, keine Verknüpfung bestehender Objekte durch bloße thematische Nähe (MEC-0013/MEC-0014-Prüfung ergab explizit "kein direkter Bezug", keine erzwungene Verknüpfung), AR-001 bis AR-008 nicht nachbearbeitet, keine Completed-W-Dateien angefasst, kein Commit/Push, keine rekursive Breitsuche außerhalb der erlaubten Verzeichnisse.

---

*Erstellt: 2026-07-14 | AR-009 | T11_SCIDEBT | KI-Redaktion Sales Codex (Claude)*
