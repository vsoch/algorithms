# The Skyline Problem

Given n rectangular buildings in a 2-dimensional city, computes the skyline of these buildings, eliminating hidden lines. The main task is to view buildings from a side and remove all sections that are not visible.

All buildings share common bottom and every building is represented by triplet (left, ht, right)

 - 'left': is x coordinated of left side (or wall).
 - 'right': is x coordinate of right side
 - 'ht': is height of building.

A skyline is a collection of rectangular strips. A rectangular strip is represented as a pair (left, ht) where left is x coordinate of left side of strip and ht is height of strip.

buildings = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25),
            (19,18,22), (23,13,29), (24,4,28) ]

## Assumptions

 - the building list isn't ordered in any particular way


I think it would be a lot easier if we can put the buildings in a defined space first. For the
complete problem, see [the notebook](the-skyline-problem.ipynb)
