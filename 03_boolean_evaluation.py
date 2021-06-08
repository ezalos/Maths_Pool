def value(operator: str, queue: list, debug=False) -> list:
	operator = int(operator) == 1
	queue.append(operator)
	if debug:
		print(f"VALUEs: {queue}")
	return queue

def operation(operator: str, queue: list, debug=False) -> list:
	q_len = len(queue)
	error_msg = f"There is not enought numbers ({q_len}) in queue for {operator} operation"
	if q_len < 1:
		raise ValueError(error_msg)
	a = queue[0]
	if operator == "!":
		if debug:
			print(f"OPERATION: {operator} {a}")
		a = not a
	else:
		if q_len < 2:
			raise ValueError(error_msg)
		b = queue.pop(1)
		if debug:
			print(f"OPERATION: {a} {operator} {b}")
		if operator == "&":
			a = a & b
		elif operator == "|":
			a = a | b
		elif operator == "^":
			a = a ^ b
		elif operator == ">":
			a = (a == True and b == False) == False
		elif operator == "=":
			a = (a == b)
	queue[0] = a
	if debug:
		print(f"{' ' * 9}= {a}")
	return queue

def eval_formula(formula: str, debug=False) -> bool:
	exp_len = len(formula)
	if exp_len <= 0:
		return None
	elif exp_len == 1:
		try:
			return int(formula[0]) == 1
		except:
			return None
	elif exp_len == 2:
		return None
	queue = []
	for l in formula:
		if l in "01":
			queue = value(l, queue, debug)
		elif l in "!&|^>=":
			queue = operation(l, queue, debug)
		else:
			raise ValueError(f"Error: eval_formula -> {l} is not a valid operator")
	return queue[0] == 1

if __name__ == "__main__":
	tests = {
		"10&": False,
		"10|": True,
		"11>": True,
		"10=": False,
		"1011||=": True,
		"1": True,
		"0": False
	}
	for test, solution in tests.items():
		answer = eval_formula(test, debug=False)
		print(f"{test} -> {answer}")
		if answer != solution:
			print(f"Error: eval_formula({test}) -> {answer} BUT it should be {solution}")
		print()