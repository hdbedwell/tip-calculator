#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator!")
bill = input("How much was the bill?\n")
bill = float(bill)
tip = input("What percentage tip would you like to add? 10, 15, or 20?\n")
tip = int(tip)
final_tip = 1 + (tip/100)
final_bill = (round(bill * final_tip, 2))
print(f"Your final bill will be: ${final_bill:.2f}")
party = input("How many people will be splitting the bill?\n")
party = int(party)
share = ((final_bill / party))
print(f"Each person's share of the bill is: ${share:.2f}")

#FAQ: How to round to 2 decimal places?
#https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
