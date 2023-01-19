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
    def __init__(self, hair_color, top, baggage):
        self.hair_color = hair_color
        self.top = top
        self.baggage = baggage

    # def __str__(self):
    #     return f"{self.hair_color}, {self.top}, {self.baggage}"
    #
    # def __repr__(self):
    #     return 'Person(%s, %s, %b)' % (self.hair_color, self.top, self.baggage)


# 2. Instantiating an object
person_1 = Person("red", "t-shirt", True)
#
# print("Name of first person: ", person_1.name)
#
# print("Whole first person: ", person_1)

# 3. Storing objects in list
# person_2 = Person("Will", 28, 98765)
# person_3 = Person("Wren", 41, 24680)
#
# obj_arr = [person_2, person_3]
#
# print("people object array", obj_arr)


# RELATIONAL DATABASE (SQL










