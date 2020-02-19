# Power System Analysis course software package
# Example of drawing the peak and valley load of a year
# Author: Chang Yanzhao(changyanzhao1997@163.com)
# date：2020-2-17
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
# Get the peak and valley load data of specific year
load = load_curve.get_day_minmax_load(load_date, load_data, year)

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

ax.plot(load[0],load[1],linewidth=1,label='peak load',color='k')
ax.plot(load[0],load[2],linewidth=1,linestyle='-',color='b',label='valley load')
ax.set_xlim([0, 366])
ax.set_ylim([0,5000])
ax.set_xticks([182,365])
ax.axis["x"].label.set_text("Time/day")
#ax.axis["x"].label.set_position((0,300))
ax.axis["y"].label.set_text("Load/MW")
ax.vlines(365, 0, load[1][364], colors='k',linewidth=1)
ax.set_title(str(year)+' Load Curve')
plt.legend()
plt.show()