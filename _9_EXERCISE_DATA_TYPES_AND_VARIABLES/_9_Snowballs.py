n = int(input())
snowballValue = 0

for i in range(1, n + 1):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())
    current_snowballValue = (snowballSnow / snowballTime) ** snowballQuality
    if current_snowballValue >= snowballValue:
        snowballValue = current_snowballValue
        lastSnow = snowballSnow
        lastSnowballTime = snowballTime
        lastSnowballQuality = snowballQuality
print(f"{lastSnow} : {lastSnowballTime} = {snowballValue:.0f} ({lastSnowballQuality})")
