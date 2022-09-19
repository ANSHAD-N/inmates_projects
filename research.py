import re

pattern = 'python'

file = open("demo.txt", 'r')

if re.search(pattern, file.read()):
    print("matched")

file.close()
