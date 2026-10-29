"""Backward chaining for definite clauses (AIMA FOL-BC-ASK)."""

from __future__ import annotations

from logic.atoms import Atom, apply_atom, format_subst, unify
from logic.forward import InferenceResult, TraceEvent
from logic.kb import KnowledgeBase, Rule


def _standardize(rule: Rule, counter: int) -> Rule:
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


def backward_chain(kb: KnowledgeBase, query: Atom, *, max_depth: int = 25) -> InferenceResult:
    """Prove the query by reducing it to known facts. Does not derive unused atoms."""
    events = [TraceEvent(f"Query: {query}")]
    counter = [0]
    visited_goals: list[Atom] = []

    def indent(depth: int) -> str:
        return "  " * depth

    def bc_or(goal: Atom, subst: dict[str, str], depth: int, stack: tuple[str, ...]) -> dict[str, str] | None:
        goal = apply_atom(goal, subst)
        key = str(goal)
        if key in stack:
            events.append(TraceEvent(f"{indent(depth)}loop: {goal} already on the goal stack — skip"))
            return None
        if depth > max_depth:
            events.append(TraceEvent(f"{indent(depth)}max depth at {goal}"))
            return None

        events.append(TraceEvent(f"{indent(depth)}goal  {goal}"))
        visited_goals.append(goal)

        for fact in kb.facts:
            theta = unify(goal, fact, subst)
            if theta is not None:
                events.append(TraceEvent(f"{indent(depth)}fact   {fact}  {format_subst(theta)}"))
                return theta

        for rule in kb.rules:
            counter[0] += 1
            fresh = _standardize(rule, counter[0])
            theta = unify(goal, fresh.head, subst)
            if theta is None:
                continue
            events.append(TraceEvent(f"{indent(depth)}rule   {rule.rule_id}  {format_subst(theta)}"))
            answer = bc_and(fresh.premises, theta, depth + 1, stack + (key,))
            if answer is not None:
                return answer
        events.append(TraceEvent(f"{indent(depth)}fail   {goal}"))
        return None

    def bc_and(premises: tuple[Atom, ...], subst: dict[str, str], depth: int, stack: tuple[str, ...]) -> dict[str, str] | None:
        if not premises:
            return subst
        first, rest = premises[0], premises[1:]
        theta = bc_or(first, subst, depth, stack)
        if theta is None:
            return None
        return bc_and(rest, theta, depth, stack)

    found = bc_or(query, {}, 0, ())
    proved = found is not None
    events.append(TraceEvent("Query proved." if proved else "Query not proved."))
    # Backward chaining does not add facts; report goals visited instead.
    unique_goals = []
    seen = set()
    for g in visited_goals:
        if str(g) not in seen:
            seen.add(str(g))
            unique_goals.append(g)
    return InferenceResult(proved, found, unique_goals, events)
