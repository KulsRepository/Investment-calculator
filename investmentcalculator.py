import inflationrate as ir
import generaldata as gd
import math
gos_at_it_list = []
Age = int(input("Enter your age ")) #22
inflationmatching = str(input("Do they match your salary to inflation? ")) #'yes'
init_inv = int(input("How much is your initial investment? "))
return_rate = float(input("What is your typical return rate? "))
next_inv = int(input("what is your yearly investment? "))
Director = str(input("""will you have only one long term investment plan with no cash out? Then type out 'no cash out'. Will you instead have similar sized sections with a cash out in between sections? 
Then type 'same size, cash out'. Would you rather have differently sized sections of years with cash outs in between? Then type 'specific'. """))
if Director == 'no cash out':
	gos_at_it = 1
	choose = int(input("""So you have a multi-year investment plan, and you will cash out after those years, 
and not go again for another set of years. For how many years will you keep your investments in the bank? """))
if Director == 'same size, cash out':
	gos_at_it = int(input("How many sections of those years would you want to have? "))
	choose = int(input("How long will they be?" ))

year = gd.current_year
return_rate = math.modf(return_rate)
r = 1 + (return_rate[1] + return_rate[0])*0.01

def calculator(init_inv, choose, next_inv, r, j, inflationmatching):
	calculator.i = 0
	calculator.init_inv = init_inv
	calculator.total_amount = init_inv
	inflationrate = ir.inflationrate
	if inflationmatching == 'no':
		inflationmatching = 1/inflationrate
	else:
		inflationmatching = 1

	while calculator.i < choose:
		calculator.i += 1
		calculator.total_amount = calculator.total_amount*r
		calculator.total_amount = calculator.total_amount + next_inv
		next_inv = next_inv*inflationrate*inflationmatching

		if Director == 'same size, cash out' or 'no cash out':

			print(f"investment year: {calculator.i+choose*(investmentcalculator.j-1)+gd.inp2}, investment amount: {int(calculator.total_amount)}, \
age: {Age+choose*(investmentcalculator.j-1)+calculator.i+gd.inp2}, year: {year+choose*(investmentcalculator.j-1)+calculator.i}")
	
	total_spent = calculator.init_inv+next_inv*calculator.i
	print(f"""the final investment amount after {calculator.i} years is {int(calculator.total_amount)}$ USD
	Total spent: {int(total_spent)}
	Total made: {int(calculator.total_amount-total_spent)}
	The total amount is {int(calculator.total_amount/(ir.inflationrate**(calculator.i)))}$ USD in the last section's worth. \
	the total made is  {int(calculator.total_amount-total_spent)/(ir.inflationrate**(calculator.i))}$ in the last section's worth. \
	My age at this point is {Age+calculator.i*investmentcalculator.j}""")

	spending_costs = int(input("How much did you spend from the investment amount at the end of this section? "))
	calculator.total_amount = calculator.total_amount - spending_costs

def investmentcalculator(init_inv, choose, next_inv, r, gos_at_it, roi_growth, income_growth, inflationmatching):
	investmentcalculator.j = 1
	roi_growth = roi_growth+investmentcalculator.j*0.01
	calculator(init_inv, choose, next_inv, r, investmentcalculator.j, inflationmatching)
	while investmentcalculator.j < gos_at_it:	
		investmentcalculator.j += 1
		print(f"""																																																					
		the new ratio is {roi_growth}
		the new yearly investment is {next_inv*income_growth*investmentcalculator.j}
		the {choose} year investment plan started with {calculator.total_amount}
																		""")
		calculator(calculator.total_amount, choose, next_inv*income_growth*choose, r*roi_growth, investmentcalculator.j, inflationmatching)
		gd.i += 1

#I will have to statistically model roi growth.
if Director == 'specific':
	print("You will be asked about how many years all desired sections will be. When you desire to halt the program, simply write the number 0.")
	inp = int(input("How many years will the first section be? "))
	investmentcalculator(0,0,0,0,0,0,0,0)
	print("ignore this, input ur data now, Ill fix this later.")
	calculator(init_inv, inp, next_inv, r, gd.k, inflationmatching)
	while inp != 0:
		calculator.Age = Age + inp
		year = year + inp
		gd.inp2 = gd.inp2 + inp
		inp = int(input("How many years will the next section be? "))
		calculator(calculator.total_amount, inp, next_inv*(inp*1.03)*investmentcalculator.j, r, gd.k, inflationmatching)
else:
	investmentcalculator(init_inv, choose, next_inv, r, gos_at_it, 1.01, 1.03, inflationmatching)

print(f"""I will have {int(calculator.total_amount)}$ USD at the age of {Age+investmentcalculator.j*calculator.i+gd.inp2}
That is worth {int(calculator.total_amount/(ir.inflationrate**(investmentcalculator.j*calculator.i+gd.inp2)))}$ USD now.""")