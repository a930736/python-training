import ex38_

states = ex38_.new()

ex38_.set(states,"Oregon", "OR")
ex38_.set(states,"Florida", "FL")
ex38_.set(states,"California", "CA")
ex38_.set(states,"Bew York", "NY")
ex38_.set(states,"Michigan", "MI")

cities = ex38_.new()

ex38_.set(cities,"CA","San Francisco")
ex38_.set(cities,"MI","Detroit")
ex38_.set(cities,"FL","Jacksonville")
ex38_.set(cities,"NY","New York")
ex38_.set(cities,"OR","Portland")

#print out some cities

print("-"*10)
print("NY State has: %s"%ex38_.get(cities,"NY"))
print("OR State has: %s"%ex38_.get(cities,"OR"))

# print some states

print("-"*10)
print("Michigan's abbreviation is : %s"%(ex38_.get(states,"Michigan")))
print("Florida's abbreviation is : %s"%(ex38_.get(states,"Florida")))

#print every state abbeviation
print("-"*10)
ex38_.list(states)

#print every cities abbeviation

print("-"*10)
ex38_.list(cities)

print("-"*10)
a = ex38_.get(states,"Texas")
print(a)

if not a:
    print("Sorry, no Texas.")

city = ex38_.get(cities,"TX", "Does not exist")
print("The city for the state 'TX' is: %s"%(city))

print(ex38_.list(states))

print(ex38_.list(cities))
