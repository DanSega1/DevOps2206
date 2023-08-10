# 7 Boom is a game where you count from 1 up.
# However, if the number is divisible with 7 or contains the digit 7, you say "Boom" instead.

for i in range(1, 101):
    if i % 7 == 0 or str(i).find("7") > -1:
        print("Boom")
    else:
        print(i)

