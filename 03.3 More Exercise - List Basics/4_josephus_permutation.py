people_list = input().split()
killed = int(input())
killed_index = 0
killed_people = []
while people_list:
    killed_index += killed - 1
    if killed_index >= len(people_list):
        killed_index = killed_index % len(people_list)
    killed_people.append(people_list[killed_index])
    people_list.__delitem__(killed_index)
print([int(x) for x in killed_people])
