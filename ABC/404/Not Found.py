#正解
S = str(list(input()))
al = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
"o","p","q","r","s","t","u","v","w","x","y","z"]


for i in range(len(S)):
  try:
    al.remove(S[i])
  except:
    pass



print(al[0])