INPUT = 325489

def test_spiral_pos():
	# result : numbers to get result
	test_cases = {
		0 : [1],
		1 : [2, 3, 4, 5, 6, 7, 8, 9],
		2 : [10, 13, 17, 21, 25],
		3 : [26, 40, 49],
		4 : [50, 69, 81],
		5 : [82, 110]
	}

	for result, numbers in test_cases.items():
		for num in numbers:
			if get_spiral_pos(num) != result:
				print('Unhealty test: get_spiral_pos(', num, ') =>', result)

def test_nearest_middle_num():
	# number : possilbe values
	test_cases = {
		2 : [1, 2],
		3 : [2, 4],
		4 : [4],
		5 : [4, 6],
		6 : [6],
		7 : [6, 8],
		9 : [8],
		10: [11]
	}

	for num, values in test_cases.items():
		result = get_nearest_middle_num(num)
		if result not in values:
			print('Unhealty test: get_nearest_middle_num(', num, ') =>', result)

def test_center_distance():
	test_cases = [
		(1, 0),
		(12, 3),
		(23, 2),
		(1024, 31)
	]

	for test_pair in test_cases:
		result = get_center_distance(test_pair[0])
		if result != test_pair[1]:
			print('Unhealty test: get_center_distance(', test_pair[0], ') =>', result)

# middle numbers are directly horizontal or vertical to 1
def get_nearest_middle_num(num):
	rotation = 0
	steps = 1
	last_middle = 1
	next_middle = 1

	while True:
		steps -= 1

		# first middle number of a rotation
		steps += (rotation + 1) * 2
		last_middle = next_middle
		next_middle = steps

		if last_middle <= num <= next_middle:
			return min([last_middle, next_middle], key=lambda x:abs(x-num))

		rotation += 1

		for _ in range(3):
			steps += rotation * 2
			last_middle = next_middle
			next_middle = steps

			if last_middle <= num <= next_middle:
				return min([last_middle, next_middle], key=lambda x:abs(x-num))


# returns the index of the rotation (i.e. radius) on which a given number is located
def get_spiral_pos(num):
	rotation = 0
	pos = 1

	while (num - pos) > 0:
		rotation += 1
		pos += rotation * 2 * 4

	return rotation

def get_center_distance(num):
	nearest_middle = get_nearest_middle_num(num)
	dist_nearest = abs(num - nearest_middle)
	dist_nearest_to_center = get_spiral_pos(num)

	return dist_nearest + dist_nearest_to_center


if __name__ == '__main__':
	print(get_center_distance(INPUT))