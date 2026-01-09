R, X = map(int, input().split(" "))
if (X == 1 and (R >= 1600 and R <= 2999)):
    print("Yes")
elif (X == 2 and (R >= 1200 and R <= 2399)):
    print("Yes")
else:
    print("No")