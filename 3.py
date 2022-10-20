l = []
for i in range(4):
    j = str(i+1)
    city = int(input("Enter the distance from city"+j+" :"))
    l.append(city)
m = max(l)
print("city"+str((l.index(m))+1)+" is the farthest")
