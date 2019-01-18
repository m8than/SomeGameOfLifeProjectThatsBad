class Stats():
    __stats = dict()
    def __init__(self, energy, stamina, happiness):
        self.__stats['Status'] = 'Happy'
        self.__stats['Energy'] = energy
        self.__stats['Stamina'] = stamina
        self.__stats['Happiness'] = happiness
    def isset(self, stat):
        return stat in self.__stats
    def get(self, stat):
        return self.__stats[stat]
    def set(self, stat, value, modify=False):
        if modify:
            self.__stats[stat] += value
        else:
            self.__stats[stat] = value
    def getStats(self):
        return self.__stats;
