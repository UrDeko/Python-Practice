#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def print_info():
        """Interface method"""

class Student(IPerson):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.type = "Student"

    def print_info(self):
        print(f"Info: {self.first_name} {self.last_name} - {self.type}")

class Teacher(IPerson):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.type = "Teacher"

    def print_info(self):
        print(f"Info: {self.first_name} {self.last_name} - {self.type}")

class PersonFactory():

    @staticmethod
    def create_person(type, first_name, last_name):
        if type == "Student":
            return Student(first_name, last_name)
        elif type == "Teacher":
            return Teacher(first_name, last_name)
        else:
            raise Exception(f"Not a valid person type: {type}")

if __name__ == "__main__":
    person_type, first_name, last_name = str(input("Please enter person type, first name and last name: ")).split(" ")
    person = PersonFactory.create_person(person_type, first_name, last_name)
    person.print_info()