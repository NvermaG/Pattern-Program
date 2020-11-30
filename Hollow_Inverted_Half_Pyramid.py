for i in range(0,6):
    for j in range(0,6-i):
        if(i == 1):
            if(j == 1 or j == 2 or j == 3):
                print('  ',end = '')
            else:
                print('* ',end = '')
        elif(i == 2):
            if(j == 1 or j == 2):
                print('  ',end = '')
            else:
                print('* ',end = '')
        elif(i == 3):
            if(j == 1):
                print('  ',end = '')
            else:
                print('* ',end = '')
        else:
            print('* ',end = '')
    print()
