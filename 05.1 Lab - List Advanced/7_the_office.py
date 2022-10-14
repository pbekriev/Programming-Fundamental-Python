employees_happiness = list(map(int, input().split()))
factor = int(input())
multiply_by_factor = [x * factor for x in employees_happiness]
happy_employeers = list(filter(lambda x: x >= sum(multiply_by_factor) / len(multiply_by_factor), multiply_by_factor))
# avr_happyiness = sum(multiply_by_factor) / len(multiply_by_factor)
# happy_employees = [x for x in multiply_by_factor if x >= avr_happyiness]
if len(happy_employeers) >= len(multiply_by_factor) / 2:
    print(f"Score: {len(happy_employeers)}/{len(multiply_by_factor)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employeers)}/{len(multiply_by_factor)}. Employees are not happy!")
