def is_valid_pw(pw):
	words = pw.split()

	for word in words:
		if words.count(word) > 1:
			return False

	return True

def is_valid_anagramless_pw(pw):
	words = pw.split()

	for word in words:
		word_list = words[:]
		word_list.remove(word)
		if contains_anagrams(word_list, word):
			return False

	return True

def contains_anagrams(words, check_word):
	for word in words:
		if is_anagram(word, check_word):
		 	return True

def is_anagram(word, check_word):
	list1 = list(word)
	list2 = list(check_word)

	list1.sort()
	list2.sort()

	return list1 == list2

if __name__ == '__main__':
	valid = 0
	invalid = 0

	valid_anagramless = 0
	invalid_anagramless = 0

	with open('input-04.txt') as file:
		for line in file:
			if is_valid_pw(line.rstrip('\n')):
				valid += 1
			else:
				invalid += 1

			if is_valid_anagramless_pw(line.rstrip('\n')):
				valid_anagramless += 1
			else:
				invalid_anagramless += 1

	print('valid:', valid)
	print('invalid:', invalid)

	print('valid anagramless:', valid_anagramless)
	print('invalid anagramless:', invalid_anagramless)