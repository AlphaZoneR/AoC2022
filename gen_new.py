import os
import pathlib
import requests
from bs4 import BeautifulSoup
import json

COMMENT_LINE_LENGTH = 90
ADVENT_OF_CODE_URL = 'https://adventofcode.com/2022/day'
HEADERS_JSON = 'headers.json'


def limit_lines_to_length(input_lines, line_length=COMMENT_LINE_LENGTH):
    reformatted_lines = []

    for line in input_lines:
        remaining_line = line
        while len(remaining_line) > line_length and ' ' in remaining_line[line_length:]:
            remaining_text = ''.join(remaining_line[line_length:])
            index_of_next_space = remaining_text.index(' ')
            index_of_space_to_split_by = line_length + index_of_next_space
            new_line = remaining_line[:index_of_space_to_split_by]
            reformatted_lines.append(new_line.strip())
            remaining_line = remaining_line[index_of_space_to_split_by:]

        reformatted_lines.append(remaining_line.strip())

    return reformatted_lines


max_day = [*sorted([f for f in os.listdir(os.curdir) if 'day' in f],
                   key=lambda f: int(f.split('day')[1]))][-1]
max_day_number = int(max_day.split('day')[1])

next_day_number = max_day_number + 1

next_day_folder_name = f'day{next_day_number}'

next_day_folder = pathlib.Path(os.curdir).joinpath(
    pathlib.Path(next_day_folder_name))
next_day_folder.mkdir()

example_file_path = next_day_folder.joinpath('example')
input_file_path = next_day_folder.joinpath('input')
part1_file_path = next_day_folder.joinpath('part1.py')
part2_file_path = next_day_folder.joinpath('part2.py')


day_description_url = f'{ADVENT_OF_CODE_URL}/{next_day_number}'
day_input_url = f'{day_description_url}/input'

with pathlib.Path(os.curdir).joinpath(HEADERS_JSON).open('r') as f:
    headers = json.loads(f.read())

print('Acquiring description:', day_description_url)
response = requests.get(url=day_description_url, headers=headers)
parser = BeautifulSoup(response.text, 'html.parser')

day_desc = parser.find('article', class_='day-desc')
desc_lines = day_desc.get_text().split('\n')
reformatted_desc_lines = limit_lines_to_length(desc_lines)
printable_desc_lines = '\n'.join(
    f'# {line}' for line in reformatted_desc_lines)

template_code = f'''{printable_desc_lines}
from utils import get_lines
INPUT = '{next_day_folder_name}/example'
# INPUT = '{next_day_folder_name}/input'

lines = get_lines(INPUT, trim=True)
print(lines)
'''

print('Acquiring input:', day_input_url)
day_input = requests.get(day_input_url, headers=headers).text

with example_file_path.open('w') as f:
    pass

with input_file_path.open('w') as f:
    f.write(day_input)

with part1_file_path.open('w') as f:
    f.write(template_code)

with part2_file_path.open('w') as f:
    f.write(template_code)
