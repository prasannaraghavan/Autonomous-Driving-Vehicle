import numpy as np
import matplotlib.pyplot as plt
# To create an array of the data values
f=open('imudata.txt',"r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(int(x.split(' ')[4]))
f.close()
n=len(result)
# Function to calculate the moving average 
def mov_avg(ivl):
    ivl_ma = []
    i=0
    while i<n-ivl+1:
        ivl_ma.append(sum(result[i:i+ivl])/ivl)
        i=i+1
    return ivl_ma
# 2- moving average
two_ma = mov_avg(2)
two_mean = np.full(len(result),np.mean(two_ma))
two_std = np.full(len(result),np.std(two_ma))
# 4- moving average    
four_ma= mov_avg(4)
four_mean = np.full(len(result),np.mean(four_ma))
four_std = np.full(len(result),np.std(four_ma))    
# 8- moving average
eight_ma = mov_avg(8)
eight_mean = np.full(len(result),np.mean(eight_ma))
eight_std = np.full(len(result),np.std(eight_ma))
# 16- moving average
sixt_ma = mov_avg(16)
sixt_mean = np.full(len(result),np.mean(sixt_ma))
sixt_std = np.full(len(result),np.std(sixt_ma))
# 64- moving average
sifo_ma = mov_avg(64)   
sifo_mean = np.full(len(result),np.mean(sifo_ma))
sifo_std = np.full(len(result),np.std(sifo_ma))
# 128- moving average
onei_ma = mov_avg(128)
onei_mean = np.full(len(result),np.mean(onei_ma))
onei_std = np.full(len(result),np.std(onei_ma))    
# Function for creating plots for moving averages
def movplot(name,ma,mean,std):
    plt.plot(result,label = "raw data", linestyle = '-')
    plt.plot(ma,label = name, linestyle = '-')
    plt.plot(mean,label = 'mean = %.5f'%mean[1],linestyle = '-')
    plt.plot(std,label = 'std = %.5f'%std[1],linestyle = '-')
    plt.ylabel("Accelerometer Amplitude")
    plt.xlabel("Frequency")
    plt.title(name)
    plt.legend()
    plt.show()
# 2- moving average and raw data
movplot("2 - moving averages",two_ma,two_mean,two_std)
# 4- moving average and raw data
movplot("4 - moving averages",four_ma,four_mean,four_std)
# 8- moving average and raw data
movplot("8 - moving averages",eight_ma,eight_mean,eight_std)
# 16- moving average and raw data
movplot("16 - moving averages",sixt_ma,sixt_mean,sixt_std)
# 64- moving average and raw data
movplot("64 - moving averages",sifo_ma,sifo_mean,sifo_std)
# 128- moving average and raw data
movplot("128 - moving averages",onei_ma,onei_mean,onei_std)

