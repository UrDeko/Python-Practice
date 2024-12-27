#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod

class IDepartment(metaclass=ABCMeta):
    def __init__(self, employees):
        self.employees = employees
    
    def get_employees(self):
        return self.employees

    @abstractmethod
    def print_employee_number():
        "Interface method"

class Accounting(IDepartment):
    def __init__(self, employees):
        super().__init__(employees)

    def print_employee_number(self):
        print(f"Accounting: {self.employees} employees")

class Development(IDepartment):
    def __init__(self, employees):
        super().__init__(employees)

    def print_employee_number(self):
        print(f"Development: {self.employees} employees")

class ParentDepartment(IDepartment):
    def __init__(self, employees):
        super().__init__(employees)
        self.base_employees = employees
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)
        self.employees += department.get_employees()

    def print_employee_number(self):
        print(f"Parent department: {self.base_employees} employees")
        for department in self.departments:
            department.print_employee_number()
        print(f"Total: {self.get_employees()} employees")

dev_dept = Development(40)
acc_dept = Accounting(50)
par_dept = ParentDepartment(10)
par_dept.add_department(dev_dept)
par_dept.add_department(acc_dept)
par_dept.print_employee_number()