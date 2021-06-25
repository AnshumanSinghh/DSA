class Employee:
    def __init__(self, idx, name, role, salary):
        self.emp_id = idx
        self.emp_name = name
        self.emp_role = role
        self.emp_salary = salary

    def calculateIncentive(self, roleIncentivePercentage):
        for key, percentage in roleIncentivePercentage.items():
            incentive = self.emp_salary * (percentage / 100)
        return incentive

    def calculateEmployeSalaryByRole(self, role, employee_list, roleIncentivePercentage):
        employee_list = []
        for i in self.emp_list:
            if(i.emp_role == role):
                i.increse_salary(percentage)
                employee_list.append(i)
        return employee_list


if __name__ == "__main__":

    noOfRole = int(input())
    print("noOfRole: ", noOfRole)
    roleIncentivePercentage = {}
    for tt in range(noOfRole):
        keys = input()  
        values = int(input())  
        roleIncentivePercentage[keys] = values
    # z = Employee()
    # print(z.calculateIncentive(roleIncentivePercentage))

    t = int(input())
    emp_l = []
    for i in range(t):
        idx = int(input())
        name = input()
        role = input()
        salary = int(input())
        emp_l.append(Employee(idx, name, role, salary))
    o = Employee(emp_l)
    print(o.calculateIncentive(roleIncentivePercentage))
    role = input()
    percentage = int(input())
    result = o.calculateEmployeSalaryByRole(role, percentage)
    for i in result:
        print(i.emp_name)
        print(i.emp_salary)
