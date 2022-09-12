import json


class AutoMessage:
    def __init__(self):
        self.file = open("users.json")
        try:
            self.database = json.load(self.file)
        except:
            self.database = {}
        
    def save_user(self, user):
        aux = self.database.get(str(user.id))
        if aux == None:
            try:
                self.database[str(user.id)] = {"id": str(user.id), "name": user.first_name}
                with open("users.json", "w") as file:
                    json.dump(self.database, file)  
            except:
                None
        else:
            None

    def delete_user(self, user):
        try:
            del self.database[str(user.id)]

            with open("users.json", "w") as file:
                json.dump(self.database, file)
        except KeyError:
            None

    def user_ids(self):
        aux = []
        for user in self.database:
            aux.append(user)
        return aux
        
