number_of_electrons = int(input())
shells = []
position = 1
while True:
    shell = 2 * position ** 2
    if shell <= number_of_electrons:
        shells.append(shell)
        number_of_electrons -= shell
    position += 1
    if number_of_electrons < shell:
        shells.append(number_of_electrons)
        break

print(shells)
