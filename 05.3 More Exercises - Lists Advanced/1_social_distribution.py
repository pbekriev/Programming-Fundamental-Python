population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
index_for_take = population.index(max(population))
no_possible = False
for index, part_of_populatoion in enumerate(population):
    if part_of_populatoion <= minimum_wealth:
        diff = minimum_wealth - part_of_populatoion
        if population[index_for_take] < minimum_wealth + diff:
            index_for_take = population.index(max(population))
        population[index] += diff
        population[index_for_take] -= diff
        if population[index_for_take] < minimum_wealth:
            no_possible = True
            break
if no_possible:
    print("No equal distribution possible")
else:
    print(population)
