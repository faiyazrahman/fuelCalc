import math 

print("Welcome! Pilot")
print()
print("BRISTELL NG5 FUEL Calculator")
print("Consumption: 20 Liters per Hour")
print()
print("Enter 0 to exit")
print()

def calculate(): 

	Total_Fuel = float(input("Enter Fuel Level (L): "))

	if Total_Fuel == 0:
		exit()

	Current_Flight_Fuel = Total_Fuel - 15
	Reserve_Fuel = 15

	print("Available flight fuel: ", Current_Flight_Fuel ,"(L)")
	print("------------------------------------------------------")
	print("Reserve fuel: " , Reserve_Fuel,"(L)")
	print("------------------------------------------------------")
	print("Reserve flight time: 45 mins")
	print("------------------------------------------------------")
	x = Current_Flight_Fuel*60
	y = x/20
	z = y/60 
	#print(z)

	w = (((math.floor(z) - z)*100)*60)/100
	r = round(w)
	minutes = r*(-1)

	#print(minutes)

	#print(math.floor(z), minutes)

	if Current_Flight_Fuel < 20:
		print("Fuel below 20L Requirement")

	if z <= 1:
		print("Flight time with current fuel:","1 hour")
		print("------------------------------------------------------")
		print()
		calculate()

	if z%2 == 0.00:
		print("Flight time with current fuel:", math.floor(z), "hours")
		print("------------------------------------------------------")
		print()
		calculate()

	else:
		print("Flight time with current fuel:", math.floor(z), "hours and", minutes ,"minutes")
		print("------------------------------------------------------")
		print()
		calculate()




calculate()
