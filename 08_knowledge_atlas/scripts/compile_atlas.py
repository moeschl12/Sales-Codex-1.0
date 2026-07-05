#!/usr/bin/env python3
"""
Atlas Compiler v0.1.3 (Hardening Sprint)
===========================================================

Erzeugt aus `03_knowledge_base/` einen strukturellen Graph-Export auf
Basis expliziter Referenzen, gemäß `08_knowledge_atlas/ATLAS_MANIFEST.md`
(Abschnitt 2: Knoten-Basis / Kanten-Basis / Analyse-Fokus).

Diese Version (v0.1.3) implementiert die im "Atlas Hardening Sprint v0.1.3"
freigegebenen Maßnahmen H-01, H-02 und H-03 (Grundlage:
`08_knowledge_atlas/SECOND_AUDIT_REMAINING_FINDINGS_TRIAGE.md`, siehe auch
`08_knowledge_atlas/ATLAS_HARDENING_SPRINT_V0_1_3_REPORT.md`):

  1. H-01 — Duplicate-ID Hard Fail: Eine Node-ID ist ein Primärschlüssel.
     Werden beim Aufbau des Knoten-Inventars mehrere Dateien mit derselben
     ID gefunden, bricht der Compiler mit einer klaren Fehlermeldung und
     Exit Code != 0 ab, BEVOR Referenzextraktion oder Output-Erzeugung
     stattfindet. Kein automatisches Merge, kein "first file wins", keine
     heuristische Auswahl.
  2. H-02 — Konservative Genitiv-Normalisierung: Ein Token wie "MEC-0011s"
     wird nur dann auf die Basis-ID "MEC-0011" normalisiert, wenn (a) das
     volle Token nicht selbst existiert, (b) es exakt auf ein kleines "s"
     endet, (c) die Basis-ID (Token ohne "s") existiert UND (d) diese
     Basis-ID dem Standardformat (PRÄFIX-####, vier Ziffern) entspricht.
     Keine pauschale Regex-Aufweichung, keine Änderung an echten
     Sonder-IDs, keine Normalisierung "erratener" Tippfehler.
  3. H-03 — Defensive Fence-Balance-Prüfung: Vor der Maskierung wird pro
     Datei geprüft, ob die Anzahl der Fenced-Code-Marker (```) gerade ist.
     Bei einer ungeraden Anzahl wird eine Warnung mit Dateiname erzeugt
     (kein Hard Fail, keine Markdown-AST, keine State-Machine) und im
     Compiler-Report dokumentiert.

Diese Version übernimmt unverändert die in v0.1.2 umgesetzten Korrekturen
F-01, F-02 und F-04 des externen Architecture Review (siehe
`08_knowledge_atlas/ATLAS_ARCHITECTURE_REVIEW_IMPLEMENTATION_REPORT.md`):

  - Vereinheitlichte, generische ID-Erkennung im Fließtext (kein statisch
    codiertes Literal-Verzeichnis für Sonder-IDs).
  - Syntaktische Vorfilterung: fenced code blocks, inline code und
    HTML-Kommentare werden vor dem Referenz-Scan maskiert (Zeilenzahl
    bleibt erhalten).
  - Kanten-Herkunft um Zeilennummer der Fundstelle erweitert.

F-03 (automatische Bereichsauflösung, z.B. "MEC-0005 bis MEC-0009"), T-04
(Inline-Backtick-Hardening), T-05 (T-0048 als Wissensobjekt anlegen), T-06
(Bereichsauflösung) und T-07 (alphabetische Sonderformate wie "P-ALPHA-001")
wurden im Hardening Sprint v0.1.3 bewusst NICHT umgesetzt (siehe Triage-
Dokument und Hardening Report) — bewusste Scope-Entscheidungen, keine
technischen Lücken dieses Sprints.

Scope (siehe Manifest, unverändert):
  - Knoten: ST, A, MEC, P, T, MOD (ausschließlich diese sechs Typen)
  - Kanten: explizite, gerichtete Referenzen (Objekt-ID im Volltext einer
    Objektdatei, unabhängig von der Markdown-Notation)
  - Analyse: ausschließlich Reference-Orphan-Identifikation

Explizit NICHT Teil dieses Compilers (Manifest Abschnitt 3):
  - keine Layer, keine Rich Edges, keine Metriken, keine Query Engine
  - keine semantische Interpretation der Referenzen (kein "unterstützt",
    "widerspricht" o.ä.)
  - keine Veränderung bestehender Wissensobjekte (rein lesender Zugriff)
  - keine automatische Bereichsauflösung (F-03, bewusst nicht umgesetzt)

Dieses Skript hat keine externen Abhängigkeiten (nur Python-Standardbibliothek),
damit es ohne zusätzliche Installation nachvollziehbar und auditierbar bleibt.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Konfiguration (aus ATLAS_MANIFEST.md Abschnitt 2.1)
# ---------------------------------------------------------------------------

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parent.parent.parent  # .../08_knowledge_atlas/scripts/ -> repo root
KB_ROOT = REPO_ROOT / "03_knowledge_base"
OUTPUT_DIR = REPO_ROOT / "08_knowledge_atlas" / "output"

COMPILER_VERSION = "v0.1.3"

# ID-Präfix -> (Objekttyp-Name, Unterordner unter 03_knowledge_base/)
NODE_TYPES: dict[str, tuple[str, str]] = {
    "ST": ("Statement", "statements"),
    "A": ("Annahme", "assumptions"),
    "MEC": ("Mechanismus", "mechanisms"),
    "P": ("Prinzip", "principles"),
    "T": ("Technik", "techniques"),
    "MOD": ("Modell", "models"),
}

# Bekannte Objekt-Präfixe, längste zuerst geprüft (MEC/MOD vor ST vor A/P/T),
# um Mehrdeutigkeiten beim Präfix-Abgleich zu vermeiden.
KNOWN_PREFIXES = ["MEC", "MOD", "ST", "A", "P", "T"]


def split_prefix(token: str) -> tuple[str, str] | None:
    """Zerlegt einen ID-Token (z.B. 'ST-0001' oder 'P-S1-001') in
    (Präfix, Rest-ohne-Präfix-und-Bindestrich). Liefert None, wenn der
    Token mit keinem der sechs bekannten Präfixe beginnt.

    Dies ist die (unveränderte) Knoten-Identifikation: Sie leitet die ID
    eines Wissensobjekts aus dessen Dateinamen ab und ist unabhängig vom
    konkreten Suffix-Format bereits vollständig generisch."""
    for prefix in KNOWN_PREFIXES:
        marker = prefix + "-"
        if token.startswith(marker):
            return prefix, token[len(marker):]
    return None


# ---------------------------------------------------------------------------
# Vereinheitlichte Referenz-Erkennung (Architecture Review, Befund F-01)
# ---------------------------------------------------------------------------
#
# EIN einziges Muster für alle Referenzen im Fließtext, unabhängig davon,
# ob sie dem Standardformat (PRÄFIX-####, vier Ziffern) oder einem
# Sonderformat (z.B. PRÄFIX-S1-001) folgen. Kein statisch codiertes
# Literal-Verzeichnis mehr -- jedes gefundene Token wird stattdessen zur
# Laufzeit gegen das aus den Dateinamen abgeleitete Knoten-Inventar
# geprüft (siehe extract_references). Das ermöglicht automatische
# Tippfehler-Erkennung auch für Sonderformate.
#
# Aufbau:
#   - Standardzweig: exakt vier Ziffern nach dem Präfix (PRÄFIX-####).
#     Stoppt dort garantiert, da \d{4} eine feste Breite hat -- ein direkt
#     angehängtes Wort (z.B. "T-0040-artigen") wird NICHT mitgezogen.
#   - Sonderzweig: greift nur, wenn der Standardzweig nicht passt. Das
#     erste Suffix-Segment muss mindestens eine Ziffer enthalten (das
#     unterscheidet echte Sonder-IDs wie "S1" von den im Repository sehr
#     häufigen generischen Begriffen wie "T-Objekt", "P-Kandidat" oder
#     "MEC-ID", die sonst massenhaft als falsche Treffer erkannt würden --
#     empirisch verifiziert gegen den realen Repository-Bestand, siehe
#     Implementation Report). Ein optionales zweites, rein numerisches
#     Segment deckt die reale Sprint-1-Notation ("S1-001") sowie deren
#     Tippfehlervarianten ("S1-01", "S1-0001") ab.
GENERIC_ID_PATTERN = re.compile(
    r"\b(?:MEC|MOD|ST|A|P|T)-(?:"
    r"\d{4}\b"
    r"|"
    r"(?=[A-Za-z0-9]*[0-9])[A-Za-z0-9]+(?:-[0-9]+)?\b"
    r")"
)


# ---------------------------------------------------------------------------
# Syntaktische Vorfilterung (Architecture Review, Befund F-02)
# ---------------------------------------------------------------------------
#
# Fenced code blocks, inline code und HTML-Kommentare werden vor dem
# Referenz-Scan maskiert (durch Leerzeichen ersetzt, Zeilenumbrüche
# bleiben erhalten), damit IDs innerhalb dieser Bereiche niemals Kanten
# erzeugen können. Normale Tabellen und Fließtext bleiben unverändert
# gültige Referenzbereiche.

FENCED_CODE_PATTERN = re.compile(r"```.*?```", re.DOTALL)
HTML_COMMENT_PATTERN = re.compile(r"<!--.*?-->", re.DOTALL)
INLINE_CODE_PATTERN = re.compile(r"`[^`\n]+`")

# Marker zum Zählen von Fenced-Code-Grenzen (H-03). Bewusst dieselbe
# literale Zeichenfolge wie im FENCED_CODE_PATTERN, keine neue Syntax.
FENCE_MARKER = "```"


def _mask_preserving_lines(match: re.Match[str]) -> str:
    return "".join(ch if ch == "\n" else " " for ch in match.group(0))


def mask_non_reference_regions(text: str) -> str:
    """Ersetzt fenced code blocks, inline code und HTML-Kommentare durch
    Leerzeichen (Zeilenumbrüche bleiben erhalten), damit Zeilennummern
    nach der Maskierung weiterhin korrekt sind. Reihenfolge ist wichtig:
    fenced code blocks zuerst, damit darin enthaltene einzelne Backticks
    nicht fälschlich als Inline-Code-Grenzen missverstanden werden."""
    text = FENCED_CODE_PATTERN.sub(_mask_preserving_lines, text)
    text = HTML_COMMENT_PATTERN.sub(_mask_preserving_lines, text)
    text = INLINE_CODE_PATTERN.sub(_mask_preserving_lines, text)
    return text


def check_fence_balance(rel_path: str, raw_text: str) -> str | None:
    """H-03 — Minimale defensive Prüfung: zählt Vorkommen des Fence-Markers
    (```) im unmaskierten Text. Bei einer ungeraden Anzahl ist mindestens
    ein Fenced-Code-Block nicht geschlossen. Liefert eine Warnmeldung
    zurück (oder None, wenn balanciert). Bewusst klein gehalten: reine
    Zählung, kein Markdown-AST, keine State-Machine, kein Hard Fail --
    dies ist Hardening für ein aktuell nicht auftretendes Szenario (siehe
    Triage T-03), keine Korrektur eines im Bestand vorhandenen Fehlers."""
    count = raw_text.count(FENCE_MARKER)
    if count % 2 != 0:
        return (
            f"Unbalancierte Fenced-Code-Bloecke in `{rel_path}`: "
            f"{count} Vorkommen von ``` (ungerade Anzahl) -- mindestens ein "
            f"Block ist nicht geschlossen. Referenz-Erkennung fuer den "
            f"betroffenen Dateibereich kann dadurch beeintraechtigt sein."
        )
    return None


