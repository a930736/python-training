#匯入模組
from sys import argv
#有兩個變數 script, filename 要在terminal input
script, filename = argv
# 定義txt 為open物件
txt = open(filename)
print("Here's your file:",filename)
# print out the data in the file
print(txt.read())
txt.close()
print("Type the filename again:")
# define file_name to store new filename, and print >
file_again = input(">")
# define an objcet to txt1
txt1 = open(file_again)
# print out the content of file
print(txt1.read())
txt1.close()
    
    
    

