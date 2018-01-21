import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s = np.cos(x),np.sin(x)
plt.figure(1)
plt.plot(x,c,color='080',linewidth=1.0,linestyle="-",label='COS',alpha=0.5)
plt.plot(x,s)
plt.title('cos & sin')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
plt.show()