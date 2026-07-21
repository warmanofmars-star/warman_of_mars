#with open("user.json", "r", encoding="utf-8") as file:
#    print (file.read())

#print ("START PROGRAM")
#result = 10/0
#print (result)
#print ("END PROGRAM")

#try/except

print ("START PROGRAM")
try:
    result = 10/0
    print (result)
except Exception as e:
    print ("An error occurred: ", e)

print ("END PROGRAM")
print ()

def is_number (text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False

try:
    value = int("25")
except ValueError:
    print ("This is not as number")
else:
    print ("The transformation was successful: ", value)
finally:
    print ("This block is always executed")



