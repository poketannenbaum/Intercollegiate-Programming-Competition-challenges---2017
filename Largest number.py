import re
numbers = input("Please enter the numbers")
numbers = re.split(" ", numbers)
answer = ""
split2dnum = []
for number in numbers:
	split2dnum.append(list(number))
split2dnum.sort()
revnumcounter = len(split2dnum)
reconstructednumber = ""
while(revnumcounter != 0):
	for number in split2dnum[revnumcounter - 1]:
		reconstructednumber += number
	answer += reconstructednumber
	reconstructednumber = ""
	revnumcounter -= 1
print(answer)