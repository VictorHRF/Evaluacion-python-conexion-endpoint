class Country:

    def __init__(self, name) -> None:
        self.name = name
        self.code = name[0:3]

    def getName(self):
        return self.name
    
    def getCode(self):
        return self.code