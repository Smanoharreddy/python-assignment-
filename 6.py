s1 = input()
s1 = list(s1)
j = len(s1)-1
only_alpha = []
for i in range(len(s1)//2):
    if s1[i].isalnum():
        if s1[j].isalnum():
            temp = s1[i]
            s1[i] = s1[j]
            s1[j] = temp
            j-=1
        else:
            while not s1[j].isalnum():
                j-=1
            temp = s1[i]
            s1[i] = s1[j]
            s1[j] = temp
            j -=1
s1 = "".join(s1)
print(s1)
