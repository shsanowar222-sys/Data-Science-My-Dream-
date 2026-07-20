# Smart retail sales data filter
sales_data = [
    {"customer": "Abir", "item": "Laptop", "amount": 75000, "status": "Success"},
    {"customer": "Sakib", "item": "Mouse", "amount": 1500, "status": "Success"},
    {"customer": "Novi", "item": "Keyboard", "amount": 2500, "status": "Failed"},
    {"customer": "Riyad", "item": "Monitor", "amount": 18000, "status": "Success"},
    {"customer": "Mitu", "item": "Phone", "amount": 45000, "status": "Failed"},
    {"customer": "Joy", "item": "RAM", "amount": 4200, "status": "Success"}
]
success_sales = 0
failed_list = [ ]
premium_list = [ ]
for sale in sales_data:
	if sale["status"] == "Success":
		success_sales = success_sales + sale["amount"]
	elif sale["status"] == "Failed":
		info = f"{sale["customer"]} {sale["amount"]} Taka"
		failed_list.append(info)
	if sale["amount"] > 10000 and sale["status"] == "Success":
		prm_info = f"{sale["customer"]} {sale["amount"]} Taka"
		premium_list.append(prm_info)
print("=========================\nTotal success sales amount",success_sales,"Taka\n ")
print("Failed sale list")
for list in failed_list:
	print(list)
print(" \nPremium sale (10,000+ Taka)")
for premium in premium_list:
	print(premium)
print("===========================")
