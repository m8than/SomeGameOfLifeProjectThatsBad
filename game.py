from general import *
from draw import Draw

class Game:
    day = 0
    time = 8
    cur_error = ''
    next_event = None
    attributes = []
    @staticmethod
    def updateStatus(person):
        happiness = person.stats.get('Happiness')
        energy = person.stats.get('Energy')
        if happiness > 120:
            status = 'Very Happy'
        elif happiness > 90:
            status = 'Happy'
        elif happiness > 50:
            status = 'Fine'
        elif happiness > 30:
            status = 'Depressed'

        if energy < 3:
            status = 'Tired'
        person.stats.set('Status', status)

    @staticmethod
    def drawGameMessage(message, person):
        message = Draw.eventBox3(message, 'Event Message', ['Press enter to continue'])
        game_box = Game.drawGameBox()
        stats_box = person.drawStatsBox()
        side_bar = Draw.addVertical(game_box, stats_box, 2)

        message_bottom = list([''] * (len(side_bar) - len(message)))
        message_bottom.extend(message)
        screen = Draw.addHorizontal(message_bottom, side_bar, 8)

        Draw.clear()
        Draw.toScreen(screen)
        input()
    @staticmethod
    def drawGameDialog(message, options, person):
        message = Draw.eventBox3(message, 'Event Message', options)
        game_box = Game.drawGameBox()
        stats_box = person.drawStatsBox()
        side_bar = Draw.addVertical(game_box, stats_box, 2)

        message_bottom = list([''] * (len(side_bar) - len(message)))
        message_bottom.extend(message)
        screen = Draw.addHorizontal(message_bottom, side_bar, 8)

        Draw.clear()
        Draw.toScreen(screen)
        return input('Option: ')
    @staticmethod
    def drawGameBox():
        gamestats_dict = {
            'Time': General.timeToStr(Game.time),
            'Day': str(Game.day)
        }
        return Draw.box3(General.dictToPrintable(gamestats_dict), 'Game')
    @staticmethod
    def getCurrentAttributes():
        result = []
        for attribute in Game.attributes:
            if attribute['day'] > Game.day:
                result.append(attribute['name'])
            elif attribute['day'] == Game.day and attribute['time'] < Game.time:
                result.append(attribute['name'])
        return result
    @staticmethod
    def attributeSet(name):
        return name in Game.getCurrentAttributes()
    @staticmethod
    def setAttribute(name, day, time):
        Game.attributes.append({'name': name, 'day': day, 'time': time})