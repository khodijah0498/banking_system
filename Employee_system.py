class Employee:
    def __init__ (self, name, id, age, department, position, salary):
        self.name = name
        self.id = id
        self.age = age
        self.department = department
        self.position = position
        self.salary = salary


class CompanyEmployeeSystem:
    def __init__(self):
        self.employees = []


    def create_employee(self, name, id, department, position, salary):
        new_employee = Employee(name, id, department, position, salary)
        self.employee.append(new_employee)
        print(f"Employee created: {name} Successfully!")


    def read_employee(self, name, id, age, department, position, salary):
        for employee in self.employee:
            if employee.name == name:
             print(f"Name:{employee.name}")
            if employee.id == id:
             print(f"ID:{employee.id}")
            if employee.age == age:
             print(f"Age:{employee.age}")
            if employee.department == department:
             print(f"Department:{employee.department}")
            if employee.position == position:
             print(f"Position:{employee.position}")
            if employee.salary == salary:
             print(f"Salary:{employee.salary}")
            print("Empolyee not found")
            return None


    def update_employee(self, name, id, department, position, salary):
        for employee in self.employee:
            if employee.name == name:
                return name
            if employee.id == id:
                return id
            if employee.department == department:
                return department
            if employee.position == position:
                return position
            if employee.salary == salary:
                return salary
            print("Empolyee not found")
            return None


    def delete_employee(self, name, id, department, position, salary):
        for employee in self.employee:
            if employee.id == id:
             self.employee.remove(employee)
             print(f"Employee created: {id}  Delete Successfully!")


    def find_employee(self, id):
        for employee in self.employee:
            if employee.id == id:
                self.employee.find(employee)
                print(f"Employee Find: {id} Find Sucessfully!")

            
employee_system = CompanyEmployeeSystem()

while True:
    print("1. Create Employee")
    print("2. Read Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Find Employee")
    print("5. Exit")

    employ = input("choose an option:")
    if employ == "1":
        name = str(input("Enter your name:"))
        id = int(input("Enter your id:"))
        age = int(input("Enter your age:"))
        department = input("Enter your department:")
        position = str(input("Enter your position:"))
        salary = float(input("Enter your salary:"))
        employee_system.create_employee(name, id, age, department, position, salary)


    elif employ == "2":
        id = str(input("Enter your id: "))
        employee = employee_system.read_employee(id)
        if employee:
            employee.read_employee()
    
    
    elif employ == "3":
        name = str(input("Enter your name:"))
        id = int(input("Enter your id:"))
        age = int(input("Enter your age"))
        department = input("Enter your department:")
        position = str(input("Enter your position:"))
        salary = float(input("Enter your salary:"))
        employee_system.update_employee(name, id, age, department, position, salary)


    elif employ == "4":
        id = str(input("Enter your id: "))
        employee = employee_system.delete_employee(id)
        # if employee:
        #     employee.delete_employee()


    elif employ == "5":
        id = str(input("Enter your id: "))
        employee = employee_system.find_employee(id)
        if employee:
            employee.find_employee()


    elif employ == "6":
        break

    else:
        print("Invalid option. Please try again.")




         


    

