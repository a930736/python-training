def cheese_and_crackers(cheese_count, boxs_of_crackers):
    print("You have %d cheese!"%(cheese_count))
    print("You have %d crackers!"%(boxs_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# 直接用數字給定參數
print("We can just give the function numbers directly: ")
cheese_and_crackers(20,30)


print("Or, we can use variables from our script: ")

amount_of_cheese = 10
amout_of_crackers = 50
# 參數可為變數
cheese_and_crackers(amount_of_cheese,amout_of_crackers)
print("We can even do math inside too: ")
# 參數可由數字加減運作得出
cheese_and_crackers(10+20,5+6)

print("And we can combine the two, variable and math: ")
# 變數與數字加減運算
cheese_and_crackers(amount_of_cheese + 100, amout_of_crackers + 1000)
# entered by user
A = eval(input("Enter "))
B = eval(input("Enter "))
cheese_and_crackers(A,B)

# called by function
def fun(a):
  return a
cheese_and_crackers(fun(3),fun(4))

# insert a list inside a function
x = [1,2,3,4,5]

cheese_and_crackers(x[0],x[4])


part_one = int(input("cheeses:"))
part_two = int(input("crackers: "))
cheese_and_crackers(part_one + int(input("?")), part_two + int(input("?")))

# combine input and variables
part_one = 198 - int(input("?"))
part_two = 200 - int(input("?"))
cheese_and_crackers(part_one,part_two)
