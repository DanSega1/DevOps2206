isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
my_list = [1, 2, 3]
is_age_above_twentyfour = a == 24 or strOne == "One"
is_not_a = not (strThree != "A")
if isTrue and is_age_above_twentyfour and is_not_a:
    print("True and two")
elif is_age_above_twentyfour and b == 2.5:
    print("blop")
else:
    print("bla")

print("moshe")


if len(my_list) > 3:
    print("I have items")
else:
    print("I have no items")