file = open("demo.txt", 'w')
file.write("This is a demo text file")
file.close()

file = open("demo.txt", 'r')
print(file.read())
file.close()

file = open("demo.txt", 'a')
file.write("\n This is an addition to this file")
file.close()

file = open("demo.txt", 'r')
print(file.read())
file.close()
