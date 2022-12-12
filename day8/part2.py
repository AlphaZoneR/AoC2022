# --- Part Two ---
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their
# tree house: they would like to be able to see a lot of trees.
# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if
# you reach an edge or at the first tree that is the same height or taller than the tree under consideration.
# (If a tree is right on the edge, at least one of its viewing distances will be zero.)
# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house
# has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.
# In the example above, consider the middle 5 in the second row:
# 30373 25512 65332 33549 35390
#     Looking up, its view is not blocked; it can see 1 tree (of height 3). Looking left, its view is blocked
#     immediately; it can see only 1 tree (of height 5, right next to it). Looking right, its view is not
#     blocked; it can see 2 trees. Looking down, its view is blocked eventually; it can see 2 trees (one of
#     height 3, then the tree of height 5 that blocks its view).
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.
# For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).
# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:
# 30373 25512 65332 33549 35390
#     Looking up, its view is blocked at 2 trees (by another tree with a height of 5). Looking left, its view
#     is not blocked; it can see 2 trees. Looking down, its view is also not blocked; it can see 1 tree.
#     Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.
# Consider each tree on your map. What is the highest scenic score possible for any tree?

import typing
from dataclasses import dataclass, field
from enum import Enum
from functools import reduce

from utils import get_lines

MAX_HEIGHT = 9

INPUT = 'day8/example'
# INPUT = 'day8/input'


Direction = Enum('Direction', ['UP', 'RIGHT', 'DOWN', 'LEFT'])


@dataclass
class Tree(object):
    height: int
    visible: bool = False
    visibility_distances: typing.Dict[Direction, int] = field(
        default_factory=lambda: {})

    def __repr__(self):
        try:
            return f'[{self.height} {"■" if self.visible else "□"} {self.score}]'
        except:
            return f'[{self.height} {"■" if self.visible else "□"}]'

    @property
    def score(self):
        for direction in list(Direction):
            if direction not in self.visibility_distances:
                raise Exception(f'Distance for {direction} was not set.')

        return reduce(lambda elem, mul: elem * mul, [self.visibility_distances[direction] for direction in list(Direction)], 1)


lines = get_lines(INPUT, trim=True)
forest = [[Tree(int(tree)) for tree in [*line]] for line in lines]

for edge_tree in forest[0]:
    edge_tree.visible = True
    edge_tree.visibility_distances[Direction.UP] = 0

for edge_tree in forest[-1]:
    edge_tree.visible = True
    edge_tree.visibility_distances[Direction.DOWN] = 0

for edge_tree in [forest[i][0] for i in range(len(forest))]:
    edge_tree.visible = True
    edge_tree.visibility_distances[Direction.LEFT] = 0

for edge_tree in [forest[i][-1] for i in range(len(forest))]:
    edge_tree.visible = True
    edge_tree.visibility_distances[Direction.RIGHT] = 0

for row in forest:
    # Left to right pass
    max_height = row[0].height

    for (index, tree) in enumerate(row):
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height
            tree.visibility_distances[Direction.LEFT] = index
        else:
            tree.visibility_distances[Direction.LEFT] = 0

    max_height = row[-1].height

    # Right to left pass
    for (index, tree) in enumerate(row[::-1]):
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height
            tree.visibility_distances[Direction.RIGHT] = index
        else:
            tree.visibility_distances[Direction.RIGHT] = 0


for i in range(len(forest[0])):
    column = [forest[j][i] for j in range(len(forest))]

    # Top to bottom pass
    max_height = column[0].height

    for (index, tree) in enumerate(column):
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height
            tree.visibility_distances[Direction.UP] = index
        else:
            tree.visibility_distances[Direction.UP] = 0

    max_height = column[-1].height

    # Bottom to top pass
    for (index, tree) in enumerate(column[::-1]):
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height
            tree.visibility_distances[Direction.DOWN] = index
        else:
            tree.visibility_distances[Direction.DOWN] = 0

nr_visible = 0
for row in forest:
    for tree in row:
        if tree.visible:
            nr_visible += 1
    print(row)
print(forest[0][0].score)
print(nr_visible)
print(forest[3][1].visibility_distances)