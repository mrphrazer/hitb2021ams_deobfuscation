#!/usr/bin/python3
from miasm.expression.expression import ExprId, ExprInt
from msynth import Simplifier


def mba():
    x = ExprId("x", 32)
    y = ExprId("y", 32)
    return (x ^ y) + ExprInt(2, 32) * (x & y)


# MBA expression
expr = mba()

# define pre-computed oracle
oracle_path = "./oracle.pickle"

# initialize simplifier -- enforce SMT solver equivalence checks
simplifier = Simplifier(oracle_path, enforce_equivalence=True)

# simplify expression
simplified = simplifier.simplify(expr)

print(f"original: {expr}")
print(f"simplified: {simplified}")
