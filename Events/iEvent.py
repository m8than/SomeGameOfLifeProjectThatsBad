class iEvent:
    def isAvailable(self, person):
        return True
    def getText(self):
        raise NotImplementedError("Should have implemented this")
    def getOptions(self):
        raise NotImplementedError("Should have implemented this")
    def optionHandler(self, option, person):
        return True