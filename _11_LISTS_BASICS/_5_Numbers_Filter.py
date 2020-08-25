def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def is_negative(number):
    return number < 0


def is_positive(number):
    return number >= 0


# Dictionary
# filters_map = {
# 'even': is_even,
# 'odd': is_odd,
#  'positive': is_positive,
#   'negative': is_negative,
# }

filters_map = {
    'even': lambda number: number % 2 == 0,
    'odd': lambda number: number % 2 != 0,
    'positive': lambda number: number >= 0,
    'negative': lambda number: number < 0,
}

n = int(input())
numbers = [int(input()) for _ in range(n)]
# command = input()

# filter_fn = filters_map[command]

#filter_fn = filters_map[input()]
# validation if the command differs even,odd,positive,negative: the output will be None
filter_fn = filters_map.get(input())

if filter_fn is not None:
    print([n for n in numbers if filter_fn(n)])
else:
    print('Unsupported command.')
