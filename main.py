from fractions import Fraction

print("*" * 51 + "\n\nWelcome to AkaTeam calculus.\n\n" + "*" * 51 + "\n")

def derive_term(term, sign):
	while term[-1] == " ": ########## Makes sure there are no spaces before or after term
		term = term[:-1]
	while term[0] == " ":
		term = term[1:]
	
	coefficient = 0
	exponent = 0

	char_number = 0 ########## Used to know index place in string
	
	for char in term:
		if char == "x":
			if char_number == 0:
				if sign == 1:
					coefficient = 1
				
				else:
					coefficient = -1
			
			else:
				coefficient = int(term[:char_number])
		
		elif char == "^":
			exponent = int(term[char_number + 1:])
			
		char_number += 1
	
	new_coefficient = str(coefficient * exponent)
	new_exponent = exponent - 1
	
	if "x" not in term: ########## If the term is a constant
		new_term = ""
	
	elif "^" not in term: ########## If x has degree 1
		new_term = " + " + str(sign * coefficient)
	
	else:
		if new_exponent == 1:
			new_term = " + " + str(sign * int(new_coefficient)) + "x"
		
		else:
			new_term = " + " + str(sign * int(new_coefficient)) + "x^" + str(new_exponent)

	new_term = new_term.replace("+ -", "- ")
	return str(new_term)

def integrate_term(term, sign):
	while term[-1] == " ": ########## Makes sure there are no spaces before or after term
		term = term[:-1]
	while term[0] == " ":
		term = term[1:]
	
	coefficient = 0
	exponent = 0

	char_number = 0 ########## Used to know index place in string
	
	for char in term:
		if char == "x":
			if char_number == 0:
				if sign == 1:
					coefficient = 1
				
				else:
					coefficient = -1
			
			else:
				coefficient = int(term[:char_number])
			exponent += 1
		
		elif char == "^":
			exponent = int(term[char_number + 1:])
			
		char_number += 1
	
	new_exponent = exponent + 1
	
	if new_exponent == 0:
		new_coefficient = str(sign * coefficient)
	
	elif new_exponent == 1:
		new_coefficient = str(sign * int(term))
	
	else:
		if coefficient / new_exponent % 1 == 0:
			new_coefficient = str(int(sign * coefficient / new_exponent))
			
			if new_coefficient == "1":
				new_coefficient = ""
		
		else:
			new_coefficient = "(" + str(sign * Fraction(sign * coefficient, new_exponent)) + ")"
	
	if "x" not in term: ########## If the term is a constant
		new_term = " + " + new_coefficient + "x"
	
	elif "^" not in term: ########## If x has degree 1
		new_term = " + " + new_coefficient + "x^2"
	
	else:
		if new_exponent == 1:
			new_term = " + " + str(new_coefficient) + "x"
		
		else:
			if new_exponent == 0:
				new_term = " + " + str(new_coefficient) + "(ln(|x|))"
			
			else:
				new_term = " + " + str(new_coefficient) + "x^" + str(new_exponent)

	return str(new_term)

def derive_polynomial(polynomial):
	terms_and_signs = polynomial.split(" ") ########## Splits polynomial into characters between spaces 
	
	if "" in terms_and_signs:
		terms_and_signs.remove("")
	if " " in terms_and_signs:
		terms_and_signs.remove(" ")
	
	terms = []
	signs = []
	
	while terms_and_signs != []: ########## Create terms list and signs list from polynomial
		if terms_and_signs[0] == "+": ########## Positive coefficient
			signs.append(1)
			terms_and_signs.remove(terms_and_signs[0])
			
		elif terms_and_signs[0] == "-": ########## Negative coefficient
			signs.append(-1)
			terms_and_signs.remove(terms_and_signs[0])
			
		else:    # If the item in the list is not a + or -, add it to the new list of terms
			terms.append(terms_and_signs[0])
			terms_and_signs.remove(terms_and_signs[0])
	
	if len(signs) < len(terms): ########## If the first term is not preceded by a minus, it must be positive
		signs.insert(0, 1)
	
	derivative = ""
	sign_to_use = 0 ########## Index for what sign to match with each term
	
	for term in terms:
		derivative += derive_term(term, signs[sign_to_use])
		sign_to_use += 1
	
	while derivative[0] == " " or derivative[0] == "+": ########## Makes sure there are no spaces or signs in front of the result
		derivative = derivative[1:]
	
	return derivative

