with open('input', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

max_sum = 0
sum = 0

for element in lines:
    if element:
        sum += int(element)

    if not element:
        if sum > max_sum:
            max_sum = sum
        sum = 0

print(max_sum)
