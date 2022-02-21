n = int(input("Enter the number of balls : "))
a = []
p1 = 0
p2 = 0
bat = True
for x in range(n):
    c = int(input("Enter the runs in: "))
    a.append(c)
print("Scores : ", a)

for x in a:
    if bat:
        p1 = p1+x
    else:
        p2 = p2+x

    if x % 2 == 0:
        bat = bat

    else:
        bat = not bat


print("P1", p1)
print("P2", p2)
