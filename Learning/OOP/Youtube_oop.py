class YouTube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    
    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1

user1 = YouTube("Lukasz")
user2 = YouTube("Jan")
user3 = YouTube("Jerry")

user1.subscribe(user2)
user3.subscribe(user1)
user3.subscribe(user2)

print("\nUSER 1:")
print(user1.username)
print(f"Subscribers: {user1.subscribers}")
print(f"Subscriptions: {user1.subscriptions}")

print("\nUSER 2:")
print(user2.username)
print(f"Subscribers: {user2.subscribers}") #amount of subscribers
print(f"Subscriptions: {user2.subscriptions}") # amount of subscribed accounts by this account

print("\nUSER 3:")
print(user3.username)
print(f"Subscribers: {user3.subscribers}")
print(f"Subscriptions: {user3.subscriptions}")
