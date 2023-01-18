import numpy as n
import matplotlib.pyplot as plt


v0 = float(input("Podaj V0: "))
katpierwszy = float(input("Podaj kat: ")) * n.pi / 180
kat = katpierwszy* n.pi / 180
time = 2 * v0 * n.sin(kat) / 9.81
hmax = v0**2 * n.sin(kat)**2 / (2 * 9.81)
zasieg = 2 * v0**2 * n.sin(kat)**2 / 9.81

punkty = 100          
t = n.linspace(0, time, punkty)
vx = [v0 * n.cos(kat) for i in range(punkty)]
vy = v0 * n.sin(kat) - 9.81 * t
x = vx * t
y = v0 * t * n.sin(kat) - 9.81 * t * t / 2

print("Maksymalna wysokość: ",hmax)
print("Zasieg rzutu: ",zasieg)
print("Czas lotu: ",time)


plt.subplot(131, title="predkosc chwilowa")
plt.plot(t, vx, t, vy)
plt.subplot(132, title="polozenie funkcji w czasie")
plt.plot(t, x, t, y)
plt.subplot(133, title="tor ruchu w rzucie ukosnum ")
plt.plot(x, y)

plt.show()

