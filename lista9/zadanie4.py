import numpy
import matplotlib.pyplot as plt

val = 0
nazwy = ('Python', 'C', 'C++', 'Java', 'C#', 'Visual Basic', 'JavaScript', 'SQL', 'Assembly language', 'PHP')
yv = [16.36, 16.26, 12.91, 12.21, 5.73, 4.64, 2.87, 2.5, 1.60, 1.39]
A = numpy.arange(len(yv))
plt.figure(figsize=(10, 5))
plt.bar(A, yv, color='m')
plt.xticks(A, nazwy)
for i in yv:
    plt.text(val - 0.25, i + 0.1, str(i)+'%')
    val+=1
plt.ylabel('[%]', color='c' , fontsize=12)
plt.title('Popularnosc roznych jezykow programowania w 2023', color='b', fontsize=18,)


plt.show();
