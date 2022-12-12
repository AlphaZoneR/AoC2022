# --- Day 8: Treetop Tree House ---
# The expedition comes across a peculiar patch of tall trees
# all planted carefully in a grid. The Elves explain that a previous expedition planted these
# trees as a reforestation effort. Now, they're curious if this would be a good location for
# a tree house.
# First, determine whether there is enough tree cover here to keep a tree house hidden. To do
# this, you need to count the number of trees that are visible from outside the grid when looking
# directly along a row or column.
# The Elves have already launched a quadcopter to generate a map with the height of each tree
# (your puzzle input). For example:
# 30373
# 25512
# 65332
# 33549
# 35390
#
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest
# and 9 is the tallest.
# A tree is visible if all of the other trees between it and an edge of the grid are shorter
# than it. Only consider trees in the same row or column; that is, only look up, down, left,
# or right from any given tree.
# All of the trees around the edge of the grid are visible - since they are already on the edge,
# there are no trees to block the view. In this example, that only leaves the interior nine
# trees to consider:
#
# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom
# since other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to
# only be trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be
# only trees of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
#
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees
# are visible in this arrangement.
# Consider your map; how many trees are visible from outside the grid?
#
from dataclasses import dataclass, field

from utils import get_lines

MAX_HEIGHT = 9

# INPUT = 'day8/example'
INPUT = 'day8/input'


@dataclass
class Tree(object):
    height: int
    visible: bool = False

    def __repr__(self):
        return f'{self.height} {"■" if self.visible else "□"}'


lines = get_lines(INPUT, trim=True)
forest = [[Tree(int(tree)) for tree in [*line]] for line in lines]

for edge_tree in [*forest[0], *forest[-1], *[forest[i][0] for i in range(len(forest))], *[forest[i][-1] for i in range(len(forest))]]:
    edge_tree.visible = True


for row in forest:
    # Left to right pass
    max_height = row[0].height

    for tree in row:
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height

    max_height = row[-1].height

    # Right to left pass
    for tree in row[::-1]:
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height

for i in range(len(forest[0])):
    # Top to bottom pass
    column = [forest[j][i] for j in range(len(forest))]

    # Left to right pass
    max_height = column[0].height

    for tree in column:
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height

    max_height = column[-1].height

    # Right to left pass
    for tree in column[::-1]:
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height

nr_visible = 0
for row in forest:
    for tree in row:
        if tree.visible:
            nr_visible += 1

print(nr_visible)
