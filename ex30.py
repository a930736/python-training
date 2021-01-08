people = 30

cars = 40

buses = 15
# compare cars people
if cars > people and cars < buses:
    print("We should take the cars.")
# compare cars > people
elif cars > people and buses < people:
    print("We should not take the cars.")
# the rest of result
else:
    print("We can't decide.")


if buses > cars:
    print("That's too many buses.")

elif buses < cars:
    print("Maybe we could take the buses.")

else:
    print("We still can't decide.")


if people > buses:
    print("Alright, let's just take the buses.")

else:
    print("Fine, let's stay home then.")
