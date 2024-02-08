class YouTube:
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers


user1 = YouTube("Lukasz")
print("\nUSER 1:")
print(user1.username)
print(user1.subscribers)

user2 = YouTube("Jan", 5)
print("\nUSER 2:")
print(user2.username)
print(user2.subscribers)

user3 = YouTube("Jerry")
print("\nUSER 3:")
user3.subscribers = 25
print(user3.username)
print(user3.subscribers)
