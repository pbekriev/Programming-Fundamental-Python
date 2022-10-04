roll_1 = input().split()
roll_2 = input().split()
roll_3 = input().split()
if (roll_1[0] == "1" and roll_1[1] == "1" and roll_1[2] == "1") or \
        (roll_2[0] == "1" and roll_2[1] == "1" and roll_2[2] == "1") or \
        (roll_3[0] == "1" and roll_3[1] == "1" and roll_3[2] == "1") or \
        (roll_1[0] == "1" and roll_2[0] == "1" and roll_3[0] == "1") or \
        (roll_1[1] == "1" and roll_2[1] == "1" and roll_3[1] == "1") or \
        (roll_1[2] == "1" and roll_2[2] == "1" and roll_3[2] == "1") or \
        (roll_1[0] == "1" and roll_2[1] == "1" and roll_3[2] == "1") or \
        (roll_1[2] == "1" and roll_2[1] == "1" and roll_3[0] == "1"):
    print("First player won")
elif (roll_1[0] == "2" and roll_1[1] == "2" and roll_1[2] == "2") or \
        (roll_2[0] == "2" and roll_2[1] == "2" and roll_2[2] == "2") or \
        (roll_3[0] == "2" and roll_3[1] == "2" and roll_3[2] == "2") or \
        (roll_1[0] == "2" and roll_2[0] == "2" and roll_3[0] == "2") or \
        (roll_1[1] == "2" and roll_2[1] == "2" and roll_3[1] == "2") or \
        (roll_1[2] == "2" and roll_2[2] == "2" and roll_3[2] == "2") or \
        (roll_1[0] == "2" and roll_2[1] == "2" and roll_3[2] == "2") or \
        (roll_1[2] == "2" and roll_2[1] == "2" and roll_3[0] == "2"):
    print("Second player won")
else:
    print("Draw!")
