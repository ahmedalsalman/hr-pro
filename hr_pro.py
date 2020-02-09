class Employee:
   def __init__(self, name, age, salary, employment_year):


	   self.name = name
	   self.age = age
	   self.salary = salary
	   self.employment_year = employment_year



   def get_working_years(self):
	   return 2020 - int(self.employment_year)

class Manager(Employee):
	def __init__(self, name, age, salary, employment_year, bonus_percentage):
		super().__init__(name, age, salary, employment_year)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		return self.bonus_percentage * self.salary
name = ""
age = 0
shosho = Employee("Shosho", 24, 666, 2018)
khalid = Employee("Khalid", 26, 500, 2017)
emp = [shosho, khalid]

sammy = Manager("sammy", 52, 4600, 2005, 0.5)
man = [sammy]

def main():
	print("Welcome to HR Pro 2019")
	while True:
		print("Options:")
		print("   1. Show Employees")
		print("   2. Show Managers")
		print("   3. Add An Employee")
		print("   4. Add A Manager")
		print("   5. Exit")

		d = int(input("What would you like to do? "))
		if d == 1:
			for n in emp:
				print(f"Name: {n.name}, Age: {n.age}, Salary: {n.salary}, Working years: {n.get_working_years()}")
		if d == 2:
			for n in man:
				print(f"Name: {n.name}, Age: {n.age}, Salary: {n.salary}, Working years: {n.get_working_years()}, Bonus: {n.get_bonus()}")
		if d == 3:
			name = Employee(input("Enter employee name: "), input("Enter employee age: "), input("Enter employee salary: "), input("Enter employee employment year: "))
			#name.name = str(name)
			#name.age = input("Enter employee age: ")
			#name.salary = input("Enter employee salary: ")
			#name.employment_year = input("Enter employee employment year: ")
			emp.append(name)
			print("Employee has been added.")
		if d == 4:
			name = Manager(input("Enter manager name: "),input("Enter manager age: "),input("Enter manager salary: "),input("Enter manager employment year: "),input("Enter manager bonus percentage: "))
			#Manager.age = input("Enter manager age: ")
			#Manager.salary = input("Enter manager salary: ")
			#Manager.employment_year = input("Enter manager employment year: ")
			#Manager.bonus_percentage = input("Enter manager bonus percentage: ")
			man.append(name)
			print("Manager has been added.")
		if d == 5:
			break
if __name__ == '__main__':
	main()
