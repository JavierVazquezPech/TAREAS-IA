"""Load a definite-clause knowledge base from YAML."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from logic.atoms import Atom, parse_atom


@dataclass(frozen=True)
class Rule:
    rule_id: str
    premises: tuple[Atom, ...]
    head: Atom

    def __str__(self) -> str:
        body = " ∧ ".join(str(p) for p in self.premises) if self.premises else "true"
        return f"{self.rule_id}:  {body}  →  {self.head}"


@dataclass
class KnowledgeBase:
    facts: list[Atom]
    rules: list[Rule]
    query: Atom | None
    source: Path | None = None

    def copy(self) -> "KnowledgeBase":
        return KnowledgeBase(list(self.facts), list(self.rules), self.query, self.source)


def load_kb(path: str | Path) -> KnowledgeBase:
    path = Path(path)
    with path.open(encoding="utf-8") as fh:
        raw = yaml.safe_load(fh) or {}
    return parse_kb(raw, source=path)


def parse_kb(raw: dict[str, Any], source: Path | None = None) -> KnowledgeBase:
    facts = [parse_atom(item) for item in (raw.get("facts") or [])]
    rules = []
    for i, item in enumerate(raw.get("rules") or [], start=1):
        if not isinstance(item, dict):
            raise ValueError(f"rule {i} must be a mapping with 'if' and 'then'")
        rule_id = str(item.get("id") or f"R{i}")
        premises = tuple(parse_atom(p) for p in (item.get("if") or []))
        head = parse_atom(item["then"])
        rules.append(Rule(rule_id, premises, head))
    query_raw = raw.get("query")
    query = parse_atom(query_raw) if query_raw else None
    return KnowledgeBase(facts, rules, query, source)


def format_kb(kb: KnowledgeBase) -> str:
    lines = []
    if kb.source:
        lines.append(f"File: {kb.source}")
    lines.append("Facts:")
    if not kb.facts:
        lines.append("  (none)")
    for fact in kb.facts:
        lines.append(f"  {fact}")
    lines.append("Rules:")
    if not kb.rules:
        lines.append("  (none)")
    for rule in kb.rules:
        lines.append(f"  {rule}")
    lines.append(f"Query: {kb.query if kb.query else '(none)'}")
    return "\n".join(lines)
