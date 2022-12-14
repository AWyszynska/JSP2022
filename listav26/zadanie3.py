A = int(input("Podaj który wyraz ciągu chcesz obliczyć:  "))
def ciag(n):
        if (n == 1):
            print('1')
        if (n == 2):
            print('11')
        a = "11"
        print('1')
        print('11')
        for i in range(2, n):
            a += 'x' 
            long = len(a)
            hm = 1 
            b = ""
            for j in range(1 , long):
                if (a[j] != a[j - 1]):
                    b += str(hm) 
                    b += a[j - 1]
                    hm = 1
                else:
                    hm += 1
            a = b
            print(a)

ciag(A)