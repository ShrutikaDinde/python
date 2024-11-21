import matplotlib.pyplot as plt
import numpy as np
#data to display on plot
x=[1,2,3,4,5,6,7,4]
plt.hist(x,bins=[1,2,3,4,5,6,7])
plt.title("Histogram")
plt.legend(["Bar"])
plt.show()