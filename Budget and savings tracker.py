# Budget and savings tracker
monthly_income = int(input("enter your monthly income"))
spend = int(input("How many ways to spend "))
total_spend = 0
for I in range(spend):
	spend_amount = int(input("enter spend amount "))
	total_spend = total_spend + spend_amount
if monthly_income >= total_spend:
	print("Savings:", monthly_income -total_spend,)
else:
	print("Alert! You are in debt by", total_spend - monthly_income, "Taka")