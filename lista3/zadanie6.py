k = int(input())
def b():
    for i in range(1,11):
        for j in range(1,k+1):
            print('{:^5}'.format(i*j)," ",end = ' ')
        print()
b()
