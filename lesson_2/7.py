prefix = "my name is "
names = ["ofek", "idan", "eden", "aviran", "avidan", "daniel", "or"]
for name in names:
    print(f"looking for or...current name is: {name}")
    if name == "or":
        print("found or")
    else:
        print("did not find or")
    print("did not find or yet")
else:
    print("did not find or at all")

# for i in range(len(names)):
#     names[i] = names[i] + "z"
#     print(f"{prefix}{names[i]}")


print(names)

result = []
for name in names:
    if name.find("dan") > -1:
        result.append(name)

my_other_result = [name + "z" for name in names if name.find("dan") > -1]
print(my_other_result)
print(my_other_result)

name_with_z_containing_dan = [name + "z" for name in names if name.find("dan") > -1]
for name in name_with_z_containing_dan:
    print(name_with_z_containing_dan)



# age = int(input("Enter your age: "))
# if age < 50:
#     print("you are  still ok")
#     age = age + 5
# else:
#     print("you are too old")


for i in range(len(names)):
    if names[i] == 'or':
        names[i] = names[i] + "z"
print(names)