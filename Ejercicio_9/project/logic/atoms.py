"""Parse atoms, substitutions, and unification."""

from __future__ import annotations

import re
from dataclasses import dataclass

_ATOM = re.compile(r"^([A-Za-z_][\w]*)\s*(?:\((.*)\))?\s*$")


@dataclass(frozen=True)
class Atom:
    """A predicate applied to terms. Example: Gato(Tom), Mortal(x)."""

    predicate: str
    args: tuple[str, ...]

    def __str__(self) -> str:
        if not self.args:
            return self.predicate
        return f"{self.predicate}({', '.join(self.args)})"


def is_variable(term: str) -> bool:
    """Lowercase first letter = variable (AIMA math notation: x, y, z)."""
    return bool(term) and term[0].islower()


def parse_atom(text: str) -> Atom:
    text = text.strip()
    match = _ATOM.match(text)
    if not match:
        raise ValueError(f"cannot parse atom: {text!r}")
    predicate, raw_args = match.group(1), match.group(2)
    if raw_args is None or raw_args.strip() == "":
        return Atom(predicate, ())
    args = tuple(part.strip() for part in raw_args.split(","))
    if any(not part for part in args):
        raise ValueError(f"empty argument in atom: {text!r}")
    return Atom(predicate, args)


def apply_term(term: str, subst: dict[str, str]) -> str:
    seen: set[str] = set()
    while is_variable(term) and term in subst and term not in seen:
        seen.add(term)
        term = subst[term]
    return term


def apply_atom(atom: Atom, subst: dict[str, str]) -> Atom:
    return Atom(atom.predicate, tuple(apply_term(a, subst) for a in atom.args))


def _occurs(var: str, term: str, subst: dict[str, str]) -> bool:
    term = apply_term(term, subst)
    if var == term:
        return True
    return False


def unify(a: Atom | str, b: Atom | str, subst: dict[str, str] | None = None) -> dict[str, str] | None:
    """Return an MGU substitution, or None if unification fails."""
    if subst is None:
        subst = {}
    else:
        subst = dict(subst)

    if isinstance(a, Atom) and isinstance(b, Atom):
        if a.predicate != b.predicate or len(a.args) != len(b.args):
            return None
        for left, right in zip(a.args, b.args):
            subst = unify(left, right, subst)
            if subst is None:
                return None
        return subst

    if isinstance(a, Atom) or isinstance(b, Atom):
        return None

    a = apply_term(a, subst)
    b = apply_term(b, subst)
    if a == b:
        return subst
    if is_variable(a):
        if _occurs(a, b, subst):
            return None
        subst[a] = b
        return subst
    if is_variable(b):
        if _occurs(b, a, subst):
            return None
        subst[b] = a
        return subst
    return None


def format_subst(subst: dict[str, str]) -> str:
    if not subst:
        return "{}"
    parts = ", ".join(f"{k}/{v}" for k, v in sorted(subst.items()))
    return "{" + parts + "}"
