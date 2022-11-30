liczby = {
    '1' : 'jeden',
    '2': 'dwa',
    '3' : 'trzy',
    '4' : 'cztery',
    '5' : 'piec',
    '6' : 'szesc',
    '7' : 'siedem',
    '8' : 'osiem',
    '9' : 'dziewiec',
    '10' : 'dziesiec',
    '11' : 'jedenascie',
    '12' : 'dwanascie',
    '13' : 'trzynascie',
    '14' : 'czternascie',
    '15' : 'pietnascie',
    '16' : 'szesnascie',
    '17' : 'siedemnascie',
    '18' : 'osiemnascie',
    '19' : 'dziewietnascie',
    '20' : 'dwadziesia',
    '30' : 'trzydziesci',
    '40' : 'czterdziesci',
    '100' : 'sto',
    '200' : 'dwiescie',
    '300' : 'trzysta',
    '400' : 'czterysta',
    '1000' : 'tysiac',
    }
a = input()
l = len(a)

def funkcja(x):
    z = x[0]
    if l == 2 and x[1] in ["2","3","7","8"]:
        for b in liczby.items():
            if x[0] == "1" and x[1] in liczby.keys():
                y = x[1]
                return(liczby[y]+"nascie")
    if x[0] in ["5","6","7","8","9"] and x[1] == "0" and l == 2:
        for b in liczby.items():
            if x[0] in liczby.keys():
                z = x[0]
                return(liczby[z]+"dziesiat")
    else:
        for b in liczby.items():
            if x in liczby.keys():
                return(liczby[x])

    if l == 3 and x[0] in ["5","6","7","8","9"] and x[1] == "0":
        for b in liczby.items():
            if x[0] in liczby.keys():
                z = x[0]
                return(liczby[z]+"set")

if l == 2 and a[0] in ["2","3","4","5","6","7","8","9"] and a[1] in ["1","2","3","4","5","6","7","8","9"]:#20-99
    o = a[0]+"0"
    h = a[1]
    print(funkcja(o),liczby[h])
if l==3 and a[1]=="0" and a[0] in ["1","2","3","4","5","6","7","8","9"] and a[2] in ["1","2","3","4","5","6","7","8","9"] and a[2] != "0" : #101
    i = a[2]
    p = a[0]+"00"
    print(funkcja(p),liczby[i])
if l == 3 and a[0] in ["1","2","3","4","5","6","7","8","9"] and a[1] in ["2","3","4","5","6","7","8","9"] and a[2] in ["1","2","3","4","5","6","7","8","9"] and a[1] != "0" and a[2] != "0":
    p = a[0]+"00"
    m = a[1]+"0"
    i = a[2]
    print(funkcja(p),funkcja(m),liczby[i])
if l == 3 and a[2] !="0" and a[1] == "0":
    p = a[0]+"00"
    n = a[1:3]
    print(funkcja(p),funkcja(n))
if l == 3 and a[1] == "1":
    p = a[0]+"00"
    n = a[1:3]
    print(funkcja(p),funkcja(n))
if l == 4 and a[1]=="0" and a[2] == "0" and a[3] != "0":
    r = a[3]
    print(liczby["1000"],liczby[r])
if l == 4 and a[1] =="0" and a[2] in ["2","3","4","5","6","7","8","9"] and a[3] in ["1","2","3","4","5","6","7","8","9"] and a[3] != "0":
    r = a[2]+"0"
    q = a[3]
    print(liczby["1000"],funkcja(r),liczby[q])
if l == 4 and a[1] =="0" and a[2] in ["2","3","4","5","6","7","8","9"] and a[3] == "0":
    A = a[2:4]
    print(liczby["1000"],funkcja(A))
if l == 4 and a[1] =="0" and a[3] in ["1","2","3","4","5","6","7","8","9"] and a[2] == "1":
    A = a[2:4]
    print(liczby["1000"],funkcja(A))
if l == 4 and a[1] == "0" and a[2] in ["2","3","4","5","6","7","8","9"] and a[3] in ["1","2","3","4","5","6","7","8","9"]:
    r = a[2]+"0"
    q = a[3]
    print(liczby["1000"],funkcja(r),liczby[q])
if l == 4 and a[1] in ["1","2","3","4","5","6","7","8","9"] and a[2] in ["2","3","4","5","6","7","8","9"] and a[3] in ["1","2","3","4","5","6","7","8","9"]:
    r = a[2]+"0"
    q = a[3]
    B = a[1]+"00"
    print(liczby["1000"],funkcja(B),funkcja(r),liczby[q])
if l == 4 and a[1] in ["1","2","3","4","5","6","7","8","9"] and a[2] =="1" and a[3] in ["1","2","3","4","5","6","7","8","9"]:
    A = a[2:4]
    B = a[1]+"00"
    print(liczby["1000"],funkcja(B),funkcja(A))
if l == 4 and a[1] in ["1","2","3","4","5","6","7","8","9"] and a[2] in ["2","3","4","5","6","7","8","9"] and a[3] =="0":
    B = a[1]+"00"
    A = a[2:4]
    print(liczby["1000"],funkcja(B),funkcja(A))
else:
    print(funkcja(a))

print(a[1:3])