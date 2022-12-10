INPUT_FILE_NAME = "input"

with open(INPUT_FILE_NAME, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    lines = [line for line in lines if line]

WIN = 6
DRAW = 3
LOSE = 0

choice_map = {
    'A': 'Rock',
    'X': 'Rock',
    'B': 'Paper',
    'Y': 'Paper',
    'C': 'Scissors',
    'Z': 'Scissors',
}

score_map = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3,
}

beat_map = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper',
}


def decide_result(choice1, choice2) -> int:
    if choice1 == choice2:
        return DRAW
    elif beat_map[choice1] == choice2:
        return LOSE
    elif beat_map[choice2] == choice1:
        return WIN
    else:
        raise Exception('What?')


def evaluate_game(choices):
    choice1, choice2 = [choice_map[choice] for choice in choices.split(' ')]
    return decide_result(choice1, choice2) + score_map[choice2]


print(sum([evaluate_game(choices) for choices in lines]))
