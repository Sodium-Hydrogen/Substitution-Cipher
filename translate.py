import os
import argparse

class translate:
    def __init__(self, directory, file):
        self.directory = directory.replace('/', '')
        self.filePath = self.directory + "/" + file

    def openCSV(self):
        if os.path.exists(self.filePath):
            file = open(self.filePath, 'r')
            text = file.read()
            file.close()
            return text
        else:
            print("Unable to open %s. File not found" % self.filePath)
            return None

    def listCSV(self):
        if os.path.exists(self.directory):
            content = os.listdir(self.directory)
            output = ''
            for i in content:
                if i.lower().find('.csv') != -1:
                    self.filePath = self.directory + "/" + i
                    output = i + " - " + self.toAlternate("ABC123") + '\n'
            return output
        else:
            print("Unable to find directory: %s" % self.directory)
            return None

    def toAlternate(self, inputString):
        return self.convert(inputString, 1, 0)

    def toOriginal(self, inputString):
        return self.convert(inputString, 0, 1)

    def convert(self, inputString, toCol, fromCol):
        csv = self.openCSV()
        output = ''
        n = 0
        while n < len(inputString) and csv is not None:
            char = inputString[n]
            if n + 1 < len(inputString):
                second = inputString[n + 1]
            else:
                second = None
            found = False
            for line in csv.strip().split('\n'):
                i = line.split(',')
                if i[fromCol].find(char) == 0:
                    if len(i[fromCol]) == 2:
                        if second is not None and i[fromCol].rfind(second) == 1:
                            output += i[toCol]
                            n += 1
                            found = True
                            break
                    else:
                        output += i[toCol]
                        found = True
                        break
            if not found:
                output += char
            n += 1
        if csv is None:
            return inputString
        else:
            return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Substitute cipher based off of a dictionary.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('input_string', type=str, nargs='?', default=None, help='Input string to be translated.')
    group.add_argument('-l', '--list', action='store_true', default=False, help='List all available dictionaries.')
    parser.add_argument('-r', '--reverse', action='store_true', default=False, help='Convert translated string back.')
    parser.add_argument('-u', '--use_case', action='store_true', default=False, help='Do not ignore capitalization of letters.')
    parser.add_argument('-D', '--dir', type=str, default='dictionaries', help='Path of dictionaries directory.')
    parser.add_argument('-d', '--dict', type=str, default='runes.csv', help='Dictionary to use.')

    args = parser.parse_args()

    if not args.use_case and not args.list:
        args.input_string = args.input_string.upper()

    tran = translate(args.dir, args.dict)
    if not args.reverse and not args.list:
        print(tran.toAlternate(args.input_string))
    elif not args.list:
        print(tran.toOriginal(args.input_string))
    else:
        output = tran.listCSV()
        if output is not None:
            print("Avaliable Dictionaries:\n%s" % output, end='')
