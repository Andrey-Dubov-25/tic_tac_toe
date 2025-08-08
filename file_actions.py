file = open("example.txt", "r", encoding="utf-8")

content = file.read(12)

print(content)

file.close()
