# #1
import math


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line_longer = False
    second_line_longer = False
    if (abs(x4 - x3) >= abs(x2 - x1) or abs(y4 - y3) >= abs(y2 - y1)) and \
            (abs(x4 - y3) >= abs(x2 - y1) or abs(y4 - x3) >= abs(y2 - x1)):
        second_line_longer = True
    else:
        first_line_longer = True
    if first_line_longer:
        if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
        return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"
    else:
        if abs(x3) + abs(y3) <= abs(x4) + abs(y4):
            return f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"
        return f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})"


point_x1 = float(input())
point_y1 = float(input())
point_x2 = float(input())
point_y2 = float(input())
point_x3 = float(input())
point_y3 = float(input())
point_x4 = float(input())
point_y4 = float(input())
print(longer_line(point_x1, point_y1, point_x2, point_y2, point_x3, point_y3, point_x4, point_y4))

# #2
#
# from math import floor
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x3 = float(input())
# y3 = float(input())
# x4 = float(input())
# y4 = float(input())
#
# def distance(_x1, _y1, _x2, _y2):
#     return (_x2-_x1)**2 + (_y2-_y1)**2
#
# x1y1 = distance(x1, y1, 0, 0)
# x2y2 = distance(x2, y2, 0, 0)
# x3y3 = distance(x3, y3, 0, 0)
# x4y4 = distance(x4, y4, 0, 0)
#
# line_1 = x1y1 + x2y2
# line_2 = x3y3 + x4y4
#
# if line_1 >= line_2:
#     if x1y1 <= x2y2:
#         print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
#     else:
#         print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
# if line_1 < line_2:
#     if x3y3 <= x4y4:
#         print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
#     else:
#         print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')
