'''
Given a homework score out of 100 points with 25% weights, a midterm score out of 100 with 25% weight, 
and a final score out of 200 with 50% weight, this script returns the weighted total and whether the student 
passed or failed the class  
'''

class Grader:

	homework = -1
	midterm = -1
	final = -1

	def calculate_weighted(self):
		homework = float(input("Enter your homework grade: "))
		while homework < 0 or homework > 100:
			print("[ERR] Invalid input. A homework grade should be in [0, 100]")
			homework = float(input("Enter your homework grade: "))

		midterm = float(input("Enter your midterm grade: "))
		while midterm < 0 or midterm > 100:
			print("[ERR] Invalid input. A midterm grade should be in [0, 100]")
			midterm = float(input("Enter your homework grade: "))

		final = float(input("Enter your homework grade: "))
		while final < 0 or final > 200:
			print("[ERR] Invalid input. A final grade should be in [0, 200]")
			final = float(input("Enter your final grade: "))

		weighted = (0.25 * homework) + (0.25 * midterm) + (0.5 * (final / 2))
		message = "[INFO] Student's weighted total is {:.2f}%"
		print(message.format(weighted))

		if weighted > 50:
			print("Student PASSED the class.")
		else:
			print("Student FAILED the class.")

obj1 = Grader()
obj1.calculate_weighted()