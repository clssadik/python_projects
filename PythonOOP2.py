class User:
    def __init__(self, user_id,username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

user1 = User("001","clssadik")
user2 = User("002","clssadik2")

user1.follow(user2)
print(user1.followers)
print(user1.following)