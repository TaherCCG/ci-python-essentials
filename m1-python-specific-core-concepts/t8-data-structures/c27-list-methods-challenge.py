crew = ["Jean-Luc", "Wesley", "Warf", "Deanna", "William", "Data", "Geordie", "Tasha"]

print(crew)
crew.pop()
print(crew)
crew.append('Beverly')
print (crew)
crew.extend(['Miles','Guinan'])
print (crew)
crew.sort(key=len, reverse=True)
print (crew)

