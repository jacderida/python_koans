#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    sides = sorted([a, b, c])
    side_a = sides[0];
    side_b = sides[1];
    side_c = sides[2];

    if side_a <= 0:
        raise TriangleError("A triangle cannot have a side less than or equal to 0.")
    if side_a + side_b <= side_c:
        raise TriangleError("The sides of the triangle must be consistent")
    if side_a == side_c:
        return 'equilateral'
    elif side_a == side_b or side_b == side_c:
        return 'isosceles'
    else:
        return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
