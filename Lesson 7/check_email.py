import re

print(re.search(r"@", "margo@gmail.com"))
print(re.search(r"[\w.]+@", "margo@gmail.com"))
print(re.search(r"[\w.]+@[\w]+", "margo@gmail.com"))
# print(re.search(r"[\w.]+@[\w]+\.[a-z]{2,3}", "margo@gmail.com"))
print(re.search(r"^[\w.]+@[\w]+\.[a-z]{2,}$", "margo@gmail.com"))
print(re.search(r"^[\w.]+@[\w]+\.[a-z]+$", "margo@gmail.com and more text"))

print(re.search(r"\w.+@\w+\.[a-z]{2,3}", "arfami@***&&@@icloud.com"))