# ---------------------------------------------------------------------------
# H-02: Konservative Genitiv-Normalisierung
# ---------------------------------------------------------------------------

def try_genitive_normalization(token: str, nodes: dict[str, "Node"]) -> str | None:
    """Konservative Normalisierung eines deutschen Genitiv-Suffixes (H-02).

    Wird ausschließlich für Tokens aufgerufen, die NICHT bereits selbst als
    Node-ID existieren (Vorbedingung 1 liegt beim Aufrufer). Normalisiert
    nur, wenn ZUSÄTZLICH alle folgenden Bedingungen erfüllt sind:

      2. Das Token endet exakt auf ein kleines "s".
      3. Das Token ohne das abschließende "s" (die Basis-ID) existiert im
         Knoten-Inventar.
      4. Diese Basis-ID hat das Standard-ID-Format (PRÄFIX-####, exakt vier
         Ziffern) -- nicht ein Sonderformat. Das schützt echte Sonder-IDs
         (z. B. ein hypothetisches "P-S1-001s") davor, unbeabsichtigt
         gekürzt zu werden, und hält die Normalisierung strikt auf den
         empirisch belegten Genitiv-Fall (Standard-ID + angehängtes "s")
         beschränkt.

    Liefert die Basis-ID zurück, wenn normalisiert werden darf, sonst None.
    Keine pauschale Entfernung eines abschließenden "s", keine Korrektur
    beliebiger unbekannter Tokens -- ohne eine tatsächlich existierende,
    standardformatige Basis-ID passiert nichts."""
    if len(token) < 2 or token[-1] != "s":
        return None
    candidate = token[:-1]
    candidate_node = nodes.get(candidate)
    if candidate_node is None:
        return None
    if not candidate_node.is_standard:
        return None
    return candidate


