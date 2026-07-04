# Codex Consistency Correction Report 2026-07

**Dokumentklasse:** Operational / Reference
**Sprint:** Consistency Correction Sprint (Meilenstein 1 aus `CODEX_AUDIT_2026-07.md`, Kapitel 11)
**Datum:** 2026-07
**Auftrag:** Ausschließlich Meilenstein 1 des Audits umsetzen — keine neue Recherche, keine neuen Wissensobjekte, keine Framework-Änderungen, keine neuen Bücher.
**Grundregel dieses Sprints:** Jede Änderung ist eine Konsistenzkorrektur, keine inhaltliche Neubewertung. Wo eine echte inhaltliche Bewertung nötig gewesen wäre, wurde sie **nicht** vorgenommen, sondern als Empfehlung dokumentiert.

---

## 1. T-0012 und T-0013 — Evidenzlevel-Synchronisation

**Befund (Audit Kapitel 3):** T-0012 (Mirroring) und T-0013 (Labeling) trugen weiterhin E3, obwohl ihre jeweiligen Basismechanismen MEC-0011 (Neural Coupling) und MEC-0010 (Amygdala-Regulation) bereits am 2026-07-01 per Peer Review Sprint 1 von E3 auf E2 herabgestuft wurden (`PEER_REVIEW_DECISION_REPORT_SPRINT_001.md`). Die Korrektur wurde damals nicht an die abhängigen Technik-Objekte weitergegeben.

**Durchgeführt:**
- `T-0012_mirroring.md`: Evidenzlevel E3 → **E2**, mit Verweis auf MEC-0011 und Erklärung der Desynchronisation.
- `T-0013_labeling.md`: Evidenzlevel E3 → **E2**, mit Verweis auf MEC-0010 und Erklärung der Desynchronisation.

Beide Änderungen sind reine Zahlenkorrekturen. Die ursprüngliche, inhaltlich zutreffende Begründung (Lieberman 2007 bzw. Stephens/Hasson 2010, Voss-Praxis, kein direkter Verhandlungstest) wurde unverändert übernommen und lediglich um den Korrekturvermerk ergänzt. Keine neue Quelle, keine neue Bewertung — die Einstufung folgt vollständig der bereits in den Basismechanismen getroffenen und dokumentierten Entscheidung.

---

## 2. Fehlende Evidenzfelder — Ergänzung bei 28 Objekten

