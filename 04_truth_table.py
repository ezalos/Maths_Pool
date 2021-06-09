eval_formula = __import__('03_boolean_evaluation').eval_formula
import copy

def get_vars_in_formulas(formula: str, debug=False) -> list:
	v_names= "QWERTYUIOPASDFGHJKLZXCVBNM"
	var_list = []
	for var in v_names:
		if var in formula:
			var_list.append(var)
	var_list.sort()
	if debug:
		print(f"Variables present in equation {var_list}")
	return var_list

def combinatories(size, debug=False) -> list:
	# Could be done with a bianry number going up to (2**size - 1)
	# Could be done in recursivity with some magic
	# Could be done with itertools
	nx2 = (1 << size)
	for comb in range(nx2):
		comb_list = []
		for ii in range(size):
			mask = (comb & (1 << ii))
			True_False = (comb & mask) != 0
			comb_list.append(1 if True_False else 0)
		if debug:
			print(f"Comb is: {comb_list}")
		yield comb_list

def translate_formula(formula: str, var_list: list, comb: list, debug=False)-> str:
	new_formula = formula[:]
	for v, c in zip(var_list, comb):
		new_formula = new_formula.replace(v, str(c))
	if debug:
		print(f"Translated formula: {new_formula}")
	return new_formula

def nice_print(formula: str, var_list: list, truth_list: list)-> None:
	# Intro line
	msg = f"Formula: {formula}\n"
	# Header
	for i in range(len(var_list)):
		msg += "| " + var_list[i] + " "
	msg += "| " + "=" + " |\n"
	# Table
	for truth in truth_list:
		for t in truth:
			msg += "| " + str(t) + " "
		msg += "|\n"
	print(msg)

def truth_table(formula: str, debug=False) -> None:
	if debug:
		print(f"Equation: {formula}")
	var_list = get_vars_in_formulas(formula, debug=False)
	combs = combinatories(var_list, debug=debug)
	truth_list = []
	for comb in combinatories(len(var_list)):
		if debug:
			print(f"Combinatory: {comb}")

		new_formula = translate_formula(formula, var_list, comb, debug=debug)
		result =eval_formula(new_formula)
		comb.append(1 if result else 0)
		truth_list.append(comb)

	if debug:
		print(f"Truth table: {truth_list}")
	nice_print(formula, var_list, truth_list)

if __name__ == "__main__":
	test = "AB&C|"
	truth_table(test, debug=False)