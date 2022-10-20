n = int(input())
r = n % 2
if r!=0:
    print("Weird")
else:
    if n>=2 and n<=9:
        print("Not Weird")
    elif n>=10 and n<=22:
        print("Weird")
    elif n>22:
        print("Not Weird")
