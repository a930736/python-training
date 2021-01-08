def add(a,b):
    print("Adding %d +%d"%(a,b))
    return a+b

def substract(a,b):
    print("SUBSTRACTING %d - %d"%(a,b))
    return a-b

def multiply(a,b):
    print("Multiplying %d * %d"%(a,b))
    return a*b

def divide(a,b):
    print("Dividing %d / %d"%(a,b))
    return a / b

print("Let's do some math with just functions!")

age = add(30,5)

height = substract(78,4)

weight = multiply(90,2)

iq = divide(100,2)

print("Age:%d, height: %d, Weight: %d, IQ: %d"%(age,height,weight,iq))

print("Here is a puzzle.")
#  (height - ((iq/2)*weight) + age)
what = add(age, substract(height,multiply(weight,divide(iq,2))))

print("That becomes:",what,"Can you do it by hand?")

# 24+34/100 -1023

print(add(24,substract(divide(34,100),1023)))
