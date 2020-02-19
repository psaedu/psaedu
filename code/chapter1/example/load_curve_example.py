import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import sys
import numpy as np
sys.path.append('../code/')
import load_curve

load_date,load_data = load_curve.get_all_load_data('..\data\load_data.csv') 
year = 2017
month = 1
day = 1 

#Some settings of drawing
fig = plt.figure(1)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,1000)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"].label.set_text("Load/MW")
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("left")

# draw load curve of specific day

load = load_curve.get_load_of_day(load_date, load_data, year, month, day)
plt.plot(load[0,:], load[1,:], linewidth = 1,color='k')
a = np.argmin(load[1,:])
b = np.argmax(load[1,:])
plt.xlim((0, 24))
plt.ylim((1000, 5000))
ax.axis["x"].label.set_text("Time/hour")
plt.xticks(np.arange(0, 25, 2))
plt.vlines(load[0,a], 1000, load[1,a], colors='k',label = '$P_min$')
plt.title(str(year)+'/'+str(month)+'/'+str(day)+' Load Curve')

#draw load curve of specific month
'''
load = load_curve.get_load_of_month(load_date, load_data, year, month)
for i in range(len(load[1:,:])-1):
    plt.plot(load[0,:],load[i+1,:],linewidth = 1)
plt.xlim((0, 24))
plt.ylim((1000, 5000))
plt.xticks(np.arange(0, 25, 2))
ax.axis["x"].label.set_text("Time/hour")
plt.title(str(year)+'/'+str(month)+' Load Curve')
'''
#draw load curve of specific year
'''
load = load_curve.get_load_of_year(load_date, load_data, year)
for i in range(len(load[1:,:])-1):
    plt.plot(load[0,:],load[i+1,:],linewidth = 0.5)
plt.xlim((0, 24))
plt.ylim((1000, 5000))
plt.xticks(np.arange(0, 25, 2))
ax.axis["x"].label.set_text("Time/hour")
plt.title(str(year)+' Load Curve')
'''
# draw daily peak & valley load of year
'''
load = load_curve.get_day_minmax_load(load_date, load_data, year)
plt.plot(load[0],load[1],linewidth=1,label='peak load')
plt.plot(load[0],load[2],linewidth=1,label='valley load')
plt.xlim((0, 370))
plt.ylim((1000, 5000))
ax.axis["x"].label.set_text("Time/hour")
plt.xticks(np.arange(0, 370, 40))
plt.title('Year '+str(year)+' Daily Peak & Valley Load Curve')
plt.legend()
'''
# draw distribution of load of year
'''
distribution = load_curve.get_load_distribution(load_date, load_data, year)
plt.plot(distribution[:,1],distribution[:,0],linewidth=2)
ax.axis["x"].label.set_text("Time/hour")
plt.title('Year '+str(year)+' Accumulated Load Curve')
plt.xlim((0, 8000))
plt.ylim((1000, 5000))
'''
# draw interpolated load of day
'''
load = load_curve.interpolate_load_of_day(load_date, load_data, year, month, day)
plt.plot(load[0,:], load[1,:], linewidth = 1)
plt.xlim((0, 24))
plt.ylim((1000, 5000))
plt.xticks(np.arange(0, 25, 2))
ax.axis["x"].label.set_text("Time/hour")
plt.title(str(year)+'/'+str(month)+'/'+str(day)+' Interpolated Load Curve')
'''
plt.show()
