import json
class Database:
    __database = dict()
    def __init__(self):
        with open('database.json', 'r') as openfile:
            self.database = dict(json.load(openfile))

    def getDatabase(self):
        return self.database

    def addUser(self, username, password, isAdmin):
        self.database[username] = password
        if("admin" in self.database):
            self.database["admin"] = self.database["admin"].append(username)
        else:
            self.database["admin"] = list().append(username)
        return True

    def serializeDatabase(self):
        json_object = json.dumps(self.database, indent=4)
        with open("database.json", "w") as outfile: 
            outfile.write(json_object)