class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()

    def say_hi_to_user(self,user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

my_username = User("clssadik","CilLSaDik@gmail.com",0000)
new_user = User("alice","alice@gmail.com",1111)

my_username.say_hi_to_user(new_user)

print(my_username.clean_email())

# this is not good
# make attribute private
my_username.email = "new@gmail.comö"
print(my_username.email)