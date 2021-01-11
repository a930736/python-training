class Thing():
    def test(self):
        print("hi")

a = Thing()
a.test()

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(" ")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now."%(len(stuff)))

print("There we go: ",stuff)

print("Let's do some things with stuff.")
# print the second number
print(stuff[1])
# print the last number
print(stuff[-1])
# pop(stuff) print out the last number and remove it from list
print(stuff.pop())
# join the element in the list with " "
print(" ".join(stuff))
# combine the forth and fifth element in the list with
# a = string not a list
a = "#".join(stuff)
print("#".join(stuff[3:5]))
print(a)
print(type(a))

