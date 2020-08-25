list_integers = list(input().split())
numbers = int(input())

for i in range(len(list_integers)):
    list_integers[i] = int(list_integers[i])

for _ in range(numbers):
    list_integers.remove(min(list_integers))

print(list_integers)

# numbers = list(map(int, input().split()))
# remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]
# print(numbers)
