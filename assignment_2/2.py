"""
Result for 2)
Although truth values was asked for, here the output is converted to 0, 1 code
"""

for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            left_side = (not a and b) and not c
            right_side = (a or c) and not (b or c)
            # The int is used to convert all boolean values back to 0, 1 code
            print(a, b, c, ':', int(left_side), 'vs.', int(right_side))
