def is_valid_pw(pw):
	words = pw.split()

	for word in words:
		if words.count(word) > 1:
			return False

	return True

if __name__ == '__main__':
	valid = 0
	invalid = 0

	with open('input-04.txt') as file:
		for line in file:
			if is_valid_pw(line.rstrip('\n')):
				valid += 1
			else:
				invalid += 1

	print('valid:', valid)
	print('invalid:', invalid)