my_file = open("name.txt")
names = my_file.readlines()
print(names)
for name in names:
    print(f"hello {name}", end='')

my_file.close()

my_file2 = open("name.txt", "a+")

for i in range(3):
    my_file2.write(input("Enter your name: ") + "\n")

my_file2.seek(0)
names = my_file2.readlines()
print(names)
