n = int(input())

positives = []
negatives = []

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

#============ Comprehension ===============
#numbers = [int(input()) for _ in range(n)]
#positives = [i for i in numbers if i >= 0]
#negatives = [i for i in numbers if i < 0]

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")
