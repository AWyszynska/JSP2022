import numpy as np

A = np.array([[1, 2, 3, -2, -1], [3, 5, 5, -3, -9],
              [2, 3, 2, 0, -8],  [2, 6, 7, -5, 1],
              [1, 2, 6, -4, -10]])

B = np.array([6, 2 ,-5, 17, 12])

wynik = np.linalg.solve(A,B)

print("x: ",wynik[0])
print("z: ",wynik[1])
print("y: ",wynik[2])
print("t: ",wynik[3])
print("u: ",wynik[4])
