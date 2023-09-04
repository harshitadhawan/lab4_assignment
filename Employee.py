from tabulate import tabulate

class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return (self.emp_id, self.name, self.age, self.salary)

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_employees(self, sort_parameter):
        if sort_parameter == 1:
            self.employees.sort(key=lambda emp: emp.age)
        elif sort_parameter == 2:
            self.employees.sort(key=lambda emp: emp.name)
        elif sort_parameter == 3:
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter.")

    def display_employees(self):
        table_headers = ["Employee ID", "Name", "Age", "Salary(PM)"]
        table_data = [[employee.emp_id, employee.name, employee.age, employee.salary] for employee in self.employees]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

if __name__ == "__main__":
    database = EmployeeDatabase()

    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    sort_parameter = int(input("Choose sorting parameter:\n1. Age   2. Name   3. Salary\nenter(1/2/3): "))

    database.sort_employees(sort_parameter)
    print("\nSorted Employee Data:")
    database.display_employees()
