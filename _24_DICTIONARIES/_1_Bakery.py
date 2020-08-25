def solution(raw_data):
    data = raw_data.split(' ')
    return {data[i]: data[i + 1] for i in range(0, len(data), 2)}


print(solution(input()))

# elements = input().split()

# bakery = {}
#
# for i in range(0, len(elements), 2):
#     key = elements[i]
#     value = elements[i + 1]
#     bakery[key] = int(value)
