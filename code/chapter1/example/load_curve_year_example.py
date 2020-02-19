# Power System Analysis course software package
# Example of drawing annual load curve of active power
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
# Get the load data of specific year
load = load_curve.get_load_of_year(load_date, load_data, year)

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

for i in range(len(load[1:,:])-1):
    ax.plot(load[0,:],load[i+1,:],linewidth = 1,color = 'k')  
ax.set_xlim([0, 25])
ax.set_ylim([0,5000])
ax.axis["x"].label.set_text("Time/hour")
ax.axis["y"].label.set_text("Load/MW")
ax.set_xticks(np.arange(0, 25, 2))
ax.set_title(str(year)+' Load Curve')
plt.show()