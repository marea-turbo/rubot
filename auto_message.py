import json
from datetime import datetime


class AutoMessage:
    def __init__(self):
        self.file = open("users.json")
        try:
            self.database = json.load(self.file)
        except:
            self.database = {}
        
    def save_user(self, user):
        try:
            self.database[user.id] = {"id": user.id, "name": user.first_name}
            with open("users.json", "w") as file:
                json.dump(self.database, file)
        except:
            print("Erro não deu /start no pv")

    def delete_user(self, user):
        print(self.database)
        print(user.id)
        del self.database[str(user.id)]
        with open("users.json", "w") as file:
            json.dump(self.database, file)

    def user_ids(self):
        for user in self.database:
            aux = []
            aux.append(user)
        return aux
        
