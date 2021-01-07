from sys import argv

script, first, second, third = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

script = input("The script is called: ")
first = input("The first is called: ")
second = input("The second is called: ")
third = input("The third is called: ")

print("""
The script is called:%r
The first variable is %r
The second variable is %r
The third variable is %r
"""%(script,first,second,third)
)
