import matplotlib.pyplot as plt
import numpy as np
x=[3,1,3,12,2,4,4]
y=[3,2,1,4,5,6,7]

plt.bar(x,y)
#Title
plt.title("Bar Graph")
#Adding legend
plt.legend(["Bar"])
plt.show()