from sys import argv
from os.path import exists


script, from_file, to_file = argv

print("Copying from %s to %s "%(from_file,to_file))

#indata =open(from_file).read()
      
print("The input file is %d bytes long"%(len(open(from_file,"r").read())))
      
print("Does the output file exist? %r"%(exists(to_file)))

print("Ready, hit Return to continue, CTRL-C to abort.")
input("?")
      
#out_file = open(to_file,"w")
#out_file.write(indata)
#output = open(to_file,"w").write(indata)
open(to_file,"w").write(open(from_file,"r").read())
print("Alright, all done.")

print(open(to_file).read())

