# Smart grade calculation 
def calculate_grade(mark):
	if 80 <= mark <= 100:
		return "A+"
	elif 70 <=  mark < 80:
		return "A"
	elif 60 <=  mark < 70:
		return "A-"
	elif 50 <= mark < 60:
		return "B"
	elif 40 <= mark < 50:
		return "C"
	elif 33 <= mark < 40:
		return "D"
	elif 0 <= mark < 33:
		return "F"
	else:
		return "Invalid match. Please enter between 1 to 100"
total_student = [ ]
total_mark = 0
while True:
			print("=== Welcome to grade calculation ===")
			user_input = input("Start or exit program: ").lower()
			if user_input == "start":
				try:
					student_input = input("Enter student name: ").lower().strip(", . ! ? ")
					mark_input = int(input("Enter student mark here: "))
					total_student.append(student_input)
					print(student_input, calculate_grade(mark_input))
					total_mark = total_mark + mark_input
				except ValueError:
					print("Wrong input! Only enter 'number' ")
			elif user_input == "exit":
				try:
					print("Total student:", len(total_student))
					print("total mark:", total_mark)
					print("Average mark:", int(total_mark / len(total_student)))
					print("Average grade: ", calculate_grade(int(total_mark / len(total_student))))
				except ZeroDivisionError:
					print("Please enter correct information ")
				print("Thank you! Program is successfully completed ")
				break
			else:
				print("Wrong input. Please enter 'start' or 'exit' ")