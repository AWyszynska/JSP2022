liczby = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def LiczbyRzymskie(x):
    sum = 0
    for i in range(len(x) - 1):
        left = x[i]
        right = x[i + 1]
        if liczby[left] < liczby[right]:
            sum -= liczby[left]
        else:
            sum += liczby[left]
    sum += liczby[x[-1]]
    return sum
a = input()
print(LiczbyRzymskie(a))