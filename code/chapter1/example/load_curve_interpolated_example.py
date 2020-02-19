# Power System Analysis course software package
# Example of drawing the interpolated load of a day
# Author: Chang Yanzhao(changyanzhao1997@163.com)
# date：2020-2-19
# License: GPL-v3

import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import sys
import numpy as np
sys.path.append('../code/')
import load_curve

# Data preparation
load_date,load_data = load_curve.get_all_load_data('..\data\load_data.csv') 
year = 2017
month = 1
day = 1 
# Get the interpolated load data of specific day
load = load_curve.interpolate_load_of_day(load_date, load_data, year, month,day)

# Some settings of drawing
fig = plt.figure(1)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("left")

ax.plot(load[0,:], load[1,:], linewidth = 1,color='k')
a = np.argmin(load[1,:])
b = np.argmax(load[1,:])
ax.set_xlim([0, 25])
ax.set_ylim([0,5000])
ax.axis["x"].label.set_text("Time/hour")
ax.axis["y"].label.set_text("Load/MW")
ax.set_xticks(np.arange(0, 25, 2))
ax.vlines(load[0,a], 0, load[1,a], colors='k',linewidth = 1)
ax.vlines(load[0,b], 0, load[1,b], colors='k',linewidth = 1)
ax.text(load[0,a]+0.5,0.5*load[1,a],'$P_{min}$')
ax.text(load[0,b]+0.5,0.5*load[1,b],'$P_{max}$')
ax.set_title(str(year)+'/'+str(month)+'/'+str(day)+' Interpolated Load Curve')
plt.show()