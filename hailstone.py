import re
numbers = input("Enter starting value")
startnumber = numbers
value = int(numbers)
iterations = 0
highestvalue = 0
while(True):
	if (value > highestvalue):
		highestvalue = value
	if (value == 4):
		break
	numbers = list(numbers)
	numblen = len(numbers)
	if(numbers[numblen - 1] == "1" or  numbers[numblen - 1] == "3" or numbers[numblen - 1] == "5" or numbers[numblen - 1] == "7" or numbers[numblen - 1] == "9"):
		value = (value * 3) + 1
	else:
		value = value // 2
	numbers = str(value)
	iterations += 1
iterations += 2
print(f"Starting number: {startnumber}; iterations: {iterations}; largest value: {highestvalue}")