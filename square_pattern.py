for i in range(0,8):
    for j in range(0,6):
        if ((i == 0) or (i == 7)):
            print('=====', end='')
        if(i>=1 and i<7):
            if((j == 0)or (j == 5)):
                print('|| \t\t\t',end='')
            else:
                print(' ',end = '')
    print()
