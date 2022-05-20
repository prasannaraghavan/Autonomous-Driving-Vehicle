import matplotlib.pyplot as plt
import numpy as np

percent=70.0
TimePeriod=1.0
Cycles=2
dt=0.01 

t= np.arange(0,Cycles*TimePeriod,dt); 
pwm= t%TimePeriod<TimePeriod*percent/100 

fig, axs = plt.subplots(2)
fig.suptitle('Reverse Configuration')
axs[0].plot(t,pwm*3,linewidth=4.0)
axs[0].set_ylabel('V(A)')
plt.ylim((0.0,3.0))
axs[1].plot(t,pwm*0,linewidth=7.0)
axs[1].set_ylabel('V(B)')
axs[1].set_xlabel('time(msec)')
#plt.gca().invert_yaxis()

plt.show()
