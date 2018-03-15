file = open("newfile.txt", "r")
print("Reading contents")
print(file.read())
file.close()

file = open("newfile.txt", "w")
file.write("Some bla bla bla")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
file.close()


