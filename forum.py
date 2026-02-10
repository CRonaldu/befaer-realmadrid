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
    
    
        
    def register_admin(self , adminname):
        self.admin = adminname

    def delete_comment(self , admin , user):
        if admin == self.admin:
            del self.comments[user.name]
        else:
            return "Only admin can delete comments."
        
        
    



user1 = User("Dastan",19,'Aktaidastangmail.com')
forum = Forum("Python Forum")
forum.add_user(user1)
forum.comment(user1 , "This is my first comment!")
print(forum.show_comments())
user2 = User("Aizhan", 25, 'aizhangmail.com')
forum.add_user(user2)
forum.comment(user2 , "Hello everyone!")
print(forum.show_comments())
admin1 = forum.register_admin("AdminUser")
forum.delete_comment(admin1, 'Dastan')
print(forum.show_comments())


    