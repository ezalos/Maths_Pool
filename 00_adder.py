def adder(a:int, b:int) -> int:
	while b:
		xor = a ^ b
		_and = (a & b) << 1
		a = xor
		b = _and
	return a

if __name__ == "__main__":
	for i in range(2 ** 8):
		for ii in range(1024):
			true = i + ii
			test = adder(i, ii)
			if true != test:
				print(f"Adding: {i:b} + {ii:b}") 
				print(f"\tTrue: {true:b}") 
				print(f"\tTest: {test:b}") 