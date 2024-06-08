import inflationrate as ir
import generaldata as gd
Age = int(input("Enter your age ")) #22
inflationmatching = str(input("Do they match your salary to inflation? "))
year_of_birth = gd.current_year - Age
year = year_of_birth + Age

def calculator(init_inv, choose, next_inv, r, j, inflationmatching):
	calculator.i = 0
	calculator.year = init_inv
	inflationrate = ir.inflationrate
	if inflationmatching == 'no':
		inflationmatching = 1/inflationrate
	else:
		inflationmatching = 1

	while calculator.i < choose:
		calculator.i += 1
		calculator.year = calculator.year*r
		calculator.year = calculator.year + next_inv
		next_inv = next_inv*inflationrate*inflationmatching
		print(f"investment year: {calculator.i+10*(investmentcalculator.j-1)}, investment amount: {int(calculator.year)}, \
age: {Age+10*(investmentcalculator.j-1)+calculator.i}, year: {year+10*(investmentcalculator.j-1)+calculator.i}")
	
	total_spent = init_inv+next_inv*calculator.i
	print(f"""the final investment amount after {calculator.i} years is {int(calculator.year)}$ USD
	Total spent: {int(total_spent)}
	Total made: {int(calculator.year-total_spent)}
	The total amount is {int(calculator.year/(ir.inflationrate**(calculator.i)))}$ USD in today's worth. \
	the total made is  {(calculator.year-total_spent)/(ir.inflationrate**(calculator.i))}$ in today's worth. \
	My age at this point is {Age+calculator.i*investmentcalculator.j}""")


#calculator(100000, 10, 100000, 1.08)

def investmentcalculator(init_inv, choose, next_inv, r, gos_at_it, roi_growth, income_growth, inflationmatching):
	investmentcalculator.j = 1
	roi_growth = roi_growth+investmentcalculator.j*0.01
	calculator(init_inv, choose, next_inv, r, investmentcalculator.j, inflationmatching)
	while investmentcalculator.j < gos_at_it:	
		investmentcalculator.j += 1
		print(f"""																																																					
		the new ratio is {r*roi_growth+investmentcalculator.j*0.01}
		the new yearly investment is {next_inv*income_growth*investmentcalculator.j}
		the {choose} year investment plan started with {calculator.year}
																		""")
		calculator(calculator.year, choose, next_inv*income_growth*investmentcalculator.j, r*roi_growth, investmentcalculator.j, inflationmatching)
#I know r*roi_growth only tops up once but It's actually better this way.		



investmentcalculator(100000, 10, 50000, 1.08, 3, 1.01, 1.5, inflationmatching)

print(f"""I will have {int(calculator.year)}$ USD at the age of {Age+investmentcalculator.j*calculator.i}
That is worth {int(calculator.year/(ir.inflationrate**(investmentcalculator.j*calculator.i)))}$ USD now.""")