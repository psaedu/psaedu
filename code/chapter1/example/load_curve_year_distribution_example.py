# Power System Analysis course software package
# Example of drawing load's distribution of year
# Author: Chang Yanzhao(changyanzhao1997@163.com)
# date：2020-2-17
# License: GPL-v3

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
distribution = load_curve.get_load_distribution(load_date, load_data, year)
#Some settings of drawing
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

ax.plot(distribution[:,0],distribution[:,1],linewidth=1,color='k')
ax.vlines(distribution[0,0], 0, distribution[0,1],colors='k',linewidth = 1)
ax.set_xticks([distribution[0,0]])
ax.set_xlim([0,9000])
ax.set_ylim([0,5000])
ax.axis["x"].label.set_text("Time/hour")
ax.axis["y"].label.set_text("Load/MW")
ax.set_title('Year '+str(year)+' Accumulated Load Curve')
plt.show()
