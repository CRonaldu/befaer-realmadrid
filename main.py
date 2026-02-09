class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    def unnamed(self , name):
        self.name = name
    
user1 = User("Alice", 30)
print(user1.greet())
user1.unnamed("Bob")
print(user1.greet())        

    