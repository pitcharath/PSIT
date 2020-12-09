# importing the required module
import matplotlib.pyplot as plt

# line 1 points
x1 = [1,2]
y1 = [2,4]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")

# setting x and y axis range
plt.ylim(0,5)
plt.xlim(0,5)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('One line Graph')

plt.grid(True)
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()