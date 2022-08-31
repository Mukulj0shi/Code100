
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1



user1 = User(373778, "mukul")
user2 = User(1234, "Raju")
user1.follow(user2)

print(f"user_id = {user1.id}, username = {user1.name}, follower = {user1.followers}, following = {user1.following}")
print(f"user_id = {user2.id}, username = {user2.name}, follower = {user2.followers}, following = {user2.following}")


