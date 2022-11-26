import re

special_pattern = r"(?i)[star]"
pattern = r".*@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*"
massages = int(input())
attacked_planets_count = 0
attacked_planets_names = []
destroyed_planets_count = 0
destroyed_planets_names = []
for i in range(massages):
    encrypted_massage = input()
    number_of_special_letters = len(re.findall(special_pattern, encrypted_massage))
    decrypt_massage = "".join([chr(ord(x) - number_of_special_letters) for x in encrypted_massage])
    result = re.search(pattern, decrypt_massage)
    if result:
        planet_name, population, attack_type, soldier_count = result.groups()
        if attack_type == "A":
            attacked_planets_count += 1
            attacked_planets_names.append(planet_name)
        if attack_type == "D":
            destroyed_planets_count += 1
            destroyed_planets_names.append(planet_name)
print(f"Attacked planets: {attacked_planets_count}")
for planet_a in sorted(attacked_planets_names):
    print(f"-> {planet_a}")
print(f"Destroyed planets: {destroyed_planets_count}")
for planet_d in sorted(destroyed_planets_names):
    print(f"-> {planet_d}")
