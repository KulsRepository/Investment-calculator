inflationrate = 1.02
Age = 29 #my actual age is 22 but I will start making decent money at 29 due to my PhD studies.
year = 2002+29

def calculator(init_inv, choose, next_inv, r, j):
	calculator.i = 0
	calculator.year = init_inv

	while calculator.i < choose:
		calculator.i += 1
		calculator.year = calculator.year*r
		calculator.year = calculator.year + next_inv
		print(f"investment year: {calculator.i+10*(multicalc.j-1)}, investment amount: {int(calculator.year)}, \
age: {Age+10*(multicalc.j-1)+calculator.i}, year: {year+10*(multicalc.j-1)+calculator.i}")
	
	total_spent = init_inv+next_inv*calculator.i
	print(f"""the final investment amount after {calculator.i} years is {int(calculator.year)}$ USD
	Total spent: {total_spent}
	Total made: {calculator.year-total_spent}
	The total amount is {int(calculator.year/(inflationrate**(calculator.i)))}$ USD in today's worth.
	the total made is  {(calculator.year-total_spent)/(inflationrate**(calculator.i))}$ in today's worth.
	My age at this point is {Age+calculator.i*multicalc.j}""")

#this investment calculator calculates the same thing but the salary is adjusted for infation, this function is hence separate because not all jobs offer that.
def calculator2(init_inv, choose, next_inv, r, j):
	calculator.i = 0
	calculator.year = init_inv

	while calculator.i < choose:
		calculator.i += 1
		calculator.year = calculator.year*r
		calculator.year = calculator.year + next_inv
		next_inv = next_inv*inflationrate
		print(f"investment year: {calculator.i+10*(multicalc.j-1)}, new yearly investment input: {int(next_inv)}, \
investment amount: {int(calculator.year)}, age: {Age+10*(multicalc.j-1)+calculator.i}, year: {year+10*(multicalc.j-1)+calculator.i}")
	
	total_spent = init_inv+next_inv*calculator.i
	print(f"""the final investment amount after {calculator.i} years is {int(calculator.year)}$ USD
	Total spent: {total_spent}
	Total made: {calculator.year-total_spent}.
	My age at this point is {Age+calculator.i*multicalc.j}""")

#calculator(100000, 10, 100000, 1.08)

def multicalc(init_inv, choose, next_inv, r, gos_at_it, roi_growth, income_growth):
	multicalc.j = 1
	roi_growth = roi_growth+multicalc.j*0.01
	calculator(init_inv, choose, next_inv, r, multicalc.j)
	while multicalc.j < gos_at_it:	
		multicalc.j += 1
		print(f"""																																																					
		the new ratio is {r*roi_growth+multicalc.j*0.01}
		the new yearly investment is {next_inv*income_growth*multicalc.j}
		the {choose} year investment plan started with {calculator.year}
																																																									""")
		calculator(calculator.year, choose, next_inv*income_growth*multicalc.j, r*roi_growth, multicalc.j)
#I know r*roi_growth only tops up once but It's actually better this way.		


multicalc(100000, 10, 50000, 1.08, 3, 1.01, 1.5)

print(f"""I will have {int(calculator.year)}$ USD at the age of {Age+multicalc.j*calculator.i}
That is worth {int(calculator.year/(inflationrate**(multicalc.j*calculator.i)))}$ USD now.""")