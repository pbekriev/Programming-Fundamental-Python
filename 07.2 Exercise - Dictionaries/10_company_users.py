companies = {}
command = input()
while command != 'End':
    company_names, employees_id = command.split(' -> ')
    if company_names not in companies.keys():
        companies[company_names] = []
    if employees_id not in companies[company_names]:
        companies[company_names].append(employees_id)
    command = input()
for company_names, employees in companies.items():
    print(company_names)
    for employees_id in employees:
        print(f"-- {employees_id}")
