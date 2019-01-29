import os
import argparse

class translate:
    def __init__(self, inputString):
        output = self.toRunes(inputString.upper())
        print(output)

    def toRunes(self, english):
        csv = self.openCSV("runes.csv")
        rune = ''
        n = 0
        while n < len(english):
            char = english[n]
            if n + 1 < len(english):
                second = english[n + 1]
            else:
                second = None
            found = False
            for line in csv.split('\n'):
                i = line.split(',')
                if i[0].find(char) == 0:
                    if len(i[0]) == 2:
                        if second is not None and i[0].rfind(second) == 1:
                            rune += i[1]
                            n += 1
                            found = True
                            break
                    else:
                        rune += i[1]
                        found = True
                        break
            if not found:
                rune += char
            n += 1
        return rune

    def openCSV(self, filePath):
        if os.path.exists(filePath):
            file = open(filePath, 'r')
            text = file.read()
            file.close()
            return text
        else:
            print("Unable to open %s. File not found" % filePath)
            return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert english to runes')
    parser.add_argument('string', type=str, help='Input string to be translated.')

    args = parser.parse_args()
    args = vars(args)
    inputString = args['string']

    tran = translate(inputString.upper())
