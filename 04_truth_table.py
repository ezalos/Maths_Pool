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

def combinatories(size) -> list:
	# NOT WORKING YET !!!

	# Could be done with a bianry number going up to (2**size - 1)
	# Could be done in recursivity with some magic
	# Could be done with itertools

	if len(vars) < 1:
		return vars_vals
	print(f"Vars = {vars}")
	print(f"vars_vals = {vars_vals}")
	vars_comb = []

	if vars_vals != []:
		vars_vals_true = copy.deepcopy(vars_vals)
		vars_vals_fals = copy.deepcopy(vars_vals)
	else:
		vars_vals_true = []
		vars_vals_fals = []

	vars_vals_true.append('1')
	print(f"vars_vals_true = {vars_vals_true}")
	ret = combinatories(vars[1:], vars_vals_true)
	vars_comb.expend(ret)

	vars_vals_fals.append('0')
	ret = combinatories(vars[1:], vars_vals_false)
	vars_comb.expend(ret)

	return vars_comb

def truth_table(formula: str, debug=False) -> None:
	if debug:
		print(f"Equation: {formula}")
	var_list = get_vars_in_formulas(formula, debug=False)
	combs = combinatories(var_list)
	if debug:
		print(f"Combinatories: {combs}")

if __name__ == "__main__":
	test = "AB&C|"
	truth_table(test, debug=True)