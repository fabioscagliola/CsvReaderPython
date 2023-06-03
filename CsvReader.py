import datetime

class CsvReader:
    def __init__(self, path: str, separator: str):
        self.path = path
        self.separator = separator
        self.line = ''
        self.lineIndex = -1
        self.lineList = list[str]
        self.keys = list[str]
        self.values = list[str]
    def Load(self, keys: list[str] = None):
        with open(self.path, 'r') as file:
            self.lineList = file.read().splitlines()
        if keys != None:
            self.keys = keys
        else:
            result = self.ReadLineTo()
            if result[0]:
                self.keys = result[1]
    def ReadLineTo(self):
        read = False
        line = ''
        self.lineIndex += 1
        if self.lineIndex < len(self.lineList):
            self.line = self.lineList[self.lineIndex]
            line = self.lineList[self.lineIndex].split(self.separator)
            read = True
        return read, line
    def ReadLine(self):
        result = self.ReadLineTo()
        if result[0]:
            self.values = result[1]
        return result[0]
    def GetStringValue(self, key: str):
        index = self.keys.index(key)
        return str(self.values[index]).strip()
    def GetBoolValue(self, key: str):
        return self.GetStringValue(key).lower() == 'true'
    def GetDateTimeValue(self, key: str, format: str):
        return datetime.datetime.strptime(self.GetStringValue(key), format)

