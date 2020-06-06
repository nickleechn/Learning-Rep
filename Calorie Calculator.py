# 基本信息填写
print("[ Welcome to bodily energy evaluator! ]")
name = input("\tCan I have your name, please? ")
weight = int(input("- What is your current weight? (kg) "))
height = int(input("- What is your height? (cm)"))
age = int(input("How old are you?"))
bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
print(f"Thanks, {name.title()}, your Basic Metabolic Rate is: {bmr}.")
print()
print("Let's calculate your daily energy consumption.")
activity_level = ['1. Barely exercise', '2. Exercise 1-3 times', '3. Exercise 3-5 times', '4. Exercise 6-7 times']
print("How many times would you exercise on a weekly basis?")
for activity in activity_level:
	print(activity)
exercise_frequency = int(input("- What's your choice?"))

#计算身体每日热量消耗
if exercise_frequency == 1:
	energy_consump = bmr * 1.2
elif exercise_frequency == 2:
	energy_consump = bmr *1.375
elif exercise_frequency == 3:
	energy_consump = bmr * 1.55
else:
	energy_consump = bmr * 1.725
energykj = energy_consump * 4.184
print()
print(f"- {name.title()}, your daily energy consumption is {energy_consump} calories. \nThe number equals to {energykj} in kj. \nMake sure your daily calorie intake is less than that.")
energyintake= []


def energy_foodcalculate(): # 计算热量食品卡路里
	print()
	print("Choose the energy food that you ate:")
	energyfood_list = ['1. Dumpling', '2. Rice', '3. Baozi/Bread', '4. Instant Noodles']
	for energyfood in energyfood_list:
		print(energyfood)
	temp_choices_typeone = int(input("What did you eat?"))
	if temp_choices_typeone == 1:
		howmanydump = int(input("\tHow many dumplings did you eat?"))
		dumplingcal = howmanydump * 52
		energyintake.append(dumplingcal)
		engage_again()
	elif temp_choices_typeone == 2:
		ricecal = 150
		energyintake.append(150)
		engage_again()
	elif temp_choices_typeone == 3:
		baozicount = int(input("\tHow many did you eat?"))
		baozical = baozicount * 250
		energyintake.append(baozical)
		engage_again()
	elif temp_choices_typeone == 4:
		noodlecal = 550
		energyintake.append(550)
		engage_again()
		
def vegetable_calculate(): #计算蔬菜卡路里
	print()
	print("What vegie did you eat?")
	vegitable_list = ['1. Potato', '2. Tomato', '3. Mushroom']
	for vegi in vegitable_list:
		print(vegi)
	vegichoice = int(input("Make your choice. "))
	if vegichoice == 1:
		energyintake.append(30)
		engage_again()
	elif vegichoice == 2:
		energyintake.append(24)
		engage_again()
	elif vegichoice == 3:
		energyintake.append(70)
		engage_again()

#计算水果卡路里
def fruit_calculate():
	print("On avergae, a common fruit contains 50 calories.")
	fruitnumber = int(input("How many fruits did you eat?"))
	fruitcal = fruitnumber * 50
	energyintake.append(fruitcal)
	engage_again()
	
def meatcalculate(): #肉类卡路里计算
	print()
	print("\tMeat is usually rich in calories. Make a selection:")
	meat_listing = ['1. Chicken', '2. Lam', '3. Beef', "4. Pork", '5. Egg']
	for meat in meat_listing:
		print(meat)
	meatchoice = int(input("Choose your meat."))
	if meatchoice == 1:
		chiweight = int(input("\tHow many grams? (g)"))
		chical = chiweight * 6
		energyintake.append(chical)
		engage_again()
	elif meatchoice == 2:
		lamweight = int(input("\tHow many grams? (g)"))
		lamcal = lamweight * 6
		energyintake.append(lamcal)
		engage_again()
	elif meatchoice == 3:
		beefweight = int(input("\tHow many grams? (g)"))
		beefcal = beefweight * 6
		energyintake.append(beefcal)
		engage_again()
	elif meatchoice == 4:
		pork_weight = int(input("\tHow many grams? (g)"))
		pork_cal = pork_weight * 6
		energyintake.append(pork_cal)
		engage_again()
	elif meatchoice == 5:
		egg_count == int(input("How many eggs did you eat?"))
		egg_cal = egg_count * 50
		energyintake.append(egg_cal)
		engage_again()
		
