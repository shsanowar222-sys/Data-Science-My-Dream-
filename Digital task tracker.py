# Digital task tracker.
today_task = int(input("How many task want to do for today"))
total_task = [ ]
for i in range(today_task):
	task = input("enter your task here")
	total_task.append(task)
print("Today total task")
for index, task in enumerate(total_task, start= 1):
	print(index,task)