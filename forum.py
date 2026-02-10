print ('hello world')

class User:

    def __init__( self, name, age , gmail):
        self.name = name
        self.age = age
        self.gmail = gmail

    def informaton(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. My email is {self.gmail}"
    
class Forum:
    def __init__(self , name):
        self.name = name
        self.users = []
        self.comments = {}

    def add_user(self , user):
        self.users.append(user)

    def comment(self , user , comment):
        self.comments = {user.name : comment}

    def show_comments(self):
        return self.comments

user1 = User('Dastan' , 18 , 'aktajdastan')
print (user1.informaton())
forum1 = Forum('Python Forum')
forum1.add_user(user1)
forum1.comment(user1 , 'This is a great forum!')
print (forum1.show_comments())


       