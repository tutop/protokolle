import matplotlib.pyplot as plt
import numpy as np

d=0.5*0.02935
T=np.array([12.78/5.,14.25/5.,16.20/5.,18.43/5.,20.47/5.,23.18/5.,25.58/5.,28.32/5.,30.83/5.,33.27/5.])
a=np.array([0.01*(3.+d),0.01*(4.71+d),0.01*(6.84+d),0.01*(8.8+d),0.01*(10.92+d),0.01*(12.91+d),0.01*(14.9+d),0.01*(17.1+d),0.01*(19.+d),0.01*(21.65+d)])

x=np.linspace(0,0.06,100)
plt.plot(a*a,T*T,'rx')
plt.plot(x,838.192*x+6.759)
plt.xlabel(r'$a^2$')
plt.ylabel(r'$T^2$')

plt.show()
