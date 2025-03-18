'                              University Management System                          '

class Employee:
    Person_list = []  # Class variable to store all Employees

    def __init__(self, name=None, age=None, designation=None, email=None, address=None, contact=None, emp_id=None):  #  default constructor
        self.name = name; self.age = age; self.designation = designation; self.email = email; self.address = address; self.contact = contact; self.id = id

    def add(self): # function to add multiple objects
        # Gather input from the user
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        designation = input("Enter the designation: ")
        email = input("Enter the email: ")
        address = input("Enter the address: ")
        contact = int(input("Enter the contact: "))
        id = input("Enter the ID: ")

        # Create a new instance of the calling class
        new_Employee = self.__class__(name, age, designation, email, address, contact, id) # __class__ creates a new instance (object)

        # Add the new Employee to the class variable list
        self.__class__.Person_list.append(new_Employee)

        # __name__ gives the name of the class
        print(f"{self.__class__.__name__} successfully added:", new_Employee.name) 

    @classmethod
    def remove(cls): # function to remove an object
        name = input("Enter the name: ")
        id = int(input("Enter the ID: "))
        found = False

        for Person in cls.Person_list:
            if Person.name.lower() == name.lower() and Person.id == id:
                cls.Person_list.remove(Person)
                print(f"{cls.__name__} successfully removed:", Person.__dict__)
                found = True
                break

        if not found:
            print(f"No {cls.__name__.lower()} found with the name: {name} and ID: {id}")

    @classmethod
    def search(cls): # function to search an object
        name = input("Enter the name: ")
        found = False
        
        for Person in cls.Person_list:
            if Person.name.lower() == name.lower():  # Case-insensitive search
                print(f"{cls.__name__} found:", Person.__dict__)
                found = True
                break
        
        if not found:
            print(f"No {cls.__name__.lower()} found with the name: {name}")

    @classmethod
    def display(cls): # function to display all objects in the list
        if not cls.Person_list:
            print(f"No {cls.__name__.lower()}s to display.")
            return
        # else
        print(f"{cls.__name__}s:")
        for Person in cls.Person_list:
            print(Person.__dict__) # Prints the attributes of each Person

    @classmethod 
    def count(cls):
       print(f"Total number of {cls.__name__} is {len(cls.Person_list)}")

class Temporary_Faculty(Employee):
    Person_list = []  # Class variable to store all temporary faculty members

class Permanent_Faculty(Employee):
    Person_list = []  # Class variable to store all permanent faculty members

class Staff(Employee):
    Person_list = []  # Class variable to store all staff members

class Administration(Employee):
    Person_list = []  # Class variable to store all administrators
    
class Students(Employee):
    Person_list = []  # Class variable to store all students

