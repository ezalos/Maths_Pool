def adder(a:int, b:int) -> int:
	while b:
		_xor = a ^ b
		_and = (a & b) << 1
		a = _xor
		b = _and
	return a

if __name__ == "__main__":
	bin_digits = 8
	for i in range(2 ** bin_digits):
		for ii in range(2 ** bin_digits):
			true = i + ii
			test = adder(i, ii)
			if true != test:
				print(f"Adding: {i:b} + {ii:b}") 
				print(f"\tTrue: {true:b}") 
				print(f"\tTest: {test:b}") 