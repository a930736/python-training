from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
# return to the begining
def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline(),end="")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:\n")

current_line = 1
# first read the first line 移動到\n 後面 也就是下一行的開頭
print_a_line(current_file,current_file)

current_line += 1
# read the second line
print_a_line(current_line,current_file)

current_line += 1
# then read the third line
print_a_line(current_line,current_file)

