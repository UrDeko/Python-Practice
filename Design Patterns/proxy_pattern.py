#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def print_info():
        """Interface method"""

class Person(IPerson):
    
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Name - {self.name}")

class ProxyPerson(IPerson):
    
    def __init__(self, name):
        self.person = Person(name)

    def print_info(self):
        print("Proxy functionality")
        self.person.print_info()

object = ProxyPerson("Mylo")
object.print_info()