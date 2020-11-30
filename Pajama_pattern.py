for i in range(0,7):
    for j in range(7,i,-1):
        print('* ',end='')
    for p in range(0,i):
        print('    ',end ='')
    for k in range(7,i,-1):
        print(' *',end='')
    print()
