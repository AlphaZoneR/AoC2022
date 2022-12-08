with open('input', 'r') as f:
	lines = f.readlines()
	lines = [line.strip() for line in lines]

curr_sum = 0
curr_sums = []

for element in lines:
	if element:
		curr_sum += int(element)

	if not element:
		curr_sums.append(curr_sum)
		curr_sum = 0

top_3 = sorted(curr_sums, reverse=True)[:3]
print(sum(top_3))
