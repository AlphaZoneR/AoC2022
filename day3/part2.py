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


grouped_components = [lines[n:n+3] for n in range(0, len(lines), 3)]
grouped_components = [(set([*component[0]]), set([*component[1]]),
                       set([*component[2]])) for component in grouped_components]
overlaps = [component[0] & component[1] & component[2]
            for component in grouped_components]
print(sum(map(calculate_priority, overlaps)))