def integrate_polynomial_indefinite(polynomial, definite):
	terms_and_signs = polynomial.split(" ") ########## Splits polynomial into characters between spaces 
	
	if "" in terms_and_signs:
		terms_and_signs.remove("")
	
	elif " " in terms_and_signs:
		terms_and_signs.remove(" ")
	
	terms = []
	signs = []
	
	while terms_and_signs != []: ########## Create terms list and signs list from polynomial
		if terms_and_signs[0] == "+": ########## Positive coefficient
			signs.append(1)
			terms_and_signs.remove(terms_and_signs[0])
		
		elif terms_and_signs[0] == "-": ########## Negative coefficient
			signs.append(-1)
			terms_and_signs.remove(terms_and_signs[0])
		
		else:    # If the item in the list is not a + or -, add it to the new list of terms
			terms.append(terms_and_signs[0])
			terms_and_signs.remove(terms_and_signs[0])
	
	if len(signs) < len(terms): ########## If the first term is not preceded by a minus, it must be positive
		signs.insert(0, 1)
	
	integral = ""
	sign_to_use = 0 ########## Index for what sign to match with each term
	
	for term in terms:
		integral += integrate_term(term, signs[sign_to_use])
		sign_to_use += 1
	
	integral = integral.replace("+ -", "- ") ########## Makes sure result does not display a "+ -"
	integral = integral.replace("+ (-", "- (")
	
	while integral[0] == " " or integral[0] == "+": ########## Makes sure there are no spaces or signs in front of the result
		integral = integral[1:]
	
	if definite == False: ########## Don't add + C if this function is called from integrate_polynomial_definite
	  integral += " + C, where C ∈ ℝ"
	
	return integral

def integrate_polynomial_definite(polynomial, lower, upper):
  upper_equation = str(integrate_polynomial_indefinite(polynomial, True)).replace("x", "(" + str(upper) +")")
  lower_equation = str(integrate_polynomial_indefinite(polynomial, True)).replace("x", "(" + str(lower) +")")
  
  final_equation = upper_equation + " - " + lower_equation
  print("\n",final_equation, "\n\nEnter that on a calculator. This program doesn't do real math.")

def home():
	user_input = input("\n Derivative is 1 and Integral is 2. ")

	while user_input != "1" and user_input != "2":
		user_input = input("\nPlease enter 1 or 2.")
		
	if user_input == "1":
		user_input = input("\nEnter 1 to take the derivative of a polynomial or 2 to take the derivative of a more complex function (does not work yet).")
	
		while user_input != "1" and user_input != "2":
			user_input = input("\nPlease enter 1 or 2.")
		
		if user_input == "1":
		  polynomial = input("\nEnter your polynomial. Make sure to separate all terms with spaces. Example: - 8x^9 + 12x^3 + 3x + 7 + 9x^-1\n\nd/dx")
		  derivative = derive_polynomial(polynomial)
		  print("\n= " + str(derivative) + "\n")
		
		elif user_input == "2":
			print("\nThis is a work in progress. This feature is not yet added.")
	
	elif user_input == "2":
		user_input = input("\nEnter 1 to take an indefinite integral or 2 to take a definite integral.")
		
		while user_input != "1" and user_input != "2":
			user_input = input("\nPlease enter 1 or 2.")
		
		if user_input == "1": ########## Indefinite Integral
			user_input = input("\nEnter 1 to take the indefinite integral of a polynomial or 2 to take the indefinite integral of a more complex function.")
		
			while user_input != "1" and user_input != "2":
				user_input = input("\nPlease enter 1 or 2.")
			
			if user_input == "1": ########## Indefinite Integral Polynomial
			  polynomial = input("\nEnter your polynomial. Make sure to separate all terms with spaces. Example: ∫ - 3x^3 + 8x^2 + x + 5 + 2x^-1\n\n∫")
			  integral = integrate_polynomial_indefinite(polynomial, False)
			  print("\n= " + str(integral) + "\n")
			
			elif user_input == "2": ########## Indefinite Integral Complex
				print("\nThis is a work in progress. This feature is not yet added.")
		
		elif user_input == "2": ########## Definite Integral Polynomial
			polynomial = input("\nEnter your polynomial. Make sure to separate all terms with spaces. Example: ∫ - 3x^3 + 8x^2 + x + 5 + 2x^-1\n\n∫")
			lower = input("\nEnter the range over which to integrate.\nLower bound: ")
			upper = input("Upper bound:")
			integrate_polynomial_definite(polynomial, lower, upper)

home()