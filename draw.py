import textwrap
import os

class Draw:
    @staticmethod
    def clear():
        os.system('cls||clear')
        print()
    @staticmethod
    def toLines(string, length, padding, centered=True):
        string = string.replace('\n', ' '*length)
        lines = textwrap.wrap(string, length, replace_whitespace=False)

        for i in range(len(lines)):
            if centered:
                lines[i] = lines[i].center(length+padding, ' ')
            else:
                lines[i] = ((' '*3) + lines[i]).ljust(length+padding, ' ')
        return lines
    @staticmethod
    def toScreen(lines):
        for line in lines:
            print(line)

    @staticmethod
    def addHorizontal(list1, list2, padding=0):
        maxlines = len(list1) if len(list1) > len(list2) else len(list2)
        lines = [''] * maxlines

        maxwidth = 0
        for x in range(len(list1)):
            lines[x] = list1[x]
            if len(list1[x]) > maxwidth:
                maxwidth = len(list1[x])

        for x in range(len(list2)):
            if x >= len(list1):
                lines[x] += (' ' * maxwidth)
            lines[x] = lines[x].rjust(maxwidth)
            lines[x] += (' ' * padding) + list2[x]

        return lines
    @staticmethod
    def addVertical(list1, list2, padding):
        result = list(list1)
        result.extend([''] * padding)
        result.extend(list2)
        return result

    @staticmethod
    def box1(message, title='', centered=True):
        box = list()
        box.append('####################################')
        if title != '':
            box.append("#" + (f" {title} ").center(34, ' ') + "#")
            box.append('####################################')

        box.extend([
                '#                                  #',
                '#                                  #'
        ])

        lines = Draw.toLines(message, 24, 10, centered)
        for line in lines:
            box.append(f"#{line}#")

        box.extend([
                '#                                  #',
                '#                                  #',
                '####################################'
        ])
        return box

    @staticmethod
    def box2(message, title='', centered=True):
        box = list()
        box.append('------------------------------------')
        if title != '':
            box.append("|" + (f" {title} ").center(34, ' ') + "|")
            box.append('------------------------------------')

        box.extend([
                '|                                  |',
                '|                                  |'
        ])

        lines = Draw.toLines(message, 24, 10, centered)
        for line in lines:
            box.append(f"|{line}|")

        box.extend([
                '|                                  |',
                '|                                  |',
                '------------------------------------'
        ])
        return box

    @staticmethod
    def box3(message, title='', centered=True):
        box = list()
        box.append('/==================================\\')
        if title != '':
            box.append("|" + (f" {title} ").center(34, ' ') + "|")
            box.append('|==================================|')

        box.extend([
                '|                                  |',
                '|                                  |'
        ])

        lines = Draw.toLines(message, 24, 10, centered)
        for line in lines:
            box.append(f"|{line}|")

        box.extend([
                '|                                  |',
                '|                                  |',
                '\==================================/'
        ])
        return box
    @staticmethod
    def eventBox3(message, title='', options=list(), centered=True):
        box = list()
        box.append('/============================================================\\')
        if title != '':
            box.append("|" + (f" {title} ").center(60, ' ') + "|")
            box.append('|============================================================|')

        box.extend([
                '|                                                            |',
                '|                                                            |'
        ])

        lines = Draw.toLines(message, 50, 10, centered)
        for line in lines:
            box.append(f"|{line}|")

        box.extend([
                '|                                                            |',
                '|                                                            |'
        ])
        if len(options) > 0:
            dividers = (len(options)-1)*2
            linewidth = int((60-dividers)/len(options))
            line = ''
            for option in options:
                line += option.center(linewidth) + '||'
            line = '|' + line[:-2].center(60) + '|'
            box.extend([
                    '|============================================================|',
                    line,
            ])
        box.append('\============================================================/')
        return box