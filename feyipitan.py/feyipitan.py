 
def get_score():
	score = int(input("Enter your Score: "))
	if score > 100 or score < 0:
		print("Invalid Score")
		return get_score()
	return score

def calculate_grade(score):
	if score == 100:
		grade = "A"
	elif score in range(80, 100):
		grade = "B"
	elif score in range(60, 80):
		grade = "C"
	elif score in range(40, 60):
		grade = "D"
	elif score in range(20, 40):
		grade = "E"
	else:
		grade = "F"
	print("Your grade is : " , grade)
	return grade

def get_feedback(grade):
	if grade == "A":
		print("Excellent performance.")
	elif grade == "B":
		print("Good job, Keep improving.")
	elif grade == "C":
		print("Fair effort, keep working on it.")
	elif grade == "D":
		print("You can do better, don't give up.")
	elif grade == "E":
		print("Needs Improvement, Ask for help.")
	else:
		print("Poor performance.")


def main():
	score = get_score()
	grade = calculate_grade(score)
	get_feedback(grade)
	
	repeat = input("Do you want to repeat this process? ")
	if repeat == 'yes':
		main()
	else:
		print("Goodbye")
main()
