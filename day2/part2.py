INPUT_FILE_NAME = "input"

with open(INPUT_FILE_NAME, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    lines = [line for line in lines if line]

WIN = 6
DRAW = 3
LOSE = 0

score_map = {
    'A': 1,
    'B': 2,
    'C': 3,
}

beat_map = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

beaten_by = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

action_map = {
    'X': (lambda opponent_choice: beat_map[opponent_choice]),
    'Y': (lambda opponent_choice: opponent_choice),
    'Z': (lambda opponent_choice: beaten_by[opponent_choice])
}

action_score_map = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN
}


def evaluate_game(choices):
    opponent_choice, required_action = choices.split(' ')
    my_choice = action_map[required_action](opponent_choice)
    my_choice_score = score_map[my_choice]
    my_action_score = action_score_map[required_action]

    return my_choice_score + my_action_score


print(sum([evaluate_game(choices) for choices in lines]))
