people_list = input().split()
killed = int(input())
killed_count = 0
killed_people = []
while people_list:
    killed_count += killed - 1
    if killed_count >= len(people_list):
        killed_count = killed_count % len(people_list)
    killed_people.append(people_list[killed_count])
    people_list.__delitem__(killed_count)
print([int(x) for x in killed_people])
