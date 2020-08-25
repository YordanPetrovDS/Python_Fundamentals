n = int(input())
word = input()
strings = []

for _ in range(n):
    strings.append(input())

# =========== List Comprehension ============
# strings = [input() for _ in range(n)]

print(strings)
print([string for string in strings if word in string])


#def is_awesome(name):
  #  return name == word


#print(list(filter(is_awesome, strings)))


