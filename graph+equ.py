"""ตัวแปรเดียว"""
from sympy import symbols, solve
x = symbols('x')
box_y = [0]
eq1 = 2*x + 11
cal = eq1.replace(x,0)
box_y.append(cal)
sol = solve(eq1)

print(box_y)
print(sol)

from matplotlib import pyplot as plt
x = [0]
y = []
y.append(cal)
x.extend(sol)
y.append(0)
plt.plot(x,y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Graph')
plt.grid(True)
plt.show()
