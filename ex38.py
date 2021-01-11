states = {
    "Oregon":"OR",
    "Florida":"FL",
    "California":"CA",
    "New York":"NY",
    "Michigan":"MI"
}

cities = {
    "CA":"San Francisco",
    "MI":"Detroit",
    "FL":"Jacksonville"
}

cities["NY"] ="New York "
cities["OR"] ="Portland"

print("-"*10)
print("NY State has:",cities["NY"])

print("OR state has:",cities["OR"])


print("Michigan's abbreviation is: ",states["Michigan"])

print("Florida's abbreviation is: ",states["Florida"])


print("Michigan has: ", cities[states["Michigan"]])

print("Florida has: ",cities[states["Florida"]])

for state, abbrev in states.items():
    print("%s is abbreviated %s"%(state, abbrev))
# items 將字典的鍵值及值 組成tuple回傳 再放進list 中
# [('Google', 'www.google.com'), ('taobao', 'www.taobao.com'), ('Runoob', 'www.runoob.com')]

for abbrev, city in cities.items():
    print("%s has the city %s"%(abbrev, city))

state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

city = cities.get("TX","Does not Exist")

print("The city for the state 'TX' is: %s"%(city))
