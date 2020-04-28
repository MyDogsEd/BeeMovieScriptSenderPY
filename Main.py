import time

# Have the user input the amount of seconds to wait in between words.
file = str(input("Enter the name and extension file that you want to read from."))
timeSleep = float(input("Enter the amount of time in seconds to wait in between words."))

# import user's file
script = open(file, "r")

# make the script file into a variable
strScript = str(script.read())

# split the script variable into an array (split on spaces)
splitScript = strScript.split()

splitScriptLength = len(splitScript)

# print the script
for i in range(0, splitScriptLength):
    print(splitScript[i])
    time.sleep(timeSleep)
