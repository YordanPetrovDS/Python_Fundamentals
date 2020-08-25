journey_cost = float(input())
months_count = int(input())
saved_money = 0

for m in range(1, months_count + 1):
    if m > 1 and m % 2 != 0:
        saved_money -= saved_money * 0.16
    if m % 4 == 0:
        saved_money += saved_money * 0.25
    saved_money += 0.25 * journey_cost

if saved_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {abs(saved_money - journey_cost):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(journey_cost - saved_money):.2f}lv. more.")
