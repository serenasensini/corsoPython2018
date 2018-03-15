file = open("filename.txt", "r")
cont = file.read()
print(cont)
print(file.readlines())
file.close()
	
file = open("filename.txt", "r")
cont = file.read()
print(cont)
for line in file:
    print(line)
file.close()


