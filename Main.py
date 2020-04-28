import time


#import beemoviescript.txt
script = open("beemoviescript.txt", "r")

#make the script file into a varible
strscript = str(script.read())

#split the script varible into an array (split on spaces)
splitscript = strscript.split()

#print the script
for i in range(0,9157):
    print(splitscript[i])
    time.sleep(0.5)
