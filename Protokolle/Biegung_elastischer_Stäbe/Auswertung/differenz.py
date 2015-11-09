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
np.savetxt('diffrecht.txt', np.column_stack([rdiff*1000]), header='diff in m')


q1,q2,ortz=np.genfromtxt('messungzylinder.txt',unpack=True)
ortz*=0.001
zdiff=(q1-q2)*0.01/1000
print(zdiff)
np.savetxt('diffzyl.txt', np.column_stack([zdiff*1000]), header='diff in m')


e1,e2,ortzweis=np.genfromtxt('rechteckzweiseitig.txt',unpack=True)
a=range(0,25)
b=range(26,50)
uhr1ortzweis=np.array(ortzweis[a])
uhr2ortzweis=np.array(ortzweis[b])

uhr1ortzweis*=0.001
uhr2ortzweis*=0.001

zweidiff1=(e1[a]-e2[a])*0.01/1000
zweidiff2=(e1[b]-e2[b])*0.01/1000

np.savetxt('diffzwei1.txt', np.column_stack([zweidiff1]), header='diff in m')
np.savetxt('diffzwei2.txt', np.column_stack([zweidiff2]), header='diff in m')

def g(x,L):
    return L*x**2-x**3/3
np.savetxt('diffrechtg(x).txt', np.column_stack([g(ortr,LeingespR)]), header='g(x)in m^3')
np.savetxt('diffzylg(x).txt', np.column_stack([g(ortz,LeingespZ)]), header='g(x)')
# np.savetxt('diffzwei1g(x).txt', np.column_stack([g(uhr1ortzweis,LzweieingespR)]), header='g(x)')
# np.savetxt('diffzwei2g(x).txt', np.column_stack([g(uhr2ortzweis,LzweieingespR)]), header='g(x)')

def f(x,L):
    return 3*L**2*x-4*x**3
# np.savetxt('diffrechtf(x).txt', np.column_stack([f(ortr,LeingespR)]), header='g(x)in m^3')
# np.savetxt('diffzylf(x).txt', np.column_stack([f(ortz,LeingespZ)]), header='g(x)')
np.savetxt('diffzwei2f(x).txt', np.column_stack([f(uhr2ortzweis,LzweieingespR)]), header='g(x)')
# np.savetxt('diffzwei2f(x).txt', np.column_stack([f(uhr2ortzweis,LzweieingespR/2)]), header='g(x)')

def h(x,L):
    return 4*x**3-12*L*x**2+9*L**2*x-L**3
np.savetxt('diffzwei1f(x).txt', np.column_stack([h(uhr1ortzweis,LzweieingespR)]), header='g(x)')



# fW1,fW1err,fW2,fW2err=linregress(f(ortr,LeingespR),rdiff)
# fQ1,fQ1err,fQ2,fQ2err=linregress(f(ortz,LeingespZ),zdiff)
hE1,hE1err,hE2,hE2err=linregress(h(uhr1ortzweis,LzweieingespR),zweidiff1)
fE1_,fE1err_,fE2_,fE2err_=linregress(f(uhr2ortzweis,LzweieingespR),zweidiff2)


W1,W1err,W2,W2err=linregress(g(ortr,LeingespR),rdiff)
Q1,Q1err,Q2,Q2err=linregress(g(ortz,LeingespZ),zdiff)
# E1,E1err,E2,E2err=linregress(f(uhr1ortzweis,LzweieingespR),zweidiff1)
# E1_,E1err_,E2_,E2err_=linregress(h(uhr2ortzweis,LzweieingespR),zweidiff2)

print('R=',W1)
print('Z=',Q1)
print('weiterweg hE1=',hE1)
print('näheran null fE1=',fE1_)





x = np.linspace(-0.1,0.2, 1000)

plt.plot(g(ortr,LeingespR),rdiff, 'kx', label='Rechteck')
plt.plot(x,W2+x*W1,'k-')
plt.xlim(0,0.1)
plt.xlabel(r'$g(x) \ / \ m^3$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.close()

plt.plot(g(ortz,LeingespZ),zdiff,'kx',label='Zylinder')
plt.plot(x,Q2+x*Q1,'k-')
plt.xlim(0,0.1)
plt.xlabel(r'$g(x) \ / \ m^3$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.close()

plt.plot(f(uhr1ortzweis,LzweieingespR),zweidiff1,'kx',label='zweiseitig eingespanntes Rechteck')
plt.plot(x,hE2+x*hE1,'k-')
# plt.xlim(0,0.1)
plt.xlabel(r'$f(x) \ / \ m^3$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot3.pdf')
plt.close()

plt.plot(h(uhr2ortzweis,LzweieingespR),zweidiff2,'kx',label='zweiseitig eingespanntes Rechteck')
plt.plot(x,fE2_+x*fE1_,'k-')
# plt.xlim(0,0.1)
plt.xlabel(r'$h(x) \ / \ m^3$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot4.pdf')
plt.close()





"""
plt.plot(f(ortr,LeingespR),rdiff, 'bx', label='Rechteck')
plt.plot(x,fW2+x*fW1,'b-')
plt.xlim(0,0.1)
plt.xlabel(r'$g(x) \ / \ m^3$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('fplot1.pdf')
plt.close()

plt.plot(f(ortz,LeingespZ),zdiff, 'bx', label='Rechteck')
plt.plot(x,fQ2+x*fQ1,'b-')
plt.xlim(0,0.1)
plt.xlabel(r'$g(x) \ / \ m^3$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('fplot2.pdf')
plt.close()

plt.plot(f(uhr1ortzweis,LzweieingespR),zweidiff1, 'bx', label='Rechteck')
plt.plot(x,fE2+x*fE1,'b-')
plt.xlim(0,0.1)
plt.xlabel(r'$g(x) \ / \ m^3$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('fplot3.pdf')
plt.close()

plt.plot(f(uhr2ortzweis,LzweieingespR),zweidiff2, 'bx', label='Rechteck')
plt.plot(x,fE2_+x*fE1_,'b-')
plt.xlim(0,0.1)
plt.xlabel(r'$g(x) \ / \ m^3$')
plt.ylabel(r'$D \ / \ m$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('fplot4.pdf')
plt.close()
"""
