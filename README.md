# CsvReader

A utility module providing a way of reading a forward-only stream of rows from a CSV file.

## Overview

The **CsvReader** module allows reading from a CSV file given its path.

It is designed to load one line at a time and retrieve the values of the individual fields using the names included in the header row.

If the file does include a header row, it is possible to inject the field names.

## Example usage

Let us consider the following CSV file including a header row.

```
Name;BirthDate;IsMarried
John;1975-01-23;true
Jane;1985-07-07;false
```

The following sample code reads from the file into a list of objects.

```python
import datetime
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
```

If the file did not include the header row, the field names could be injected using the Load() method.

```python
reader.Load(['Name', 'BirthDate', 'IsMarried'])
```

