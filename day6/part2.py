# --- Part Two ---
# Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.
# 
# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.
# 
# Here are the first positions of start-of-message markers for all of the above examples:
# 
# mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
# How many characters need to be processed before the first start-of-message marker is detected?

from utils import get_lines
# INPUT = 'day6/example'
INPUT = 'day6/input'

REQUIRED_DIFFERENT_CHARACTERS = 14

lines = get_lines(INPUT, trim=True)
line = lines[0]

for i in range(len(line) - REQUIRED_DIFFERENT_CHARACTERS):
    if len(set([*line[i:i+REQUIRED_DIFFERENT_CHARACTERS]])) == REQUIRED_DIFFERENT_CHARACTERS:
        print(i + REQUIRED_DIFFERENT_CHARACTERS)
        break