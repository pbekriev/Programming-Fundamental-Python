gifts_plan = input().split()
command_before_split = ""
while command_before_split != "No Money":
    command_before_split = input()
    command = command_before_split.split()
    if "OutOfStock" in command:
        for gift_for_remove in range(len(gifts_plan)):
            if gifts_plan[gift_for_remove] == command[1]:
                gifts_plan[gift_for_remove] = None
    elif "Required" in command:
        if int(command[2]) <= len(gifts_plan)-1:
            gifts_plan[int(command[2])] = command[1]
    elif "JustInCase" in command:
        gifts_plan[-1] = command[1]
final_gifts = [gift for gift in gifts_plan if gift]

print(" ".join(final_gifts))