# ---------------------------------------------------------------------------
# Datenstrukturen
# ---------------------------------------------------------------------------

@dataclass
class Node:
    id: str
    type: str
    filename: str
    path: str  # repo-relativer Pfad
    title: str = ""
    is_standard: bool = True  # False = Sonder-ID-Format (z.B. P-S1-001)


@dataclass
class Edge:
    source_id: str
    source_type: str
    target_id: str
    target_type: str
    declared_in: str  # repo-relativer Pfad der Quelldatei
    line_number: int  # Zeile der (ersten) Fundstelle in der Quelldatei


@dataclass
class CompilerResult:
    nodes: dict[str, Node] = field(default_factory=dict)
    edges: list[Edge] = field(default_factory=list)
    duplicate_ids: dict[str, list[str]] = field(default_factory=dict)  # id -> [paths]
    unresolved_references: list[tuple[str, str, str]] = field(default_factory=list)
    # (source_id, target_id_text, declared_in)
    fence_warnings: list[str] = field(default_factory=list)  # H-03
    genitive_normalizations: int = 0  # H-02, Diagnosezähler (keine Analysefunktion)


# ---------------------------------------------------------------------------
# Schritt 1: Knoten-Inventar aufbauen
# ---------------------------------------------------------------------------

def extract_title(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return ""


def build_node_inventory(result: CompilerResult) -> dict[str, list[Path]]:
    """Scannt die definierten KB-Unterordner, erzeugt Nodes, erkennt Duplikat-IDs.

    Rückgabe: id -> Liste der Dateipfade, die diese ID beanspruchen
    (Länge > 1 bedeutet Duplikat-ID).
    """
    id_claims: dict[str, list[Path]] = defaultdict(list)

    for prefix, (_type_name, subfolder) in NODE_TYPES.items():
        folder = KB_ROOT / subfolder
        if not folder.is_dir():
            continue
        for file_path in sorted(folder.rglob("*.md")):
            token = file_path.stem.split("_", 1)[0]
            parsed = split_prefix(token)
            if parsed is None:
                # Datei ohne erkennbares Präfix im Dateinamen -> außerhalb
                # des Scopes von v0.1 (Knoten-Basis erfordert explizite ID).
                continue
            file_prefix, suffix = parsed
            if file_prefix != prefix:
                # Datei liegt im falschen Unterordner (Präfix passt nicht
                # zum erwarteten Typ dieses Ordners) -> wird trotzdem als
                # Duplikat-/Inkonsistenz-Kandidat erfasst, aber nicht als
                # Node dieses Typs angelegt.
                continue
            node_id = f"{file_prefix}-{suffix}"
            rel_path = file_path.relative_to(REPO_ROOT).as_posix()
            id_claims[node_id].append(file_path)

            if node_id not in result.nodes:
                text = file_path.read_text(encoding="utf-8", errors="replace")
                result.nodes[node_id] = Node(
                    id=node_id,
                    type=file_prefix,
                    filename=file_path.name,
                    path=rel_path,
                    title=extract_title(text),
                    is_standard=bool(re.fullmatch(r"\d{4}", suffix)),
                )

    duplicates = {nid: [p.relative_to(REPO_ROOT).as_posix() for p in paths]
                  for nid, paths in id_claims.items() if len(paths) > 1}
    result.duplicate_ids = duplicates
    return id_claims


# ---------------------------------------------------------------------------
# H-01: Duplicate-ID Hard Fail
# ---------------------------------------------------------------------------

def abort_on_duplicate_ids(result: CompilerResult) -> None:
    """H-01 — Eine Node-ID ist ein Primärschlüssel. Werden Duplikate
    gefunden, bricht der Compiler HIER ab -- vor jeder Referenzextraktion
    und vor jeder Output-Erzeugung. Kein automatisches Merge, kein "first
    file wins", keine heuristische Auswahl. Exit Code 1."""
    if not result.duplicate_ids:
        return

    print("FATAL: Duplicate Node-IDs erkannt -- Compiler abgebrochen.", file=sys.stderr)
    print(
        "Eine Node-ID ist ein Primaerschluessel im Knowledge Atlas. Ein Graph auf "
        "Basis mehrdeutiger Primaerschluessel darf nicht als regulaerer Atlas-Output "
        "veroeffentlicht werden.",
        file=sys.stderr,
    )
    print("", file=sys.stderr)
    print(f"Anzahl betroffener IDs: {len(result.duplicate_ids)}", file=sys.stderr)
    print("", file=sys.stderr)
    for nid in sorted(result.duplicate_ids.keys()):
        print(f"  Duplicate ID: {nid}", file=sys.stderr)
        for p in result.duplicate_ids[nid]:
            print(f"    - {p}", file=sys.stderr)
    print("", file=sys.stderr)
    print(
        "Es wurden KEINE neuen oder bestehenden Atlas-Outputs erzeugt oder "
        "ueberschrieben. Referenzextraktion wurde nicht durchgefuehrt (mehrdeutige "
        "Node-Basis). Bitte die ID-Kollision im Repository beheben (Dateien "
        "umbenennen oder zusammenfuehren) und den Compiler danach erneut ausfuehren.",
        file=sys.stderr,
    )
    sys.exit(1)


# ---------------------------------------------------------------------------
# Schritt 2: Explizite Referenzen erkennen (Kanten-Basis, Manifest 2.2)
# ---------------------------------------------------------------------------

def extract_references(result: CompilerResult) -> None:
    """Scannt jede Node-Datei mit EINEM einzigen, generischen Muster
    (GENERIC_ID_PATTERN) auf ID-Referenzen -- nach vorheriger Maskierung
    von Code-Blöcken, Inline-Code und HTML-Kommentaren. Jedes gefundene
    Token wird gegen das Knoten-Inventar validiert: existiert es (ggf.
    nach konservativer Genitiv-Normalisierung, H-02), wird eine Kante (mit
    Zeilennummer der ersten Fundstelle) angelegt; andernfalls wird es als
    unaufgelöste Referenz erfasst. Selbstreferenzen werden verworfen (auch
    nach Normalisierung), mehrfache Nennungen derselben Kante dedupliziert
    (erste Fundstelle bleibt maßgeblich). Zusätzlich wird je Datei die
    Fence-Balance geprüft (H-03)."""
    seen_edges: dict[tuple[str, str], int] = {}  # (source_id, target_id) -> line_number

    for node in sorted(result.nodes.values(), key=lambda n: n.id):
        file_path = REPO_ROOT / node.path
        raw_text = file_path.read_text(encoding="utf-8", errors="replace")

        fence_warning = check_fence_balance(node.path, raw_text)
        if fence_warning is not None:
            result.fence_warnings.append(fence_warning)

        scan_text = mask_non_reference_regions(raw_text)

        for m in GENERIC_ID_PATTERN.finditer(scan_text):
            target_id = m.group(0)

            if target_id not in result.nodes:
                normalized = try_genitive_normalization(target_id, result.nodes)
                if normalized is not None:
                    target_id = normalized
                    result.genitive_normalizations += 1

            if target_id == node.id:
                continue  # Selbstreferenz ignorieren (auch nach Normalisierung)

            if target_id not in result.nodes:
                result.unresolved_references.append((node.id, target_id, node.path))
                continue

            edge_key = (node.id, target_id)
            if edge_key in seen_edges:
                continue  # Duplikat-Kante (mehrfache Nennung derselben Referenz)
            line_number = scan_text.count("\n", 0, m.start()) + 1
            seen_edges[edge_key] = line_number

            result.edges.append(
                Edge(
                    source_id=node.id,
                    source_type=node.type,
                    target_id=target_id,
                    target_type=result.nodes[target_id].type,
                    declared_in=node.path,
                    line_number=line_number,
                )
            )


# ---------------------------------------------------------------------------
# Schritt 3: Reference Orphans (Manifest 2.3)
# ---------------------------------------------------------------------------

def find_reference_orphans(result: CompilerResult) -> list[Node]:
    connected: set[str] = set()
    for e in result.edges:
        connected.add(e.source_id)
        connected.add(e.target_id)

    orphans = [n for nid, n in result.nodes.items() if nid not in connected]
    return sorted(orphans, key=lambda n: (n.type, n.id))


# ---------------------------------------------------------------------------
# Export: CSV / DOT / Report
# ---------------------------------------------------------------------------

def write_nodes_csv(result: CompilerResult) -> Path:
    out_path = OUTPUT_DIR / "nodes.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "type", "filename", "path", "title"])
        for node in sorted(result.nodes.values(), key=lambda n: (n.type, n.id)):
            writer.writerow([node.id, node.type, node.filename, node.path, node.title])
    return out_path


def write_edges_csv(result: CompilerResult) -> Path:
    out_path = OUTPUT_DIR / "edges.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["source_id", "source_type", "target_id", "target_type", "declared_in", "line_number"])
        for e in sorted(result.edges, key=lambda e: (e.source_id, e.target_id)):
            writer.writerow([e.source_id, e.source_type, e.target_id, e.target_type, e.declared_in, e.line_number])
    return out_path


def write_orphans_csv(orphans: list[Node]) -> Path:
    out_path = OUTPUT_DIR / "reference_orphans.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "type", "filename", "path", "title"])
        for node in orphans:
            writer.writerow([node.id, node.type, node.filename, node.path, node.title])
    return out_path


def write_dot(result: CompilerResult) -> Path:
    out_path = OUTPUT_DIR / "atlas_network.dot"
    type_shape = {
        "ST": "box",
        "A": "ellipse",
        "MEC": "hexagon",
        "P": "diamond",
        "T": "component",
        "MOD": "doubleoctagon",
    }
    lines = [
        f"// Atlas Network Export {COMPILER_VERSION} (Hardening Sprint)",
        "// Gerichteter Graph exp. Referenzen. Keine semantische Kantentypisierung.",
        "digraph AtlasNetwork {",
        "  rankdir=LR;",
        "  node [style=filled, fillcolor=white];",
        "",
    ]
    for node in sorted(result.nodes.values(), key=lambda n: n.id):
        shape = type_shape.get(node.type, "ellipse")
        label = node.id.replace('"', "'")
        lines.append(f'  "{node.id}" [label="{label}", shape={shape}];')
    lines.append("")
    for e in sorted(result.edges, key=lambda e: (e.source_id, e.target_id)):
        lines.append(f'  "{e.source_id}" -> "{e.target_id}";')
    lines.append("}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def write_report(result: CompilerResult, orphans: list[Node], id_claims: dict[str, list[Path]]) -> Path:
    out_path = OUTPUT_DIR / "atlas_compiler_report.md"

    node_counts: dict[str, int] = defaultdict(int)
    for n in result.nodes.values():
        node_counts[n.type] += 1
    total_nodes = sum(node_counts.values())
    special_count = sum(1 for n in result.nodes.values() if not n.is_standard)

    orphan_counts: dict[str, int] = defaultdict(int)
    for n in orphans:
        orphan_counts[n.type] += 1

    unresolved_by_target: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for source_id, target_text, declared_in in result.unresolved_references:
        unresolved_by_target[target_text].append((source_id, declared_in))

    lines: list[str] = []
    lines.append(f"# Atlas Compiler Report — {COMPILER_VERSION} (Hardening Sprint)")
    lines.append("")
    lines.append("**Dokumentklasse:** Reference (Generierter Analyse-Output)")
    lines.append("**Erzeugt von:** `08_knowledge_atlas/scripts/compile_atlas.py`")
    lines.append(f"**Erzeugt am:** {date.today().isoformat()}")
    lines.append("**Grundlage:** `08_knowledge_atlas/ATLAS_MANIFEST.md`, Abschnitt 2 (Knoten-Basis, Kanten-Basis, Analyse-Fokus)")
    lines.append("**Hinweis:** Rein lesend erzeugt. Keine Wissensobjekte in `03_knowledge_base/` wurden verändert. Dieser Report wird nur erzeugt, wenn keine Duplicate-IDs vorliegen (H-01) — siehe Abschnitt 5.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 1. Nodes je Typ")
    lines.append("")
    lines.append("| ID-Präfix | Objekttyp | Anzahl |")
    lines.append("|---|---|---|")
    for prefix, (type_name, _folder) in NODE_TYPES.items():
        lines.append(f"| `{prefix}` | {type_name} | {node_counts.get(prefix, 0)} |")
    lines.append(f"| **Gesamt** | | **{total_nodes}** |")
    lines.append(f"| davon Sonder-ID-Format (z. B. `P-S1-XXX`) | | {special_count} |")
    lines.append("")

    lines.append("## 2. Edges")
    lines.append("")
    lines.append(f"Anzahl gerichteter, deduplizierter expliziter Referenzen: **{len(result.edges)}**")
    lines.append("")
    lines.append("Eine Kante `(source_id -> target_id)` bedeutet: Die Datei von `source_id` enthält im Volltext (außerhalb von Code-Blöcken, Inline-Code und HTML-Kommentaren) eine explizite Nennung von `target_id`. Keine semantische Typisierung, keine Gewichtung (Manifest Abschnitt 2.2). Seit v0.1.2 enthält jede Kante zusätzlich die Zeilennummer der (ersten) Fundstelle (`edges.csv`, Spalte `line_number`). Seit v0.1.3 kann `target_id` auch das Ergebnis einer konservativen Genitiv-Normalisierung sein (H-02, siehe Abschnitt 6.3).")
    lines.append("")

    lines.append("## 3. Reference Orphans")
    lines.append("")
    lines.append(f"Anzahl Reference Orphans (Knoten ohne jede eingehende oder ausgehende explizite Referenz): **{len(orphans)}** von {total_nodes} Knoten")
    lines.append("")
    lines.append("| ID-Präfix | Objekttyp | Orphans | Nodes gesamt | Anteil |")
    lines.append("|---|---|---|---|---|")
    for prefix, (type_name, _folder) in NODE_TYPES.items():
        n_total = node_counts.get(prefix, 0)
        n_orphan = orphan_counts.get(prefix, 0)
        share = f"{(n_orphan / n_total * 100):.1f}%" if n_total else "–"
        lines.append(f"| `{prefix}` | {type_name} | {n_orphan} | {n_total} | {share} |")
    lines.append("")
    lines.append("Vollständige Liste: `reference_orphans.csv`. Ein Reference-Orphan-Befund ist keine Qualitätsaussage (Manifest Abschnitt 4).")
    lines.append("")

    lines.append("## 4. Unaufgelöste Referenzen")
    lines.append("")
    lines.append(f"Anzahl textlicher ID-Muster, die auf keine existierende Node-ID im Knoten-Inventar verweisen: **{len(result.unresolved_references)}**")
    lines.append(f"Anzahl unterschiedlicher betroffener Ziel-IDs: **{len(unresolved_by_target)}**")
    lines.append("")
    if unresolved_by_target:
        lines.append("| Referenzierte (nicht existierende) ID | Genannt in |")
        lines.append("|---|---|")
        for target_text in sorted(unresolved_by_target.keys()):
            sources = unresolved_by_target[target_text]
            cited_by = ", ".join(sorted({s for s, _ in sources}))
            lines.append(f"| `{target_text}` | {cited_by} |")
    else:
        lines.append("Keine unaufgelösten Referenzen gefunden.")
    lines.append("")

    lines.append("## 5. Duplikat-IDs")
    lines.append("")
    lines.append("Seit v0.1.3 (H-01) bricht der Compiler bei erkannten Duplikat-IDs vor der Referenzextraktion und vor jeder Output-Erzeugung mit Exit Code != 0 ab (siehe `abort_on_duplicate_ids()`). Dieser Report wird also nur erzeugt, wenn zum Zeitpunkt des Laufs **keine** Duplikat-IDs vorlagen.")
    lines.append("")
    if result.duplicate_ids:
        # Sollte praktisch nie erreicht werden (Hard Fail erfolgt vorher),
        # bleibt als defensive Absicherung erhalten, falls main() künftig
        # anders verdrahtet wird.
        lines.append(f"Anzahl IDs mit mehr als einer beanspruchenden Datei: **{len(result.duplicate_ids)}**")
        lines.append("")
        lines.append("| ID | Dateien |")
        lines.append("|---|---|")
        for nid in sorted(result.duplicate_ids.keys()):
            paths = "; ".join(result.duplicate_ids[nid])
            lines.append(f"| `{nid}` | {paths} |")
    else:
        lines.append("Keine Duplikat-IDs gefunden (jede ID wird in genau einer Datei beansprucht).")
    lines.append("")

    lines.append("## 6. Korrekturhistorie")
    lines.append("")
    lines.append("### 6.1 Erster Lauf → Sonder-ID-Korrektur (2026-07-04, v0.1.1)")
    lines.append("")
    lines.append("Der erste Compiler-Lauf erkannte Node-IDs nur im Standardformat `PRÄFIX-####`. Vier reale Prinzip-Objekte mit Sonderformat (`P-S1-001` bis `P-S1-004`) fehlten dadurch im Knoten-Inventar. Nach Korrektur der Knoten-Identifikation (dateinamenbasiert statt festes Zahlenformat) waren alle vier Objekte und ihre Referenzen erfasst, jedoch über ein zusätzliches, statisch codiertes Literal-Verzeichnis im Referenz-Scan (asymmetrische Parser-Logik).")
    lines.append("")
    lines.append("| Kennzahl | v0.1 (Standardformat-Bug) | v0.1.1 (Literal-Fix) |")
    lines.append("|---|---|---|")
    lines.append("| Nodes gesamt | 510 | 514 |")
    lines.append("| Edges | 2031 | 2076 |")
    lines.append("| Reference Orphans | 18 | 18 |")
    lines.append("| Unaufgelöste Referenzen | 1 | 2 |")
    lines.append("")
    lines.append("### 6.2 Architecture Review Implementation (2026-07-04, v0.1.2)")
    lines.append("")
    lines.append("Externes Architecture Review identifizierte die in 6.1 beschriebene Literal-Lösung als architektonischen Mangel (Befund F-01, MAJOR): Tippfehler in Sonder-ID-Referenzen wurden dadurch stillschweigend ignoriert statt als unaufgelöste Referenz gemeldet. Zusätzlich fehlte eine Vorfilterung von Code-Blöcken/Kommentaren (F-02) und eine Zeilennummer in der Kanten-Herkunft (F-04). Details: `08_knowledge_atlas/ATLAS_ARCHITECTURE_REVIEW_IMPLEMENTATION_REPORT.md`.")
    lines.append("")
    lines.append("| Kennzahl | v0.1.1 (vor Review-Sprint) | v0.1.2 |")
    lines.append("|---|---|---|")
    lines.append("| Nodes gesamt | 514 | 514 |")
    lines.append("| Edges | 2076 | 2071 |")
    lines.append("| Reference Orphans | 18 | 18 |")
    lines.append("| Unaufgelöste Referenzen | 2 | 7 |")
    lines.append("| Duplikat-IDs | 0 | 0 |")
    lines.append("")
    lines.append("### 6.3 Atlas Hardening Sprint v0.1.3 (2026-07-05)")
    lines.append("")
    lines.append("Ein zweites, unabhängiges Architecture Audit (`SECOND_INDEPENDENT_ARCHITECTURE_AUDIT.md`) sowie die anschließende technische Triage (`SECOND_AUDIT_REMAINING_FINDINGS_TRIAGE.md`) identifizierten drei umzusetzende Robustheitslücken: H-01 (Duplicate-ID-Verhalten, T-02), H-02 (Genitiv-Suffix-Erkennung, T-01) und H-03 (fehlende Fence-Balance-Prüfung, T-03). Alle drei wurden in diesem Sprint umgesetzt (siehe `ATLAS_HARDENING_SPRINT_V0_1_3_REPORT.md` für Details). Der zuvor im zweiten Audit behauptete deterministische Laufzeitabsturz wurde bereits separat als nicht reproduzierbar zurückgewiesen (`SECOND_AUDIT_CRASH_FINDING_VERIFICATION.md`) und ist von diesem Sprint nicht betroffen.")
    lines.append("")
    lines.append("| Kennzahl | v0.1.2 (vor Hardening) | v0.1.3 (aktueller Lauf) |")
    lines.append("|---|---|---|")
    lines.append(f"| Nodes gesamt | 514 | {total_nodes} |")
    lines.append(f"| Edges | 2071 | {len(result.edges)} |")
    lines.append(f"| Reference Orphans | 18 | {len(orphans)} |")
    lines.append(f"| Unaufgelöste Referenzen | 7 | {len(result.unresolved_references)} |")
    lines.append(f"| Duplikat-IDs | 0 | {len(result.duplicate_ids)} |")
    lines.append(f"| Genitiv-Normalisierungen (H-02, Diagnosezähler) | — | {result.genitive_normalizations} |")
    lines.append(f"| Fence-Balance-Warnungen (H-03) | — | {len(result.fence_warnings)} |")
    lines.append("")
    if result.fence_warnings:
        lines.append("**Fence-Balance-Warnungen (H-03):**")
        lines.append("")
        for w in result.fence_warnings:
            lines.append(f"- {w}")
        lines.append("")
    else:
        lines.append("**Fence-Balance-Warnungen (H-03):** Keine — alle geprüften Dateien mit Fenced-Code-Blöcken sind balanciert.")
        lines.append("")

    lines.append(f"## 7. Grenzen des Compilers {COMPILER_VERSION}")
    lines.append("")
    lines.append("- **Kein Query Interface, keine Layer, keine Rich Edges, keine Metriken** — dies ist ein reiner Struktur-Export gemäß Manifest Abschnitt 3, keine Analyseplattform.")
    lines.append("- **Volltext-Scan ohne Abschnittserkennung (reduziert, nicht behoben).** Seit v0.1.2 werden Code-Blöcke, Inline-Code und HTML-Kommentare vor dem Scan ausgeschlossen. Der Compiler unterscheidet aber weiterhin nicht, ob eine verbleibende ID-Nennung in einem benannten Referenzabschnitt, in normalem Fließtext oder in einer Tabelle steht — jede dieser Nennungen zählt gleichermaßen als explizite Referenz.")
    lines.append("- **Sonderformat-Erkennung erfordert mindestens eine Ziffer im ersten Suffix-Segment.** Diese Heuristik unterscheidet echte Sonder-IDs (z. B. \"S1\" in `P-S1-001`) von den im Repository sehr häufigen generischen Begriffen wie \"T-Objekt\", \"P-Kandidat\" oder \"MEC-ID\". Ein rein alphabetisches Sonderformat ohne jede Ziffer (z. B. hypothetisch \"P-ALPHA-001\") würde dadurch nicht erkannt — im aktuellen Repository-Bestand kommt ein solches Format nicht vor und ist auch durch keine Governance-Regel vorgesehen (Triage T-07, bewusst nicht in v0.1.3 adressiert).")
    lines.append("- **Genitiv-Normalisierung (H-02) ist bewusst eng gefasst.** Nur ein Token, das (a) nicht selbst existiert, (b) auf ein kleines \"s\" endet und (c) dessen Basis-ID im Standardformat (PRÄFIX-####) existiert, wird normalisiert. Andere Suffixe (z. B. \"MEC-0011er\", Genitiv mit Apostroph, oder ein Genitiv-\"s\" an einer Sonderformat-ID) werden weiterhin nicht aufgelöst und bleiben unaufgelöste Referenzen. Dies ist eine bewusste Konservativität, kein technisches Versehen.")
    lines.append("- **Kompakte Bereichsangaben werden nicht aufgelöst (bewusst, siehe F-03).** Notationen wie \"MEC-0005 bis MEC-0009\" werden nur an den textlich vollständig genannten IDs erkannt. Diese Erweiterung wurde im Architecture Review vorgeschlagen, vom Herausgeber aber ausdrücklich nicht freigegeben und daher nicht implementiert.")
    lines.append("- **Fence-Balance-Prüfung (H-03) ist eine reine Zählung, keine Strukturprüfung.** Sie erkennt eine ungerade Gesamtzahl von ``` je Datei, kann aber eine geradzahlige, jedoch falsch gepaarte Konstellation (z. B. ``` als unbeabsichtigter Trenner) nicht erkennen. Kein Markdown-AST, keine zeilenweise State-Machine — bewusst minimal gehalten (Triage T-03: aktuell kein realer Vorkommensfall im Bestand).")
    lines.append("- **Inline-Backtick-Hardening (T-04) wurde bewusst nicht umgesetzt.** Der theoretische Schadensradius ist durch die Musterkonstruktion (`` `[^`\\n]+` ``) strukturell auf eine einzelne Zeile begrenzt; im aktuellen Bestand existiert kein Fall eines ungepaarten Backticks (empirisch verifiziert, siehe Triage T-04).")
    lines.append("- **Keine Gewichtung von Mehrfachnennungen.** Wird dieselbe Ziel-ID mehrfach in derselben Quelldatei genannt, entsteht dennoch nur eine Kante; die gespeicherte Zeilennummer bezieht sich auf die erste Fundstelle, nicht auf alle Fundstellen.")
    lines.append("- **Keine Validierung der inhaltlichen Richtigkeit** einer Referenz — der Compiler prüft nur, ob die referenzierte ID im Knoten-Inventar existiert (siehe Abschnitt 4), nicht ob die Referenz fachlich sinnvoll ist.")
    lines.append("- **Keine Erkennung von IDs außerhalb der sechs definierten Typen** (z. B. SRC-, VAL-, SPR-, B-, W-IDs) — diese sind laut Manifest Abschnitt 2.1 nicht Teil der Knoten-Basis und werden vom Compiler grundsätzlich ignoriert, auch wenn sie im Fließtext vorkommen.")
    lines.append("- **Dateinamenbasierte ID-Zuordnung.** Die ID eines Knotens wird ausschließlich aus dem Dateinamen abgeleitet (Segment vor dem ersten Unterstrich). Abweichungen zwischen Dateiname und internem ID-Feld werden nicht geprüft.")
    lines.append("- **Kein inkrementeller Modus.** Jeder Lauf verarbeitet das gesamte Knoten-Inventar neu; es gibt keinen automatisierten Abgleich gegen einen vorherigen Lauf (die Vergleiche in Abschnitt 6 sind manuell dokumentierte Einzelfälle, kein laufender Mechanismus).")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Dieser Report ist ein generierter Analyse-Output, kein Wissensobjekt. Er ersetzt keine Herausgeberentscheidung und trifft keine inhaltliche Bewertung.*")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    result = CompilerResult()
    id_claims = build_node_inventory(result)

    # H-01: Hard Fail bei Duplicate-IDs -- VOR jeder Referenzextraktion und
    # VOR jeder Output-Erzeugung. Beendet den Prozess (sys.exit(1)), falls
    # Duplikate vorliegen; kehrt sonst folgenlos zurück.
    abort_on_duplicate_ids(result)

    extract_references(result)
    orphans = find_reference_orphans(result)

    nodes_path = write_nodes_csv(result)
    edges_path = write_edges_csv(result)
    orphans_path = write_orphans_csv(orphans)
    dot_path = write_dot(result)
    report_path = write_report(result, orphans, id_claims)

    print(f"Compiler Version:    {COMPILER_VERSION}")
    print(f"Nodes:              {len(result.nodes)}  -> {nodes_path.relative_to(REPO_ROOT)}")
    print(f"Edges:               {len(result.edges)}  -> {edges_path.relative_to(REPO_ROOT)}")
    print(f"Reference Orphans:   {len(orphans)}  -> {orphans_path.relative_to(REPO_ROOT)}")
    print(f"Unresolved refs:     {len(result.unresolved_references)}")
    print(f"Duplicate IDs:       {len(result.duplicate_ids)}")
    print(f"Genitive normalizations (H-02): {result.genitive_normalizations}")
    print(f"Fence balance warnings (H-03):  {len(result.fence_warnings)}")
    for w in result.fence_warnings:
        print(f"  WARNUNG: {w}")
    print(f"DOT export:          -> {dot_path.relative_to(REPO_ROOT)}")
    print(f"Report:              -> {report_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
