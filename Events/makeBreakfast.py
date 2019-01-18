from Events.iEvent import iEvent
from Events.goToWash import goToWash
from game import Game

import random
class makeBreakfast(iEvent):
    def getText(self):
        random_foods = [['cereal', 8, 4, .2], ['eggs', 10, 2, .5], ['toast', 8, 2, .5], ['coffee', 5, 5, .3],
                        ['bagel', 5, 3, .2], ['berries and yoghurt', 9, 3, .6], ['nuts', 4, 4, .1],
                        ['apple', 6, 3, .15], ['berry smoothie', 10, 3, .7]]
        self.foods = random.sample(random_foods, 3)
        return f"You're hungry, what do you eat for breakfast?\na - {self.foods[0][0]}\nb - {self.foods[1][0]}\nc - {self.foods[2][0]}"

    def getOptions(self):
        return ['a', 'b', 'c']

    def optionHandler(self, option, person):
        Game.time += self.foods[0][3]
        Game.next_event = goToWash
        if option == 'a':
            person.stats.set('Happiness', self.foods[0][1], True)
            person.stats.set('Energy', self.foods[0][2], True)
            return True
        elif option == 'b':
            person.stats.set('Happiness', self.foods[1][1], True)
            person.stats.set('Energy', self.foods[1][2], True)
            return True
        elif option == 'c':
            person.stats.set('Happiness', self.foods[2][1], True)
            person.stats.set('Energy', self.foods[2][2], True)
            return True
        else:
            return False
