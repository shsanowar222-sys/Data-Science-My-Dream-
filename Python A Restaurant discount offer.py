# Restaurant discount offer
premium_member = input("premium enter yes or no")
premium  = premium_member.capitalize()
total_bills = int(input("enter customers total bills"))
if total_bills >= 1000 and premium == "Yes":
	print("discount", total_bills * .2, "taka")
	print("without discount total bills" , total_bills - (total_bills * .2 ), "taka")
elif total_bills >= 1000:
	print("discount", total_bills * .1, "taka")
	print("without discount total bills", total_bills - (total_bills *.1), "taka")
else:
	print("sorry you don't get any discount ")
	print("total bills", total_bills)
