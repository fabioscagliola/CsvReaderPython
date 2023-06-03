import datetime
import unittest
import CsvReader

class Person:
    def __init__(self):
        self.Name = str
        self.BirthDate = datetime.datetime
        self.IsMarried = bool

def ReadPeople():
    people = []
    reader = CsvReader.CsvReader('People.csv', ';')
    reader.Load()
    while reader.ReadLine():
        person = Person()
        person.Name = reader.GetStringValue('Name')
        person.BirthDate = reader.GetDateTimeValue('BirthDate', '%Y-%m-%d')
        person.IsMarried = reader.GetBoolValue('IsMarried')
        people.append(person)
    return people

class CsvReaderTest(unittest.TestCase):
    def test_ExampleUsage(self):
        people = ReadPeople()
        self.assertEqual(2, len(people))

if __name__ == '__main__':
    unittest.main()

