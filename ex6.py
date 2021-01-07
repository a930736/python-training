# this combine the string and numbers
x = "Ther are %d types of people."%10
# this define a string
binary = "binary"
# this define a string
do_not ="don't"
# this insert two strings insdie a string 1
y = "Those who know %s and those who %s."%(binary,do_not)
# print
print(x)
print(y)
# insert x string 2
print("I said:%r."%(x))
# insert y string 3
print("I also said:'%s'"%(y))

hilarious = False
# 4
joke_evaluation = "Isn't that joke so funny?! %r"
#joke裡有格式化變量，而那個變量為hilarious
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = " a string with a right side."
# add two strings
print(w+e)
