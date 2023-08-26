
with open("hello", "a") as archive:
    names = ["João", "Maria", "José"]
    for name in names:
        archive.write(name+"\n")

with open("hello", "r") as archive:
    for line in archive:
        print(line)

