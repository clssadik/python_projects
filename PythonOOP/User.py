class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self,user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

my_username = User("clssadik","cillsadik@gmail.com",0000)
new_user = User("alice","alice@gmail.com",1111)

my_username.say_hi_to_user(new_user)