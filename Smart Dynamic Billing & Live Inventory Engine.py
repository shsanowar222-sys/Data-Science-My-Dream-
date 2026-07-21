# Smart Dynamic Billing & Live Inventory Engine
mobile_price = {"Iphone": 125000, "Samsang": 95000, "Vivo": 25000, "Redme": 18000, "Oppo": 20000}
all_time_mobile_list = [ ]
while True:
	print("\n ============")
	command = input("Type start,  exit or report: ").capitalize()
	if command == "Exit":
		print("Thank you! Program is successfully finished")
		break
	elif command == "Report":
		print("All time total mobile:", " , ".join(all_time_mobile_list), "\n Note: if you are exit the program, you will lose all the collection")
	elif command == "Start":
			mobile_list = [ ]
			discount = 0
			for i in range (3):
				mobile_name = input("Enter mobile name here: ").capitalize()
				mobile_list.append(mobile_name)
				if mobile_name == "Samsang":
					discount = discount + (mobile_price[mobile_name] * .05)
				elif mobile_name == "Vivo" or mobile_name == "Oppo":
					discount = discount + (mobile_price[mobile_name] * .1)
				elif mobile_name == "Redme":
					discount = discount + (mobile_price[mobile_name] * .08)
			all_time_mobile_list.extend(mobile_list)
			total_price = 0
			for mobile in mobile_list:
				if mobile in mobile_price:
					total_price = total_price + mobile_price[mobile]
					print(mobile, "price is:", mobile_price[mobile])
				elif mobile not in mobile_price:
					print("Sorry!", mobile, "price is not available")
			print("Original price:", total_price)
			print("Discount:",  int(discount))
			print("Payable amount:", int(total_price - discount))