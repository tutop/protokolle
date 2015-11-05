import matplotlib.pyplot as plt
import numpy as np
xdata = np.genfromtxt('GeschwindigkeitWagen.txt',unpack=True)
ySchwdata=np.genfromtxt('Schwebung_delta_nü.txt',usecols=(0),unpack=True)
ydata=np.genfromtxt('delta_nü_hin_zurück.txt',usecols=(0),unpack=True)

x=np.linspace(0,100)
#ylin=0,9933333*x-0.16
plt.plot(x,ydata,'rx')
plt.xlabel('$v in m/s$')
plt.ylabel('$delta nü$')
plt.plot(x,0.9933333*x-0.16)

plt.tight_layout()
plt.savefig('loesung.pdf')
