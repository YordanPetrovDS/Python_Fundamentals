import math

biscuits_per_day = int(input())
workers_count = int(input())
competitor_biscuits = int(input())
total_biscuits = 0

for day in range(1, 31):
    if day % 3 == 0:
        total_biscuits += math.floor(0.75 * biscuits_per_day * workers_count)
    else:
        total_biscuits += biscuits_per_day * workers_count

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > competitor_biscuits:
    print(f"You produce {((total_biscuits - competitor_biscuits) * 100 / competitor_biscuits):.2f} percent more biscuits.")
else:
    print(f"You produce {((competitor_biscuits - total_biscuits) * 100 / competitor_biscuits):.2f} percent less biscuits.")