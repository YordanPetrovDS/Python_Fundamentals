n = int(input())
chairs_list = []
chairs_left = 0
valid = True
for room in range(1, n + 1):
    chairs_list = input().split()
    if len(chairs_list[0]) >= int(chairs_list[1]):
        chairs_left += (len(chairs_list[0]) - int(chairs_list[1]))
    else:
        print(f"{abs(len(chairs_list[0]) - int(chairs_list[1]))} more chairs needed in room {room}")
        valid = False

if valid:
    print(f"Game On, {chairs_left} free chairs left")
