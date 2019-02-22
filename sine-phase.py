import matplotlib.pyplot as plt
import numpy as m
F=5
t=m.arange(0,1,0.01)
v=m.sin(2*m.pi*F*t)
plt.subplot(211)
plt.plot(t,v)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
p=m.sin((2*m.pi*F*t)+90)
plt.subplot(212)
plt.plot(t,p)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
plt.show()
