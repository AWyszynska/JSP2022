a = int(input())
def trojkat(n):
   for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print('{0:1}'.format(C), ' ', sep='', end='')
         C = C * (i - j) // j
      print()

print(trojkat(a)) 