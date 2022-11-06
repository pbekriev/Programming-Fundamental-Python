countries = input().split(", ")
capitals = input().split(", ")
# final_result = {countries[index]: capitals[index] for index in range(len(capitals))}
final_result = dict(zip(countries, capitals))
for country, capital in final_result.items():
    print(f"{country} -> {capital}")
