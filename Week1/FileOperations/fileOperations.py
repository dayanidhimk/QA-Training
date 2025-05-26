f = open("notes.txt", 'w')
f.write("Python is fun!")
f.close()

f = open("notes.txt")
print(f.read())