def drinkcal(): #计算饮料卡路里
	print()
	print("These are the common beverages:")
	drinklist = ['1. Coke', '2. Milk', '3. Yougourt', '4. Skim Milk', '5. Coffee', '6. Milk Tea']
	for drink in drinklist:
		print(drink)
	drinkchoose = int(input("What is your choice?"))
	if drinkchoose == 1:
		energyintake.append(140)
		engage_again()
	elif drinkchoose == 2:
		energyintake.append(160)
		engage_again()
	elif drinkchoose == 3:
		energyintake.append(180)
		engage_again()
	elif drinkchoose == 4:
		energyintake.append(80)
		engage_again()
	elif drinkchoose == 5:
		drinksize = int(input("How many cups did you drink?"))
		coffecal = drinksize * 120
		energyintake.append(coffecal)
		engage_again()
	elif drinkchoose == 6:
		energyintake.append(564)
		engage_again()
		
def calculator(): #卡路里千焦换算
	print()
	print("Please choose a function")
	functionlist = ['1. kj to kcal', '2. kcal to kj']
	for singlefun in functionlist:
		print(singlefun)
	functionresponse = int(input("Your choice: "))
	if functionresponse == 1:
		kjcount = int(input("- Please key-in your kj count:"))
		kj2cal = kjcount / 4.186
		print(f"\t{kjcount} kj = {kj2cal} calories")
	else:
		calcount = int(input("- Please key-in your cal count:"))
		cal2kj = calcount * 4.186
		print(f"\t{cal2kj} cal = {kjcount} kj")
		
def snackcal():
	print()
	print("What kind of snack did you eat?")
	snacklist = ['1. Ice Cream (150)', '2. Almounds (870)', '3.Chips (500)', '4. 手抓饼 (500)']
	snackchoice = int(input("- Your choice? "))
	if snackchoice == 1:
		energyintake.append(150)
		engage_again()
	elif snackchoice == 2:
		energyintake.append(870)
		engage_again()
	elif snackchoice == 3:
		energyintake.append(500)
		engage_again()
	elif snackchoice == 4:
		energyintake.append(500)
		engage_again()

def userinput():
	print()
	userinputno = int(input("\tPlease register your calorie intake:"))
	energyintake.append(userinputno)
	engage_again()
				
#选择食品大类
def choose_foodtype():
	print()
	print("Choose from the types of food you had today:")
	foodtype = ['1. Energy food', '2. Vegetables', '3. Fruits', '4. Beverages', '5. Animal products', '6. Snack', '7. kj <-> Calories', '8. Customer Register']
	for food in foodtype:
		print(food)
	foodchoice = int(input("- What's your choice?"))
	if foodchoice == 1:
		energy_foodcalculate()
	elif foodchoice == 2:
		vegetable_calculate()
	elif foodchoice == 3:
		fruit_calculate()
	elif foodchoice == 4:
		drinkcal()
	elif foodchoice == 5:
		meatcalculate()
	elif foodchoice == 6:
		meatcalculate()
	elif foodchoice == 7:
		calculator()
	elif foodchoice == 8:
		userinput()
	else:
		choose_foodtype()
				
def engage_again(): #再次邀约用户计算
	restart = input("\tConfirmed. \n\tWould you register more food? (y/n)")
	if restart == "y":
		choose_foodtype()
	else:
		totalintake = sum(energyintake)
		remaining_cal = totalintake - energy_consump
		print()
		print(f"- {name.title()}, your total energy intake is {totalintake} calories.")
		exercise_needed = totalintake / 650
		print(f"\tYou'll need to exercise for {exercise_needed} hours to burn it off!")
		if totalintake <= energy_consump:
			print(f"You don't need exercise today. Your remaining calories are {remaining_cal}.")
		else:
			print(f"\tPlease exercise immediately! You still have {remaining_cal} calories remaining.")

choose_foodtype()