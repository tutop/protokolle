import numpy as np
import matplotlib.pyplot as plt
from linregress import linregress

LeingespR=.535
LeingespZ=.525
LzweieingespR=.553

w1,w2,ortr=np.genfromtxt('messungrechteck.txt',unpack=True)
ortr*=0.001
rdiff=(w1-w2)*0.01/1000
print(rdiff)

q1,q2,ortz=np.genfromtxt('messungzylinder.txt',unpack=True)
ortz*=0.001
zdiff=(q1-q2)*0.01/1000
print(zdiff)

e1,e2,ortzweis=np.genfromtxt('rechteckzweiseitig.txt',unpack=True)
a=range(0,25)
b=range(26,50)
uhr1ortzweis=np.array(ortzweis[a])
uhr2ortzweis=np.array(ortzweis[b])

uhr1ortzweis*=0.001
uhr2ortzweis*=0.001
print(uhr1ortzweis)
print(uhr2ortzweis)

zweidiff1=(e1[a]-e2[a])*0.01/1000
zweidiff2=(e1[b]-e2[b])*0.01/1000
print(zweidiff2)

def g(x,L):
    return L*x**2-x**3/3

W1,W1err,W2,W2err=linregress(g(ortr,LeingespR),rdiff)
Q1,Q1err,Q2,Q2err=linregress(g(ortz,LeingespZ),zdiff)
E1,E1err,E2,E2err=linregress(g(uhr1ortzweis,LzweieingespR),zweidiff1)
E1_,E1err_,E2_,E2err_=linregress(g(uhr2ortzweis,LzweieingespR),zweidiff2)


x = np.linspace(0,0.1, 1000)

"""plt.plot(g(ortr,LeingespR),rdiff, 'bx', label='Rechteck')
plt.plot(x,W2+x*W1,'b-')
plt.plot(g(ortz,LeingespZ),zdiff,'rx',label='Zylinder')
plt.plot(x,Q2+x*Q1,'r-')
"""

plt.plot(g(uhr1ortzweis,LzweieingespR),zweidiff1,'gx',label='zweiseitig eingespanntes Rechteck')
plt.plot(x,E2+x*E1,'g-')
plt.plot(g(uhr2ortzweis,LzweieingespR),zweidiff2,'gx',label='zweiseitig eingespanntes Rechteck')
plt.plot(x,E2_+x*E1_,'g-')


plt.xlim(0,0.1)
plt.xlabel(r'$g(x) \ / \ m$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('loesung.pdf')
