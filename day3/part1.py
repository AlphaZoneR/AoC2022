import string

INPUT_FILE_NAME = "input"

with open(INPUT_FILE_NAME, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    lines = [line for line in lines if line]


def calculate_priority(overlap):
    overlap = list(overlap)
    if overlap:
        if overlap[0] in string.ascii_lowercase:
            return ord(overlap[0]) - ord('a') + 1
        else:
            return ord(overlap[0]) - ord('A') + 27


components = [(set([*line[:int(len(line) / 2)]]),
               set([*line[int(len(line) / 2):]])) for line in lines]
overlaps = [component[0] & component[1] for component in components]
overlap_priorities = list(map(calculate_priority, overlaps))
print(sum(overlap_priorities))
