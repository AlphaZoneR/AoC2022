def get_lines(filename: str, trim=False):
    with open(filename, 'r') as f:
        lines = [line.replace('\n', '') for line in f.readlines() if line.strip()]

        if trim:
            lines = [line.strip() for line in lines]

    return lines
