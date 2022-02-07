class User:
    def __init__(self, name, user_id):
        # initialise attributes of the class
        self.name = name
        self.user_id = user_id


user_1 = User("Ranga", "007")
print(user_1.name, user_1.user_id)