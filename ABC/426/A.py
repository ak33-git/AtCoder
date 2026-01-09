X, Y = map(str,input().split())

if X == "Lynx":
    print("Yes")
elif X == "Serval":
    if Y != "Lynx":
        print("Yes")
    else:
        print("No")
else:
    if Y == "Ocelot":
        print("Yes")
    else:
        print("No")