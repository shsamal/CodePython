"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):

    def __init__(self):
        self.items = []

    def addItem(self, add_items):
        # add_items = input("New Item: ")
        self.items.append(add_items)

    def getClassiness(self):
        self.points = 0
        for i in self.items:
            if i == "tophat":
                self.points += 2
            elif i == "bowtie":
                self.points += 4
            elif i == "monocle":
                self.points += 5
        # else:
        #     self.points += 0
        return self.points


# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
print(me.items)
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
print(me.items)
# Should be 11
print(me.getClassiness())
#
me.addItem("bowtie")
print(me.items)
# Should be 15
print(me.getClassiness())

