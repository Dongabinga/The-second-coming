import numpy as np
import matplotlib.pyplot as plt
from numpy import random



norm = np.random.normal(size=(2,200))
x=norm[0,]
y=norm[1,]
uni = np.random.uniform(size=(2,200))
log = np.random.lognormal(size=(2,200))
epsilon = 0.1
mask = np.abs(x**2+1/3*y**2) < epsilon #Маска для распределения Капчинского
plt.subplot(3, 1, 1)
plt.scatter(norm[0, ], norm[1, ])
plt.scatter(x[mask], y[mask], color='orange', s=40, marker='o')
plt.subplot(3, 1, 2)
plt.scatter(uni[0, ], uni[1, ])
plt.subplot(3, 1, 3)
plt.scatter(log[0, ], log[1, ])
plt.show