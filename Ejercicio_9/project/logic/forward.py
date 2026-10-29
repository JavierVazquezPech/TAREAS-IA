"""Forward chaining for definite clauses (AIMA FOL-FC-ASK)."""

from __future__ import annotations

from dataclasses import dataclass, field

from logic.atoms import Atom, apply_atom, format_subst, unify
from logic.kb import KnowledgeBase, Rule


@dataclass
class TraceEvent:
    message: str


@dataclass
class InferenceResult:
    proved: bool
    subst: dict[str, str] | None
    inferred: list[Atom]
    events: list[TraceEvent] = field(default_factory=list)


def _standardize(rule: Rule, counter: int) -> Rule:
    """Rename rule variables so two firings do not clash."""
    mapping: dict[str, str] = {}

    def rename_atom(atom: Atom) -> Atom:
        new_args = []
        for arg in atom.args:
            if arg[:1].islower():
                mapping.setdefault(arg, f"{arg}_{counter}")
                new_args.append(mapping[arg])
            else:
                new_args.append(arg)
        return Atom(atom.predicate, tuple(new_args))

    return Rule(rule.rule_id, tuple(rename_atom(p) for p in rule.premises), rename_atom(rule.head))


def _satisfy(premises: tuple[Atom, ...], facts: list[Atom], subst: dict[str, str]) -> list[dict[str, str]]:
    if not premises:
        return [subst]
    first, rest = premises[0], premises[1:]
    goal = apply_atom(first, subst)
    results: list[dict[str, str]] = []
    for fact in facts:
        theta = unify(goal, fact, subst)
        if theta is not None:
            results.extend(_satisfy(rest, facts, theta))
    return results


def forward_chain(kb: KnowledgeBase, query: Atom, *, max_rounds: int = 50) -> InferenceResult:
    """Derive every consequence of the facts, then test the query.

    Running to quiescence (not stopping at the first hit) shows the extra
    facts that backward chaining never bothers to infer.
    """
    facts = list(kb.facts)
    inferred: list[Atom] = []
    events = [TraceEvent(f"Agenda (given facts): {', '.join(str(f) for f in facts) or '(empty)'}")]
    events.append(TraceEvent(f"Query: {query}"))

    counter = 0
    for round_no in range(1, max_rounds + 1):
        new_atoms: list[Atom] = []
        events.append(TraceEvent(f"--- round {round_no} ---"))
        for rule in kb.rules:
            counter += 1
            fresh = _standardize(rule, counter)
            for theta in _satisfy(fresh.premises, facts, {}):
                head = apply_atom(fresh.head, theta)
                if head in facts or head in new_atoms:
                    continue
                new_atoms.append(head)
                inferred.append(head)
                events.append(TraceEvent(f"Fire {rule.rule_id}  {format_subst(theta)}  ⇒  {head}"))
        if not new_atoms:
            events.append(TraceEvent("No new facts."))
            break
        facts.extend(new_atoms)
    else:
        events.append(TraceEvent("Stopped: max_rounds reached."))

    for fact in facts:
        theta = unify(query, fact, {})
        if theta is not None:
            events.append(TraceEvent(f"Query proved: {query}"))
            return InferenceResult(True, theta, inferred, events)
    events.append(TraceEvent("Query not proved."))
    return InferenceResult(False, None, inferred, events)