if __name__ == "__main__":
    Emp = Employee()
    Admin = Administration()
    P_faculty = Permanent_Faculty()
    T_faculty = Temporary_Faculty()
    staff = Staff()
    student = Students()

    while True:
        print("Enter 1 for Employees               Enter 2 for Administration")
        print("Enter 3 for Permanent Faculty       Enter 4 for Temporary Faculty")
        print('Enter 5 for Staff                   Enter 6 for Students')
        choice = int(input('Select an option: '))
        # Employee
        if choice == 1: 
            print('Enter 1 to Add an Employee           Enter 2 to Remove an Employee')
            print('Enter 3 to Search an Employee        Enter 4 to Display all Employee')
            print('Enter 5 to check Count of Employees')
            option = int(input('Select an option: '))

            match option:
                case 1: 
                    while True:
                        Emp.add()
                        if input("Do you want to add more employees? (y/n): ").lower() != "y":
                            break

                case 2: 
                    while True:
                        Emp.remove()
                        if input('Do you want to remove more employees? (y/n)').lower() != 'y':
                            break
                case 3: 
                    while True:
                        Emp.search()
                        if input("Do you want to search more employees? (y/n): ").lower() != "y":
                            break
                case 4: 
                    Emp.display()
                case 5: 
                    Emp.count()

        # Administration
        elif choice == 2: 
            print('Enter 1 to Add an Administration             Enter 2 to Remove an Administtration')
            print('Enter 3 to Search an Administration          Enter 4 to Display all administration')
            print('Enter 5 to  check Count of Administration')
            option = int(input('Select an option: '))

            match option:
                case 1:
                    while True:
                        Admin.add()
                        if ('Do you want to add more administration? (y/n)').lower() == 'n':
                            break
                case 2:
                    while True:
                        Admin.remove()  
                        if ('Do you want to remove more administration? (y/n)').lower() == 'n':
                            break    
                case 3:
                    while True:
                        Admin.search()
                        if ('Do you want to search more administration? (y/n)').lower() == 'n':
                            break     
                case 4:
                    Admin.display()
                case 5:
                    Admin.count() 

        # Permanent Faculty
        elif choice == 3: 
            print('Enter 1 to Add a Permanent Faculty               Enter 2 to Remove a Permanent Faculty')
            print('Enter 3 to Search a Permanent Faculty            Enter 4 to Display all Permanent Faculty')
            print('Enter 5 to check Count of Permanent Faculty')
            option = int(input('Select an option: '))

            match option:
                case 1:
                    while True:
                        P_faculty.add()
                        if ('Do you want to add more permanent faculty? (y/n)').lower() == 'n':
                            break
                case 2:
                    while True:
                        P_faculty.remove()
                        if ('Do you want to remove more permanent faculty? (y/n)').lower() == 'n':
                            break
                case 3:
                    while True:
                        P_faculty.search()
                        if ('Do you want to search more permanent faculty? (y/n)').lower() == 'n':
                            break
                case 4:
                    P_faculty.display()
                case 5:
                    P_faculty.count()

        # Temporary Faculty
        elif choice == 4: 
            print('Enter 1 to Add a Temporary Faculty               Enter 2 to Remove a Temporary Faculty')
            print('Enter 3 to Search a Temporary Faculty            Enter 4 to Display all Temporary Faculty')
            print('Enter 5 to check Count of Temporary Faculty')
            option = int(input('Select an option: '))

            match option:
                case 1: 
                    while True:
                        T_faculty.add()
                        if ('Do you want to add more temporary faculty? (y/n)').lower() != 'y':
                            break
                case 2:
                    while True:
                        T_faculty.remove()
                        if ('Do you want to remove more temporary faculty? (y/n)').lower() != 'y':
                            break
                case 3:
                    while True:
                        T_faculty.search()
                        if ('Do you want to search more temporary faculty? (y/n)').lower() != 'y':
                            break
                case 4:
                    T_faculty.display()
                case 5:
                    T_faculty.count()

        # Staff
        elif choice == 5: 
            print('Enter 1 to Add a Staff Member               Enter 2 to Remove a Staff Member')
            print('Enter 3 to Search a Staff Member            Enter 4 to Display all Staff Members')
            print('Enter 5 to check Count of Staff Members')
            option = int(input('Select an option: '))

            match option:
                case 1:
                    while True:
                        staff.add()
                        if ('Do you want to add more staff members? (y/n)').lower() == 'n':
                            break
                case 2:
                    while True:
                        staff.remove()
                        if ('Do you want to remove more staff members? (y/n)').lower() == 'n':
                            break
                case 3:
                    while True:
                        staff.search()
                        if ('Do you want to search more staff members? (y/n)').lower() == 'n':
                            break
                case 4:
                    staff.display()
                case 5:
                    staff.count()

        # Students
        elif choice == 6: 
            print('Enter 1 to Add a Student               Enter 2 to Remove a Student')
            print('Enter 3 to Search a Student            Enter 4 to Display all Student')
            print('Enter 5 to check Count of Students')
            option = int(input('Select an option: '))

            match option:
                case 1:
                    while True:
                        student.add()
                        if ('Do you want to add more students? (y/n)').lower() == 'n':
                            break
                case 2:
                    while True:
                        student.remove()
                        if ('Do you want to remove more students? (y/n)').lower() == 'n':
                            break
                case 3:
                    while True:
                        student.search()
                        if ('Do you want to search more students? (y/n)').lower() == 'n':
                            break
                case 4:
                    student.display()
                case 5: 
                    student.count()

        # Exit the loop
        if input("Do you want to exit to main menu? (y/n): ").lower() != "y":
            print('Program exited.')
            break