**Befund (Audit Kapitel 3):** 12 Techniken (T-0019, T-0020, T-0021, T-0026–T-0034) und 8 Prinzipien (P-0027–P-0034) hatten überhaupt kein Evidenzklassifikations-Feld. Zusätzlich hatten 4 Techniken (T-0022–T-0025) ein Feld unter abweichendem Namen („Evidenzgrad"). Die 4 Meta-Prinzipien (P-S1-001–004) wurden im Audit ebenfalls als „fehlend" gelistet.

**Methodisches Problem und wie es gelöst wurde:** Eine echte Evidenzeinstufung für ein Technik- oder Prinzipien-Objekt (z. B. „ist die sechsschrittige Commercial-Teaching-Sequenz selbst empirisch getestet, nicht nur der zugrunde liegende Mechanismus?") ist eine inhaltliche Bewertung — genau das, was dieser Sprint explizit **nicht** leisten soll („keine inhaltliche Neubewertung über den Audit hinaus"). Für die 20 tatsächlich leeren Objekte (12 T + 8 P) wurde daher **keine neue Evidenzzahl erfunden**. Stattdessen wurde bei jedem Objekt ein Feld ergänzt, das:

1. explizit festhält, dass kein eigenständiges Evidenzlevel vergeben wurde,
2. die bereits im Objekt selbst verlinkten Mechanismen/Annahmen mit ihren **bereits bestehenden, unverändert übernommenen** Evidenzwerten auflistet (reine Cross-Referenz, keine neue Recherche),
3. explizit auf diesen Audit und Sprint verweist,
4. eine künftige inhaltliche Bewertung als Empfehlung dokumentiert statt sie selbst vorzunehmen — gemäß der Regel „Wenn eine Änderung nicht sicher möglich ist, dokumentiere sie als Empfehlung statt sie umzusetzen".

### 2.1 Techniken — neu ergänzt (12 Objekte)

| Objekt | Verlinkte Objekte mit bestehendem Evidenzlevel |
|---|---|
| T-0019 (Commercial Teaching Pitch) | MEC-0013 (E3), MEC-0002 (E4) |
| T-0020 (Stakeholder-Tailoring) | MEC-0014 (E3), MEC-0013 (E3) |
| T-0021 (Prozessausstieg/RFP-Exit) | MEC-0003 (E4), MEC-0002 (E4) |
| T-0026 (JOLT-J, Judge the Indecision) | MEC-0016 (E4), MEC-0015 (E5), A-0030 (E2) |
| T-0027 (JOLT-O, Offer Your Recommendation) | MEC-0015 (E5), MEC-0016 (E4), MEC-0008 (E4) |
| T-0028 (JOLT-L, Limit the Exploration) | MEC-0008 (E4), MEC-0015 (E5), A-0034 (E2) |
| T-0029 (JOLT-T, Take Risk Off the Table) | MEC-0016 (E4), MEC-0003 (E4), A-0031 (E2), A-0033 (E2) |
| T-0030 (Buyer's Agent Positionierung) | MEC-0008 (E4), MEC-0007 (E4) |
| T-0031 (BATNA-Entwicklung) | A-0038 (E3), MEC-0002 (E4) |
| T-0032 (Interessen-Exploration) | MEC-0017 (E4), A-0036 (E3) |
| T-0033 (Negotiation Jujitsu) | MEC-0003 (E4), MEC-0010 (E2) |
| T-0034 (Objective Criteria Framing) | MEC-0012 (E4), MEC-0017 (E4) |

### 2.2 Techniken — Feldname harmonisiert, Wert unverändert (4 Objekte)

T-0022, T-0023, T-0024, T-0025 (alle Gap Selling): Header „Evidenzgrad" → „Evidenzlevel". E-Wert (jeweils E2) und Begründungstext vollständig unverändert übernommen — reine Namenskorrektur mit Vermerk.

### 2.3 Prinzipien — neu ergänzt (8 Objekte)

| Objekt | Verlinkte Objekte mit bestehendem Evidenzlevel |
|---|---|
| P-0027 (Entscheidungsfähigkeits-Qualifikation) | A-0030 (E2), MEC-0016 (E4) |
| P-0028 (Empfehlung statt Optionen) | MEC-0015 (E5), MEC-0016 (E4), A-0032 (E4) |
| P-0029 (Informationsfluss kontrollieren) | MEC-0008 (E4), A-0034 (E2) |
| P-0030 (Risikoabbau statt Risikoaktivierung) | MEC-0016 (E4), MEC-0003 (E4), A-0031 (E2), A-0033 (E2) |
| P-0031 (Interessen statt Positionen) | MEC-0017 (E4), A-0036 (E3) |
| P-0032 (Objektive Kriterien) | MEC-0012 (E4), MEC-0003 (E4) |
| P-0033 (BATNA kennen und entwickeln) | A-0038 (E3) |
| P-0034 (Menschen vom Problem trennen) | A-0037 (E3), MEC-0010 (E2) |

Neuer Feldname: „## Evidenzklassifikation" — die im Repository am häufigsten verwendete Formulierung für Prinzipien (u. a. P-0001–P-0021).

### 2.4 Meta-Prinzipien P-S1-001 bis P-S1-004 — Korrektur des Audit-Befunds selbst

**Wichtige Richtigstellung:** Bei genauer Prüfung hatten alle vier Meta-Prinzipien bereits ein vollständiges Evidenzlevel — nicht als Markdown-Abschnitt, sondern im **YAML-Frontmatter** jeder Datei (Feld `e_level:`). Der Audit `CODEX_AUDIT_2026-07.md` hatte diese Objekte fälschlich als „ohne Evidenzfeld" gelistet, weil die damalige Prüfung ausschließlich nach Markdown-Überschriften (`## Evidenz...`) gesucht und YAML-Frontmatter nicht erfasst hatte. Dies ist eine Methodik-Lücke des Audits selbst, kein tatsächliches Content-Defizit der vier Objekte.

**Durchgeführt:** Bei allen vier Objekten wurde ein zusätzlicher, menschenlesbarer Abschnitt „## Evidenzklassifikation" ergänzt, der den bereits bestehenden Frontmatter-Wert **unverändert spiegelt** (keine neue Bewertung) und diese Richtigstellung explizit dokumentiert:

| Objekt | Bestehender `e_level` (Frontmatter, unverändert) |
|---|---|
| P-S1-001 | E4 (MEC-0002) + E2 (methodologische Konvergenz, QK-5) |
| P-S1-002 | E4 (MEC-0004, Labor) + E2 (methodologische Konvergenz, QK-4) |
| P-S1-003 | E3 (CEB-Studie, B-0004) + E2 (methodologische Konvergenz, QK-4) |
| P-S1-004 | E5 (Miller's Law) + E2 (methodologische Konvergenz, QK-4) |

**Konsequenz für den Audit:** `CODEX_AUDIT_2026-07.md` bleibt als historisches Dokument unverändert (siehe Grundsatz „nicht rückwirkend schönschreiben" in Abschnitt 4 dieses Berichts). Diese Richtigstellung wird hier und in den vier betroffenen Objekten selbst festgehalten.

---

## 3. Feldbenennung — Vereinheitlichung im Rahmen des Sprint-Scopes

**Entscheidung zum Geltungsbereich:** Der Auftrag verlangt „Feldbenennung vereinheitlichen, soweit ohne Framework-Änderung möglich" als Teil von Meilenstein 1, der explizit auf die Objektliste T-0012/T-0013, T-0019–T-0034, P-0027–P-0034, P-S1-001–004 begrenzt ist. Dieser Sprint hat die Vereinheitlichung **ausschließlich innerhalb dieser Liste** vorgenommen:

- **Techniken:** Standard = „## Evidenzlevel" (bereits die häufigste Formulierung im Repository, u. a. T-0001–T-0018). Angewendet auf alle 16 in diesem Sprint bearbeiteten Techniken.
- **Prinzipien:** Standard = „## Evidenzklassifikation" (häufigste Formulierung, u. a. P-0001–P-0021). Angewendet auf alle 8 in diesem Sprint bearbeiteten Prinzipien plus die 4 Meta-Prinzipien (ergänzender Spiegel-Abschnitt).

**Bewusst NICHT angetastet:** T-0036–T-0041 („Evidenzklasse") und P-0025/P-0026/P-0035–P-0043 („Evidenzgrad"/„Evidenzklasse") liegen außerhalb der im Audit für Meilenstein 1 benannten Objektliste. Eine repository-weite Vereinheitlichung aller ca. 60 verbleibenden Objekte mit abweichender Feldbenennung würde den Scope „ausschließlich Meilenstein 1" überschreiten und ist hiermit **als Empfehlung für einen eigenen, künftigen Harmonisierungs-Sprint dokumentiert**, nicht in diesem Sprint umgesetzt.

---

## 4. Erratum: E5-Zähler-Diskrepanz im Reifegradbericht

**Befund (Audit Kapitel 4):** `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (Abschnitt 1.1) behauptet: „5 Mechanismen auf E5 (replizierter Konsens): MEC-0002, MEC-0009, MEC-0012, MEC-0015, MEC-0021". Eine Vollprüfung der `## Evidenzlevel`-Abschnitte in den tatsächlichen Objektdateien zeigt:

| Objekt | Tatsächliches Evidenzlevel laut Objektdatei |
|---|---|
| MEC-0002 | **E4** (mit E3/E2-Staffelung je nach Anwendungsebene) |
| MEC-0009 | **E4** |
| MEC-0012 | **E4** |
| MEC-0015 | **E5** ✓ |
| MEC-0021 | **E5** ✓ |

**Richtigstellung:** Nur **MEC-0015 und MEC-0021** tragen tatsächlich E5 als Gesamtobjekt-Rating in ihren jeweiligen Objektdateien. Die Behauptung „5 Mechanismen auf E5" im Reifegradbericht ist um 150 % zu hoch. Die betroffenen Objekte selbst (MEC-0002, MEC-0009, MEC-0012) sind korrekt und konservativ mit E4 plus granularer Aufschlüsselung dokumentiert — die Inflation liegt ausschließlich in der zusammenfassenden Erzählebene des Reifegradberichts, nicht in den Wissensobjekten.

**Entscheidung dieses Sprints:** `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` selbst wird **nicht editiert**. Dies entspricht der ausdrücklichen Vorgabe „bitte nicht rückwirkend schönschreiben" — ein nachträgliches, stillschweigendes Ändern der Zahl „5" im Originaldokument würde den historischen Fehler verdecken statt ihn transparent zu machen. Stattdessen wird dieser Abschnitt als **formales Erratum** geführt: Wer `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` liest, findet dort weiterhin die ursprüngliche (fehlerhafte) Aussage; wer den Zustand des Repositorys aktuell und korrekt nachvollziehen will, findet hier und in `CODEX_AUDIT_2026-07.md` Kapitel 4 die geprüfte Richtigstellung.

**Empfehlung an den Herausgeber:** Bei einer künftigen inhaltlichen Überarbeitung des Reifegradberichts (nicht Teil dieses Sprints) sollte dort ein sichtbarer Verweis auf dieses Erratum ergänzt werden, ohne den ursprünglichen Text zu entfernen.

---

## 5. Leerer Duplikat-Ordner — `04_book_analysis/Never_Split_The_Difference/`

**Befund (Audit Kapitel 2):** Ein leerer, verwaister Ordner (Unterstrich-Schreibweise) existiert neben dem korrekt befüllten `04_book_analysis/Never Split the Difference/` (Leerzeichen-Schreibweise). Verifiziert: Der Ordner enthält 0 Dateien.

**Entscheidung dieses Sprints:** Der Ordner wird **nicht gelöscht**. Löschung ist eine strukturelle Repository-Änderung, und die Projektgrundregel lautet „Ändere die Repository-Struktur nicht eigenständig". Auch wenn der Ordner leer und die Löschung risikoarm erscheint, ist eine Löschung eine irreversible Strukturänderung, die außerhalb einer reinen Konsistenzkorrektur liegt.

**Vorgemerkt zur Entfernung:** Der Ordner ist hiermit offiziell zur Entfernung vorgemerkt. **Empfehlung an den Herausgeber:** Vor Version 1.0 den Ordner manuell entfernen oder explizit die Löschfreigabe erteilen, damit eine künftige Session ihn strukturell bereinigen kann.

---

## 6. `codex_knowledge_model.md` vs. `canonical_knowledge_model.md`

**Befund (Audit Kapitel 8):** Zwei Wissensmodell-Dokumente koexistieren im selben Ordner (`01_framework/05_knowledge_model/`): `canonical_knowledge_model.md` (334 Zeilen, versioniert, mit Entscheidungslogik, Evidenzklassen, Nicht-Anlage-Dokumentation) und `codex_knowledge_model.md` (69 Zeilen, einfacheres, unversioniertes Modell ohne diese Abschnitte). Letzteres wird im gesamten Repository nirgends als aktive Referenz zitiert — `canonical_knowledge_model.md` ("CKM") ist durchgängig das referenzierte Dokument.

**Entscheidung dieses Sprints:** `codex_knowledge_model.md` wurde **nicht gelöscht** (Unsicherheit über ursprünglichen Zweck und mögliche externe Verweise; Löschung wäre zudem eine Strukturänderung). Stattdessen wurde ein deutlicher Hinweis-Banner am Dateianfang ergänzt, der:
- die Datei explizit als „wahrscheinlich veraltet" kennzeichnet,
- auf `canonical_knowledge_model.md` als maßgebliche, aktuell gültige Quelle verweist,
- drei konkrete Optionen für den Herausgeber benennt (nach `99_archive/` verschieben / löschen / explizit als Kurzfassung erhalten),
- auf diesen Bericht und den Audit verweist.

Der ursprüngliche Inhalt der Datei wurde vollständig erhalten, nicht überschrieben.

---

## 7. Aktualisierte Objekte — Gesamtübersicht

**Wissensobjekte (30 Dateien, ausschließlich Konsistenzkorrekturen, keine neuen Objekte):**
T-0012, T-0013 (E-Level-Synchronisation) · T-0019, T-0020, T-0021, T-0026, T-0027, T-0028, T-0029, T-0030, T-0031, T-0032, T-0033, T-0034 (Evidenzfeld neu ergänzt) · T-0022, T-0023, T-0024, T-0025 (Feldname harmonisiert) · P-0027, P-0028, P-0029, P-0030, P-0031, P-0032, P-0033, P-0034 (Evidenzfeld neu ergänzt) · P-S1-001, P-S1-002, P-S1-003, P-S1-004 (Sichtbarkeits-Spiegel ergänzt, Audit-Methodikfehler richtiggestellt)

**Framework-/Governance-Dateien (Hinweise/Markierungen, keine inhaltliche Änderung):**
`01_framework/05_knowledge_model/codex_knowledge_model.md` (Veraltet-Banner ergänzt)

**Nicht verändert, nur dokumentiert:**
`04_book_analysis/Never_Split_The_Difference/` (leerer Ordner, zur Entfernung vorgemerkt) · `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md` (Erratum hier dokumentiert, Originaldokument unverändert)

**Keine neuen Wissensobjekte (ST/A/MEC/P/T/MOD) angelegt. Keine neuen Quellen recherchiert. Keine Framework-Dateien in ihrer Struktur oder Entscheidungslogik verändert.**

---

## 8. Offene Empfehlungen aus diesem Sprint (nicht umgesetzt, zur künftigen Entscheidung)

1. **Inhaltliche Evidenzbewertung der 20 neu mit Platzhalter versehenen T-/P-Objekte** (Abschnitt 2.1 und 2.3) — erfordert einen dedizierten Bewertungssprint, keine reine Konsistenzarbeit.
2. **Repository-weite Vereinheitlichung der Evidenzfeld-Benennung** über die in diesem Sprint bearbeiteten Objekte hinaus (T-0036–041, P-0025/026/035–043 sowie alle 48 Assumptions, die „Wie gut ist sie belegt?"/„Evidenzstatus" verwenden) — als eigener Harmonisierungs-Sprint vorgeschlagen.
3. **Sichtbares Erratum in `WISSENSCHAFTLICHER_REIFEGRADSBERICHT.md`** ergänzen (siehe Abschnitt 4) bei nächster inhaltlicher Überarbeitung dieses Dokuments.
4. **Herausgeber-Entscheidung zu `codex_knowledge_model.md`** (archivieren / löschen / als Kurzfassung erhalten) und zum leeren Duplikat-Ordner (Löschfreigabe).

---

*Erstellt: 2026-07 | Consistency Correction Sprint | Grundlage: `CODEX_AUDIT_2026-07.md` Kapitel 11, Meilenstein 1 | KI-Redaktion Sales Codex*
