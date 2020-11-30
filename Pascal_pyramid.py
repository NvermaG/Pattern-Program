import math as mp
for i in range(1,6):
    for k in range(5,i,-1):
        print(' ',end = '')
    for j in range(1,i+1):
        ans = mp.factorial(i-1) // (mp.factorial((i-1) - (j-1)) * mp.factorial(j-1))
        print(ans,end=' ')
    print()
