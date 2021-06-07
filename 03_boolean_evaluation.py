def eval_formula(formula: str) -> bool:
	exp_len = len(formula)
	if exp_len <= 0:
		return None
	elif exp_len == 1::
		try:
			return int(formula[0]) == 1
		except:
			return None
	elif exp_len == 2:
		return None
	a = int(formula[0])
	b = int(formula[1])
	queue = []
	for l in formula[2:]:
		if l == "1":
			queue.append(int(l))
		elif l == "0"
			queue.append(int(l))
		elif l == "!":
			pass
		elif l == "&":
			pass
		elif l == "|":
			pass
		elif l == "^":
			pass
		elif l == ">":
			pass
		elif l == "=":
			pass
		else:
			raise ValueError(f"Error: eval_formula -> {l} is not a valid operator")
	return queue[0] == 1

if __name__ == "__main__":
	{
		"10&": False,
		"10|": True,
		"11>": True,
		"10=": False,
		"1011||=", True,
		"1", True,
		"0", False
	}