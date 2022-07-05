class Language:

    def __init__(self, name) -> None:
        self.name = name
        self.code = name[0:2]

    def getName(self):
        return self.name
    
    def getCode(self):
        return self.code