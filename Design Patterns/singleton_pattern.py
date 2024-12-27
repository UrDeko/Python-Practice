#!/usr/bin/env python3
class SingletonPerson():
    __instance = None

    @staticmethod
    def get_instance():
        if not SingletonPerson.__instance:
            raise Exception("No Singleton instance available")
        
        return SingletonPerson.__instance

    def __init__(self, name, age):
        if SingletonPerson.__instance:
            raise Exception("Singleton instance has already been created")
        else:
            self.name = name
            self.age = age
            SingletonPerson.__instance = self

    def print_info(self):
        print(f"Name: {self.name}; Age: {self.age}")

person = SingletonPerson("John", 40)
person.print_info()

p2 = SingletonPerson.get_instance()
p2.print_info()