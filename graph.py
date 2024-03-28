import matplotlib.pyplot as plt
import numpy as np
 
## color code
# b: blue
# g: green
# r: red
# c: cyan
# m: magenta
# y: yellow
# k: black
# w: white
 
## marker style
# ================ ===============================
# character description
# ================ ===============================
# - solid line style
# -- dashed line style
# -. dash-dot line style
# : dotted line style
# . point marker
# , pixel marker
# o circle marker
# v triangle_down marker
# ^ triangle_up marker
# < triangle_left marker # > triangle_right marker
# 1 tri_down marker
# 2 tri_up marker
# 3 tri_left marker
# 4 tri_right marker
# s square marker
# p pentagon marker
# * star marker
# h hexagon1 marker
# H hexagon2 marker
# + plus marker
# x x marker
# D diamond marker
# d thin_diamond marker
# | vline marker
# _ hline marker
# ================ ===============================
 
## Drawing each lines
# plot first line graph
plt.errorbar(
[0, 2, 36], # X
[122.1 #/122.1*100
 ,22.7 #/122.1*100
 ,14.6 #/122.1*100
], # Y
# yerr=[54,12,41], # Y-errors
fmt="ko-", # format line like for plot()
linewidth=2, # width of plot line
elinewidth=0.5,# width of error bar line
ecolor='k', # color of error bar
capsize=3, # cap length for error bar
capthick=0.5 # cap thickness for error bar
)
# plot second line graph
plt.errorbar(
[0, 2 ,36], # X
[179 # /179*100
 ,76.85 # /179*100
 ,11.65 # /179*100
], # Y
# yerr=[134,124,21,9], # Y-errors
fmt="ko-", # format line like for plot()
linewidth=2, # width of plot line
elinewidth=0.5,# width of error bar line
ecolor='k', # color of error bar
capsize=3, # cap length for error bar
capthick=0.5 # cap thickness for error bar
)
# plot Third line graph
plt.errorbar(
[0 ,2 ,36], # X
[10.75 # /10.75*100
 , 3.605 #/10.75*100
 , 4.05 #/10.75*100
 ], # Y
# yerr=[44,34,21,13], # Y-errors
fmt="ko-", # format line like for plot()
linewidth=2, # width of plot line
elinewidth=0.5,# width of error bar line
ecolor='k', # color of error bar
capsize=3, # cap length for error bar
capthick=0.5 # cap thickness for error bar
)

plt.errorbar(
[0 ,2, 36], # X
[44.3 # /44.3*100
 ,8.5 #/44.3*100
 , 30.8 # /44.3*100
 ], # Y
# yerr=[44,34,21,13], # Y-errors
fmt="ko-", # format line like for plot()
linewidth=2, # width of plot line
elinewidth=0.5,# width of error bar line
ecolor='k', # color of error bar
capsize=3, # cap length for error bar
capthick=0.5 # cap thickness for error bar
)
 

plt.errorbar(
[0, 2, 36], # X
[70.2 #/70.2*100
  , 42.3 # /70.2*100
  , 39.2 #/70.2*100
 ], # Y
# yerr=[44,34,21,13], # Y-errors
fmt="ko-", # format line like for plot()
linewidth=2, # width of plot line
elinewidth=0.5,# width of error bar line
ecolor='k', # color of error bar
capsize=3, # cap length for error bar
capthick=0.5 # cap thickness for error bar
)
 
 
## Settings
# plt.legend() # show figure legend
plt.ylabel('H/M ratio')
plt.xlabel('time')
plt.title('Long term follow up (3yrs, 5patients)')
# plt.xticks(np.arange(0,3), labels=['0','2','36'])
plt.xscale('symlog')
plt.yscale('linear') #Set y-axis scale
# plt.xlim((0.5,4.5)) #Set X-axis limits
# plt.ylim((0,100)) #Set Y-axis limits
# plt.xticks([1,2,3,4]) #get only ticks we want
# plt.yticks([0,5,10,15,20])
 
## showing plot
plt.show()