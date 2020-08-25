card_list = input().split()
players_off = []
count_A = 0
count_B = 0

for card in card_list:
    team = card.split("-")
    if team[0] == "A" and card not in players_off:
        count_A += 1
        players_off.append(card)
    elif team[0] == "B" and card not in players_off:
        count_B += 1
    players_off.append(card)

print(f"Team A - {11 - count_A}; Team B - {11 - count_B}")
if count_A > 4 or count_B > 4:
    print(f"Game was terminated")
