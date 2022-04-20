with open("Fruits/vegetables.txt", "a+") as myfile:
    myfile.write("Cucumber\nOnion\nTomato")
    myfile.seek(0)
    content = myfile.read()
print(content)

with open("Fruits/vegetables.txt", "a+") as myfile:
    myfile.write("Cucumber\nOnion\nTomato")
    myfile.seek(0)
    content = myfile.read()
print(content)