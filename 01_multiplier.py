adder = __import__('00_adder')

def multiplier(a:int, b:int) -> int:
	res = 0
	for i in range(32):
		mult_bin = (((b >> i) & 1) * a) << i
		res = adder.adder(res, mult_bin)
	return res

if __name__ == "__main__":
	bin_digits = 8
	for i in range(2 ** bin_digits):
		for ii in range(2 ** bin_digits):
			true = i * ii
			test = multiplier(i, ii)
			if true != test:
				print(f"Adding: {i:b} + {ii:b}") 
				print(f"\tTrue: {true:b}") 
				print(f"\tTest: {test:b}") 