with open("users.txt", "w", encoding="utf-8") as file:
    file.write("tony \n")
    file.write("ivan \n")
    file.write("anna \n")

#read() - reading full file
with open("users.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
print(len(content))

#readlines() - vozvrashaets spisok, gde kajdii element - odna stroka
with open("users.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print (lines)

for line in lines:
    print(line.strip())

print ()

with open("users.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())