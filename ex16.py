from sys import argv

script, filename = argv

print("We're going to erase %r."%(filename))
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit Enter.")
input("?")

print("Opening the file...")
target = open(filename,"w")

print("Truncating the file. Goodbye!")
target.truncate()
# truncate 要在w模式下才可用
print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm goning to write these to the file.")

target.write(line1+"\n"+line2+"\n"+line3+"\n")


print("And finally, we close it")
target.close()


