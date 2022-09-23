number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shild_price = float(input())
armor_price = float(input())
broken_helmes = number_of_lost_fights // 2
broken_sword = number_of_lost_fights // 3
broken_shild = number_of_lost_fights // 6
broken_armor = number_of_lost_fights // 12
expenses = helmet_price * broken_helmes + \
           sword_price * broken_sword + \
           shild_price * broken_shild + \
           armor_price * broken_armor
print(f"Gladiator expenses: {expenses:.2f} aureus")
