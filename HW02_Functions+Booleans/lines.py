# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def are_parallel(m1:float, b1:float, m2:float, b2:float) -> bool:
    return (m1 == m2) and (b1 != b2)


def are_same(m1:float, b1:float, m2:float, b2:float) -> bool:
    return (m1 == m2) and (b1 == b2)


def have_unique_intersection(m1:float, b1:float, m2:float, b2:float) -> bool:
    return m1 != m2


def have_intersection(m1:float, b1:float, m2:float, b2:float) -> bool:
    return have_unique_intersection(m1, b1, m2, b2) or are_same(m1, b1, m2, b2)


def x_intersect(m1:float, b1:float, m2:float, b2:float) -> float:
    assert have_unique_intersection(m1, b1, m2, b2), "ERROR!"
    x = -((b1 - b2) / (m1 - m2))
    return x


def y_intersect(m1:float, b1: float, m2:float, b2:float) -> float:
    assert have_unique_intersection(m1, b1, m2, b2), "ERROR!"
    x = x_intersect(m1, b1, m2, b2)
    y = (m1 * x) + b1

    return y