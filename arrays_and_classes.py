# ARRAYS (aka LISTS)

# 1. Initializing
people = ['Tim', 'Ted', 'Tif']
# print("all values in people: ", people)

counts = [1, 2, 4]
# print("all values in counts: ", counts)

booleans = [True, False, True]
# print("all values in booleans: ", booleans)

misc = [0, '', False]
# print("all values in misc", misc)

# 2. Accessing elements (zero-indexed)
# print("value at index 0: ", people[0])
# print("value at index 2: ", people[2])

# numPeople = len(people)
# print("length of people: ", numPeople)
# print("value at end of the list: ", people[numPeople - 1])

# 3. Adding elements
# people.append('Tes')
# print("after adding a new value: ", people)

# 4. Other operations possible too...
# people.sort()
# people.pop()
# people.count("Tim")


# CLASSES AND OBJECTS

# 1. Defining a class
class Person:
    def __init__(self, hair_color, top, baggage, passenger_id):
        self.hair_color = hair_color
        self.top = top
        self.baggage = baggage
        self.passenger_id = passenger_id

    def __str__(self):
        return f"{self.passenger_id} {self.hair_color}, {self.top}, {self.baggage}"

    def __repr__(self):
        return 'Person(%i, %s, %s, %i)' % (self.passenger_id, self.hair_color, self.top, self.baggage)


# 2. Instantiating an object
# person_1 = Person("red", "t-shirt", True, 12345)
#
# print("Name of first person: ", person_1.name)
#
# print("Whole first person: ", person_1)

# 3. Storing objects in list
# person_2 = Person("blonde", "blazer", True, 67890)
# person_3 = Person("brunette", "overcoat", False, 24680)
#
# obj_arr = [person_2, person_3]
#
# print("people object array", obj_arr)


# RELATIONAL DATABASE (SQLite)

# 1. Creating the database and table
import sqlite3
connection = sqlite3.connect('passengers.db')
cursor = connection.cursor()

# table = """CREATE TABLE PASSENGERS (
#     PASSENGER_ID INTEGER not null primary key,
#     HAIR_COLOR VARCHAR(20) not null,
#     TOP VARCHAR(20) not null,
#     BAGGAGE INTEGER not null )"""
# cursor.execute(table)
#
# # 2. Inserting rows into table
# cursor.execute("INSERT INTO PASSENGERS VALUES (123, 'red', 'peacoat', 0)")
# cursor.execute("INSERT INTO PASSENGERS VALUES (456, 'brown', 'sportcoat', 1)")
# cursor.execute("INSERT INTO PASSENGERS VALUES (789, 'blonde', 'hoodie', 0)")
# connection.commit()
# connection.close()

# 3. Retrieving the data
# cursor.execute("SELECT * FROM PASSENGERS")
# passengerRecords = cursor.fetchall()
# print("passengerRecords", passengerRecords)
# print("passengerRecords[0]", passengerRecords[0])

# 4. Storing the data in objects and a list
# passengerList = []
# 
# for p in passengerRecords:
#     passenger = Person(p[1], p[2], p[3], p[0])
#     passengerList.append(passenger)
# 
# print("passengerList", passengerList)








