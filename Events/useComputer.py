from Events.iEvent import iEvent
import random
from general import General

from game import Game


class useComputer(iEvent):
    def getText(self):
        return "You're sitting at your computer. What do you want to do?\na - Play some games\nb - Browse the web\nc " \
               "- watch some videos\nd - work on your own project\ne - do nothing"

    def getOptions(self):
        return ['a', 'b', 'c', 'd', 'e']

    def optionHandler(self, option, person):
        option = option.lower()
        if option not in ['a', 'b', 'c', 'd']:
            time = 1
        else:
            time = ''
            while not time.replace('.', '').isdigit() or time == '' or abs(float(time)) > 5:
                time = Game.drawGameDialog("How long do you want to spend on your computer?", ["Please enter a decimal number of hours between 0-5 (eg 1.5)"], person)

        time = float(time)
        time_spent = random.uniform(abs(time-.5), time+.5) if person.stats.get('Happiness') > 90 else random.uniform(float(time), float(time)+3)
        additional_text = " A bit longer than expected. Guess you got carried away." if time_spent > time else ""
        if option in ['a', 'b', 'c', 'd', 'e']:
            Game.time += time_spent
        if option == 'a':
            person.stats.set('Energy', -time_spent/1.2, True)
            if person.stats.isset('Assignment'):
                days_left = 7-Game.day
                assignment_todo = 100-person.stats.get('Assignment')
                if assignment_todo > days_left*20:
                    person.stats.set('Happiness', -time_spent * 4, True)
                else:
                    person.stats.set('Happiness', time_spent * 2, True)
            else:
                person.stats.set('Happiness', time_spent * 4, True)

            Game.drawGameMessage("You spent " + General.timeToStr(time_spent) + " hours playing games", person)
            return True
        elif option == 'b':
            person.stats.set('Energy', -time_spent/1.8, True)
            person.stats.set('Happiness', time_spent * 2, True)
            Game.drawGameMessage("You spent " + General.timeToStr(time_spent) + " hours browsing the web." + additional_text, person)
            return True
        elif option == 'c':
            person.stats.set('Energy', -time_spent/1.5, True)
            person.stats.set('Happiness', time_spent * 2, True)
            Game.drawGameMessage("You spent " + General.timeToStr(time_spent) + " hours watching videos." + additional_text, person)
            return True
        elif option == 'd':
            person.stats.set('Energy', -time_spent*1.2, True)
            person.stats.set('Happiness', time_spent * 5, True)
            Game.drawGameMessage("You spent " + General.timeToStr(time_spent) + " hours working on your personal project." + additional_text, person)
            return True
        elif option == 'e':
            person.stats.set('Energy', -time_spent/1.5, True)
            person.stats.set('Happiness', -time_spent, True)
            Game.drawGameMessage("You spent " + General.timeToStr(time_spent) + " hours doing nothing.", person)
            return True
        else:
            return False
