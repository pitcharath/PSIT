from sympy import symbols, solve, sympify
eq = '2*x+4=0'
eq2 = eq.replace('x','0')
eq3 = eq2.replace('0','y')
#หา y จากสมการข้างบน

sympy_eq = sympify("Eq(" + eq.replace("=", ",") + ")")
sol = solve(sympy_eq)
#อันนี้หา x ได้แล้ว
sympy_eq2 = sympify("Eq(" + eq3.replace("=", ",") + ")")
sol2 = solve(sympy_eq2)
find_y = sol2[0]*(-1)
#หา y

box_x = [sol,0]
box_y = [0]
box_y.append(find_y)
print(find_y)
print(sol)

from matplotlib import pyplot as plt
x = [0]
y = []
y.append(find_y)
x.extend(sol)
y.append(0)
plt.plot(x,y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Graph')
plt.grid(True)
plt.show()
