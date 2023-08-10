a = "aviel 'buskila'"
b = 'aviel buskila'
c = 'aviel \"buskila\"'
d = "devops experts"
h = {"fname": "dan", "lname": "segal",
     "age": 25, "is_married": False,
     "hobbies": ["coding", "gaming", "reading"]}
print(b + " from " + d)
e = f"his name is{h['fname']} {h['lname']} and his hobbies are {h['hobbies']}"
print(e)
g = "%s  %s" % (b, d)
print(g)

i = ("dan", "segal", 33, True)

# join