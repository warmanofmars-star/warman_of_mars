age = 25
Name = 'Ivan'

said = 'She said "Hello"'
print (said)

raw_string = r"C:\Program Files\Python"
print (raw_string)

s1 = "Hello wold"
print (type (s1))
s2 = 5
print (type(s2))
s3 = False
print (type(s3))
s4 = 3.8
print(type(s4))

s1 = 'zeleno'
s2 = 'glazka'
s3 = s1 + s2
s4 = s2 + s1
print (s3)
print (s4)

#join ()
words = ["Hello", "Word", "and", "Python"]
result = " ".join(words)
print (result)

st = 'ab' * 7
print (st)

s1 = 'Vasya Pupkin'
s2 = 'Vasya'
if s2 in s1:
    print ("User Vasya in our database")
else:
    print ("User Vasya not in our database")

st = 'a'
if st=='a' or st=='b' or st=='c' or st=='b':
    print ("Yes")

if st in 'abcd':
    print ("Yes")

ln = len ('zelenoglazka')
print (ln)

st = "Python"
for x in st:
    print (x)
print (st[0:3])
print (st[2:5])
print (st[2:4])

my_string = "Hello world!"
every_second_char = my_string [::2]
reversed_string = my_string [::-1]
print (every_second_char)
print (reversed_string)

name = 'Alice'
age = 30
formatted_string = f"Hello, my name {name}. My age {age}"
print (formatted_string)

s = 'Abrakadabra'
str = 'bra'
print(s.find(str))
print(s.rfind(str))
print(s.count(str))
print (s.lower())
print (s.upper())
print (s)

s = "Cat, Dog,Hamster Rabbit, PIG"
print (s.split())
print (s.split(','))
print (s.split(',', 2))

s = "Hi!"
print (s.rjust(10, '*'))
print(s.ljust(10, '*'))

test = ["Login", "Cart", "API"]
for t in test:
    print(t.ljust(15), "OK")

text = "QA automation with Python"
pos = text.index("automation")
print (pos)

text1 = "I like Java"
print (text1.replace("Java", "Python"))
text3 = "2026-07-03"
new_text = text3.replace("-", "/")
print (text3)
print (new_text)

x=1
while x<5:
    print (x)
    x = x+1
