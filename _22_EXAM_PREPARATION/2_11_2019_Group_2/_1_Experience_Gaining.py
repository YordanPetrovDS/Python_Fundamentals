needed_experience = float(input())
count_of_battles = int(input())
total_exp = 0
for i in range(1, count_of_battles + 1):
    exp_per_battle = float(input())

    if i % 3 == 0:
        total_exp += exp_per_battle * 1.15
    elif i % 5 == 0:
        total_exp += exp_per_battle * 0.9
    else:
        total_exp += exp_per_battle
    if total_exp >= needed_experience:
        print(f"Player successfully collected his needed experience for {i} battles.")
        break

if total_exp < needed_experience:
    print(f"Player was not able to collect the needed experience, {(needed_experience - total_exp):.2f} more needed.")
