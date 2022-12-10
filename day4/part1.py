INPUT_FILE_NAME = "input"


class Range(object):
    begin: int
    end: int

    def __init__(self, b: int, e: int):
        self.begin = b
        self.end = e

    def contains(self, other: 'Range'):
        return self.begin <= other.begin and self.end >= other.end

    def __repr__(self):
        return f'{self.begin}-{self.end}'

    def __str__(self):
        return f'{self.begin}-{self.end}'


def to_range(text_repr) -> Range:
    begin, end = [int(id) for id in text_repr.split('-')]
    return Range(begin, end)


with open(INPUT_FILE_NAME, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    lines = [line for line in lines if line]


pairs = [(to_range(line.split(',')[0]), to_range(line.split(',')[1]))
         for line in lines]
overlapping_pairs = [pair for pair in pairs if pair[0].contains(
    pair[1]) or pair[1].contains(pair[0])]
print(overlapping_pairs)

print(len(overlapping_pairs))
