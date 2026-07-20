# smart inventory search and stouck editor
today_mobile = int(input("How many mobile's comes for today: "))
mobile_list = [ ]
for i in range(today_mobile):
	mobile_name = input("Enter name of mobile: ").capitalize()
	mobile_list.append(mobile_name)
print("Total mobile", today_mobile)
print(mobile_list)
search_mobile = input("Find your mobile here: ").capitalize()
for mobile in mobile_list:
	if mobile == search_mobile:
		print("Yes!", search_mobile, "is available in our stock ")
		break
else:
	print("Sorry! This is out of stock ")
stock_out_phone = input("enter stock out mobile name: ").capitalize()
mobile_list.remove(stock_out_phone)
mobile_list.sort()
print("Update list", mobile_list)
count_mobile = input("Enter mobile name to count: ").capitalize()
print("Total", count_mobile, "have", mobile_list.count(count_mobile), "in our stock")
