from utils import get_lines
import typing
import re

INPUT = "./day5/input"


class StackHolder(object):
    stacks: typing.List[typing.List[str]]

    def __init__(self) -> None:
        self.stacks = []

    def add_stack(self, stack: typing.List[str]):
        self.stacks.append(stack)

    def move(self, number_of_crates_to_move, from_index, to_index):
        assert from_index < len(self.stacks), 'from_index out of bounds'
        assert to_index < len(self.stacks), 'to_index out of bounds'
        assert number_of_crates_to_move <= len(
            self.stacks[from_index]), f'not enough crates on stack: {len(self.stacks[from_index])}'

        crates_to_move = self.stacks[from_index][-number_of_crates_to_move:][::-1]
        self.stacks[from_index] = self.stacks[from_index][:-number_of_crates_to_move]
        self.stacks[to_index] = [*self.stacks[to_index], *crates_to_move]

    def __repr__(self) -> str:
        result = ''
        for (index, stack) in enumerate(self.stacks):
            result += f'{index + 1} {" ".join(stack)}'

            if index + 1 < len(self.stacks):
                result += '\n'
        top = ''.join([stack[-1] for stack in self.stacks if len(stack) > 0])
        result += f'\ntop={top}'
        result += '\n----'
        return result

    def __str__(self) -> str:
        return self.__repr__()


lines = get_lines(INPUT)

stack_input = []
move_lines = []
for line in lines:
    if 'move' in line:
        move_lines.append(line)
    else:
        stack_input.append(line)

moves = [re.findall('move (\d+) from (\d+) to (\d+)', move_line)[0]
         for move_line in move_lines]
moves: typing.Tuple[int, int, int] = [
    (int(m[0]), int(m[1]) - 1, int(m[2]) - 1) for m in moves]

crates: typing.List[str] = stack_input[:-1]
index_line: str = stack_input[-1]

stack_holder = StackHolder()

for (follow_through_index, index) in enumerate(index_line):
    if index.strip():
        crates_for_index = [crate[follow_through_index]
                            for crate in crates if crate[follow_through_index].strip()]
        stack_holder.add_stack(crates_for_index[::-1])

for (index, move) in enumerate(moves):
    stack_holder.move(*move)

print(stack_holder)
