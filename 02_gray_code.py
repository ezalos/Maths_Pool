def gray_code(num: int) -> int:
	return num ^ (num >> 1)

if __name__ == "__main__":
	gray_codes = [0, 1, 3, 2, 6, 7, 5, 4, 12]

	for i, g in enumerate(gray_codes):
		test = gray_code(i)
		if g != test:
			print(f"Error for nb: {i}")
			print(f"\tTrue: {g:b}")
			print(f"\tTest: {test:b}")