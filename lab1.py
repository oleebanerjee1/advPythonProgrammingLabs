salaryString = input("Enter your salary: ")
salary = int(salaryString)
if salary <= 0:
    print("Error, salary must be positive.")
    quit()

hoursString = input("Enter your hours: ")
hours = int(hoursString)
if hours < 0:
    print("Error, hours must be positive.")
    quit()

if hours > 40:
    earnings = 40*salary + (hours-40)*salary*1.5
    print("You earned " + str(earnings) + " dollars.")
else:
    print("You earned " + str(int(salary*hours)) + " dollars.")


