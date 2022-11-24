import re

racers = {}
list_of_participants = input().split(", ")
command = input()
while command != "end of race":
    name = "".join(re.findall("(?i)[a-z]", command))
    distance = re.findall("[0-9]", command)
    distance = [int(x) for x in distance]
    if (name in list_of_participants) and (name not in racers.keys()):
        racers[name] = 0
    if name in racers.keys():
        racers[name] += sum(distance)
    command = input()
racers = sorted(racers.items(), key=lambda x: -x[1])
print(f"""1st place: {racers[0][0]}
2nd place: {racers[1][0]}
3rd place: {racers[2][0]}""")
