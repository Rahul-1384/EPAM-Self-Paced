# Ways to initialize strings
name = "Rahul"
name = 'Rahul'
name = '''Rahul'''

# Indexing
name = "Rahul"
print(name[0])  # 'R'
print(name[-1]) # 'l;

# String Slicing
name = "Rahul"
print(name[0:4])
print(name[0:])
print(name[:5])
print(name[-4:-1])

print("String Operations\n")
# String Operations
name = "Hello" + "RR"
print(name)
name = "Hii" * 3
print(name)
print('P' in "Python")
print(len("Python"))


print("String methods\n")
# String Methods
# .upper()
print("hello".upper())

# .lower()
print("HELLO".lower())

# .capitalize()
print("hello".capitalize())

# .title()
print("i am rr".title())

# .strip()
print("  Hii   ".strip())

# .replace()
print("Rahul".replace("R", "r"))

# .split()
print("I am Rahul".split())

# .join()
print("".join(["I", " am", " Rahul"]))

# .find()
print("Rahul".find("R"))

# .count()
print("Rahul".count("a"))

# .startswith()
print("Rahul".startswith("R"))