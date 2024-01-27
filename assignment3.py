 #1
class Employee:

    # declared a data member to count the number of Employees
    no_of_employees = 0

    # constructor to initialize the object's attributes
    def __init__(self, name, family_name, salary, department):
        self.__name = name
        self.__family_name = family_name
        self.salary = salary
        self.__department = department
        Employee.no_of_employees += 1

    # declared average_salary function to return average salary
    def average_salary(employees):
        """
        function to average salary
        """
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.no_of_employees

# Created a Fulltime Employee class and inherited the properties of Employee class
class FulltimeEmployee(Employee):
    """
    Full Time Employee is a sub class of Employee
    """

    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def full_time_member(self):
        print("Calling FulltimeEmployee member function.")

# Created the instances of Fulltime Employee class and Employee class and calling their member functions.
def main():
    employees = []
    ftEmployee1 = FulltimeEmployee("Vamshi", "Rapolu", 140000, "Software Engineering")
    ftEmployee1.full_time_member()
    employees.append(ftEmployee1)
    ftEmployee2 = FulltimeEmployee("Bharath", "Karingula", 170000, "Cyber Security")
    employees.append(ftEmployee2)
    employee1 = Employee("Vamshi", "Miryala", 150000, "Testing")
    employees.append(employee1)
    employee2 = Employee("Dileep", "Podeti", 192000, "Product Manager")
    employees.append(employee2)
    print("Average salary:", FulltimeEmployee.average_salary(employees))


 #2

mport numpy as np

# created a random vector of size 20 with float values between 1 and 20
ranvec = np.random.uniform(low=1, high=20, size=20)
print(ranvec)
# reshape the array to 4 by 5 using reshape method
mat45 = ranvec.reshape(4, 5)
print(mat45)
# replace the max in each row by 0 using where method
mat45 = np.where(mat45 == np.amax(mat45, axis=1, keepdims=True), 0, mat45)
print(mat45)

# declared this method to execute code When the file runs as a script.
if __name__ == "__main__":
    main()
