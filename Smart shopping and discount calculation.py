# Smart shopping and discount calculation
total_items = int(input("Enter items total bought "))
total_bills = 0
for I in range(total_items):
	price = int(input("Enter item price"))
	total_bills = total_bills + price
print("Actual bills", total_bills, "Taka")
if total_bills >= 5000:
	print("Discount ", total_bills * .1,"Taks")
	print("After discount total bills", total_bills - (total_bills * .1), "Taka")
elif total_bills >= 2000:
	print("Discount", total_bills * .05, "Taka")
	print("After discount total bills", total_bills -(total_bills * .05), "Taka")
else:
	print("Sorry!"
	"you don't get any discount."
	"You need to pay", total_bills)