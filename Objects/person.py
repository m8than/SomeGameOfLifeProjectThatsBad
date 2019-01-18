from Objects.stats import Stats
from draw import Draw
from general import *

class Person():
    def __init__(self, name):
        self.stats = Stats(10, 10, 100)
        self.name = name
    def drawStatsBox(self):
        return Draw.box3(General.dictToPrintable(self.stats.getStats(), True), self.name + ' - Stats')