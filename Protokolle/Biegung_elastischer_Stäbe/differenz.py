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
ortzweis*=0.001
zweidiff=(e1-e2)*0.01/1000
print(zweidiff)

def g(x,L):
    return L*x**2-x**3/3

W1,W1err,W2,W2err=linregress(g(ortr,LeingespR),rdiff)
Q1,Q1err,Q2,Q2err=linregress(g(ortz,LeingespZ),zdiff)
E1,E1err,E2,E2err=linregress(g(ortzweis,LzweieingespR),zweidiff)

x = np.linspace(0,0.1, 1000)
plt.plot(g(ortr,LeingespR),rdiff, 'bx', label='Rechteck')
plt.plot(x,W2+x*W1,'b-')
plt.plot(g(ortz,LeingespZ),zdiff,'rx',label='Zylinder')
plt.plot(x,Q2+x*Q1,'r-')
# plt.plot(g(ortzweis,LzweieingespR),zweidiff,'gx',label='zweiseitig eingespanntes Rechteck')
# plt.plot(x,E2+x*E1,'g-')
plt.xlabel(r'$g(x) \ / \ m$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('loesung.pdf')
